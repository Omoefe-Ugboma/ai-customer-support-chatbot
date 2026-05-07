from openai import OpenAI

from app.core.config import settings

from app.services.memory_service import (
    get_conversation,
    save_message,
)

from app.services.rag_service import (
    retrieve_context,
)

from app.services.analytics_service import (
    log_interaction,
)

from app.core.logger import logger

from app.utils.timer import (
    start_timer,
    end_timer,
)

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def generate_streaming_response(
    message: str,
    db,
    session_id: str,
):

    start = start_timer()

    try:

        # =========================
        # MEMORY
        # =========================
        history = get_conversation(
            db,
            session_id,
            limit=5
        )

        # =========================
        # RAG CONTEXT
        # =========================
        context = retrieve_context(
            message
        )

        # =========================
        # PROMPT
        # =========================
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a professional AI assistant. "
                    "Use provided context carefully."
                ),
            }
        ]

        # CONTEXT
        if context:

            messages.append({
                "role": "system",
                "content":
                    f"Knowledge:\n{context}"
            })

        # HISTORY
        for msg in history:

            messages.append({
                "role": msg.role,
                "content": msg.content,
            })

        # USER MESSAGE
        messages.append({
            "role": "user",
            "content": message,
        })

        # =========================
        # STREAM RESPONSE
        # =========================
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.4,
            stream=True,
        )

        full_response = ""

        for chunk in stream:

            delta = (
                chunk.choices[0]
                .delta
                .content
            )

            if delta:

                full_response += delta

                yield delta

        # =========================
        # SAVE MEMORY
        # =========================
        save_message(
            db,
            session_id,
            "user",
            message,
        )

        save_message(
            db,
            session_id,
            "assistant",
            full_response,
        )

        # =========================
        # ANALYTICS
        # =========================
        response_time = end_timer(
            start
        )

        log_interaction(
            db=db,
            user_email=session_id,
            question=message,
            response=full_response,
            response_time=response_time,
            category="chat",
        )

    except Exception as e:

        logger.error(
            f"Streaming error: {str(e)}"
        )

        yield "Something went wrong."