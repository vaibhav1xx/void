from fastapi import APIRouter
from app.brain.brain import Brain

router = APIRouter()

brain = Brain()


@router.post("/chat")
def chat(data: dict):
    message = data.get("message", "")
    return brain.process_request(message)
