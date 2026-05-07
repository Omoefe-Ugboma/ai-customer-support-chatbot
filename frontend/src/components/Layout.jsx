import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

export default function Layout({
  children,
}) {

  return (
    <div className="flex h-screen bg-slate-950 text-white overflow-hidden">

      {/* SIDEBAR */}
      <Sidebar />

      {/* MAIN CONTENT */}
      <div className="flex-1 flex flex-col">

        {/* TOPBAR */}
        <Topbar />

        {/* PAGE CONTENT */}
        <main className="flex-1 overflow-y-auto p-6">

          {children}

        </main>

      </div>

    </div>
  );
}