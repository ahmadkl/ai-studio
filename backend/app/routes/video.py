from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class VideoRequest(BaseModel):
    prompt: str
    duration_seconds: int = 10
    fps: int = 24

@router.post("/generate")
def generate_video(payload: VideoRequest):
    return {
        "status": "queued",
        "prompt": payload.prompt,
        "duration_seconds": payload.duration_seconds,
        "fps": payload.fps,
        "output": "/storage/generated/sample-video.mp4"
    }

@router.post("/extend")
def extend_video():
    return {"status": "queued", "message": "extension job started"}
