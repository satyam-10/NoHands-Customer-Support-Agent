from langgraph.prebuilt import create_react_agent
from app.llm.models import llm
from app.tools.invoice_tools import invoice_tools
from app.memory.stores import checkpointer, long_term_store

invoice_agent = create_react_agent(
    llm,
    tools=invoice_tools,
    name="invoice_agent",
    checkpointer=checkpointer,
    store=long_term_store
)
