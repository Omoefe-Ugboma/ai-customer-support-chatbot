import sys

from fastapi import (
    FastAPI,
)

from fastapi.middleware.cors import (
    CORSMiddleware,
)

from app.core.config import (
    settings,
)

from app.db.database import (
    Base,
    engine,
)

# Routers
from app.api.routes import (
    router,
)

from app.api.auth_routes import (
    router as auth_router,
)

from app.api.admin_routes import (
    router as admin_router,
)

from app.api.thread_routes import (
    router as thread_router,
)

# Models
from app.models.analytics import (
    Analytics,
)

# UTF-8 FIX
sys.stdout.reconfigure(
    encoding="utf-8"
)

# CREATE TABLES
Base.metadata.create_all(
    bind=engine
)

# =========================
# APP
# =========================
app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0",
)

# =========================
# CORS
# =========================
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# =========================
# ROUTERS
# =========================
app.include_router(router)

app.include_router(auth_router)

app.include_router(admin_router)

app.include_router(thread_router)

# =========================
# ROOT
# =========================
@app.get(
    "/",
    tags=["Root"],
)
def root():

    return {
        "message":
            "AI SaaS Platform Running",
    }