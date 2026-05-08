from openai import OpenAI
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logger import logger

from app.services.memory_service import (
    get_conversation,
    save_message
)

from app.services.rag_service import retrieve_context

from app.services.analytics_service import log_interaction

from app.services.cache_service import (
    get_cached,
    set_cache
)

from app.utils.timer import (
    start_timer,
    end_timer
)


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


# =========================
# 💬 CHAT RESPONSE
# =========================
def generate_chat_response(
    message: str,
    db: Session,
    thread_id: str
):

    start = start_timer()

    try:

        # =========================
        # ⚡ CACHE
        # =========================
        cached_response = get_cached(
            thread_id,
            message
        )

        if cached_response:
            logger.info("⚡ Cache hit")

            return cached_response

        # =========================
        # 🧠 MEMORY
        # =========================
        history = get_conversation(
            db,
            thread_id,
            limit=5
        )

        # =========================
        # 🔎 RAG
        # =========================
        context = retrieve_context(message)

        # =========================
        # 🧠 PROMPT
        # =========================
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a professional AI assistant.\n"
                    "Answer ONLY using the provided context.\n"
                    "If answer is unavailable, say:\n"
                    "'I don't know based on the provided data.'"
                )
            }
        ]

        # CONTEXT
        if context:
            messages.append({
                "role": "system",
                "content": f"Context:\n{context}"
            })

        # MEMORY
        for msg in history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        # USER
        messages.append({
            "role": "user",
            "content": message
        })

        # =========================
        # 🤖 OPENAI
        # =========================
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3
        )

        reply = response.choices[0].message.content

        # =========================
        # ⏱️ PERFORMANCE
        # =========================
        response_time = end_timer(start)

        # =========================
        # 💾 SAVE MEMORY
        # =========================
        save_message(
            db,
            thread_id,
            "user",
            message
        )

        save_message(
            db,
            thread_id,
            "assistant",
            reply
        )

        # =========================
        # 📊 ANALYTICS
        # =========================
        log_interaction(
            db=db,
            user_email=thread_id,
            question=message,
            response=reply,
            response_time=response_time,
            category="general"
        )

        # =========================
        # ⚡ CACHE SAVE
        # =========================
        set_cache(
            thread_id,
            message,
            reply
        )

        return reply

    except Exception as e:

        logger.error(
            f"❌ Chat error: {str(e)}"
        )

        return "Something went wrong"