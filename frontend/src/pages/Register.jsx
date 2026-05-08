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
  registerUser,
} from "../services/authService";


export default function Register() {

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

  const [
    success,
    setSuccess,
  ] = useState("");

  // =========================
  // SUBMIT
  // =========================
  const onSubmit =
    async (data) => {

      try {

        setLoading(true);

        setError("");

        setSuccess("");

        // REGISTER USER
        await registerUser(

          data.email,

          data.password
        );

        setSuccess(
          "Registration successful"
        );

        // REDIRECT
        setTimeout(() => {

          navigate("/login");

        }, 1200);

      } catch (error) {

        console.error(
          "Registration error:",
          error
        );

        setError(

          error?.response?.data
            ?.detail ||

          "Registration failed"
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

            Create Account

          </h1>

          <p className="text-slate-400 mt-2">

            Register to start using AI SaaS

          </p>

        </div>

        {/* SUCCESS */}
        {success && (

          <div className="bg-green-500/10 border border-green-500 text-green-400 p-3 rounded-xl mb-6">

            {success}

          </div>
        )}

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

              placeholder="Create password"

              required

              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white outline-none focus:border-blue-500 transition"
            />

          </div>

          {/* BUTTON */}
          <button
            type="submit"

            disabled={loading}

            className="w-full bg-green-600 hover:bg-green-700 transition text-white py-3 rounded-xl font-semibold disabled:opacity-50"
          >

            {loading
              ? "Creating Account..."
              : "Register"}

          </button>

        </form>

        {/* LOGIN */}
        <p className="text-slate-400 text-center mt-6">

          Already have an account?{" "}

          <Link
            to="/login"
            className="text-blue-400 hover:text-blue-300"
          >

            Login

          </Link>

        </p>

      </div>

    </div>
  );
}