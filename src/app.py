from flask import Flask, render_template, request, redirect
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import filters
import sys
import logging
from static.data.training_dict import trainset
import text_to_sql_api as api
import adapter

app = Flask(__name__)
DATABASE_FILE = "medical.sql"

# logging.basicConfig(level=logging.INFO) # uncomment to enable lots of log info in terminal

#### CHATBOT ##########################

# this filter is on by default and stops the chatbot from repeating itself, however with limited responses it means the chatbot repsonds incorrectly to some prompts, this overrides what it does and makes it do nothing
filters.get_recent_repeated_responses = lambda *args, **kwargs: []

# Create a new instance Minerva
bot = ChatBot('Minerva',
    logic_adapters=[
            {
                'import_path': 'adapter.QueryAdapter' # Custom logic adapter to recognise database queries
            },
            {
                'import_path': 'chatterbot.logic.BestMatch', # Best match adapter chooses from Minerva's pretrained answers
                'default_response': "I'm sorry but I don't understand your message, I am still learning. If you don't know what to ask just ask me “What can you do?” and I will be able to show you!",
                'maximum_similarity_threshold': 0.80 # if unconfident in answer Minerva will say she doesn't understand
            }
        ],
    filters=[],
    database_uri = 'sqlite:///static/data/db.sqlite3'
)

#### TRAINING #########################

if "train" in sys.argv:
    trainer = ListTrainer(bot)
    # Training with the trainset imported 
    for resp in trainset:
        query_list = trainset[resp]
        for q in query_list:
                trainer.train([q, resp])
                trainer.train([q.lower(), resp])
                trainer.train([q.upper(), resp])
                trainer.train([q.title(), resp])

#######################################
# FLASK ENDPOINTS

@app.route("/") # Default endpoint to load webpage
def hello_world():
    return render_template('index.html')

@app.route("/get", methods=['POST']) # Get a response to statement
def get_bot_response():
    data = json.loads(request.data) # decode the request from json into a python dict
    userText = data["msg"] # take users message out
    adapter.SQLcheck(data["sql"])   # update the SQL flag

    bot_resp = bot.get_response(userText) # send the users message to Minerva
    
    return_json = {
        "msg" : str(bot_resp)
    }

    data = json.dumps(return_json) # transform the response into json
    return data                     

@app.route("/database", methods=['POST']) # change the database
def database_action():
    global DATABASE_FILE # the database file that is currently loaded
    data = json.loads(request.data) # decode message
    databaseChoice = data["db_name"] # what the user chose to load

    if (databaseChoice != "") and (databaseChoice != DATABASE_FILE): 
        DATABASE_FILE = databaseChoice # update the database variable

    return_json = {"db_name" : DATABASE_FILE} # acknowledgement message
    data = json.dumps(return_json)
    api.swapDB() # swap the loaded database in the backend api file
    return data

if sys.argv[1] == "deploy":
    app.run(host="127.0.0.1", port=5000, debug=False)