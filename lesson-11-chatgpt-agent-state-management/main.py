from planner import (
    create_plan,
    parse_plan
)

from executor import (
    execute_plan
)


goal = input(
    "Enter goal: "
)

plan_text = create_plan(goal)

print("\nPLAN:")
print(plan_text)

print("\nRAW PLAN:")
print(plan_text)

steps = parse_plan(plan_text)

print("\nParsed Steps:")
print(steps)

if not steps:

    print(
        "\nNo valid steps found in plan."
    )

else:

    final_state = execute_plan(
        steps
    )

    print("\nFinal State:")
    print(final_state)