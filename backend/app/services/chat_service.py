from openai import OpenAI
from app.core.config import settings
from app.core.logger import logger

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_chat_response(message: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional AI customer support assistant. Be clear, polite, and helpful."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content

        return reply

    except Exception as e:
        logger.error(f"OpenAI error: {str(e)}")
        return "Sorry, something went wrong. Please try again later."