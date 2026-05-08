export async function streamMessage(
  message,
  threadId,
  onChunk
) {

  const token =
    localStorage.getItem("token");

  const response = await fetch(
    "http://127.0.0.1:8000/chat/stream",
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/json",

        Authorization:
          `Bearer ${token}`,
      },

      body: JSON.stringify({
        message,
        thread_id: Number(threadId),
      }),
    }
  );

  // HANDLE ERRORS
  if (!response.ok) {

    const errorText =
      await response.text();

    throw new Error(errorText);
  }

  const reader =
    response.body.getReader();

  const decoder =
    new TextDecoder();

  let done = false;

  while (!done) {

    const result =
      await reader.read();

    done = result.done;

    const chunk =
      decoder.decode(
        result.value || new Uint8Array(),
        {
          stream: true,
        }
      );

    if (chunk) {

      onChunk(chunk);
    }
  }
}