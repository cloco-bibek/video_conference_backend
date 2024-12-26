from pydantic import BaseModel
from typing import Optional, Dict, Any

class WebRTCMessage(BaseModel):
    type: str
    roomId: str
    offer: Optional[Dict[str, Any]] = None
    answer: Optional[Dict[str, Any]] = None
    candidate: Optional[Dict[str, Any]] = None