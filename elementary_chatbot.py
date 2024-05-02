import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I am good, thank you!", "I'm doing well.", "All good!"],
    "bye": ["Goodbye!", "Bye!", "Take care!"],
    "help": ["How can I assist you today?", "What do you need help with?"],
    "information": ["Please provide more details.", "I can help with that."],
    "your name": ["I am a chatbot!", "You can call me Chatbot."],
    "customer support": ["You can reach our customer support at support@example.com."],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?"]
}

def get_response(user_input):
    # Check user input against predefined patterns and return a response
    user_input = user_input.lower()

    if user_input in responses:
        return random.choice(responses[user_input])
    elif "name" in user_input:
        return random.choice(responses["your name"])
    elif "support" in user_input:
        return random.choice(responses["customer support"])
    elif "help" in user_input:
        return random.choice(responses["help"])
    elif "information" in user_input or "info" in user_input:
        return random.choice(responses["information"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(responses["bye"])
    elif user_input.startswith("hi") or user_input.startswith("hello"):
        return random.choice(responses["hi"])
    else:
        return random.choice(responses["default"])

def chat_with_user():
    print("Welcome! How can I assist you today?")
    print("Enter 'bye' to exit the chat.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'bye':
            print("Chatbot:", get_response(user_input))
            break

        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_user()
