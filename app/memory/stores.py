from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = MemorySaver()
long_term_store = InMemoryStore()