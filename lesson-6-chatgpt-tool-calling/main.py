import tools
message = str(input())
if message == "environment":
  print(tools.get_current_environment())
elif message == "subscription":
  print(tools.get_subscription_name())
elif message == "resource groups":
  print(tools.get_resource_group_count())
else:
  print("wrong input")
