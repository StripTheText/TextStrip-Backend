from fastapi import FastAPI, WebSocket


# Define the FastAPI app
app = FastAPI(
    title="Textstrip - Server",
    description="A  server for the Textstrip API and WebSocket",
    version="0.1.0",
    docs_url="/",
    debug=True,
    include_in_schema=True
)
