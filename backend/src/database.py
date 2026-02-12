from sqlmodel import create_engine, Session
from sqlalchemy import engine
from typing import Generator
from .models.user import User
from .models.task import Task
from .models.ai_agent_session import AI_Agent_Session
from .models.user_request import User_Request
from .models.mcp_tool_call import MCP_Tool_Call
from .models.agent_response import Agent_Response
import os
from pathlib import Path

# Use SQLite database
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{Path(__file__).parent.parent}/todo.db")

engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    """Create database tables if they don't exist."""
    from sqlmodel import SQLModel
    # Create tables for the original todo application
    SQLModel.metadata.create_all(engine)