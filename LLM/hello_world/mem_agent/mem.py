from dotenv import load_dotenv
from openai import OpenAI
from mem0 import Memory
import os 

load_dotenv()
client = OpenAI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
config={
    "version":"v1.1",
    "embedder":{
        "provider":"openai",
        "config":{"api_key": OPENAI_API_KEY, "model":"text-embedding-3-small"}
    },
    "llm":{
        "provider":"openai",
        "config":{"api_key": OPENAI_API_KEY, "model":"gpt-4.1"}
    },
    "vector_store":{
        "provider":"qdrant",
        "config":{
            "host":"localhost",
            "port":6333,
        }
    }
}
mem_client=Memory.from_config(config)
while(True):
    user_query=input(">")
    response=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user","content":user_query}
        ]
    )
    ai_response=response.choices[0].message.content
    print(f"AI: {ai_response}")
    mem_client.add(user_id="MS",
                   messages=[
                       {"role":"user","content":user_query},
                       {"role":"assistant","content":ai_response}  
                   ]
    )
    print("Memory has been saved...")
    