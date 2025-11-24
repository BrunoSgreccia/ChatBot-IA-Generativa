# vector_store.py
import pinecone
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
INDEX_NAME = os.getenv("INDEX_NAME")

model = SentenceTransformer("all-MiniLM-L6-v2")

def init_pinecone():
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    if INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(INDEX_NAME, dimension=384)
    return pinecone.Index(INDEX_NAME)

def index_documents(documents):
    index = init_pinecone()
    items = []
    for doc in documents:
        embedding = model.encode(doc["texto"]).tolist()
        items.append((doc["id"], embedding, {"text": doc["texto"]}))
    index.upsert(items)