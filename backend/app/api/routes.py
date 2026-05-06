# app/api/routes.py

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

# DB
from app.db.database import SessionLocal

# Schemas
from app.schemas.chat import ChatRequest, ChatResponse

# Services
from app.services.chat_service import generate_chat_response
from app.services.document_service import add_documents
from app.services.file_service import extract_text_from_pdf, extract_text_from_txt
from app.services.vector_store import vector_store
from app.services.cache_service import clear_cache

# 🔐 Auth
from app.api.deps import get_current_user

router = APIRouter()


# =========================
# 📦 DATABASE DEPENDENCY
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# 🏠 ROOT (PUBLIC)
# =========================
@router.get("/")
def root():
    return {"message": "🚀 AI SaaS API is running"}


# =========================
# 💬 CHAT (PROTECTED)
# =========================
@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    reply = generate_chat_response(
        message=request.message,
        db=db,
        session_id=current_user.email
    )

    return ChatResponse(
        message=request.message,
        reply=reply
    )

# =========================
# 📄 DOCUMENT REQUEST MODEL
# =========================
class DocumentRequest(BaseModel):
    texts: list[str]


# =========================
# 📥 ADD DOCUMENTS (PROTECTED)
# =========================
@router.post("/add-documents")
def add_docs(
    req: DocumentRequest,
    user_email: str = Depends(get_current_user)  # 🔒 PROTECTED
):
    if not req.texts:
        raise HTTPException(status_code=400, detail="No documents provided")

    add_documents(req.texts)

    return {
        "message": "Documents added successfully",
        "user": user_email
    }


# =========================
# 🔄 RESET VECTOR STORE (PROTECTED)
# =========================
@router.post("/reset-documents")
def reset_docs(user_email: str = Depends(get_current_user)):
    vector_store.reset()

    return {
        "message": "Vector store cleared",
        "user": user_email
    }


# =========================
# 🧹 CLEAR CACHE (PROTECTED)
# =========================
@router.post("/clear-cache")
def clear_cache_endpoint(user_email: str = Depends(get_current_user)):
    clear_cache()

    return {
        "message": "Cache cleared",
        "user": user_email
    }


# =========================
# 📤 FILE UPLOAD (PROTECTED)
# =========================
@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    user_email: str = Depends(get_current_user)
):
    try:
        filename = file.filename.lower()

        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file.file)

        elif filename.endswith(".txt"):
            text = extract_text_from_txt(await file.read())

        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        if not text.strip():
            raise HTTPException(status_code=400, detail="Empty file")

        add_documents([text])

        return {
            "message": "File processed successfully",
            "filename": filename,
            "user": user_email
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# # =========================
# # 📊 ADMIN SUMMARY (PROTECTED)
# # =========================
# @router.get("/admin/summary")
# def get_summary(user_email: str = Depends(get_current_user)):
#     from app.services.analytics_service import get_summary

#     return get_summary()


# # =========================
# # 📊 ADMIN RECENT (PROTECTED)
# # =========================
# @router.get("/admin/recent")
# def get_recent(user_email: str = Depends(get_current_user)):
#     from app.services.analytics_service import get_recent

#     return get_recent()