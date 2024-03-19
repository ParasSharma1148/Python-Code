import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking.",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no worries.", "No problem.",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am an AI and I do not have a physical location. But I can assist you with information!',]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!", "Have a great day!"]
    ],
]

# Create a Chatbot
def chatbot():
    print("Hi! I'm ChatBot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
