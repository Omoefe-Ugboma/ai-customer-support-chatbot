export default function TypingIndicator() {

  return (
    <div className="flex justify-start">

      <div className="bg-slate-900 border border-slate-800 rounded-2xl px-5 py-4">

        <div className="flex gap-2">

          <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></span>

          <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-100"></span>

          <span className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-200"></span>

        </div>

      </div>

    </div>
  );
}