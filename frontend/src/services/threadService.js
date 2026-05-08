import api from "../api/axios";


// =========================
// CREATE THREAD
// =========================
export async function createThread() {

  const response =
    await api.post(
      "/threads/"
    );

  return response.data;
}


// =========================
// GET THREADS
// =========================
export async function getThreads() {

  const response =
    await api.get(
      "/threads/"
    );

  return response.data;
}


// =========================
// GET THREAD MESSAGES
// =========================
export async function getThreadMessages(
  threadId
) {

  const response =
    await api.get(
      `/threads/${threadId}/messages`
    );

  return response.data;
}


// =========================
// DELETE THREAD
// =========================
export async function deleteThread(
  threadId
) {

  await api.delete(
    `/threads/${threadId}`
  );
}


// =========================
// RENAME THREAD
// =========================
export async function renameThread(
  threadId,
  title
) {

  const response =
    await api.put(
      `/threads/${threadId}`,
      {
        title,
      }
    );

  return response.data;
}