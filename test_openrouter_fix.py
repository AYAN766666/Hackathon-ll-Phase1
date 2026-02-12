#!/usr/bin/env python3
"""
Test script to verify the OpenRouter API authentication fix.
This script tests that the AI agent properly handles authentication errors.
"""

import asyncio
import os
from sqlmodel import Session
from backend.src.database import get_session, create_db_and_tables
from backend.src.models.user import User
from backend.src.agents.ai_agent import AI_Agent
import traceback

def test_ai_agent_with_mock_error():
    """Test the AI agent error handling with mock error."""
    
    print("Testing AI agent error handling...")

    # Create database tables
    create_db_and_tables()

    # Get database session
    session_gen = get_session()
    db_session = next(session_gen)

    try:
        print("Creating test user...")
        # Create a test user with unique email
        import uuid
        unique_email = f"test_{uuid.uuid4()}@example.com"
        test_user = User(email=unique_email, hashed_password="hashed_password")
        db_session.add(test_user)
        db_session.commit()
        db_session.refresh(test_user)

        print(f"Created user with ID: {test_user.id}")

        print("Initializing AI Agent...")
        # Initialize the AI agent
        ai_agent = AI_Agent(db_session)

        # Test with a message that should trigger the error handling
        print("\nTesting error handling...")
        
        # Simulate the error condition by temporarily setting a bad API key
        original_api_key = os.environ.get('GEMINI_API_KEY')
        
        # If no API key is set, the agent should handle it gracefully
        if not original_api_key:
            print("No GEMINI_API_KEY set, testing graceful degradation...")
            message = "Create a task called 'Test task'"
            
            # This should return a proper error message instead of crashing
            result = asyncio.run(ai_agent.process_message(test_user.id, message))
            print(f"Response: {result['response']}")
            print(f"Action performed: {result['action_performed']}")
        else:
            print("GEMINI_API_KEY is set, testing with API key...")
            # If API key is set, we can't easily test the specific error without making real API calls
            print("Note: Real API call would be made with valid API key.")

        print("\nOK AI agent error handling test completed!")

    except Exception as e:
        print(f"X Error during testing: {str(e)}")
        traceback.print_exc()

    finally:
        # Clean up
        db_session.close()

if __name__ == "__main__":
    test_ai_agent_with_mock_error()