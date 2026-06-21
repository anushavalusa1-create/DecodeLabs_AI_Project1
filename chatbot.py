print("Welcome to AI Chatbot")
print("Type 'bye' to exit")

while True:

    user = input("You: ")
    user = user.lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine.")

    elif user == "what is your name":
        print("Bot: I am an AI Chatbot.")
    elif user== "im boring":
        print("Bot: Can i tell u a joke?")
    elif user == "yes":
        print("Bot: shall we marry?")
    elif user== "joke of the day ":
        print("finaly u lauhghed")
    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")