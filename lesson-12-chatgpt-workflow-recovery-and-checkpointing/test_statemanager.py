from state_manager import (
    create_state,
    save_state,
    load_state
)

state = create_state()

state["resources"] = [
    "vnet-prod"
]

save_state(state)

loaded = load_state()

print(loaded)