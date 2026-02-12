# Todo Application (CLI + Web API)

A comprehensive todo application with both CLI and web API interfaces, featuring AI-powered natural language processing for todo management.

## Features

- **CLI Interface**: Command-line interface for managing tasks
- **Web API**: RESTful API with authentication
- **AI Agent**: Natural language processing for todo commands
- **CRUD Operations**: Create, read, update, and delete tasks
- **Authentication**: JWT-based user authentication

### CLI Features
- **Add Tasks**: Create new tasks with titles and optional descriptions
- **View Tasks**: List all tasks with their completion status
- **Update Tasks**: Modify existing task titles and descriptions
- **Delete Tasks**: Remove tasks from your list
- **Toggle Completion**: Mark tasks as complete/incomplete

### Web API Features
- **Authentication**: Register and login endpoints
- **Task Management**: Full CRUD operations for tasks
- **AI Agent**: Natural language processing for todo commands

## Requirements

- Python 3.13 or higher
- UV package manager

## Installation

1. Clone or download the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
# Database
DATABASE_URL=sqlite:///./todo_app.db

# JWT Secret for authentication
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Gemini API Key (get one from Google AI Studio)
GEMINI_API_KEY=your-gemini-api-key-here
```

For the AI agent to work properly, you need to obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

## Usage

### CLI Application
Run the CLI application using:
```bash
python -m src.cli.main
```

The application provides a menu-driven interface:

1. **Add Task**: Enter a title (required) and description (optional) to create a new task
2. **View Tasks**: Display all tasks with their ID, title, status, and description
3. **Update Task**: Enter a task ID and provide new title/description values
4. **Delete Task**: Enter a task ID to remove a task
5. **Toggle Complete**: Enter a task ID to switch between complete/incomplete status
6. **Exit**: Quit the application

### Web API Server
Start the web API server:
```bash
python run_server.py
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /tasks/` - Get user's tasks
- `POST /tasks/` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task
- `POST /ai-agent/message` - Send message to AI agent

## Testing

Run the unit tests:
```bash
python -m pytest tests/unit/
```

Run the integration tests:
```bash
python -m pytest tests/integration/
```

Run all tests:
```bash
python -m pytest
```

## Architecture

The application follows a layered architecture:

- **Models**: Define data structures
- **Services**: Handle business logic
- **API**: Handle HTTP requests and responses
- **CLI**: Handle command-line interface
- **Agents**: Handle AI processing and external integrations

## Data Storage

The application uses SQLite database for persistent storage.

## Development

All code was generated using Claude Code following the Spec-Driven Development methodology. The implementation adheres to the architectural simplicity principle and functional completeness requirements defined in the project constitution.