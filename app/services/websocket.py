# Import of required Libaries
from fastapi import APIRouter, WebSocket

# Create new Api-Router
websocket_route = APIRouter()


# Define Entry Point of Websocket
@websocket_route.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
