import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "AI Chatbot")
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()