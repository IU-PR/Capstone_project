---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

* FastAPI - A good framework for backend development.
* telebot - It is a lib for bot development on python.
* MongoDB - We know this database well. It's proven itself.
* Python - All of our team members have extensive experience with python.
* Others - Other technical tools that will emerge during the development process.

### **Architecture Design**

1. **Component Breakdown**:

![project_schema](/2024/FindRecipe/project_schema.jpg)

* Telegram Bot - service to communicate with the customer. It contacts the server to get information.
* Server - it's used to calculate and compose the optimal menu.
  The server communicates with the database and processes the results.
  Responds to requests from the bot.
* DB - stores recipe information. communicates with the server.


2. **Data Management**: ...

3. **User Interface (UI) Design**:

![UI design](/2024/FindRecipe/BotUI.jpg)

This is a sketch that may undergo changes,
but in general the framework and the main buttons and their actions are ready.

4. **Integration and APIs**: 

Structure of request for our server:

![UI design](/2024/FindRecipe/API_req.jpg)

Structure of response from our server:

![UI design](/2024/FindRecipe/API_res.jpg)

5. **Scalability and Performance**: 

We implement part of the server on a framework (FastAPI) that has a large number of pluses. 
The first is asynchrony, which allows us to process many clients at one moment. 
Performance, it has proven itself in the labor market.
It will also easily handle your current server architecture.

Also, given our archeitecture, we can say that the funcionale can be added at any stage. 
The system is very flexible on any of the nodes since they are separated and not connected in any way.

6. **Security and Privacy**: ...

7. **Error Handling and Resilience**: ...

8. **Deployment and DevOps**: ...

### **Week 2 questionnaire:**

1) Tech Stack Resources: 

We do not use any project-based books as source of technical information. 
Instead we utilize internet resources

2) Mentorship Support: 

Currently, we do not have a mentor actively involved in our project, nor have we sought one. 
However, we may consider seeking mentorship in the future for guidance and support, especially in addressing specific project-related queries and challenges.

3) Exploring Alternative Resources: 

As a main source of information within out tech stack we use technical documentation of the tools we use. 
If specific questions appear we seek for help  in video tutorials and blogs. (stackoverflow, geeksforgeeks, FastAPI course (https://www.youtube.com/playlist?list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS))

4) Identifying Knowledge Gaps: 

There are indeed knowledge gaps within our tech stack that we aim to address. 
We plan to fill these gaps through the use of video tutorials, detailed documentation reviews, and by actively seeking clarification through inquiries.

5) Engaging with the Tech Community: 

We actively engage with the tech community of our unversity (coursemates, professors). 
These engagements allow us to seek guidance and learn from professionals in our tech stack.

6) Learning Objectives: 

This week, our specific learning objectives include deepening our understanding of advanced features within our tech stack and understanding what specifically is needed for our project. 
To achieve these objectives, we will utilize video tutorials, participate in focused discussions, and explore advanced technical documentation.

7) Sharing Knowledge with Peers: 

We facilitate the exchange of insights and experiences related to our tech stack through organized knowledge-sharing sessions and discussions among team members. 
Moreover, whenever some of us has a technical related question, we seek for help in our team's chat where everyone is ready to help.

8) Leveraging AI: 

We leverage LLMs if there are specific issues or to structure our knowledge.

### **Tech Stack and Team Allocation**

| Team Member        | Track               | Responsibilities  |
|--------------------|---------------------|-------------------|
| Egor Lebedev       | Backend             | Server on FastAPI |
| Alie Ablaeva       | Backend/UI/Design   | Telegram Bot      |
| Sofia Gamershmidt  | Backend/UI/Design   | Telegram Bot      |
| Ilsiia Nasibullina | Backend/UI/DB       | Telegram Bot      |  
| Alex Shulmin       | Backend/DB          | MongoDB, Parsing  |

### **Weekly Progress Report**

This week our team has been researching available information, recipes.
We started parsing the food.ru website and converting the information into a database.

### **Challenges & Solutions**

The problem with parsing turned out to be query limitation and user ban.
This problem was solved by correctly selected optimal timeouts.

### **Conclusions & Next Steps**

Now we can say that we have a database to work with.
Of course, it can be extended, but it allows us to start server development.
But first we need to put the database on any resource for remote access.