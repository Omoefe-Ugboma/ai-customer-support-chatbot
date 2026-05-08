from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.models.user import User

from app.models.chat_thread import (
    ChatThread,
)

from app.api.deps import (
    get_current_user,
)

router = APIRouter(
    prefix="/threads",
    tags=["Threads"],
)


# =========================
# DB DEPENDENCY
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

    # FIND USER
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

    # CREATE THREAD
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