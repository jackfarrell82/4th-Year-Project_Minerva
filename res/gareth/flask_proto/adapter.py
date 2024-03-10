from chatterbot.logic import LogicAdapter

class QueryAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        # Return True if the statement is recognized as a query prompt
        return True if statement.text.lower().startswith("query") else False

    def process(self, statement, additional_response_selection_parameters):
        # Extract the query from the statement
        query = statement.text.lower().replace("query", "").strip()
        
        # Submit the query to another function and get the response
        response = functionX(query)

        # Create a response statement using the response
        response_statement = self.get_response_statement(response)

        return response_statement

    def get_response_statement(self, response):
        # Create a response statement with the provided text
        from chatterbot.conversation import Statement
        return Statement(text=response) 
    

def functionX(query):
    answer = "The Answer is: " + query
    return answer