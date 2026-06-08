from tool_registry import TOOLS
from state_manager import (
    create_state,
    validate_state
)


def execute_plan(steps):

    state = create_state()

    state["workflow"]["status"] = "running"

    try:

        for step in steps:

            state["workflow"]["current_step"] = step

            # Validate before execution
            validate_state(state)

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

            state["execution_history"].append(
                {
                    "step": step,
                    "status": "success"
                }
            )

            # Validate after execution
            validate_state(state)

        state["workflow"]["status"] = "completed"
        state["workflow"]["current_step"] = None

    except Exception as e:

        state["workflow"]["status"] = "failed"

        state["errors"].append(
            {
                "step": state["workflow"]["current_step"],
                "error": str(e)
            }
        )

        print(f"\nWorkflow Failed: {e}")

    return state