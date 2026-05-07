import api from "../api/axios";

export async function sendMessage(
  message
) {

  const response = await api.post(
    "/chat",
    {
      message,
      session_id: "frontend-session",
    }
  );

  return response.data;
}