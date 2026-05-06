from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.services.auth_service import login_user, register_user
from app.schemas.user import UserCreate

router = APIRouter(prefix="/auth", tags=["Authentication"])


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
# REGISTER
# =========================
@router.post("/register")
def register(
    request: UserCreate,
    db: Session = Depends(get_db)
):
    user = register_user(
        db,
        request.email,
        request.password
    )

    return {
        "message": "User registered successfully",
        "email": user.email
    }


# =========================
# LOGIN
# =========================
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return login_user(
        db,
        form_data.username,
        form_data.password
    )