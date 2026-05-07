import api from "../api/axios";


// =========================
// ROOT STATUS
// =========================
export async function getSystemStatus() {

  const response = await api.get(
    "/"
  );

  return response.data;
}