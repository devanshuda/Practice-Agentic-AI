from tool_registry import TOOLS


def execute_plan(steps):

    state = {}

    for step in steps:

        print(f"\nExecuting: {step}")

        if step == "discover_resources":

            result = TOOLS[step]()

            state["resources"] = result

            print(result)

        elif step == "generate_terraform":

            result = TOOLS[step](
                state["resources"]
            )

            state["terraform"] = result

            print(result)

        elif step == "create_pull_request":

            result = TOOLS[step]()

            state["pull_request"] = result

            print(result)

    return state