from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from training_dict import trainset
import sys

n = len(sys.argv)

# Create a new instance of a ChatBot
bot = ChatBot('Minerva',
    logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': "I'm sorry but I don't understand your message, I am still learning. If you don't know what to ask just ask me “What can you do?” and I will be able to show you!",
                'maximum_similarity_threshold': 0.75
            }
        ]
    )

# empty storage, reset the responses that might be built in, DO NOT RUN EVERYTIME
# bot.storage.drop()

if n == 1:
    trainer = ListTrainer(bot)
    # trainer.train("chatterbot.corpus.english")
    # Training with the trainset
    for resp in trainset:
        query_list = trainset[resp]
        for q in query_list:
                trainer.train([q, resp])

# Welcome Message
print("\033[95m Welcome to Minerva, start chatting with her below! \033[0m")


## if no arguments, accept user input from terminal
if n == 1:
    # The following loop will execute each time the user enters input
    while True:
        try:
            user_input = input("User" + ": ")

            print(f"Minerva: {bot.get_response(user_input)}")

        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
# otherwise read in test file
else:
    print("Tests Started")
    test_file = sys.argv[1]
    with open(test_file, "r") as f:
        for line in f:
            query, resp = line.split(":")
            bot_resp = bot.get_response(query)
            print(query)
            print(bot_resp, "&", resp)
            if bot_resp == resp:
                print("SUCCESS")
            else:
                print("FAIL")