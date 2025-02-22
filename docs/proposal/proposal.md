# School of Computing &mdash; Year 4 Project Proposal Form

## SECTION A

|                     |                   |
|---------------------|-------------------|
|Project Title: | Minerva: Data Assitance Chatbot |
|Student 1 Name: | Gareth Hogan |
|Student 1 ID: | 20379616 |
|Student 2 Name:  | Jack Farrell |
|Student 2 ID: | 20352136|
|Project Supervisor: | Gareth Jones |

## SECTION B

### Introduction

The idea for our project is to create an interactive system to help users interact and utilise data stored inside a database in our system. Our system will be interacted with through a chatbot we will call Minerva, through an interactive conversational interface the users will be able to access, search and manipulate our database, some examples of what we hope to enable users to do is a simple search, queries with SQL, visualise, produce graphs and perhaps even classify unseen data.

### Outline

Our project idea is split into two major parts:<br>
**Our Interactive Interface Minerva**<br>
This portion of the project involves displaying our chatbot interface on a simple webpage to users, taking input through a conversation-like interface and processing the user's queries with a rules-based chatbot approach. Once a user's intent has been identified we can process their query and then send a call to the backend to the correct function, and display the results retrieved back to the user.<br>
**Backend Functions and Database**<br>
Behind our user interface will lie the database and the program that controls access to it, this part of our project will be filled with the different functions and methods that the user can utilise to achieve their goals, this is where search queries will be constructed, graphs will be made and where the database is stored, Minerva will invoke functions in the backend and then will display the results returned from here to the user.

### Background

The idea for this project started early on, we decided to pair up early on in the summer and started to brainstorm project ideas. We worked on separate projects in third year and we brought together ideas and improvements from last year and thought about how we wanted to improve for this year's project. During the summer we both looked at past projects and online for ideas and themes we could make a project out of, we both knew we wanted to challenge ourselves whilst also working on something we had a genuine interest in, Jack had an interest in exploring data, through analysis, visualisation or similar methods, Gareth had an interest in creating a different kind of user interface to an app or website and had experience with chatbots before. So we brought our interests together and named our project Minerva, with a backend powered by data and the user able to interact with it through our chatbot.

### Achievements

The function of Minerva is to provide a tool that allows users unfamiliar with database languages like SQL to be able to search a database and easily find the information they are looking for, Other functionalities that Minerva will have will be to visualise the data retrieved from the database, produce graphs showing the change in the data over time and perhaps even classify unseen data. As we progress through the project we may be able to include more functionalities like the ability for Minerva to not only read but write data to the database.

The users of Minerva will be people working in fields that require them to store and retrieve large amounts of data, A consulting company wanting to find the information on a particular business, A nurse wanting to find a record of a specific patient or a large warehouse wanting to see the information regarding one specific product.

### Justification

Minerva will be helpful to users who do not have database skills or who might have difficulty sifting through and getting information out of a large or complex database. Minerva would enable users to interface with a database and ask for exactly what they want rather than staring blankly at thousands of rows and columns of data which could mean nothing to the user. Instead of spending hours searching for all the data a user needs in a database, they should be able to tell Minerva what exactly they want and she can format an SQL query which returns the data the user requires with a much faster turnaround time, Minerva will also have the ability to transform raw data into graphs and charts, helping a user gather better insights from the database then would be possible by looking at the raw numbers. Minerva might even be able to help users input new unseen data entries, classifying where they belong or comparing them to database tuples to predict an unknown attribute the user is looking for.

#### Example Use Case

One example use case in which Minerva could be used is in a Medical setting, Minerva could contain a master database of patients' information, this database could have thousands of entries spanning multiple years, with hundreds of attributes for each patient ranging from basic personal info to blood type, doctors name, symptoms, etc. A nurse or doctor trying to do anything more than a simple search in this database would have a difficult time extracting useful information quickly and easily, this is where Minerva comes in. Through a simple and clean UI a nurse could tell Minerva exactly what they are looking for, whether it be the records of one patient, all patients seen by a specific doctor, any blood type AB patients or perhaps any patients with a specific set of symptoms, Minerva would be able to process their query into an appropriate database query and return the data back to the nurse, stripped of anything that isn’t relevant to what the nurse wants. Minerva can also visualise the database, and graph it over time to find insights and trends over a specific time period, in a certain ward, etc. 

### Programming language(s)

The primary language of our project is going to be Python, we chose this language because it is very good at doing machine learning and data analysis tasks which suits our project very well. There may be some small bits of other languages such as JavaScript and html for our user interface.

### Programming tools / Tech stack

For the frontend, we plan to use Python to build it as a Flask application using the Chatterbot library to construct our chatbot from scratch, and designing our interface visuals using JS, HTML & CSS

For the backend, we plan to use SQL to build the database that will store our information, Using APIs to connect the database to the chatbot so they can communicate with one another. We will be trying and comparing multiple methods of converting our Natural Language input into SQL queries from our research.

**Frontend Chatbot:**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python + Chatterbot + Flask
	
**Backend Database Functions:**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SQL + Chatbot API + DataMining Algorithms + Data Visualization + Text-to-SQL


### Learning Challenges

The main challenges we face in this project are the design and research into new tools and libraries we will have to use. We are excited to face the challenge our project entails but we are making sure we plan out every eventuality we could be faced with, a minimum project level we hope to achieve followed by our envisioned project plan and then even options for extensions if all things go smoothly

For the frontend Gareth will have to do a lot of research into the chatterbot library and think about how we want to design our conversations with the user, converting our user's potential queries into conversation flows and then programming and training our chatbot to recognise them and respond correctly.

In the backend, Jack will have to find ways of connecting the chatbot's output to an SQL database and make sure that the database can recognise the chatbot's request. I will also be in charge of making sure the API to the database is correct and accepting the right information while also ensuring that the requested information is being sent back to the chatbot and the user. Learning and implementing data visualisation will be difficult as it is something that I will have to research in full as I have never done it before. Data mining will be of a lesser challenge as both of us will have some experience with data mining due to our data warehousing module. The use of Text-to-SQL will be a challenge as I have never used it before nor do I have experience with natural language.

### Breakdown of work

As mentioned before we have designed this project with two defined halves which cater to both our interests. We will both be in charge of one of these halves but we will of course be working closely together at all times when it comes to aspects of the project such as design, planning, testing and research, coming together whenever we encounter difficulties in our work or when a question about design and how we want to do something arises.

#### Gareth

Gareth will focus on designing and implementing Minerva as the interface of our project, the major things I will be doing include designing the conversations Minerva will have with users, converting these into design flows and then implementing these into Minerva. We plan to design the frontend in an extensible and modifiable fashion so that as our project progresses we can add in new functionality, change Minerva's responses and train her to recognise synonyms and different ways users could interact with her. I will then have to put all our design into actual code, building up our chatbot following the design of a rules-based chatbot with the Chatterbot library in Python. I will also be in charge of designing and programming the interface that the user will see using some HTML and JS in our Flask application.

#### Jack

Jack will focus on the backend database, ensuring that information is being correctly received and sent to and from Minerva. I will also be responsible for creating the database that Minerva will be getting the information from and ensuring that the requests that Minerva generates get the correct information from the database. We plan to use SQL as our database language as it is something that we have both covered during the course. APIs will be how we connect the chatbot to the database and how the information is returned to the chatbot. Data visualisation will be a high priority once we have the core of our project made as that will be a feature that will require time to research, test, and implement into our system. Data visualisation will be a feature that both of us will be working closely together on while data mining can be done less so as we would have experience from our data warehousing module.
