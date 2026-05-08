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


class ChatThread(Base):

    __tablename__ = "chat_threads"

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

    title = Column(
        String,
        default="New Chat",
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    # =========================
    # RELATIONSHIPS
    # =========================
    user = relationship(
        "User",
        back_populates="threads",
    )

    messages = relationship(
        "ChatMessage",
        back_populates="thread",
        cascade="all, delete-orphan",
    )