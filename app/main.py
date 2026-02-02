import uuid
from langchain_core.messages import HumanMessage
from app.graph.final_graph import final_graph
from app.config.langsmith_config import setup_langsmith

setup_langsmith()


def main():
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    question = input("Ask: ")

    result = final_graph.invoke(
        {"messages": [HumanMessage(content=question)]},
        config=config
    )

    for msg in result["messages"]:
        print(msg.content)


if __name__ == "__main__":
    main()
