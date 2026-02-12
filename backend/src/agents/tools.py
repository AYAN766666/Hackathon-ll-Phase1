"""
MCP Tools for the AI Agent - This module defines the specific tools that the AI agent can use.
Each tool corresponds to a specific function that interacts with the existing Todo API.
"""
from typing import Dict, Any, Optional
from uuid import UUID
from sqlmodel import Session
from ..models.mcp_tool_call import MCP_Tool_Call
from ..models.ai_agent_session import AI_Agent_Session
from ..services.todo_services import TodoService
from ..models.task import TaskCreate, TaskUpdate
import json
from datetime import datetime


class MCPTaskTools:
    """
    Collection of MCP tools that the AI agent can use to perform todo operations.
    Each tool maps to an existing API endpoint.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.todo_service = TodoService(db_session)

    async def create_task(self, session_id: UUID, request_id: UUID, **kwargs) -> Dict[str, Any]:
        """
        Tool to create a new task.
        Maps to POST /api/{user_id}/tasks
        """
        # Create tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="create_task",
            parameters=json.dumps(kwargs),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get user_id from session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            # Create the todo
            todo_create = TaskCreate(
                title=kwargs.get("title", "Untitled Task"),
                description=kwargs.get("description", ""),
            )
            created_todo = self.todo_service.create_todo(todo_create, user_id)

            # Update tool call result
            tool_call.result = json.dumps({
                "task_id": created_todo.id,
                "title": created_todo.title,
                "description": created_todo.description
            })
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": True,
                "result": {
                    "task_id": created_todo.id,
                    "title": created_todo.title
                },
                "message": f"Task '{created_todo.title}' created successfully"
            }
        except Exception as e:
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": False,
                "error": str(e),
                "message": f"Failed to create task: {str(e)}"
            }

    async def list_tasks(self, session_id: UUID, request_id: UUID, **kwargs) -> Dict[str, Any]:
        """
        Tool to list all tasks for the user.
        Maps to GET /api/{user_id}/tasks
        """
        # Create tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="list_tasks",
            parameters=json.dumps(kwargs),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get user_id from session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            # Get user's tasks
            todos = self.todo_service.get_user_todos(user_id)

            # Update tool call result
            tool_call.result = json.dumps([{
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "completed": todo.completed
            } for todo in todos])
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": True,
                "result": [{
                    "id": todo.id,
                    "title": todo.title,
                    "completed": todo.completed,
                    "description": todo.description
                } for todo in todos],
                "message": f"Retrieved {len(todos)} tasks"
            }
        except Exception as e:
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": False,
                "error": str(e),
                "message": f"Failed to list tasks: {str(e)}"
            }

    async def update_task(self, session_id: UUID, request_id: UUID, **kwargs) -> Dict[str, Any]:
        """
        Tool to update a task.
        Maps to PUT /api/{user_id}/tasks/{id}
        """
        # Create tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="update_task",
            parameters=json.dumps(kwargs),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get user_id from session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            task_id = kwargs.get("id")
            if not task_id:
                raise ValueError("Task ID is required for update operation")

            # Prepare update data
            update_data = TaskUpdate()
            if kwargs.get("title"):
                update_data.title = kwargs["title"]
            if kwargs.get("description"):
                update_data.description = kwargs["description"]
            if "completed" in kwargs:
                update_data.completed = kwargs["completed"]

            # Update the task
            updated_todo = self.todo_service.update_todo(task_id, user_id, update_data)

            # Update tool call result
            tool_call.result = json.dumps({
                "id": updated_todo.id,
                "title": updated_todo.title,
                "description": updated_todo.description,
                "completed": updated_todo.completed
            })
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": True,
                "result": {
                    "id": updated_todo.id,
                    "title": updated_todo.title,
                    "completed": updated_todo.completed
                },
                "message": f"Task '{updated_todo.title}' updated successfully"
            }
        except ValueError as ve:
            # Handle value errors (like invalid task ID format)
            tool_call.result = json.dumps({"error": str(ve)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": False,
                "error": str(ve),
                "message": f"Invalid request: {str(ve)}"
            }
        except Exception as e:
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            # Check if it's a task not found error
            error_msg = str(e).lower()
            if "not found" in error_msg or "does not exist" in error_msg:
                return {
                    "success": False,
                    "error": str(e),
                    "message": f"Task with that ID was not found. Please check the task ID and try again."
                }
            else:
                return {
                    "success": False,
                    "error": str(e),
                    "message": f"Failed to update task: {str(e)}"
                }

    async def delete_task(self, session_id: UUID, request_id: UUID, **kwargs) -> Dict[str, Any]:
        """
        Tool to delete a task.
        Maps to DELETE /api/{user_id}/tasks/{id}
        """
        # Create tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="delete_task",
            parameters=json.dumps(kwargs),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get user_id from session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            task_id = kwargs.get("id")
            if not task_id:
                raise ValueError("Task ID is required for delete operation")

            # Delete the task
            deleted_todo = self.todo_service.delete_todo(task_id, user_id)

            # Update tool call result
            tool_call.result = json.dumps({
                "id": deleted_todo.id,
                "title": deleted_todo.title
            })
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": True,
                "result": {
                    "id": deleted_todo.id,
                    "title": deleted_todo.title
                },
                "message": f"Task '{deleted_todo.title}' deleted successfully"
            }
        except ValueError as ve:
            # Handle value errors (like invalid task ID format)
            tool_call.result = json.dumps({"error": str(ve)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": False,
                "error": str(ve),
                "message": f"Invalid request: {str(ve)}"
            }
        except Exception as e:
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            # Check if it's a task not found error
            error_msg = str(e).lower()
            if "not found" in error_msg or "does not exist" in error_msg:
                return {
                    "success": False,
                    "error": str(e),
                    "message": f"Task with that ID was not found. Please check the task ID and try again."
                }
            else:
                return {
                    "success": False,
                    "error": str(e),
                    "message": f"Failed to delete task: {str(e)}"
                }

    async def complete_task(self, session_id: UUID, request_id: UUID, **kwargs) -> Dict[str, Any]:
        """
        Tool to complete a task.
        Maps to PATCH /api/{user_id}/tasks/{id}/complete
        """
        # Create tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="complete_task",
            parameters=json.dumps(kwargs),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get user_id from session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            task_id = kwargs.get("id")
            completed = kwargs.get("completed", True)
            if not task_id:
                raise ValueError("Task ID is required for complete operation")

            # Update the task completion status
            update_data = TaskUpdate(completed=completed)
            updated_todo = self.todo_service.update_todo(task_id, user_id, update_data)

            status_word = "completed" if completed else "marked as incomplete"

            # Update tool call result
            tool_call.result = json.dumps({
                "id": updated_todo.id,
                "title": updated_todo.title,
                "completed": updated_todo.completed
            })
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": True,
                "result": {
                    "id": updated_todo.id,
                    "title": updated_todo.title,
                    "completed": updated_todo.completed
                },
                "message": f"Task '{updated_todo.title}' has been {status_word}"
            }
        except ValueError as ve:
            # Handle value errors (like invalid task ID format)
            tool_call.result = json.dumps({"error": str(ve)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "success": False,
                "error": str(ve),
                "message": f"Invalid request: {str(ve)}"
            }
        except Exception as e:
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            # Check if it's a task not found error
            error_msg = str(e).lower()
            if "not found" in error_msg or "does not exist" in error_msg:
                return {
                    "success": False,
                    "error": str(e),
                    "message": f"Task with that ID was not found. Please check the task ID and try again."
                }
            else:
                return {
                    "success": False,
                    "error": str(e),
                    "message": f"Failed to update task completion: {str(e)}"
                }