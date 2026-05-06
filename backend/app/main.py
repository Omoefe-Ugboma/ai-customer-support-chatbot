from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.config import settings
from app.db.database import Base, engine
from app.models import chat, analytics
from app.api.admin_routes import router as admin_router
from app.api.auth_routes import router as auth_router
from app.db.database import Base, engine
from app.models.analytics import Analytics


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

# CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(admin_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "AI Chatbot API Running"}