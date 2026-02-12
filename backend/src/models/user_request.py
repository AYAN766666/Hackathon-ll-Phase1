from datetime import datetime
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg


class User_Request(SQLModel, table=True):
    """
    Represents natural language input from the user to the AI agent requesting todo operations.
    """
    __tablename__ = "user_requests"

    request_id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    session_id: UUID = Field(foreign_key="ai_agent_sessions.session_id", nullable=False)
    content: str = Field(max_length=2000, nullable=False)  # Natural language content
    timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    processed_status: str = Field(default="pending", nullable=False)  # pending, processing, completed, failed