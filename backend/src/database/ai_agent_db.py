"""
Database configuration for AI Agent operations.
Sets up SQLite database for storing AI agent session data.
"""
import os
from pathlib import Path
from sqlmodel import create_engine, Session
from ..models.ai_agent_session import AI_Agent_Session
from ..models.user_request import User_Request
from ..models.mcp_tool_call import MCP_Tool_Call
from ..models.agent_response import Agent_Response


# Default path for AI agent SQLite database
DEFAULT_AI_AGENT_DB_PATH = "database/ai_agent_db.sqlite"

# Get database path from environment or use default
AI_AGENT_DATABASE_URL = os.getenv("AI_AGENT_DATABASE_URL", f"sqlite:///{DEFAULT_AI_AGENT_DB_PATH}")


def create_ai_agent_db_and_tables():
    """
    Create the AI agent database and all required tables.
    """
    # Ensure the database directory exists
    db_path = Path(AI_AGENT_DATABASE_URL.replace("sqlite:///", ""))
    db_dir = db_path.parent
    db_dir.mkdir(parents=True, exist_ok=True)

    # Create engine
    engine = create_engine(AI_AGENT_DATABASE_URL, echo=False)

    # Create all tables
    AI_Agent_Session.metadata.create_all(engine)
    User_Request.metadata.create_all(engine)
    MCP_Tool_Call.metadata.create_all(engine)
    Agent_Response.metadata.create_all(engine)

    return engine


def get_ai_agent_session(engine):
    """
    Get a database session for AI agent operations.

    Args:
        engine: The database engine to use

    Yields:
        Session: Database session
    """
    with Session(engine) as session:
        yield session


# Global engine instance
ai_agent_engine = create_ai_agent_db_and_tables()