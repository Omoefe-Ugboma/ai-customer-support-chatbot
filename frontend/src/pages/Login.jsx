import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

import { loginUser } from "../services/authService";
import { useAuth } from "../context/AuthContext";

export default function Login() {
  const { register, handleSubmit } = useForm();

  const navigate = useNavigate();

  const { login } = useAuth();

  const onSubmit = async (data) => {
    try {
      const response = await loginUser(data);

      login(response.access_token);

      navigate("/dashboard");

    } catch (error) {
      alert("Login failed");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">

      <form
        onSubmit={handleSubmit(onSubmit)}
        className="bg-slate-800 p-8 rounded w-96"
      >
        <h1 className="text-2xl mb-4">
          Login
        </h1>

        <input
          {...register("email")}
          placeholder="Email"
          className="w-full p-2 mb-4 text-black"
        />

        <input
          {...register("password")}
          type="password"
          placeholder="Password"
          className="w-full p-2 mb-4 text-black"
        />

        <button
          className="bg-blue-600 px-4 py-2 rounded w-full"
        >
          Login
        </button>

      </form>

    </div>
  );
}