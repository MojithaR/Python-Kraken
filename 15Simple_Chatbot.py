# Simple_Chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "weather" in user_input:
        return "I can't check the weather yet, but you can use a weather app!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I don't understand that."

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input.lower():
            break
