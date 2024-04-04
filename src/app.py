from flask import Flask, render_template, request, redirect
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import filters
import sys
import logging
from static.data.training_dict import trainset
import text_to_sql_api as api

app = Flask(__name__)
DATABASE_FILE = "medical.sql"


#### CHATBOT ##########################

# this filter is on by default and stops the chatbot from repeating itself, however with limited responses it means the chatbot repsonds incorrectly to some prompts, this overrides what it does and makes it do nothing
filters.get_recent_repeated_responses = lambda *args, **kwargs: []

# Create a new instance of a ChatBot
bot = ChatBot('Minerva',
    logic_adapters=[
            {
                'import_path': 'adapter.QueryAdapter'
            },
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': "I'm sorry but I don't understand your message, I am still learning. If you don't know what to ask just ask me “What can you do?” and I will be able to show you!",
                'maximum_similarity_threshold': 0.90
            }
        ],
    filters=[],
    database_uri = 'sqlite:///static/data/db.sqlite3'
    )

#### TRAINING #########################

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

#######################################

@app.route("/")
def hello_world():
    print(api.DB_LOADED)
    return render_template('index.html')

@app.route("/get", methods=['POST'])
def get_bot_response():
    data = json.loads(request.data)
    userText = data["msg"]
    
    bot_resp = bot.get_response(userText)    
    
    return_json = {
        "msg" : str(bot_resp)
    }

    data = json.dumps(return_json)
    return data

@app.route("/database", methods=['POST'])
def database_action():
    global DATABASE_FILE
    data = json.loads(request.data)
    databaseChoice = data["db_name"]
    #  <option value="medical.sql">Medical Data (medical.sql)</option>
    #  <option value="financial.sql">Finance Data (financial.sql)</option>

    if (databaseChoice != "") and (databaseChoice != DATABASE_FILE):
        DATABASE_FILE = databaseChoice

    return_json = {"db_name" : DATABASE_FILE}
    data = json.dumps(return_json)
    api.swapDB()
    return data

if sys.argv[1] == "deploy":
    app.run(host="127.0.0.1", port=5000, debug=False)
else:
    for arg in sys.argv[1:]:
        print("Test File Started: ", arg)
        test_file = sys.argv[1]
        with open(test_file, "r") as f:
            for line in f:
                query, resp = line.split(":")
                bot_resp = bot.get_response(query)
                print("Query Given: ", query)
                print("Bot Response: ", bot_resp)
                print("Expected Response: ", resp)
