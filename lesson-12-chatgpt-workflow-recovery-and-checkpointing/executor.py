from state_manager import (
    create_state,
    validate_state,
    save_state
)

from tool_registry import TOOLS


def execute_plan(steps, state=None):

    if state is None:
        state = create_state()

    state["workflow"]["status"] = "running"

    validate_state(state)

    for step in steps:

        try:

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

        except Exception as e:

            print(
                f"Step Failed: {step}"
            )

            state["errors"].append(
                str(e)
            )

            state["execution_history"].append(
                {
                    "step": step,
                    "status": "failed",
                    "error": str(e)
                }
            )

            state["workflow"]["status"] = (
                "failed"
            )

            save_state(state)

            print(
                "Failure Checkpoint Saved"
            )

            return state

    state["workflow"]["status"] = (
        "completed"
    )

    state["workflow"][
        "current_step"
    ] = None

    save_state(state)

    return state

def get_remaining_steps(
    original_steps,
    execution_history
):

    completed_steps = []

    for item in execution_history:

        if item["status"] == "success":

            completed_steps.append(
                item["step"]
            )

    remaining_steps = []

    for step in original_steps:

        if step not in completed_steps:

            remaining_steps.append(
                step
            )

    return remaining_steps