import unittest
import difflib
import sys
import os
from dotenv import load_dotenv
sys.path.append('../')

import text_to_sql_api as api
from text_to_sql_api import *

import requests
import json

load_dotenv("../config.env")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("DB_PORT")
HOST = os.getenv("DB_HOST")
PASSWORD = os.getenv("DB_PASSWORD")


api.config["password"] = PASSWORD
api.config["host"] = HOST
api.config['user'] = DB_USER
api.headers['Authorization'] = AUTH_TOKEN

api.config['database'] = api.database_M
api.data['schema'] = api.schema_M


class TestTextToSQL(unittest.TestCase):
    def test_changeDB(self):
        self.assertEqual(api.DB_LOADED, "metabolic_syndrome")
        self.assertEqual(api.SCHEMA, "metabolic_syndrome (seqn: int, Age: int, Sex: text, Marital: text, Income: text, Race: text, WaistCirc: double, BMI: double, Albuminuria: int, UrAlbCr: double, UricAcid: double, BloodGlucose: int, HDL: int, Triglycerides: int, MetabolicSyndrome: int)")
        swapDB()
        self.assertEqual(api.DB_LOADED, "financial")
        self.assertEqual(api.SCHEMA,"indexprocessed (Index: text, Date: text, Open: double, High: double, Low: double, Close: double, Adj Close: double, Volume: double, CloseUSD: double)")
        swapDB()
        self.assertEqual(api.DB_LOADED, "metabolic_syndrome")
        self.assertEqual(api.SCHEMA, "metabolic_syndrome (seqn: int, Age: int, Sex: text, Marital: text, Income: text, Race: text, WaistCirc: double, BMI: double, Albuminuria: int, UrAlbCr: double, UricAcid: double, BloodGlucose: int, HDL: int, Triglycerides: int, MetabolicSyndrome: int)")

    def test_toSQL_MEDICAL(self):
        api.config['database'] = api.database_M
        api.data['schema'] = api.schema_M

        example_prompt = "how many age are under 40"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*)  FROM metabolic_syndrome  WHERE Age < 40;"))

        example_prompt = "how many have a marital status of single"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*)  FROM metabolic_syndrome  WHERE Marital = 'Single';"))

        example_prompt = "show me all the records for Males"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT *  FROM metabolic_syndrome  WHERE Sex = 'Male';"))


    def test_toSQL_FINANCIAL(self):
        api.config['database'] = api.database_F
        api.data['schema'] = api.schema_F
    
        example_prompt = "how many have a high price greater than 700"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*) FROM indexprocessed WHERE High > 700;"))
        
        example_prompt = "how many close at over 2000"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*) FROM indexprocessed WHERE Close > 2000;"))

        example_prompt = "what trades have 0 volume"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT * FROM indexprocessed WHERE Volume = 0;"))

class TestMinervaPrompts(unittest.TestCase):
    def test_Greetings(self):
        self.assertEqual(minerva("hello"), "Hi there, I am Minerva, how can I help you?")

        self.assertEqual(minerva("hey there"), "Hi there, I am Minerva, how can I help you?")

        self.assertEqual(minerva("howdy"), "Hi there, I am Minerva, how can I help you?")

        self.assertEqual(minerva("Sup"), "Hi there, I am Minerva, how can I help you?")

        self.assertEqual(minerva("What's up"), "Hi there, I am Minerva, how can I help you?")

    def test_Questions(self):
        # what are you? What can you do?
        self.assertEqual(minerva("Who are you?"), "My Name is Minerva, I am a chatbot created by Gareth & Jack, I can help you access data in your databases")
        self.assertEqual(minerva("What are you?"), "My Name is Minerva, I am a chatbot created by Gareth & Jack, I can help you access data in your databases")
        self.assertEqual(minerva("What is this?"), "My Name is Minerva, I am a chatbot created by Gareth & Jack, I can help you access data in your databases")
        self.assertEqual(minerva("What is Minerva"), "My Name is Minerva, I am a chatbot created by Gareth & Jack, I can help you access data in your databases")
        self.assertEqual(minerva("Who is there?"), "My Name is Minerva, I am a chatbot created by Gareth & Jack, I can help you access data in your databases")

        self.assertEqual(minerva("What can you do?"), "I am a database assistance bot, I can help you retrieve and filter data from the loaded database. Some of the things I can do are - XXX - XXX Try asking me something now!")
        self.assertEqual(minerva("What functions do you do?"), "I am a database assistance bot, I can help you retrieve and filter data from the loaded database. Some of the things I can do are - XXX - XXX Try asking me something now!")
        self.assertEqual(minerva("What stuff can you do?"), "I am a database assistance bot, I can help you retrieve and filter data from the loaded database. Some of the things I can do are - XXX - XXX Try asking me something now!")
        self.assertEqual(minerva("What can you do with the database?"), "I am a database assistance bot, I can help you retrieve and filter data from the loaded database. Some of the things I can do are - XXX - XXX Try asking me something now!")

    def test_Help(self):
        self.assertEqual(minerva("I am stuck"), "I'm very sorry you are struggling to get what you want, I am still in beta and learning new things. If you want to know what I can do at the moment just ask me “What can you do?”")
        self.assertEqual(minerva("I need help"), "I'm very sorry you are struggling to get what you want, I am still in beta and learning new things. If you want to know what I can do at the moment just ask me “What can you do?”")
        self.assertEqual(minerva("Help"), "I'm very sorry you are struggling to get what you want, I am still in beta and learning new things. If you want to know what I can do at the moment just ask me “What can you do?”")

    def test_Submission(self):
        self.assertEqual(minerva("How do you work?"), "To submit a query to the database simple enter the word 'Query' followed by your query, I will send this to the database and return the results right to you! I can also answer some other simple questions, ask me what I can do to find them.")
        self.assertEqual(minerva("How do I submit a query?"), "To submit a query to the database simple enter the word 'Query' followed by your query, I will send this to the database and return the results right to you! I can also answer some other simple questions, ask me what I can do to find them.")
        self.assertEqual(minerva("How to I ask the database something"), "To submit a query to the database simple enter the word 'Query' followed by your query, I will send this to the database and return the results right to you! I can also answer some other simple questions, ask me what I can do to find them.")
        


def minerva(prompt):
    Minerva_url = 'http://127.0.0.1:5000/get'
    data = {'msg': ''}
    data['msg'] = prompt
    response = requests.post(Minerva_url, json=data)
    resp_dict = json.loads(response.text)
    reply = resp_dict['msg']
    return reply

def string_similar(string1, string2, threshold=0.8):
    similarity = difflib.SequenceMatcher(None, string1, string2).ratio()
    
    if similarity < threshold:
        print("\n" + string1 + " != " + string2)
   
    return similarity >= threshold
        
if __name__ == '__main__':
    unittest.main()