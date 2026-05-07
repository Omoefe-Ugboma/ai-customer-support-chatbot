import {
  MessageSquare,
  Upload,
  BarChart3,
  ArrowRight,
} from "lucide-react";

import { Link } from "react-router-dom";

import Layout from "../components/Layout";


export default function Dashboard() {

  const cards = [
    {
      title: "AI Chat",
      description:
        "Interact with your AI assistant in real time.",
      icon: <MessageSquare size={28} />,
      path: "/chat",
      color: "bg-blue-600",
    },
    {
      title: "Upload Documents",
      description:
        "Upload PDF or TXT documents for RAG processing.",
      icon: <Upload size={28} />,
      path: "/upload",
      color: "bg-emerald-600",
    },
    {
      title: "Analytics",
      description:
        "Monitor AI usage, requests, and system insights.",
      icon: <BarChart3 size={28} />,
      path: "/analytics",
      color: "bg-purple-600",
    },
  ];

  return (
    <Layout>

      <div className="space-y-10">

        {/* ========================= */}
        {/* HEADER */}
        {/* ========================= */}
        <div>

          <h1 className="text-4xl font-bold text-white">
            Dashboard
          </h1>

          <p className="text-slate-400 mt-2 text-lg">
            Welcome to your AI SaaS platform.
          </p>

        </div>

        {/* ========================= */}
        {/* QUICK STATS */}
        {/* ========================= */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <p className="text-slate-400">
              System Status
            </p>

            <h2 className="text-3xl font-bold mt-3 text-green-400">
              Online
            </h2>

          </div>

          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <p className="text-slate-400">
              AI Engine
            </p>

            <h2 className="text-3xl font-bold mt-3 text-blue-400">
              GPT-4o
            </h2>

          </div>

          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <p className="text-slate-400">
              Vector Database
            </p>

            <h2 className="text-3xl font-bold mt-3 text-purple-400">
              Active
            </h2>

          </div>

        </div>

        {/* ========================= */}
        {/* FEATURE CARDS */}
        {/* ========================= */}
        <div>

          <h2 className="text-2xl font-semibold text-white mb-6">
            Platform Features
          </h2>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

            {cards.map((card) => (

              <Link
                key={card.title}
                to={card.path}
                className="group bg-slate-900 border border-slate-800 rounded-2xl p-6 hover:border-slate-700 hover:scale-[1.02] transition-all duration-300"
              >

                <div className={`w-14 h-14 rounded-xl flex items-center justify-center text-white ${card.color}`}>

                  {card.icon}

                </div>

                <h3 className="text-2xl font-semibold mt-6 text-white">
                  {card.title}
                </h3>

                <p className="text-slate-400 mt-3 leading-relaxed">
                  {card.description}
                </p>

                <div className="flex items-center gap-2 mt-6 text-blue-400 group-hover:translate-x-1 transition-all">

                  <span>
                    Open
                  </span>

                  <ArrowRight size={18} />

                </div>

              </Link>

            ))}

          </div>

        </div>

      </div>

    </Layout>
  );
}