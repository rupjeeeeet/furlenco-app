import { useState } from "react";

export default function Chat() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);

  async function sendMessage() {
    if (!query.trim()) return;

    const userMsg = { role: "user", text: query };
    setMessages((prev) => [...prev, userMsg]);
    setQuery("");

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      const botMsg = { role: "bot", text: data.answer || "No answer." };

      setMessages((prev) => [...prev, botMsg]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "⚠️ Error contacting assistant." },
      ]);
    }
  }

  return (
    <div>

      {/* Inline CSS */}
      <style>{`
        .chat-page {
          max-width: 850px;
          margin: 40px auto;
          padding: 20px;
          color: #fff;
          font-family: 'Inter', sans-serif;
        }

        .chat-title {
          font-size: 24px;
          margin-bottom: 20px;
          font-weight: 600;
          text-align: center;
        }

        .chat-box {
          background: #1e1e1e;
          padding: 20px;
          border-radius: 14px;
          height: 420px;
          overflow-y: auto;
          border: 1px solid #333;
          display: flex;
          flex-direction: column;
          gap: 14px;
        }

        .msg {
          max-width: 75%;
          padding: 12px 16px;
          border-radius: 14px;
          font-size: 15px;
          line-height: 1.5;
        }

        .user {
          align-self: flex-end;
          background: #4f46e5;
          color: white;
          border-radius: 14px 14px 0px 14px;
        }

        .bot {
          align-self: flex-start;
          background: #2d2d2d;
          color: #e5e5e5;
          border: 1px solid #3a3a3a;
          border-radius: 14px 14px 14px 0px;
        }

        .chat-input-area {
          margin-top: 20px;
          display: flex;
          gap: 10px;
        }

        .chat-input-area input {
          flex: 1;
          padding: 12px;
          border-radius: 8px;
          outline: none;
          background: #111;
          color: white;
          border: 1px solid #333;
          font-size: 15px;
        }

        .chat-input-area button {
          padding: 12px 20px;
          background: #6366f1;
          border: none;
          color: white;
          border-radius: 8px;
          cursor: pointer;
          font-size: 15px;
          transition: 0.2s;
        }

        .chat-input-area button:hover {
          background: #4f46e5;
        }
      `}</style>

      <div className="chat-page">
        <h2 className="chat-title">AI Shopping Assistant 🤖</h2>

        <div className="chat-box">
          {messages.map((msg, i) => (
            <div key={i} className={`msg ${msg.role}`}>
              {msg.text}
            </div>
          ))}
        </div>

        <div className="chat-input-area">
          <input
            type="text"
            placeholder="Ask something..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}
