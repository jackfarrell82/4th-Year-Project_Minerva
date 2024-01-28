from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from training_dict import trainset

# Create a new instance of a ChatBot
bot = ChatBot('Minerva',
    logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': "I'm sorry but I don't understand your message, I am still learning. If you don't know what to ask just ask me “What can you do?” and I will be able to show you!",
                'maximum_similarity_threshold': 0.90
            }
        ]
    )

# empty storage, reset the responses that might be built in, DO NOT RUN EVERYTIME
# bot.storage.drop()

trainer = ListTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Training with the trainset
for resp in trainset:
    query_list = trainset[resp]
    for q in query_list:
        trainer.train([q, resp])

# Welcome Message
print("\033[95m Welcome to Minerva, start chatting with her below! \033[0m")

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input("User" + ": ")

        print(f"Minerva: {bot.get_response(user_input)}")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break