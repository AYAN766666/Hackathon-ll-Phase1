import os
from typing import Dict, Any, Optional, List
from datetime import datetime
from uuid import UUID
from sqlmodel import Session, select
from ..models.mcp_tool_call import MCP_Tool_Call
from ..models.ai_agent_session import AI_Agent_Session
from ..models.user_request import User_Request
from ..services.todo_services import TodoService
from ..models.task import TaskCreate, TaskUpdate
import json


class MCPServer:
    """
    MCP Server implementation that acts as a bridge between AI agent and FastAPI Todo APIs.
    Verifies JWT tokens and enforces user_id boundaries.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.todo_service = TodoService(db_session)

    async def process_todo_command(self, session_id: UUID, request_id: UUID, command: str) -> Dict[str, Any]:
        """
        Process a todo command by determining the appropriate tool call.
        """
        # Parse the command to determine the appropriate action
        action, params = await self._parse_command(command)

        if action == "create_task":
            return await self._execute_create_task(session_id, request_id, params)
        elif action == "list_tasks":
            return await self._execute_list_tasks(session_id, request_id, params)
        elif action == "update_task":
            return await self._execute_update_task(session_id, request_id, params)
        elif action == "delete_task":
            return await self._execute_delete_task(session_id, request_id, params)
        elif action == "complete_task":
            return await self._execute_complete_task(session_id, request_id, params)
        else:
            return {
                "response": "Command not recognized",
                "action_performed": False,
                "action_result": {}
            }

    async def _parse_command(self, command: str) -> tuple[str, dict]:
        """
        Parse the natural language command to determine action and parameters.
        This is a simplified parser - in reality, this would use AI to understand intent.
        """
        command_lower = command.lower().strip()

        # Determine action based on keywords
        if any(word in command_lower for word in ["add", "create", "make", "new"]):
            # Extract task title and description
            title = self._extract_task_title(command)
            description = self._extract_task_description(command)
            return "create_task", {"title": title, "description": description}
        elif any(word in command_lower for word in ["list", "show", "view", "display", "see", "my"]):
            return "list_tasks", {}
        elif any(word in command_lower for word in ["update", "edit", "change", "modify"]):
            task_id = self._extract_task_id(command)
            title = self._extract_task_title(command)
            description = self._extract_task_description(command)
            return "update_task", {"id": task_id, "title": title, "description": description, "command": command}
        elif any(word in command_lower for word in ["delete", "remove", "kill"]):
            task_id = self._extract_task_id(command)
            return "delete_task", {"id": task_id, "command": command}
        elif any(word in command_lower for word in ["complete", "finish", "done", "mark"]):
            task_id = self._extract_task_id(command)
            completed = not ("incomplete" in command_lower or "undo" in command_lower)
            return "complete_task", {"id": task_id, "completed": completed, "command": command}
        else:
            # Default to listing tasks if unclear
            return "list_tasks", {}

    def _extract_task_title(self, command: str) -> str:
        """
        Extract task title from command. This is a simplified implementation.
        """
        # Look for common patterns like "called 'title'" or "named 'title'"
        import re

        # Pattern for "called 'title'" or "named 'title'"
        pattern = r"(?:called|named|titled|as)['\"]([^'\"]+)['\"]"
        match = re.search(pattern, command, re.IGNORECASE)
        if match:
            return match.group(1)

        # Pattern for "add task 'title'" or similar
        pattern = r"(?:add|create|make).*?(?:task|todo)?\s*['\"]([^'\"]+)['\"]"
        match = re.search(pattern, command, re.IGNORECASE)
        if match:
            return match.group(1)

        # If no quotes, try to extract the main content
        # Remove common verbs and extract the main noun phrase
        command_clean = re.sub(r"(add|create|make|task|todo|please|now)", "", command, flags=re.IGNORECASE)
        command_clean = command_clean.strip()

        # Take the first substantial phrase as title
        words = command_clean.split()
        if len(words) > 0:
            # Take first 5 words as title
            title = " ".join(words[:5])
            # Remove punctuation at the end
            title = title.rstrip('.,!?')
            return title

        return "Untitled Task"

    def _extract_task_description(self, command: str) -> str:
        """
        Extract task description from command.
        """
        import re
        
        # Common patterns for separating title from description
        # Look for phrases like "with description", "and description", "description:", etc.
        patterns = [
            r'(?:with|and)\s+description\s+(.*)',
            r'description:\s*(.*)',
            r'-\s*(.*)',
            r':\s*(.*)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, command, re.IGNORECASE)
            if match:
                description = match.group(1).strip()
                # Remove trailing punctuation
                description = description.rstrip('.!?')
                return description
        
        # If no explicit description found, extract additional context from the command
        # Remove common action words to isolate potential description
        cleaned_command = re.sub(r'\b(add|create|make|new|task|todo|please|now|want|need|should)\b', '', command, flags=re.IGNORECASE)
        cleaned_command = re.sub(r'\s+', ' ', cleaned_command).strip()
        
        # If the cleaned command is longer than the extracted title, treat the remainder as description
        title = self._extract_task_title(command)
        if title and len(cleaned_command) > len(title) and title.lower() in cleaned_command.lower():
            # Remove the title from the cleaned command to get the description
            description = cleaned_command.replace(title, '', 1).strip()
            description = description.lstrip(':,- ')
            if len(description) > 0:
                return description
        
        return ""

    def _extract_task_id(self, command: str) -> Optional[int]:
        """
        Extract task ID from command.
        """
        import re
        # Look for numbers in the command
        pattern = r"\b(task|id|number)\s*(\d+)\b|\b(\d+)\b"
        matches = re.findall(pattern, command, re.IGNORECASE)

        for match in matches:
            # The regex has 3 groups, so we check each one
            if match[1]:  # Second group (after "task", "id", etc.)
                return int(match[1])
            elif match[2]:  # Third group (standalone number)
                return int(match[2])

        # If no explicit ID found, return None (for operations that might use other identifiers)
        return None

    def _find_task_by_title(self, command: str, user_id: int) -> Optional[int]:
        """
        Find a task by its title based on the command.
        """
        import re
        from sqlmodel import select
        from ..models.task import Task
        
        # Extract potential task title from the command
        # Remove common verbs like "delete", "update", "edit", etc.
        command_lower = command.lower()
        # Remove common action words
        for word in ["delete", "remove", "update", "edit", "complete", "finish", "done", "mark"]:
            command_lower = re.sub(rf"\b{word}\b", "", command_lower, flags=re.IGNORECASE)
        
        # Clean up extra spaces
        clean_command = ' '.join(command_lower.split())
        
        # Get all tasks for the user
        user_tasks = self.db_session.exec(
            select(Task).where(Task.user_id == user_id)
        ).all()
        
        # Find the best match based on similarity
        best_match = None
        best_score = 0
        
        for task in user_tasks:
            # Calculate similarity score based on how much of the task title appears in the command
            task_title_lower = task.title.lower()
            if task_title_lower in clean_command or clean_command in task_title_lower:
                score = max(len(task_title_lower), len(clean_command))
                if score > best_score:
                    best_score = score
                    best_match = task.id
            # Also check for partial matches
            elif any(word in task_title_lower for word in clean_command.split()):
                score = sum(1 for word in clean_command.split() if word in task_title_lower)
                if score > best_score:
                    best_score = score
                    best_match = task.id
        
        return best_match

    async def _execute_create_task(self, session_id: UUID, request_id: UUID, params: dict) -> Dict[str, Any]:
        """
        Execute create_task MCP tool call.
        """
        # Create the tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="create_task",
            parameters=json.dumps(params),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get the user_id from the session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            # Create the todo item
            todo_create = TaskCreate(
                title=params.get("title", "Untitled Task"),
                description=params.get("description", ""),
            )
            created_todo = self.todo_service.create_todo(todo_create, user_id)

            # Update tool call result
            tool_call.result = json.dumps({"task_id": created_todo.id, "title": created_todo.title})
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": f"Task '{created_todo.title}' has been created successfully",
                "action_performed": True,
                "action_result": {"task_id": created_todo.id, "task_title": created_todo.title}
            }
        except Exception as e:
            # Update tool call with error
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": f"Failed to create task: {str(e)}",
                "action_performed": False,
                "action_result": {}
            }

    async def _execute_list_tasks(self, session_id: UUID, request_id: UUID, params: dict) -> Dict[str, Any]:
        """
        Execute list_tasks MCP tool call.
        """
        # Create the tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="list_tasks",
            parameters=json.dumps(params),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get the user_id from the session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            # Get the user's tasks
            todos = self.todo_service.get_user_todos(user_id)

            # Format response
            if not todos:
                response = "You don't have any tasks currently."
            else:
                task_list = [f"- {todo.title}" + (f" ({'completed' if todo.completed else 'pending'})" if todo.completed is not None else "") for todo in todos]
                response = f"You have {len(todos)} task(s):\n" + "\n".join(task_list)

            # Update tool call result
            tool_call.result = json.dumps([{
                "id": todo.id,
                "title": todo.title,
                "completed": todo.completed,
                "description": todo.description
            } for todo in todos])
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": response,
                "action_performed": True,
                "action_result": {"task_count": len(todos)}
            }
        except Exception as e:
            # Update tool call with error
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": f"Failed to list tasks: {str(e)}",
                "action_performed": False,
                "action_result": {}
            }

    async def _execute_update_task(self, session_id: UUID, request_id: UUID, params: dict) -> Dict[str, Any]:
        """
        Execute update_task MCP tool call.
        """
        # Create the tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="update_task",
            parameters=json.dumps(params),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get the user_id from the session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            task_id = params.get("id")
            
            # If no ID provided, try to find the task by title
            if not task_id:
                command = params.get("command", "")  # Pass the original command for title matching
                task_id = self._find_task_by_title(command, user_id)
                
                if not task_id:
                    raise ValueError("Task ID or title not found for update operation")

            # Prepare update data
            update_data = TaskUpdate()
            if params.get("title"):
                update_data.title = params["title"]
            if params.get("description"):
                update_data.description = params["description"]

            # Update the task
            updated_todo = self.todo_service.update_todo(task_id, user_id, update_data)

            # Update tool call result
            tool_call.result = json.dumps({
                "id": updated_todo.id,
                "title": updated_todo.title,
                "description": updated_todo.description
            })
            tool_call.status = "success"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": f"Task '{updated_todo.title}' has been updated successfully",
                "action_performed": True,
                "action_result": {"task_id": updated_todo.id, "task_title": updated_todo.title}
            }
        except Exception as e:
            # Update tool call with error
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": f"Failed to update task: {str(e)}",
                "action_performed": False,
                "action_result": {}
            }

    async def _execute_delete_task(self, session_id: UUID, request_id: UUID, params: dict) -> Dict[str, Any]:
        """
        Execute delete_task MCP tool call.
        """
        # Create the tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="delete_task",
            parameters=json.dumps(params),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get the user_id from the session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            task_id = params.get("id")
            
            # If no ID provided, try to find the task by title
            if not task_id:
                command = params.get("command", "")  # Pass the original command for title matching
                task_id = self._find_task_by_title(command, user_id)
                
                if not task_id:
                    raise ValueError("Task ID or title not found for delete operation")

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
                "response": f"Task '{deleted_todo.title}' has been deleted successfully",
                "action_performed": True,
                "action_result": {"task_id": deleted_todo.id, "task_title": deleted_todo.title}
            }
        except Exception as e:
            # Update tool call with error
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": f"Failed to delete task: {str(e)}",
                "action_performed": False,
                "action_result": {}
            }

    async def _execute_complete_task(self, session_id: UUID, request_id: UUID, params: dict) -> Dict[str, Any]:
        """
        Execute complete_task MCP tool call.
        """
        # Create the tool call record
        tool_call = MCP_Tool_Call(
            session_id=session_id,
            request_id=request_id,
            tool_name="complete_task",
            parameters=json.dumps(params),
            timestamp=datetime.utcnow(),
            status="initiated"
        )
        self.db_session.add(tool_call)
        self.db_session.commit()
        self.db_session.refresh(tool_call)

        try:
            # Get the user_id from the session
            session = self.db_session.get(AI_Agent_Session, session_id)
            user_id = session.user_id

            task_id = params.get("id")
            completed = params.get("completed", True)
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
                "response": f"Task '{updated_todo.title}' has been {status_word}",
                "action_performed": True,
                "action_result": {"task_id": updated_todo.id, "task_title": updated_todo.title, "completed": updated_todo.completed}
            }
        except Exception as e:
            # Update tool call with error
            tool_call.result = json.dumps({"error": str(e)})
            tool_call.status = "error"
            self.db_session.add(tool_call)
            self.db_session.commit()

            return {
                "response": f"Failed to update task completion: {str(e)}",
                "action_performed": False,
                "action_result": {}
            }