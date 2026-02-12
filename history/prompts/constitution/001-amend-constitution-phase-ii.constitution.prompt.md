---
id: 001
title: Amend Constitution Phase II
stage: constitution
date: 2026-01-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-task-crud
user: Claude Code
command: sp.constitution
labels: [constitution, phase-ii, todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
# 📜 Project Constitution - Phase II
## Full-Stack Todo Application (User + Tasks with SQL Database)

---

## 1. Purpose (Very Simple Words)

Phase II ka purpose **real-world Todo Application banana** hai jahan:

- User **signup** kare
- User **login** kare
- User ka **data database me save ho**
- Har user apne **alag tasks** banaye
- Koi bhi user doosre user ka data **na dekh sake**

Is phase me app bilkul **real software jaisi behave karegi**.

---

## 2. User Journey (Second by Second - 1-1 Pal ki Khabar)

### 🕐 Pal 1 - User Website Open Karta Hai
- Browser me app open hoti hai
- System check karta hai:
  - User login hai? ❌
- User ko **Login Page** dikhaya jata hai

---

### 🕐 Pal 2 - User Signup Karta Hai (New User)

#### Signup Page par:
User ye details bharta hai:
- Email
- Password

#### System kya karega:
1. Password ko **hash** karega
2. User ka data **SQL database** me save karega
3. User table me entry hogi:
   - id
   - email
   - hashed_password
   - created_at
4. Signup successful message show hoga
5. User ko **Login Page** par bhej diya jayega

---

### 🕐 Pal 3 - User Login Karta Hai

#### Login Page par:
- Email
- Password

#### System kya karega:
1. Database se email match karega
2. Password verify karega
3. Agar sahi:
   - JWT token generate hoga
   - Token frontend ko milega
4. User ko **Dashboard** par redirect kar diya jayega

❌ Agar ghalat:
- Error message show hoga

---

### 🕐 Pal 4 - Dashboard Load Hota Hai

User ko dikhai deta hai:
- Welcome message
- Logout button
- "Create Task" button
- Task list (agar pehle se koi hai)

System kya karta hai:
- JWT token se user identify karta hai
- Sirf **usi user ke tasks** database se load karta hai

---

### 🕐 Pal 5 - User Task Create Karta Hai

User "Create Task" button press karta hai

#### Task form:
- Title (required)
- Description (optional)

#### System kya karega:
1. Task table me entry karega:
   - task_id
   - title
   - description
   - completed (false)
   - user_id (foreign key)
2. Task database me save ho jayega
3. UI par task turant show ho jayega

---

### 🕐 Pal 6 - User Tasks Dekhta Hai

Dashboard par:
- Sirf **logged-in user ke tasks**
- Har task ke sath:
  - Title
  - Description
  - Status
  - Edit / Delete / Complete buttons

---

### 🕐 Pal 7 - User Task Complete Karta Hai

User "Complete" button dabata hai

System:
- Task ka `completed = true` set karta hai
- Database update hota hai
- UI me task completed dikh jata hai

User chahe to wapas incomplete bhi kar sakta hai

---

### 🕐 Pal 8 - User Task Update Karta Hai

User "Edit" button dabata hai:
- Title change
- Description change

System:
- Task ko update karta hai
- Database me save hota hai
- UI refresh hoti hai

---

### 🕐 Pal 9 - User Task Delete Karta Hai

User "Delete" button dabata hai

System:
- Task database se delete karta hai
- UI se task remove ho jata hai

---

### 🕐 Pal 10 - User Logout Karta Hai

User Logout button press karta hai

System:
- Token clear karta hai
- User ko Login Page par le jata hai

---

## 3. Database Constitution (SQLModel)

### 🧑 User Table

| Field | Type |
|-----|------|
| id | Integer (PK) |
| email | String (unique) |
| hashed_password | String |
| created_at | DateTime |

---

### ✅ Task Table

| Field | Type |
|-----|------|
| id | Integer (PK) |
| title | String |
| description | String |
| completed | Boolean |
| user_id | Foreign Key (User.id) |

---

## 4. Backend Rules (FastAPI)

- Har request me JWT token required
- Token se user identify hoga
- User sirf **apna data** access karega
- Invalid token → request reject

---

## 5. Frontend Rules (Next.js)

- Login ke baghair koi page open nahi hoga
- Token local storage me safe hoga
- Har API call token ke sath jayegi
- Simple clean UI (no confusion)

---

## 6. Security Constitution

- Password kabhi plain text me store nahi hoga
- JWT expire hoga
- User data isolated rahega

---

## 7. Strict Development Rules

❌ Manual coding nahi
❌ Phase I delete nahi
✅ Sirf specs se code generate
✅ Database required
✅ Real user flow requir# 📜 Project Constitution - Phase II
## Full-Stack Todo Application (Next.js + FastAPI + SQL)

---

## 1. Purpose (Phase II ka Maqsad)

Phase II ka maqsad Phase I ki CLI Todo App ko **real-world full-stack web application** me evolve karna hai jahan:

- Multiple users ho sakte hain
- Har user ka data secure ho
- Proper **Login / Signup flow** ho
- **Next.js UI** ho (clear pages, buttons, forms)
- **FastAPI backend** ho
- **SQL database** me user aur task data save ho

Ye phase **production-style application behavior** demonstrate karega.

---

## 2. Absolute Rules (No Confusion Allowed)

1. Phase I ka code **delete ya overwrite nahi hoga**
2. Phase II ka code **new folders** me add hoga
3. Manual coding strictly prohibited
4. Har feature pehle **spec me likha hoga**
5. UI behavior bhi spec ka hissa hoga
6. Next.js App Router mandatory
7. Backend FastAPI hoga
8. SQLModel ORM use hoga

---

## 3. Folder Structure (Strict)


---

## 5. Frontend UI Constitution (IMPORTANT)

### 🎨 Colors (Simple & Clean)

| Purpose | Color |
|------|------|
| Background | #f9fafb |
| Primary Button | #2563eb |
| Text | #111827 |
| Success | #16a34a |
| Error | #dc2626 |

---

## 6. Pages Detail (Child-Friendly Explanation)

---

### 🔐 Login Page (`/login`)

**User yahan kya karega?**
- Email likhega
- Password likhega
- Login button press karega

**UI me kya hoga?**
- Page center me ek box
- Box ke andar:
  - Email input
  - Password input
  - Login button
- Neeche link:
  👉 "Don’t have an account? Sign up"

**After Login**
- User dashboard par redirect hoga

---

### 📝 Signup Page (`/signup`)

**User yahan kya karega?**
- Email enter karega
- Password set karega
- Signup button dabaye ga

**UI me kya hoga?**
- Simple form
- Validation errors show hongi
- Successful signup pe login page par redirect

---

### 🧠 Dashboard (`/dashboard`)

**User yahan kya dekhega?**
- Welcome message
  👉 "Welcome, Ayan 👋"
- Button:
  ➕ "Create New Task"
- List of tasks

**Navigation**
- Top bar:
  - App name (Todo App)
  - Logout button

---

### ✅ Tasks Page (`/tasks`)

**Har task ke liye UI:**
- Title (bold)
- Description (small text)
- Status:
  - ✅ Completed
  - ⏳ Pending
- Buttons:
  - Edit
  - Delete
  - Complete / Incomplete

**User kya kar sakta hai?**
- New task add
- Task edit
- Task delete
- Task complete mark
- Task incomplete wapas kare

---

## 7. Backend + UI Connection (Simple Flow)

1. Frontend button click
2. API request FastAPI ko
3. FastAPI database se data le
4. JSON response frontend ko
5. UI update ho jaye

---

## 8. Authentication Rules

- Login ke baad JWT token milega
- Token browser me store hoga
- Har API call me token jayega
- Backend bina token request reject karega

---

## 9. Phase II Functional Features

✅ Signup
✅ Login
✅ Logout
✅ Create Task
✅ Read Tasks
✅ Update Task
✅ Delete Task
✅ Task Complete / Incomplete

---

## 10. Strict Rules (Repeat Important)

- ❌ Manual co jab user fastapi  hr page ki Ui hu sab Ui button jo b hu ache se hu
```

## Response snapshot

# Todo Application Constitution - Phase II

## Core Principles

### Purpose-Driven Development
The purpose of this project is to demonstrate Spec-Driven Development using Claude Code and Spec-Kit Plus. Phase II focuses on evolving the Phase I CLI Todo application into a real-world full-stack web application with user authentication, database persistence, and proper security. This phase validates the developer's ability to build a complete web application with user isolation, secure authentication, and modern web technologies (Next.js + FastAPI + SQL).

### Scope Adherence
This constitution applies strictly to Phase II of the hackathon. Included: Next.js frontend with App Router, FastAPI backend, SQL database with user and task tables, JWT authentication, user signup/login/logout, task CRUD operations with user isolation, responsive UI with login/signup/dashboard/tasks pages. Excluded: Advanced features beyond basic CRUD, third-party integrations, complex business logic, manual coding outside of spec-driven generation.

### Development Rule Compliance (NON-NEGOTIABLE)
All code MUST be generated by Claude Code. Manual coding is strictly prohibited. All functionality MUST be defined in specifications before implementation. Specs are the single source of truth. UV MUST be used for Python project and dependency management. Python version MUST be 3.13 or higher. Next.js App Router MUST be used for frontend routing. SQLModel ORM MUST be used for database operations. Phase I code MUST NOT be deleted or overwritten. Violating any rule invalidates the phase submission.

### Functional Completeness
The application MUST support the following features: User Signup (email and password with hashing), User Login (with JWT token generation), User Logout (token clearing), Create Task (title required, description optional), Read Tasks (show only logged-in user's tasks), Update Task (title and/or description by task ID), Delete Task (remove task by task ID), Mark Task Complete/Incomplete (toggle completion status by task ID). All operations MUST respect user data isolation.

### Data Model Consistency
The application MUST maintain two database tables with the following structure:
- User Table: id (Integer PK), email (String unique), hashed_password (String), created_at (DateTime)
- Task Table: id (Integer PK), title (String), description (String), completed (Boolean), user_id (Foreign Key to User.id)
All data MUST be stored persistently in the SQL database with proper relationships maintained.

## User Interface Requirements

### Frontend Technology
- Next.js App Router MUST be used for routing
- Clean, responsive UI with consistent styling
- Proper form validation and error handling
- JWT token management in browser storage
- API calls MUST include authentication tokens

### Page Structure
- `/login` - Login page with email/password form and signup link
- `/signup` - Signup page with email/password form and login link
- `/dashboard` - Dashboard showing welcome message, create task button, and task list
- `/tasks` - Tasks page showing all user tasks with CRUD operations

### UI Design Requirements
- Background color: #f9fafb
- Primary button color: #2563eb
- Text color: #111827
- Success color: #16a34a
- Error color: #dc2626
- All UI elements MUST be clearly visible and accessible
- All buttons MUST have clear labels and appropriate functionality

### Login Page (`/login`)
- Centered form box with email input, password input, and login button
- Link to signup page: "Don't have an account? Sign up"
- After successful login, user MUST be redirected to dashboard

### Signup Page (`/signup`)
- Simple form with email and password inputs
- Validation errors MUST be displayed
- After successful signup, user MUST be redirected to login page

### Dashboard (`/dashboard`)
- Welcome message showing user's email: "Welcome, {user_email} 👋"
- "Create New Task" button
- List of user's tasks with edit/delete/complete options
- Top navigation bar with app name and logout button

### Tasks Page (`/tasks`)
- Each task MUST display: title (bold), description (small text), status (completed/pending)
- Each task MUST have: Edit, Delete, Complete/Incomplete buttons
- User MUST be able to create, read, update, delete, and toggle completion of tasks

## Backend Rules
- FastAPI MUST be used for backend API
- JWT tokens MUST be required for all authenticated endpoints
- Token validation MUST identify the user making the request
- Users MUST only access their own data based on user_id foreign key
- Invalid tokens MUST result in request rejection with 401 status
- All API responses MUST be in JSON format

## Frontend Rules
- No page MUST be accessible without valid authentication token
- JWT tokens MUST be stored securely in browser local storage
- All API calls MUST include the authentication token in headers
- UI MUST update immediately after successful API operations
- Error messages MUST be displayed clearly to users
- UI MUST be simple and clean with no confusing elements

## Security Constitution
- Passwords MUST never be stored in plain text
- Passwords MUST be hashed using proper hashing algorithms
- JWT tokens MUST have appropriate expiration times
- User data MUST be completely isolated (one user cannot access another's data)
- Authentication MUST be required for all sensitive operations
- Database queries MUST use parameterized statements to prevent injection

## Quality Standards
Code MUST be readable and maintainable. Functions MUST be small and focused. No unused code. No commented-out code. All tests MUST pass before deployment. Error handling MUST be comprehensive and user-friendly.

## Verification Criteria
Phase II is considered complete when: The web application runs successfully, All eight required features work correctly (signup, login, logout, create, read, update, delete, complete/incomplete), Database properly stores and retrieves user and task data, User isolation is maintained (users cannot see other users' tasks), The repository contains full spec history, No manual code changes are present, UI meets all specified design requirements.

## Governance
This constitution applies to Phase II. Phase I code remains unchanged. All development must strictly adhere to the rules defined in this constitution. Any deviation invalidates the phase submission. Amendments to this constitution require explicit approval and version increment.

**Version**: 2.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2026-01-05

## Outcome

- ✅ Impact: Updated constitution from Phase I (CLI app) to Phase II (full-stack web app with auth)
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated
- 🔁 Next prompts: Continue with Phase II implementation following new constitution
- 🧠 Reflection: Constitution successfully updated to reflect Phase II requirements with user authentication, database persistence, and Next.js/FastAPI stack

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin Phase II implementation with new constitution