from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import require_admin
from app.db.database import SessionLocal

from app.services.analytics_service import (
    get_summary,
    get_recent
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================
# 📊 SUMMARY
# =========================
@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return get_summary(db, admin.email)


# =========================
# 📊 RECENT
# =========================
@router.get("/recent")
def recent(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    return get_recent(db, admin.email)