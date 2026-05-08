from sqlalchemy import (
    Column,
    Integer,
    String,
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):

    __tablename__ = "users"

    # =========================
    # COLUMNS
    # =========================
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False,
    )

    password = Column(
        String,
        nullable=False,
    )

    role = Column(
        String,
        default="user",
    )

    # =========================
    # RELATIONSHIPS
    # =========================
    threads = relationship(
        "app.models.chat_thread.ChatThread",
        back_populates="user",
        cascade="all, delete-orphan",
    )