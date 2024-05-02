# Define trading rules and corresponding actions
trading_rules = {
    "rule1": {
        "condition": "stock_price > moving_average",
        "action": "buy"
    },
    "rule2": {
        "condition": "rsi < 30",
        "action": "buy"
    },
    "rule3": {
        "condition": "stock_price < moving_average",
        "action": "sell"
    },
    "rule4": {
        "condition": "rsi > 70",
        "action": "sell"
    }
}

def evaluate_trading_decision(stock_data):
    """
    Evaluate trading decision based on predefined rules and stock data.
    
    Args:
        stock_data (dict): Dictionary containing stock data attributes.
            Example: {
                "stock_price": 100,
                "moving_average": 90,
                "rsi": 25
            }
    
    Returns:
        str: Trading action ("buy", "sell", or "hold") based on evaluation rules.
    """
    for rule_name, rule_data in trading_rules.items():
        condition = rule_data["condition"]
        # Evaluate the condition using eval() (Note: Use with caution for security reasons)
        if eval(condition, {}, stock_data):
            return rule_data["action"]
    
    # Default action if no rules match
    return "hold"

def get_stock_data():
    """
    Prompt user to enter stock data attributes and return as dictionary.
    
    Returns:
        dict: Dictionary containing stock data entered by user.
    """
    stock_data = {}
    stock_data["stock_price"] = float(input("Enter current stock price: "))
    stock_data["moving_average"] = float(input("Enter moving average price: "))
    stock_data["rsi"] = float(input("Enter RSI (Relative Strength Index): "))
    return stock_data

def display_trading_decision(stock_data):
    """
    Display trading decision based on stock data evaluation.
    
    Args:
        stock_data (dict): Dictionary containing stock data attributes.
    """
    action = evaluate_trading_decision(stock_data)
    print(f"Based on evaluation, you should {action} the stock.")

# Main function to execute the stock market trading expert system
def main():
    print("Welcome to the Stock Market Trading Expert System")
    stock_data = get_stock_data()
    display_trading_decision(stock_data)

if __name__ == "__main__":
    main()
