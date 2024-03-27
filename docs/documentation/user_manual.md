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
> pic of the web page
> describes what parts are where 
---

## Using Mineva
Minerva is very simple to use even if users have never had experience with chatbots before. Minerva has two functions that users can use to interact with her and they are using the text box to enter in and submit questions and viewing the output of the questions in the chat history bo above. Once Minerva has been set up corectly users will open up the web page and be greated with the layout as described above in the [Layout of the Web Page](#layout-of-the-web-page).

### Entering your Questions
Once there the user has arrived on the web page they will see the text box at the bottom, Users can click on the box and start typing in their question that they want Minerva to go and find. Similar to how sending messages works users will see their question be placed into the above chat history section before Minerva goes about getting that information from the connected databases. If Minerva does not understand the question or an error occured she may suggest you change the wording of the question this will be displayed to the user in the chat history.

### Viewing the Output
If the users question was succesful Minerva will output the information in the chat history before asking the user if they would like to enter another question. Once there are enough mesages that they all cannot fit on the page the chat history will get a scroll wheel allowing the users to go back and see what questions they asked and what answers they got. Using that a user may be able to learn and ask different questions until they are satisfied with the infomation they recevied.

---