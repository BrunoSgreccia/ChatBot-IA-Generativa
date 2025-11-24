"""
Exemplos e dicas de arquitetura de prompt para Groq LLM
"""

# 1. Prompt Simples (Assistente Geral)
SIMPLE_ASSISTANT = [
    ("system", "Você é um assistente de IA. Responda de forma clara e objetiva."),
    ("user", "{input}")
]

# 2. Prompt Estruturado (Extração de Dados)
PRODUCT_EXTRACTION = [
    ("system", "Extraia os detalhes do produto em JSON: { 'name': string, 'price': number, 'features': [string] }"),
    ("user", "{input}")
]

# 3. Prompt com Persona
PERSONA_ASSISTANT = [
    ("system", "Você é um atendente virtual simpático e informal. Sempre cumprimente o usuário pelo nome."),
    ("user", "{input}")
]

# 4. Prompt para Respostas Curtas
SHORT_ANSWER = [
    ("system", "Responda em no máximo 2 frases."),
    ("user", "{input}")
]

# Dicas de boas práticas:
# - Seja explícito sobre o formato da resposta desejada.
# - Use instruções claras no papel do 'system'.
# - Adapte o prompt ao contexto do seu negócio.
# - Teste diferentes variações para encontrar o melhor resultado.
