# Import of required Libraries
from fastapi import APIRouter

router = APIRouter()


# Transcribe the Incoming Audio-File and send it back to the Front-End
@router.post("/")
async def audio2text():
    pass
