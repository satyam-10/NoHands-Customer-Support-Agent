import os
from app.config.settings import settings

def setup_langsmith():
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_API_KEY"] = settings.LANGSMITH_API_KEY
    os.environ["LANGSMITH_PROJECT"] = "NoHands-Customer-Support"
