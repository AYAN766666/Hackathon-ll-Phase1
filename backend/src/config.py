"""
Configuration module for the Todo Application AI Agent and MCP Server integration.
Handles environment variables and application settings.
"""
import os
from typing import Optional
from dotenv import load_dotenv
import logging

# Load environment variables from .env file, overriding system variables
load_dotenv(override=True)

logger = logging.getLogger(__name__)

class Config:
    """Application configuration class"""

    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")

    # JWT settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # AI Agent settings
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")  # Can be either Gemini API key or OpenRouter API key

    # Validate required settings
    @classmethod
    def validate(cls):
        """Validate that required configuration values are set"""
        # Only warn about missing GEMINI_API_KEY, don't raise an error
        # This allows the app to start but with limited AI functionality
        if not cls.GEMINI_API_KEY:
            logger.warning("GEMINI_API_KEY environment variable is not set. AI agent will have limited functionality.")


# Validate configuration on import
Config.validate()