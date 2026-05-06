from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.analytics import Analytics


# =========================
# 📊 LOG INTERACTION
# =========================
def log_interaction(
    db: Session,
    user_email: str,
    question: str,
    response: str,
    response_time: float,
    category: str = "general"
):
    record = Analytics(
        user_email=user_email,
        question=question,
        response=response,
        response_time=response_time,
        category=category
    )

    db.add(record)
    db.commit()


# =========================
# 📊 SUMMARY (PER USER)
# =========================
def get_summary(db: Session, user_email: str):
    total_requests = db.query(Analytics).filter(
        Analytics.user_email == user_email
    ).count()

    avg_response_time = db.query(
        func.avg(Analytics.response_time)
    ).filter(
        Analytics.user_email == user_email
    ).scalar() or 0

    category_data = db.query(
        Analytics.category,
        func.count(Analytics.id)
    ).filter(
        Analytics.user_email == user_email
    ).group_by(
        Analytics.category
    ).all()

    return {
        "total_requests": total_requests,
        "avg_response_time": round(avg_response_time, 2),
        "categories": [
            {"category": cat, "count": count}
            for cat, count in category_data
        ]
    }


# =========================
# 📊 RECENT (PER USER)
# =========================
def get_recent(db: Session, user_email: str, limit: int = 10):
    records = db.query(Analytics).filter(
        Analytics.user_email == user_email
    ).order_by(
        Analytics.created_at.desc()
    ).limit(limit).all()

    return [
        {
            "question": r.question,
            "response": r.response,
            "time": r.response_time,
            "category": r.category,
            "created_at": r.created_at
        }
        for r in records
    ]