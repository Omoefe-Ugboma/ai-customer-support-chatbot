import {
  Pencil,
  Trash2,
  Plus,
} from "lucide-react";

import {
  deleteThread,
  renameThread,
} from "../services/threadService";

export default function ConversationSidebar({

  conversations,

  activeConversation,

  setActiveConversation,

  createConversation,
}) {

  // =========================
  // DELETE
  // =========================
  const handleDelete =
    async (
      e,
      threadId
    ) => {

      e.stopPropagation();

      try {

        await deleteThread(
          threadId
        );

        window.location.reload();

      } catch (error) {

        console.error(
          error
        );
      }
    };

  // =========================
  // RENAME
  // =========================
  const handleRename =
    async (
      e,
      thread
    ) => {

      e.stopPropagation();

      const newTitle =
        prompt(
          "Rename chat",
          thread.title
        );

      if (!newTitle) {
        return;
      }

      try {

        await renameThread(
          thread.id,
          newTitle
        );

        window.location.reload();

      } catch (error) {

        console.error(
          error
        );
      }
    };

  return (

    <div className="w-80 border-r border-slate-800 flex flex-col">

      {/* HEADER */}
      <button

        onClick={
          createConversation
        }

        className="m-4 flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 transition rounded-xl py-4 text-white font-semibold"
      >

        <Plus size={18} />

        New Chat

      </button>

      {/* THREADS */}
      <div className="flex-1 overflow-y-auto px-3 pb-4 space-y-2">

        {conversations.map(
          (conversation) => (

          <div

            key={
              conversation.id
            }

            onClick={() =>
              setActiveConversation(
                conversation.id
              )
            }

            className={`group flex items-center justify-between rounded-xl px-4 py-3 cursor-pointer transition ${
              activeConversation ===
              conversation.id

                ? "bg-slate-800 text-white"

                : "hover:bg-slate-900 text-slate-300"
            }`}
          >

            <span className="truncate text-sm">

              {conversation.title}

            </span>

            {/* ACTIONS */}
            <div className="hidden group-hover:flex items-center gap-2">

              <button
                onClick={(e) =>
                  handleRename(
                    e,
                    conversation
                  )
                }
              >

                <Pencil size={15} />

              </button>

              <button
                onClick={(e) =>
                  handleDelete(
                    e,
                    conversation.id
                  )
                }
              >

                <Trash2 size={15} />

              </button>

            </div>

          </div>
        ))}
      </div>

    </div>
  );
}