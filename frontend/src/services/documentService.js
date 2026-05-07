import api from "../api/axios";


// =========================
// UPLOAD FILE
// =========================
export async function uploadDocument(
  file
) {

  const formData =
    new FormData();

  formData.append(
    "file",
    file
  );

  const response = await api.post(
    "/upload",
    formData,
    {
      headers: {
        "Content-Type":
          "multipart/form-data",
      },
    }
  );

  return response.data;
}


// =========================
// ADD DOCUMENTS
// =========================
export async function addDocuments(
  texts
) {

  const response = await api.post(
    "/add-documents",
    {
      texts,
    }
  );

  return response.data;
}


// =========================
// RESET DOCUMENTS
// =========================
export async function resetDocuments() {

  const response = await api.post(
    "/reset-documents"
  );

  return response.data;
}


// =========================
// CLEAR CACHE
// =========================
export async function clearCache() {

  const response = await api.post(
    "/clear-cache"
  );

  return response.data;
}