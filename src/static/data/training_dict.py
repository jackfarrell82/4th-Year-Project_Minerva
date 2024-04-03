trainset = {
    # Greetings
    "Hi there, I am Minerva, how can I help you?" : 
    ["Hi", "Hello", "What's up", "Sup", "Howdy", "Hey", "Hey there", "Hello there", "How's it going", "Hewwo", "Hello?", "Hi there"],
    # Who/What are you?
    "My Name is Minerva, I am a chatbot created by Gareth & Jack, I can help you access data in your databases" :
    ["Who are you?", "What are you?", "What is this?", "What is Minerva", "Who is there?", "Who?"],
    # What can you do?
    "I am a chatbot that assists with accessing databases, I can help you retrieve and filter data from the databases that are loaded. <br> You don't need any SQL knowledge with my help, try submitting a query by sending me 'Query: <i>your query here</i>' <br> I can also answer some simple questions about the databases and SQL, ask me 'What is SQL' or 'What datasets are available'" :
    ["What can you do?", "What functions do you do?", "Available commands", "What commands can you do?", "What functionalities do you have?", "What stuff can you do?", "What can you do with the database?"],
    # Response to Help
    "I'm very sorry you are struggling to get what you want, I am still in beta and learning new things. If you want to know what I can do at the moment just ask me “What can you do?”" :
    ["Help", "I need help", "I am lost", "I am stuck", "Help me"],
    # How do you work
    "To submit a query to the database simple enter the word 'Query' followed by your query, I will send this to the database and return the results right to you! I can also answer some other simple questions, ask me what I can do to find them." :
    ["How do you work?", "How do I send a query?", "How do I submit a query?", "How to I use the database?", "Submitting a query", "How to I ask the database something", "How do I use you?", "How does this work?", "How do I use this system?"],
    # What is SQL
    "Structure Query Language (SQL) is a programming language that is used to interact with and retrieve data from large relational databases, with my help you don't need to know any SQL, I can translate your query into SQL":
    ["SQL", "SQL?", "What is SQL", "Structured Query Language", "Do I need to know SQL", "Do I need SQL", "Do you use SQL", "How does SQL work", "SQL question", "Do you make SQL", "Can you translate to SQL"],
    # What databases are available
    "In my Beta version I have access to two databases: <br> The default database is a medical dataset that contains information on individuals with metabolic syndrome, you can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome'>source here</a><br> You can also swap to our finance dataset, which is full of numbers that describe the daily index prices for different stock exchanges, you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a>":
    ["What are the databases", "What datasets are available", "What databases are loaded", "What data is there", "Where do you get your data", "What are the sources of data", "Where is the data from", "What are the two datasets", "What database is there", "What data do you have", "What data can I search", "What database can I query"],
    # Load own database
    "In this Beta version I can only interact with the two example databases, in a future version my creators hope I will be able to help with any database loaded in by a user.":
    ["Can I load my own database", "How do I use other data", "How do I use my own database", "Can I load any file", "Change to my own data", "Use other databases", "How to use another dataset"],
    # Medical Database
    "The medical dataset is filled with data about people with Metabolic syndrome, a complex medical condition associated with a cluster of risk factors for cardiovascular diseases and type 2 diabetes. You can view the <a href='https://www.kaggle.com/datasets/antimoni/metabolic-syndrome' target=”_blank”>source here</a> <br> The columns in this database are described below: <br> <i>seqn: Sequential identification number.</i><br><i>Age: Age of the individual.</i><br><i>Sex: Gender of the individual (e.g., Male, Female).</i><br><i>Marital: Marital status of the individual.</i><br><i>Income: Income level or income-related information.</i><br><i>Race: Ethnic or racial background of the individual.</i><br><i>WaistCirc: Waist circumference measurement.</i><br><i>BMI: Body Mass Index, a measure of body composition.</i><br><i>Albuminuria: Measurement related to albumin in urine.</i><br><i>UrAlbCr: Urinary albumin-to-creatinine ratio.</i><br><i>UricAcid: Uric acid levels in the blood.</i><br><i>BloodGlucose: Blood glucose levels, an indicator of diabetes risk.</li><br><i>HDL: High-Density Lipoprotein cholesterol levels (the 'good' cholesterol).</i><br><i>Triglycerides: Triglyceride levels in the blood.</i><br><i>MetabolicSyndrome: Binary variable indicating the presence (1) or absence (0) of metabolic syndrome.</i>":
    ["What is the medical database", "What is in the medical database", "What data is in the medical database", "What are the columns in the medical database"],
    # Financial Database
    "The financial database is filled with daily price data from indexes tracking stock exchanges from all over the world (United States, China, Canada, Germany, Japan, and more), you can view the <a href='https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data' target=”_blank”>source here</a> <br> The columns in this database are described below: <br> <i>Index: Ticker symbol for indexes</i><br><i>Date: Date of observation</i><br><i>Open: Opening price</i><br><i>High: Highest price during trading day</i><br><i>Low: Lowest price during trading day</i><br><i>Close: Closing price</i><br><i>Adj Close: Closing price adjusted for dividends and stock splits</i><br><i>Volume: Number of shares traded during trading day</i><br><i>CloseUSD: Close price in terms-of USD</i><br>":
    ["What is the financial database", "What is in the finance database", "What data is in the financial database", "What are the columns in the financial database"],
}