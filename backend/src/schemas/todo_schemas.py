"""
Todo Schemas for the AI Agent and MCP Server integration.
Defines the data structures for todo operations.
"""
from pydantic import BaseModel
from typing import Optional


class TodoBase(BaseModel):
    """Base schema for todo items."""
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False


class TodoCreate(TodoBase):
    """Schema for creating a new todo item."""
    user_id: int

    class Config:
        from_attributes = True


class TodoUpdate(BaseModel):
    """Schema for updating a todo item."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        from_attributes = True


class Todo(TodoBase):
    """Schema for returning a todo item."""
    id: int
    user_id: int

    class Config:
        from_attributes = True