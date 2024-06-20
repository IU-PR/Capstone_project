---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

**Objective:**

Ensure high scalability, performance, ease of development, cost-effectiveness, and security.

**Criteria:**

- Compatibility with existing systems
- Community support and documentation
- Cost and licensing
- Security features
- Ease of integration
- Performance and scalability

**Final Selection:**

- **Backend:** FastAPI
  - *Reason:* High performance, easy to use, and modern Python integration.
- **Database ORM:** SQLAlchemy
  - *Reason:* Flexible, easy to use, integrates with FastAPI.
- **Database:** PostgreSQL
  - *Reason:* Robust, reliable, supports complex queries, open-source.
- **Caching:** Redis
  - *Reason:* High performance for caching and real-time analytics.
- **CI/CD:** GitHub Actions
  - *Reason:* Seamless GitHub integration, flexible workflows.
- **Frontend:** React
  - *Reason:* High performance, reusable components, large community support.
- **State Management:** Redux
  - *Reason:* Predictable state management, ease of debugging.
- **Language:** JavaScript (JS)
  - *Reason:* Ubiquitous in web development, extensive libraries and frameworks.

### **Architecture Design**

1. **Component Breakdown**:

- **Backend:** Handles API requests, business logic, and database interactions using FastAPI.
- **Database:** Stores all application data, managed with PostgreSQL.
- **Cache:** Implements Redis for caching frequently accessed data to improve performance.
- **Frontend:** Built with React, provides the user interface and interacts with backend APIs.
- **State Management:** Uses Redux to manage application state.
- **CI/CD:** Utilizes GitHub Actions for continuous integration and deployment.

2. **Data Management**:

- **Database Schema:** Designed using SQLAlchemy ORM, ensuring data integrity and efficient queries.
- **Data Storage:** PostgreSQL used for persistent data storage, Redis for temporary caching.
- **Data Flow:** Data flows between frontend and backend through RESTful APIs, with Redux managing state on the client side.

3. **User Interface (UI) Design**:

- **Responsive Design:** Ensures the application works well on both desktop and mobile devices.
- **Component-Based Architecture:** UI components are modular and reusable, built with React.
- **User Experience (UX):** Focused on ease of use, accessibility, and intuitive navigation.

4. **Integration and APIs**:

- **RESTful APIs:** Designed using FastAPI to handle CRUD operations and business logic.
- **External Services:** Integration with third-party services (e.g., payment gateways, mapping services) as needed.
- **API Documentation:** Automatically generated with FastAPI's built-in tools, ensuring clarity and ease of use for developers.


5. **Scalability and Performance**:

- **Load Balancing:** Implemented to distribute traffic evenly across multiple instances of the backend.
- **Caching Strategy:** Uses Redis to reduce load on the database and speed up response times.
- **Horizontal Scaling:** Plan to scale horizontally by adding more instances of the backend and frontend services.

6. **Security and Privacy**:

- **Authentication and Authorization:** Implemented using OAuth2 and JWT for secure access.
- **Data Encryption:** Ensures sensitive data is encrypted in transit and at rest.
- **Security Best Practices:** Follows OWASP guidelines to protect against common vulnerabilities.

7. **Error Handling and Resilience**:

- **Error Logging:** Centralized logging to track and debug errors efficiently.
- **Graceful Degradation:** Ensures the application continues to function at a basic level even if some services fail.
- **Automated Recovery:** Implements automated scripts to restart services in case of failure.

8. **Deployment and DevOps**:

- **Continuous Integration:** Uses GitHub Actions for automated testing and integration.
- **Continuous Deployment:** Automates deployment processes to ensure quick and reliable releases.
- **Infrastructure as Code:** Manages infrastructure using tools like Terraform or Ansible for consistency and scalability.

## **User Journey**

<div style="text-align: center;">
<img src="/2024/kuda_team/week2/UserRoad.png" width="600" height="300"> 
</div>

## **Database Design**:
<div style="text-align: center;">
<img src="/2024/kuda_team/week2/DBdesign.png" width="600" height="300"> 
</div>

### **Week 2 questionnaire:**

1) Tech Stack Resources:
While we did not use any specific tech stack resources, we relied on internet resources such as documentation, tutorials, and forums.

2) Mentorship Support:
Our project is still in its early stages and doesn't have a mentor yet. While we understand the benefits of having one, our team's diverse backgrounds and experience with various technologies are helping us navigate effectively for now. We're open to seeking mentorship as we progress, especially during challenging phases, to benefit from expert guidance.

3) Exploring Alternative Resources:
To better understand working with React and JavaScript, we often refer to the official documentation on https://react.dev. It provides detailed guides, examples, and updates on the latest versions of React. In addition to this, we also use tutorials and guides from Yandex.

4) Identifying Knowledge Gaps:
In frontend development, we are encountering specific challenges with using React due to our team's limited level of knowledge and experience with this framework.

5) Engaging with the Tech Community:
We engage with the broader technical community through platforms such as Stack Overflow and Habr. These forums enable us to study the experiences and solutions to complex problems shared by other participants.

6) Learning Objectives:
We have set a goal to improve our skills in React and JavaScript. Our objective is to master key concepts and actively apply new knowledge in our current project. We plan to deepen our understanding through systematic study of official documentation and guides.

7) Sharing Knowledge with Peers:
Regularly, our team gathers for meetings to discuss current tasks, share completed work, and address any issues that arise. We also exchange new techniques and tools that we find beneficial for the entire group. Additionally, we've created a Telegram group for communication and scheduling meetings as needed.

8) Leveraging AI:
We use OpenAI's ChatGPT to solve technical issues in the project and to explore new information needed for coding.

### **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
| Dmitry Zvidrin (Lead)      | Backend | Team lead, backend development, assists with reports |
| Danila Tretyakov             | Backend | Main backend developer, architecture design |
| Anton Fadeenkov             | Design/Frontend | Application design, frontend development |
| Kseniia Voronova             | Frontend | Frontend development, assists with reports |
| Yassine Allala             | Frontend | Frontend development, mobile version of the application |


### **Weekly Progress Report**

Our team made progress this week:

We initiated the design process for our project, focusing on the logo and overall visual appearance.
A database design was completed, laying the foundation for our application's data management.
Backend development commenced with the creation of an authentication service.
To streamline our workflow, we developed a user story and backlog. This helped us prioritize features and determine the starting point for our work.

### **Challenges & Solutions**

During the week, we encountered a few challenges:

1. **Design Consensus:** Achieving consensus on the design direction for our project, particularly regarding the logo and overall visual appearance, proved challenging due to differing opinions within the team. To address this, we held brainstorming sessions and conducted polls to gather feedback from team members, ultimately leading to a design that satisfied everyone.

2. **Database Complexity:** Designing the database structure for our application posed a challenge, especially in determining the optimal schema to support our features while ensuring scalability and efficiency.

### **Conclusions & Next Steps**

In conclusion, despite encountering challenges, our team successfully initiated the design process, completed the database design, and commenced backend development. Looking ahead, our next steps include:

- **Design Refinement:** Continuing to refine the design of our project, incorporating feedback from stakeholders and ensuring consistency across all visual elements.
- **Database Implementation:** Proceeding with the implementation of the database design, focusing on creating efficient queries and ensuring data integrity.
- **Backend Development:** Continuing to develop the backend, with a focus on implementing additional services and features to support our application's functionality.
- **User Story Refinement:** Refining our user story and backlog based on ongoing feedback and insights gained during the development process.
- **Testing and Feedback:** Conducting thorough testing of each component to identify and resolve any issues, and gathering feedback from users to iteratively improve the application.

Overall, we are pleased with the progress made this week and are excited about the upcoming stages of our project.
