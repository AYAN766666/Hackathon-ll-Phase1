---
description: "Task list for CLI Todo application implementation"
---

# Tasks: Task CRUD – Phase I (CLI Todo App)

**Input**: Design documents from `/specs/001-task-crud/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks are included as requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python project with UV for dependency management
- [X] T003 [P] Configure linting and formatting tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Task model in src/models/task.py
- [X] T005 Create TaskService in src/services/task_service.py
- [X] T006 [P] Setup in-memory storage in TaskService
- [X] T007 [P] Implement ID generation in TaskService
- [X] T008 Create basic CLI structure in src/cli/main.py
- [X] T009 Setup error handling infrastructure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with required title and optional description

**Independent Test**: Can be fully tested by running the CLI app, selecting "Add Task", entering a title and description, and verifying the task appears in the system with a unique ID and incomplete status.

### Tests for User Story 1 (OPTIONAL - included per spec) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Unit test for Task model creation in tests/unit/test_task.py
- [X] T011 [P] [US1] Unit test for TaskService add_task functionality in tests/unit/test_task_service.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement Task class in src/models/task.py
- [X] T013 [US1] Implement add_task method in src/services/task_service.py
- [X] T014 [US1] Implement Add Task option in CLI menu in src/cli/main.py
- [X] T015 [US1] Add input validation for required title in src/cli/main.py
- [X] T016 [US1] Add success/error messaging for task creation in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P2)

**Goal**: Allow users to see all their tasks with their completion status to understand what needs to be done

**Independent Test**: Can be fully tested by adding some tasks, then selecting "View Tasks" and verifying all tasks display with ID, title, and completion status.

### Tests for User Story 2 (OPTIONAL - included per spec) ⚠️

- [X] T017 [P] [US2] Unit test for TaskService get_all_tasks functionality in tests/unit/test_task_service.py
- [X] T018 [P] [US2] Integration test for View Tasks CLI option in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T019 [P] [US2] Implement get_all_tasks method in src/services/task_service.py
- [X] T020 [US2] Implement View Tasks option in CLI menu in src/cli/main.py
- [X] T021 [US2] Add proper formatting for task display in src/cli/main.py
- [X] T022 [US2] Handle empty task list case in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: Allow users to update the title or description of an existing task to keep information current

**Independent Test**: Can be fully tested by creating a task, then selecting "Update Task", entering a valid ID, and modifying title/description.

### Tests for User Story 3 (OPTIONAL - included per spec) ⚠️

- [X] T023 [P] [US3] Unit test for TaskService update_task functionality in tests/unit/test_task_service.py
- [X] T024 [P] [US3] Integration test for Update Task CLI option in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement update_task method in src/services/task_service.py
- [X] T026 [US3] Implement Update Task option in CLI menu in src/cli/main.py
- [X] T027 [US3] Add input validation for task ID in src/cli/main.py
- [X] T028 [US3] Add error handling for non-existent task ID in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P4)

**Goal**: Allow users to remove completed or unwanted tasks from their list

**Independent Test**: Can be fully tested by creating a task, then selecting "Delete Task", entering the ID, and verifying it's removed.

### Tests for User Story 4 (OPTIONAL - included per spec) ⚠️

- [X] T029 [P] [US4] Unit test for TaskService delete_task functionality in tests/unit/test_task_service.py
- [X] T030 [P] [US4] Integration test for Delete Task CLI option in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T031 [P] [US4] Implement delete_task method in src/services/task_service.py
- [X] T032 [US4] Implement Delete Task option in CLI menu in src/cli/main.py
- [X] T033 [US4] Add error handling for non-existent task ID in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Toggle Task Completion (Priority: P5)

**Goal**: Allow users to mark tasks as complete when finished or mark completed tasks as incomplete if needed

**Independent Test**: Can be fully tested by creating a task, then selecting "Toggle Complete", entering the ID, and verifying status changes.

### Tests for User Story 5 (OPTIONAL - included per spec) ⚠️

- [X] T034 [P] [US5] Unit test for TaskService toggle_complete functionality in tests/unit/test_task_service.py
- [X] T035 [P] [US5] Integration test for Toggle Complete CLI option in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T036 [P] [US5] Implement toggle_complete method in src/services/task_service.py
- [X] T037 [US5] Implement Toggle Complete option in CLI menu in src/cli/main.py
- [X] T038 [US5] Add error handling for non-existent task ID in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Add menu display functionality in src/cli/main.py
- [X] T040 [P] Add input validation for menu selection in src/cli/main.py
- [X] T041 [P] Add graceful exit functionality in src/cli/main.py
- [X] T042 [P] Add error handling for invalid menu selections in src/cli/main.py
- [X] T043 [P] Documentation updates in README.md
- [X] T044 Code cleanup and refactoring
- [X] T045 [P] Additional unit tests (if needed) in tests/unit/
- [X] T046 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

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

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Task model creation in tests/unit/test_task.py"
Task: "Unit test for TaskService add_task functionality in tests/unit/test_task_service.py"

# Launch all implementation for User Story 1 together:
Task: "Implement Task class in src/models/task.py"
Task: "Implement add_task method in src/services/task_service.py"
```

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
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
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