from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
)

from fastapi.responses import (
    StreamingResponse,
)

from sqlalchemy.orm import Session

from pydantic import BaseModel

# DB
from app.db.database import (
    SessionLocal,
)

# Schemas
from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

# Services
from app.services.chat_service import (
    generate_chat_response,
)

from app.services.chat_stream_service import (
    generate_streaming_response,
)

from app.services.document_service import (
    add_documents,
)

from app.services.file_service import (
    extract_text_from_pdf,
    extract_text_from_txt,
)

from app.services.vector_store import (
    vector_store,
)

from app.services.cache_service import (
    clear_cache,
)

# Auth
from app.api.deps import (
    get_current_user,
)

# =========================
# ROUTER
# =========================
router = APIRouter(
    tags=["AI Chat"],
)

# =========================
# DATABASE
# =========================
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# =========================
# HEALTH CHECK
# =========================
@router.get(
    "/health",
    tags=["System"],
)
def health_check():

    return {
        "status": "ok",
        "message": "AI SaaS API Running",
    }

# =========================
# CHAT
# =========================
@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat_endpoint(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    ),
):

    reply = generate_chat_response(

        message=request.message,

        db=db,

        thread_id=request.thread_id,
    )

    return ChatResponse(
        message=request.message,
        reply=reply,
    )

# =========================
# STREAMING CHAT
# =========================
@router.post("/chat/stream")
async def stream_chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):

    async def event_generator():

        async for chunk in generate_streaming_response(

            message=request.message,

            db=db,

            thread_id=request.thread_id,

            user_email=user.email,
        ):

            yield chunk

    return StreamingResponse(
        event_generator(),
        media_type="text/plain",
    )

# =========================
# DOCUMENT MODEL
# =========================
class DocumentRequest(
    BaseModel
):

    texts: list[str]

# =========================
# ADD DOCUMENTS
# =========================
@router.post("/add-documents")
def add_docs(
    req: DocumentRequest,
    current_user=Depends(
        get_current_user
    ),
):

    if not req.texts:

        raise HTTPException(
            status_code=400,
            detail="No documents provided",
        )

    add_documents(req.texts)

    return {
        "message":
            "Documents added successfully",

        "user":
            current_user.email,
    }

# =========================
# RESET VECTOR STORE
# =========================
@router.post("/reset-documents")
def reset_docs(
    current_user=Depends(
        get_current_user
    ),
):

    vector_store.reset()

    return {
        "message":
            "Vector store cleared",

        "user":
            current_user.email,
    }

# =========================
# CLEAR CACHE
# =========================
@router.post("/clear-cache")
def clear_cache_endpoint(
    current_user=Depends(
        get_current_user
    ),
):

    clear_cache()

    return {
        "message":
            "Cache cleared",

        "user":
            current_user.email,
    }

# =========================
# FILE UPLOAD
# =========================
@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    current_user=Depends(
        get_current_user
    ),
):

    try:

        filename = (
            file.filename.lower()
        )

        if filename.endswith(".pdf"):

            text = extract_text_from_pdf(
                file.file
            )

        elif filename.endswith(".txt"):

            text = extract_text_from_txt(
                await file.read()
            )

        else:

            raise HTTPException(
                status_code=400,
                detail="Unsupported file type",
            )

        if not text.strip():

            raise HTTPException(
                status_code=400,
                detail="Empty file",
            )

        add_documents([text])

        return {

            "message":
                "File processed successfully",

            "filename":
                filename,

            "user":
                current_user.email,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )