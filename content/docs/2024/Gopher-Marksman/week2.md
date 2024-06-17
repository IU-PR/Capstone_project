---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

Our chosen tech stack combines efficiency, scalability, and ease of development, suitable for handling the demands of a real-time trading platform:

- **Backend:** Python with FastAPI, for its fast, asynchronous capabilities.
- **Blockchain Interaction:** Pythoniq, offering direct and efficient interactions with the TON Blockchain.
- **Database:** PostgreSQL, for robust data management and transaction safety.
- **Frontend:** React.js, enhanced with Redux (or Context API) for state management, React Router for navigation, and JWT for secure authentication.
- **Visualization Tools:** Chart.js or D3.js for dynamic data visualization.
- **HTTP Client:** Axios for making efficient HTTP requests.
- **Containerization:** Docker, ensuring consistent environments and smooth deployment.
- **UI Framework:** Ant Design and shadcn, providing elegant templates and UI components.

### **Architecture Design**

**Component Breakdown**:

Project includes five main components:

1. Nginx - entry-point reverse proxy for all components.
2. API service - serves API requests.
3. TG service - handles requests from telegram (bots).
4. Workers - nodes for execution of background tasks (sending notifications, collecting real-time exchange rates, indexing new tokens, etc...).
5. Frontend service - serves frontend static files.

Backend of the project follows monolithic architecture approach and will be built using FastAPI, SQLAlchemy, Celery, and Alembic.
The code follows common multi-layer pattern:

- repository level for CRUD operations,
- service layer for business logic,
- routing layer for exposing endpoints.
API, workers, and telegram handlers are built on top of same repository and service layers and provide their own logic.

Current code structure looks like this:

```
App/
├─ core/ (project-wide properties e.g. settings)
├─ models/ (definition of sqlalchemy models)
├─ repo/ (data access layer)
├─ schemas/ (data transfer objects)
├─ services/ (main business logic)
├─ web_api/ (API routing)
├─ ├─ v1/ 
├─ tg/ (telegram bot handlers)
├─ worker_tasks (background execution of business logic)
```

**Data Management**:

The user data will be stored in postgreSQL, and operational data on exchange rates and important real-time metrics will be stored in in-memory database with frequent dump to postgreSQL for historical overview.

**Integration and APIs**:

TON Blockchain Interaction: Our application interacts directly with the TON Blockchain using Pythoniq, facilitating real-time transactions and data retrieval.

TonAPI: This API is utilized to access additional blockchain data and services that are not directly managed through Pythoniq, enhancing our application's capabilities in managing blockchain interactions.

**Scalability and Performance**:

The app is containerised. API is easily scalable since it can be replicated and by design placed behind nginx which also work as a load balancer.

```
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/
```

**Security and Privacy**:

App works only for authorized users. Authentication is handled using telegram (it is the only method of signing in). After successful authentication 2 tokens are granted to user: access (JWT which is valid for very short time) and refresh (one-time token valid for long time and used to obtain new pair of access and refresh tokens). Short-living access token helps to reduce number of requests to database and refresh tokens allows user to manage and invalidate sessions.
Additionally, load and activity monitoring should be introduced into infrastructure so that teams knows about lack of resources or breach attempts.

**Error Handling and Resilience**:

All releases must be tested before shipping to production, however in case of error container will be automatically restarted and team will receive notification about incident. 

**Deployment and DevOps**:

MVP will be serviced on a single VPS. Code linting and testing is done with help of Gihub Actions,

**User Interface (UI) Design**:

For the Gopher-Marksman project, low-fidelity wireframes have been deployed for two primary screens: Wallets and Currency Exchange. These wireframes serve as initial conceptual models for the interface, aimed at testing and gathering feedback from stakeholders.

***Wallets Screen:***
The Wallets screen displays a list of available cryptocurrency assets with key details such as balance and current value. The emphasis on simplicity and user-friendliness allows users to easily manage their assets and obtain real-time information about their status.

![Wallets Screen](/2024/Gopher-Marksman/Wallets-Low.jpg "Wallets Screen")

***Currency Exchage Screen:***
The Currency Exchange screen provides an interface for executing cryptocurrency exchange operations. Users can select currency pairs for exchange, specify desired amounts, and view current exchange rates. The design prioritizes simplicity and intuitive usability to enable users to quickly familiarize themselves with the functionality and execute exchange operations efficiently.

![Exchange Screen](/2024/Gopher-Marksman/Exchange-Low.jpg "Exchange Screen")

***Purpose of Low-Fidelity Wireframes:***
The low-fidelity wireframes are designed to illustrate initial interface concepts for Gopher-Marksman project, gather feedback, and lay the foundation for more detailed prototyping. Future steps will involve integrating feedback to enhance design and functionality before progressing to advanced development stages.


### **Week 2 questionnaire:**

1) Tech Stack Resources:
   - Backend (Python/FastAPI): Dive into resources like the [official FastAPI documentation](https://fastapi.tiangolo.com/), [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) and [Nginx documentation](https://docs.nginx.com/).
   - Blockchain Interaction: Utilize the [TON documentation](https://docs.ton.org/develop/overview) and the [TON developer community forums](https://tonresear.ch/) for examples and best practices.
   - Frontend: Use the [official React documentation](https://react.dev/learn).

2) Mentorship Support:
   - Regular consultations with blockchain experts from the TON community have underscored important considerations such as transaction security, data integrity, and the effective use of blockchain APIs for enhanced functionalities.

3) Identifying Knowledge Gaps:
   - Through our exploration of alternative resources, we've identified gaps in:
     - Advanced state management techniques in React.
     - Optimizing FastAPI for low-latency applications.
     - Understanding complex blockchain interactions for decentralized applications.

4) Engaging with the Tech Community:
   - We participate in tech forums such as Stack Overflow, GitHub discussions, and local meetups in Innopolis. These interactions help gain insights and address specific technical challenges.

5) Learning Objectives:
   - Aim to master asynchronous programming in Python using FastAPI and understand the reactive patterns in React for frontend state management.
   - Deepen understanding of blockchain technology with Pythoniq and its practical applications in financial technology.
   - Develop robust API integrations using Axios and secure authentication mechanisms using JWT.

6) Sharing Knowledge with Peers:
   - We conduct bi-weekly internal workshops to share knowledge on newly learned technologies and solutions to technical challenges. Documentation is maintained on an internal wiki, accessible to all team members for quick reference.

7) Leveraging AI:
   - Investigating AI-driven analytics tools to optimize trading strategies and risk assessment. Utilizing AI-powered libraries to enhance user interface interactions and predictive functionalities in our application.

### **Tech Stack and Team Allocation**

| Team Member              | Track             | Responsibilities                                      |
|--------------------------|-------------------|-------------------------------------------------------|
| Georgii Butakov (Lead)   | Backend           | Teamlead, Backend development, integration with blockchain      |
| Artyom Shaposhnikov      | Backend           | Backend development, DevOps |
| Nikita Ruchkin           | UI/UX,Frontend    | UI/UX designer |
| Ivan Platonov            | Backend           | Backend development, DevOps |
| Mikhail Dudinov          | Frontend/Design   | Frontend development|

### **Weekly Progress Report**

This week, the team accomplished significant milestones in both the technological foundation and the user interface design of the Gopher-Marksman project. We finalized our tech stack, choosing technologies that ensure scalability, robust performance, and ease of use for end-users. The architecture was meticulously planned, integrating components like Nginx, API services, and worker nodes, which form the backbone of our application. Concurrently, UI design took a front seat as we started with low-fidelity wireframes to test and gather initial feedback.

#### **More about work done with UI/UX part:**

In the second week of the project, the development of the User Interface (UI) for Gopher-Marksman began, emphasizing theoretical aspects and hypotheses aimed at optimizing user experience and efficiently managing trading operations across various decentralized exchanges (DEX).

1. User Needs Exploration and Hypotheses:
   - Initially, an analysys of potential user expectations and behavioral patterns was conducted.
   - Hypotheses regarding which UI features and elements would be most in demand were formulated based on open data trends in cryptocurrency trading and consultations with experts.
   - Key principles of usability heuristics were applied, including visibility of system status, system-world compatibility, and error prevention.
2. Application of Theoretical Design Patterns:
   - The design process involved consideration and selection of theoretical design patterns, such as Atomic Design for organizing interface components, and the Double Diamond methodology. The latter encompasses two primary cycles: first, understanding user needs and usage contexts; second, iterative testing and design improvement based on feedback.
   - These approaches aim to create a logically structured system that easily scalable for future development iterations.
3. Preliminary Modeling and Prototyping:
   - Preliminary conceptual models and prototypes of the UI were developed to visualize proposed solutions and obtain feedback from potential users and stakeholders.
   - This stage refined concepts and representations of functionality within the framework of theoretical hypotheses and assumptions.

### **Challenges & Solutions**

1. Challenge: Integration of diverse technologies into a cohesive architecture.
   - Solution: We adopted a monolithic architecture with clear component segregation to facilitate easier management and scalability. This approach simplifies the interaction between different parts of the application while maintaining robust performance.
2. Challenge: Ensuring real-time data handling and transaction safety in a trading platform.
   - Solution: We chose PostgreSQL for its strong transaction support and integrated Pythoniq for efficient blockchain interactions. This setup is designed to handle real-time data with high reliability and security.
3. Challenge: Balancing advanced functionality with user-friendly design in the UI.
   - Solution: Our UI team began with theoretical exploration and gradually moved to practical prototyping, ensuring that the design is both aesthetically pleasing and functionally robust. The iterative design process is supported by expert consultations and user feedback to refine the interface continually.

### **Conclusions & Next Steps**

- Conclusions: The second week marked a pivotal phase in the Gopher-Marksman project, with solid progress in both technological groundwork and user interface design. The tech stack and architecture are aligned with our goals for a high-performance trading platform, and the initial UI designs have been well-received.

- Next Steps:
    1. Implement the core backend functionalities using FastAPI and integrate it with the frontend components developed in React.js.
    2. Continue enhancing the UI based on ongoing feedback and integrate advanced visualization tools like Chart.js or D3.js for dynamic data presentation.
    3. Start the development of the API and worker services that will handle the backend logic and real-time data processing.
