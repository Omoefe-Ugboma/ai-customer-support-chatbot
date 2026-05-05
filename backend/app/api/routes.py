from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import generate_chat_response
from app.db.database import SessionLocal

from app.services.document_service import add_documents
from pydantic import BaseModel

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    reply = generate_chat_response(
        request.message,
        db,
        request.session_id
    )

    return ChatResponse(
        message=request.message,
        reply=reply
    )
 
class DocumentRequest(BaseModel):
    texts: list[str]   
    
@router.post("/add-documents")
def add_docs(req: DocumentRequest):
    add_documents(req.texts)
    return {"message": "Documents added successfully"}