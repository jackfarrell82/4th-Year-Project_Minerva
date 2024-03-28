# DCU CA400 - Final Year Project

![Minerva Banner](../../res/media/minerva_banner.png)

>Gareth Hogan 20379616  & Jack Farrell 20352136

---

## Table of contents

1. Setting Up Minerva 
2. Web Page
    - Layout of the Web Page
3. Using Minerva
    - Entering your Questions
    - Viewing the Output

---

## Setting Up Minerva

Before Minerva can be used she has to be set up and connected to the database. All of the code for Minerva can be found in the src directory along side the requirements.txt file which will download all the necessary modules. A config.env file has to be made with the following information in order for Minerva to be able to connect to the database. They are:  <br>
    - Database Username <br>
    - Database Password <br>
    - Database IP Address (if the database is on the same system as Minerva than the device IPv4 address should be used) <br>
    - Database port (3360 is the default) <br>
    - Authorization token (used for the [text2sql-API](https://www.text2sql.ai/app)) <br>

<p> The Name and Schema of the databases will need to be added to the text_to_sql_api.py file in order connect to the database.
</p>
---

## Web Page

Minerva's locally hosted web page consists of a text box where users can enter their questions alongside the chat history between Minerva and the user.

### Layout of the Web Page
![Web Page 1](../../res/media/layout1.png)

This is the layout of the web page that a user will see once they begin using Minerva, Here you can see Minerva greeting the user and the chat history where the user has asked Minerva "What can you do?". as shown, Minerva's response to the user will be in the chat history box similarly to how text messages and other messaging apps allow you to view the history of what was said by what person. Minerva answers the users question explaining to the user what she is and what she can do. Along the bottom of the web page we can see the text box that the user is currently typing in their next question to Minerva, this area is visibly shown to be different due to the background colour being different from the history box above. Once the user has finished typing in their question they can click on the send button found on the right hand side. Common user questions can be found just above the text box that allows users to ask them without having to type it out.

On the far right hand side there is a "Change Database" button this will then bring up a list of databases allowing the user to change what database Minerva gets the information from.
![Web Page 2](../../res/media/layout2.png)
This is what the user will see when they click on the Change Database button

![Web Page 3](../../res/media/layout3.png)
When a user changes database the background changes to a different colour to easily and quickly tell the user that the database was changes succesfully. The top left corner also displays what the current database is if the user is unaware what colour is assigned to each database. In this screenshot it shows that Minerva can give you information about the database including what columns there are and what each column represents, this can assist the user in constructing their questions to get the information they want out of the database.
---

## Using Mineva
Minerva is very simple to use even if users have never had experience with chatbots before. Minerva has two functions that users can use to interact with her and they are using the text box to enter in and submit questions and viewing the output of the questions in the chat history bo above. Once Minerva has been set up corectly users will open up the web page and be greated with the layout as described above in the [Layout of the Web Page](#layout-of-the-web-page).

### Entering your Questions
Once there the user has arrived on the web page they will see the text box at the bottom, Users can click on the box and start typing in their question that they want Minerva to go and find. If a user wants to ask Minerva a question they can enter it in normally before hitting send, if the user wants Minerva to get information from the database they need to add "Query:" to the begining of their question. A query button is available allowing users to just click it instead of typing out "Query:" every time. Similar to how sending messages works users will see their question be placed into the above chat history section before Minerva goes about getting that information from the connected databases. If Minerva does not understand the question or an error occured she may suggest you change the wording of the question this will be displayed to the user in the chat history.

### Viewing the Output
If the users question was succesful Minerva will output the information in the chat history before asking the user if they would like to enter another question. Once there are enough mesages that they all cannot fit on the page the chat history will get a scroll wheel allowing the users to go back and see what questions they asked and what answers they got. Using that a user may be able to learn and ask different questions until they are satisfied with the infomation they recevied.

---