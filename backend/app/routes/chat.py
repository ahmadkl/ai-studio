from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    model: str = "default"

@router.post("/send")
def send_chat(payload: ChatRequest):
    return {
        "reply": f"AI: {payload.message}",
        "model": payload.model,
        "status": "mocked"
    }

@router.get("/history")
def chat_history():
    return {"messages": []}
