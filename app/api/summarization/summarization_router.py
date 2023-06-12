# Import of required Libraries
from fastapi import APIRouter

router = APIRouter()


# Summarize the incoming Text[str] -> Class[str]
@router.post("/")
async def summarize_text():
    pass
