from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import generate_chat_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        reply = generate_chat_response(request.message)

        return ChatResponse(
            message=request.message,
            reply=reply
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )