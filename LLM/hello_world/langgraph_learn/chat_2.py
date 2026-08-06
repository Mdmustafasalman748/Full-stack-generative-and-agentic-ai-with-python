from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph,START,END
from openai import OpenAI
load_dotenv()
client = OpenAI()
class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state:State):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role":"user","content":State.get("user_query")
            }
        ]
    )
    State["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state:State)-> Literal["chatbot_gemini","endnode"]:
    if True:
        return "endnode"
    return "chatbot_gemini"

def chatbot_gemini(state:State):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role":"user","content":State.get("user_query")
            }
        ]
    )
    State["llm_output"] = response.choices[0].message.content
    return state

    def endnode(state:State):
        print("\n\n Inside endnode",state)
        return state
    
    graph_builder.add_node("chatbot",chatbot)
    graph_builder.add_node("chatbot_gemini",chatbot_gemini)
    graph_builder.add_node("endnode",endnode)

    graph_builder.add_edge(START,"chatbot")
    graph_builder.add_edge("chatbot","chatbot_gemini")
    graph_builder.add_edge("chatbot_gemini","endnode")
    graph_builder.add_edge("endnode",END)
    graph_builder.add_conditional_edge("chatbot","endnode",evaluate_response)
    graph_builder.add_edge("chatbot_gemini","endnode")
    graph_builder.add_edge("endnode",END)
    graph=graph_builder.compile()

    updated_state=graph.invoke(State({"user_query":"Hey, what is 2+2"}))
    print("\n\n Updated_state", updated_state)      