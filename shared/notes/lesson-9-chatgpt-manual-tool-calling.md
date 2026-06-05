# Lesson 9 - Manual Tool Calling Agent

## Objective

Build a complete AI agent capable of:

1. Understanding a user's request.
2. Selecting the appropriate tool.
3. Executing the tool.
4. Using the tool output to generate a human-friendly response.

This lesson introduces the core architecture used by modern AI agents.

---

# Concepts Covered

## Tool Calling

Tool calling allows an LLM to interact with external systems.

Without tools, an LLM can only generate text.

With tools, an LLM can:

- Query Azure
- Execute Terraform
- Create ServiceNow tickets
- Read repositories
- Generate reports

### Important Principle

```text
LLM = Reasoning
Tool = Facts and Actions
```

The LLM decides what should happen.

The tool performs the action.

---

## Tool Registry Pattern

A tool registry provides a centralized location for all available tools.

Example:

```python
TOOLS = {
    "get_current_environment": get_current_environment,
    "get_subscription_name": get_subscription_name,
    "get_resource_group_count": get_resource_group_count,
    "get_terraform_version": get_terraform_version,
    "get_current_region": get_current_region
}
```

Benefits:

- Easy to add tools
- Easy to remove tools
- Scalable architecture

---

## System Prompt Design

The system prompt informs the LLM:

- Which tools exist
- What each tool does
- How tool selection should be returned

Example:

```text
TOOL: get_terraform_version
```

The model was instructed to return only tool names when tool execution was required.

---

## Agent Loop

The first agent loop implemented:

```text
Observe
↓
Reason
↓
Act
↓
Observe Result
```

Example:

User:
"What Terraform version is installed?"

↓

LLM:
TOOL: get_terraform_version

↓

Tool:
Terraform v1.13.0

↓

Agent receives result
```

---

# Architecture Implemented

## Phase 1

User Question
↓
LLM
↓
Tool Selection
↓
Tool Execution
↓
Print Result

Example:

```text
User:
What Terraform version is installed?

LLM:
TOOL: get_terraform_version

Tool:
Terraform v1.13.0
```

---

## Phase 2

Added a second LLM call.

Architecture:

```text
User
↓
LLM
↓
Tool Selection
↓
Tool Execution
↓
LLM
↓
Human Friendly Response
```

Example:

### User

```text
What environment are we in?
```

### First LLM Call

```text
TOOL: get_current_environment
```

### Tool Result

```text
Production
```

### Second LLM Call

Input:

```text
User Question:
What environment are we in?

Tool Result:
Production
```

Output:

```text
We are currently operating in the Production environment.
```

---

# Project Structure

```text
lesson-09-manual-tool-calling/
│
├── main.py
├── tools.py
├── tool_registry.py
├── requirements.txt
└── README.md
```

---

# Files Created

## tools.py

Contains tool implementations.

Example:

```python
def get_current_environment():
    return "Production"
```

---

## tool_registry.py

Maps tool names to Python functions.

Example:

```python
TOOLS = {
    ...
}
```

---

## main.py

Responsible for:

1. Accepting user input
2. Calling the LLM
3. Determining tool selection
4. Executing tools
5. Calling the LLM again
6. Returning a final response

---

# Knowledge Check Review

## Why is LLM Routing Better Than Hardcoded If Statements?

Hardcoded logic:

```python
if "subscription" in question:
```

requires constant maintenance.

LLM routing understands intent naturally.

Example:

```text
What Azure subscription are we using?

Which subscription is configured?

What subscription is currently connected?
```

All map to the same tool.

---

## Who Knows the Subscription Name?

Answer:

Tool

Reason:

The LLM should not invent infrastructure facts.

---

## Do New Tools Require Model Retraining?

Answer:

No

Reason:

Adding a tool only requires:

- Updating the registry
- Updating the system prompt

The model itself does not need retraining.

---

## Error Handling

Best Practice:

Tool:
Detects technical errors

Example:

```text
ERROR: Azure API unavailable
```

LLM:
Explains errors to users in natural language

Example:

```text
Unable to retrieve Azure information because the Azure API is currently unavailable.
```

---

# Enterprise AI Agent Lessons

A Terraform Import Agent would use the same pattern:

```text
User
↓
Discover Resources
↓
Compare Terraform State
↓
Generate HCL
↓
Create Pull Request
↓
Summarize Results
```

Tools perform actions.

LLMs provide reasoning and communication.

---

# Single Tool vs Multi-Step Agents

## Single Tool Agent

```text
Question
↓
Tool
↓
Answer
```

Current implementation.

---

## Multi-Step Agent

```text
Question
↓
Plan
↓
Tool 1
↓
Observe
↓
Tool 2
↓
Observe
↓
Tool 3
↓
Final Answer
```

This introduces:

- State
- Planning
- Autonomous decision making

---

# Key Takeaways

1. Agents are more than LLMs.
2. Tools provide actions and facts.
3. LLMs provide reasoning.
4. Tool registries make systems scalable.
5. Multi-step agents require state management.
6. Modern agent frameworks automate patterns that can be implemented manually.

---

# Lesson Completion Status

✅ Tool Registry

✅ Tool Selection

✅ LLM Routing

✅ Tool Execution

✅ Second Reasoning Pass

✅ Agent Loop

✅ Error Handling Concepts

✅ Enterprise Agent Architecture

Lesson 9 Complete