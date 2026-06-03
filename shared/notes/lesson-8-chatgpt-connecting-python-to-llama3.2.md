# Lesson 8 - Connecting Python to Ollama

## Why Ollama?

Benefits:

* Free
* Local execution
* No API cost
* Good for learning

## Installation

ollama pull llama3.2

## Python Integration

from ollama import chat

response = chat(
model="llama3.2",
messages=[
{
"role": "user",
"content": "Explain Terraform"
}
]
)

## Architecture

User
↓
Python
↓
Ollama
↓
LLM Response

## Key Takeaways

Ollama enables local AI development.
