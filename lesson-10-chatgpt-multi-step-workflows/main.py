from tool_registry import TOOLS

state = {}

resources = TOOLS["discover_resources"]()
state["resources"] = resources
print(state)

if not state["resources"]:
    print("No resources found.")
    exit()

terraform_result = TOOLS["generate_terraform"](state["resources"])
state["terraform"] = terraform_result
print(state)

pr_result = TOOLS["create_pull_request"]()
state["pull_request"] = pr_result
print(state)

print("\nWorkflow Complete\n")
print(f"Resources Found: {len(state['resources'])}")
print(
    f"Terraform Generated: "
    f"{state['terraform']['generated']}"
)
print(
    f"Pull Request: "
    f"{state['pull_request']['pr_number']}"
)