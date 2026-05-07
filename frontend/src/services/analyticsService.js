import api from "../api/axios";


// =========================
// SUMMARY
// =========================
export async function getSummary() {

  const response = await api.get(
    "/admin/summary"
  );

  return response.data;
}


// =========================
// RECENT CHATS
// =========================
export async function getRecent() {

  const response = await api.get(
    "/admin/recent"
  );

  return response.data;
}