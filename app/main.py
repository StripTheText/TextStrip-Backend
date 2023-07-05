# Import of required libraries
from fastapi import FastAPI

# Import of internal libraries / Routers
from app.api.api_router import api_router

app = FastAPI(
    title="Textstrip Server",
    description="This is the Server of the Textstrip Project",
    version="0.2.0",
    debug=True,
    include_in_schema=True
)


@app.on_event("startup")
async def startup_event():
    pass


@app.on_event("shutdown")
async def shutdown_event():
    pass


app.include_router(api_router, prefix="/api")

