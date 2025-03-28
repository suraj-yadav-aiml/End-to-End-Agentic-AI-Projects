from typing_extensions import TypedDict
from typing import List, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]