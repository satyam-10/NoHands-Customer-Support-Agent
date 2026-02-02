from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import SystemMessage
from app.tools.music_tools import music_tools
from app.llm.models import llm
from app.prompts.music_prompts import generate_music_prompt
from app.memory.stores import checkpointer, long_term_store

llm_tools = llm.bind_tools(music_tools)
tool_node = ToolNode(music_tools)

def music_assistant(state, config):
    prompt = generate_music_prompt()
    response = llm_tools.invoke([SystemMessage(prompt)] + state["messages"])
    return {"messages": [response]}

def should_continue(state, config):
    if not state["messages"][-1].tool_calls:
        return "end"
    return "continue"

workflow = StateGraph(dict)
workflow.add_node("assistant", music_assistant)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "assistant")
workflow.add_conditional_edges("assistant", should_continue, {
    "continue": "tools",
    "end": END
})
workflow.add_edge("tools", "assistant")

music_agent = workflow.compile(
    checkpointer=checkpointer,
    store=long_term_store
)
