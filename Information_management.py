# Define information management rules and corresponding actions
information_rules = {
    "rule1": {
        "keywords": ["document", "file", "report"],
        "action": "Organize the document in the appropriate category."
    },
    "rule2": {
        "keywords": ["article", "publication", "journal"],
        "action": "Catalog the article under the relevant topic or subject."
    },
    "rule3": {
        "keywords": ["data", "record", "dataset"],
        "action": "Store and manage the data in the specified database or repository."
    },
    "rule4": {
        "keywords": ["knowledge base", "information repository"],
        "action": "Update and maintain the knowledge base with the latest information."
    }
}

def manage_information(input_text):
    """
    Manage information based on predefined rules and user input.
    
    Args:
        input_text (str): User's input text describing the information.
    
    Returns:
        str: Recommended action for managing the information.
    """
    for rule_name, rule_data in information_rules.items():
        keywords = rule_data["keywords"]
        if any(keyword in input_text.lower() for keyword in keywords):
            return rule_data["action"]
    
    # Default action if no rules match
    return "Unable to determine a management recommendation."

def get_user_input():
    """
    Prompt user to enter a description of the information.
    
    Returns:
        str: User's input text describing the information.
    """
    input_text = input("Please describe the information you want to manage: ")
    return input_text

def handle_information_management():
    """
    Handle information management based on user input and expert system rules.
    """
    print("Welcome to the Information Management Expert System")
    input_text = get_user_input()
    action = manage_information(input_text)
    print(f"Based on your input, the recommended action is: {action}")

def main():
    handle_information_management()

if __name__ == "__main__":
    main()
