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
        self.assertEqual(True, string_similar(toSQL(example_prompt)[0], "SELECT COUNT(*)  FROM metabolic_syndrome  WHERE Age < 40;"))

        example_prompt = "how many have a marital status of single"
        self.assertEqual(True, string_similar(toSQL(example_prompt)[0], "SELECT COUNT(*)  FROM metabolic_syndrome  WHERE Marital = 'Single';"))

        example_prompt = "show me all the records for Males"
        self.assertEqual(True, string_similar(toSQL(example_prompt)[0], "SELECT *  FROM metabolic_syndrome  WHERE Sex = 'Male';"))


    def test_toSQL_FINANCIAL(self):
        api.config['database'] = api.database_F
        api.data['schema'] = api.schema_F
    
        example_prompt = "how many have a high price greater than 700"
        self.assertEqual(True, string_similar(toSQL(example_prompt)[0], "SELECT COUNT(*) FROM indexprocessed WHERE High > 700;"))
        
        example_prompt = "how many close at over 2000"
        self.assertEqual(True, string_similar(toSQL(example_prompt)[0], "SELECT COUNT(*) FROM indexprocessed WHERE Close > 2000;"))

        example_prompt = "what trades have 0 volume"
        self.assertEqual(True, string_similar(toSQL(example_prompt)[0], "SELECT * FROM indexprocessed WHERE Volume = 0;"))

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

        self.assertEqual(minerva("What can you do?"), "I am a chatbot that assists with accessing databases, I can help you retrieve and filter data from the databases that are loaded. <br> You don't need any SQL knowledge with my help, try submitting a query by sending me 'Query: <i>your query here</i>' <br> I can also answer some simple questions about the databases and SQL, ask me 'What is SQL' or 'What datasets are available'<br> You can also view some starter tips and information by pressing the help icon at the top right of our chat.")
        self.assertEqual(minerva("What functions do you do?"), "I am a chatbot that assists with accessing databases, I can help you retrieve and filter data from the databases that are loaded. <br> You don't need any SQL knowledge with my help, try submitting a query by sending me 'Query: <i>your query here</i>' <br> I can also answer some simple questions about the databases and SQL, ask me 'What is SQL' or 'What datasets are available'<br> You can also view some starter tips and information by pressing the help icon at the top right of our chat.")
        self.assertEqual(minerva("What stuff can you do?"), "I am a chatbot that assists with accessing databases, I can help you retrieve and filter data from the databases that are loaded. <br> You don't need any SQL knowledge with my help, try submitting a query by sending me 'Query: <i>your query here</i>' <br> I can also answer some simple questions about the databases and SQL, ask me 'What is SQL' or 'What datasets are available'<br> You can also view some starter tips and information by pressing the help icon at the top right of our chat.")
        self.assertEqual(minerva("What can you do with the database?"), "I am a chatbot that assists with accessing databases, I can help you retrieve and filter data from the databases that are loaded. <br> You don't need any SQL knowledge with my help, try submitting a query by sending me 'Query: <i>your query here</i>' <br> I can also answer some simple questions about the databases and SQL, ask me 'What is SQL' or 'What datasets are available'<br> You can also view some starter tips and information by pressing the help icon at the top right of our chat.")

        self.assertEqual(minerva("Who made you?"), "I was created by two students at DCU for their final year project, their names are Gareth Hogan and Jack Farrell")
        self.assertEqual(minerva("Where did you come from"), "I was created by two students at DCU for their final year project, their names are Gareth Hogan and Jack Farrell")
        self.assertEqual(minerva("Who created you"), "I was created by two students at DCU for their final year project, their names are Gareth Hogan and Jack Farrell")

        self.assertEqual(minerva("What are all the buttons"), "The buttons on the left of the chat allow you to change the loaded database and also give some information on the available databases. <br> The buttons on the right allow you to toggle whether you wish to see the SQL code I make, and link to some example prompts and my source code. <br> Above text entry box you can see some quick suggestion buttons to quickly ask me questions and to start off your query. <br> And at the very top of the chat you can click the trashcan icon to clear the chat, or the help icon to see some tips and helpful info for new users.")
        self.assertEqual(minerva("What does everything do?"), "The buttons on the left of the chat allow you to change the loaded database and also give some information on the available databases. <br> The buttons on the right allow you to toggle whether you wish to see the SQL code I make, and link to some example prompts and my source code. <br> Above text entry box you can see some quick suggestion buttons to quickly ask me questions and to start off your query. <br> And at the very top of the chat you can click the trashcan icon to clear the chat, or the help icon to see some tips and helpful info for new users.")
        self.assertEqual(minerva("What does each button do?"), "The buttons on the left of the chat allow you to change the loaded database and also give some information on the available databases. <br> The buttons on the right allow you to toggle whether you wish to see the SQL code I make, and link to some example prompts and my source code. <br> Above text entry box you can see some quick suggestion buttons to quickly ask me questions and to start off your query. <br> And at the very top of the chat you can click the trashcan icon to clear the chat, or the help icon to see some tips and helpful info for new users.")

    def test_Help(self):
        self.assertEqual(minerva("I am stuck"), "I'm very sorry you are struggling to get what you want, I am still in beta and learning new things. <br>If you are a new user you can check the helpful information by clicking the help icon in the top right of the chat. <br>If you want to know more about the databases see the information on the left or ask me about them. <br>If you aren't sure what to ask or queries to send, see our example prompts sheet in the bottom right or ask me 'What can you do?'<br> If you are having more serious problems please contact my creators.")
        self.assertEqual(minerva("I need help"), "I'm very sorry you are struggling to get what you want, I am still in beta and learning new things. <br>If you are a new user you can check the helpful information by clicking the help icon in the top right of the chat. <br>If you want to know more about the databases see the information on the left or ask me about them. <br>If you aren't sure what to ask or queries to send, see our example prompts sheet in the bottom right or ask me 'What can you do?'<br> If you are having more serious problems please contact my creators.")
        self.assertEqual(minerva("Help"), "I'm very sorry you are struggling to get what you want, I am still in beta and learning new things. <br>If you are a new user you can check the helpful information by clicking the help icon in the top right of the chat. <br>If you want to know more about the databases see the information on the left or ask me about them. <br>If you aren't sure what to ask or queries to send, see our example prompts sheet in the bottom right or ask me 'What can you do?'<br> If you are having more serious problems please contact my creators.")

    def test_Submission(self):
        self.assertEqual(minerva("How do you work?"), "To submit a query to the database simple enter the word 'Query' followed by your query, I will send this to the database and return the results right to you! I can also answer some other simple questions, ask me what I can do to find them.")
        self.assertEqual(minerva("How do I submit a query?"), "To submit a query to the database simple enter the word 'Query' followed by your query, I will send this to the database and return the results right to you! I can also answer some other simple questions, ask me what I can do to find them.")
        self.assertEqual(minerva("How to I ask the database something"), "To submit a query to the database simple enter the word 'Query' followed by your query, I will send this to the database and return the results right to you! I can also answer some other simple questions, ask me what I can do to find them.")
    
    def test_SQL(self):
        self.assertEqual(minerva("What is SQL"), "Structure Query Language (SQL) is a programming language that is used to interact with and retrieve data from large relational databases, with my help you don't need to know any SQL, I can translate your query into SQL <br> If you want to see what SQL your query is transformed into, click the Show SQL button in the lower righthand corner.")
        self.assertEqual(minerva("Do I need to know SQL"), "Structure Query Language (SQL) is a programming language that is used to interact with and retrieve data from large relational databases, with my help you don't need to know any SQL, I can translate your query into SQL <br> If you want to see what SQL your query is transformed into, click the Show SQL button in the lower righthand corner.")
        self.assertEqual(minerva("Do you use SQL"), "Structure Query Language (SQL) is a programming language that is used to interact with and retrieve data from large relational databases, with my help you don't need to know any SQL, I can translate your query into SQL <br> If you want to see what SQL your query is transformed into, click the Show SQL button in the lower righthand corner.")
        self.assertEqual(minerva("How does SQL work"), "Structure Query Language (SQL) is a programming language that is used to interact with and retrieve data from large relational databases, with my help you don't need to know any SQL, I can translate your query into SQL <br> If you want to see what SQL your query is transformed into, click the Show SQL button in the lower righthand corner.")

    def test_Databases(self):
        self.assertEqual(minerva("What datasets are available"), "In my Beta version I have access to two databases: <br> The default database is a medical dataset that contains information on individuals with metabolic syndrome, you can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome'>source here</a><br> You can also swap to our finance dataset, which is full of numbers that describe the daily index prices for different stock exchanges, you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a>")
        self.assertEqual(minerva("What data is there"), "In my Beta version I have access to two databases: <br> The default database is a medical dataset that contains information on individuals with metabolic syndrome, you can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome'>source here</a><br> You can also swap to our finance dataset, which is full of numbers that describe the daily index prices for different stock exchanges, you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a>")
        self.assertEqual(minerva("What are the two datasets"), "In my Beta version I have access to two databases: <br> The default database is a medical dataset that contains information on individuals with metabolic syndrome, you can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome'>source here</a><br> You can also swap to our finance dataset, which is full of numbers that describe the daily index prices for different stock exchanges, you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a>")
        self.assertEqual(minerva("What data can I search"), "In my Beta version I have access to two databases: <br> The default database is a medical dataset that contains information on individuals with metabolic syndrome, you can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome'>source here</a><br> You can also swap to our finance dataset, which is full of numbers that describe the daily index prices for different stock exchanges, you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a>")
    
    def test_loadDB(self):
        self.assertEqual(minerva("Can I load my own database"), "In this Beta version I can only interact with the two example databases, in a future version my creators hope I will be able to help with any database loaded in by a user.")
        self.assertEqual(minerva("How do I use my own database"), "In this Beta version I can only interact with the two example databases, in a future version my creators hope I will be able to help with any database loaded in by a user.")
        self.assertEqual(minerva("How to use another dataset"), "In this Beta version I can only interact with the two example databases, in a future version my creators hope I will be able to help with any database loaded in by a user.")

    def test_DBinfo(self):
        self.assertEqual(minerva("What is the medical database"), "The medical dataset is filled with data about people with Metabolic syndrome, a complex medical condition associated with a cluster of risk factors for cardiovascular diseases and type 2 diabetes. You can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome' target=”_blank”>source here</a> <br> The columns in this database are described below: <br> <i>seqn: Sequential identification number.</i><br><i>Age: Age of the individual.</i><br><i>Sex: Gender of the individual (e.g., Male, Female).</i><br><i>Marital: Marital status of the individual.</i><br><i>Income: Income level or income-related information.</i><br><i>Race: Ethnic or racial background of the individual.</i><br><i>WaistCirc: Waist circumference measurement.</i><br><i>BMI: Body Mass Index, a measure of body composition.</i><br><i>Albuminuria: Measurement related to albumin in urine.</i><br><i>UrAlbCr: Urinary albumin-to-creatinine ratio.</i><br><i>UricAcid: Uric acid levels in the blood.</i><br><i>BloodGlucose: Blood glucose levels, an indicator of diabetes risk.</li><br><i>HDL: High-Density Lipoprotein cholesterol levels (the 'good' cholesterol).</i><br><i>Triglycerides: Triglyceride levels in the blood.</i><br><i>MetabolicSyndrome: Binary variable indicating the presence (1) or absence (0) of metabolic syndrome.</i>")
        self.assertEqual(minerva("What data is in the medical database"), "The medical dataset is filled with data about people with Metabolic syndrome, a complex medical condition associated with a cluster of risk factors for cardiovascular diseases and type 2 diabetes. You can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome' target=”_blank”>source here</a> <br> The columns in this database are described below: <br> <i>seqn: Sequential identification number.</i><br><i>Age: Age of the individual.</i><br><i>Sex: Gender of the individual (e.g., Male, Female).</i><br><i>Marital: Marital status of the individual.</i><br><i>Income: Income level or income-related information.</i><br><i>Race: Ethnic or racial background of the individual.</i><br><i>WaistCirc: Waist circumference measurement.</i><br><i>BMI: Body Mass Index, a measure of body composition.</i><br><i>Albuminuria: Measurement related to albumin in urine.</i><br><i>UrAlbCr: Urinary albumin-to-creatinine ratio.</i><br><i>UricAcid: Uric acid levels in the blood.</i><br><i>BloodGlucose: Blood glucose levels, an indicator of diabetes risk.</li><br><i>HDL: High-Density Lipoprotein cholesterol levels (the 'good' cholesterol).</i><br><i>Triglycerides: Triglyceride levels in the blood.</i><br><i>MetabolicSyndrome: Binary variable indicating the presence (1) or absence (0) of metabolic syndrome.</i>")

        self.assertEqual(minerva("What is the financial database"), "The financial database is filled with daily price data from indexes tracking stock exchanges from all over the world (United States, China, Canada, Germany, Japan, and more), you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a> <br> The columns in this database are described below: <br> <i>Index: Ticker symbol for indexes</i><br><i>Date: Date of observation</i><br><i>Open: Opening price</i><br><i>High: Highest price during trading day</i><br><i>Low: Lowest price during trading day</i><br><i>Close: Closing price</i><br><i>Adj Close: Closing price adjusted for dividends and stock splits</i><br><i>Volume: Number of shares traded during trading day</i><br><i>CloseUSD: Close price in terms-of USD</i><br>")
        self.assertEqual(minerva("What data is in the financial database"), "The financial database is filled with daily price data from indexes tracking stock exchanges from all over the world (United States, China, Canada, Germany, Japan, and more), you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a> <br> The columns in this database are described below: <br> <i>Index: Ticker symbol for indexes</i><br><i>Date: Date of observation</i><br><i>Open: Opening price</i><br><i>High: Highest price during trading day</i><br><i>Low: Lowest price during trading day</i><br><i>Close: Closing price</i><br><i>Adj Close: Closing price adjusted for dividends and stock splits</i><br><i>Volume: Number of shares traded during trading day</i><br><i>CloseUSD: Close price in terms-of USD</i><br>")

    def test_Thanks(self):
        self.assertEqual(minerva("Thanks"), "You're very welcome, I'm glad I could be of assistance.")
        self.assertEqual(minerva("Thx"), "You're very welcome, I'm glad I could be of assistance.")
        self.assertEqual(minerva("Thank you"), "You're very welcome, I'm glad I could be of assistance.")
        self.assertEqual(minerva("Much appreciated"), "You're very welcome, I'm glad I could be of assistance.")



def minerva(prompt):
    Minerva_url = 'http://127.0.0.1:5000/get'
    data = {'msg': '', 'sql': 'off'}
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