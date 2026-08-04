from typing_extensions import TypeDict
from typing import Annotated
from langgraph.graph.message import add_message
from langgraph.graph import StateGraph
class State(TypeDict):
    messages:Annotated[list, add_message]
graph_builder=StateGraph(State)