import json
import os

STATE_FILE = "workflow_state.json"


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

    return True


def save_state(state):

    with open(
        STATE_FILE,
        "w"
    ) as f:

        json.dump(
            state,
            f,
            indent=4
        )


def load_state():

    if not os.path.exists(
        STATE_FILE
    ):
        return None

    with open(
        STATE_FILE,
        "r"
    ) as f:

        return json.load(f)


def delete_state():

    if os.path.exists(
        STATE_FILE
    ):
        os.remove(
            STATE_FILE
        )