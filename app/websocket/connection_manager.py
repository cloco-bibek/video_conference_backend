from fastapi import WebSocket
from typing import Dict, Set
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.rooms: Dict[str, Set[WebSocket]] = {}
        self.active_connections: Set[WebSocket] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)
        logger.info(f"New connection established. Total connections: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket, room_id: str = None):
        self.active_connections.remove(websocket)
        if room_id and room_id in self.rooms:
            self.rooms[room_id].remove(websocket)
            if len(self.rooms[room_id]) == 0:
                del self.rooms[room_id]
        logger.info(f"Connection closed. Total connections: {len(self.active_connections)}")

    async def join_room(self, room_id: str, websocket: WebSocket):
        if room_id not in self.rooms:
            self.rooms[room_id] = set()
        self.rooms[room_id].add(websocket)
        logger.info(f"Client joined room {room_id}. Room size: {len(self.rooms[room_id])}")

    async def broadcast_to_room(self, room_id: str, message: str, sender: WebSocket):
        if room_id in self.rooms:
            for peer in self.rooms[room_id]:
                if peer != sender:
                    try:
                        await peer.send_text(message)
                    except Exception as e:
                        logger.error(f"Error broadcasting message: {e}")