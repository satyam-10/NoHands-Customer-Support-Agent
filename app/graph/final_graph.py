from langgraph.graph import StateGraph, START, END
from app.agents.supervisor import supervisor
from app.graph.state import State

def build_final_graph():
    graph = StateGraph(State)

    graph.add_node("supervisor", supervisor)
    graph.add_edge(START, "supervisor")
    graph.add_edge("supervisor", END)

    return graph.compile()

