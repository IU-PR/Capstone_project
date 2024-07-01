---
weight: 2
bookFlatSection: true
title: "Week #2"
---


# Week #2

### **Tech Stack Selection**

- Frontend: Figma, SvelteKit
- Backend: Python, FastAPI
- Database: PostgreSQL
- Telegram Bot: Python, Aiogram

### **Architecture Design**

1. **Component Breakdown**: Below is the model of the project architechture. It contains the outline and descriptions of the main project components.
    
    ![c4](/2024/LLTeam/week1/c4.jpg)
    
    Our backend application is presented as an API service that processes business logic. It serves several frontend implementations: 
    
    - A website consisting of a users' control panel, where they can interact with created links, and a redirect page, which is served to short link followers
    - A Telegram Bot, providing the same functionality as the Web App to manage links


2. **Data Management**: We use PostgreSQL for storing and managing the service data.
    ![erd](/2024/LLTeam/week2/erd.svg)
    - The `Users` (user information) and `Tokens` (session storage) tables are used for the logic of user accounts
    - The `Links` table stores all created links, and the `Banners` table stores information about the banners that appear before the redirect — we store them as a separate entity
    - The `Redirects` table stores all redirect events for a short links
    
3. **User Interface (UI) Design**: User Interface will be delivered in the format of web frontend application. During the process of UX/UI design, the user experience (UX) and design principles were considered:
    - Flowchart & user stories — representation of user’s journey through the application using user stories in [Figma sketch file](https://www.figma.com/board/KgVoL9hHxk4ozTUbwjQerF/UX-Flowchart?node-id=0-1&t=WB7jVFZ2U7qkgVna-1).
    - Wireframing — first version of UI layout for desktop is created in [Figma design file](https://www.figma.com/design/cmUJUrV3SsOqX8GXTZvsKH/LinkLink-In?node-id=1-2&t=6KvIGb1kaesy4RUK-0).
4. **Integration and APIs:** 
    Currently, we plan no integrations with external services.
    
5. **Scalability and Performance**: We plan to use following techniques to ensure the scalability and performance of application:
    - DB indexes — implementation of indexes on frequently queried columns in tables. The record retrieval time is expected to be significantly reduced.
    - Additional key-value based database integration for short links — integration of a such database in case of the increasing user load and the amount of links will optimize the overall system architecture and decrease the load.
    - Database cache integration — caching mechanisms could be integrated along our main database. Storing frequently accessed data is expected to reduce the load on the main database.
    - Load balancing — distribution of the application across multiple nodes ensures that no single server is overloaded. Load balancer will manage the incoming traffic.
6. **Security and Privacy:**
    - Our service assumes the implementation of accounts where each user has access exclusively to their links. 
    - Hashing will be used to securely store sensitive data such as passwords and passphrases in database. 
    - Containerization of the project modules with Docker will provide additional security for the service.
    
7. **Error Handling and Resilience**: 
    
    Our strategy for fast error handling focuses on two key areas: advanced logging and swift recovery measures. Advanced logging mechanisms are being implemented to provide immediate insights into runtime errors, allowing us to quickly identify and resolve issues.
    
    We have prepared a recovery plan that includes the automated restart of error-affected nodes. This proactive approach aims to minimize service disruptions and ensure continuous availability, underscoring our commitment to providing a reliable and efficient service.
    
8. **Deployment and DevOps:**

    The application will be deployed in containers using Docker and Docker Compose
    
    We intend to set up a robust CI/CD with using of GitHub Actions for automatic testing and continuous deployment of developed software. 
    

### **Week 2 questionnaire:**

1. **Tech Stack Resources:** At the moment, we are not utilizing project-based books that specifically cover our tech stack. We are using other online resources about our tech stack components to enhance our knowledge rather than books.
2. **Mentorship Support:** We have considered seeking the mentor, but at the moment, we do not plan to consult experts or involve students from other teams.
3. **Exploring Alternative Resources:**
    - [FastAPI documentation](https://fastapi.tiangolo.com/)
    - [Svelte documentation](https://svelte.dev/docs)
    - [SvelteKit documentation](https://kit.svelte.dev/docs)
    - [PostgreSQL documentation](https://www.postgresql.org/docs/16/index.html)
    - [aiogram documentation](https://aiogram-birdi7.readthedocs.io/en/latest/)
4. **Identifying Knowledge Gaps:** Several frontend developers have no prior experience with SvelteKit. However, such knowledge gap may be dealt with studying the documentation of this framework. Moreover, most of the developers have React knowledge that can significantly accelerate concept learning.
5. **Engaging with the Tech Community:** Our team did not participate in forums or meetups. However, we are engaged with the broader tech community via online communities and tech stack-specific chats.
6. **Learning Objectives:** Frontend developers have set the goal to learn `SvelteKit` as this is a new framework for most of them. Backend developers focus on improving development skills to build reliable and safe API. Moreover, our DevOps engineers aim to learn how to set up a robust `CI/CD` for the application and perform operations with its use. Additionally, our team intend to gain practical skills in setting monitoring and logging system as well.
7. **Sharing Knowledge with Peers:** During the planning of our service architecture we have shared our knowledge quite extensively, as we had to discuss pros and cons of different approaches, sharing diverse expertise and experience from our previous projects.
8. **Leveraging AI:** We leverage AI to accelerate the development process and enhance our knowledge of technologies from the stack. We may use LLM for explaining challenging programming concepts and debugging if necessary.

### **Tech Stack and Team Allocation**

| Team Member | Track | Responsibilities |
| --- | --- | --- |
| Evgeniy Anisov | Team Lead & Architecture & Backend | Project management and development of a strategy; Making architectural decisions; Backend development |
| Maksim Kamenetskii | Backend & DevOps; | Backend development; DevOps engineering |
| Munir Khisamov | Backend & DevOps | Backend development; DevOps engineering; |
| Roman Pogrebnyak | Backend  & Frontend | Fullstack development |
| Polina Moiseeva | Frontend & UX/UI Design | Frontend development; Reporting |
| Daniil Nikulin | Frontend & UX/UI Design | Frontend development; UX/UI app design |
| Marat Akhmetov | Backend | Backend development; Reporting |

### **Weekly Progress Report**

During this week we mostly planned our future service design:

1. Architecture of application
2. Architecture of database
3. Develop a user flow
4. Develop a first version of UI layout

And also, on development side, some proof-of-concept API endpoints have already been written to serve as starting point of our development process.

### **Challenges & Solutions**

- Challenge of robust architecture.

    Our team has faced the challenge of building a robust and resilient architecture. To accomplish this mission, we decided to come to solution collectively by discussing several approaches and keeping in mind different tradeoffs and reach the most optimal solution.

- Challenge of tech stack.  

    There was a tradeoff between technologies we already know and those that we find most suitable for the project. Although some of the front-end team members are unfamiliar with `SvelteKit`, we decided to use this framework as it is very efficient and supports fast development cycles. And we also decided to use `Python & FastAPI` for back-end as a balance between expertise we have and efficiency a framework can provide.  

### **Conclusions & Next Steps**

In conclusion, our team has accomplished one of the most significant milestones — design of the architecture and choice of tech stack. These tasks required the engagement of all team members, which was reached by regular meetings and discussions. We talked over versatile approaches and tech stack options and came to the project consensus.

Our next step will be the start of application development to deliver the first prototype in the future.