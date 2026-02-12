from datetime import datetime
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg


class Agent_Response(SQLModel, table=True):
    """
    Represents AI-generated response to the user's natural language request.
    """
    __tablename__ = "agent_responses"

    response_id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    session_id: UUID = Field(foreign_key="ai_agent_sessions.session_id", nullable=False)
    content: str = Field(max_length=2000, nullable=False)  # AI agent's response
    timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    request_id: UUID = Field(foreign_key="user_requests.request_id", nullable=False)