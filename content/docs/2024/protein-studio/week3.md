---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

To create a technical infrastructure that is efficient for coding and testing, our team decided to establish the workflow via GitHub to employ a version control system and to effectively share the code among team members.

Next, we will focus on consideration of hardware requirements for our project deployment. For example, we have to understand the system requirements to run the Machine Learning Units. Moreover, we have to consider handling multiple users and distributing the workload between multiple servers. 

Finally, we will have to consider the DevOps part of the project which will include Docker and containerization of different parts of the project. Containerization will provide the basis for future testing and deployment of the application.

- **Backend Development**:

This week we plan to design the API that will be used to communicate between frontend and backend parts of the project. 

Next, we have to create the Telegram Bot and connect it to the Machine Learning model, such that the user will be able to have a conversation with the basic model.

Finally, we have to implement the authentication for the users to be able to authorize on the website.

- **Frontend Development**:

Firstly, we plan to finish designing the frontend part of our project and start implementing the website.

Secondly, our team has to build the main components of the application in React and start assembling the website following the design.

Finally, we have to integrate the API from our backend part of the project to make the website functional and usable. 

- **Data Management**:

This week our team plans to set up the database for storing the user data. The database will be used to store and retrieve user logins and passwords. In the future, the database will be updated to store the machine learning models as well.


- **Prototype Testing**:

To test the project's usability, we will have to check if our project aligns with the predetermined requirements. This approach will help us determine the issues that users experience when using our project.

## **Weekly Progress Report**:

#### **Frontend**
This week we have implemented a prototype of the website with the basic UI elements. Our frontend developers reserved the space for buttons and other elements that will be added in the future.

<div style="text-align: center;">
<img src="/2024/protein-studio/prototype1/website_ui.jpg" width="800" height="800"> 
</div>

<div style="text-align: center;">
<img src="/2024/protein-studio/prototype1/website_auth.jpg" width="800" height="800"> 
</div>

<div style="text-align: center;">
<img src="/2024/protein-studio/prototype1/website_login.jpg" width="800" height="800"> 
</div>

#### **Backend and Database**
At the moment, the registration, authentication and authorization systems are fully implemented. 

To get access to the main functions of the site, the user must create their own account. To do this, the user needs to fill in the appropriate fields -- type his email and come up with a password. After that, he will be able to log in.

After registration, some user data is stored in the database (remark - there is no way to enter your username on the site yet). Each user is assigned an ID, and the password is encrypted. When the user successfully logs in, the server generates a JWT and stores it in cookies, which are stored for an hour. 

In addition to the main table in the database, which stores all the basic information about the user, there is a table for storing information about the status of user accounts. Users can have premium or common status. Upon registration, each user is assigned the status of a common user.

<div style="text-align: center;">
<img src="/2024/protein-studio/prototype1/database_user.jpg" width="800" height="800"> 
</div>

<div style="text-align: center;">
<img src="/2024/protein-studio/prototype1/database_roles.jpg" width="500" height="500"> 
</div>

#### **Machine Learning Unit and Telegram Bot**
The machine learning developers have created a neutral conversational model. Moreover, the user is already able to talk with the model via the Telegram Bot. The telegram bot runs locally. The user can provide the basic token and talk communicate with the model via telegram messages.

An example of communication with the model via telegram bot:

<div style="text-align: center;">
<img src="/2024/protein-studio/prototype1/bot_example.jpg" width="300" height="200"> 
</div>


### **Challenges & Solutions**

Our main challenges were: \
    1. Creating the neutral language model. The solution was found by communicating with students from other groups and exploring the internet resources. \
    2. Establishing the connection between the language model and the telegram bot. Our developers had to organize team meetings to discuss the problem and come up with potential solutions. Finally, the problem has been solved.

### **Conclusions & Next Steps**

This week we were able to deliver the first prototype of our project. Now, each part of the project was developed to some minimal usability extent. The first prototype includes such main components as: functional neutral language model, functional telegram bot, authentication and authorization on the backend part, first prototype of the UI design, and the first database set up.

We plan to continue developing our project. Our next tasks include finalization of the frontend part of the website, creating advanced language models that will be able to mimic specific individual's communication style, and continuing to develop the backend API to support more features (e.g. creating the custom language model on the website).