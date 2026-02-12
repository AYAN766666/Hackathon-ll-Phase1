from sqlmodel import Session, select
from typing import List, Optional
from ..models.task import Task, TaskCreate, TaskUpdate
from ..models.user import User
from fastapi import HTTPException, status

class TaskService:
    @staticmethod
    def create_task(session: Session, task_create: TaskCreate, user_id: int) -> Task:
        """Create a new task for a user."""
        # Create the task with the user_id
        db_task = Task(
            title=task_create.title,
            description=task_create.description,
            completed=task_create.completed,
            user_id=user_id
        )

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        return db_task

    @staticmethod
    def get_tasks_by_user(session: Session, user_id: int) -> List[Task]:
        """Get all tasks for a specific user."""
        tasks = session.exec(select(Task).where(Task.user_id == user_id)).all()
        return tasks

    @staticmethod
    def get_task_by_id(session: Session, task_id: int, user_id: int) -> Optional[Task]:
        """Get a specific task by ID for a specific user."""
        task = session.exec(
            select(Task).where(Task.id == task_id, Task.user_id == user_id)
        ).first()
        return task

    @staticmethod
    def update_task(session: Session, task_id: int, task_update: TaskUpdate, user_id: int) -> Optional[Task]:
        """Update a specific task for a user."""
        task = session.exec(
            select(Task).where(Task.id == task_id, Task.user_id == user_id)
        ).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        # Update task fields
        for field, value in task_update.dict(exclude_unset=True).items():
            setattr(task, field, value)

        session.add(task)
        session.commit()
        session.refresh(task)

        return task

    @staticmethod
    def delete_task(session: Session, task_id: int, user_id: int) -> bool:
        """Delete a specific task for a user."""
        task = session.exec(
            select(Task).where(Task.id == task_id, Task.user_id == user_id)
        ).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        session.delete(task)
        session.commit()

        return True

    @staticmethod
    def toggle_task_completion(session: Session, task_id: int, user_id: int, completed: bool) -> Optional[Task]:
        """Toggle the completion status of a specific task for a user."""
        task = session.exec(
            select(Task).where(Task.id == task_id, Task.user_id == user_id)
        ).first()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )

        task.completed = completed

        session.add(task)
        session.commit()
        session.refresh(task)

        return task