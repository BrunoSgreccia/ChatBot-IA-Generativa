# retriever.py
from sentence_transformers import SentenceTransformer
import pinecone
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
INDEX_NAME = os.getenv("INDEX_NAME")

model = SentenceTransformer("all-MiniLM-L6-v2")

def buscar_contexto(query, top_k=3):
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    index = pinecone.Index(INDEX_NAME)
    query_embedding = model.encode(query).tolist()
    resultado = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
    return [match["metadata"]["text"] for match in resultado["matches"]]