from openai import OpenAI
from app.core.config import settings
from app.core.logger import logger
from app.services.memory_service import get_conversation, save_message
from app.services.rag_service import retrieve_context
from app.services.cache_service import get_cached, set_cache

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_chat_response(message: str, db, session_id: str):
    print("\n=== DEBUG START ===")

    try:
        # 🧠 MEMORY
        history = get_conversation(db, session_id)
        print("HISTORY OK")

        # 🔎 RAG
        context = retrieve_context(message)
        print("CONTEXT:", context)

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]

        if context:
            messages.append({
                "role": "system",
                "content": f"Context:\n{context}"
            })

        for msg in reversed(history):
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        messages.append({
            "role": "user",
            "content": message
        })

        print("MESSAGES BUILT")

        # 🤖 OPENAI CALL
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        print("OPENAI RESPONSE RECEIVED")

        reply = response.choices[0].message.content

        save_message(db, session_id, "user", message)
        save_message(db, session_id, "assistant", reply)

        print("=== SUCCESS ===\n")
        return reply

    except Exception as e:
        print("❌ ERROR:", str(e))
        return f"DEBUG ERROR: {str(e)}"