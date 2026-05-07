import {
  useEffect,
  useRef,
  useState,
} from "react";

import Layout from "../components/Layout";

import ChatMessage
from "../components/ChatMessage";

import TypingIndicator
from "../components/TypingIndicator";

import ConversationSidebar
from "../components/ConversationSidebar";

import { sendMessage }
from "../services/chatService";


export default function Chat() {

  // =========================
  // CONVERSATIONS
  // =========================
  const [conversations,
    setConversations] = useState([
    {
      id: 1,
      title: "New Conversation",
      messages: [],
    },
  ]);

  const [activeConversation,
    setActiveConversation] =
    useState(1);

  const [message,
    setMessage] =
    useState("");

  const [loading,
    setLoading] =
    useState(false);

  const messagesEndRef =
    useRef(null);

  // =========================
  // ACTIVE CHAT
  // =========================
  const currentConversation =
    conversations.find(
      (c) =>
        c.id === activeConversation
    );

  // =========================
  // AUTO SCROLL
  // =========================
  useEffect(() => {

    messagesEndRef.current
      ?.scrollIntoView({
        behavior: "smooth",
      });

  }, [currentConversation]);

  // =========================
  // NEW CHAT
  // =========================
  const createConversation =
    () => {

      const newConversation = {
        id: Date.now(),
        title: "New Conversation",
        messages: [],
      };

      setConversations((prev) => [
        newConversation,
        ...prev,
      ]);

      setActiveConversation(
        newConversation.id
      );
    };

  // =========================
  // SEND MESSAGE
  // =========================
  const handleSend =
    async () => {

      if (!message.trim())
        return;

      const userMessage = {
        role: "user",
        content: message,
        timestamp: new Date(),
      };

      updateConversationMessages(
        userMessage
      );

      const currentMessage =
        message;

      setMessage("");

      setLoading(true);

      try {

        const response =
          await sendMessage(
            currentMessage
          );

        const aiMessage = {
          role: "assistant",
          content: response.reply,
          timestamp: new Date(),
        };

        updateConversationMessages(
          aiMessage
        );

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }
    };

  // =========================
  // UPDATE CHAT
  // =========================
  const updateConversationMessages =
    (newMessage) => {

      setConversations((prev) =>
        prev.map((conversation) => {

          if (
            conversation.id !==
            activeConversation
          ) {
            return conversation;
          }

          const updatedMessages = [
            ...conversation.messages,
            newMessage,
          ];

          return {
            ...conversation,
            title:
              conversation.messages
                .length === 0
                ? newMessage.content
                    .slice(0, 30)
                : conversation.title,
            messages:
              updatedMessages,
          };
        })
      );
    };

  // =========================
  // ENTER TO SEND
  // =========================
  const handleKeyDown =
    (e) => {

      if (
        e.key === "Enter" &&
        !e.shiftKey
      ) {

        e.preventDefault();

        handleSend();
      }
    };

  return (
    <Layout>

      <div className="flex h-full gap-6">

        {/* SIDEBAR */}
        <ConversationSidebar
          conversations={conversations}
          activeConversation={
            activeConversation
          }
          setActiveConversation={
            setActiveConversation
          }
          createConversation={
            createConversation
          }
        />

        {/* CHAT */}
        <div className="flex-1 flex flex-col">

          {/* HEADER */}
          <div className="mb-6">

            <h1 className="text-4xl font-bold">
              AI Assistant
            </h1>

            <p className="text-slate-400 mt-2">
              Ask anything.
            </p>

          </div>

          {/* MESSAGES */}
          <div className="flex-1 overflow-y-auto space-y-6 pr-2">

            {currentConversation
              ?.messages.length === 0 && (

              <div className="h-full flex items-center justify-center text-slate-500 text-lg">

                Start a conversation...

              </div>

            )}

            {currentConversation
              ?.messages.map(
                (msg, index) => (

                <ChatMessage
                  key={index}
                  message={msg}
                />

              ))}

            {loading && (
              <TypingIndicator />
            )}

            <div ref={messagesEndRef} />

          </div>

          {/* INPUT */}
          <div className="mt-6">

            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-4 flex items-end gap-4">

              <textarea
                value={message}
                onChange={(e) =>
                  setMessage(
                    e.target.value
                  )
                }
                onKeyDown={
                  handleKeyDown
                }
                rows={1}
                placeholder="Message AI..."
                className="flex-1 resize-none bg-transparent outline-none text-white"
              />

              <button
                onClick={handleSend}
                disabled={loading}
                className="bg-blue-600 hover:bg-blue-700 transition px-5 py-3 rounded-xl disabled:opacity-50"
              >
                Send
              </button>

            </div>

          </div>

        </div>

      </div>

    </Layout>
  );
}