from planner import create_plan, parse_plan
from executor import execute_plan

goal = input("Enter Goal: ")

plan_text = create_plan(goal)

print("\nGenerated Plan:\n")
print(plan_text)

steps = parse_plan(plan_text)

state = execute_plan(steps)

print("\nFinal State:\n")
print(state)