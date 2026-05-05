from openai import OpenAI
from app.core.config import settings
from app.core.logger import logger
from app.services.memory_service import get_conversation, save_message
from app.services.rag_service import retrieve_context

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_chat_response(message: str, db, session_id: str):
    try:
        # 🧠 Memory
        history = get_conversation(db, session_id)

        # 🔎 RAG context
        context = retrieve_context(message)

        messages = [
            {
                "role": "system",
                "content": "You are an AI support assistant. Use provided context if relevant."
            }
        ]

        # Add retrieved knowledge
        if context:
            messages.append({
                "role": "system",
                "content": f"Relevant information:\n{context}"
            })

        # Add memory
        for msg in reversed(history):
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        # Add user message
        messages.append({
            "role": "user",
            "content": message
        })

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content

        # Save
        save_message(db, session_id, "user", message)
        save_message(db, session_id, "assistant", reply)

        return reply

    except Exception as e:
        logger.error(f"RAG error: {str(e)}")
        return "Something went wrong"