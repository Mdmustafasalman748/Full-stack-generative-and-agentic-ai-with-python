from typing_extensions import TypeDict
from typing import Annotated
from langgraph.graph.message import add_message
from langgraph.graph import StateGraph
class State(TypeDict):
    messages:Annotated[list, add_message]
    
def chatbot(state:State):
    print("\n\n Inside chatbot node",state)
    return {"messages":["Hi, This is a message from chatbot node"]}

def samplenode(state:State):
    print("\n\n Inside samplenode",state)
    return {"messages":["Sample Message Appended"]}
graph_builder=StateGraph(State)
graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("samplenode",samplenode)

#state={"messages":["Hey There"]}
#node runs: chatbot(state:["Hey There"]) -> ["Hi, This is a message from chatbot node"]
#state={"messages":["Hey There","Hi, This is a message from chatbot node"]}