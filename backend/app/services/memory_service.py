from sqlalchemy.orm import Session

from app.models.chat_message import (
    ChatMessage,
)


# =========================
# SAVE MESSAGE
# =========================
def save_message(
    db: Session,
    thread_id: int,
    role: str,
    content: str,
):

    message = ChatMessage(
        thread_id=thread_id,
        role=role,
        content=content,
    )

    db.add(message)

    db.commit()

    db.refresh(message)

    return message


# =========================
# GET CONVERSATION
# =========================
def get_conversation(
    db: Session,
    thread_id: int,
    limit: int = 10,
):

    return (
        db.query(ChatMessage)
        .filter(
            ChatMessage.thread_id
            == thread_id
        )
        .order_by(
            ChatMessage.created_at.asc()
        )
        .limit(limit)
        .all()
    )