from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings


# =========================
# 🔐 PASSWORD HASHING
# =========================
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

ACCESS_TOKEN_EXPIRE_MINUTES = 60


# =========================
# 🔑 NORMALIZE PASSWORD
# =========================
def normalize_password(password: str) -> str:
    return password[:72]


# =========================
# 🔒 HASH PASSWORD
# =========================
def hash_password(password: str):
    password = normalize_password(password)
    return pwd_context.hash(password)


# =========================
# ✅ VERIFY PASSWORD
# =========================
def verify_password(plain, hashed):
    plain = normalize_password(plain)
    return pwd_context.verify(plain, hashed)


# =========================
# 🎫 CREATE JWT TOKEN
# =========================
def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt