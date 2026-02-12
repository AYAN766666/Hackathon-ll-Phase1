---
description: "Task list for AI Agent + MCP Server Integration"
---

# Tasks: AI Agent + MCP Server Integration

**Input**: Design documents from `/specs/001-ai-agent-mcp-integration/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume web app - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are based on the feature specification and design documents.

  Tasks are organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan with backend/frontend directories
- [x] T002 [P] Initialize Python project with UV for dependency management in backend/
- [x] T003 [P] Install OpenAI Agents SDK and related dependencies with UV
- [x] T004 [P] Install FastAPI and related dependencies with UV
- [x] T005 [P] Install SQLite and SQLModel dependencies with UV
- [x] T006 [P] Set up frontend project structure with Next.js in frontend/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks based on design:

- [x] T007 [P] Install and configure OpenAI Agents SDK for AI agent in backend/src/agents/
- [x] T008 [P] Set up SQLite database for AI agent operations with proper file path
- [x] T009 Configure MCP Server as bridge between AI agent and FastAPI backend
- [x] T010 [P] Implement JWT token verification for AI agent requests
- [x] T011 [P] Create database models for AI agent entities (AI_Agent_Session, User_Request, etc.)
- [x] T012 [P] Set up environment configuration management for GEMINI_API_KEY
- [x] T013 [P] Create utility functions for UUID generation and timestamp handling

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - AI Agent Interaction (Priority: P1) 🎯 MVP

**Goal**: Enable users to interact with the AI agent to manage their todo tasks using natural language.

**Independent Test**: Can be fully tested by sending natural language commands to the AI agent and verifying it performs the correct todo actions.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T014 [P] [US1] Contract test for AI agent endpoint in backend/tests/test_ai_agent_api.py
- [x] T015 [P] [US1] Integration test for natural language processing in backend/tests/integration/test_ai_agent.py

### Implementation for User Story 1

- [x] T016 [P] [US1] Create AI_Agent_Session model in backend/src/models/ai_agent_session.py
- [x] T017 [P] [US1] Create User_Request model in backend/src/models/user_request.py
- [x] T018 [P] [US1] Create MCP_Tool_Call model in backend/src/models/mcp_tool_call.py
- [x] T019 [P] [US1] Create Agent_Response model in backend/src/models/agent_response.py
- [x] T020 [US1] Implement AI agent configuration with Gemini AI settings in backend/src/agents/ai_agent.py
- [x] T021 [US1] Implement MCP server with JWT verification in backend/src/agents/mcp_server.py
- [x] T022 [US1] Implement MCP tools (create_task, list_tasks, etc.) in backend/src/agents/tools.py
- [x] T023 [US1] Create AI agent endpoint in backend/src/api/ai_agent_api.py
- [x] T024 [US1] Add validation and error handling for AI agent requests
- [x] T025 [US1] Add logging for AI agent operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Secure AI Agent Access (Priority: P1)

**Goal**: Ensure users access the AI agent only after authenticating to maintain data security and proper task isolation.

**Independent Test**: Can be tested by attempting to access the AI agent without authentication and verifying it's not accessible.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T026 [P] [US2] Contract test for JWT validation in backend/tests/test_auth.py
- [x] T027 [P] [US2] Integration test for user data isolation in backend/tests/integration/test_security.py

### Implementation for User Story 2

- [x] T028 [P] [US2] Enhance JWT validation middleware to extract user_id in backend/src/middleware/auth.py
- [x] T029 [US2] Implement user_id enforcement in MCP server for data isolation
- [x] T030 [US2] Add user_id validation in all MCP tool calls
- [x] T031 [US2] Implement unauthorized access handling with 401 responses
- [x] T032 [US2] Add security tests for token expiration handling

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - AI Agent Task Operations (Priority: P2)

**Goal**: Enable users to perform various task operations (create, read, update, delete, complete) through the AI agent interface.

**Independent Test**: Each operation can be tested individually by sending specific commands to the AI agent.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T033 [P] [US3] Contract test for task operations via AI agent in backend/tests/test_task_operations.py
- [x] T034 [P] [US3] Integration test for task CRUD operations via AI in backend/tests/integration/test_task_crud.py

### Implementation for User Story 3

- [x] T035 [P] [US3] Enhance MCP tools with proper error handling for invalid task IDs
- [x] T036 [US3] Implement task validation in all MCP tool calls
- [x] T037 [US3] Add proper response formatting for task operations
- [x] T038 [US3] Implement off-topic request rejection with "Main sirf Todo ke liye hoon."
- [x] T039 [US3] Add comprehensive error messages for task operations

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Frontend Integration

**Goal**: Integrate AI agent UI components into the existing dashboard interface.

### Implementation for Frontend Integration

- [x] T040 [P] Create AI agent icon component in frontend/src/components/ai-agent/AgentIcon.tsx
- [x] T041 [P] Create AI agent panel component in frontend/src/components/ai-agent/AgentPanel.tsx
- [x] T042 Integrate AI agent components into dashboard page in frontend/src/pages/dashboard/index.tsx
- [x] T043 Implement AI agent service for API communication in frontend/src/services/ai-agent-service.ts
- [x] T044 Style components with blue icon and white background as specified

---

## Phase 7: Error Handling & Off-topic Requests

**Goal**: Implement proper error handling and off-topic request rejection.

### Implementation for Error Handling

- [x] T045 Implement JWT invalid response handling (401) in backend/src/agents/mcp_server.py
- [x] T046 Implement task not found error messages in backend/src/agents/tools.py
- [x] T047 Implement polite off-topic rejection in backend/src/agents/ai_agent.py
- [x] T048 Add comprehensive error logging and monitoring

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T049 [P] Documentation updates in docs/
- [x] T050 Code cleanup and refactoring
- [x] T051 Performance optimization for AI agent response time
- [x] T052 [P] Additional unit tests (if requested) in backend/tests/unit/
- [x] T053 Security hardening
- [x] T054 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Frontend Integration (Phase 6)**: Depends on backend API completion
- **Error Handling (Phase 7)**: Depends on core functionality
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add Frontend Integration → Test → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence