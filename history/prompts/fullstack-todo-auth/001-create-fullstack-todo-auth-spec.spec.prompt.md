---
id: 001
title: Create Fullstack Todo Auth Spec
stage: spec
date: 2026-01-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: fullstack-todo-auth
branch: 002-fullstack-todo-auth
user: Claude Code
command: sp.specify
labels: [specification, fullstack, authentication, todo]
links:
  spec: specs/002-fullstack-todo-auth/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-fullstack-todo-auth/spec.md
 - specs/002-fullstack-todo-auth/checklists/requirements.md
tests:
 - none
---

## Prompt

```text
# 📘 Specification - Hackathon Phase II
## Full-Stack Multi-User Todo Application

---

## 1. Phase II Goal (Exactly kya banana hai)

Phase II ka goal ek **real-world full-stack Todo application** banana hai jisme:

- Users signup & login kar sakte hain
- Har user ka data alag aur secure ho
- Tasks database me save hon
- Modern web UI ho (Next.js)
- Backend FastAPI ho
- Proper API + UI integration ho

Is phase me **CLI app extend nahi hogi**, balkay:
👉 CLI (Phase I) alag rahegi
👉 Phase II ka system **new backend + new frontend** hoga

---

## 2. Phase II Timeline (Pal-Pal Breakdown)

### 🕐 Step 1: User Website Open Karta Hai

- User browser me app open karta hai
- Default page `/login` open hota hai
- Agar user already logged in ho:
  - Direct `/dashboard` redirect

---

## 3. Authentication Flow (Signup → Login → Dashboard)

---

### 🟦 Signup Flow (`/signup`)

#### UI Elements:
- Page heading: **Create Account**
- Input field: Email
- Input field: Password
- Button: **Sign Up**
- Text link: **Already have an account? Login**

#### Behavior (Pal-Pal):
1. User email type karta hai
2. User password type karta hai
3. User "Sign Up" click karta hai
4. Frontend validation:
   - Email empty → error
   - Password empty → error
5. API request backend ko jati hai
6. Backend:
   - Email unique check
   - Password hash
   - User SQL database me save
7. Success:
   - Redirect to `/login`
8. Failure:
   - Error message UI par show

---

### 🟦 Login Flow (`/login`)

#### UI Elements:
- Page heading: **Login**
- Email input
- Password input
- Button: **Login**

#### Behavior:
1. User credentials enter karta hai
2. Login click
3. Backend:
   - User verify
   - JWT token generate
4. Token frontend ko milta hai
5. Token save hota hai (secure storage)
6. Redirect to `/dashboard`

---

## 4. Dashboard Flow (`/dashboard`)

### UI Structure:

#### Header:
- App Name: **Todo App**
- Logout Button

#### Main Area:
- Create Task Section
- Task List Section

---

## 5. Create Task Flow (Pal-Pal)

#### UI:
- Title input (required)
- Description textarea (optional)
- Button: **Add Task**

#### Behavior:
1. User title likhta hai
2. Optional description likhta hai
3. Add Task click karta hai
4. Frontend:
   - Title empty → error
5. API call backend ko
6. Backend:
   - JWT se user identify
   - Task database me insert
7. Response success
8. Task list auto refresh

---

## 6. View Tasks Flow

#### UI:
- Tasks list/cards format me
- Har task me:
  - Title
  - Description
  - Status (Completed / Pending)

#### Rules:
- Sirf logged-in user ke tasks
- Agar zero tasks:
  - Message: **No tasks yet**

---

## 7. Update Task Flow

#### UI:
- Har task ke sath **Edit** button

#### Behavior:
1. Edit click
2. Fields editable ho jate hain
3. User update karta hai
4. Save click
5. Backend:
   - Ownership verify
   - Task update
6. UI refresh

---

## 8. Delete Task Flow

#### UI:
- Delete button per task

#### Behavior:
1. Delete click
2. Confirmation dialog
3. Confirm:
   - Backend delete
4. UI update

---

## 9. Toggle Complete Flow

#### UI:
- Checkbox / Toggle button

#### Behavior:
1. User toggle karta hai
2. Backend status update
3. UI me status badge change

---

## 10. Logout Flow

#### Behavior:
1. Logout button click
2. Token remove
3. Redirect to `/login`

---

## 11. Backend Responsibilities (Clear)

- FastAPI backend
- SQLModel ORM
- JWT verification
- User isolation
- RESTful endpoints
- Error handling

---

## 12. Database Rules

### User Table:
- id
- email (unique)
- password_hash

### Task Table:
- id
- title
- description
- completed
- user_id (FK)

Rules:
- Task bina user ke nahi ho sakta
- User sirf apne tasks dekh sakta hai

---

## 13. Security Rules

- JWT required
- Unauthorized → 401
- Token expire supported
- No shared sessions

---

## 14. Phase II Completion Criteria

Phase II complete tab hoga jab:

✅ Signup kaam kare
✅ Login kaam kare
✅ Dashboard kaam kare
✅ Task CRUD kaam kare
✅ Data SQL me save ho
✅ UI predictable ho
✅ Phase I untouched ho

---

## 15. Final Instruction to# 📘 Specification - Hackathon Phase II
## Full-Stack Todo Web Application (Next.js + FastAPI)

---

## 1. Phase II Objective

Phase II ka objective ek **production-style full-stack Todo application** banana hai jisme:

- Modern web UI ho
- Multiple users support hon
- Har user ka data secure ho
- Tasks database me store hon
- Frontend aur backend proper API ke zariye connected hon

Is phase me **CLI app (Phase I)** ko modify nahi kiya jayega.
Phase I alag rahega, Phase II **web-based system** hoga.

---

## 2. Technology Stack (Mandatory)

### Frontend
- Next.js (App Router)
- TypeScript (strict mode)
- Tailwind CSS (UI styling)
- Fetch / API client for backend calls

### Backend
- FastAPI (Python)
- SQLModel (ORM)
- SQL Database (initially SQLite / file-based, future-ready)
- JWT-based authentication

---

## 3. User Journey (Pal-Pal Detail)

---

### 🟦 Step 1: App Open Hoti Hai

- User browser me app open karta hai
- Default route `/login` hota hai
- Agar user already authenticated ho:
  - Direct `/dashboard` redirect

---

## 4. Authentication System (Signup & Login)

---

### 🟩 Signup Page (`/signup`)

#### UI Requirements (Next.js + Tailwind)

- Centered card layout
- Heading: **Create Account**
- Input fields:
  - Email
  - Password
- Button:
  - **Sign Up**
- Link:
  - **Already have an account? Login**

#### Behavior:
1. User email aur password enter karta hai
2. Frontend validation:
   - Empty email → error
   - Empty password → error
3. API request backend ko jati hai
4. Backend:
   - Email uniqueness check
   - Password hash
   - User database me save
5. Success:
   - Redirect `/login`
6. Failure:
   - Error UI me show

---

### 🟩 Login Page (`/login`)

#### UI:
- Heading: **Login**
- Email input
- Password input
- Login button

#### Behavior:
1. User credentials enter karta hai
2. Backend verify karta hai
3. JWT token generate hota hai
4. Token frontend me save hota hai
5. Redirect `/dashboard`

---

## 5. Dashboard Page (`/dashboard`)

---

### UI Layout

#### Header Section:
- App Name: **Todo App**
- Logout Button (top right)

#### Main Content:
- Create Task Form
- Task List View

---

## 6. Create Task Feature

#### UI:
- Input:
  - Title (required)
- Textarea:
  - Description (optional)
- Button:
  - **Add Task**

#### Behavior:
1. User title likhta hai
2. Description optional
3. Add Task click
4. Frontend validation
5. API call backend ko
6. Backend:
   - JWT se user identify
   - Task user ke sath link
   - Database me save
7. Task list refresh

---

## 7. View Tasks Feature

#### UI:
- Tasks list cards ya rows me
- Har task show kare:
  - Title
  - Description
  - Status badge (Completed / Pending)

#### Rules:
- Sirf logged-in user ke tasks show hon
- Agar koi task na ho:
  - Message: **No tasks found**

---

## 8. Update Task Feature

#### UI:
- Har task ke sath **Edit** button

#### Behavior:
1. Edit click
2. Fields editable ho jate hain
3. User title / description update karta hai
4. Save click
5. Backend:
   - Ownership verify
   - Task update
6. UI refresh

---

## 9. Delete Task Feature

#### UI:
- Delete button per task

#### Behavior:
1. Delete click
2. Confirmation dialog
3. Backend task delete
4. UI refresh

---

## 10. Toggle Complete Feature

#### UI:
- Checkbox / toggle switch

#### Behavior:
1. Toggle click
2. Backend completed flag update
3. Status badge update

---

## 11. Logout Feature

#### Behavior:
1. Logout click
2. JWT token remove
3. Redirect `/login`

---

## 12. Backend API Responsibilities

- FastAPI REST endpoints
- JWT verification middleware
- SQLModel ORM usage
- User-task relationship enforce
- Proper HTTP status codes

---

## 13. Database Schema Rules

### User Table
- id
- email (unique)
- password_hash

### Task Table
- id
- title
- description
- completed
- user_id (foreign key)

Rules:
- Task bina user ke create nahi hoga
- User sirf apne tasks access karega

---

## 14. UI Styling Rules (Tailwind)

- Clean & minimal UI
- Mobile responsive
- Consistent spacing
- Clear error messages
- No random colors (simple theme)

---

## 15. Phase II Comp Next.js use ho gi typescript use ho gi
```

## Response snapshot

# Feature Specification: Full-Stack Todo Application with User Authentication

**Feature Branch**: `002-fullstack-todo-auth`
**Created**: 2026-01-05
**Status**: Draft
**Input**: User description: "Full-Stack Multi-User Todo Application with Next.js, FastAPI, SQL database, and JWT authentication"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - User Registration and Authentication (Priority: P1)

A new user visits the application and wants to create an account to manage their personal tasks. The user enters their email and password, submits the registration form, receives confirmation, and can then log in to access their tasks.

**Why this priority**: This is the foundational functionality that enables all other features - without user accounts, there's no way to provide personalized task management.

**Independent Test**: Can be fully tested by creating a new user account and logging in successfully, delivering the core value of personal task management.

**Acceptance Scenarios**:

1. **Given** user is on the signup page, **When** user enters valid email and password and clicks "Sign Up", **Then** account is created and user is redirected to login page
2. **Given** user has an account, **When** user enters valid credentials on login page and clicks "Login", **Then** user is authenticated and redirected to dashboard

---

### User Story 2 - Task Management (Priority: P1)

An authenticated user wants to create, view, update, and delete their personal tasks. The user can add new tasks with titles and descriptions, see their existing tasks, edit them, mark them as complete, or delete them.

**Why this priority**: This is the core functionality of the todo application that provides the primary value to users.

**Independent Test**: Can be fully tested by creating, viewing, updating, and deleting tasks as an authenticated user, delivering the core todo management value.

**Acceptance Scenarios**:

1. **Given** user is authenticated and on dashboard, **When** user enters task title and description and clicks "Add Task", **Then** new task is created and appears in the task list
2. **Given** user has created tasks, **When** user views the dashboard, **Then** all their tasks are displayed with title, description, and status
3. **Given** user has a task, **When** user clicks edit and updates the task, **Then** task is updated in the system
4. **Given** user has a task, **When** user clicks delete and confirms, **Then** task is removed from the system

---

### User Story 3 - Task Completion Tracking (Priority: P2)

An authenticated user wants to mark their tasks as complete or incomplete to track their progress. The user can toggle the completion status of their tasks and see visual indicators of which tasks are completed.

**Why this priority**: This provides essential functionality for tracking progress and organizing tasks, which is a core requirement of todo applications.

**Independent Test**: Can be fully tested by toggling task completion status and seeing the updated status displayed, delivering the value of progress tracking.

**Acceptance Scenarios**:

1. **Given** user has an incomplete task, **When** user toggles the completion status, **Then** task is marked as complete and displays as completed
2. **Given** user has a completed task, **When** user toggles the completion status, **Then** task is marked as incomplete and displays as pending

---

### User Story 4 - Secure Session Management (Priority: P1)

An authenticated user wants to securely access their account and properly log out. The user can log out to end their session and must provide credentials to access the application again.

**Why this priority**: Security is critical for protecting user data and maintaining trust in the application.

**Independent Test**: Can be fully tested by logging in, performing actions, logging out, and being unable to access protected features without re-authenticating, delivering the value of secure access.

**Acceptance Scenarios**:

1. **Given** user is authenticated, **When** user clicks logout button, **Then** session is terminated and user is redirected to login page
2. **Given** user is not authenticated, **When** user tries to access protected pages, **Then** user is redirected to login page

---

### Edge Cases

- What happens when a user tries to register with an email that already exists?
- How does the system handle invalid email formats during registration?
- What happens when a user's JWT token expires during a session?
- How does the system handle attempts to access another user's tasks?
- What happens when a user tries to delete a task that no longer exists?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support user registration with email and password
- **FR-002**: System MUST validate email format and password requirements during registration
- **FR-003**: System MUST prevent registration with duplicate email addresses
- **FR-004**: System MUST hash passwords before storing user credentials
- **FR-005**: System MUST support user authentication with email and password
- **FR-006**: System MUST generate JWT tokens upon successful authentication
- **FR-007**: System MUST require valid JWT tokens for accessing protected routes
- **FR-008**: System MUST support creating tasks with required title and optional description
- **FR-009**: System MUST associate each task with the authenticated user who created it
- **FR-010**: System MUST display only the authenticated user's tasks on the dashboard
- **FR-011**: System MUST support updating task title and/or description
- **FR-012**: System MUST support deleting tasks by ID
- **FR-013**: System MUST support toggling task completion status
- **FR-014**: System MUST store all user and task data in SQL database
- **FR-015**: System MUST support user logout functionality
- **FR-016**: System MUST clear JWT tokens upon logout
- **FR-017**: System MUST prevent users from accessing other users' tasks
- **FR-018**: System MUST validate JWT tokens for each authenticated request
- **FR-019**: System MUST provide clear error messages for failed operations

### Key Entities *(include if feature involves data)*

- **User**: Represents a registered user with unique email, hashed password, and creation timestamp
- **Task**: Represents a todo item with title, description, completion status, and association to a specific user
- **Session**: Represents an authenticated user session managed through JWT tokens

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can register and log in successfully within 2 minutes
- **SC-002**: 95% of user registration attempts complete successfully without technical errors
- **SC-003**: 90% of users can create, view, update, and delete tasks without technical errors
- **SC-004**: Users can securely log out and their session is properly terminated
- **SC-005**: Users can only access their own tasks (no cross-user data leakage)
- **SC-006**: 98% of authenticated requests are processed successfully
- **SC-007**: Users can mark tasks as complete/incomplete with immediate visual feedback

## Outcome

- ✅ Impact: Created comprehensive specification for full-stack todo application with user authentication
- 🧪 Tests: none
- 📁 Files: specs/002-fullstack-todo-auth/spec.md, specs/002-fullstack-todo-auth/checklists/requirements.md
- 🔁 Next prompts: Continue with planning phase using /sp.plan
- 🧠 Reflection: Specification covers all required user journeys and functional requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning implementation