from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg


class AI_Agent_Session(SQLModel, table=True):
    """
    Represents a user's interaction session with the AI agent, including conversation history.
    """
    __tablename__ = "ai_agent_sessions"

    session_id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    conversation_history: Optional[str] = Field(default=None)  # JSON string
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    last_interaction_at: Optional[datetime] = Field(default=None)