
import logging
from typing import Dict, Any
from datetime import datetime
import traceback

from agents import Agent  # Keep Agent for potential future use

from sqlmodel import Session
from ..models.ai_agent_session import AI_Agent_Session
from ..models.user_request import User_Request
from ..models.agent_response import Agent_Response
from .mcp_server import MCPServer
from ..config import Config

logger = logging.getLogger(__name__)

# ================= CONFIG =================

class AI_Agent_Configuration:
    def __init__(self):
        # No API key required - using local rule-based parsing instead of external AI
        self.model = None  # No model needed for local parsing
        self.run_config = None  # No run config needed for local parsing
        logger.info("AI agent configured with local rule-based parsing (no external API required)")

# ================= AGENT =================

class AI_Agent:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.config = AI_Agent_Configuration()
        self.mcp_server = MCPServer(db_session)
        # Keep the agent attribute for potential future use but set to None
        self.agent = None

    async def process_message(self, user_id: int, message: str) -> Dict[str, Any]:
        logger.info(f"AI message from user {user_id}: {message}")

        # Create AI session
        session = self._create_session(user_id)

        # Save user request
        user_request = User_Request(
            session_id=session.session_id,
            content=message,
            timestamp=datetime.utcnow(),
            processed_status="processing",
        )
        self.db_session.add(user_request)
        self.db_session.commit()
        self.db_session.refresh(user_request)

        # Local rule-based parser to determine ai_command
        message_lower = message.lower().strip()

        if "add" in message_lower:
            # Treat the full message as ai_command for adding tasks
            ai_command = message
        elif "delete" in message_lower:
            # Treat the full message as ai_command for deleting tasks
            ai_command = message
        elif "update" in message_lower or "edit" in message_lower:
            # Treat the full message as ai_command for updating tasks
            ai_command = message
        elif "show" in message_lower or "view" in message_lower:
            # Set ai_command to "show my tasks" for displaying tasks
            ai_command = "show my tasks"
        else:
            # For any other message, return the specified response
            return {
                "response": "Main sirf Todo ke liye hoon.",
                "action_performed": False,
                "action_result": {}
            }

        try:
            # MCP processing
            todo_result = await self.mcp_server.process_todo_command(
                session.session_id,
                user_request.request_id,
                ai_command,
            )

            # Save agent response
            agent_response = Agent_Response(
                session_id=session.session_id,
                content=todo_result.get("response", ""),
                timestamp=datetime.utcnow(),
                request_id=user_request.request_id,
            )
            self.db_session.add(agent_response)

            user_request.processed_status = "completed"
            self.db_session.commit()

            return {
                "response": todo_result.get("response", ""),
                "action_performed": todo_result.get("action_performed", False),
                "action_result": todo_result.get("action_result", {}),
            }

        except Exception as e:
            traceback.print_exc()
            logger.error(f"AI Agent Error: {e}", exc_info=True)

            return {
                "response": f"Sorry, kuch error aa gaya: {str(e)}",
                "action_performed": False,
                "action_result": {},
            }

    def _create_session(self, user_id: int) -> AI_Agent_Session:
        session = AI_Agent_Session(
            user_id=user_id,
            created_at=datetime.utcnow(),
        )
        self.db_session.add(session)
        self.db_session.commit()
        self.db_session.refresh(session)
        return session
