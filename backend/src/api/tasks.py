
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from ..database import get_session
from ..models.task import TaskCreate, TaskUpdate
from ..schemas.task import TaskResponse
from ..services.task_service import TaskService
from ..utils.auth import get_current_user
from ..models.user import User

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(
    task_create: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Create a new task for the current user."""
    return TaskService.create_task(session, task_create, current_user.id)

@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get all tasks for the current user."""
    return TaskService.get_tasks_by_user(session, current_user.id)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update a specific task for the current user."""
    return TaskService.update_task(session, task_id, task_update, current_user.id)

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Delete a specific task for the current user."""
    TaskService.delete_task(session, task_id, current_user.id)
    return {"message": "Task deleted successfully"}

@router.patch("/{task_id}/complete")
def toggle_task_completion(
    task_id: int,
    completed: bool,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a specific task for the current user."""
    task = TaskService.toggle_task_completion(session, task_id, current_user.id, completed)
    return {"id": task.id, "title": task.title, "completed": task.completed, "user_id": task.user_id}