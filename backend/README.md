Alternate of openai - Ollama:

1️⃣ Install Ollama (in terminal)

Ollama is not a Python package — it runs as a local service.

👉 Download & install:
https://ollama.com

After install, verify:

ollama --version


ollama serve
ollama pull llama3
ollama pull nomic-embed-text



Steps to Run:

cd backend

python3 -m venv venv

source venv/bin/activate

Step 3: Install backend dependencies
pip install -r requirements.txt

pip install "langchain[document_loaders]" pypdf


Step 5: Ingest your resume (VERY IMPORTANT)

This step:

Reads data/resume.pdf

Creates embeddings

Saves FAISS files into vectorstore/

Run:

python3 ingest.py

python3 -m uvicorn main:app --reload

Input:

{
  "query": "What is the name/address of the person in the resume?"
}


In Render:

1. set:

LLM_MODE=demo in .env

2. Don't install ollama

