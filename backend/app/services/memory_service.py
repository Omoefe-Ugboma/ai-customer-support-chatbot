from sqlalchemy.orm import Session
from app.models.chat import ChatMessage


def save_message(db: Session, session_id: str, role: str, content: str):
    msg = ChatMessage(
        session_id=session_id,
        role=role,
        content=content
    )
    db.add(msg)
    db.commit()


def get_conversation(db: Session, session_id: str, limit: int = 10):
    return (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.desc())
        .limit(limit)
        .all()
    )