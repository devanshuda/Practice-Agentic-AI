from ollama import chat


PLANNER_PROMPT = """
You are a workflow planner.

Available tools:

1. discover_resources
2. generate_terraform
3. create_pull_request

Workflow Rules:

- generate_terraform requires discover_resources first.
- create_pull_request requires generate_terraform first.
- Always include prerequisite steps.

Example:

User Goal:
Generate Terraform for unmanaged resources

Plan:

discover_resources
generate_terraform
create_pull_request

Return ONLY the plan.
"""

## User Goal: Generate Terraform for unmanaged resources

def create_plan(user_goal):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": PLANNER_PROMPT
            },
            {
                "role": "user",
                "content": user_goal
            }
        ]
    )

    return response["message"]["content"]


def parse_plan(plan_text):

    steps = []

    valid_steps = [
        "discover_resources",
        "generate_terraform",
        "create_pull_request"
    ]

    for line in plan_text.splitlines():

        line = line.strip()

        # Remove numbering if LLM adds it
        if "." in line:

            parts = line.split(".", 1)

            if parts[0].isdigit():
                line = parts[1].strip()

        if line in valid_steps:
            steps.append(line)

    return steps