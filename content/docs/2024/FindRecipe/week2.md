---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

* Python - All of our team members have extensive experience with python.
* FastAPI - A good framework for backend development.
* telebot - It is a lib for bot development on python.
* MongoDB - We know this database well. It's proven itself.
* Others - Other technical tools that will emerge during the development process.

### **Architecture Design**

1. **Component Breakdown**:

![project_schema](/2024/FindRecipe/project_schema.jpg)

* Telegram Bot - service to communicate with the customer. It contacts the server to get information.
* Server - it's used to calculate and select the optimal menu.
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

1) Tech Stack Resources: ...

2) Mentorship Support: ...

3) Exploring Alternative Resources: ...

4) Identifying Knowledge Gaps: ...

5) Engaging with the Tech Community: ...

6) Learning Objectives: ...

7) Sharing Knowledge with Peers: ...

8) Leveraging AI: ...

### **Tech Stack and Team Allocation**

| Team Member        | Track                   | Responsibilities  |
|--------------------|-------------------------|-------------------|
| Egor Lebedev       | Backend                 | Server on FastAPI |
| Alie Ablaeva       | Backend/Frontend/Design | TG Bot            |
| Sofia Gamershmidt  | Backend/Frontend/Design | TG Bot            |
| Ilsiia Nasibullina | Backend/Frontend/DB     | TG Bot            |
| Alex Shulmin       | Backend/DB              | MongoDB, Parsing  |

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