---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

During the second week of the NeuroCoach project, the team focused on transitioning from idea validation to actual implementation, with a strong emphasis on technical preparation and detailed requirement specification. The main goal was to lay a solid architectural and functional foundation for all components of the system: backend, frontend, mobile application, databases, and AI integration.

One of the key tasks was the start of backend infrastructure development, including the implementation of an authentication system and data validation. This was essential for ensuring security, managing user access, and personalizing content. It was important to introduce the REST API early to establish communication between different parts of the application and create a base for future integrations.

Another important task was the design and setup of the database layer. Work began with PostgreSQL as the primary storage for structured data — such as user profiles, workout plans, and progress metrics. At the same time, MongoDB was integrated to store unstructured data like chat history with the AI coach. This separation allowed the team to build a flexible and scalable data storage system.

The development of the client side — both the mobile app and the web interface — also started during this week. At this stage, the basic structure and navigation were defined, allowing the team to outline the user journey from login to completing the first workout. It was also important to test how the frontend would communicate with the backend to ensure correct data transfer.

A significant amount of work was dedicated to UX/UI design, as usability and visual appeal play a crucial role in user retention. The design needed to be not only visually attractive but also intuitive, especially for fitness beginners. A landing page was also created, which could later be used for marketing and collecting early registrations.

User research continued throughout the week, helping the team better understand the real needs of the target audience. Additional interviews provided valuable insights that helped refine the product direction and ensure that development aligned with actual user expectations. A business model and unit economics framework were also developed to help the team understand how the product could grow and generate revenue in the long term.

Task management and team coordination reached a new level — the use of Kanban made the process more transparent and organized, while task distribution ensured clarity and accountability.

In summary, the tasks of the second week were aimed at starting full-scale development, forming the internal structure of the product, and conducting deeper user research. These actions represented a natural progression from the first week, when the idea and problem were validated, and allowed the team to move toward building a working prototype.


### Prioritized backlog

We introduced the Kanban system to manage tasks and improve coordination within the NeuroCoach team. This method has been especially helpful during the early stages of development, allowing us to clearly organize work, track progress, and adapt quickly to changes.

Tasks were divided into four main categories: To Do , In Progress , Done , and Completed . This helped the team visualize the status of each task and understand dependencies between different parts of the project. We used the Kanban board to plan weekly goals, prioritize tasks, and ensure smooth collaboration between backend, frontend, mobile development, and research activities.

Kanban improved our ability to manage workload, identify bottlenecks, and maintain a steady flow of progress. It also made it easier for mentors and instructors to review our progress and provide timely feedback. Overall, using Kanban helped us stay organized, focused, and aligned throughout the project.

Our Kanban can be found at this link: https://markpetrov2015.aspro.cloud/_module/st/view/project/21?tab=project_tasks.board, but you will need to register. Therefore, attaching screenshots of the board at this link: https://docs.google.com/document/d/1bwesTSD9BgaIw2RDh2v8X8Q5hdqjhzYbMoSn7tBjCAA/edit?usp=sharing.

## Project specific progress

### Backend

During the second week, significant progress was made in backend development, establishing a strong foundation for the entire NeuroCoach system. The team implemented a complete authentication and authorization system, including user registration, login via email/password, and route protection using JWT tokens. This ensures secure access to personalized data such as workout history and chat logs with the AI coach.

A validation layer was also introduced to ensure that all incoming data meets required formats and constraints. This includes checks for valid emails, password strength, and structured inputs for user profiles and workouts. In parallel, both PostgreSQL and MongoDB were integrated — the former for structured data like user profiles and workout plans, and the latter for unstructured data such as chat history. Migrations, data models, and initial REST API routes were created to support communication between frontend, mobile, and backend components. Docker was introduced to containerize the service, simplifying deployment and ensuring consistency across development environments.



### Frontend

Frontend development focused on building the core structure of the web interface and integrating it with the backend. Key screens such as profile and progress tracking were started, forming the basis for future feature expansion. A major milestone was connecting these components to the backend API, enabling real-time data exchange and testing of live interactions.

The team also began developing an analytics dashboard where users will be able to visually track their performance over time. The design followed a unified system aligned with the mobile version, ensuring a consistent experience across platforms. These efforts laid the groundwork for a fully functional and responsive web application that will serve both individual users and B2B clients.



### DevOps

DevOps work centered around containerizing the backend using Docker, allowing for isolated environments and smoother deployment. A docker-compose configuration was set up to manage multiple services — backend, PostgreSQL, and MongoDB — together, making local development and testing more efficient.

In addition, initial steps were taken toward setting up CI/CD pipelines using GitHub Actions. This will automate testing and deployment processes, improving code quality and speeding up development cycles. These measures ensured that the infrastructure is scalable, maintainable, and ready for continuous integration moving forward.



### Manager

Project management during this week involved task planning, sprint organization, and market research. Tasks were managed using a Kanban board to improve transparency and coordination within the team. The manager also oversaw sprint execution and facilitated communication between developers, designers, and researchers.

A business model and unit economics framework were developed to better understand how the product can scale and generate revenue. Additionally, 7 customer discovery interviews (custdevs) and 3 problem interviews were conducted to gather insights into user expectations and validate the relevance of key features. These findings helped refine the product roadmap and ensure that development remains user-focused.



### Product Designer

The product designer finalized the UI/UX for both mobile and web applications, focusing on simplicity, accessibility, and user engagement. Final screen designs were completed for home, profile, workout, progress, and chat pages. A consistent visual language was maintained throughout, including color schemes, typography, and iconography, creating a cohesive look and feel.

A landing page was also designed to support marketing efforts and collect early registrations. Additionally, a prototype of the user journey from first launch to completing a workout was built, helping identify potential friction points and improve navigation flow. This work ensured that the design supports both functionality and emotional connection with the user.



### Public Relations & Customer Development

This week included conducting 7 new customer discovery interviews (custdevs) and 3 problem interviews to gain deeper insight into user needs and validate the relevance of NeuroCoach. The goal was to assess whether the product idea resonates with real users and which features are most valued. Respondents emphasized the importance of personalization, real-time feedback, and flexible workout plans.

These insights have already begun influencing task prioritization. For example, users showed high interest in saving chat history with the AI coach and receiving recommendations based on their progress. Data on willingness to pay was also collected, which will help shape the pricing strategy. This ongoing research ensures that the team remains confident that NeuroCoach addresses real user problems and aligns with market expectations.



# Weekly commitments

## Individual contribution of each participant

Mariia Nikolashina

As the technical lead for the backend development of the NeuroCoach application, Mariia Nikolashina was fully responsible for the system architecture and the execution of backend components. She designed and implemented a robust microservice-based architecture, selecting key communication patterns between services to ensure fault tolerance and scalability under high load. This architectural foundation enabled seamless integration with both frontend and mobile clients. She defined the RESTful API format, prepared comprehensive API documentation in both OpenAPI and Markdown formats, and organized backend-frontend synchronization meetings, ensuring technical alignment across teams and facilitating efficient development. To ensure secure and stable user interaction, she implemented JWT-based authorization and authentication, including a custom middleware layer that authenticated every request and validated incoming data, significantly improving the security, stability, and data integrity of the platform. On the data layer, she led the selection and integration of PostgreSQL, developed the initial ORM models and service layer for database interactions. She also participated in discussions regarding the use of MongoDB for non-relational storage scenarios. Mariia personally developed the core functional modules, including:
User authentication
User management (Store personal information and account data)
Workout plan generation, with logic to interface with AI modules (mocked initially for integration testing)
To streamline development and improve team productivity, she authored the Makefile and development configuration files, ensuring a consistent environment for local development and easier onboarding for other developers. She also implemented a mock communication layer with a Large Language Model (LLM) to support early-stage testing of AI-assisted workflows. Beyond technical contributions, Mariia conducted two customer discovery (custdev) interviews, which provided valuable insights into user needs and helped shape feature prioritization in the MVP. Finally, she facilitated regular developer synchronization meetings, coordinating the efforts of backend, frontend, and mobile teams to ensure smooth integration and timely delivery of the product.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/13
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/issues/2
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/10
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/14
-  https://docs.google.com/document/d/1fNs-UU7we4hzzBqaJmHwYyxyYvC80TCqdgGRMmIbye4/edit?usp=sharing

Mark Petrov
Mark acted as the Product Owner and team coordinator. He organized weekly meetings, planned sprints, and set clear goals for the upcoming stages of product development. As part of the market research efforts, he conducted 1 customer discovery interview (custdev) to validate user needs and refine the product vision. Mark was heavily involved in shaping the business model for NeuroCoach, laying the groundwork for future commercialization. He also began calculating the unit economics to understand how the product can scale sustainably and generate revenue. His strategic input helped align technical development with long-term business goals.
- https://docs.google.com/document/d/1B6ePdvTPKXFGY3r8kPvBhdKi1BiaincWDDckN9KjLpQ/edit?usp=sharing
- https://docs.google.com/document/d/1U45ZUr8eIht06DCMukE6KzfstyqCfn7yFkJ37tqbhls/edit?usp=sharing
- https://docs.google.com/document/d/1fNs-UU7we4hzzBqaJmHwYyxyYvC80TCqdgGRMmIbye4/edit?usp=sharing

Maxim Oleynik
Maxim worked on designing the structure of the databases that will power NeuroCoach. He analyzed data flows across the system and created logical models for both relational (PostgreSQL) and non-relational (MongoDB) storage. He mapped out how user profiles, workout plans, progress logs, chat interactions with the AI coach, and feedback would be stored and retrieved. Maxim also defined relationships between entities, normalized tables where necessary, and optimized schemas for scalability and performance. His work laid the foundation for efficient data handling across all parts of the application. In addition, he conducted 3 problem interviews and 4 customer discovery interviews (custdevs), which provided valuable insights into user pain points and helped shape the direction of the product. Maxim set up and enforced the repository's branching strategy, including rules for pull requests, code reviews, and CI/CD integration, ensuring a clean, maintainable, and collaborative development workflow.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/commit/029cf770d87316995dc426193830971a121f0d43
- https://docs.google.com/document/d/1fNs-UU7we4hzzBqaJmHwYyxyYvC80TCqdgGRMmIbye4/edit?usp=sharing

Danil Fishchenko
Daniil worked on the design of the user interface and overall UX/UI for both the mobile app and web version of the service. He designed screens for the home page, user profile, workouts, progress tracking, and gamification features. Daniil created prototypes of all key modules and coordinated them with the team before development began. His design focuses on simplicity, engagement, and intuitive navigation — especially important for fitness newcomers. He also participated in discussions about color schemes, typography, and animations to be used in the app.
- https://www.figma.com/design/ggsx8HjvuNhfUltSbONPfu/Untitled?node-id=0-1&t=CN432rmJ0ESmdEj7-1

Klimentii Chistyakov
Klim worked on the architecture of the Flutter-based mobile app. He designed the project structure, implemented basic architectural patterns (MVVM and Bloc), configured routing, and started building screen logic. Klim also initiated the integration of the mobile client with backend services to enable data exchange related to users, workouts, and progress tracking. He actively tested the app’s performance and is already working on making the interface as responsive and device-adaptive as possible.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/16

Saidaziz Kadirov
Said focused on the frontend architecture of the web version of NeuroCoach. He designed the structure, selected necessary libraries, and started coding the main pages: profile, workouts, and progress dashboard. He collaborated closely with Daniil to maintain a consistent design system across both mobile and web platforms. Said also built initial components for displaying user progress and configured communication between the frontend and backend via REST API. His goal is to make the web interface user-friendly for regular users and scalable for potential B2B clients like fitness clubs.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/17

## Plan for Next Week

During the upcoming week, the NeuroCoach team will focus on actively developing and integrating core features of the product. The main goal is to move from initial development to a more complete prototype that can be tested internally.

A key priority will be the continued work on the backend to ensure stable communication between components, as well as the first steps in integrating artificial intelligence to support users in real time. This will allow us to begin testing the concept of having an AI coach available 24/7.

The mobile app and web interface will also be improved to better display user data and enhance the overall experience. Special attention will be given to making the workout experience more engaging through gamification and personalized training plans. These improvements are aimed at increasing user motivation and long-term engagement.

In addition, this week marks the beginning of internal testing, which will help identify any issues early and improve the overall performance of the system. We will also start preparing for the product presentation and gathering feedback from real users, which will guide our next steps and confirm that NeuroCoach addresses actual user needs effectively.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
