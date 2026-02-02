from langgraph_supervisor import create_supervisor
from app.agents.music_agent import music_agent
from app.agents.invoice_agent import invoice_agent
from app.llm.models import llm

supervisor = create_supervisor(
    agents=[music_agent, invoice_agent],
    model=llm
)

