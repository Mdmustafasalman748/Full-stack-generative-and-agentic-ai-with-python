from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()
openai_client=OpenAI()
#Vector embeddings  
emdeddings_model=OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db=QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=emdeddings_model
)

def process_query(query:str):
    print("Searching Chunks", query)
    search_results = vector_db.similarity_search(query=query)
    context = "\n\n\n".join([
        f"Page Content:{result.page_content}\n Page Number:{result.metadata['page_label']}\n File Location:{result.metadata['source']}"
        for result in search_results
    ])

    system_prompt = f"""
You are a helpful AI Assistant who answers user query based on the available content retrieved from a PDF file along with page_content and page_number.
You should only answer the user based on the following context and navigate the user to open the right page number to know more.
Context:
{context}
"""

    response = openai_client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )
    print(f"{response.choices[0].message.content}")
    return response.choices[0].message.content