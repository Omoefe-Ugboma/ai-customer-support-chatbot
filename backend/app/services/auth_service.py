from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


# =========================
# 📝 REGISTER USER
# =========================
def register_user(db: Session, email: str, password: str):

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    new_user = User(
        email=email,
        password=hash_password(password),
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# =========================
# 🔐 AUTHENTICATE USER
# =========================
def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    # ❌ USER NOT FOUND
    if not user:
        return None

    # ❌ WRONG PASSWORD
    if not verify_password(password, user.password):
        return None

    return user


# =========================
# 🚪 LOGIN USER
# =========================
def login_user(
    db: Session,
    email: str,
    password: str
):

    user = authenticate_user(
        db,
        email,
        password
    )

    # ❌ INVALID LOGIN
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # ✅ GENERATE TOKEN
    access_token = create_access_token({
        "sub": user.email,
        "role": user.role
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }