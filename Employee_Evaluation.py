# Define evaluation rules and their corresponding point values
evaluation_rules = {
    "deadlines_met": (True, 20),
    "expectations_exceeded": (True, 30),
    "initiative_taken": (True, 15),
    "absences": (True, -25),
    "performance_below_expectations": (True, -35)
}

def evaluate_employee_performance(employee_data):
    """
    Evaluate employee performance based on provided data and defined rules.
    
    Args:
        employee_data (dict): Dictionary containing employee data.
            Example: {
                "deadlines_met": True,
                "expectations_exceeded": True,
                "initiative_taken": True,
                "absences": False,
                "performance_below_expectations": False
            }
    
    Returns:
        int: Total score calculated based on evaluation rules.
    """
    total_score = 0
    
    for key, (condition, points) in evaluation_rules.items():
        if employee_data.get(key, False) == condition:
            total_score += points
    
    return total_score

def get_employee_data():
    """
    Prompt user to enter employee data and return as dictionary.
    
    Returns:
        dict: Dictionary containing employee data entered by user.
    """
    employee_data = {}
    n = int(input("Enter the number of employees you want to evaluate: "))
    
    for i in range(n):
        name = input(f"Enter the name of employee {i+1}: ")
        data = {
            "deadlines_met": bool(int(input("Did the employee meet all project deadlines? (Enter 1 for Yes, 0 for No): "))),
            "expectations_exceeded": bool(int(input("Did the employee consistently exceed expectations? (Enter 1 for Yes, 0 for No): "))),
            "initiative_taken": bool(int(input("Did the employee show initiative and take on additional responsibilities? (Enter 1 for Yes, 0 for No): "))),
            "absences": bool(int(input("Was the employee frequently absent or missed deadlines? (Enter 1 for Yes, 0 for No): "))),
            "performance_below_expectations": bool(int(input("Did the employee consistently perform below expectations? (Enter 1 for Yes, 0 for No): ")))
        }
        employee_data[name] = data
    
    return employee_data

def display_evaluation_results(employee_data):
    """
    Display evaluation results for each employee.
    
    Args:
        employee_data (dict): Dictionary containing employee data and scores.
    """
    print("Employee Evaluation Results:")
    for name, data in employee_data.items():
        score = evaluate_employee_performance(data)
        print(f"Employee {name} scored {score} points")

# Main function to execute the employee evaluation system
def main():
    print("Welcome to the Employee Evaluation System")
    employee_data = get_employee_data()
    display_evaluation_results(employee_data)

if __name__ == "__main__":
    main()
