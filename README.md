
# ResumeGPT: AI-Powered Resume Assistant using RAG + LLM

ResumeGPT is a full-stack Retrieval-Augmented Generation (RAG) application that allows users to ask natural language questions about a resume PDF.

It combines:

🔎 FAISS vector search

🧠 LangChain RAG pipeline

🦙 Ollama (LLaMA 3) for local LLM inference

⚡ FastAPI backend

🎨 React + Tailwind frontend

☁️ Hybrid deployment (Render + Vercel)


## Architecture

**Frontend (React + Tailwind)** → Vercel

**Backend (FastAPI + FAISS)** → Render

**LLM (Ollama LLaMA 3)** → Local Machine


**Modes:**

local → Full RAG + Ollama

demo → Cloud-safe deployment mode


## Setup — Run Locally (Full AI Mode)

**1️⃣ Install Ollama**

Download from:

https://ollama.com

Then pull required models:

```
ollama pull llama3

ollama pull nomic-embed-text
```


Start Ollama:

```
ollama serve
```

**2️⃣ Backend Setup**

```
cd backend

python -m venv venv

source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt #include langchain-ollama
``` 


Create .env file:

```
LLM_MODE=local
```

**3️⃣ Ingest Resume**

Place your resume PDF inside:

```
backend/data/
```


Then run:

```
python ingest.py
```


This will:

Load the PDF

Split into chunks

Generate embeddings

Store FAISS index locally

**4️⃣ Start Backend**
```
python3 -m uvicorn main:app --reload
```

Backend runs on:

http://127.0.0.1:8000

**5️⃣ Frontend Setup**

```
cd frontend
npm install
```

Change in `src/api.ts`:

```
const API_URL = "http://127.0.0.1:8000";
```


Start frontend:
```
npm run dev
```

App runs on:

http://localhost:5173


## Setup — Dev Deployment (Hybrid Mode)

### Backend → Render

Push backend to GitHub

Create Web Service on Render

Root directory → backend

**Build command:**
```
pip install -r requirements.txt
```

**Start command:**
```
uvicorn main:app --host 0.0.0.0 --port 10000
```

**Add environment variable:**
```
LLM_MODE=demo
```

**Copy Render URL:**

https://rag-chat-llm.onrender.com


### Frontend → Vercel

Import frontend repo into Vercel

Change in `src/api.ts`:

```
const API_URL = "https://rag-chat-llm.onrender.com";
```

Deploy

**Update CORS in backend/main.py to allow incoming requests from Vercel**

Update:

```
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # local
    allow_methods=["*"],
    allow_headers=["*"],
)
```

to

```
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://rag-chat-llm.vercel.app"],  # replace with Vercel URL
    allow_methods=["*"],
    allow_headers=["*"],
)
```



**Deployments:**

Vercel (Frontend) - https://rag-chat-llm.vercel.app

Render (Backend) - https://rag-chat-llm.onrender.com
