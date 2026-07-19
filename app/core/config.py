"""
TaskMesg Settings Module
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Centralized application configuration.

    Loads values from environment variables and `.env`.

    Args:
        BaseSettings (BaseSettings): Inherits Pydantic BaseSettings Module 
    """
    app_name: str = "TaskMesh"
    app_version: str = "0.1.0"
    debug: bool = False
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

# Initilize Settings class object
settings = Settings()
