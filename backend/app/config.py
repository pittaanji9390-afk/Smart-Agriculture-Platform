"""
Application Configuration Module
Handles environment settings, database paths, and telemetry parameters.
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    APP_NAME: str = "AgriSphere Smart Agriculture Platform"
    APP_VERSION: str = "2.5.0"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "sqlite:///./agrisphere.db"
    
    # CORS
    CORS_ORIGINS: List[str] = ["*"]
    
    # Telemetry & IoT Simulator Settings
    TELEMETRY_INTERVAL_SECONDS: float = 2.5
    DEFAULT_ZONES_COUNT: int = 4
    
    # Weather Simulation
    DEFAULT_LOCATION: str = "Hyderabad, India"
    DEFAULT_LATITUDE: float = 17.3850
    DEFAULT_LONGITUDE: float = 78.4867
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
