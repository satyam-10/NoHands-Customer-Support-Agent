from langgraph.graph import StateGraph, START, END
from app.agents.supervisor import supervisor
from app.graph.state import State

graph = StateGraph(State)
graph.add_node("supervisor", supervisor)
graph.add_edge(START, "supervisor")
graph.add_edge("supervisor", END)

final_graph = graph.compile()

