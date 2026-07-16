"""
TaskMesg Settings Module
"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Class to Define Application Related Configuration

    Args:
        BaseSettings (BaseSettings): Inherits Pydantic BaseSettings Module 
    """
    app_name: str
    app_version: str
    debug: bool
    log_level: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )

# Initilize Settings class object
settings = Settings()
