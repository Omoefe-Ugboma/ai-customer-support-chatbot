from pydantic import BaseModel


class ChatRequest(BaseModel):

    message: str

    thread_id: int


class ChatResponse(BaseModel):

    message: str

    reply: str