export default function ChatMessage({
  role,
  content,
}) {

  return (
    <div
      className={`mb-4 p-4 rounded-lg ${
        role === "user"
          ? "bg-blue-600 ml-auto w-fit max-w-[70%]"
          : "bg-slate-800 mr-auto w-fit max-w-[70%]"
      }`}
    >
      {content}
    </div>
  );
}