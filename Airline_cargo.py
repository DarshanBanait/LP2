# Define airline scheduling rules and corresponding actions
airline_scheduling_rules = {
    "rule1": {
        "condition": lambda flight, day: flight == "Flight1" and day in ["Monday", "Wednesday", "Friday"],
        "action": "Schedule Flight1 on Monday, Wednesday, and Friday."
    },
    "rule2": {
        "condition": lambda flight, day: flight == "Flight2" and day in ["Tuesday", "Thursday", "Saturday"],
        "action": "Schedule Flight2 on Tuesday, Thursday, and Saturday."
    }
}

# Define cargo scheduling rules and corresponding actions
cargo_scheduling_rules = {
    "rule1": {
        "condition": lambda cargo_type: cargo_type == "Perishable",
        "action": "Prioritize scheduling for perishable cargo."
    },
    "rule2": {
        "condition": lambda cargo_type: cargo_type == "Fragile",
        "action": "Handle fragile cargo with special care."
    }
}

def schedule_airline_flight(flight, day):
    """
    Schedule airline flight based on predefined rules and input parameters.
    
    Args:
        flight (str): Flight identifier (e.g., "Flight1", "Flight2").
        day (str): Day of the week (e.g., "Monday", "Tuesday").
    
    Returns:
        str: Recommended action for scheduling the airline flight.
    """
    for rule_name, rule_data in airline_scheduling_rules.items():
        condition_func = rule_data["condition"]
        if condition_func(flight, day):
            return rule_data["action"]
    
    # Default action if no rules match
    return "Unable to determine a scheduling recommendation."

def allocate_cargo_schedule(cargo_type):
    """
    Allocate cargo schedule based on predefined rules and input cargo type.
    
    Args:
        cargo_type (str): Type of cargo (e.g., "Perishable", "Fragile").
    
    Returns:
        str: Recommended action for allocating the cargo schedule.
    """
    for rule_name, rule_data in cargo_scheduling_rules.items():
        condition_func = rule_data["condition"]
        if condition_func(cargo_type):
            return rule_data["action"]
    
    # Default action if no rules match
    return "Unable to determine a scheduling recommendation for the cargo."

def handle_airline_scheduling():
    """
    Handle airline flight scheduling based on user input and expert system rules.
    """
    print("Welcome to the Airline Scheduling Expert System")
    flight = input("Enter the flight identifier (e.g., Flight1, Flight2): ")
    day = input("Enter the day of the week (e.g., Monday, Tuesday): ")
    action = schedule_airline_flight(flight, day)
    print(f"Based on input, the recommended action is: {action}")

def handle_cargo_scheduling():
    """
    Handle cargo scheduling based on user input and expert system rules.
    """
    print("Welcome to the Cargo Scheduling Expert System")
    cargo_type = input("Enter the type of cargo (e.g., Perishable, Fragile): ")
    action = allocate_cargo_schedule(cargo_type)
    print(f"Based on input, the recommended action is: {action}")

def main():
    print("Welcome to the Expert System Hub")
    
    while True:
        print("\nPlease select which expert system you want to interact with:")
        print("1. Airline Scheduling")
        print("2. Cargo Scheduling")
        print("3. Terminate")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            handle_airline_scheduling()
        elif choice == "2":
            handle_cargo_scheduling()
        elif choice == "3":
            print("Thank you for using the Expert System Hub.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
