---
id: 001
title: "Hackathon Phase III Constitution"
stage: constitution
date_iso: 2026-01-12
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: "/sp.constitution"
labels: ["constitution", "hackathon", "phase-iii", "ai-agent", "mcp-server"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
  - ".specify/templates/plan-template.md"
  - ".specify/templates/spec-template.md"
  - ".specify/templates/tasks-template.md"
tests_yaml: []
---

# Hackathon Phase III Constitution Update

## User Input

```
Hackathon II - Phase III Constitution
AI Agent Integrated Todo Application
📌 Phase III Overview

Phase III ka maqsad Phase II ke Todo Web Application ke upar AI Agent banana hai.

Is phase mein:

Phase II ka koi bhi feature delete ya replace nahi hoga

AI agent additional helper ke taur par kaam karega

Agent Todo management ke ilawa kisi aur cheez ka jawab nahi dega

🧱 Phase II Foundation (Already Completed)

Phase II mein following system already maujood hai:

✅ Frontend: Next.js Todo Web Application

✅ Backend: FastAPI (Python)

✅ Database: Neon PostgreSQL

✅ Authentication: JWT (Login / Signup)

✅ Todo Features:

Task Add

Task View

Task Edit

Task Delete

Task Complete

⚠️ Constitution Rule:
Phase III mein Phase II ke backend, APIs, database, auth ya UI ka koi bhi hissa delete ya change nahi kiya jayega.

🤖 Phase III ka Naya Feature: AI Agent
AI Agent kahan banega?

AI agent Phase II ke system ke andar integrate hoga

Agent backend aur frontend dono se connected hoga

🧠 AI Agent ka Role

AI agent:

User ke messages samjhega

Sirf Todo related kaam karega

Khud se task likh sakta hai

Existing APIs ko call karega

Off-topic baaton se mana karega

Example:

User: "Task add kar do"
Agent: "Task add ho gaya"

User: "Tum mujhe joke sunao"
Agent: ❌ "Main sirf Todo tasks ke liye hoon"

⚙️ AI Agent Backend (Phase III - Backend Flow)
Technologies:

Python

FastAPI

OpenAI Agents SDK

Backend ka kaam:

User ka message receive karna

OpenAI SDK ke zariye AI agent ko dena

Agent decide karega:

Task add

Task delete

Task view

Task edit

Agent FastAPI ke existing Todo APIs ko call karega

API response wapas agent ko milega

Agent ka reply frontend ko bheja jayega

⚠️ Agent:

Database ko direct access nahi karega

Sirf FastAPI APIs use karega

🔗 Backend Integration Rule

AI agent Phase II ke FastAPI backend ke sath hi kaam karega

Koi naya backend replace nahi hoga

APIs bilkul same rahengi

🖥️ Frontend Integration (Phase III - UI)
Kab agent show hoga?

User login hone ke baad

Dashboard page par

AI Agent UI Design

AI agent Todo dashboard ke andar show hoga

Ek icon hoga 🤖

Icon par click karne se agent open hoga

🎨 Agent UI Colors

🔵 Blue → Header / Icon

⚪ White → Background

Clean aur simple design

Phase II ke color theme ke sath match karega

🧩 AI Agent Features (Frontend se)

Agent ye kaam kar sakta hai:

Task add karna

Task delete karna

Task view karna

Task edit karna

Task complete / incomplete

Sab commands chat ke zariye hongi.

🔐 Authentication Rule

Agent sirf logged-in user ke liye kaam karega

Login ke baghair agent accessible nahi hoga

JWT ke zariye user identify hoga

Har task usi user ke data par apply hoga

🚫 Agent Limitations (Strict Rules)

AI agent:

❌ General chat nahi karega

❌ Kisi aur topic par baat nahi karega

❌ Database ko direct access nahi karega

❌ Phase II ka data delete ya corrupt nahi karega

🛠️ Development Rules (Hackathon Compliance)

❌ Manual coding allowed nahi

✅ Spec-driven development follow kHackathon II - Phase III Constitution
AI Agent + MCP Server Integrated Todo Application
📌 Phase III Overview

Phase III mein Phase II ke Todo Web Application ke upar:

Ek AI Agent

Aur ek MCP Server
integrate kiya gaya hai.

Yeh dono mil kar user ke natural language commands ko real Todo actions mein convert karte hain.

⚠️ Phase II ka koi bhi feature delete ya modify nahi kiya gaya.

🧱 Phase II Foundation (Untouched)

Phase II already provide karta hai:

Next.js frontend

FastAPI backend (Python)

Todo REST APIs

JWT Authentication

Neon PostgreSQL database

⚠️ Constitution Rule:
Phase III mein Phase II ka koi code remove nahi hoga.

🤖 AI Agent (Phase III)
AI Agent ka Kaam

AI agent:

User ka message samjhta hai

Decide karta hai kaunsa Todo action chahiye

MCP Server ke tools use karta hai

Direct backend ya database ko access nahi karta

AI agent:

OpenAI Agents SDK use karta hai

Python mein implement hota hai

Sirf Todo related replies deta hai

🧩 MCP Server (Phase III ka Core Part)
MCP Server ka Role (BOHOT IMPORTANT ⚠️)

MCP Server:

AI agent aur FastAPI backend ke darmiyan bridge hai

Todo APIs ko MCP tools mein convert karta hai

JWT verify karta hai

user_id enforce karta hai

Security aur boundaries maintain karta hai

👉 AI agent sirf MCP tools ke zariye backend se baat karta hai.

MCP Server kya kya karta hai?

AI agent se tool request receive karta hai

JWT token verify karta hai

user_id extract karta hai

Correct FastAPI Todo API call karta hai

API response AI agent ko return karta hai

🔧 MCP Tools (Todo Operations)

MCP server following tools provide karta hai:

Tool NameBackend API
create_taskPOST /api/{user_id}/tasks
list_tasksGET /api/{user_id}/tasks
update_taskPUT /api/{user_id}/tasks/{id}
delete_taskDELETE /api/{user_id}/tasks/{id}
complete_taskPATCH /api/{user_id}/tasks/{id}/complete
⚙️ Backend Flow (Phase III)

Backend: FastAPI (Python)

AI agent aur MCP server isi backend ke andar run karte hain

Database ko direct access nahi hota

Sirf existing APIs use hoti hain

🖥️ Frontend Integration (Next.js + TailwindCSS)
Agent kab show hota hai?

User ke login hone ke baad

Todo Dashboard par

Agent UI

Dashboard par ek AI Agent icon (🔵 Blue)

Icon click karne par AI chat panel open hota hai

Chat UI:

Background: ⚪ White

Header/Icon: 🔵 Blue

Error/Delete warnings: 🔴 Red

🧠 Agent ke Allowed Actions

Agent yeh kaam kar sakta hai:

Task add

Task delete

Task view

Task edit

Task complete

Off-topic request par agent mana karega.

🔐 Authentication & Security

JWT har AI request ke sath required

MCP server JWT validate karta hai

user_id enforce hota hai

Agent sirf logged-in user ke tasks access karta hai

🚫 Strict Agent & MCP Rules

❌ Agent direct DB access nahi karega

❌ Agent FastAPI APIs ko bypass nahi karega

❌ MCP server bina JWT ke kaam nahi karega

❌ Phase II ka data delete ya corrupt nahi hoga

🏗️ Complete System Architecture
User (Login)
   ↓
Next.js Dashboard (TailwindCSS)
   ↓
AI Agent Icon (Blue)
   ↓
AI Agent backend me databse neon db nh balke Sqlite databse use hora hoga file base databse hoga or han openai ka package use krna uv ka package ke agenr Ai agent bana na Uv ka insatt krna phir use krna uv ke package ke andr Ai agent bana na or hn configration gemini ki krna package openai ka use krna async def main():
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
 ye confiration krna
```

## Response Summary

Updated the project constitution to reflect Phase III requirements for AI Agent and MCP Server integration. The constitution now includes detailed sections for:

- AI Agent Constitution (technology stack, capabilities, limitations)
- MCP Server Constitution (role, tools, enforcement)
- AI Agent Integration Rules (backend/frontend integration)
- Authentication & Security for AI (JWT requirements, data isolation)

Also updated dependent templates (plan, spec, tasks) to align with the new constitutional requirements. The updated constitution maintains all Phase II functionality while adding the AI agent and MCP server integration requirements.

## Outcome

The constitution has been successfully updated to version 3.0.0, reflecting the transition from Phase II to Phase III with AI Agent and MCP Server integration. All templates have been updated to maintain consistency with the new constitutional requirements.