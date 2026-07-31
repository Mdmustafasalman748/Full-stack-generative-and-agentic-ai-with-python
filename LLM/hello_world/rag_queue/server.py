from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query
from dotenv import load_dotenv
load_dotenv()
app=FastAPI()
@app.get("/")
def root():
    return {"Status":'Server is up and running'}
@app.post("/chat")
def chat(
    query:str=Query(...,description="The chat query of user")
):
    job=queue.enqueue_call(process_query,query)
    return {"Status":"Queued","job_id":job.id}
