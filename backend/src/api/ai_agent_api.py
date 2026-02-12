from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Dict, Any
from pydantic import BaseModel
from ..database import get_session
from ..middleware.auth import get_current_user
from ..models.user import User
from ..agents.ai_agent import AI_Agent
import asyncio
import logging


class AIRequest(BaseModel):
    message: str

# Set up logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ai-agent", tags=["AI Agent"])


@router.post("/message")
async def send_ai_agent_message(
    request: AIRequest,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
) -> Dict[str, Any]:
    """
    Send a message to the AI agent for processing.
    The AI agent will interpret the natural language command and perform appropriate todo operations.
    """
    try:
        # Check if current_user is valid (this is handled by get_current_user dependency)
        if not current_user:
            logger.warning("Attempt to access AI agent with invalid JWT token")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired JWT token"
            )

        # Initialize the AI agent with the database session
        ai_agent = AI_Agent(db_session)

        # Process the message
        result = await ai_agent.process_message(current_user.id, request.message)

        return result
    except HTTPException as he:
        # Log the HTTP exception
        logger.warning(f"HTTP error in AI agent request: {he.detail}")
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log any other errors
        logger.error(f"Unexpected error in AI agent request: {str(e)}", exc_info=True)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing AI agent request: {str(e)}"
        )


@router.get("/health")
async def ai_agent_health_check():
    """
    Health check endpoint for the AI agent service.
    """
    return {"status": "healthy", "service": "AI Agent"}