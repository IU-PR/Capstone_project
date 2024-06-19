---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

For the current project our team has decided to use the next tech stack: ReactJS, Kotlin, FastAPI, PostgreSQL, Docker, GitHub Actions.

### **Architecture Design**

1. **Component Breakdown**: 
    
    * ReactJS for frontend website design

    * Kotlin Multiplatform, Compose Multiplatform, Ktor, Kodein, Decompose + MviKotlin for mobile development
    
    * FastAPI for backend development
    
    * PostgreSQL for data storage
    
    * Docker for deployment
    
    * GitHub Actions for testing. 

2. **Data Management**: PostgreSQL

3. **User Interface (UI) Design**: Figma

4. **Integration and APIs**: FastAPI for backend development

5. **Scalability and Performance**: Trello deck for checking the task completion

6. **Security and Privacy**: 1FA for user authentification

7. **Error Handling and Resilience**: Unit tests \& GitHub Actions for CI/CD pipeline

8. **Deployment and DevOps**: Docker

### **Week 2 questionnaire:**

1) Tech Stack Resources: Tech Stack was chosen by discussing with other group members \& searching for solutions through Google and YouTube

2) Mentorship Support: Our team have discussed the tech stack with our assigned TA and determined the main vector of our work for current week.

3) Exploring Alternative Resources: Searching solutions for the design through the internet, particularly from dribbble.com

4) Identifying Knowledge Gaps: Lack of knowlege in dockerizing the Alembic tool

5) Engaging with the Tech Community: Checking solutions for dockerizing Alembic on Stackowerflow \& GitHub

6) Learning Objectives: 
    * Efficient designing workflow through Figma

    * Projecting a created design in form of mobile application

    * Database structuring

    * Working with Alembic for database migration

7) Sharing Knowledge with Peers: Created the Trello deck for better task management

8) Leveraging AI: Used PyCharm AI assistant for improved autocompletion

### **Tech Stack and Team Allocation**

| Team Member       | Track             | Responsibilities                |
|-------------------|-------------------|---------------------------------|
| Anton Chulakov    | Designer          | Design of the mobile application|
| Denis Mikhailov   | Web backend       | Registration \& authorization   |
| Arseny Savchenko  | Mobile            | Mobile application development  |
| Ilya Zubkov       | Frontend          | General structure creation      |
| Sergey Atkonov    | Quality Assurance | Report                          |


### **Weekly Progress Report**

#### **Design**

Current state of the application design:

<figure>
    <img src="/2024/CookingCorner/icon.jpg"
         width="240" height="200">
    <figcaption>Icon of the mobile application</figcaption>
</figure>


![](/2024/CookingCorner/splash_screen.jpg)

![](/2024/CookingCorner/main_screen.jpg)

![](/2024/CookingCorner/Sign_up.jpg)

![](/2024/CookingCorner/sign_in_form.jpg)

![](/2024/CookingCorner/mobile_sign_up.jpg)

![](/2024/CookingCorner/mobile_sign_in.jpg)

Link for better acknowlegment with the design: https://www.figma.com/design/VutdYJEW7nxaz0BhGJExvL/Cooking-Recipe-App-design?node-id=0-1&t=UEvomQhrpfn9WVeD-1

#### **Mobile**

1. Implemented core architectural aspects (UDF architecture with MVI pattern)

2. Implemented UI layer for Sign In / Sign Up for both mobile platforms

3. Implemented core business logic aspects for authorization (caching of login & password + network client implementation)

4. Implemented Unit test to check the connectivity of DI dependency graph during compile time (Kodein Service Locator library was used)


#### **Web backend**

1. Implemented core architecture

2. Implemented login/register/logout endpoints

3. Configured launch of backend and database via docker-compose

4. Created general database structure and implemented orm models (User, Category, Tag and Recipe for now)


### **Challenges & Solutions**

Authentication was implemented, but needs testing. Unit tests should be created for future work; Alembic was hard to integrate with Docker: it required additional script for running it.

### **Conclusions & Next Steps**

In future our team will create 

* Functionality for recipes (creation, deletion, correcting, adding to favorites, tags creation)

* Backend connection with mobile application, UI \& authentication testing

* Creating the user profile

