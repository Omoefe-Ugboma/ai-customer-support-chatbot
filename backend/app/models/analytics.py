from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)

    # User (multi-tenant tracking)
    user_email = Column(String, index=True)

    # Chat data
    question = Column(String)
    response = Column(String)

    # Performance
    response_time = Column(Float)

    # Classification
    category = Column(String)

    # Timestamp
    created_at = Column(DateTime, default=datetime.utcnow)