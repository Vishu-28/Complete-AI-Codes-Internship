#import useful libraries
import random

#define some sample responses
greetings = ["Hello!", "Hi there!", "Greetings!", "Hey There! How can I help you?"]
help_responses = ["Sure, I can help you with that.", "What do you need assistance with?", "I'm here to help!"]
farewells = ["Goodbye!", "See you later!", "Take care!", "Have a great day!"]

#function to run the chatbot
def chatbot_response(user_input):
    """This function generates a response based on user input."""
    user_input = user_input.lower()
    if any(greet in user_input for greet in ["hello", "hi", "hey", "greetings"]):
        return random.choice(greetings)
    elif any(help_word in user_input for help_word in ["help", "assist", "support"]):
        return random.choice(help_responses)
    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you", "thank you"]):
        return random.choice(farewells) 
    elif "your name" in user_input:
        return "Hi! My name is Pixel. I am an AI chatbot."
    elif "how are you" in user_input:
        return "I'm doing well, thank you for asking!\n How do you feel today?" 
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

#main function to run the chatbot
def chatbot():
    print("Hello! I am Pixel, an AI chatbot.. How can I assist you today?")
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Pixel: Goodbye! Have a great day!")
                break
            else:
                # Here you would typically process the user input and generate a response
                # print(f"Chatbot: You said '{user_input}'. How can I help you further?")
                response = chatbot_response(user_input)
                print(f"Pixel: {response}")
    except KeyboardInterrupt:
        print("\nPixel: Program interrupted safely. Bye!")

#running the chatbot 
if __name__ == "__main__":
    chatbot()