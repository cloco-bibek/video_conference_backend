from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.websocket.handlers import WebRTCHandler
from fastapi import WebSocket

app = FastAPI(title="WebRTC Signaling Server")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize WebRTC handler
webrtc_handler = WebRTCHandler()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await webrtc_handler.handle_websocket(websocket)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )