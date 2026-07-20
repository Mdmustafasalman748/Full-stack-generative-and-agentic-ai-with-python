#Zero short prompting
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
#Zero shot prompting - Directly giving the instruction to the model.
SYSTEM_PROMPT="""You shhould only and only answer the coding related questions. Do not answer anything else. Your name is Alexa. If user asks something else other than coding, just say sorry
Examples:
Q.Can you explain the a+b whole square?
A. Sorry, I can only answer coding related questions.
Q. Can you write a python code for adding two numbers?
A. def add(a,b): 
    return a+b
    """
response=client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you write a python code to translate the word hello?"},
    ]
)
print(response.choices[0].message.content)
#Few shot prompting: The model is provided wiht a few examples before asking it to generate a response.