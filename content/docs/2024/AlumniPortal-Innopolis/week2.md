---
title: "Week #2"
---

# Week 2 Report

## Tech Stack Selection

### Tech Stack Overview
*It is essential to highlight that Tech Stack Overview was taken from 1st week and rewrited with some changes. Some parts (like Envoy usage) remained the same.*

Our project aims to create a comprehensive alumni portal for Innopolis University, enhancing connectivity and collaboration between alumni, students, and the university. After evaluating scalability, performance, security, and development efficiency, we have selected the following tech stack:

- **Front-end**: HTML5, CSS3, JavaScript, Vue 3
   - *Vite*: Front-end build tool that offers fast development server and optimized builds, improving development workflow.
   - *Vuetify*: UI library that provides ready-to-use, aesthetically pleasing components for rapid development.
   - *Pinia*: State management library that is intuitive and integrates seamlessly with Vue 3.
   - *Axios*: Promise-based HTTP client for making API requests, simplifying data fetching and error handling.
   - *Vue Router*: Official Vue 3 router for managing navigation and creating a multi-page application experience.
   - *Jest*: JavaScript testing framework that facilitates unit testing, ensuring code reliability and catching bugs early.
- **Back-end**: Go, Python
  - *Redis*: In-memory data structure store used for caching and session management, providing fast data retrieval.
  - *GORM*: Go Object-Relational Mapping (ORM) library for simplifying database interactions with PostgreSQL, facilitating data modeling and query execution.
  - *gin*: Web framework for Go that offers a fast HTTP router and middleware support, enabling rapid development of RESTful APIs and web services.
  - *gRPC*: Remote Procedure Call (RPC) framework for efficient communication between microservices, using protocol buffers for serialization and providing low-latency, high-throughput interactions.
  - *Aiogram + Pyrogram*: Asyncio-based libraries for building Telegram bots in Python, simplifying bot development with intuitive API wrappers and event handling.
- **Database**: PostgreSQL (+Redis)
- **AI Integration**: Python (+TensorFlow)
- **Proxy**: Envoy for gRPC integration

### Justification for Tech Stack Components

- **Front-end (HTML5, CSS3, JavaScript, Vue 3)**:
  - *Suitability*: Vue.js offers simplicity, scalability, and efficient development of interactive user interfaces.
  - *Team Expertise*: One team members have commercial experience with Vue 3, ensuring a smooth development process and making possible taking the lead of the Front-end team.

- **Back-end (Go, Redis, GORM, gin, Python (Aiogram + Pyrogram))**:
  - *Suitability*: Go is chosen for its exceptional performance and strong concurrency capabilities, making it well-suited for developing scalable back-end services that can handle concurrent user requests efficiently. Redis serves as an in-memory data store, optimizing data retrieval speed and supporting caching mechanisms crucial for enhancing application performance. GORM (Go Object-Relational Mapping) streamlines database interactions by abstracting SQL queries, facilitating efficient data modeling and management within PostgreSQL. The gin web framework complements Go by providing a lightweight and flexible HTTP router with robust middleware support, enabling rapid development of RESTful APIs and web applications.
  - *Team Expertise*: The team possesses solid foundational knowledge in Go programming and back-end development, supported by practical experience in commercial projects involving Go. This expertise includes leveraging Redis for caching strategies and optimizing database operations with GORM. Additionally, the team is proficient in using Python's Aiogram library for asynchronous Telegram bot development, enhancing their versatility in implementing interactive chatbot functionalities.

- **Database (PostgreSQL, Redis)**:
  - *Suitability*: PostgreSQL is reliable, scalable, and suitable for structured data storage. Redis supports caching and session management.
  - *Team Expertise*: The team has experience with PostgreSQL from prior coursework.

- **AI Integration (Python, TensorFlow)**:
  - *Suitability*: Python and TensorFlow are widely used for machine learning and AI applications, making them suitable for implementing recommendation systems and spam filtering.
  - *Team Expertise*: All team members have some experience in machine learning and TensorFlow from the ML course.

- **Proxy (Envoy for gRPC integration)**:
  - *Suitability*: Envoy is a high-performance proxy suitable for handling gRPC communication between microservices, supporting scalable and efficient architecture.
  - *Team Expertise*: While Envoy may require some learning, its use aligns with modern microservices architecture principles, and the team is prepared to leverage its features.

### Knowledge Gaps and Mitigation:

- **Front-end**: Vue 3 basics will be reinforced by the front-end developers via the knowledge and mentorship of the expertised team member.
- **Back-end**: Go advanced topics related to the back-end development and gRPC will be reinforced using official documentation.
- **AI Integration**: TensorFlow advanced features and practical applications will be learned through "Hands-On Machine Learning."
- **University API Integration**: After receiving necessary documentation, our team will start to analyze and learn it.

## Architecture Design

### Component Breakdown

- **Front-end**: Responsible for user interface and experience, developed using Vue 3.
- **Back-end**: Manages business logic and data processing, built with Go.
- **Database**: Stores user information and project details, using PostgreSQL and Redis.
- **AI Integration**: Implements recommendation systems and spam filtering, using Python and TensorFlow.
- **Proxy**: Handles communication between microservices, using Envoy for gRPC.

*More descriptive and fulfilling component breakdown can be found in Diagrams section*

### Data Management

- **Structured Data Storage**: We will use PostgreSQL to store structured data such as user profiles, project details, and event information. PostgreSQL is chosen for its robustness, support for complex queries, and ACID compliance, ensuring data integrity and reliability.
- **Caching**: Redis will be used to cache frequently accessed data, such as user sessions and recently accessed project details. This will significantly reduce the load on the PostgreSQL database, leading to faster data retrieval and improved application performance.
- **Database Interactions**: GORM, a powerful ORM library for Go, will be employed to facilitate database interactions. GORM will simplify the process of querying, inserting, updating, and deleting records in PostgreSQL, allowing developers to work with high-level data models instead of raw SQL queries.

### User Interface (UI) Design

- **Principles**: The UI will be crafted with a strong focus on user experience (UX) principles, ensuring the interface is intuitive, user-friendly, and visually appealing. 
- **Framework**: Vue 3 will be utilized to build the UI, offering a reactive and component-based structure that supports creating dynamic and responsive interfaces.
- **Visualization**: Wireframes and mockups will be created using Figma to visualize the layout, flow, and functionality of the application. These visual tools will help in planning and iterating on the UI design before implementation that will be started in the second half of the next week.

### Integration and APIs

- **System Integration**: Our application will integrate with the university's existing systems to enable user verification and manage events seamlessly. This ensures that the platform can leverage current data and authentication mechanisms, providing a cohesive user experience.
- **Microservices Communication**: gRPC will be used for communication between microservices. This protocol is chosen for its performance benefits, such as low latency and efficient binary serialization, which are crucial for a responsive and scalable application.
- **Authentication and Single-sign on (SSO) services**: Utilizing authentication services such as JWT or OAuth / OpenID Connect can simplify user registration and login by enabling users to authenticate with their existing accounts from platforms like Google.
- **Payment Gateway Integration**: Integrating with a popular payment gateway that supports Russian payments, such as Yandex.Checkout or Sberbank Online, will allow users to make secure online donations using various methods like credit cards, digital wallets, or bank transfers.
- **Telegram API**: To automate the creation of channels for every project posted on the Alumni portal and send automatic messages for updates, we will integrate with the Telegram API using Python frameworks like Aiogram and pyrogram. Telegram offers robust APIs that allow us to programmatically interact with Telegram channels and send messages.

### Scalability and Performance

- **Architecture Design**: The architecture is meticulously designed to accommodate increasing user loads and data volumes. This includes load balancing, database optimization, and efficient data caching strategies.
- **Performance**: By leveraging Go's high performance and concurrency capabilities along with Envoy's efficient handling of gRPC communications, we ensure that the system remains responsive and scalable as usage grows.

### Security and Privacy

- **Security Measures**: Comprehensive security measures will be implemented, including robust authentication and authorization protocols to control access to the platform. Data encryption will be used to protect sensitive information both in transit and at rest.
- **Best Practices**: We will adhere to industry best practices for secure data handling and storage, such as using secure coding standards, regular security audits, and applying patches and updates promptly.
- **Donation Security**: The team will utilize secure donation gateways, adhere to PCI DSS compliance standards, and ensure no sensitive payment data is stored.
- **Privacy Compliance**: Our product will ensure adherence to privacy regulations, obtain user consent, and provide mechanisms for users to manage their personal data.

### Error Handling and Resilience

- **Error Management**: Strategies for effective error logging and monitoring will be put in place to quickly identify and address issues. This includes setting up alerting mechanisms to notify the team of any critical errors. The system will have a centralized error logging and monitoring mechanism to track and manage errors across the microservices.
- **Resilience**: We will ensure the application's resilience through robust error handling mechanisms, allowing the system to recover gracefully from unexpected failures and continue operating smoothly.

### Deployment and DevOps

- **Automation**: Deployment tasks will be automated to streamline the process and reduce the risk of human error. This includes automated builds, testing, and deployment pipelines.
- **Development Workflow**: A robust development workflow is already established, incorporating version control via git (using trunk-based git workflow) and task management via trello. CI/CD will be established later, during the week 3. This ensures that new features and updates can be delivered quickly and reliably.

*Detailed Deployment strategy may be found further*


## Week 2 Questionnaire

### Tech Stack Resources

Our team leverages a combination of official documentation, online resources, and industry-related articles to enhance our knowledge and expertise in our tech stack. While we do not currently rely on project-based books specifically, we have identified several key resources that we anticipate will be instrumental in our development process.

#### Official Documentation
- **Go Programming Language**: We extensively use the [official Go documentation](https://golang.org/doc/) to understand best practices, language features, and standard libraries.
- **Vue.js**: The [Vue.js official guide](https://vuejs.org/v3/guide/) is our primary resource for developing user interfaces, ensuring we follow the latest conventions and patterns.
- **PostgreSQL**: The [PostgreSQL documentation](https://www.postgresql.org/docs/) helps us manage our database interactions efficiently and securely.

#### Online Resources and Articles
- **Medium and Dev.to Articles**: We frequently consult articles on Medium and Dev.to for real-world examples, tutorials, and best practices related to our tech stack. These platforms provide insights from industry professionals and help us stay updated with the latest trends and techniques.
- **Community Forums and Discussions**: Platforms like Stack Overflow and Reddit are invaluable for troubleshooting and learning from the experiences of other developers in the community.

#### Anticipated Books
Although we primarily rely on the aforementioned resources, we are considering incorporating the following books to further enhance our understanding:

1. **"Learning Go: An Idiomatic Approach to Real-World Go Programming" by Jon Bodner**: This book provides practical examples and idiomatic approaches to Go programming, which will help us write cleaner and more efficient code.
2. **"PostgreSQL: Up and Running" by Regina O. Obe and Leo S. Hsu**: This book covers PostgreSQL essentials and advanced features, assisting us in optimizing our database management and performance.
3. **"Building Microservices" by Sam Newman**: This book can help us to deep into the designing and implementing microservice architecture.

#### Utilization of These Materials
We anticipate utilizing these materials in the following ways:

- **Structured Learning**: Books and official documentation provide a structured approach to learning, ensuring that we cover all fundamental and advanced aspects of our tech stack systematically.
- **Real-World Examples**: Project-based books and online articles offer practical examples and case studies, helping us understand how to apply theoretical knowledge to real-world scenarios.
- **Continuous Improvement**: By regularly consulting these resources, we can continuously improve our skills, stay updated with the latest developments, and implement best practices in our projects.

In summary, while we predominantly rely on official documentation and online resources, we recognize the value of project-based books and anticipate incorporating them into our learning regimen to enhance our technical expertise and project outcomes.

### Mentorship Support

Currently, we do not have a mentor actively involved in our project. Instead of seeking a traditional mentor, we are focusing on engaging a project customer from the 319 Department of the university. This approach will provide us with a unique perspective and valuable insights directly from an invested stakeholder.

#### Why a Project Customer from the 319 Department?

1. **Domain Expertise**: A project customer from the 319 Department will possess deep knowledge of the university`s operations, challenges, and objectives related to the given problem and our solution. Their expertise will help us align our project with the specific needs and goals of the department and university.
2. **Stakeholder Feedback**: Having a project customer involved ensures that we receive continuous feedback from the primary stakeholders, allowing us to make informed decisions and adjustments throughout the development process.
3. **Enhanced Relevance**: Direct involvement from a project customer will help us create a solution that is highly relevant and beneficial, increasing the likelihood of successful adoption and implementation.

We believe that having a project customer will significantly contribute to the success of our project by providing us with practical, real-world insights and ensuring that our solution meets the needs of its intended users.

### Exploring Alternative Resources

*We have already mentioned some of the alternative resources answering the first question, there are some additions*

- **Online Courses**:
  - Vue Mastery (Vue 3 course)
  - Udemy (Backend Master Class)
  - Coursera (TensorFlow: Advanced techniques Specialization)

### Identifying Knowledge Gaps

Our team has identified two primary knowledge gaps within our tech stack: AI (specifically in spam filtering and recommendation system building) and generally building a microservice architecture.

#### Tech Stack Division

1. **AI Development**
   - **Current Gap**: Our team needs more expertise in implementing spam filtering and building effective recommendation systems.
   - **Plan to Address**:
     - **Online Courses and Workshops**: Enroll in specialized courses on platforms like Coursera and Udacity that focus on spam filtering algorithms and recommendation systems.
     - **Official Documentation and Case Studies**: Study the latest documentation and case studies from industry leaders like Google AI and OpenAI.
     - **Collaborative Learning**: Organize weekly study groups to discuss and implement AI algorithms, leveraging tutorials and articles from Medium and other tech blogs.

2. **Microservice Architecture**
   - **Current Gap**: Our team needs a deeper understanding of designing and implementing microservice architectures.
   - **Plan to Address**:
     - **Project-Based Books**: Utilize books like "Building Microservices" by Sam Newman, "Microservices Patterns" by Chris Richardson, and "Designing Data-Intensive Applications" by Martin Kleppmann to gain theoretical and practical knowledge.
     - **Online Resources**: Follow tutorials and courses on platforms like Pluralsight and LinkedIn Learning that cover Docker Swarm and microservice best practices.
     - **Practice and Implementation**: Conduct experiments within our development environment to apply learned concepts and refine our microservice architecture skills.

By systematically addressing these gaps through targeted learning and practical application, we aim to build a well-rounded understanding of our chosen technologies, ensuring the success and robustness of our project.

### Engaging with the Tech Community

Yes, our team tries to actively engages with the broader tech community to seek guidance and learn from experienced professionals in our tech stack. This engagement is crucial for addressing our knowledge gaps and ensuring we stay updated with the latest industry practices.

#### Online Forums and Groups

- **Stack Overflow and GitHub**: We regularly consult and contribute to Stack Overflow and GitHub repositories. These platforms provide a wealth of information, including solutions to common problems, code examples, and best practices shared by the global developer community.

#### Engaging Experts through Professional Networks

- **LinkedIn and Professional Networks**: We leverage LinkedIn and other professional networks to connect with experts in AI and microservice architecture. By following thought leaders and joining relevant groups, we can directly reach out to professionals for advice on critical tech stack problems.

By actively participating in these communities and utilizing our professional networks, we ensure continuous learning and access to expert guidance, which is vital for overcoming our knowledge gaps and successfully implementing our project.

### Learning Objectives

- **Front-end**: Deepen Vue 3 skills
- **Back-end**: Master Go and gRPC integration
- **Database**: Optimize PostgreSQL usage and Database load 
- **AI Integration**: Try to Implement recommendation system related to our project

  Strategies include regular study sessions, project-based learning, and knowledge sharing.

### Sharing Knowledge with Peers

- We have organized two knowledge-sharing sessions between 3 groups of developers: for backend, frontend and UI/UX (Design) team.
- During the week we were discussing our gaps and ways to resolve the problems that may occur during the further development almost each day.

### Leveraging AI

- We were utilizing AI-powered tools like GitHub Copilot to expedite the learning process and practicing in code development.
- ChatGPT and other NLP tools were used to optimize the path related improving our practical skills.

## Tech Stack and Team Allocation

Here’s a detailed explanation of how our project is structured, including the specific technologies and corresponding team members responsible for each component:

1. **Front-end Team**:
   - **Technologies**: HTML5, CSS3, JavaScript, Vue 3
   - **Team Members**: 2 developers: *Stepan Leonov (Front-end Team Lead)* and *Ekaterina Zaitseva*
   - **Responsibilities**:
     - Develop the user interface (UI) using Vue 3, ensuring it is interactive, responsive, and adheres to UX principles.
     - Implement front-end functionality to integrate with the back-end services.
     - Collaborate closely with the UI/UX Design team to translate wireframes and mockups into a functional UI design.
     - Ensure cross-browser compatibility and optimize performance for a seamless user experience.

2. **Back-end Team**:
   - **Technologies**: Go, Gin, Redis, GORM, Aiogram + Pyrogram
   - **Team Members**: 4 developers: *Daniil Vasilev (Back-end Team Lead)*, *Apollinariia Azarskova*, *Julia Martynova*, *Artem Volkonitin* 
   - **Responsibilities**:
     - Develop scalable and efficient back-end services using Go, leveraging Redis for caching and session management.
     - Implement business logic, data processing, and database interactions using GORM for PostgreSQL.
     - Integrate with third-party APIs and university systems for user authentication, event management, and data synchronization.
     - Ensure security measures such as encryption, authentication, and authorization are implemented at the back-end level.
     - Set up microservices architecture using gRPC for efficient communication between services, managed with Envoy.

3. **Database Team**:
   - **Technologies**: PostgreSQL, Redis
   - **Team Members**: 2 developers: *Artem Volkonitin* and *Daniil Vasilev*
   - **Responsibilities**:
     - Design and optimize the database schema in PostgreSQL for storing structured data including user profiles, project details, and event information.
     - Configure Redis for caching frequently accessed data to improve application performance.
     - Ensure data integrity, scalability, and efficient query performance through indexing and database optimization techniques.
     - Collaborate with the back-end team to integrate database operations seamlessly into the application’s architecture.

4. **AI Integration Team**:
   - **Technologies**: Python, TensorFlow
   - **Team Members**: 2 developers: *Daniil Vasilev* and *TBC*
   - **Responsibilities**:
     - Implement AI-driven features such as recommendation systems and spam filtering using Python and TensorFlow.
     - Develop algorithms to analyze user behavior, recommend relevant content, and enhance user engagement.
     - Integrate AI models with the back-end services to provide personalized experiences based on user data.
     - Optimize machine learning algorithms for performance and accuracy, iterating based on feedback and testing results.

5. **Proxy Management**:
   - **Technologies**: Envoy for gRPC integration
   - **Team Members**: Managed by back-end team
   - **Responsibilities**:
     - Configure Envoy proxy for handling gRPC communication between microservices.
     - Monitor and optimize proxy performance to ensure low latency and efficient service-to-service communication.
     - Collaborate with the back-end and DevOps teams to deploy and manage Envoy configurations in the production environment.

6. **QA Team**:
   - **Technologies**: Selenium, JUnit, Postman, Docker
   - **Team Members**: 2 QA Engineers: *Artem Volkonitin* and *Dinara Murtazina*
   - **Responsibilities**:
     - Develop and execute automated test scripts using Selenium and JUnit to ensure the functionality, reliability, and performance of the application across different browsers and platforms.
     - Perform manual testing for edge cases, usability, and user acceptance testing (UAT) to validate the application’s behavior under real-world scenarios.
     - Create and maintain test cases, test plans, and testing documentation to facilitate thorough testing coverage and traceability.
     - Utilize Postman for API testing to validate endpoints, data integrity, and error handling mechanisms.
     - Collaborate with development teams to identify and resolve defects, ensuring high-quality deliverables and a seamless user experience.
     - Implement Docker for containerization of testing environments, enabling consistent and reproducible testing across development, staging, and production environments.

7. **UI/UX Design Team**:
   - **Technologies**: Figma, UI Sketch
   - **Team Members**: 3 designers: *Julia Martynova*, *Apollinariia Azarskova* and *Dinara Murtazina*
   - **Responsibilities**:
     - Create wireframes, prototypes, and visual designs for the user interface (UI) using Figma and UI Sketch.
     - Collaborate closely with the Front-end Team to translate designs into functional and intuitive user interfaces.
     - Ensure consistency in design elements, typography, colors, and overall user experience across the application.
     - Work with stakeholders and developers to align design decisions with project goals and user needs.

8. **DevOps Team**:
   - **Technologies**: GitHub Actions, Docker Swarm, Docker
   - **Team Members**: 2 DevOps Engineers: *Daniil Vasilev* and *Julia Martynova*
   - **Responsibilities**:
     - Automate deployment pipelines using GitHub Actions for continuous integration and continuous deployment (CI/CD).
     - Manage containerized applications with Docker and orchestrate using Docker Swarm for scalability and reliability.
     - Monitor application performance, logging, and ensure high availability through effective DevOps practices and tooling.

### Structuring Responsibilities

**Task Allocation**: Tasks are assigned on Trello based on the division of responsibilities among the teams. Each team focuses on specific aspects crucial to the development and functionality of the alumni portal.

**Collaboration**: Cross-team collaboration is essential for integrating various components and ensuring a cohesive application:

- **Front-end and Back-end Team**: Work closely to integrate UI designs with backend services, ensuring functionality aligns with user interface requirements.
- **AI Integration with Back-end Team**: Collaborate on integrating AI models into the backend to enhance data processing and user interaction capabilities.
- **Database Team with Back-end Team**: Collaborate to optimize database operations and ensure data integrity and scalability.
- **UI/UX Design Team with Front-end Team**: Ensure seamless integration of UI designs into functional interfaces, maintaining consistency and user-centric design principles.
- **QA Team with all other teams**: Validate functionality across teams through testing, ensuring quality assurance aligns with project goals.

Regular meetings, code reviews, and collaborative tools will facilitate knowledge sharing and alignment of goals among teams.

**Responsibility Overlaps**: Interdisciplinary tasks require collaboration between teams:

- **Front-end and Back-end Team**: Collaborate on integrating front-end interfaces with back-end logic for seamless user experience.
- **AI Integration and Back-end Team**: Collaborate on integrating AI-driven functionalities into backend systems for enhanced data analysis and user engagement.
- **QA Team with Back-end Team**: Verify backend functionality through rigorous testing to ensure performance and reliability.

### Ensuring Effectiveness

To optimize team performance and ensure project success:

- **Clear Role Definition**: Roles and responsibilities are clearly defined based on each team member's expertise and project requirements, ensuring efficient task execution.
- **Regular Updates**: Daily stand-ups and weekly progress reviews keep team members aligned with project goals and deadlines.
- **Feedback Mechanism**: Continuous feedback loops allow for adjustments in task assignments based on individual strengths and challenges, fostering a supportive team environment.

By structuring our project in this manner, leveraging our team’s strengths, and fostering collaboration, we are confident in delivering a robust alumni portal that meets the university’s needs and exceeds user expectations.

## Conclusions & Next Steps

### Key Takeaways
This week's work has solidified our tech stack choices and provided valuable insights into the project's feasibility and implementation. We've established a strong foundation with Vue 3 for the front-end, Go for the back-end, and strategic integrations with Redis, PostgreSQL, and TensorFlow for AI capabilities. The decision to use Envoy as a proxy for gRPC communication aligns with our goal of creating a scalable and efficient microservices architecture. Moreover, to our mind engaging with a project customer from the university will enrich our understanding of specific requirements and validated our approach.

### Actionable Next Steps
Building upon the progress made this week, our focus for Week #3 will be on accelerating development and expanding functionality:

1. **Front-end Development**: Initiate UI development based on finalized designs in Figma. Implement Vue 3 components and integrate with back-end APIs to ensure seamless user interactions.
   
2. **Back-end Development**: Continue building core functionalities in Go, integrating Redis for caching and optimizing database interactions with PostgreSQL via GORM. Begin initial setups for microservices architecture using gRPC and Envoy.
   
3. **AI Integration**: Start implementing AI-powered features such as spam filtering and recommendation systems using TensorFlow. Conduct testing to refine models and ensure accuracy.

4. **Infrastructure and CI/CD**: Lay the groundwork for a robust CI/CD pipeline using GitHub Actions and Docker Swarm. Automate build, test, and deployment processes to streamline development workflows.

5. **Testing and Quality Assurance**: Implement thorough testing across all components, focusing on functionality, performance, and security. Utilize automated testing tools like Selenium and Postman to validate APIs and user flows.

By adhering to these actionable steps, we aim to maintain momentum and deliver a feature-rich alumni portal that meets both technical standards and user expectations.

## Challenges & Solutions

### Obstacles Encountered
Throughout the week, several challenges emerged that required prompt attention and strategic resolution:

1. **Technical Complexity**: Integrating gRPC communication with Envoy posed initial challenges due to its configuration intricacies.
   
2. **Resource Allocation**: Allocating adequate resources across different teams (Front-end, Back-end, AI Integration) while maintaining a balanced workload was challenging.
   
3. **Skill Gaps**: The team identified gaps in AI and Microservice architecture expertises.

#### Mitigation Strategies
To address these challenges effectively, the team implemented the following strategies:

1. **Technical Training**: Dedicated time for particular back-end team members to familiarize themselves with Envoy's features and configuration options.
   
2. **Balancing Resource Allocation**: Conducted regular workload assessments and adjusted task assignments based on individual team members' strengths and workload capacities.
   
3. **Skills Development**: Enrolled in specialized AI courses and workshops to deepen understanding of TensorFlow functionalities and refine AI algorithms for enhanced performance.

### Lessons Learned
Reflecting on these challenges provided valuable insights into our project's dynamics and team capabilities:

- **Adaptability**: Flexibility in adjusting to new technologies like Envoy reinforced our ability to innovate and optimize communication within our microservices architecture.
  
- **Balancing**: Adopting a flexible resource allocation strategy promotes team collaboration and ensures equitable distribution of responsibilities, enhancing overall project efficiency.
  
- **Continuous Learning**: Emphasized the need for ongoing skills development in AI and emerging technologies to meet project requirements.

By leveraging these lessons learned, we are better positioned to navigate future challenges and drive progress towards delivering a robust and scalable alumni portal.

# Additional Sections

## Microservice architecture

### Building Microservice Infrastructure for the Alumni Portal

To build a robust microservice infrastructure for the alumni portal, we will follow a systematic approach that involves defining the basic architecture, setting up communication protocols, and ensuring proper deployment and monitoring using Docker Swarm for orchestration.

#### Basic Architecture

1. **Service Identification**: Break down the application into smaller, manageable services based on functionality. Each service should have a single responsibility.
   - **User Service**: Manages user authentication, authorization, and profile management.
   - **Project Service**: Handles project creation, updates, and queries.
   - **Event Service**: Manages university events, including creation and updates.
   - **Notification Service**: Sends notifications to users about relevant events and updates.
   - **Recommendation Service**: Uses AI to provide personalized project and event recommendations.
   - **Funding and Donation Service**: Manages fundings, donations, and financial transactions.
   - **Volunteer Service**: Coordinates volunteer activities, recruitment, and task assignments. Also manages CustDev activities.
   - **Analytics Service**: Collects and analyzes data related to user engagement, project success metrics, and event participation.
   - **Community Interaction Service**: Facilitates user interactions and community engagement implemented via telegram.
   - **Additional Requests Service**: Handles miscellaneous requests (e.g. temporary housing requests, pass requests).
   - **Gateway Service**: Serves as the entry point for client requests, handling routing and load balancing.

2. **Database Layer**:
   - **PostgreSQL**: Primary database for structured data such as user information, projects, and events.
   - **Redis**: Used for caching frequently accessed data to enhance performance.

#### Communication Between Microservices

1. **Inter-Service Communication**:
   - **gRPC**: Chosen for its performance advantages, gRPC enables efficient and low-latency communication between microservices.
   - **Protobuf**: Protocol Buffers (protobuf) will be used to define the service interfaces and data structures for gRPC communication.

2. **Service Discovery and Load Balancing**:
   - **Consul**: Used for service discovery, allowing microservices to locate each other dynamically.
   - **Traefik**: Acts as an edge router and load balancer, providing dynamic routing, SSL termination, and secure communication between services.

3. **API Gateway**:
   - **Traefik**: As the API Gateway, Traefik will route external client requests to appropriate internal microservices, manage API rate limiting, authentication, and logging.

#### Deployment Strategy

1. **Containerization**:
   - **Docker**: Each microservice will be containerized using Docker, ensuring consistency across different environments.

2. **Orchestration**:
   - **Docker Swarm**: Manages container orchestration, providing features like automated deployments, scaling, and management of containerized applications.

3. **CI/CD Pipeline**:
   - **GitHub Actions**: Automate the build, test, and deployment process. Ensures that code changes are automatically tested and deployed to the staging/production environment.

#### Monitoring and Logging

1. **Monitoring**:
   - **Prometheus**: Collects metrics from microservices and provides real-time monitoring.
   - **Grafana**: Visualizes metrics collected by Prometheus, providing dashboards and alerting.

2. **Logging**:
   - **ELK Stack (Elasticsearch, Logstash, Kibana)**: Centralizes logs from all microservices, allowing for efficient search, analysis, and visualization of log data.

#### Diagram: Basic Architecture and Communication
{{<mermaid>}}
graph LR;
    A[API_Gateway_Traefik] --> Envoy
    Envoy --> B[User_Service]
    Envoy --> C[Project_Service]
    Envoy --> F[Notification_Service]
    Envoy --> G[Event_Service]
    Envoy --> H[Recommendation_Service]
    Envoy --> J[Funding_Donation_Service]
    Envoy --> K[Volunteer_Service]
    Envoy --> L[Analytics_Service]
    Envoy --> M[Community_Interaction_Service]
    Envoy --> N[Additional_Requests_Service]
    B --> D[PostgreSQL]
    B --> E[Redis]
    C --> D
    C --> E
    G --> D
    G --> E
    H --> D
    J --> D
    K --> D
    K --> E
    L --> D
    M --> D
    N --> D
    N --> E
    E --> I[Consul]


{{</mermaid>}}

*By following this architecture and communication strategy, and utilizing Docker Swarm for orchestration, we can build a scalable, efficient, and robust microservice infrastructure for the alumni portal.*

## Communication Diagram
*(Previous microservice communication visualization, inserted for comparing)*
{{<mermaid>}}
graph TD
    subgraph "User"
        N[Student] --> |Register| B[User Registration]
        B --> |Post the request| H[Registration Approval]
        N --> |Submit Projects| C[Project Proposal Service]
        C --> |Post the request| I[Project Submission Approval]
        N --> |View Projects| D[Project Viewing and Filtering]
        N --> |View Details| E[Project Details Page]
        N --> |Submit Portfolio| F[Student Hiring Service]
        N --> |See Offers| F[Student Hiring Service]
        N --> |Request consultation or CustDev Interview| G[Consult & CustDev Service]
    end
{{</mermaid>}}
{{<mermaid>}}
graph TD
   subgraph "University Admin"
            U[Admin] --> |Approve or Decline request| H2[Registration Approval Service]
            U --> |Approve or Decline request| I2[Project Submission Approval Service]
            U --> |Approve or Decline request| A2[Additional Feature Services]
            U --> |Change the project status| B[Project Status Management]
            U --> |Watch donation and volunteer registartion history| C[Contribution Monitoring]
            U --> |View metrics| D[Analytics and Reports]
      end
{{</mermaid>}}
{{<mermaid>}}
graph TD
   subgraph "Alumni"
            A[Alumni] --> |Register| B[User Registration]
            B --> |Post the request| C[Registration Approval]
            A --> |Submit Project| D[Project Proposal Service]
            D --> |Post the request| I[Project Submission Approval]
            A --> |Watch donation history| F[Contribution Monitoring]
            A --> |Submit Job Offer| F2[Student Hiring Service]
            A --> |Make donation to support projects| G[Funding and Donation]
            A --> |Register in volunteering, assignments, view volunteer profiles.| Z[Volunteer Management]
      end
{{</mermaid>}}

## UseCase Diagrams
![UseCase - Auth](/2024/AlumniPortal-Innopolis/usecase1.png)
![UseCase - Project](/2024/AlumniPortal-Innopolis/usecase2.png)
![UseCase - Funding And Donation](/2024/AlumniPortal-Innopolis/usecase3.png)
![UseCase - Project + Recommendation (Viewing)](/2024/AlumniPortal-Innopolis/usecase4.png)
![UseCase - Management](/2024/AlumniPortal-Innopolis/usecase5.png)
![UseCase - Volunteer](/2024/AlumniPortal-Innopolis/usecase6.png)
![UseCase - Requests](/2024/AlumniPortal-Innopolis/usecase7.png)

## DataBase Architecture Results
*This is ERD .svg file, so if the image is too small you can download it*

![ERD](/2024/AlumniPortal-Innopolis/erd.svg)

## Design Description
*Figma design is in progress*
{{< embed-pdf url="/2024/AlumniPortal-Innopolis/DesignDescription.pdf" >}}