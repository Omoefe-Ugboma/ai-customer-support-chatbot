import api from "../api/axios";


// =========================
// REGISTER
// =========================
export async function registerUser(
  email,
  password
) {

  try {

    const response =
      await api.post(
        "/auth/register",
        {
          email,
          password,
        }
      );

    return response.data;

  } catch (error) {

    console.error(
      "Register error:",
      error
    );

    throw error;
  }
}


// =========================
// LOGIN
// =========================
export async function loginUser(
  email,
  password
) {

  try {

    // FORM DATA
    const formData =
      new URLSearchParams();

    formData.append(
      "username",
      email
    );

    formData.append(
      "password",
      password
    );

    const response =
      await api.post(

        "/auth/login",

        formData,

        {
          headers: {

            "Content-Type":
              "application/x-www-form-urlencoded",
          },
        }
      );

    return response.data;

  } catch (error) {

    console.error(
      "Login error:",
      error
    );

    throw error;
  }
}