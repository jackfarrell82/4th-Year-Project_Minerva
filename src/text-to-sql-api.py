import requests
import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'LAPTOP-EDUNB10Q', #Device Name
  'password': 'Destiny14',
  'host': '192.168.0.65', #Device ipv4 address
  'port': '3306',
  'database': 'financial',
  'raise_on_warnings': True,
}

prompt = "how many iterations do we have where open is less than close" # Will change this to arguments

headers = {
    'Authorization': 'Bearer 59ad71fc36bd590f4237955b6ac578d612c5cad6825dcf908aa8e76d0af1b01c', # what allows us to use the api
}

data = {
    "prompt": prompt, # passes in the prompt
    "type": "mysql", # the language it is translating too
    "schema": "indexprocessed (Index: text, Date: text, Open: double, High: double, Low: double, Close: double, Adj Close: double, Volume: double, CloseUSD: double)"
}

response = requests.get("https://www.text2sql.ai/api/sql/generate", headers=headers, data=data) # send it to the api
response = response.text # get the text version back
list = response.split('"') # modify the output to be just the SQL query
response = list[3]
response = response.replace("\\n", " ")

print(prompt)
print(response)

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

    result = cursor.execute(response) # sends the query to the database
    rows = cursor.fetchall()    # gets all the results and prints it out
    for r in rows:
        print(r)

    cursor.close()
    cnx.close()