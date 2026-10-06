from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PersonaRequest(BaseModel):
    name: str
    description: str = ""
    style: str = "general"

@router.post("/save")
def save_persona(payload: PersonaRequest):
    return {
        "status": "saved",
        "name": payload.name,
        "style": payload.style,
        "description": payload.description,
    }

@router.get("/list")
def list_personas():
    return {"personas": []}
