# DCU CA400 - Final Year Project

![Minerva Banner](../media/minerva_banner.png)

>Gareth Hogan 20379616  & Jack Farrell 20352136

---  

## Table of contents

1. Introduction  
   1.1 Overview
   1.2 Glossary 
2. Motivation
3. Research  
4. Design  
5. Implementation  
6. Problems and Solutions  
7. Testing  
8. Installation Guide  
9. What we have learnt  
10. Future Work

---  

## Introduction

### Overview

The system we created is called Minerva, Minerva is a database chat bot assistant who is designed to take a users natural language question and turn that question into MYSQL code before then sending that generated query to the database to return to the user the information they were asking. Minerva is accesessed through a flask website where users can enter in their questions. Once Minerva has identified a question, that question is then transformed into MYSQL code using a Text-to-SQL program. This returns the translated question which is then sent to the database via the MYSQL API and returns the requested information back to Minerva who can present it to the user. Minerva is a chatbot but we decided to focus more on her ability to interact with a database than her ability to have a conversation.

### Glossary

| Term | Description |
| --- | ----------- |
| Computer Vision | Computer Vision is a field of AI. It enables computers and systems to be able to see and observe, it allows them to derive information and data from visual inputs such as images and videos. |


## Motivation

**Why did we choose this project?**

The initial plan for this project started with Gareth wanting to do a project that involved a chatbot as during a summer internship he was on a team that was responsible for testing a chatbot and gained valuable insight into how they operate. Jack was interested in databases and would want a project that had database and database interaction as a core part of the project. 

It was decided early on in the project timeline that we would create a database assistant chatbot with the main focus being on tranlating natural language questions into MYSQL code that the database could understand. We went to discuss the project idea with one of our lecturers who focused on database's and datamining, What was suggested was that we focus more on the database functionality of the bot by adding in additional features. such featuers were data mining and using multiple models for the data mining to turn this into a more research focused project. This did not resonate with us as we much prefered to focus on creating a system rather than answering questions. We decided to go to another lectuerer of ours who had experience dealing with chatbots and pitched our project to him, he was more receptive to our initial idea so we decided to ask him to be our supervisor for this project.

The idea for Minerva hasn't changed as progress was made, During our presentation for project approval it was suggested that we have minerva connected to 2 databases as it would show that we are'nt hard coding in our anwers and also showes her versatility
---

## Research


---

## Design


---

## Implementation

---

## Problems and Solutions


---

## Testing


---

## What we learnt

---

## Installation Guide

If you would like to try out the system for yourself please follow these instructions:
> *These instructions were made and tested in a fresh Ubuntu environment, your system may already have some of these libraries installed*

1. First make sure you have Git installed (sudo apt install git)
2. Clone our repo
3. Navigate to /src in your terminal
4. For the backend:
   a. First make sure you have the pip installer **sudo apt install python3-pip**
   b. navigate to /src/backend
   c. use pip to install the requirements **pip install -r requirements.txt**
   d. start the Django backend with the command **python3 manage.py runserver**
5. For the frontend: (Open a second terminal window)
   a. Make sure you have NPM installed - **sudo apt install npm**
   b. navigate to /src/frontend
   c. Install Nodemon **npm install nodemon**
   d. Start the Node server with the command **npm start**
6. Once both servers are running head to *localhost:3000* to view the webpage

> *Note about flask: when you start the flask service it takes a moment to start, the new tab will say failed to connect briefly before it will display the UI*

## Future Work
