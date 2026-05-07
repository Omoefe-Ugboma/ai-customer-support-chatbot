export default function ConversationSidebar({
  conversations,
  activeConversation,
  setActiveConversation,
  createConversation,
}) {

  return (
    <div className="w-80 bg-slate-950 border-r border-slate-800 flex flex-col">

      {/* HEADER */}
      <div className="p-4 border-b border-slate-800">

        <button
          onClick={createConversation}
          className="w-full bg-blue-600 hover:bg-blue-700 transition rounded-xl py-3 font-medium"
        >
          + New Chat
        </button>

      </div>

      {/* CONVERSATIONS */}
      <div className="flex-1 overflow-y-auto p-3 space-y-2">

        {conversations.map((conversation) => (

          <button
            key={conversation.id}
            onClick={() =>
              setActiveConversation(
                conversation.id
              )
            }
            className={`
              w-full
              text-left
              px-4
              py-3
              rounded-xl
              transition-all
              ${
                activeConversation ===
                conversation.id
                  ? "bg-slate-800"
                  : "hover:bg-slate-900"
              }
            `}
          >

            <p className="truncate text-sm font-medium">

              {conversation.title}

            </p>

          </button>

        ))}

      </div>

    </div>
  );
}