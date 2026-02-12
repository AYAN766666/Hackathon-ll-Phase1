# Research: AI Agent + MCP Server Integration

**Feature**: AI Agent + MCP Server Integration
**Date**: 2026-01-12
**Researcher**: Claude Code

## Executive Summary

This research document covers the investigation and decision-making process for implementing the AI Agent and MCP Server integration. It addresses all technical unknowns and provides rationale for the chosen approaches based on the project constitution and requirements.

## 1. AI Agent Implementation Research

### Decision: Use OpenAI Agents SDK with Gemini AI integration
- **Rationale**: Aligns with constitution requirement for OpenAI SDK and Gemini AI
- **Implementation Approach**: Use OpenAI-compatible API to connect with Gemini AI service
- **Configuration**: Use the specific configuration required by the constitution:

```python
async def main():
    api_key = os.getenv("GEMINI_API_KEY")

    external_client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash",
        openai_client=external_client
    )

    run_config = RunConfig(
         model=model,
         model_provider=external_client,
         tracing_disabled=True
    )
```

### Alternatives Considered:
1. **LangChain**: More complex framework with broader scope than needed
2. **Custom NLP Solutions**: Would require extensive development and maintenance
3. **Other AI Providers**: Not compliant with constitution requirements

## 2. MCP Server Architecture Research

### Decision: Implement MCP server as a bridge between AI agent and FastAPI APIs
- **Rationale**: Required by constitution to avoid direct database access and ensure security
- **Architecture**: MCP server will validate JWT tokens and forward requests to existing APIs
- **Security**: Ensures all requests are properly authenticated and user-isolated

### Alternatives Considered:
1. **Direct API calls from agent**: Would violate security requirements
2. **Separate microservices**: Would complicate the architecture unnecessarily
3. **Client-side AI processing**: Would not meet security requirements

## 3. SQLite Integration Research

### Decision: Use file-based SQLite for AI agent operations
- **Rationale**: Constitution mandates SQLite for AI operations
- **Benefits**: Simple, lightweight, file-based storage for AI session data
- **Implementation**: Store conversation history, agent state, and operational data

### Alternatives Considered:
1. **In-memory storage**: Would lose data on restart
2. **PostgreSQL extension**: Would violate the specific SQLite requirement
3. **External databases**: Would complicate the architecture

## 4. JWT Token Handling Research

### Decision: Validate JWT tokens in MCP server for each request
- **Rationale**: Security requirement from constitution
- **Process**: Extract user_id from JWT and ensure user isolation
- **Error Handling**: Return 401 for invalid tokens

### Alternatives Considered:
1. **Session-based authentication**: Would not be consistent with existing system
2. **API keys**: Would require additional infrastructure

## 5. Frontend Integration Research

### Decision: Add AI agent icon to dashboard with panel overlay
- **Rationale**: Matches UI requirements in constitution
- **Design**: Blue icon (🔵) on dashboard, white background panel (⚪)
- **User Experience**: Accessible only after login, maintains existing UI

### Alternatives Considered:
1. **Separate AI page**: Would disrupt existing UX flow
2. **Always-visible panel**: Would clutter the interface

## 6. Natural Language Processing Research

### Decision: Use AI agent to interpret natural language commands
- **Commands Supported**: Add, view, update, delete, complete tasks
- **Off-topic Handling**: Reject with "Main sirf Todo ke liye hoon."
- **Validation**: Ensure commands map to allowed operations only

### Alternatives Considered:
1. **Structured commands**: Would reduce usability
2. **Voice input**: Would add unnecessary complexity

## 7. Tool Mapping Research

### Decision: Map MCP tools to existing API endpoints
- **create_task**: Maps to POST /api/{user_id}/tasks
- **list_tasks**: Maps to GET /api/{user_id}/tasks
- **update_task**: Maps to PUT /api/{user_id}/tasks/{id}
- **delete_task**: Maps to DELETE /api/{user_id}/tasks/{id}
- **complete_task**: Maps to PATCH /api/{user_id}/tasks/{id}/complete

## 8. Error Handling Research

### Decision: Comprehensive error handling strategy
- **JWT Invalid**: Return 401 Unauthorized
- **Task Not Found**: Return appropriate error message
- **Off-topic Requests**: Politely reject with clear messaging
- **API Failures**: Graceful degradation with informative messages

## 9. Performance Considerations

### Decision: Optimize for response time under 5 seconds
- **Caching**: Minimal caching for AI responses
- **Connection pooling**: For database connections
- **Resource limits**: Appropriate limits for AI processing

## 10. Security Measures

### Decision: Multi-layer security approach
- **JWT validation**: At MCP server level
- **User isolation**: Enforced by user_id extraction
- **Input sanitization**: For all natural language inputs
- **Access controls**: Limited to authenticated users only

## Conclusion

All research findings align with the project constitution and requirements. The chosen approach balances functionality, security, and maintainability while ensuring Phase II functionality remains unchanged.