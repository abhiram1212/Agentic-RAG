from fastapi import FastAPI
from pydantic import BaseModel
import app.agent as agent

app = FastAPI()

class AskRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return{"status":"ok"}

@app.get("/")
def project_message():
    return{"message": "Agentic RAG Gmail API"}

@app.post("/ask")
def question(request:AskRequest):
    return{"answer":agent.process_question(request.question)}