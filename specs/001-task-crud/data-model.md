# Data Model: Task CRUD – Phase I (CLI Todo App)

**Date**: 2025-12-30
**Feature**: 001-task-crud
**Input**: Feature specification from `/specs/001-task-crud/spec.md`

## Entity: Task

### Attributes

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | integer | Unique, Auto-generated | Unique identifier for the task |
| title | string | Required | Title of the task |
| description | string | Optional | Optional description of the task |
| completed | boolean | Default: false | Completion status of the task |

### Validation Rules

- **id**: Must be unique, auto-incremented integer starting from 1
- **title**: Must be provided (non-empty), string type
- **description**: Optional, can be empty string if not provided
- **completed**: Boolean value, defaults to false for new tasks

### State Transitions

- **New Task**: `completed = false` (default)
- **Toggle Complete**: `completed = !completed` (switches state)
- **Update Task**: Attributes can be modified except for id

### Relationships

- **None**: Task entity is standalone with no relationships to other entities

## In-Memory Storage

### Data Structure

The tasks will be stored in memory using a dictionary where:
- **Key**: Task ID (integer)
- **Value**: Task object/record

### Operations

- **Create**: Add new task to the dictionary with auto-generated ID
- **Read**: Retrieve task by ID from the dictionary
- **Update**: Modify existing task attributes in the dictionary
- **Delete**: Remove task from the dictionary by ID

### ID Generation

- Auto-incrementing integer IDs starting from 1
- IDs are never reused after deletion
- Maintains uniqueness across all operations

## Implementation Considerations

### Memory Management

- Data exists only during runtime
- No persistence to files or external storage
- All data is lost when the application terminates

### Thread Safety

- Not required for single-user CLI application
- No concurrent access concerns

### Performance

- O(1) lookup by ID using dictionary
- O(1) insertion and deletion
- O(n) iteration for list operations (view all tasks)