from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # =========================
    # 🔑 OPENAI
    # =========================
    OPENAI_API_KEY: str

    # =========================
    # 🗄️ DATABASE
    # =========================
    DATABASE_URL: str

    # =========================
    # 🔐 JWT
    # =========================
    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    # =========================
    # ⚙️ APP
    # =========================
    APP_NAME: str = "AI Chatbot"

    DEBUG: bool = True

    # =========================
    # ⚡ CACHE
    # =========================
    REDIS_HOST: str = "localhost"

    REDIS_PORT: int = 6379

    # =========================
    # 📦 VECTOR DB
    # =========================
    PINECONE_API_KEY: str = ""

    PINECONE_INDEX_NAME: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()