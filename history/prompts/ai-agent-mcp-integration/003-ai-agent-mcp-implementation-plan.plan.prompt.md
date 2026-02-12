---
id: 003
title: "AI Agent MCP Implementation Plan"
stage: plan
date_iso: 2026-01-12
surface: agent
model: claude-sonnet-4-5-20250929
feature: ai-agent-mcp-integration
branch: 001-ai-agent-mcp-integration
user: user
command: "/sp.plan"
labels: ["plan", "ai-agent", "mcp-server", "todo-app", "architecture"]
links:
  spec: "specs/001-ai-agent-mcp-integration/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/001-ai-agent-mcp-integration/plan.md"
  - "specs/001-ai-agent-mcp-integration/research.md"
  - "specs/001-ai-agent-mcp-integration/data-model.md"
  - "specs/001-ai-agent-mcp-integration/contracts/ai-agent-api.yaml"
  - "specs/001-ai-agent-mcp-integration/quickstart.md"
tests_yaml: []
---

# AI Agent + MCP Server Implementation Plan

## User Input

```
🧭 PHASE III - FULL EXECUTION PLAN
AI Agent + MCP Server for Todo App
🔒 GOLDEN RULE (Sab se pehle)

Phase II ka koi bhi feature, code, API, database, UI delete ya replace nahi hoga.

Phase III sirf ek extra intelligent layer add karega.

STEP 1️⃣ - Repo & Structure Ready Karo
Kya karna hai

Phase II ka repo same rakho

Sirf naye folders add karo:

/specs/
  ├── sp.specify.md
  ├── features/
  │     └── agent.md
  ├── api/
  │     └── mcp-tools.md
  └── architecture.md

Kya nahi karna

❌ Phase II files delete
❌ Backend refactor
❌ API rename

STEP 2️⃣ - Constitution Lock Karo
Kya karna hai

README.md mein likho:

Agent sirf Todo ka kaam karega

Off-topic request reject hogi

MCP server mandatory hai

JWT har request ke sath hoga

Kya nahi karna

❌ General chatbot banana
❌ Multi-purpose AI banana

STEP 3️⃣ - Agent Scope Define Karo (BOHOT IMPORTANT)
Agent yeh karega ✅

Task add

Task view

Task update

Task delete

Task complete / incomplete

Agent yeh nahi karega ❌

Joke

General Q&A

Advice

Weather

Kisi aur app ka kaam

Rule

Agar Todo se bahar sawal aaye:

"Main sirf Todo management ke liye hoon."

STEP 4️⃣ - MCP Server ka Plan
MCP Server kya karega

AI Agent ↔ FastAPI APIs bridge

Tools provide karega

JWT verify karega

user_id enforce karega

MCP Server kya nahi karega

❌ Database direct access
❌ Business logic change

STEP 5️⃣ - MCP Tools Define Karo
Tools list:
ToolKaam
create_taskTask add
list_tasksTasks show
update_taskTask edit
delete_taskTask delete
complete_taskTask complete
Rule

Har tool ek existing API call kare

user_id JWT se aaye

STEP 6️⃣ - Backend Agent Flow (Python + FastAPI)
Flow:

User message aaye

JWT validate ho

Message agent ko jaye

Agent decide kare action

Agent MCP tool call kare

MCP API call kare

Response wapas aaye

Kya nahi karna

❌ Agent ko DB se connect
❌ Agent ko auth bypass karwana

STEP 7️⃣ - Frontend Agent Integration (Next.js + Tailwind)
Kya karna hai

Dashboard par agent icon show karo

Icon color: 🔵 Blue

Background: ⚪ White

Agent kab dikhe

Sirf login ke baad

Dashboard page par

Kya nahi karna

❌ Login page par agent
❌ Existing buttons remove

STEP 8️⃣ - User Interaction Rules
User message:

"Task add karo"

Agent:

Sahi tool call kare

Confirmation de

User message:

"Tum kon ho?"

Agent:

❌ "Main sirf Todo ke liye hoon."

STEP 9️⃣ - Authentication & Security
Kya karna hai

JWT har AI request ke sath

MCP server JWT verify kare

Kya nahi karna

❌ Hardcoded user_id
❌ Public agent access

STEP 🔟 - Error Handling Plan
CaseResponse
JWT invalid401
Task not foundError message
Off-topicReject politely
STEP 1️⃣1️⃣ - Testing Plan (Judge Ready)
Test commands:

"Task add karo"

"Meri tasks dikhao"

"Task delete karo"

"Joke sunao" ❌

Judge dekhna chahte hain:

Focus

Security

Discipline

STEP 1️⃣2️⃣ - What NOT To Add (Very Important)

❌ Vector database
❌ ChatKit
❌ New auth system
❌ Extra AI features
❌ Auto background jobs

STEP 1 jab phase 3 bano gey Ai agent to uv ka package use krna uv ke andr Ai agnt bana na or configration gemini ki krna keo ham ham gemini ki api key use kre gey pckage Openai ka use krna gemini ki configration ase ho gey async def main():
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
 or Neon db nh balke Sqlite database use hoga file base database
```

## Response Summary

Created a comprehensive implementation plan for the AI Agent + MCP Server integration. The plan includes:

- Detailed technical context with all required technologies
- Complete constitution check ensuring all requirements are met
- Project structure with clear separation of concerns
- Phase 0 research document covering all technical decisions
- Data model defining entities for AI operations
- API contracts for the AI agent endpoint
- Quickstart guide for setup and usage

The implementation follows all constitutional requirements including:
- Using OpenAI Agents SDK with Gemini AI
- Implementing MCP server as a bridge
- Using SQLite for AI agent operations
- Maintaining all Phase II functionality
- Enforcing JWT authentication
- Rejecting off-topic requests

## Outcome

Successfully created the complete implementation plan with all supporting documents. The plan is ready for the task generation phase where individual implementation tasks will be created.