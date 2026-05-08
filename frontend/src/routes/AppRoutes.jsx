import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Login from "../pages/Login";

import Register from "../pages/Register";

import Dashboard from "../pages/Dashboard";

import Chat from "../pages/Chat";

import Upload from "../pages/Upload";

import Analytics from "../pages/Analytics";

import Settings from "../pages/Settings";

import { useAuth } from "../context/AuthContext";


// =========================
// PRIVATE ROUTE
// =========================
function PrivateRoute({
  children,
}) {

  const {
    isAuthenticated,
  } = useAuth();

  if (!isAuthenticated) {

    return (
      <Navigate
        to="/login"
        replace
      />
    );
  }

  return children;
}


// =========================
// ROUTES
// =========================
export default function AppRoutes() {

  return (

    <BrowserRouter>

      <Routes>

        {/* ROOT */}
        <Route
          path="/"
          element={
            <Navigate
              to="/dashboard"
              replace
            />
          }
        />

        {/* AUTH */}
        <Route
          path="/login"
          element={<Login />}
        />

        <Route
          path="/register"
          element={<Register />}
        />

        {/* DASHBOARD */}
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>

              <Dashboard />

            </PrivateRoute>
          }
        />

        {/* CHAT */}
        <Route
          path="/chat"
          element={
            <PrivateRoute>

              <Chat />

            </PrivateRoute>
          }
        />

        {/* UPLOAD */}
        <Route
          path="/upload"
          element={
            <PrivateRoute>

              <Upload />

            </PrivateRoute>
          }
        />

        {/* ANALYTICS */}
        <Route
          path="/analytics"
          element={
            <PrivateRoute>

              <Analytics />

            </PrivateRoute>
          }
        />

        {/* SETTINGS */}
        <Route
          path="/settings"
          element={
            <PrivateRoute>

              <Settings />

            </PrivateRoute>
          }
        />

        {/* FALLBACK */}
        <Route
          path="*"
          element={
            <Navigate
              to="/dashboard"
              replace
            />
          }
        />

      </Routes>

    </BrowserRouter>
  );
}