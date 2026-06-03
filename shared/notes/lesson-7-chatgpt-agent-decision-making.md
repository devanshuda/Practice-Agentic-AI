# Lesson 7 - Agent Decision Making

## Intent Detection

Determine what the user wants.

Example:

"What Terraform version is installed?"

Intent:

Get Terraform Version

## Router Pattern

User
↓
Router
↓
Tool

## Rule-Based Routing

Example:

if "terraform version" in request:
run_tool()

## Key Takeaways

Decision making determines which tool should be used.
