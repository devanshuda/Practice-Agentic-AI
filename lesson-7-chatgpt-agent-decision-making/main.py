import tools

def route_request(user_input):
    user_input = user_input.lower()

    if "environment" in user_input:
        return tools.get_current_environment()

    elif "subscription" in user_input:
        return tools.get_subscription_name()

    elif "resource group" in user_input:
        return tools.get_resource_group_count()
    
    elif "terraform version" in user_input:
        return tools.get_terraform_version()
  
    elif "region" in user_input:
        return tools.get_current_region()

    return "I don't know how to help with that."

if __name__ == "__main__":
  user_input = input("Ask Agent: ")
  result = route_request(user_input)
  print(result)