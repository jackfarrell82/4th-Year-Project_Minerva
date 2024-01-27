from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new instance of a ChatBot
bot = ChatBot('Minerva')

trainer = ListTrainer(bot)
trainer.train("chatterbot.corpus.english")

with open("training_data.txt", "r") as f:
    while True:
        query = f.readline().strip()
        resp = f.readline().strip()
        if not resp: break

        trainer.train([query, resp])

name=input("Enter Your Name: ")

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input(name + ": ")

        print(f"Minerva: {bot.get_response(user_input)}")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break