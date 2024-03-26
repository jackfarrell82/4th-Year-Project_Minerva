# DCU CA400 - Final Year Project

![Minerva Banner](../media/minerva_banner.png)

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

### Entering your Questions

### Viewing the Output

---