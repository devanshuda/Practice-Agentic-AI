from ollama import chat
from tool_registry import TOOLS

def execute_tool(tool_name, user_input):
    if tool_name in TOOLS:
        result = TOOLS[tool_name]()
        print("\nTool Result:")
        print(result)
        final_response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": """
                            You are an infrastructure assistant.

                            Use the tool result to answer the user's question.

                            Do not mention tools.
                            Provide a natural response.
                        """
                },
                {
                    "role": "user",
                    "content": f"""
                            User Question:
                            {user_input}

                            Tool Result:
                            {result}
                        """
                }
            ]
        )
        print("\nFinal Answer:")
        print(final_response["message"]["content"])
        
    else:
        print("Unknown tool requested.")

SYSTEM_PROMPT = """
You are an infrastructure assistant.

Available tools:

1. get_current_environment
   Returns current environment.

2. get_subscription_name
   Returns Azure subscription.

3. get_resource_group_count
   Returns number of resource groups.

4. get_terraform_version
   Returns Terraform version.

5. get_current_region
   Returns deployment region.

If a tool is required, respond ONLY with:

TOOL: tool_name

Examples:

User: What environment are we using?
Response:
TOOL: get_current_environment

User: What Terraform version is installed?
Response:
TOOL: get_terraform_version
"""

user_input = input("Ask Agent: ")

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

decision = response["message"]["content"]

print("\nModel Decision:")
print(decision)

if decision.startswith("TOOL:"):
    tool_name = decision.replace("TOOL:", "").strip()
    execute_tool(tool_name, user_input)
else:
    print("No tool requested. Model response:")
    print(decision)