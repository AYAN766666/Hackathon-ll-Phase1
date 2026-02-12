# Data Model: Full-Stack Todo Application with User Authentication

## User Entity

**Fields**:
- `id`: Integer (Primary Key, Auto-increment)
- `email`: String (Unique, Required, Max length 255)
- `hashed_password`: String (Required, Max length 255)
- `created_at`: DateTime (Auto-generated on creation)

**Relationships**:
- One-to-Many: User → Tasks (via user_id foreign key)

**Validation Rules**:
- Email must be valid email format
- Email must be unique across all users
- Email is required
- Password must be hashed before storage

## Task Entity

**Fields**:
- `id`: Integer (Primary Key, Auto-increment)
- `title`: String (Required, Max length 255)
- `description`: String (Optional, Max length 1000)
- `completed`: Boolean (Default: false)
- `user_id`: Integer (Foreign Key to User.id, Required)

**Relationships**:
- Many-to-One: Task → User (via user_id foreign key)

**Validation Rules**:
- Title is required
- Title must not be empty
- User_id must reference an existing user
- Task can only be accessed by the owning user

## Session/Authentication Model

**Conceptual Model** (JWT-based, no persistent storage):
- JWT Token contains user identity
- Token includes expiration time
- Token is validated on each authenticated request

**Validation Rules**:
- JWT must be valid and not expired
- Token must contain valid user ID
- User must exist in database for token to be valid

## State Transitions

### Task Completion State
- Initial: `completed = false`
- When marked complete: `completed = true`
- When marked incomplete: `completed = false`

### User Authentication State
- Not authenticated: No valid JWT token
- Authenticated: Valid JWT token present
- Session ended: JWT token cleared/invalidated

## Constraints

1. **Referential Integrity**: All tasks must reference an existing user
2. **User Isolation**: Users can only access their own tasks
3. **Data Validation**: All required fields must be present and valid
4. **Uniqueness**: Email addresses must be unique across users
5. **Security**: Passwords must be hashed, never stored in plain text