# Import of required Libraries
from fastapi import APIRouter

router = APIRouter()


# Classify the incoming Text[str] -> Class[str]
@router.post("/")
async def classify_text():
    pass
