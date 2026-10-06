from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ImageRequest(BaseModel):
    prompt: str
    style: str = "cinematic"
    width: int = 1024
    height: int = 1024

@router.post("/generate")
def generate_image(payload: ImageRequest):
    return {
        "status": "queued",
        "prompt": payload.prompt,
        "style": payload.style,
        "output": "/storage/generated/sample-image.png"
    }
