---
id: 002
title: Create Fullstack Todo Auth Plan
stage: plan
date: 2026-01-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: fullstack-todo-auth
branch: 002-fullstack-todo-auth
user: Claude Code
command: sp.plan
labels: [plan, fullstack, authentication, todo, api]
links:
  spec: specs/002-fullstack-todo-auth/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-fullstack-todo-auth/plan.md
 - specs/002-fullstack-todo-auth/research.md
 - specs/002-fullstack-todo-auth/data-model.md
 - specs/002-fullstack-todo-auth/quickstart.md
 - specs/002-fullstack-todo-auth/contracts/api-contract.md
tests:
 - none
---

## Prompt

```text
# 🧭 /sp.plan - Hackathon Phase II
## Full-Stack Todo Web Application (Next.js + FastAPI)

---

## Phase II High-Level Plan

Is phase me hum Phase I ki CLI Todo App ko **ek real web application** me evolve karenge:

- Frontend: Next.js (TypeScript + Tailwind CSS)
- Backend: FastAPI
- Database: SQLModel (SQL database)
- Auth: Email + Password (JWT based)

---

## STEP 0: Application Start Flow

1. User browser me app URL open karta hai
2. Frontend Next.js app load hoti hai
3. System check karta hai:
   - JWT token present hai ya nahi
4. Agar token nahi:
   → User `/login` page par redirect
5. Agar token hai:
   → User `/dashboard` par redirect

---

## STEP 1: Frontend Project Setup (Next.js)

### Tasks:
- Next.js App Router project create
- TypeScript enable
- Tailwind CSS configure
- Basic layout component banani

### Result:
- Clean UI foundation ready
- Pages banana easy ho jaye

---

## STEP 2: Authentication Pages

---

### 2.1 Signup Page (`/signup`)

#### UI:
- Heading: Create Account
- Input: Email
- Input: Password
- Button: **Sign Up**
- Link: Login page

#### Behavior:
1. User email + password enter karta hai
2. Sign Up button click hota hai
3. Frontend validation:
   - Empty email → error
   - Empty password → error
4. Backend request jati hai:
   - User create
   - Password hash
   - Database me save
5. Success:
   - Redirect `/login`
6. Error:
   - Message UI pe show

---

### 2.2 Login Page (`/login`)

#### UI:
- Heading: Login
- Input: Email
- Input: Password
- Button: **Login**

#### Behavior:
1. User credentials enter karta hai
2. Login click
3. Backend:
   - Credentials verify
   - JWT token generate
4. Token frontend me store hota hai
5. Redirect `/dashboard`

---

## STEP 3: Dashboard Page (`/dashboard`)

### Page Structure:

#### Top Bar:
- App Name: Todo App
- Logout Button

#### Main Area:
- Create Task Section
- View Tasks Section

---

## STEP 4: Add Task Feature

### UI:
- Title input (required)
- Description textarea (optional)
- Button: **Add Task**

### Flow:
1. User title likhta hai
2. Description optional likhta hai
3. Add Task button click
4. Frontend check:
   - Title empty → error
5. Backend API call:
   - JWT se user identify
   - Task database me insert
6. Success:
   - Task list refresh

---

## STEP 5: View Tasks Feature

### UI:
- Task cards / list format
- Har task me:
  - Title
  - Description
  - Status badge (Pending / Completed)
  - Buttons:
    - Edit
    - Delete
    - Toggle Complete

### Behavior:
- Sirf logged-in user ke tasks load hon
- Agar tasks nahi:
  - Message: **No tasks yet**

---

## STEP 6: Update Task Feature

### Flow:
1. User Edit button click karta hai
2. Title & description editable ho jate hain
3. Save button click
4. Backend:
   - User ownership verify
   - Task update
5. UI refresh ho jata hai

---

## STEP 7: Delete Task Feature

### Flow:
1. Delete button click
2. Confirmation popup
3. Confirm:
   - Backend delete request
4. Task list update

---

## STEP 8: Toggle Complete Feature

### Flow:
1. User checkbox / toggle click karta hai
2. Backend:
   - Completed true/false update
3. Status badge update hota hai

---

## STEP 9: Logout Feature

### Flow:
1. Logout button click
2. JWT token remove hota hai
3. Redirect `/login`

---

## STEP 10: Backend Implementation Plan

### Tasks:
- FastAPI project setup
- SQLModel models:
  - User
  - Task
- JWT auth middleware
- CRUD APIs:
  - Create task
  - View tasks
  - Update task
  - Delete task
  - Toggle complete

### Rules:
- Har request me JWT required
- User sirf apne tasks access kare

---

## STEP 11: Database Flow

### Tables:
- users
- tasks

### Data Flow:
1. User signup → user table
2. User login → token generate
3. Task create → task table (user_id ke sath)
4. Task fetch → user_id filter
5. Update/Delete → ownership check

---

## STEP 12: Phase II Completion Criteria

Phase II tab complete hoga jab:

✅ Next.js UI properly render ho
✅ Signup & Login work kare
✅ JWT auth enforce ho
✅ Task Create / View / Update / Delete work kare
✅ Tasks database me save hon   app backend se api fetch kr le lao jo ose example forened me show kro gi example jese ueer saniup kre api se request jai database me data save hu forened bana ne se phele backend call krna sari api url fetch krna forened me lagana take sab kam successfully hu
```

## Response snapshot

# Implementation Plan: Full-Stack Todo Application with User Authentication

**Branch**: `002-fullstack-todo-auth` | **Date**: 2026-01-01 | **Spec**: [specs/002-fullstack-todo-auth/spec.md](./spec.md)
**Input**: Feature specification from `/specs/[002-fullstack-todo-auth]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Full-stack web application with user authentication enabling personalized task management. The system consists of a Next.js frontend with JWT-based authentication and a FastAPI backend with SQL database storage. Users can register, login, create tasks, manage their tasks, and securely logout. The architecture ensures data isolation between users and follows security best practices.

## Technical Context

**Language/Version**: Python 3.13+ (Backend), TypeScript 5+ (Frontend)
**Primary Dependencies**: FastAPI, SQLModel, Next.js, JWT, Tailwind CSS
**Storage**: SQL database (SQLite/PostgreSQL) with User and Task tables
**Testing**: pytest (Backend), Jest/React Testing Library (Frontend)
**Target Platform**: Web application (Browser-based)
**Project Type**: web - fullstack application with separate frontend and backend
**Performance Goals**: Sub-second API response times, responsive UI interactions
**Constraints**: JWT-based authentication, user data isolation, secure password hashing
**Scale/Scope**: Single-user focused with multi-user architecture ready

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- All code MUST be generated by Claude Code (No manual coding) ✅
- All functionality MUST be defined in specifications before implementation ✅
- Specs are the single source of truth ✅
- UV MUST be used for Python project and dependency management ✅
- Python version MUST be 3.13 or higher ✅
- Next.js App Router MUST be used for frontend routing ✅
- SQLModel ORM MUST be used for database operations ✅
- JWT-based authentication required for all endpoints ✅
- User data isolation must be maintained ✅
- Passwords must be hashed using proper algorithms ✅

## Project Structure

### Documentation (this feature)

```text
specs/002-fullstack-todo-auth/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── user.py
│   │   └── task.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   └── task_service.py
│   ├── api/
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── tasks.py
│   └── main.py
├── tests/
│   ├── unit/
│   └── integration/
└── pyproject.toml

frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── signup/
│   │   │   └── page.tsx
│   │   └── dashboard/
│   │       └── page.tsx
│   ├── components/
│   │   ├── LoginForm.tsx
│   │   ├── SignupForm.tsx
│   │   ├── TaskList.tsx
│   │   ├── TaskForm.tsx
│   │   └── Navbar.tsx
│   ├── services/
│   │   ├── api.ts
│   │   └── auth.ts
│   └── types/
│       ├── user.ts
│       └── task.ts
├── styles/
│   └── globals.css
├── package.json
└── tailwind.config.js
```

**Structure Decision**: Web application structure selected with separate backend and frontend directories to maintain clean separation of concerns between client and server code.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Separate backend/frontend | Clear separation of concerns, scalability | Monolithic structure would mix concerns and limit scalability |
| JWT authentication | Secure stateless authentication | Session-based auth would require server-side storage |
| SQL database | Persistent data storage with relationships | In-memory storage would not persist data between sessions |

# Research: Full-Stack Todo Application with User Authentication

## Decision: Technology Stack Selection
**Rationale**: Selected Next.js 14+ with App Router for frontend due to its excellent server/client component architecture, built-in optimization features, and strong TypeScript support. FastAPI for backend due to its high performance, automatic API documentation, and excellent Python type hinting support.

**Alternatives considered**:
- React + Vite: More complex setup, no built-in routing solution
- Express.js: Less performant, no automatic documentation
- Django: Overkill for simple API, heavier framework
- Remix: Good but less mature ecosystem than Next.js

## Decision: Authentication Strategy
**Rationale**: JWT (JSON Web Tokens) with HTTP-only cookies or localStorage for token storage. JWTs provide stateless authentication which scales well and integrates cleanly with both Next.js frontend and FastAPI backend.

**Alternatives considered**:
- Session-based auth: Requires server-side session storage
- OAuth providers: More complex setup, not required by spec
- API keys: Not appropriate for user authentication

## Decision: Database and ORM
**Rationale**: SQLModel as required by constitution, with SQLite for development and PostgreSQL for production. SQLModel provides excellent integration with FastAPI and supports both SQLAlchemy and Pydantic patterns.

**Alternatives considered**:
- Pure SQLAlchemy: More verbose, no Pydantic integration
- Tortoise ORM: Async-native but less mature
- Prisma: Requires Node.js, not suitable for Python backend

## Decision: Frontend Styling
**Rationale**: Tailwind CSS for utility-first styling approach, providing rapid UI development while maintaining consistency. Integrates well with Next.js and provides responsive design out of the box.

**Alternatives considered**:
- CSS Modules: More verbose, requires more custom CSS
- Styled-components: React-specific, adds bundle size
- Material UI: Too opinionated, larger bundle size

## Decision: API Design
**Rationale**: RESTful API design with standard HTTP methods and status codes. FastAPI's Pydantic models for request/response validation and automatic OpenAPI documentation generation.

**Alternatives considered**:
- GraphQL: More complex for simple todo app requirements
- gRPC: Overkill for web frontend
- RPC-style: Less standard, harder to document

## Decision: Security Measures
**Rationale**: Password hashing with bcrypt, JWT with expiration times, input validation at API layer, and proper error handling to prevent information disclosure.

**Alternatives considered**:
- Other hashing algorithms: bcrypt is industry standard for password hashing
- Longer JWT expiration: Security risk, shorter is safer
- Basic error messages: Need balance between user experience and security

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

# Quickstart Guide: Full-Stack Todo Application

## Prerequisites

- Node.js 18+ with npm/yarn
- Python 3.13+
- uv (Python package manager)
- A SQL database (SQLite for development, PostgreSQL for production)

## Setup Instructions

### 1. Clone and Initialize Repository

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install Python dependencies with uv
cd backend
uv init
uv add fastapi sqlmodel python-jose bcrypt python-multipart python-dotenv
uv sync
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env with your database URL and secret keys

# Run database migrations (if applicable)
uv run python -m src.main migrate

# Start the backend server
uv run python -m src.main dev
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
# Edit with your backend API URL

# Start the development server
npm run dev
```

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout

### Users
- `GET /users/me` - Get current user info

### Tasks
- `GET /tasks` - Get user's tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task
- `PATCH /tasks/{id}/complete` - Toggle task completion

## Environment Variables

### Backend (.env)
```env
DATABASE_URL=sqlite:///./todo_app.db
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Running Tests

### Backend Tests
```bash
cd backend
uv run pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Development Workflow

1. Start the backend server
2. Start the frontend development server
3. Access the application at `http://localhost:3000`
4. Register a new account or login with existing credentials
5. Create and manage tasks through the dashboard

## Database Migrations

If using PostgreSQL or other SQL databases:
```bash
# Run migrations
uv run alembic upgrade head

# Create new migration
uv run alembic revision --autogenerate -m "migration message"
```

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

## Outcome

- ✅ Impact: Created comprehensive implementation plan for full-stack todo application with user authentication
- 🧪 Tests: none
- 📁 Files: specs/002-fullstack-todo-auth/plan.md, specs/002-fullstack-todo-auth/research.md, specs/002-fullstack-todo-auth/data-model.md, specs/002-fullstack-todo-auth/quickstart.md, specs/002-fullstack-todo-auth/contracts/api-contract.md
- 🔁 Next prompts: Continue with task creation using /sp.tasks
- 🧠 Reflection: Plan includes all necessary components for full-stack development with proper architecture and security

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task creation and implementation