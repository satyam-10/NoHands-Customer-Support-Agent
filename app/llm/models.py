from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.config.settings import settings

llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_ENDPOINT,
    model=settings.MODEL_NAME,
    temperature=0
)

embedding_model = OpenAIEmbeddings(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_ENDPOINT,
    model=settings.EMBED_MODEL
)

print("OPENAI KEY:", settings.OPENAI_API_KEY)