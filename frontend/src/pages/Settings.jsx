import {
  useState,
} from "react";

import {
  useNavigate,
  Link,
} from "react-router-dom";

import {
  registerUser,
} from "../services/authService";


export default function Register() {

  const navigate =
    useNavigate();

  const [
    email,
    setEmail,
  ] = useState("");

  const [
    password,
    setPassword,
  ] = useState("");

  const [
    loading,
    setLoading,
  ] = useState(false);

  const [
    error,
    setError,
  ] = useState("");

  const handleRegister =
    async (e) => {

      e.preventDefault();

      setError("");

      setLoading(true);

      try {

        await registerUser(
          email,
          password
        );

        // REDIRECT TO LOGIN
        navigate("/login");

      } catch (err) {

        console.error(err);

        setError(
          err?.response?.data?.detail ||
          "Registration failed"
        );

      } finally {

        setLoading(false);
      }
    };

  return (

    <div className="min-h-screen bg-slate-950 flex items-center justify-center px-6">

      <div className="w-full max-w-md bg-slate-900 border border-slate-800 rounded-2xl p-8">

        <h1 className="text-4xl font-bold text-white mb-2">

          Create Account

        </h1>

        <p className="text-slate-400 mb-8">

          Register to start using AI SaaS

        </p>

        {error && (

          <div className="bg-red-500/10 border border-red-500 text-red-400 p-3 rounded-lg mb-6">

            {error}

          </div>
        )}

        <form
          onSubmit={handleRegister}
          className="space-y-6"
        >

          {/* EMAIL */}
          <div>

            <label className="block text-slate-300 mb-2">

              Email

            </label>

            <input
              type="email"

              value={email}

              onChange={(e) =>
                setEmail(
                  e.target.value
                )
              }

              required

              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white outline-none focus:border-blue-500"
            />

          </div>

          {/* PASSWORD */}
          <div>

            <label className="block text-slate-300 mb-2">

              Password

            </label>

            <input
              type="password"

              value={password}

              onChange={(e) =>
                setPassword(
                  e.target.value
                )
              }

              required

              className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-white outline-none focus:border-blue-500"
            />

          </div>

          {/* BUTTON */}
          <button
            type="submit"

            disabled={loading}

            className="w-full bg-blue-600 hover:bg-blue-700 transition text-white py-3 rounded-xl font-semibold disabled:opacity-50"
          >

            {loading
              ? "Creating Account..."
              : "Register"}

          </button>

        </form>

        <p className="text-slate-400 mt-6 text-center">

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