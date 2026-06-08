from state_manager import (
    create_state,
    validate_state,
    save_state
)

from tool_registry import TOOLS


def execute_plan(steps):

    state = create_state()

    state["workflow"]["status"] = "running"

    validate_state(state)

    for step in steps:

        print(f"\nExecuting: {step}")

        state["workflow"]["current_step"] = step

        if step == "discover_resources":

            result = TOOLS[step]()

            state["resources"] = result

        elif step == "generate_terraform":

            result = TOOLS[step](
                state["resources"]
            )

            state["terraform"] = result

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

        validate_state(state)

        save_state(state)

        print(
            "Checkpoint Saved"
        )

    state["workflow"]["status"] = (
        "completed"
    )

    state["workflow"][
        "current_step"
    ] = None

    save_state(state)

    return state