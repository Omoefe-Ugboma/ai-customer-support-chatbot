from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.db.database import Base


class ChatMessage(Base):

    __tablename__ = "chat_messages"

    __table_args__ = {
        "extend_existing": True
    }

    # =========================
    # COLUMNS
    # =========================
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    role = Column(
        String,
        nullable=False,
    )

    content = Column(
        String,
        nullable=False,
    )

    thread_id = Column(
        Integer,
        ForeignKey("chat_threads.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    # =========================
    # RELATIONSHIP
    # =========================
    thread = relationship(
        "ChatThread",
        back_populates="messages",
    )