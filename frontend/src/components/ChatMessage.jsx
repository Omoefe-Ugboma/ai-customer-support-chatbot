import ReactMarkdown from "react-markdown";

import remarkGfm from "remark-gfm";

import { Prism as SyntaxHighlighter }
from "react-syntax-highlighter";

import { tomorrow }
from "react-syntax-highlighter/dist/esm/styles/prism";

import { format }
from "date-fns";


export default function ChatMessage({
  message,
}) {

  const isUser =
    message.role === "user";

  return (
    <div
      className={`flex ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}
    >

      <div
        className={`
          max-w-[85%]
          rounded-2xl
          px-5
          py-4
          shadow-lg
          ${
            isUser
              ? "bg-blue-600 text-white"
              : "bg-slate-900 border border-slate-800 text-slate-100"
          }
        `}
      >

        {/* MESSAGE */}
        <div className="prose prose-invert max-w-none">

          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            components={{
              code({
                inline,
                className,
                children,
                ...props
              }) {

                const match =
                  /language-(\w+)/.exec(
                    className || ""
                  );

                return !inline && match ? (
                  <SyntaxHighlighter
                    style={tomorrow}
                    language={match[1]}
                    PreTag="div"
                    {...props}
                  >
                    {String(children).replace(
                      /\n$/,
                      ""
                    )}
                  </SyntaxHighlighter>
                ) : (
                  <code
                    className="bg-slate-800 px-1 py-0.5 rounded"
                    {...props}
                  >
                    {children}
                  </code>
                );
              },
            }}
          >
            {message.content}
          </ReactMarkdown>

        </div>

        {/* TIME */}
        <div className="text-xs text-slate-400 mt-3 text-right">

          {message.timestamp ||
              message.created_at
                ? format(

                    new Date(

                      message.timestamp ||
                      message.created_at
                    ),

                    "HH:mm"
                  )

                : "--:--"
                }

        </div>

      </div>

    </div>
  );
}