# Laden von Bibliotheken
from fastapi import Depends, APIRouter

# Importiere von FastAPI-Routern
from api.classifier import classifier_router
from api.summarizer import summarization_router

# Definiere einen neuen Router (APIRouter)
api_router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
    dependencies=[]
)


# Definiere eine Page für die API-Anbindung
@api_router.get("/")
async def read_api():
    return {"message": "Welcome to the StripTheText 2.0 API!"}


# Registriere die API-Router der unterschiedlichen Anwendungen
api_router.include_router(classifier_router)
api_router.include_router(summarization_router)
