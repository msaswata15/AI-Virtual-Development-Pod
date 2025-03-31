from fastapi import APIRouter
from agents.business_analyst import BusinessAnalyst

router = APIRouter()

@router.get("/generate_user_stories/")
def generate_stories(requirements: str):
    ba = BusinessAnalyst()
    return {"user_stories": ba.generate_user_stories(requirements)}
