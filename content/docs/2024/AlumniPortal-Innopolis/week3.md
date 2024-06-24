---
title: "Week #3"
---

# Week 3 Report

This week's progress report outlines significant developments and strategic adjustments as we advance towards our project goals.

## Prototype Features *Developed*:
*Currently we have ~1000 lines of functional code written in go in the backend part, web-design and around 150-200 of YAML/Dockerfile configuration lines*
- **Additional Requests Service:** Implemented RESTful API endpoints for managing additional requests with full CRUD functionality.
- **Auth Service:** Finalized user authentication features including signup, login, and token validation, supported by robust middleware for role-based access control.
- **Community & Donation & Event/Project Services:** Started development of these services. After finalizing, MVP core functionality on the back-end part will be finalized.
- **AI Integration:** Started implementation of the AI-based service for spam filtering and user recommendations.
- **Backend Environment (Monitoring and Logging)** Almost finalized: implemented ELK Stack for gathering logs across microservices. At the moment we are configuring Prometheus & Grafana for metrics monitoring.

## Prototype Features *to be developed:*
*The plan of features development remains the same as for week #1 and week #2. Further changes are possible only due to the lack of time*

## User Interface:
We have finished the web design phase, establishing key screens and interactions essential for the frontend development phase.

## Challenges and Solutions:
Throughout our project journey, we encountered several significant challenges, notably:

- **AI Model Implementation:** Integrating AI for spam filtering and recommendation services.
- **Microservices Architecture:** Developing a microservices architecture following best practices.
- **Backend Environment Optimization:** Creating an optimal backend environment for logging, monitoring, and metrics collection.

We successfully found solutions for the latter two challenges by studying numerous implementation examples and seeking guidance from domain experts. This enabled us to commence the development of a robust backend infrastructure effectively.

However, in the realm of artificial intelligence, our exploration continues. We remain dedicated to unraveling answers to our questions and enhancing our skills. We aim to achieve our objectives in the coming week by further deepening our understanding and practical application in this critical area.

## Next Steps:
1. **Frontend Development:** Initiate frontend development based on finalized web designs, focusing on seamless integration with backend APIs.
2. **Testing and Validation:** Conduct comprehensive testing to ensure backend and frontend functionalities meet design specifications and usability standards. Write unit tests to cover potential bugs and enhance code reliability.
3. **Documentation and Collaboration:** Enhance API documentation using tools like Postman, promoting clarity and facilitating seamless collaboration across teams.
4. **Security Enhancements:** Implement additional security measures such as request validation and HTTPS enforcement to fortify application integrity and user data protection.
5. **AI Implementation:** Continue the development and integration of AI-based services for spam filtering and user recommendations, aiming to refine and optimize their performance.
6. **Monitoring Configuration:** Finalize the configuration of monitoring tools like Prometheus and Grafana for metrics collection and visualization, ensuring robust logging and system monitoring.
7. **Core Functionalities:** Continue development of Community, Donation, and Event/Project services. Finalize these core functionalities to complete the MVP back-end part.

# Additional Sections

## Tasks distribution & Management
Our team has chosen Trello as a platform for task management. Currently we have descriptive tasks we are working on and at any time can see the progress of each other.
![Trello - Kanban board](/2024/AlumniPortal-Innopolis/TrelloBoardw3.png)

## Backend development progress
*Can be found here: [Backend branch](https://github.com/IU-Capstone-Project-2024/AlumniPortal-Innopolis/tree/backend_services)*

## Completed Web Design
*Can be found here: [Figma Link](https://www.figma.com/design/SfF0bsqgwOKq8h1XcPZ87I/Untitled?node-id=0-1&t=1AkJuqLnqNlBNXH5-0)*

## Feedback (core aspects) received from 319 Office

- The idea of supporting events is promising, but a crucial question remains: will graduates donate and sustain these initiatives? Success hinges on motivating them effectively.

- Graduates cannot request passes even for the duration of events, per Semenikhin's decision. Their only option is to obtain a university pass. Additionally, no one will be housed in dormitories for free during events unless the graduate rents a room themselves.

- Sponsoring events with not just money, but also with services or products, is our top idea and potentially more effective.

- We are currently developing a news channel for graduates, which aligns well with promoting donations and contributions.

- One graduate manages a scholarship and contributes significantly to the university. However, scholarships are a separate project, and for the MVP, a detailed functional description should suffice.

- Supporting student startups could be challenging to organize effectively due to existing structures like the Startup Studio. Establishing partnerships requires substantial documentary groundwork. However, structuring this as donations should alleviate concerns.

- How can graduates be assured their donations support real projects and not just empty promises? (This question has been resolved.)

- There's a hiring question: while hiring from 1st and 2nd years is straightforward, 3rd and 4th years have their own internships. It might be more effective to focus on delegating tasks rather than direct hiring. For instance, a graduate's company needing a website could delegate the task to students.

- It's commendable that your portal emphasizes careers, events, and idea implementation. Such a service is much needed.