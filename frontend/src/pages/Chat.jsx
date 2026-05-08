import {
  useEffect,
  useRef,
  useState,
} from "react";

import Layout from "../components/Layout";

import ChatMessage from "../components/ChatMessage";

import TypingIndicator from "../components/TypingIndicator";

import ConversationSidebar from "../components/ConversationSidebar";

import {
  streamMessage,
} from "../services/chatService";

import {
  createThread,
} from "../services/threadService";

export default function Chat() {

  // =========================
  // STATE
  // =========================
  const [
    conversations,
    setConversations,
  ] = useState([]);

  const [
    activeConversation,
    setActiveConversation,
  ] = useState(null);

  const [
    message,
    setMessage,
  ] = useState("");

  const [
    loading,
    setLoading,
  ] = useState(false);

  const messagesEndRef =
    useRef(null);

  // =========================
  // ACTIVE CONVERSATION
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
  // CREATE CONVERSATION
  // =========================
  const createConversation =
    async () => {

      try {

        const backendThread =
          await createThread();

        const newConversation = {

          id: backendThread.id,

          title:
            backendThread.title ||
            "New Chat",

          messages: [],
        };

        setConversations(
          (prev) => [
            newConversation,
            ...prev,
          ]
        );

        setActiveConversation(
          backendThread.id
        );

      } catch (error) {

        console.error(
          "Create thread error:",
          error
        );
      }
    };

  // =========================
  // SEND MESSAGE
  // =========================
  const handleSend =
    async () => {

      if (
        !message.trim()
      ) {
        return;
      }

      let currentThreadId =
        activeConversation;

      // =========================
      // CREATE THREAD IF NONE
      // =========================
      if (!currentThreadId) {

        try {

          const backendThread =
            await createThread();

          currentThreadId =
            backendThread.id;

          const newConversation = {

            id: backendThread.id,

            title:
              backendThread.title ||
              "New Chat",

            messages: [],
          };

          setConversations(
            (prev) => [
              newConversation,
              ...prev,
            ]
          );

          setActiveConversation(
            backendThread.id
          );

        } catch (error) {

          console.error(
            "Failed to create thread:",
            error
          );

          return;
        }
      }

      const currentMessage =
        message;

      setMessage("");

      setLoading(true);

      // =========================
      // USER MESSAGE
      // =========================
      const userMessage = {

        role: "user",

        content: currentMessage,

        timestamp:
          new Date(),
      };

      // =========================
      // EMPTY AI MESSAGE
      // =========================
      const aiMessage = {

        role: "assistant",

        content: "",

        timestamp:
          new Date(),
      };

      // =========================
      // ADD BOTH MESSAGES
      // =========================
      setConversations(
        (prev) =>
          prev.map(
            (conversation) => {

              if (
                conversation.id !==
                currentThreadId
              ) {
                return conversation;
              }

              return {

                ...conversation,

                title:
                  conversation.messages
                    .length === 0
                    ? currentMessage
                        .slice(0, 30)
                    : conversation.title,

                messages: [
                  ...(conversation.messages || []),

                  userMessage,

                  aiMessage,
                ],
              };
            }
          )
      );

      try {

        await streamMessage(

          currentMessage,

          currentThreadId,

          (chunk) => {

            setConversations(
              (prev) =>
                prev.map(
                  (
                    conversation
                  ) => {

                    if (
                      conversation.id !==
                      currentThreadId
                    ) {
                      return conversation;
                    }

                    const messages = [
                      ...conversation.messages,
                    ];

                    const lastIndex =
                      messages.length - 1;

                    // IMMUTABLE UPDATE
                    messages[
                      lastIndex
                    ] = {

                      ...messages[
                        lastIndex
                      ],

                      content:
                        (
                          messages[
                            lastIndex
                          ]?.content || ""
                        ) + chunk,
                    };

                    return {

                      ...conversation,

                      messages,
                    };
                  }
                )
            );
          }
        );

      } catch (error) {

        console.error(
          "Streaming failed:",
          error
        );

      } finally {

        setLoading(false);
      }
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

        {/* CHAT AREA */}
        <div className="flex-1 flex flex-col">

          {/* HEADER */}
          <div className="mb-6">

            <h1 className="text-4xl font-bold text-white">
              AI Assistant
            </h1>

            <p className="text-slate-400 mt-2">
              Ask anything.
            </p>

          </div>

          {/* MESSAGES */}
          <div className="flex-1 overflow-y-auto space-y-6 pr-2">

            {(!currentConversation ||
              currentConversation
                ?.messages
                ?.length === 0) && (

              <div className="h-full flex items-center justify-center text-slate-500 text-lg">

                Start a conversation...

              </div>
            )}

            {currentConversation
              ?.messages?.map(
                (
                  msg,
                  index
                ) => (

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

                className="bg-blue-600 hover:bg-blue-700 transition px-5 py-3 rounded-xl disabled:opacity-50 text-white"
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