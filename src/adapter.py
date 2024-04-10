from chatterbot.logic import LogicAdapter
import text_to_sql_api as api
from text_to_sql_api import *

SQL_FLAG = "on"
DB = ""

schema_F = "Ticker Symbol for Index | Date | Opening Price | Highest Price | Lowest Price | Closing Price | Adjusted Closing Price | Volume Traded | Close price in USD"
schema_M = "Patient ID | Age | Sex | Marital Status | Income | Race | Waist Circumference | BMI | Albumin Level | Urinary Albumin-to-Creatine ratio | Uric Acid | Blood Glucose | Cholesterol Level | Triglyceride Level | Metabolic Syndrome"

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
            data = processQuery(query) # data is a list of all rows (tuples) returned
            response = "<i>I've submitted your query to the database, here is the data I got back:</i><br><font color='#50C878'>"
            
            if SQL_FLAG == "on":
                transformation = data.pop()
                response = response + "<font color='black'>" + transformation + "</font><br>"
            
            if len(data) == 1:
                answer = data[0]
                if len(answer) == 1:
                    response = response + "<font color='black'>Answer:</font> <b>" + str(answer[0]) + "</b>"
                elif len(answer) == 9 and DB == "financial":
                    response = response + "<font color='black'>Data Legend:</font><br>"
                    response = response + "<font color='#801010' size=2px>" + schema_F + "</font><br>"
                    response = response + "<font color='black'>Answer:</font> <b><br>" + str(answer) + "</b>"
                elif len(answer) == 15 and DB == "metabolic_syndrome":
                    response = response + "<font color='black'>Data Legend:</font><br>"
                    response = response + "<font color='#00334E' size=2px>" + schema_M + "</font><br>"
                    response = response + "<font color='black'>Answer:</font> <b><br>" + str(answer) + "</b>"
                else:
                    response = response + "<font color='black'>Answer:</font> <b>" + str(answer) + "</b>"
            else:
                for entry in data:
                    response = response + str(entry)[1:-1] + "<br>"

            response = response + "</font>"

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
    global SQL_FLAG, DB
    api.setupDB()
    package = api.toSQL(query)
    transformed = package[0]
    DB = package[1]
    response = api.toDatabase(transformed)
    if(SQL_FLAG == "on"):
        response.append("Query transformed into SQL: <br> <font color='var(--med)'>" + transformed + "</font>")

    return response # response is a list