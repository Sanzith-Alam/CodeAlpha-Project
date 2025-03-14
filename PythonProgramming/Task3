import random
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only required once)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What's on your mind?", "Hey! How can I assist you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great! How about you?", "All good here. How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot. You can call me ChatBot!", "I go by the name ChatBot. Nice to meet you!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! See you soon!", "Take care!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Happy to help!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer basic questions, and help you with simple tasks. Feel free to ask me anything!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! It was nice talking to you."]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def start_chat():
    print("ChatBot: Hello! I'm your friendly chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"ChatBot: {response}")
        else:
            print("ChatBot: I'm not sure how to respond to that. Can you rephrase?")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
