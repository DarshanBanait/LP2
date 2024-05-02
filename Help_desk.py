# Define help desk rules and corresponding actions
help_desk_rules = {
    "rule1": {
        "keywords": ["password"],
        "action": "Reset the user's password."
    },
    "rule2": {
        "keywords": ["network"],
        "action": "Check network connectivity and settings."
    },
    "rule3": {
        "keywords": ["software"],
        "action": "Reinstall or update the software."
    },
    "rule4": {
        "keywords": ["hardware"],
        "action": "Check hardware connections and perform diagnostics."
    },
    "rule5": {
        "keywords": ["email"],
        "action": "Check email settings and configuration."
    },
    "rule6": {
        "keywords": ["printer"],
        "action": "Troubleshoot printer connectivity and driver issues."
    }
}

def resolve_help_desk_issue(user_issue):
    """
    Resolve help desk issue based on predefined rules and user input.
    
    Args:
        user_issue (str): User's reported issue or query.
    
    Returns:
        str: Recommended action or solution for the reported issue.
    """
    for rule_name, rule_data in help_desk_rules.items():
        keywords = rule_data["keywords"]
        if any(keyword in user_issue.lower() for keyword in keywords):
            return rule_data["action"]
    
    # Default action if no rules match
    return "Unable to determine a solution. Please escalate the issue to a human operator."

def get_user_issue():
    """
    Prompt user to enter the reported issue or query.
    
    Returns:
        str: User's reported issue or query.
    """
    user_issue = input("Please describe the issue you are experiencing: ")
    return user_issue

def handle_help_desk_requests():
    """
    Handle multiple help desk requests until user indicates no further problems.
    """
    print("Welcome to the Help Desk Management System")
    while True:
        user_issue = get_user_issue()
        action = resolve_help_desk_issue(user_issue)
        print(f"Based on your input, the recommended action is: {action}")
        
        another_problem = input("Do you have another problem? (yes/no): ").lower()
        if another_problem != "yes":
            break
    
    print("Thank you for using the Help Desk Management System.")

# Main function to execute the help desk management expert system
def main():
    handle_help_desk_requests()

if __name__ == "__main__":
    main()
