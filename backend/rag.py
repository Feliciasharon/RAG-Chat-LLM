'''from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Load env vars (still useful later)
load_dotenv()

# -----------------------------
# Embeddings (mock for dev)
# -----------------------------
#from mock_embeddings import FakeEmbeddings
#embeddings = FakeEmbeddings()

from langchain_ollama import OllamaEmbeddings

def get_embeddings():
    return OllamaEmbeddings(
        model="nomic-embed-text"
    )
embeddings = get_embeddings()
# -----------------------------
# Load FAISS vectorstore
# -----------------------------
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# -----------------------------
# Local LLM via Ollama
# -----------------------------
llm = ChatOllama(
    model="llama3",
    temperature=0
)

# -----------------------------
# Prompt Template
# -----------------------------
PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are answering questions strictly using the resume content below.

Rules:
- Use ONLY the resume information.
- If the answer is not present, say: "Not mentioned in the resume."
- Be concise and factual.

Resume:
{context}

Question:
{question}

Answer:
"""
)

# -----------------------------
# RAG function
# -----------------------------
def ask_question(question: str):
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    response = llm.invoke(
        PROMPT.format(context=context, question=question)
    )

    return {
        "answer": response.content,
        "sources": [doc.metadata.get("page", "unknown") for doc in docs]
    }
'''


import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()

LLM_MODE = os.getenv("LLM_MODE", "dev")

# -----------------------------
# LOCAL MODE — Ollama
# -----------------------------
if LLM_MODE == "local":
    
    # -----------------------------
    # Embeddings
    # -----------------------------
    from langchain_ollama import OllamaEmbeddings
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template="""
    You are answering questions strictly using the resume content below.
    
    Resume:
    {context}
    
    Question:
    {question}
    
    Answer:
    """
    )
    

    from langchain_ollama import ChatOllama
    llm = ChatOllama(model="llama3", temperature=0)

# -----------------------------
# DEMO MODE — Safe fallback
# -----------------------------
def demo_llm_answer():
    return "This is a demo deployment. Please run the app locally to see full AI-powered responses."

# -----------------------------
# RAG function
# -----------------------------
def ask_question(question: str):

    if LLM_MODE == "local":
        docs = retriever.invoke(question)
        context = "\n\n".join(d.page_content for d in docs)
        response = llm.invoke(
            PROMPT.format(context=context, question=question)
        )
        answer = response.content
        
        return {
            "answer": answer,
            "sources": [d.metadata.get("page", "unknown") for d in docs]
        }
    
    else:
        answer = demo_llm_answer()

        return {
            "answer": answer
        }
