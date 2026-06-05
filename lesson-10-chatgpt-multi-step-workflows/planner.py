from ollama import chat


PLANNER_PROMPT = """
You are a workflow planner.

Available tools:

1. discover_resources
2. generate_terraform
3. create_pull_request

Return ONLY a plan.

Example:

User Goal:
Generate Terraform for unmanaged resources

PLAN:
discover_resources
generate_terraform
create_pull_request
"""


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

    for line in plan_text.splitlines():

        line = line.strip()

        if line in [
            "discover_resources",
            "generate_terraform",
            "create_pull_request"
        ]:
            steps.append(line)

    return steps