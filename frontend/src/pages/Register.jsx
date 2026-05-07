import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

import { registerUser } from "../services/authService";

export default function Register() {

  const { register, handleSubmit } = useForm();

  const navigate = useNavigate();

  const onSubmit = async (data) => {

    try {

      await registerUser(data);

      alert("Registration successful");

      navigate("/");

    } catch (error) {

      alert("Registration failed");

    }
  };

  return (
    <div className="flex items-center justify-center h-screen">

      <form
        onSubmit={handleSubmit(onSubmit)}
        className="bg-slate-800 p-8 rounded w-96"
      >
        <h1 className="text-2xl mb-4">
          Register
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
          className="bg-green-600 px-4 py-2 rounded w-full"
        >
          Register
        </button>

      </form>

    </div>
  );
}