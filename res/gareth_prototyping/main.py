from chatterbot import ChatBot
from chatterbot import comparisons
from chatterbot import response_selection
from chatterbot.trainers import ListTrainer
from training_dict import trainset
import sys
import logging

if "log" in sys.argv:
    logging.basicConfig(level=logging.INFO)

n = len(sys.argv)

# Create a new instance of a ChatBot
bot = ChatBot('Minerva',
    logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': "I'm sorry but I don't understand your message, I am still learning. If you don't know what to ask just ask me “What can you do?” and I will be able to show you!",
                'maximum_similarity_threshold': 0.90
            }
        ],
    filters=[],
    )

# empty storage, reset the responses that might be built in, DO NOT RUN EVERYTIME
# bot.storage.drop()

if "train" in sys.argv:
    trainer = ListTrainer(bot)
    # trainer.train("chatterbot.corpus.english")
    # Training with the trainset
    for resp in trainset:
        query_list = trainset[resp]
        for q in query_list:
                trainer.train([q, resp])
                trainer.train([q.lower(), resp])
                trainer.train([q.upper(), resp])
                trainer.train([q.title(), resp])


# Welcome Message
print("\033[95m Welcome to Minerva, start chatting with her below! \033[0m")


## user specified
if "user" in sys.argv:
    # The following loop will execute each time the user enters input
    while True:
        try:
            user_input = input("User" + ": ")
            resp = bot.get_response(user_input)

            print("Minerva: ", resp)
        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
# otherwise read in test file
else:
    for arg in sys.argv[1:]:
        if arg not in ["train", "log"]:
            print("Test File Started: ", arg)
            test_file = sys.argv[1]
            with open(test_file, "r") as f:
                for line in f:
                    query, resp = line.split(":")
                    bot_resp = bot.get_response(query)
                    print("Query Given: ", query)
                    print("Bot Response: ", bot_resp)
                    print("Expected Response: ", resp)