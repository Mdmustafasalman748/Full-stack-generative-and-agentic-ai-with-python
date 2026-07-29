from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
load_dotenv()
openai_client = OpenAI()

#Vector embeddings
embeddings_model=OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db=QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embeddings_model
)

#Take user input
user_query=input("Ask something: ")
#Relevant chunks from the vector db
search_results=vector_db.similarity_search(query=user_query)
context="\n\n\n".join([f"Page Content:{result.page_content}\n Page Number:{result.metadata['page_label']}\n File Location:{result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT=f"""
You are a helpful AI Assistant who answers user query based on the available content retrieved from a PDF file along with page_content and page_number.
You should only answer the user absed on the following context and navigate the user to open the right page number to know more
Context:
{context}
"""
response=openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ]
)
print(response.choices[0].message.content)