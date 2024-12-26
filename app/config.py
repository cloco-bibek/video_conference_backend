from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    CORS_ORIGINS: str
    HOST: str
    PORT: int

    @property
    def CORS_ORIGINS_LIST(self) -> List[str]:
        # Convert the comma-separated string to a list
        return [origin.strip() for origin in self.CORS_ORIGINS.split(',')]

    class Config:
        env_file = ".env"

settings = Settings()
