from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg


class MCP_Tool_Call(SQLModel, table=True):
    """
    Represents structured API call made by the AI agent through the MCP server to backend services.
    """
    __tablename__ = "mcp_tool_calls"

    call_id: UUID = Field(default_factory=uuid4, primary_key=True, nullable=False)
    session_id: UUID = Field(foreign_key="ai_agent_sessions.session_id", nullable=False)
    request_id: UUID = Field(foreign_key="user_requests.request_id", nullable=False)
    tool_name: str = Field(nullable=False)  # create_task, list_tasks, update_task, delete_task, complete_task
    parameters: str = Field(default="{}")  # JSON string
    result: Optional[str] = Field(default=None)  # JSON string
    timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    status: str = Field(default="initiated", nullable=False)  # initiated, success, failed, error