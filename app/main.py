print("RUNNING THIS MAIN FILE again")

import uuid
from langchain_core.messages import HumanMessage
from app.graph.final_graph import build_final_graph
from app.config.langsmith_config import setup_langsmith

setup_langsmith()

def main():
    # Build graph once
    graph = build_final_graph()

    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    question = input("Ask: ")

    result = graph.invoke(
        {"messages": [HumanMessage(content=question)]},
        config=config
    )

    for msg in result["messages"]:
        print(msg.content)


if __name__ == "__main__":
    main()
