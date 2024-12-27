from fastapi import WebSocket, WebSocketDisconnect
from app.models import WebRTCMessage
from app.websocket.connection_manager import ConnectionManager
import logging

logger = logging.getLogger(__name__)

class WebRTCHandler:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    async def handle_websocket(self, websocket: WebSocket):
        await self.connection_manager.connect(websocket)
        room_id = None

        try:
            while True:
                data = await websocket.receive_text()
                message = WebRTCMessage.parse_raw(data)
                room_id = message.roomId

                # Join room if not already in it
                await self.connection_manager.join_room(room_id, websocket)

                # Log the message type for debugging
                logger.info(f"Received message type: {message.type} for room: {room_id}")

                # Broadcast the message to all peers in the room
                await self.connection_manager.broadcast_to_room(room_id, data, websocket)

        except WebSocketDisconnect:
            logger.info("WebSocket disconnected")
            self.connection_manager.disconnect(websocket, room_id)
        except Exception as e:
            logger.error(f"Error handling WebSocket message: {e}")
            self.connection_manager.disconnect(websocket, room_id)
