import api from "../api/axios";


// =========================
// CREATE THREAD
// =========================
export async function createThread() {

  try {

    const response =
      await api.post(
        "/threads/"
      );

    return response.data;

  } catch (error) {

    console.error(
      "Create thread error:",
      error
    );

    throw error;
  }
}


// =========================
// GET THREADS
// =========================
export async function getThreads() {

  try {

    const response =
      await api.get(
        "/threads/"
      );

    return response.data || [];

  } catch (error) {

    console.error(
      "Get threads error:",
      error
    );

    return [];
  }
}


// =========================
// DELETE THREAD
// =========================
export async function deleteThread(
  threadId
) {

  try {

    await api.delete(
      `/threads/${threadId}`
    );

    return true;

  } catch (error) {

    console.error(
      "Delete thread error:",
      error
    );

    return false;
  }
}


// =========================
// RENAME THREAD
// =========================
export async function renameThread(
  threadId,
  title
) {

  try {

    const response =
      await api.put(
        `/threads/${threadId}`,
        {
          title,
        }
      );

    return response.data;

  } catch (error) {

    console.error(
      "Rename thread error:",
      error
    );

    throw error;
  }
}


// =========================
// GET SINGLE THREAD
// =========================
export async function getThread(
  threadId
) {

  try {

    const response =
      await api.get(
        `/threads/${threadId}`
      );

    return response.data;

  } catch (error) {

    console.error(
      "Get thread error:",
      error
    );

    throw error;
  }
}