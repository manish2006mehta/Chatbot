# Personal Chat assistant Project
import datetime
import time

name = input("Please enter your name: ")

presenthour = datetime.datetime.now().hour
if 5<= presenthour <= 11:
    print(f"Good morning!, {name}")
elif 11< presenthour <= 16:
    print(f"Good Afternoon!, {name}")
elif 16< presenthour <= 19:
    print(f"Good Evening!, {name}")    
else:
    print(f"God Night!, {name}")

    
print("\nWelcome to your Personal Assistant")
print("Let's talk!, Type 'bye' for exit\n")

responses = {
    "hello": "Hi, How can i help you?",
    "how are you": "I'm very fine. Thank you!",
    "who are you": "I'm your personal assistant",
    "motivate me": "Keep going, Every bug of your project makes you better.",
    "happy": "Great to hear that"
}

def getResponse(userquestion):
    userquestion = userquestion.lower()
    for key in responses:
        if key in userquestion:
            return responses[key]
    return "Sorry, I don't understand that yet."

while True:
    user = input("Please ask your question: ")

    if "bye" in user.lower():
        print("Bot: Goodbye! Have a great day 👋")
        break

    reply = getResponse(user)
    print("Bot Response: ", reply)