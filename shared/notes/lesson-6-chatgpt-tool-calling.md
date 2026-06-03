# Lesson 6 - Tool Calling

## Why Tools?

LLMs cannot:

* Run Terraform
* Query Azure
* Create ServiceNow tickets

Tools perform these actions.

## Architecture

User
↓
Agent
↓
Tool
↓
Result

## Example

Tool:

def get_subscription():
return "Prod-Subscription"

Agent:

"What subscription am I using?"

Tool Result:

"Prod-Subscription"

## Key Takeaways

Tools allow agents to interact with real systems.
