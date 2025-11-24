from fastapi import FastAPI
import sys
import os
from fastapi.middleware.cors import CORSMiddleware
from services.retriever import buscar_contexto  
from services.vector_store import index_documents  

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models.model import Pergunta
from services.groq_service import get_groq_response

app = FastAPI()

# Configuração de CORS para permitir o frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/chat")
def responder(pergunta: Pergunta) :
    # 1. Buscar contexto no banco vetorial
    contexto = buscar_contexto(pergunta.mensagem)

    # 2. Montar prompt com contexto + pergunta
    prompt = f"""
    Contexto recuperado:
    {contexto}

    Pergunta do usuário:
    {pergunta.mensagem}
    """

    # 3. Chamar Groq para gerar resposta
    resposta = get_groq_response(prompt, pergunta.assistent)
    return {"resposta": resposta}

@app.post("/indexdocs")
def indexar_docs(docs: list[dict]):
    """
    Espera uma lista de documentos no formato:
    [{"id": "doc1", "texto": "conteúdo aqui"}, ...]
    """
    index_documents(docs)
    return {"status": "Documentos indexados com sucesso"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

