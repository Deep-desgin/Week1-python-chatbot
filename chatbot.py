name = input("Kindly, Enter your name: ")

print("Hello", name + ", welcome to the AI chatbot!")

while True:
    msg = input("You: ")

    if msg == "hi" or msg == "hello":
        print("Hello!")

    elif msg == "how are you":
        print("I am doing great!")

    elif msg == "bye":
        print("Goodbye!")

    elif msg == "exit":
        break

    else:
        print("I don't understand that yet.")