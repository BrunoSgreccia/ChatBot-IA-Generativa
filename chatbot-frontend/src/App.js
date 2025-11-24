import React, { useState } from "react";
import logo from './logo.svg';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    { sender: "bot", text: "Olá! Como posso ajudar você hoje?" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [assistent, setAssistent] = useState([
    {
      AssitenteSimples: 0,
      AssitenteExtracao: 1,
      AssistentePessoal: 2,
      AssistenteCurto: 3
    }
  ]);
  const [selectedAssistent, setSelectedAssistent] = useState(0);

  const sendMessage = async (e) => {
    e.preventDefault();

    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };

    setMessages((msgs) => [...msgs, userMsg]);
    setLoading(true);
    setInput("");

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensagem: input, assistent:selectedAssistent })
      });
      const data = await res.json();
      setMessages((msgs) => [...msgs, { sender: "bot", text: data.resposta }]);
    } catch (err) {
      setMessages((msgs) => [...msgs, { sender: "bot", text: "Erro ao conectar ao backend." }]);
    }
    setLoading(false);
  };

  return (
    <div className="chat-container">
      <div className="combo-box">
          <select   
            value={selectedAssistent}
            onChange={(e) => setSelectedAssistent(Number(e.target.value))}
          >
          {Object.entries(assistent[0]).map(([key, value]) => (
            <option key={value} value={value}>
              {key}
            </option>
          ))}
        </select>
      </div>
      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={msg.sender === "user" ? "user-msg" : "bot-msg"}>
            <b>{msg.sender === "user" ? "Você" : "Bot"}:</b> {msg.text}
          </div>
        ))}
        {loading && <div className="bot-msg">Bot: ...</div>}
      </div>
      <form className="chat-form" onSubmit={sendMessage}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Digite sua mensagem..."
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>Enviar</button>
      </form>
    </div>
  );
}

export default App;