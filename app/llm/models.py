from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.config.settings import OPENAI_API_KEY, OPENAI_ENDPOINT, MODEL_NAME, EMBED_MODEL

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_ENDPOINT,
    model=MODEL_NAME,
    temperature=0
)

embedding_model = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_ENDPOINT,
    model=EMBED_MODEL
)