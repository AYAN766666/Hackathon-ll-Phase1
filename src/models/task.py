"""
Task model representing a todo item.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a todo task with id, title, description, and completion status.
    """
    id: int
    title: str
    description: Optional[str] = ""
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title is required and cannot be empty")