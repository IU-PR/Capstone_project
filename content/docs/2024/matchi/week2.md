---
title: "Week # 2"
---

# Match&Watch: Project Report for Week 2

## **Tech Stack Selection**

| Backend                                                                                               | Frontend                                                                                                          |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white) | ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) |

| ![postgresql](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-306998?logo=python&logoColor=white) |
| ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## **Architecture Design**

### **Component Breakdown**

- User Profile Management: A microservice to keeps track of user profiles, their personal traits, their hobbies, their general preferences, and their movies history.

- Mood Extraction Model: It accurately extract mood features from user responses by combining common industry methedologies, and preprocessing reliable public datasets.

- Recommendation System: A microservice which will be responsible for giving the movie picks by using the developed models along with the user personal information, personal traits and hobbies, and past preferences.

- User Interface: We showcase our product by developing a modern frontend interface with a very convenient user experience.

### **Data Management**

- The platform will employ a relational database management system (we might have non relational DBMS also ). We will use PostgreSQL to store user profiles, movie preferences and personality aspects

### **User Interface (UI) Design**

- We have agreed on the main design for our website The design are available on figma and can be accessed through the following link: https://www.figma.com/design/R6yh9RPTT7hIzjcS1LVZdK/Match-%26-Watch-Design?node-id=0-1&t=YbytWJyPrmN73iCK-1

### **Possible Integration and 3rd party APIs**

- IMDb API
- TMDb API (Comprehensive movie and TV show details)

### **Scalability and Performance**

- Our platform will leverage Kubernetes to ensure scalability. Kubernetes facilitates seamless scaling by dynamically allocating resources according to demand
- Stress tests are conducted to maintain or improve performance, especially under concurrent operations.

### **Security and Privacy**

- The platform will implement advanced hashing techniques to secure sensitive data. We will utilize Docker and GitHub Secrets to manage sensitive variables securely. Additionally, robust authentication and authorization mechanisms will be implemented to protect user data and ensure privacy. Unit tests will be written to mock database operations, ensuring that security measures are validated throughout the development lifecycle.

### **Error Handling and Resilience**

- Our approach will integrates manual testing and unit testing to thoroughly validate code, ensuring robust error handling and proactive issue identification to enhance application resilience. Specifically, we utilize custom FastAPI exception classes meticulously crafted to address every potential issue. Each type of error is assigned a clear error code, documented comprehensively for clarity and efficient troubleshooting.

### **Deployment and DevOps**

- We will implement CI/CD (Continuous Integration/Continuous Deployment) using GitHub actions. this tool will automate the build, testing, and deployment process, ensuring efficient software delivery.
- Note : we use 4 repos. But for the course submission, we will stick with the usual requiement of 1 repo in the course org. so for The detailed work will be mainly showcasen in the 4 repositories in our personal accounts. Some of these details can't be realistically realized on 1 repository (the course org repo).

## **Questionnaire**

1. FastAPI ,Vue.js Documentation and kaggle for ML .

2. We currently do not have a mentor.

3. We expanded our understanding for the technical stack mainly by researching and reading articles online and resources provided by the frameworks we are using.

4. We do not feel that we are facing knowledge gaps at the moment.

5. we heavily rely on online resources for our work ,also we can conveniently discover solutions to any inquiries on platforms like Stack Overflow.

6. Our team employs the Scrum methodology with one-week sprints to manage teamwork efficiently. To track our progress, we utilize a Backlog where tasks are assigned and organized. At the conclusion of each sprint, we conduct meetings to review our achievements and assess the outcomes of our efforts.
   out task for this week : - registration and login mechanism - Dummy post endpoint for movie recommnedation - Dockerization

7. We organized several meeting for for discussion and knowledge sharing
8. Currently, we haven't integrated AI to compensate for any gaps in our tech stack. Our approach relies on the expertise and experience of our team to develop and maintain our platform.

## **Tech Stack and Team Allocation**

| Team Member    | Track (in general) | Responsibilities (For this week)                              |
| -------------- | ------------------ | ------------------------------------------------------------- |
| Louay Farah    | Backend            | create post endpoint for movie recommendation                 |
| Saleem Asekrea | Backend            | Start creating authentication mechanism                       |
| Aymen Daassi   | Frontend/Design    | Create the design for the website using Figma                 |
| Karam Khaddour | Frontend           | Start working on the log in and sign up pages                 |
| Laith Nayal    | ML                 | make research on AI and determined the model structure to use |

## **Weekly Progress Report**

- Created the design for the website using Figma, start working on the authentication and endpoint for movie recommendation

## **Challenges & Solutions**

The challenging part is to develop a method to accurately extract mood-related features from user responses to a series of questions. Since we haven't found data that directly categorizes movies by mood or mental state, we will likely perform reverse engineering to address this issue. We plan to extract mood-related tags from movie plot summaries then use these results to map the answers from the users with movies.
Another challenge is deciding among different types of recommendation systems, such as collaborative filtering, content-based filtering, hybrid systems, and deep learning-based systems, to choose the one that best fits our goals. We will make this decision once we finalize the process of generating the questions that users will answer.

## **Conclusions & Next Steps**

During this week, our team made significant progress in various areas of the project. We successfully created the initial design for our website using Figma, which provides a solid foundation for the frontend development. The backend team has started implementing the authentication mechanism and created a dummy POST endpoint for movie recommendations. Additionally, we have established a clear direction for our machine learning model, focusing on mood-related features and recommendation system types.

1. Registration
2. Login
3. create an endpoint for a dummy movie recommnedation scenario
4. Dockerization
5. Finalize the concept for generating user questions that will guide the recommendation process (Decide on the methods combination, categories to determine the current mood, question generation, etc.)
6. Extract categories' scores which will determine the current mood by looking at a person's current state from all prospectives, from movie data (summary, tags, genre, year, etc.). We could also explore existing datasets that categorize movies by mood.
