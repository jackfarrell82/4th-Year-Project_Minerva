import requests
import sys
import os
import mysql
from mysql.connector import errorcode
from dotenv import load_dotenv

database_M = "metabolic_syndrome"
schema_M = "metabolic_syndrome (seqn: int, Age: int, Sex: text, Marital: text, Income: text, Race: text, WaistCirc: double, BMI: double, Albuminuria: int, UrAlbCr: double, UricAcid: double, BloodGlucose: int, HDL: int, Triglycerides: int, MetabolicSyndrome: int)"

database_F = "financial"
schema_F = "indexprocessed (Index: text, Date: text, Open: double, High: double, Low: double, Close: double, Adj Close: double, Volume: double, CloseUSD: double)"

DB_LOADED = database_M
SCHEMA = schema_M

config = {
'user': "", #User Name, keep it as root but make sure the data base has all permisions
'password': "", 
'host': "", #database ipv4 address
'port': "",
'database': "", #What database we are sending our query too
'raise_on_warnings': True,
}

headers = {
    'Authorization': "", # what allows us to use the api
}

data = {
    "prompt": "", # passes in the prompt needs to be in quotes
    "type": "mysql", # the language it is translating too
    "schema": ""
}

def setupDB():
    # default DB is medical
    global DB_LOADED, SCHEMA # access the DB_LOADED and SCHEMA variables that are outside the function
    print(DB_LOADED)

    load_dotenv("config.env") # loads the config.env file allowing its data to be read
    DB_USER = os.getenv("DB_USER") # assign DB_USER in the config.env file to DB_USER in this function
    DB_PORT = os.getenv("DB_PORT")
    config["user"] = DB_USER # assigns DB_USER to user in the config field
    config["port"] = DB_PORT

    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    headers["Authorization"] = AUTH_TOKEN # assigns AUTH_TOKEN to Authorization in the headers field

    HOST = os.getenv("DB_HOST")
    PASSWORD = os.getenv("DB_PASSWORD")
    config["password"] = PASSWORD
    config["host"] = HOST

    config["database"] = DB_LOADED
    data["schema"] = SCHEMA # assigns SCHEMA to schema in the data field

def swapDB():
    global DB_LOADED, SCHEMA # access the DB_LOADED and SCHEMA variables that are outside the function
    if DB_LOADED == database_M: # checks to see if the metabolic database is the database currently loaded
        DB_LOADED = database_F # if it is then we replace DB_LOADED and SCHEMA with the financial database and schema
        SCHEMA = schema_F
    else:
        DB_LOADED = database_M # if the financial database is loaded then we replace DB_LOADED and SCHEMA with the metabolic database and schema
        SCHEMA = schema_M

    config["database"] = DB_LOADED # we then assign the new database and schema to the necessary fields which is necessary for the api's to function
    data["schema"] = SCHEMA

def toSQL(prompt):
    data["prompt"] = prompt # puts the prompt into the data field
    response = requests.get("https://www.text2sql.ai/api/sql/generate", headers=headers, data=data) # send it to the api
    response = response.text # get the text version back
    resp_list = response.split('"') # modify the output to be just the SQL query
    response = resp_list[3]
    response = response.replace("\\n", " ")
    package = [response, DB_LOADED] # packages up the response and the database that is currently loaded
    return package

def toDatabase(query):
    try: # error handling for database
        cnx = mysql.connector.connect(**config, auth_plugin='mysql_native_password') # attempts to connect to the database
    except mysql.connector.Error as err: # if an error occurs we then go here
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: # if access is denied
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR: # if the database name is incorrecct
            print("Database does not exist")
        else:
            print(err) # print the error
    else:
        cursor = cnx.cursor(buffered=True)

        cursor.execute(query) # sends the query to the database
        rows = cursor.fetchall() # gets all the results and prints it out

        cursor.close()
        cnx.close()
        return rows

## this is where stuff happens when this file is run, not when it is imported into Minerva
if __name__ == "__main__":
    setupDB() # calls the setupDB function

    if "medical" in sys.argv: # determines which database to load first based on the argument passed 
        DB_LOADED = database_M
        SCHEMA = schema_M   
    if "financial" in sys.argv:
        DB_LOADED = database_F
        SCHEMA = schema_F

    print("Database = " + DB_LOADED) # prints the loaded database name to the command line
    prompt = input("Input a prompt: ") # asks user for a prompt

    response = toSQL(prompt) # translates the prompt to sql
    print("Prompt: " + prompt + " transformed into: " + response) # prints the prompt and its translation to the command line
    resp = toDatabase(response) # sends the translated query to the database
    for r in resp: # prints the data retrieved from the database
        print(r)

    swapDB() # changes the database to the one that was not intially loaded, before repeating the same code
    print("Database = " + DB_LOADED)
    prompt = input("Input a prompt: ")

    response = toSQL(prompt)
    print("Prompt: " + prompt + " transformed into: " + response)
    resp = toDatabase(response)
    for r in resp:
        print(r)