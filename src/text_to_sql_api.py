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
'user': "", #Device Name, keep it as root but make sure the data base has all permisions
'password': "", # need to find a way to have this not be just written in a file
'host': "", #Device ipv4 address 192.168.0.150
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
    global DB_LOADED, SCHEMA

    load_dotenv("config.env")
    DB_USER = os.getenv("DB_USER")
    DB_PORT = os.getenv("DB_PORT")
    config["user"] = DB_USER
    config["port"] = DB_PORT

    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    headers["Authorization"] = AUTH_TOKEN

    HOST = os.getenv("DB_HOST")
    PASSWORD = os.getenv("DB_PASSWORD")
    config["password"] = PASSWORD
    config["host"] = HOST

    config["database"] = DB_LOADED
    data["schema"] = SCHEMA

def swapDB():
    global DB_LOADED, SCHEMA
    if DB_LOADED == database_M:
        DB_LOADED = database_F
        SCHEMA = schema_F
    else:
        DB_LOADED = database_M
        SCHEMA = schema_M

    config["database"] = DB_LOADED
    data["schema"] = SCHEMA

def toSQL(prompt):
    data["prompt"] = prompt
    response = requests.get("https://www.text2sql.ai/api/sql/generate", headers=headers, data=data) # send it to the api
    response = response.text # get the text version back
    resp_list = response.split('"') # modify the output to be just the SQL query
    response = resp_list[3]
    response = response.replace("\\n", " ")
    return response

def toDatabase(query):
    try: # error handling for database
        cnx = mysql.connector.connect(**config, auth_plugin='mysql_native_password')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = cnx.cursor(buffered=True)

        cursor.execute(query) # sends the query to the database
        rows = cursor.fetchall() # gets all the results and prints it out

        cursor.close()
        cnx.close()
        return rows

## this is where shit happens when this file is run, not when it is imported into Minerva
if __name__ == "__main__":
    setupDB()

    if "medical" in sys.argv:
        DB_LOADED = database_M
        SCHEMA = schema_M   
    if "financial" in sys.argv:
        DB_LOADED = database_F
        SCHEMA = schema_F

    print("Database = " + DB_LOADED)
    prompt = input("Input a prompt: ")

    response = toSQL(prompt)
    print("Prompt: " + prompt + " transformed into: " + response)
    resp = toDatabase(response)
    for r in resp:
        print(r)

    swapDB()
    print("Database = " + DB_LOADED)
    prompt = input("Input a prompt: ")

    response = toSQL(prompt)
    print("Prompt: " + prompt + " transformed into: " + response)
    resp = toDatabase(response)
    for r in resp:
        print(r)

#### STORE EXAMPLES TO TEST HERE IN COMMENTS
## MEDICAL
# how many patients are there below 40
# how many have a marital status of single
# show me all the records for Males
    

## FINANCIAL
# how many have a high price greater than 700
# how many close at over 2000
# what trades have 0 volume