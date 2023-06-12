# Import of external libraries
from fastapi import APIRouter

# Import of internal libraries / Routers
from app.api.classifier.classification_router import router as classification_router
from app.api.summarization.summarization_router import router as summarization_router
from app.api.whisper.whisper_router import router as whisper_router

# Init of new APIRouter Object
api_router = APIRouter()

# Include of all Routers of the API in the APIRouter Object
api_router.include_router(classification_router, prefix="/classification")
api_router.include_router(summarization_router, prefix="/summarization")
api_router.include_router(whisper_router, prefix="/sound2text")
