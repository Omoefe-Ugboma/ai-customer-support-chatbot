from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import (
    Session,
)

from app.db.database import (
    SessionLocal,
)

from app.models.user import (
    User,
)

from app.models.chat_thread import (
    ChatThread,
)

from app.api.deps import (
    get_current_user,
)

# =========================
# ROUTER
# =========================
router = APIRouter(

    prefix="/threads",

    tags=["Threads"],
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
# CREATE THREAD
# =========================
@router.post("/")
def create_thread(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    user = (
        db.query(User)
        .filter(
            User.email ==
            current_user.email
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    thread = ChatThread(

        title="New Chat",

        user_id=user.id,
    )

    db.add(thread)

    db.commit()

    db.refresh(thread)

    return {
        "id": thread.id,
        "title": thread.title,
    }

# =========================
# GET THREADS
# =========================
@router.get("/")
def get_threads(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    user = (
        db.query(User)
        .filter(
            User.email ==
            current_user.email
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    threads = (

        db.query(ChatThread)

        .filter(
            ChatThread.user_id ==
            user.id
        )

        .order_by(
            ChatThread.created_at.desc()
        )

        .all()
    )

    return threads

# =========================
# DELETE THREAD
# =========================
@router.delete("/{thread_id}")
def delete_thread(
    thread_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    thread = (
        db.query(ChatThread)
        .filter(
            ChatThread.id == thread_id
        )
        .first()
    )

    if not thread:

        raise HTTPException(
            status_code=404,
            detail="Thread not found",
        )

    db.delete(thread)

    db.commit()

    return {
        "message":
            "Thread deleted"
    }

# =========================
# RENAME THREAD
# =========================
@router.put("/{thread_id}")
def rename_thread(
    thread_id: int,
    data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    thread = (
        db.query(ChatThread)
        .filter(
            ChatThread.id == thread_id
        )
        .first()
    )

    if not thread:

        raise HTTPException(
            status_code=404,
            detail="Thread not found",
        )

    thread.title = data.get(
        "title",
        thread.title
    )

    db.commit()

    db.refresh(thread)

    return thread

# =========================
# GET THREAD MESSAGES
# =========================
@router.get("/{thread_id}/messages")
def get_thread_messages(
    thread_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    user = (
        db.query(User)
        .filter(
            User.email ==
            current_user.email
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    thread = (
        db.query(ChatThread)
        .filter(
            ChatThread.id == thread_id,
            ChatThread.user_id == user.id,
        )
        .first()
    )

    if not thread:

        raise HTTPException(
            status_code=404,
            detail="Thread not found",
        )

    return [
        {
            "id": msg.id,
            "role": msg.role,
            "content": msg.content,
            "created_at": msg.created_at,
        }
        for msg in thread.messages
    ]