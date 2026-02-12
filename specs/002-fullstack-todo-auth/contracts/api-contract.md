# API Contract: Full-Stack Todo Application

## Authentication API

### POST /auth/register
**Description**: Register a new user account

**Request**:
- Content-Type: `application/json`
- Body:
  ```json
  {
    "email": "user@example.com",
    "password": "securePassword123"
  }
  ```

**Responses**:
- `200 OK`: User registered successfully
  ```json
  {
    "message": "User registered successfully",
    "user_id": 123
  }
  ```
- `400 Bad Request`: Invalid input or duplicate email
- `422 Unprocessable Entity`: Validation errors

### POST /auth/login
**Description**: Authenticate user and return JWT token

**Request**:
- Content-Type: `application/json`
- Body:
  ```json
  {
    "email": "user@example.com",
    "password": "securePassword123"
  }
  ```

**Responses**:
- `200 OK`: Login successful
  ```json
  {
    "access_token": "jwt_token_here",
    "token_type": "bearer"
  }
  ```
- `401 Unauthorized`: Invalid credentials

### POST /auth/logout
**Description**: Logout user (invalidate session)

**Headers**:
- `Authorization: Bearer {token}`

**Responses**:
- `200 OK`: Logout successful
- `401 Unauthorized`: Invalid or expired token

## User API

### GET /users/me
**Description**: Get current authenticated user info

**Headers**:
- `Authorization: Bearer {token}`

**Responses**:
- `200 OK`: User data returned
  ```json
  {
    "id": 123,
    "email": "user@example.com",
    "created_at": "2023-01-01T00:00:00Z"
  }
  ```
- `401 Unauthorized`: Invalid or expired token

## Tasks API

### GET /tasks
**Description**: Get all tasks for the authenticated user

**Headers**:
- `Authorization: Bearer {token}`

**Responses**:
- `200 OK`: Tasks returned
  ```json
  [
    {
      "id": 1,
      "title": "Complete project",
      "description": "Finish the todo app implementation",
      "completed": false,
      "user_id": 123,
      "created_at": "2023-01-01T00:00:00Z"
    }
  ]
  ```
- `401 Unauthorized`: Invalid or expired token

### POST /tasks
**Description**: Create a new task for the authenticated user

**Headers**:
- `Authorization: Bearer {token}`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "title": "New task",
  "description": "Task description (optional)",
  "completed": false
}
```

**Responses**:
- `201 Created`: Task created successfully
  ```json
  {
    "id": 124,
    "title": "New task",
    "description": "Task description (optional)",
    "completed": false,
    "user_id": 123,
    "created_at": "2023-01-01T00:00:00Z"
  }
  ```
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Invalid or expired token

### PUT /tasks/{id}
**Description**: Update an existing task

**Path Parameters**:
- `id`: Task ID (integer)

**Headers**:
- `Authorization: Bearer {token}`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "title": "Updated task title",
  "description": "Updated description",
  "completed": true
}
```

**Responses**:
- `200 OK`: Task updated successfully
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Invalid or expired token
- `404 Not Found`: Task not found or doesn't belong to user

### DELETE /tasks/{id}
**Description**: Delete a task

**Path Parameters**:
- `id`: Task ID (integer)

**Headers**:
- `Authorization: Bearer {token}`

**Responses**:
- `204 No Content`: Task deleted successfully
- `401 Unauthorized`: Invalid or expired token
- `404 Not Found`: Task not found or doesn't belong to user

### PATCH /tasks/{id}/complete
**Description**: Toggle task completion status

**Path Parameters**:
- `id`: Task ID (integer)

**Headers**:
- `Authorization: Bearer {token}`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "completed": true
}
```

**Responses**:
- `200 OK`: Task completion status updated
  ```json
  {
    "id": 124,
    "title": "Task title",
    "description": "Task description",
    "completed": true,
    "user_id": 123
  }
  ```
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Invalid or expired token
- `404 Not Found`: Task not found or doesn't belong to user