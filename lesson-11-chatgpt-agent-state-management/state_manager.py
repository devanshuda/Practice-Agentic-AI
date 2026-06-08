def create_state():

    return {
        "workflow": {
            "status": "pending",
            "current_step": None
        },

        "resources": [],

        "terraform": {},

        "pull_request": {},

        "errors": [],

        "execution_history": []
    }


def validate_state(state):

    required_keys = [
        "workflow",
        "resources",
        "terraform",
        "pull_request",
        "errors",
        "execution_history"
    ]

    for key in required_keys:

        if key not in state:
            raise ValueError(
                f"Missing state key: {key}"
            )

    if not isinstance(state["workflow"], dict):
        raise ValueError(
            "workflow must be a dictionary"
        )

    if not isinstance(state["resources"], list):
        raise ValueError(
            "resources must be a list"
        )

    if not isinstance(state["terraform"], dict):
        raise ValueError(
            "terraform must be a dictionary"
        )

    if not isinstance(state["pull_request"], dict):
        raise ValueError(
            "pull_request must be a dictionary"
        )

    if not isinstance(state["errors"], list):
        raise ValueError(
            "errors must be a list"
        )

    if not isinstance(
        state["execution_history"],
        list
    ):
        raise ValueError(
            "execution_history must be a list"
        )

    return True