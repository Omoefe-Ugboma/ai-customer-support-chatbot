from openai import OpenAI
from app.core.config import settings
from app.core.logger import logger
from app.services.memory_service import get_conversation, save_message

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_chat_response(message: str, db, session_id: str):
    try:
        # 🧠 Get memory
        history = get_conversation(db, session_id)

        messages = [
            {
                "role": "system",
                "content": "You are a professional AI support assistant."
            }
        ]

        # Add history
        for msg in reversed(history):
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        # Add new message
        messages.append({
            "role": "user",
            "content": message
        })

        # 🔥 Call LLM
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content

        # 💾 Save conversation
        save_message(db, session_id, "user", message)
        save_message(db, session_id, "assistant", reply)

        return reply

    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return "Something went wrong"