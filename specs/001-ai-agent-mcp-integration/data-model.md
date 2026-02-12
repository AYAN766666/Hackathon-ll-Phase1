# Data Model: AI Agent + MCP Server Integration

**Feature**: AI Agent + MCP Server Integration
**Date**: 2026-01-12
**Modeler**: Claude Code

## Overview

This document defines the data structures required for the AI Agent and MCP Server integration. It includes both new entities for AI operations and relationships to existing Phase II entities.

## AI Agent Session Entity

### Properties
- **session_id** (UUID, Primary Key)
  - Unique identifier for each AI agent session
  - Generated as UUID4 upon session creation
  - Required: Yes

- **user_id** (Integer, Foreign Key to User.id)
  - Links the session to the authenticated user
  - Retrieved from JWT token validation
  - Required: Yes

- **conversation_history** (JSON)
  - Stores the conversation history between user and AI agent
  - Contains messages, timestamps, and metadata
  - Required: No (can be null initially)

- **created_at** (DateTime)
  - Timestamp when the session was created
  - Automatically set to current time
  - Required: Yes

- **last_interaction_at** (DateTime)
  - Timestamp of the last interaction in this session
  - Updated with each user interaction
  - Required: No (can be null initially)

### Relationships
- Belongs to: User (via user_id foreign key)
- Has many: User Requests (via session_id)
- Has many: Agent Responses (via session_id)
- Has many: MCP Tool Calls (via session_id)

### Validation Rules
- user_id must exist in the User table
- session_id must be unique
- created_at cannot be in the future

## User Request Entity

### Properties
- **request_id** (UUID, Primary Key)
  - Unique identifier for each user request
  - Generated as UUID4 upon creation
  - Required: Yes

- **session_id** (UUID, Foreign Key to AI_Agent_Session.session_id)
  - Links the request to the session
  - Required: Yes

- **content** (Text)
  - The natural language content of the user's request
  - Maximum length: 2000 characters
  - Required: Yes

- **timestamp** (DateTime)
  - When the request was made
  - Automatically set to current time
  - Required: Yes

- **processed_status** (String)
  - Status of request processing: "pending", "processing", "completed", "failed"
  - Default: "pending"
  - Required: Yes

### Relationships
- Belongs to: AI Agent Session (via session_id foreign key)
- Has one: MCP Tool Call (via request_id relationship)

### Validation Rules
- session_id must exist in the AI_Agent_Session table
- content cannot be empty
- processed_status must be one of the allowed values

## MCP Tool Call Entity

### Properties
- **call_id** (UUID, Primary Key)
  - Unique identifier for each tool call
  - Generated as UUID4 upon creation
  - Required: Yes

- **session_id** (UUID, Foreign Key to AI_Agent_Session.session_id)
  - Links the tool call to the session
  - Required: Yes

- **request_id** (UUID, Foreign Key to User_Request.request_id)
  - Links the tool call to the original request
  - Required: Yes

- **tool_name** (String)
  - Name of the MCP tool being called
  - Values: "create_task", "list_tasks", "update_task", "delete_task", "complete_task"
  - Required: Yes

- **parameters** (JSON)
  - Parameters passed to the tool
  - Structure varies by tool type
  - Required: Yes

- **result** (JSON)
  - Result returned by the tool
  - Structure varies by tool type
  - Required: No (null until completed)

- **timestamp** (DateTime)
  - When the tool call was initiated
  - Automatically set to current time
  - Required: Yes

- **status** (String)
  - Status of the tool call: "initiated", "success", "failed", "error"
  - Default: "initiated"
  - Required: Yes

### Relationships
- Belongs to: AI Agent Session (via session_id foreign key)
- Belongs to: User Request (via request_id foreign key)

### Validation Rules
- session_id must exist in the AI_Agent_Session table
- request_id must exist in the User_Request table
- tool_name must be one of the allowed values
- parameters must be valid for the tool type

## Agent Response Entity

### Properties
- **response_id** (UUID, Primary Key)
  - Unique identifier for each agent response
  - Generated as UUID4 upon creation
  - Required: Yes

- **session_id** (UUID, Foreign Key to AI_Agent_Session.session_id)
  - Links the response to the session
  - Required: Yes

- **content** (Text)
  - The AI agent's response to the user
  - Maximum length: 2000 characters
  - Required: Yes

- **timestamp** (DateTime)
  - When the response was generated
  - Automatically set to current time
  - Required: Yes

- **request_id** (UUID, Foreign Key to User_Request.request_id)
  - Links the response to the original request that triggered it
  - Required: Yes

### Relationships
- Belongs to: AI Agent Session (via session_id foreign key)
- Belongs to: User Request (via request_id foreign key)

### Validation Rules
- session_id must exist in the AI_Agent_Session table
- request_id must exist in the User_Request table
- content cannot be empty

## State Transitions

### User Request Processing
1. User Request created with "pending" status
2. Request processed by AI agent
3. MCP Tool Call initiated
4. Tool Call completed with result
5. Agent Response generated
6. User Request status updated to "completed"

### MCP Tool Call Lifecycle
1. MCP Tool Call created with "initiated" status
2. Tool executed against backend API
3. Result captured
4. Status updated to "success" or "failed"

## Indexes

### Performance Indexes
- AI_Agent_Session: index on user_id for quick user lookup
- User_Request: index on session_id for session-based queries
- MCP_Tool_Call: composite index on session_id and timestamp for chronological queries
- Agent_Response: index on session_id for session-based retrieval

## Constraints

### Referential Integrity
- All foreign key relationships must reference existing records
- Deletion of a user should cascade delete their sessions and related data
- Deletion of a session should cascade delete all related requests, responses, and tool calls

### Data Consistency
- All timestamps must be in UTC
- User isolation must be maintained: a session's data can only be accessed by the associated user
- Tool parameters must match the expected schema for each tool type

## Integration with Existing Models

### Relationship to Phase II Models
- AI_Agent_Session.user_id references User.id from Phase II
- MCP Tool Calls ultimately interact with the existing Task table through backend APIs
- All operations respect the existing user_id foreign key relationships in the Task table

This data model ensures proper isolation of user data, maintains the integrity of Phase II functionality, and provides the necessary structures for AI agent operations while adhering to all constitutional requirements.