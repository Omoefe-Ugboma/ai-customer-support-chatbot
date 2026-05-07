import api from "../api/axios";

export async function loginUser(data) {
  const form = new URLSearchParams();

  form.append("username", data.email);
  form.append("password", data.password);

  const response = await api.post(
    "/auth/login",
    form,
    {
      headers: {
        "Content-Type":
          "application/x-www-form-urlencoded",
      },
    }
  );

  return response.data;
}

export async function registerUser(data) {
  const response = await api.post(
    "/auth/register",
    data
  );

  return response.data;
}