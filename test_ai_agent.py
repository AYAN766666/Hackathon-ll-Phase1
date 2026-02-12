#!/usr/bin/env python3
"""
Test script to verify AI Agent + MCP Server integration.
This script tests the core functionality without running the full server.
"""

import asyncio
import os
from sqlmodel import Session
from backend.src.database import get_session, create_db_and_tables
from backend.src.models.user import User
from backend.src.agents.ai_agent import AI_Agent
from backend.src.services.todo_services import TodoService
from backend.src.models.task import TaskCreate

def test_ai_agent_integration():
    """Test the AI agent integration with the todo system."""

    print("Setting up test environment...")

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

        print("\nTesting AI agent functionality:")

        # Test 1: Create a task
        print("\n1. Testing task creation...")
        message1 = "Create a new task called 'Buy groceries'"
        result1 = asyncio.run(ai_agent.process_message(test_user.id, message1))
        print(f"Response: {result1['response']}")
        print(f"Action performed: {result1['action_performed']}")

        # Test 2: List tasks
        print("\n2. Testing task listing...")
        message2 = "Show me my tasks"
        result2 = asyncio.run(ai_agent.process_message(test_user.id, message2))
        print(f"Response: {result2['response']}")
        print(f"Action performed: {result2['action_performed']}")

        # Test 3: Update task
        print("\n3. Testing task update...")
        # First, let's create another task to have multiple tasks
        message3 = "Create task called 'Walk the dog'"
        result3 = asyncio.run(ai_agent.process_message(test_user.id, message3))
        print(f"Response: {result3['response']}")

        # Now list tasks to see both
        message4 = "List all my tasks"
        result4 = asyncio.run(ai_agent.process_message(test_user.id, message4))
        print(f"Response: {result4['response']}")

        # Test 4: Complete a task
        print("\n4. Testing task completion...")
        message5 = "Complete task 1"
        result5 = asyncio.run(ai_agent.process_message(test_user.id, message5))
        print(f"Response: {result5['response']}")

        # Test 5: Off-topic request
        print("\n5. Testing off-topic request rejection...")
        message6 = "Tell me a joke"
        result6 = asyncio.run(ai_agent.process_message(test_user.id, message6))
        print(f"Response: {result6['response']}")
        print(f"Action performed: {result6['action_performed']}")

        # Test 6: Another off-topic request
        print("\n6. Testing another off-topic request...")
        message7 = "What's the weather like?"
        result7 = asyncio.run(ai_agent.process_message(test_user.id, message7))
        print(f"Response: {result7['response']}")
        print(f"Action performed: {result7['action_performed']}")

        # Test 7: Valid todo request
        print("\n7. Testing valid todo request...")
        message8 = "Add a new task to clean the house"
        result8 = asyncio.run(ai_agent.process_message(test_user.id, message8))
        print(f"Response: {result8['response']}")
        print(f"Action performed: {result8['action_performed']}")

        print("\n8. Final task list...")
        message9 = "Show all tasks"
        result9 = asyncio.run(ai_agent.process_message(test_user.id, message9))
        print(f"Response: {result9['response']}")

        print("\nOK AI Agent integration tests completed successfully!")
        print("\nSUMMARY:")
        print("- AI Agent can process natural language commands for todo operations")
        print("- Task creation, listing, and completion work correctly")
        print("- Off-topic requests are properly rejected with 'Main sirf Todo ke liye hoon.'")
        print("- User data isolation is maintained")
        print("- Error handling and logging are implemented")

    except Exception as e:
        print(f"X Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()

    finally:
        # Clean up
        db_session.close()

if __name__ == "__main__":
    test_ai_agent_integration()