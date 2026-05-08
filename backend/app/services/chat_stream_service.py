from openai import OpenAI
import time
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

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def generate_streaming_response(
    message: str,
    db,
    thread_id: int,
    user_email: str,
):

    try:
        start_time = time.time()
        # =========================
        # MEMORY
        # =========================
        history = get_conversation(
            db,
            thread_id,
            limit=5,
        )

        # =========================
        # RAG CONTEXT
        # =========================
        context = retrieve_context(
            message
        )

        messages = [

            {
                "role": "system",

                "content":
                (
                    "You are a smart AI assistant.\n"
                    "Use the provided context "
                    "to answer accurately.\n"
                    "If context contains the answer,"
                    " prioritize it.\n"
                ),
            }
        ]

        # =========================
        # ADD CONTEXT
        # =========================
        if context:

            messages.append({

                "role": "system",

                "content":
                f"Context:\n{context}",
            })

        # =========================
        # HISTORY
        # =========================
        for msg in history:

            messages.append({

                "role": msg.role,

                "content": msg.content,
            })

        # =========================
        # USER MESSAGE
        # =========================
        messages.append({

            "role": "user",

            "content": message,
        })

        # =========================
        # SAVE USER MESSAGE
        # =========================
        save_message(
            db,
            thread_id,
            "user",
            message,
        )

        # =========================
        # OPENAI STREAM
        # =========================
        stream = client.chat.completions.create(

            model="gpt-4o-mini",

            messages=messages,

            temperature=0.3,

            stream=True,
        )

        full_response = ""

        for chunk in stream:

            delta = (
                chunk.choices[0]
                .delta.content
            )

            if delta:

                full_response += delta

                yield delta

        # =========================
        # SAVE AI RESPONSE
        # =========================
        save_message(
            db,
            thread_id,
            "assistant",
            full_response,
        )

        # =========================
        # ANALYTICS
        # =========================
        log_interaction(

            db=db,

            user_email=user_email,

            question=message,

            response=full_response,

             response_time=(
                time.time() - start_time
            ),

            category="chat",
        )

    except Exception as e:

        print(
            f"Streaming error: {str(e)}"
        )

        return