# CLI API Contract: Task CRUD – Phase I (CLI Todo App)

**Date**: 2025-12-30
**Feature**: 001-task-crud
**Input**: Feature specification from `/specs/001-task-crud/spec.md`

## Overview

This document defines the contract for the CLI Todo application's user interface. The application follows a menu-driven approach with numbered options for user interaction.

## Menu Interface

### Main Menu Options

| Option | Command | Description | Input Required |
|--------|---------|-------------|----------------|
| 1 | Add Task | Add a new task to the list | Title (required), Description (optional) |
| 2 | View Tasks | Display all tasks with ID, title, and completion status | None |
| 3 | Update Task | Update title/description of an existing task | Task ID, New Title (optional), New Description (optional) |
| 4 | Delete Task | Remove a task from the list | Task ID |
| 5 | Toggle Complete | Change completion status of a task | Task ID |
| 6 | Exit | Close the application | None |

## Input/Output Specifications

### Add Task (Option 1)
- **Input**:
  - Prompt for title: "Enter task title: "
  - Prompt for description: "Enter task description (optional): "
- **Output**:
  - Success: "Task added successfully with ID: {id}"
  - Error: Appropriate error message

### View Tasks (Option 2)
- **Input**: None
- **Output**:
  - If tasks exist: Formatted list with ID, Title, and Status
  - If no tasks: "No tasks found."

### Update Task (Option 3)
- **Input**:
  - Prompt for task ID: "Enter task ID to update: "
  - Prompt for new title: "Enter new title (leave blank to keep current): "
  - Prompt for new description: "Enter new description (leave blank to keep current): "
- **Output**:
  - Success: "Task updated successfully"
  - Error: Appropriate error message

### Delete Task (Option 4)
- **Input**:
  - Prompt for task ID: "Enter task ID to delete: "
- **Output**:
  - Success: "Task deleted successfully"
  - Error: Appropriate error message

### Toggle Complete (Option 5)
- **Input**:
  - Prompt for task ID: "Enter task ID to toggle: "
- **Output**:
  - Success: "Task completion status updated"
  - Error: Appropriate error message

### Exit (Option 6)
- **Input**: None
- **Output**: Application terminates gracefully

## Error Handling

### Input Validation
- Invalid menu selection → Display error and show menu again
- Non-integer input → Display error and request valid input
- Non-existent task ID → Display error and return to menu

### Error Messages
- "Invalid input. Please enter a number between 1-6."
- "Task with ID {id} does not exist."
- "Invalid ID. Please enter a valid task ID."

## State Management

- Tasks are stored in-memory only
- Task IDs are auto-incremented integers
- All data is lost when the application exits
- Application maintains a continuous loop until Exit option is selected