import {
  useState,
} from "react";

import {
  useForm,
} from "react-hook-form";

import {
  Link,
  useNavigate,
} from "react-router-dom";

import {
  loginUser,
} from "../services/authService";

import {
  useAuth,
} from "../context/AuthContext";


export default function Login() {

  // =========================
  // FORM
  // =========================
  const {
    register,
    handleSubmit,
  } = useForm();

  // =========================
  // NAVIGATION
  // =========================
  const navigate =
    useNavigate();

  // =========================
  // AUTH CONTEXT
  // =========================
  const { login } =
    useAuth();

  // =========================
  // STATE
  // =========================
  const [
    loading,
    setLoading,
  ] = useState(false);

  const [
    error,
    setError,
  ] = useState("");

  // =========================
  // SUBMIT
  // =========================
  const onSubmit =
    async (data) => {

      try {

        setLoading(true);

        setError("");

        // LOGIN REQUEST
        const response =
          await loginUser(

            data.email,

            data.password
          );

        // SAVE TOKEN
        login(

          response.access_token,

          {
            email:
              data.email,
          }
        );

        // REDIRECT
        navigate(
          "/dashboard"
        );

      } catch (error) {

        console.error(
          "Login error:",
          error
        );

        setError(
          error?.response?.data
            ?.detail ||
          "Invalid credentials"
        );

      } finally {

        setLoading(false);
      }
    };

  return (

    <div className="min-h-screen bg-slate-950 flex items-center justify-center px-6">

      <div className="w-full max-w-md bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-2xl">

        {/* TITLE */}
        <div className="mb-8 text-center">

          <h1 className="text-4xl font-bold text-white">

            Welcome Back

          </h1>

          <p className="text-slate-400 mt-2">

            Login to continue using AI SaaS

          </p>

        </div>

        {/* ERROR */}
        {error && (

          <div className="bg-red-500/10 border border-red-500 text-red-400 p-3 rounded-xl mb-6">

            {error}

          </div>
        )}

        {/* FORM */}
        <form
          onSubmit={
            handleSubmit(
              onSubmit
            )
          }
          className="space-y-6"
        >

          {/* EMAIL */}
          <div>

            <label className="block text-slate-300 mb-2">

              Email

            </label>

            <input

              {...register(
                "email"
              )}

              type="email"

              placeholder="Enter your email"

              required

              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white outline-none focus:border-blue-500 transition"
            />

          </div>

          {/* PASSWORD */}
          <div>

            <label className="block text-slate-300 mb-2">

              Password

            </label>

            <input

              {...register(
                "password"
              )}

              type="password"

              placeholder="Enter your password"

              required

              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white outline-none focus:border-blue-500 transition"
            />

          </div>

          {/* BUTTON */}
          <button
            type="submit"

            disabled={loading}

            className="w-full bg-blue-600 hover:bg-blue-700 transition text-white py-3 rounded-xl font-semibold disabled:opacity-50"
          >

            {loading
              ? "Signing In..."
              : "Login"}

          </button>

        </form>

        {/* REGISTER */}
        <p className="text-slate-400 text-center mt-6">

          Don’t have an account?{" "}

          <Link
            to="/register"
            className="text-blue-400 hover:text-blue-300"
          >

            Register

          </Link>

        </p>

      </div>

    </div>
  );
}