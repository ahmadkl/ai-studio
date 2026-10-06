from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.image import router as image_router
from app.routes.video import router as video_router
from app.routes.persona import router as persona_router

app = FastAPI(
    title="AI Studio API",
    version="0.1.0",
    description="AI Studio backend API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/chat", tags=["chat"])
app.include_router(image_router, prefix="/api/image", tags=["image"])
app.include_router(video_router, prefix="/api/video", tags=["video"])
app.include_router(persona_router, prefix="/api/persona", tags=["persona"])

@app.get("/")
def root():
    return {"message": "Welcome to AI Studio"}

@app.get("/health")
def health():
    return {"status": "ok"}
