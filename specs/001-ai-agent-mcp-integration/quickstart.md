# Quickstart Guide: AI Agent + MCP Server Integration

**Feature**: AI Agent + MCP Server Integration
**Date**: 2026-01-12
**Guide Version**: 1.0.0

## Overview

This guide provides step-by-step instructions to set up, configure, and run the AI Agent and MCP Server integration with the existing Todo application.

## Prerequisites

- Python 3.13 or higher
- Node.js 18 or higher
- uv package manager (for Python dependencies)
- GEMINI_API_KEY environment variable with valid Gemini API key
- Existing Phase II Todo application setup

## Setup Instructions

### 1. Environment Setup

1. Clone or update the repository to include the AI Agent and MCP Server features
2. Navigate to the project directory

### 2. Backend Setup

1. Install Python dependencies using uv:
   ```bash
   cd backend
   uv venv  # Create virtual environment (optional but recommended)
   uv pip install openai fastapi uvicorn python-multipart python-jose[cryptography] passlib[bcrypt] sqlmodel sqlalchemy sqlite3
   ```

2. Set up environment variables:
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key-here"
   ```

3. Start the backend server:
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

### 3. Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### 4. Database Initialization

1. The system will automatically create the SQLite database file for AI agent operations when first accessed
2. The file will be created as `database/ai_agent_db.sqlite`

## Usage Instructions

### 1. Access the Application

1. Open your browser and navigate to `http://localhost:3000`
2. Register or log in with existing credentials
3. You'll be directed to the dashboard

### 2. Using the AI Agent

1. On the dashboard page, locate the blue AI agent icon (🔵) in the interface
2. Click the icon to open the AI agent panel with white background (⚪)
3. Type natural language commands related to todo operations:
   - "Add a task called 'Buy groceries'"
   - "Show me my tasks"
   - "Complete task 1"
   - "Delete task 'Old task'"
   - "Edit task 'Old task' to 'Updated task'"

### 3. Expected Behavior

- The AI agent will respond to todo-related commands
- Off-topic requests will be politely rejected with "Main sirf Todo ke liye hoon."
- All operations will be tied to your authenticated user account
- Task operations will appear in your existing task list

## Configuration

### Environment Variables

Required:
- `GEMINI_API_KEY`: Your Google Gemini API key for AI processing

Optional:
- `AI_AGENT_PORT`: Port for the AI agent service (default: 8000)
- `DATABASE_URL`: Path to SQLite database (default: ./database/ai_agent_db.sqlite)

## Troubleshooting

### Common Issues

1. **AI Agent not responding**
   - Verify GEMINI_API_KEY is set correctly
   - Check backend server is running

2. **Authentication errors**
   - Ensure JWT token is valid and not expired
   - Log out and log back in if needed

3. **Database connection errors**
   - Verify database permissions
   - Check that the database directory exists

### Error Messages

- `401 Unauthorized`: Invalid or expired JWT token - log in again
- `403 Forbidden`: Action not permitted for this user
- `500 Internal Server Error`: Contact administrator

## Verification Steps

To verify the installation was successful:

1. Log into the application
2. Open the AI agent panel
3. Try adding a task with "Add a task called 'Test'"
4. Verify the task appears in your task list
5. Try other commands like "Show me my tasks" or "Complete task 1"
6. Verify off-topic requests are rejected with appropriate messaging

## Next Steps

- Customize AI agent responses if needed
- Monitor AI agent usage and responses
- Implement additional analytics for AI agent interactions