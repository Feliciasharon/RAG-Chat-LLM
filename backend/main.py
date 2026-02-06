from fastapi import FastAPI
from pydantic import BaseModel
from rag import ask_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://rag-chat-llm.vercel.app"],  # replace later with Vercel URL or '*' in local
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    query: str

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: Question):
    return ask_question(q.query)
