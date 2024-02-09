from flask import Flask, render_template, request, redirect
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import filters
import sys
import logging

app = Flask(__name__)

#### CHATBOT ##########################

# this filter is on by default and stops the chatbot from repeating itself, however with limited responses it means the chatbot repsonds incorrectly to some prompts, this overrides what it does and makes it do nothing
filters.get_recent_repeated_responses = lambda *args, **kwargs: []

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
    database_uri = 'sqlite:///static/data/db.sqlite3'
    )

#######################################

@app.route("/")
def hello_world():
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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
