<<<<<<< HEAD
from typing import TypedDict, List
from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    messages: List[BaseMessage]
=======
from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class State(TypedDict):
    messages: List[BaseMessage]
>>>>>>> bdd219cdf7302f4a8d9ee76a963009770dc3d161
