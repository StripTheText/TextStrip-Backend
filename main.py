# Laden von Bibliotheken
from fastapi import FastAPI

# Importing von FastAPI-Router
from api import api_router

# Erstelle eine neue FastAPI Anwendung
app = FastAPI(
    title="StripTheText 2.0 - Backend Server",
    description="This is the backend server for the StripTheText 2.0 project",
    version="2.0.0",
    docs_url="/"
)


@app.on_event("startup")
def startup_event():
    pass


@app.on_event("shutdown")
def shutdown_event():
    pass


# Registiere den API-Router
app.include_router(api_router)
