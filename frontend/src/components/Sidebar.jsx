import {
  LayoutDashboard,
  MessageSquare,
  Upload,
  BarChart3,
  Settings,
  LogOut,
  Sparkles,
} from "lucide-react";

import {
  NavLink,
  useNavigate,
} from "react-router-dom";

import { useAuth } from "../context/AuthContext";


export default function Sidebar() {

  const navigate = useNavigate();

  const { logout } = useAuth();

  // =========================
  // NAVIGATION ITEMS
  // =========================
  const navigation = [
    {
      name: "Dashboard",
      path: "/dashboard",
      icon: LayoutDashboard,
    },
    {
      name: "AI Chat",
      path: "/chat",
      icon: MessageSquare,
    },
    {
      name: "Upload",
      path: "/upload",
      icon: Upload,
    },
    {
      name: "Analytics",
      path: "/analytics",
      icon: BarChart3,
    },
    {
      name: "Settings",
      path: "/settings",
      icon: Settings,
    },
  ];

  // =========================
  // LOGOUT
  // =========================
  const handleLogout = () => {

    logout();

    navigate("/");

  };

  return (
    <aside className="w-72 min-h-screen bg-slate-900 border-r border-slate-800 flex flex-col">

      {/* ========================= */}
      {/* LOGO */}
      {/* ========================= */}
      <div className="h-20 flex items-center px-6 border-b border-slate-800">

        <div className="flex items-center gap-3">

          <div className="w-11 h-11 rounded-xl bg-blue-600 flex items-center justify-center">

            <Sparkles size={22} className="text-white" />

          </div>

          <div>

            <h1 className="text-xl font-bold text-white">
              AI SaaS
            </h1>

            <p className="text-xs text-slate-400">
              Enterprise Platform
            </p>

          </div>

        </div>

      </div>

      {/* ========================= */}
      {/* NAVIGATION */}
      {/* ========================= */}
      <nav className="flex-1 p-4 space-y-2">

        {navigation.map((item) => {

          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `
                flex items-center gap-4 px-4 py-3 rounded-xl transition-all duration-200 group
                ${
                  isActive
                    ? "bg-blue-600 text-white shadow-lg shadow-blue-600/20"
                    : "text-slate-300 hover:bg-slate-800 hover:text-white"
                }
                `
              }
            >

              <Icon
                size={20}
                className="group-hover:scale-110 transition-transform"
              />

              <span className="font-medium">
                {item.name}
              </span>

            </NavLink>
          );
        })}

      </nav>

      {/* ========================= */}
      {/* FOOTER */}
      {/* ========================= */}
      <div className="p-4 border-t border-slate-800">

        <button
          onClick={handleLogout}
          className="w-full flex items-center gap-4 px-4 py-3 rounded-xl text-slate-300 hover:bg-red-600 hover:text-white transition-all duration-200"
        >

          <LogOut size={20} />

          <span className="font-medium">
            Logout
          </span>

        </button>

      </div>

    </aside>
  );
}