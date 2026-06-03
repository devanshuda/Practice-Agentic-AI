from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Explain Terraform in one paragraph."
        }
    ]
)

print(response["message"]["content"])