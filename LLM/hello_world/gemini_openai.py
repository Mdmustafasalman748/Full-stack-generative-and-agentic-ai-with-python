import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(model="gemini-3.5-flash", messages=[{"role": "system","content": "You are an expert in Maths and only and only answer maths related questions. That if the query is not related to maths. Just say sorry and do not answer that"},
                                                                              {"role": "user", "content": "Hey, can you help me solve tha a+b whole square"}])
print(response.choices[0].message.content)
