---
weight: 2
bookFlatSection: true
title: "Week #2"
---

# **Week #2**

### **Architecture Design**

#### **Component Breakdown** 

The main components of our project include: 
1. **The website** -- for the user to register, create new chatbot models, receive tokens to access these models in the Telegram bot.
The website will be the entry point for the user to interact with the project.
2. **Telegram bot** -- for the user to interact with the created chatbot model and have a conversation.
3. **The database** -- for the website and chatbot to store and retrieve data, access tokens and models. 
4. **Machine Learning Unit** -- the unit that is used to create and develop new chatbot models that will imitate the communication style of some person.

#### **Data management**
The data will be stored and accessed with the help of a PostgreSQL database, which will handle user information, models’ access tokens, chat logs, and other data. The database schema will include tables for users, authentication tokens, and models' metadata. User information will be securely stored to ensure user privacy. The data will be regularly backed up to prevent any potential data loss risks. 

#### **User Interface Design**
Website user interface design sketch:

<div style="text-align: center;">
<img src="/2024/protein-studio/ui_design_sketch.jpg" width="700" height="600"> 
</div>

#### **Integration and APIs**
To implement our project, we will use SQL queries to communicate with the PostgreSQL database. The Telegram API will be used to write the Telegram bot that is the main user interaction point of our application.\
To implement the backend part of the website and its communications with the database and the machine learning unit, we will use the Django Python framework. 

#### **Scalability and Performance**
To provide the best performance for the users, we plan to employ Docker containerization enabling our application to scale.\
We understand that the machine learning procedure will require a large number of resources and, therefore, we consider scaling our application such that the machine learning unit will be run across multiple environments. This architecture will enable us to distribute the machine learning unit across multiple containers, ensuring efficient load balancing and high availability for users.

#### **Security and Privacy** 
To protect user data, we will implement the best authentication and encryption practices. Our application will employ JWT (JSON Web Tokens) for secure user authentication. \
Additionally, the user information will be hashed and encrypted before being stored in the database. 

#### **Error Handling and Resilience** 
Our project will designed in such a way to prevent crashes and to log errors. Possibly, the application will be deployed across multiple servers using a cloud provider like AWS to ensure high availability and fault tolerance. This separation is necessary to implement graceful error recovery and to follow the best monitoring practices.

#### **Deployment and DevOps**
Our team has decided to build, test and deploy our application using the CI/CD pipelines. Each unit of our project will be built, tested, and deployed separately, following a microservices architecture approach.\
This microservice approach will enable our team to rapidly fix errors and to add new functionality to different parts of the application.  

## **Week 2 questionnaire:**  

1) **Tech Stack Resources**. To develop this project our team members decided to utilize several project-based books. We believe that these books will help us to deepen our knowledge of our technological stack, help to resolve arising issues if any, and help us to effectively provide value for our project. 

| Name of the book | Author | Value for our team |
|--------------------------|---------------|-----------------|
| Clean Code | Robert Martin | This book is about writing the code that is not only able to function, but is also easy to support and organize. We believe that this book will help us organize our project in an effective manner and evade potential risks. |
| Docker Deep Dive | Nigel Poulton | This book will help us familiarize ourselves with Docker and orchestration. This information is valuable as we will try to follow the microservice approach and spread our application across multiple servers. | 
| Django for Beginners | William S. Vincent | Our team believes that this book will help us learn Django to develop the backend part of our website, work with databases and manage the API. |



2) **Mentorship Support**. We do not have a mentor actively involved in our project, but we believe that having a mentor could positively influence our project by providing expert guidance in several ways. For example, mentor could help our team to avoid common mistakes. Moreover, he could help us to make decisions regarding the project's architecture and implementation details. 

3) **Exploring Alternative Resources**. In addition to project-based books, we have explored various resources to expand our understanding of our tech stack. \
*Online courses* -- Platforms like Coursera, Udemy and FreeCodeCamp have several courses on SQL, Django and Docker. \
*Video tutorials* -- Several Youtube channels of programming professionals can help us deepen our knowledge of our tech stack. Some of these channels are: Corey Schafer and FreeCodeCamp. \
*Documentation* -- Official frameworks' documentation has a lot of useful information that can help us implement the application and to solve the issues that we run into while developing the project. 

4) **Identifying Knowledge Gaps**. Our main knowledge gap is in Docker and orchestration. To address this, we plan to employ several solutions. \
First, we will attempt to seek help from friends who have experience with Docker and container orchestration. \
Secondly, we will use resources mentioned before (online tutorials and guides) to fill this knowledge gap. 

    We have divided our tech stack into the following teams:
    1. *Frontend Development* -- working on the website appearance and interface;
    2. *Backend Development* --  working on the website and telegram bot underlying logic;
    3. *Machine Learning Development* -- developing the chatbot models using machine learning;
    4. *CI/CD pipelining* -- managing deployment and CI/CD pipelines.

    Each team will focus on addressing their specific knowledge gaps through collaboration and using the resources mentioned above.

5) **Engaging with the Tech Community**. Engaging with the Tech Community could positively affect our team and project in several ways. Our team could participate in online forums and groups (for example, StackOverflow) to seek experienced people, their help and guidance. Moreover, our team could attend local meetups in Kazan and Innopolis to listen to professionals and deepen our knowledge. 

6) **Learning Objectives**. This week our frontend developers are actively improving the website appearance and interface. More precisely, they are learning advanced tools like React to create a modern and user-friendly website. \
Additionally, machine learning developers from our team are developing a concise plan for implementing the machine learning unit for our project. \
To achieve these learning objectives we will use online resources like online courses and tutorials. Moreover, our teammates are actively collaborating in order to rapidly solve issues and make decisions.  

7) **Sharing Knowledge with Peers**. Every week our team organizes meetings to discuss challenges and to make decisions on the next objectives. Moreover, we propose solutions to existing problems and exchange information about achieved results. This discussion sessions help our team organize the working process, rapidly solve problems and keep our team organized and collaborative.  

8) **Leveraging AI**. To compensate for lacking expertise in our tech stack we also use ChatGPT and GitHub Copilot. Some of our team members use these tools to ask questions, resolve issues and sometimes to generate code. However, we try to thoroughly understand any answer or code generated by an AI tool. This is because we believe that AI tools' responses always have to be checked beforehand, because these tools may provide false data or vulnerable code. 


### **Tech Stack and Team Allocation**
After finalizing the consideration of technological stack and team allocation, each team member was assigned to a backend/frontend/ML part of the project according to his experience, interests and skills. We have defined the role and tech stack for each member to ensure that everyone have been assigned to an appropriate task.

Roles and stack distribution:

| Team Member              | Project part   | Tech stack   | Responsibilities |
|--------------------------|---------------|-----------------|-----------------|
| Andrey Kupriyanov        | Machine Learning | Python, Pytorch, Tensorflow, Keras | Leads the development of the machine learning unit. |
| Egor Poliakov            | Machine Learning | Python, Pytorch, Tensorflow, Keras | Developer of the machine learning unit. | 
| Kamil Sitdikov           | Frontend Development | React, HTML, CSS | Develops the website and the user interface. |
| Mikhail Kalinin          | Backend Development, Reports | Python, Django, SQL, Markdown | Supports the development of the website. Writes weekly reports. | 
| Emil Gainullin           | Backend Development | Python, SQL | Organizes the work with the Database. |
| Almaz Gayazov            | Backend Development | Python, TelegramAPI, SQL | Implements the telegram bot. |
| Egor Nischikh            | Fullstack Web Development | Python, Django, SQL, React | Implements the underlying logic of the website. Facilitates the frontend development of the website. |

---

### **Weekly Progress Report**

This week our team took several steps in several parts of our project. \
Firstly, we have developed the user interface design. We tried our best to create the most appealing and user-friendly interface of our website. \
Secondly, we finalized creating the architecture plan of our project. We have discussed the technological stack, assigned the roles and outlined the most important interactions between components of our project. \
Our machine learning developers brainstormed implementation ideas for the machine learning unit of our project and started the preliminary work. \
Our backend developers team began implementing secure user authentication using JWT and initializing the database to store user data.

We faced challenges in brainstorming user interface design ideas, deciding on the best possible user experience on our future website. Additionally, our team had to resolve the issue with the telegram bot -- we had to decide on the exact user interactions within the telegram bot part of our project. \
Finally, we had to clearly understand the role of Docker and orchestration within our project. 

**Key lessons**

Our team practiced effective communication, brainstorming ideas, and problem solving skills. This week our team has successfully resolved all the arisen issues.