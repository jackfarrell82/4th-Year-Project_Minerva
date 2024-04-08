from chatterbot.logic import LogicAdapter
import text_to_sql_api as api
from text_to_sql_api import *

SQL_FLAG = "on"

class QueryAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        # Return True if the statement is recognized as a query prompt
        return True if statement.text.lower().startswith("query") else False

    def process(self, statement, additional_response_selection_parameters):
        # Extract the query from the statement
        query = statement.text.lower().replace("query:", "").strip()
        
        # Submit the query to another function and get the response
        try:
            data = processQuery(query)
            if SQL_FLAG == "on":
                transformation = data.pop()
                response = transformation + "<br>"
            else:
                response = ""
            if len(data) == 1:
                response = response + "Answer Returned: <b><font color='#50C878'>" + str(data[0]) + "</font></b>"
            else:
                response = response + "Rows returned shown below: <br>"
                for entry in data:
                    response = response + str(entry) + "<br>"

        except Exception as e:
            response = "Oh dear, something went wrong when I went to process this query! <br>" + "ERROR: " + str(e)

        

        # Create a response statement using the response
        response_statement = self.get_response_statement(response)

        return response_statement

    def get_response_statement(self, response):
        # Create a response statement with the provided text
        from chatterbot.conversation import Statement
        return Statement(text=response) 

def SQLcheck(flag):
    global SQL_FLAG
    SQL_FLAG = flag

def processQuery(query):
    global SQL_FLAG
    api.setupDB()
    transformed = api.toSQL(query)
    response = api.toDatabase(transformed)
    if(SQL_FLAG == "on"):
        response.append("Query transformed into SQL: <br> <font color='var(--med)'>" + transformed + "</font>")

    return response # response is a list