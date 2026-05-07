import { useNavigate } from "react-router-dom";

import { useAuth } from "../context/AuthContext";

export default function Topbar() {

  const navigate = useNavigate();

  const { logout } = useAuth();

  const handleLogout = () => {

    logout();

    navigate("/");

  };

  return (
    <header className="h-16 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-6">

      <div>

        <h1 className="text-xl font-semibold">
          AI SaaS Platform
        </h1>

      </div>

      <button
        onClick={handleLogout}
        className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg transition"
      >
        Logout
      </button>

    </header>
  );
}