from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """
You're an expert AI Assistant.

You work on START, PLAN and OUTPUT steps.

Your job is:
1. START - Understand the user's request.
2. PLAN - Create a short plan. PLAN can happen multiple times.
3. OUTPUT - Give the final answer.

Rules:
- Return ONLY valid JSON.
- Return ONLY ONE JSON object per response.
- Never return multiple JSON objects together.
- Do not add markdown.
- Do not add explanations outside JSON.

JSON Format:

{
    "step": "START",
    "content": "string"
}

OR

{
    "step": "PLAN",
    "content": "string"
}

OR

{
    "step": "OUTPUT",
    "content": "string"
}

Example:

User:
Solve 2+3*5/10

Assistant:

{
    "step":"START",
    "content":"User wants to solve a math problem"
}

Assistant:

{
    "step":"PLAN",
    "content":"Apply BODMAS rules to solve the expression"
}

Assistant:

{
    "step":"PLAN",
    "content":"First calculate multiplication: 3*5 = 15"
}

Assistant:

{
    "step":"OUTPUT",
    "content":"The final answer is 3.5"
}
"""

print("\n\n\n")

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={
            "type": "json_object"
        },
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

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n\n")