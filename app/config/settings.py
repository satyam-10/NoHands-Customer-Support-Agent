import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT")

    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
    EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")

    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
