import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary NLTK resources
nltk.download('punkt')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.", "You can call me Chatbot!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Could you please rephrase?"]
    ]
]
def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatbot()
