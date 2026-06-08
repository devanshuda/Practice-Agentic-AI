def discover_resources():

    return [
        "vnet-prod",
        "storage-prod",
        "keyvault-prod"
    ]


def generate_terraform(resources):

    return {
        "generated": True,
        "resource_count": len(resources)
    }


def create_pull_request():

    return {
        "pr_number": 123,
        "status": "created"
    }