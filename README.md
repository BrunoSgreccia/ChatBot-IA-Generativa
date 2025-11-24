# Guia de Execução do Projeto ChatBot IA Groq

Este projeto é composto por duas aplicações independentes:
- **Backend (FastAPI)**: Responsável pela API e integração com a IA Groq.
- **Frontend (React)**: Interface web de chat para interação com o bot.

---

## 1. Como rodar o Backend (FastAPI)

1. Abra o terminal na raiz do projeto (onde está o arquivo `requirements.txt`).
2. Crie o ambiente virtual do Python:
   ```powershell
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - No **PowerShell**:
     ```powershell
     .\venv\Scripts\Activate
     ```
   - No **cmd**:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - No **bash (Git Bash/MINGW64)**:
     ```bash
     source venv/Scripts/activate
     ```
4. Instale as dependências do Python:
   ```powershell
   pip install -r requirements.txt
   ```
5. Certifique-se de que o arquivo `.env` contém sua chave da Groq:
   ```env
   GROQ_API_KEY=sua-chave-groq-aqui
   ```
6. Execute o backend:
   ```bash
   cd app
   uvicorn main:app --reload
   ```
   O backend estará disponível em: http://localhost:8000

---

## 2. Como rodar o Frontend (React)

1. Abra outro terminal e navegue até a pasta do frontend:
   ```bash
   cd chatbot-frontend
   ```
2. Instale as dependências do Node.js:
   ```bash
   npm install --legacy-peer-deps
   ```
3. Inicie o frontend:
   ```bash
   npm start
   ```
   O frontend estará disponível em: http://localhost:3000

---

## Observações
- O backend precisa estar rodando antes do frontend para que o chat funcione corretamente.
- Se precisar alterar a porta ou o endereço, ajuste as URLs no frontend (`App.js`) e nas configurações de CORS do backend (`main.py`).
- Para dúvidas ou problemas, consulte os arquivos de código ou peça ajuda ao assistente!
