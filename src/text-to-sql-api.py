import sys
import requests
import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'DESKTOP-7LEP5EQ', #Device Name LAPTOP-EDUNB10Q DESKTOP-7LEP5EQ
  'password': 'Destiny14',
  'host': '192.168.0.150', #Device ipv4 address 192.168.0.150
  'port': '3306',
  'database': 'financial', #What database we are sending our query too
  'raise_on_warnings': True,
}

headers = {
    'Authorization': 'Bearer 59ad71fc36bd590f4237955b6ac578d612c5cad6825dcf908aa8e76d0af1b01c', # what allows us to use the api
}

example_prompt = "how many iterations do we have where open is less than close"

schema = "indexprocessed (Index: text, Date: text, Open: double, High: double, Low: double, Close: double, Adj Close: double, Volume: double, CloseUSD: double)"

data = {
    "prompt": example_prompt, # passes in the prompt needs to be in quotes
    "type": "mysql", # the language it is translating too
    "schema": schema
}

def changeDatabase():
    if schema == "indexprocessed (Index: text, Date: text, Open: double, High: double, Low: double, Close: double, Adj Close: double, Volume: double, CloseUSD: double)":
        schema == "metabolic syndrome (seqn: int, Age: int, Sex: text, Marital: text, Income: text, Race: text, WaistCirc: double, BMI: double, Albuminuria: int, UrAlbCr: double, UricAcid: double, BloodGlucose: int, HDL: int, Triglycerides: int, MetabolicSyndrome: int)"
    else:
        schema == "indexprocessed (Index: text, Date: text, Open: double, High: double, Low: double, Close: double, Adj Close: double, Volume: double, CloseUSD: double)"

def toSQL(prompt):
    data["prompt"] = prompt;
    response = requests.get("https://www.text2sql.ai/api/sql/generate", headers=headers, data=data) # send it to the api
    response = response.text # get the text version back
    list = response.split('"') # modify the output to be just the SQL query
    response = list[3]
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
        rows = cursor.fetchall()    # gets all the results and prints it out
        for r in rows:
            print(r)

        cursor.close()
        cnx.close()

response = toSQL(example_prompt)
print(example_prompt)
print(response)
toDatabase(response)