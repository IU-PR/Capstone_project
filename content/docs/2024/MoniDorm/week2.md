---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

**Python 3** 🐍
- [aiogram3](https://docs.aiogram.dev/en/latest/) — for Telegram bot
- [pylint](https://pypi.org/project/pylint/) — python code linter
- [jinja2](https://pypi.org/project/Jinja2/) — generate emails for email confirmation, generate json file for crashes

**HTML/CSS** — appearance of email confirmation email

**MongoDB** 🌱 — a database for storing the state of bot users

**CI/CD** ⚙️
- GitHub Actions — Fully Qualified CI/CD pipelines with the immediate pushing of the latest version of product
- bash — for writing automation scripts
- SonarQube — Linter for the code quality

**Docker** 🐳 — running microservices in containers

**Docker-compose** 🐙 — managing the launch sequence of all containers

**Java 21** ☕️

- [SpringBoot 3.2](https://spring.io/projects/spring-boot) — Web, REST Controllers
- [SpringBoot WebFlux](https://docs.spring.io/spring-framework/reference/web/webflux.html) — HttpClient
- [SpringData JPA](https://spring.io/projects/spring-data-jpa) — Database Manipulation
- [SpringBoot Metrics](https://docs.spring.io/spring-boot/reference/actuator/metrics.html) (Actuator, DevTools) — Metrics
- [Lombok](https://projectlombok.org/) — Code Boilerplate Reduction
- [JUnit](https://junit.org/junit5/), [AssertJ](https://assertj.github.io/doc/), [TestContainers](https://java.testcontainers.org/) — Unit + Integration Test

**PostgreSQL** 🐘 — main database with all records about reports

**Liquibase** — Version management of DB (migrations)

### **Architecture Design**

1. **Component Breakdown**:
    
    **Backend Components**

    - <u>API:</u>

        1. Serve as the primary interface for data interaction between the frontend, Telegram bot, and databases.
        2. Handle requests related to reporting issues, fetching user data, and managing statistics.
        3. Ensure secure and efficient communication between components.

        Interactions:
        - Receives and processes data from the Telegram bot and WebApp.
        - Communicates with PostgreSQL for report storage.
        - Interfaces with the LLM system for comment analysis.
    - <u>PostgreSQL Database for reports:</u>

        1. Store and manage reports related to dormitory infrastructure issues.
        2. Maintain data integrity and support complex queries for report statistics and analysis.
        
        Interactions:
        - API communicates with PostgreSQL to store, retrieve, and update report data.
        - WebApp queries PostgreSQL for generating statistics and reports.
     - <u>MongoDB Database for bot:</u>

        1. Store and manage user information, including user profiles and interaction history.
        2. Provide a flexible schema for handling diverse user data.
        
        Interactions:
        - Telegram Bot uses MongoDB to store, retrieve, and update user information.
    - <u>LLM System:</u>

        1. Analyze comments in reports to extract insights and detect patterns.
        2. Assist in categorizing issues and providing additional context for reported problems.
        3. Summarize comments in several reports to identify one common problem.
        
        Interactions:
        - Receives comments from the API for analysis.
        - Sends analysis results back to the API to enhance report data.

    **Frontend Components**

    - <u>Telegram Bot (+ REST Listener):</u>

        1. Provide a user-friendly interface for students to report issues.
        2. Collect data such as the type of failure, location, and user comments.
        3. Send notifications and updates to users about the status of their reports.
        4. Perform authorization for security.
        
        Interactions:
        - Sends collected report data to the API.
        - Receives notifications and updates from the API to send back to users.
    - <u>WebApp for Admins:</u>

        1. Provide a dashboard for administrators to view statistics and manage reports.
        2. Display data visualizations for better understanding of infrastructure issues and user interactions.
        3. Allow admins to update report statuses and communicate with users if necessary.
        
        Interactions:
        - Queries the API to fetch report data, user information, and analysis results.
        - Displays statistics and insights fetched from PostgreSQL and MongoDB.

2. **Data Management**:

    Our system has two databases for reports (PostgreSQL) and for user information (MongoDB).

    **PostgreSQL Database (for Reports)**
    
    <u>Why we deciced to choose this database:</u>
    - Relational database structure to handle structured data efficiently.
    - Support for advanced querying and indexing to enhance performance.
    - ACID compliance to guarantee transactional integrity and reliability.

    <u>Purpose:</u>
    1. Store and manage all reports related to dormitory infrastructure issues.
    2. Ensure data integrity, support complex queries, and facilitate efficient data retrieval for reporting and analysis.

    <u>Data Types Stored:</u>

    Report ID, category of failure, placement, failure date, proceeded date, owner email, information about failure confirmation by admin or analysis mechanism, information about resolving problem by admin or user, full description.

    **MongoDB Database (for User Information)**

    <u>Why we deciced to choose this database:</u>
    - NoSQL database structure for handling unstructured and semi-structured data.
    - Schema-less design allowing easy updates and scaling.
    - High availability and scalability to accommodate growing data volumes.

    <u>Purpose:</u>
    1. Store and manage user information, including user profiles and interaction history.
    2. Provide a flexible schema to handle diverse and evolving user data requirements.
    
    <u>Data Types Stored:</u>

    User ID, name, contact details, interaction history, including reports submitted and notifications received.

3. **User Interface (UI) Design**: ...

4. **Integration and APIs**: ...

5. **Scalability and Performance**: ...

6. **Security and Privacy**: ...

7. **Error Handling and Resilience**: ...

8. **Deployment and DevOps**: ...

### **Week 2 questionnaire:**

1) **Tech Stack Resources:**

    At present, we do not utilize any project-based books. Instead, we rely extensively on the documentation and resources provided by the frameworks that we are employing.

2) **Mentorship Support:**

    Currently, we do not have a mentor involved in our project, as our idea is in the early stages of development. However, we are considering the option of hiring a mentor in the future to enhance our system and expand its scope beyond the student dormitory level. After implementing the minimum functionality of our project, we plan to seek feedback from the dormitory administration. This feedback will be invaluable, as it will allow us to effectively tailor the project to our target audience and facilitate its adoption by users.

3) **Exploring Alternative Resources:**

    We have explored various other resources to expand our understanding of the technology stack. These include online courses, video tutorials, and comprehensive documentation.

    The documentation acted as the definitive reference for syntax, features, and best practices, ensuring standards compliance, optimization of our implementations, and code cleanliness:
    - [Python Documentation](https://docs.python.org/3)
    - [StringBoot Documentation](https://docs.spring.io/spring-boot/index.html)
    - [MongoDB Documentation](https://www.mongodb.com/docs)
    - [PostgreSQL Documentation](https://www.postgresql.org/docs)

    The tutorials provided practical knowledge and examples to facilitate the implementation and debugging of our technology stack components:
    - [PostgreSQL Tutorial](https://www.postgresqltutorial.com)
    - [Docer Compose Tutorial](https://youtu.be/SXwC9fSwct8?si=IshiKzRXBZQfRABD)
    - [HTML & CSS Full Course](https://youtu.be/G3e-cpL7ofc?si=q3fhcyvZi7J7iAqL)

    By utilizing these diverse resources, we were able to deepen our understanding of our technology stack, overcome challenges, and ensure the robust development of MoniDorm.

4) **Identifying Knowledge Gaps:** ...

5) **Engaging with the Tech Community:**

    We frequently turn to online forums and groups, such as Stack Overflow, to ask and review questions related to Python, Docker, Spring Boot, and other components of our technology stack. Additionally, we use GitHub repositories to explore open-source projects, where we can find answers to our queries and extract practical information from code reviews and community feedback.

6) **Learning Objectives:** ...

7) **Sharing Knowledge with Peers:**

    As a team, we have established an effective information-sharing strategy. We use a Telegram chat divided into several sections (general, project reports, meeting organization, useful resources, daily reports). This structure facilitates easy access to necessary information, ensuring each team member quickly inform about project updates. Our communication extends beyond the digital space because we organize two meetings every week (one at the beginning and one near the end), where all team members participate. These meetings, conducted either offline or online, allow us to discuss achieved results and plan next steps. Additionally, team members working on the same component can arrange extra calls or meetings during the week as needed.

    We organize week-long sprints to enhance productivity, using GitHub issues to track tasks, assign responsibilities, and label components. To avoid last-minute rushes, we report daily on our progress to motivate each other and keep everyone informed about the project's status.

8) **Leveraging AI:**

    We sometimes use artificial intelligence-based tools, in particular ChatGPT, to accelerate knowledge acquisition and improve the development process. ChatGPT provides instant resolution of technical issues, helps us understand complex concepts, and supplements formal documentation with explanations. We also use AI-based code review tools to optimize performance and maintain high code quality. This AI integration has accelerated our learning, increased productivity, and enhanced the overall capabilities of our team, allowing us to solve problems more efficiently and stay up-to-date on the latest best practices.

### **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities                                                                                                                      |
|--------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Evgeny Bobkunov          | Project Management                          | Team management, [GitHub repository](https://github.com/IU-Capstone-Project-2024/MoniDorm) support, Issues creation and task tracking |
| Matvey Korinenko         | Team Lead, Fullstack                        | Creating a Telegram bot as a frontend interface for users, Development of the project architecture, Working with MongoDB database     |
| Artur Mukhutdinov        | Backend, Deputy Team Lead                   | Development of API and architecture, Working with PostgreSQL database                                                                 |
| Daniil Prostiruk         | Frontend                                    | Development of Telegram WebApp for the administration panel                                                                           |
| Rufina Gafiiatullina     | ML, DS                                      | Exploring the feasibility of applying LLM to the project, Development of a fault detection algorithm                                  |

### **Weekly Progress Report**

Our team did...

### **Challenges & Solutions**

...

### **Conclusions & Next Steps**

...