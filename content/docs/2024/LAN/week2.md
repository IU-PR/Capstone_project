---
title: "Week #2"
---

# Week #2

## **Team Allocation**

| Team Member              | Occupation                    | Responsibilities                         |
|--------------------------|-------------------------------|------------------------------------------|
| Alexey Tkachenko         | Leader                        | Lead the team and decide team objectives |
| Andrey Gerasimov         | Leader of Fronted development | Main frontend developer. UI/UX.          | 
| Kirill Archipov          | Assistant frontend developer  | Assistive frontend development           |
| Elina Pavlova            | Designer                      | Design of the product, public image      |
| Olga Puzhalina           | Marketing & Client researcher | Marketing management, customer development, UX elaboration |
| Rodion Chikibaev         | Leader of Backend development | Lead the backend team                    |
| Timur Zheksimbaev        | Assistant backend developer   | Primary backend developer                |

## Architecture Design 
1. **Component Breakdown:**
   At the moment, our application consists of 3 primary services:
   - Frontend of the webapp for user interaction
   - Backend of the webapp
   - Telegram bot for distributing the webapp

   We hoped that we would be able to provide a comprehensive component diagram with detailed development phases, however, we could not make it in time for the report. We will provide it next week.

   Right now we have design flowcharts for our core features, such as Matching and Routines:

   ![MA](ma.png)

   ![routines](routines.png)   

   Here are the links:

   https://drive.google.com/file/d/1nXDaNAshYR5E49ns1KhzdZZ0YZU0vw1H/view?usp=drive_link

   https://drive.google.com/file/d/187WwcdZDA0xKm-I0CT2W1UzY2IlE1Htl/view?usp=drive_link


   Open the link, then press "Open with..." at the top of the page and select draw.io

2. **Data Management:**

   Here you can view our database design:

   ![ERD](erd.png)


   ![RD](rd.png)

   Our backend developers decided to use Postgres to store the data. We do not plan to store any passwords, since we will use authentication via Telegram, so less worries about data security. We plan to learn best business practices for deploying our database in production from prof. Hamsa Salem. We have already contacted them during database design, and we plan to engage with them further.

   Here's the draw.io file for the diagrams:

   https://drive.google.com/file/d/1YLfxw9JNmRe4kPnlMPxqYOB2V3dftZp_/view?usp=drive_link

   Open the link, then press "Open with..." at the top of the page and select draw.io

3. **User Interface (UI) Design:**

   Here is our Figma design:

   https://www.figma.com/design/nsMVIUzWCZDg0S8kwunA8J/CoLife?node-id=564-268&t=nA3PtvmWaSsbQN30-1

   This our first draft of the design of the Telegram webapp. Our team could not collect user experience data to evaluate and iterate on this design, however, we plan to do so next week during the development of the first prototype.

4. **Integration and APIs:**
   
   Our backend team was supposed to draft up the API design in Postman or Hoppscotch, however, due to lack of experience, we only completed Routine microservice.

   https://www.postman.com/mission-candidate-68304040/workspace/capstone/collection/34862374-57bf1d0c-2a92-40be-9f53-658f3d2eab55

   We plan to finish up the remaining 2 microservices the next week, so that we can reference them during development


5. **Scalability and Performance:**

   We plan to implement our application as a set of scalable microservices. This will ensure that we can easily scale for waves of new users and add new features in the future.

   We anticipate problems using only Postgres to store all of the data. From little research we did, the possibilities are overkill for our MVP (which is a release for IU students). Django has a lot of built-in tools that will help us connect our app to its database.

6. **Security and Privacy:**

   Since our application will use login with Telegram feature, we only will require a rudimentary token-based authentication service. Our backend team has already found resources to study while learning how to implement such a service.

7. **Error Handling and Resilience:**

   - **Backend**:

      To handle errors, we will utilize the following tools:

      1. The built-in Python module `logging` for logging purposes. This module has extensive documentation and support, making it suitable for our project.
      
      2. We anticipate a significant volume of logs, as we require logs for each of our services, including user interactions, authentication, and various critical operations. Therefore, we plan to implement several log management strategies:
         - **Log Rotation:** Implement log file rotation to prevent a single log file from growing indefinitely.
         - **Log Archiving:** Archive or compress older log files to free up disk space while retaining historical log data for future reference or analysis.
         - **Log Levels:** Configure appropriate log levels (e.g., DEBUG, INFO, WARNING, ERROR) to control the verbosity of logging.

      3. For testing, we will use the framework provided by Django for creating tests.
      4. Backend development involves a variety of testing types, including:
         1. Unit Tests
         2. Integration Tests
         3. Functional Tests
         4. Performance Tests
         5. Security Tests
         6. Regression Tests
      5. In our project, we will use the following types of tests:
         1. Unit Tests: For testing individual components.
         2. Integration Tests: For testing the integration between different components.
         3. Security Tests: To ensure the security of our system.
   - **Frontend:**

      **Which tests will help us write quality code**
      - **Unit Tests:** Contribute to writing quality code by testing each module or function.
      - **E2E Tests:** Provide confidence that the application works correctly in real usage scenarios.
      - **Functional Tests:** Ensure that the application performs its primary functions correctly.
      - **User Interface Tests:** Guarantee correct interface display across different devices.

8. **Deployment and DevOps:**
   During our meeting with Rustam Luckmanov our leader has asked them if IU could provide us with hosting options if any. Right now our options are either to use IU's servers, or host everything on our private services. Our lead programmers have opted to use GitLab as the hosting platform, since it allows so with its Actions feature. We also consider renting VPSs, however, the discussion is still ongoing.

# Week 2 questionnaire:

   **Tech Stack Resources:**

   Since we chose popular and industry-standard frameworks for development, we have access to high-quality documentation.

   **Mentorship Support:**

   Currently, our only mentor is prof. Hamsa Salem for database design & deployment. We plan to ask for more help as we start developing our prototypes. Namely, we might need advice from IU NLP for our improved AI-powered matching algorithm, which we have not documented yet and postponed for Prototype 2. Our project is still very early in development, and we anticipate a lot of questions to our future mentors. 

   **Identifying Knowledge Gaps:**

   Our main knowledge gap is the lack of industrial production development & deployment. We plan to ask IU professors for advice.

   Our team also has little experience in the techstacks they chose. 

   **Engaging with the Tech Community:**

   Primary reasons to choose our current teckstack despite the lack of experience was their apparent simplicity, and, most importantly, rich documentation and a large developer base. We hope we can find help on forums (Discord, Discourse, StackOverflow, others) related to technologies we use.

   **Learning Objectives:**
   We plan to expand our knowledge in domains outlined in "Occupation" section of "Team allocation"

   **Sharing Knowledge with Peers:**
   We hold meetings every week to ensure that everybody is staying on track. We formulate tasks and track their progress using Linear.

   **Leveraging AI:**

   Currently, we mostly use aggregation tools like ChatGPT, Phind.com, perplexity.ai to learn new technologies and quickly cover our knowledge gaps.


