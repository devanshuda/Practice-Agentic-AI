from planner import (
    create_plan,
    parse_plan
)

from executor import (
    execute_plan,
    get_remaining_steps
)

from state_manager import (
    load_state,
    delete_state
)

state = load_state()

if (
    state is not None
    and
    state["workflow"]["status"]
    == "failed"
):

    print(
        "\nRecovery checkpoint found."
    )

    choice = input(
        "Resume workflow? (Y/N): "
    )

    if choice.lower() == "y":

        goal = input(
            "\nEnter original goal: "
        )

        plan_text = create_plan(
            goal
        )

        steps = parse_plan(
            plan_text
        )

        remaining_steps = (
            get_remaining_steps(
                steps,
                state[
                    "execution_history"
                ]
            )
        )

        print(
            "\nRemaining Steps:"
        )

        print(
            remaining_steps
        )

        final_state = (
            execute_plan(
                remaining_steps,
                state
            )
        )

        print(
            "\nRecovered State:"
        )

        print(
            final_state
        )

    else:

        delete_state()

        print(
            "\nOld state deleted."
        )

else:

    goal = input(
        "Enter goal: "
    )

    plan_text = create_plan(
        goal
    )

    print("\nPLAN:")

    print(plan_text)

    print(
        "\nRAW PLAN:"
    )

    print(plan_text)

    steps = parse_plan(
        plan_text
    )

    print(
        "\nParsed Steps:"
    )

    print(steps)

    final_state = (
        execute_plan(
            steps
        )
    )

    print(
        "\nFinal State:"
    )

    print(
        final_state
    )