#Zero short prompting
from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import requests
from pydantic import BaseModel, Field
from typing import Optional
load_dotenv()
client = OpenAI()
def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"

available_tools={
    "get_weather":get_weather
}
                

#Zero shot prompting - Directly giving the instruction to the model.
SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to ve done.
The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of available tools.
for every tool call tool if required from the list of available tools
Rules:
- Strictly follow the given JSON output format.
- Only run one step at a time.
- The sequence of steps is START(where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).
OUTPUUT JSON Format:
{"step":"START"|"PLAN"|"OUTPUT"|"TOOL","content":"string","tool":"string","input":"string"}
Available tools:
+- get_weather(city:str): Takes city name as input string and returns the weather info about the city. 
Example 1:
START: Hey, can you solve 2+3*5/10
PLAN: {"step":"PLAN","content":""Seems like user is interested in math problem"}
PLAN:{"step":"PLAN","content":"looking at the problem, we should solve this using BODMAS method"}
PLAN:{"step":"PLAN","content":"Yes, The BODMAS is correct thing to be done here"}
PLAN:{"step":"PLAN","content":"first we must multiply 3*5 which is 15"}
PLAN:{"step":"PLAN","content":"Now the new equation is 2+15/10"}
PLAN:{"step":"PLAN","content":"We must perform divide that is 2+15/10=1.5"}
PLAN:{"step":"PLAN","content":"Now the new equation is 2+1.5"}
PLAN:{"step":"PLAN","content":"Now, finally lets perform the add 3.5"}
PLAN:{"step":"PLAN","content":"Great, We have solved and finally left with 3.5 as answer"}

Example 2:
START: Hey, What is the weather of Delhi?
PLAN: {"step":"PLAN","content":""Seems like user is interested in getting waether of Delhi in India"}
PLAN:{"step":"PLAN","content":"Lets see if we have any available tool from the list of available tools"}
P
+
N:{"step":"PLAN","content":"Great, we have get_weather tool available for this query."}
PLAN:{"step":"PLAN","content":"I need to call get_weather tool for delhi as input for city"}
PLAN:{"step":"TOOL":"tool":"get_weather","input":"delhi"}
PLAN:{"step":"OBSERVE":"tool":"get_weather","output":"The temp of delhi is cloudy with 20 c"}
PLAN:{"step":"PLAN","content":"Great, I got the weather info about delhi"}
OUTPUT:{"step":"OUTPUT","content":"The current weather in delhi is 20 c with same cloudy sky"}
    """
response=client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey. write a code to add n numbers in js"},
        {"role": "assistant", "content":json.dumps({"step":"START","content":"You want a JAvaScript code to add n numbers."})},
        {"role": "assistant", "content": json.dumps({"step":"PLAN","content":"I need to provide a JavaScript function that can add any number of arguments or elements in an array. I will use the rest parameter syntax (....) to accept multiple numbers and then use the 'reduce' method to sum them up."})},
        {"role": "assistant", "content": json.dumps({"step":"OUTPUT","content":"I will define a JavaScript function that accepts an arbitrary number of arguments using the rest parameter. Inside the function, I will use the 'reduce' array method to iterate over these arguments and calculate their sum. Finally, I will return the sum."})},
    ]
)
print(response.choices[0].message.content)
class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The optional tool to call")
    input: Optional[str] = Field(None, description="The input params for the tool")

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

user_query = input("👉 ")

message_history.append(
    {
        "role": "user",
        "content": user_query
    }
)

while True:

    response = client.chat.completions.parse(
        model="gpt-4o-mini",
        response_format=MyOutputFormat,
        temperature=0,
        messages=message_history
    )

    raw_result = response.choices[0].message.content

    message_history.append(
        {
            "role": "assistant",
            "content": raw_result
        }
    )

    parsed_result = response.choices[0].message.parsed

    if parsed_result.step == "START":
        print("🔥", parsed_result.content)
        continue
    
    if parsed_result.step == "TOOL":
        tool_to_call = parsed_result.tool
        tool_input=parsed_result.input
        print({tool_to_call,tool_input})
        tool_response=available_tools[tool_to_call](tool_input)
        message_history.append(
        {"role":"developer","content":json.dumps(
         {"step":"OBSERVE","tool":tool_to_call,"input":tool_input,"output":tool_response})
         }
        )
        continue
    if parsed_result.step == "PLAN":
        print("🧠", parsed_result.content)
        continue

    if parsed_result.step == "OUTPUT":
        print("🤖", parsed_result.content)
        break

print("\n\n\n")
    
    