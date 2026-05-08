import { Suspense } from "react";

import AppRoutes from "./routes/AppRoutes";

import { AuthProvider } from "./context/AuthContext";


// =========================
// APP
// =========================
export default function App() {

  return (

    <AuthProvider>

      <Suspense
        fallback={

          <div className="min-h-screen bg-slate-950 flex items-center justify-center text-white text-xl">

            Loading AI SaaS...

          </div>
        }
      >

        <AppRoutes />

      </Suspense>

    </AuthProvider>
  );
}