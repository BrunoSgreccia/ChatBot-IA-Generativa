from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from prompts.prompt_examples import SIMPLE_ASSISTANT
from prompts.prompt_examples import SHORT_ANSWER
from prompts.prompt_examples import PRODUCT_EXTRACTION
from prompts.prompt_examples import PERSONA_ASSISTANT
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

def get_groq_response(user_message: str, asistent: int) -> dict:

    assitent = get_status(asistent)
    
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.7,
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_messages(assitent)

    chain = prompt | llm
    result = chain.invoke({"input": user_message})

    # Se for um objeto com atributo 'content', retorna apenas o texto
    if hasattr(result, "content"):
        return result.content
    
    # Se for dict, tenta extrair o campo 'content'
    if isinstance(result, dict) and "content" in result:
        return result["content"]
    
    return str(result)

def get_status(code: int) -> str:
    switch_map = {
        0: SIMPLE_ASSISTANT,
        1: SHORT_ANSWER,
        2: PRODUCT_EXTRACTION,
        3: PERSONA_ASSISTANT,
    }
    return switch_map.get(code, "Unknown")
