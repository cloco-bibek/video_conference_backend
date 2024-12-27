from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    CORS_ORIGINS: str
    HOST: str
    PORT: int

    STUN_SERVERS: List[str] = ["stun:stun.l.google.com:19302"]
    TURN_SERVERS: List[dict] = []

    @property
    def CORS_ORIGINS_LIST(self) -> List[str]:
        if self.CORS_ORIGINS == "*":
            return ["*"]
        # Convert the comma-separated string to a list
        return [origin.strip() for origin in self.CORS_ORIGINS.split(',')]

    class Config:
        env_file = ".env"

settings = Settings()
