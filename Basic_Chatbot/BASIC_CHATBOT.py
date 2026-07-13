print("Welcome to ChatBot!")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I am fine. How about you?")

    elif user == "name":
        print("Bot: I am a chatbot.")

    elif user == "python":
        print("Bot: Python is a programming language.")

    elif user == "ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")