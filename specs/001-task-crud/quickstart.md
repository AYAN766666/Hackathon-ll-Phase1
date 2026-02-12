# Quickstart Guide: Task CRUD – Phase I (CLI Todo App)

**Date**: 2025-12-30
**Feature**: 001-task-crud
**Input**: Feature specification from `/specs/001-task-crud/spec.md`

## Getting Started

This guide provides instructions to set up and run the CLI Todo application.

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Setup Instructions

### 1. Clone or Create Project Directory
```bash
# Navigate to your project directory
cd your-project-directory
```

### 2. Initialize UV Project
```bash
# Initialize the project with UV
uv init
```

### 3. Project Structure
Create the following directory structure:
```
src/
├── models/
│   └── task.py
├── services/
│   └── task_service.py
└── cli/
    └── main.py
```

### 4. Install Dependencies
Since this project uses only Python standard library, no additional dependencies are required.

## Running the Application

### Method 1: Using UV (Recommended)
```bash
uv run src/cli/main.py
```

### Method 2: Direct Python Execution
```bash
python src/cli/main.py
```

## Application Usage

Once the application starts, you'll see the main menu:

```
Todo Application
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Toggle Complete
6. Exit
Choose an option:
```

### Available Operations

1. **Add Task**: Enter a title and optional description to create a new task
2. **View Tasks**: See all tasks with their IDs and completion status
3. **Update Task**: Modify an existing task by ID
4. **Delete Task**: Remove a task by ID
5. **Toggle Complete**: Change completion status of a task by ID
6. **Exit**: Close the application

## Development

### Adding New Features
- Add new functionality to the appropriate module (models, services, or cli)
- Maintain separation of concerns as defined in the architecture
- Follow the same error handling patterns

### Testing
- Unit tests should be added for model and service classes
- Integration tests for CLI functionality
- All tests should use Python's built-in unittest module

## Troubleshooting

### Common Issues
- **Python version**: Ensure you're using Python 3.13 or higher
- **Module not found**: Verify the directory structure matches the expected format
- **Permission errors**: Ensure you have read/write permissions for the project directory

### Error Messages
- "Invalid input" - Enter a number between 1-6 for menu options
- "Task not found" - Verify the task ID exists in the task list
- "Invalid ID" - Enter a valid integer ID that corresponds to an existing task