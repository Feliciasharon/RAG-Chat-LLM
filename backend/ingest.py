'''from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()

def ingest():
    loader = PyPDFLoader("data/Resume_FeliciaSharon.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = splitter.split_documents(documents)

    #embeddings = OpenAIEmbeddings()
    from mock_embeddings import FakeEmbeddings
    embeddings = FakeEmbeddings()

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("vectorstore")

    print("✅ Resume embedded successfully")

if __name__ == "__main__":
    ingest()
'''

'''from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

def ingest():
    loader = PyPDFLoader("resume.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("faiss_index")

    print("✅ Resume embedded successfully")

if __name__ == "__main__":
    ingest()
'''


from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

load_dotenv()

def ingest():
    loader = PyPDFLoader("data/Resume_FeliciaSharon.pdf")
    documents = loader.load()

    for doc in documents[:1]:
      print("RAW PDF TEXT:\n", doc.page_content[:500])

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = splitter.split_documents(documents)

    # Mock embeddings to avoid OpenAI + tiktoken issues
    '''from mock_embeddings import FakeEmbeddings
    embeddings = FakeEmbeddings()'''

    from langchain_ollama import OllamaEmbeddings
    
    def get_embeddings():
        return OllamaEmbeddings(
            model="nomic-embed-text"
        )
    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("vectorstore")

    print("✅ Resume embedded successfully")

if __name__ == "__main__":
    ingest()
