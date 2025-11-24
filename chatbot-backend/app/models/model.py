from pydantic import BaseModel

class Pergunta(BaseModel):
    mensagem: str
    assistent: int