"""
Todo Service for the AI Agent and MCP Server integration.
Provides methods for creating, reading, updating, and deleting todo items.
"""
from sqlmodel import Session, select
from typing import List, Optional
from ..models.task import Task, TaskCreate, TaskUpdate
from ..models.user import User
from ..schemas.todo_schemas import TodoCreate, TodoUpdate
from fastapi import HTTPException, status


class TodoService:
    """
    Service class for handling todo operations.
    Maps to existing FastAPI Todo APIs to maintain compatibility.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_todo(self, todo_create: TaskCreate, user_id: int) -> Task:
        """
        Create a new todo item.
        Maps to POST /api/{user_id}/tasks
        """
        # Create the task with the user_id
        db_task = Task(
            title=todo_create.title,
            description=todo_create.description or "",
            completed=getattr(todo_create, 'completed', False),  # Default to not completed
            user_id=user_id
        )

        self.db_session.add(db_task)
        self.db_session.commit()
        self.db_session.refresh(db_task)

        return db_task

    def get_user_todos(self, user_id: int) -> List[Task]:
        """
        Get all todos for a specific user.
        Maps to GET /api/{user_id}/tasks
        """
        todos = self.db_session.exec(
            select(Task).where(Task.user_id == user_id)
        ).all()

        return todos

    def get_todo_by_id(self, todo_id: int, user_id: int) -> Optional[Task]:
        """
        Get a specific todo by ID for a specific user.
        Maps to GET /api/{user_id}/tasks/{id}
        """
        todo = self.db_session.exec(
            select(Task).where(Task.id == todo_id, Task.user_id == user_id)
        ).first()

        return todo

    def update_todo(self, todo_id: int, user_id: int, todo_update: TodoUpdate) -> Task:
        """
        Update a specific todo for a user.
        Maps to PUT /api/{user_id}/tasks/{id}
        """
        todo = self.db_session.exec(
            select(Task).where(Task.id == todo_id, Task.user_id == user_id)
        ).first()

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Update task fields
        update_data = todo_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            if hasattr(todo, field):
                setattr(todo, field, value)

        self.db_session.add(todo)
        self.db_session.commit()
        self.db_session.refresh(todo)

        return todo

    def delete_todo(self, todo_id: int, user_id: int) -> Task:
        """
        Delete a specific todo for a user.
        Maps to DELETE /api/{user_id}/tasks/{id}
        """
        todo = self.db_session.exec(
            select(Task).where(Task.id == todo_id, Task.user_id == user_id)
        ).first()

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Store the todo for returning before deletion
        todo_to_return = todo

        self.db_session.delete(todo)
        self.db_session.commit()

        return todo_to_return

    def toggle_todo_completion(self, todo_id: int, user_id: int, completed: bool) -> Task:
        """
        Toggle the completion status of a specific todo for a user.
        Maps to PATCH /api/{user_id}/tasks/{id}/complete
        """
        todo = self.db_session.exec(
            select(Task).where(Task.id == todo_id, Task.user_id == user_id)
        ).first()

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        todo.completed = completed

        self.db_session.add(todo)
        self.db_session.commit()
        self.db_session.refresh(todo)

        return todo