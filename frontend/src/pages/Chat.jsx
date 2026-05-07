import { useState } from "react";

import Layout from "../components/Layout";

import { sendMessage } from "../services/chatService";

export default function Chat() {

  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const handleSend = async () => {

    if (!message.trim()) return;

    const userMessage = {
      role: "user",
      content: message,
    };

    setMessages((prev) => [
      ...prev,
      userMessage,
    ]);

    setLoading(true);

    try {

      const response =
        await sendMessage(message);

      const aiMessage = {
        role: "assistant",
        content: response.reply,
      };

      setMessages((prev) => [
        ...prev,
        aiMessage,
      ]);

    } catch (error) {

      console.error(error);

      alert("Chat failed");

    } finally {

      setLoading(false);

    }

    setMessage("");

  };

  return (
    <Layout>

      <div className="flex flex-col h-full">

        <div className="mb-6">

          <h1 className="text-4xl font-bold">
            AI Chat
          </h1>

          <p className="text-slate-400 mt-2">
            Ask your AI assistant anything.
          </p>

        </div>

        {/* CHAT AREA */}
        <div className="flex-1 bg-slate-900 rounded-2xl border border-slate-800 p-6 overflow-y-auto space-y-4">

          {messages.length === 0 && (

            <div className="text-slate-500">
              No messages yet.
            </div>

          )}

          {messages.map((msg, index) => (

            <div
              key={index}
              className={`max-w-[75%] p-4 rounded-2xl ${
                msg.role === "user"
                  ? "bg-blue-600 ml-auto"
                  : "bg-slate-800"
              }`}
            >
              {msg.content}
            </div>

          ))}

          {loading && (
            <div className="text-slate-400">
              AI is thinking...
            </div>
          )}

        </div>

        {/* INPUT */}
        <div className="mt-4 flex gap-3">

          <input
            type="text"
            value={message}
            onChange={(e) =>
              setMessage(e.target.value)
            }
            placeholder="Type your message..."
            className="flex-1 bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 outline-none"
          />

          <button
            onClick={handleSend}
            className="bg-blue-600 hover:bg-blue-700 px-6 rounded-xl transition"
          >
            Send
          </button>

        </div>

      </div>

    </Layout>
  );
}