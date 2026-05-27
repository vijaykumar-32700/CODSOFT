print("=== Smart Chatbot ===")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if "hi" in user or "hello" in user:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I am good. How can I help you?")

    elif "name" in user:
        print("Bot: My name is SimpleBot.")

    elif "course" in user:
        print("Bot: I can help with basic programming questions.")

    elif "python" in user:
        print("Bot: Python is an easy and powerful programming language.")

    elif "thanks" in user:
        print("Bot: You're welcome!")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")