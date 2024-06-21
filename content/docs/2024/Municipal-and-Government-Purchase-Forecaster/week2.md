# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

Selected Tech Stack:
After careful deliberation, our team chose the following tech stack:

* Python for ML and Data Analysis: Utilizing Pandas, scikit-learn (sklearn), ARIMA for time series analysis, and matplotlib for data visualization and predictions.
* Python with Flask: Implementing Flask for building the Telegram bot interface, facilitating seamless user interactions and data processing.
* Java with Spring: Employing Spring framework for backend development to manage core business logic, ensure robust system integration, and enhance security measures

### **Architecture Design**

1. **Component Breakdown**: 
    
    1.1. Python Model:
        * Responsibilities:
            Develop algorithms for data analysis, including detection of regular purchase patterns and forecasting future needs.
            Implement machine learning models to improve prediction accuracy over time.
        * Interactions:
            Interacts with the database to fetch and store data for analysis.
            Provides data outputs and forecasts to the bot and web interface for user consumption.
    1.2. Python Bot:
        * Responsibilities:
            Serve as the primary user interaction interface through Telegram.
            Handle user requests for data visualizations, forecasts, and download links for JSON files.
        * Interactions:
            Communicates with the Telegram API to receive and send messages.
            Interacts with the Python model to request data analysis and forecasts.
            Fetches data from the database as needed.
            Utilizes the Keycloak API for user authentication and authorization.
    1.3. Java Backend:
        * Responsibilities:
            Manage core business logic and handle backend processing.
            Facilitate communication between the frontend (bot and web interface) and the database.
        * Interactions:
            Acts as a bridge between the user interfaces and the database.
            Handles API requests from the Python bot and web interface.
            Implements security measures and data encryption.

2. **Data Management**: 

    * Parsing Initial Dataset: Extract data from provided files (e.g., “Выгрузка контрактов по Заказчику”, “КПГЗ, СПГЗ, СТЕ”, “Складские остатки”, “Обороты по счету”) and load into a database.
    * Database Setup: Choose a database (e.g., PostgreSQL, MongoDB) to store parsed data.
    * Data Analysis: Implement algorithms to analyze purchase data, detect regular purchase patterns, and forecast future needs.

3. **User Interface (UI) Design**:
    
    * Telegram Bot Interface: Develop a chatbot using the Telegram API to interact with users, allowing them to request data visualizations, forecasts, and download JSON files.

4. **Integration and APIs**:

    * Telegram API: For creating the bot and handling user interactions.
    * GPT API: For processing natural language commands if needed for advanced interaction.
    * Keycloak API: For handling user authentication and authorization.

5. **Scalability and Performance**:

    * Service Scalability: Design the service to support multiple organizations and various time periods.
    * Load Balancing: Use load balancing techniques to ensure service stability under high demand.
    * Database Optimization: Implement indexing and caching strategies to handle large datasets efficiently.

6. **Security and Privacy**:
    
    * User Authentication and Authorization: Implement Keycloak for secure user authentication and authorization.
    * Role Management: Differentiate between common users and administrators, restricting access to sensitive functionalities and data.
    * Data Encryption: Encrypt sensitive data both in transit and at rest.

7. **Error Handling and Resilience**:
    
    * Error Logging: Implement comprehensive logging for tracking errors and issues.
    * Retry Mechanisms: Develop retry mechanisms for failed operations, especially for API calls.
    * Graceful Degradation: Ensure the system can still function with reduced capabilities in case of partial failures.

8. **Deployment and DevOps**:
    * Docker Containers: Containerize the application using Docker for consistency across development, testing, and production environments.
    * Remote Server: Deploy the application on a remote server (e.g., AWS, Azure) for accessibility and scalability.

### **Week 2 questionnaire:**

1) Tech Stack Resources: No special project-based books were used. Instead of relying on specific project-based books, the development team utilizes a variety of online resources and mentorship for guidance and support.

2) Mentorship Support: Yes, a mentor is involved who acts as a business analyst. The mentor provides detailed insights into how the service should work, guiding the team in understanding the business requirements and aligning the technical implementation with those needs.

3) Exploring Alternative Resources: 

* YouTube: For video tutorials and practical demonstrations on various aspects of the tech stack and project implementation.
* Stack Overflow: To find solutions to specific coding issues, seek advice from the developer community, and understand best practices.
* GPT (OpenAI): For obtaining explanations, generating code snippets, and gaining insights into complex technical concepts.
* Documentations: Official documentation for Python, Java, PostgreSQL, MongoDB, Telegram API, and other relevant technologies for accurate and detailed information.

4) Identifying Knowledge Gaps:

* How to predict in time series: Understanding the principles and techniques for time series forecasting to make accurate predictions about future data points.
* Laws for creating a forecasted purchase: Gaining knowledge about the legal and business regulations that affect purchase forecasting, ensuring compliance and relevance in predictions.

5) Engaging with the Tech Community: No specific meetups were attended. However, the team remains engaged with the broader tech community through online forums and discussion groups.

6) Learning Objectives:

* Learn more about using ML in projects: Deepen the understanding of machine learning algorithms and their practical application in real-world projects.
* Using backend knowledge to implement logic: Enhance backend development skills to effectively implement business logic and ensure seamless integration with other components.
* Using Telegram API for a friendly user path: Gain proficiency in using the Telegram API to create an intuitive and user-friendly chatbot interface.

7) Sharing Knowledge with Peers:

* Weekly meetups: The team conducts weekly meetings to share progress, discuss challenges, and exchange knowledge.
* Documentation: Comprehensive documentation is created for every part of the project, ensuring that all team members have access to the information and can understand the contributions made by others.
* Explaining parts done by individuals: Each team member explains their contributions to other interested members, fostering a collaborative learning environment.

8) Leveraging AI:

* GPT for natural language processing: Using GPT for processing natural language commands to enhance user interaction with the service.

* Use of GPT for project assistance: Utilizing GPT to assist with various aspects of the project, such as generating code snippets, debugging, and providing explanations for complex technical concepts.

### **Tech Stack and Team Allocation**

Team discussions led to the selection of a tech stack focused on machine learning (ML) and data analysis, aligning with project goals.

| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
| Erokhin Evgenii (Lead)   | [DS]                                        | [MLEngineer/Lead]  |
| Daniil Zimin             | [SD]                                        | [DA/DataPrep]      |
| Pakhomov Roman           | [SD]                                        | [DA/DataPrep]      |
| Krasheninnikov Ilya      | [AI]                                        | [PythonBack/TgBot] |
| Zverev Demyan            | [SD]                                        | [JavaBack]         |
| Davydov Danil            | [DS]                                        | [MLEngineer]       |
| Niyaz Shaydullin         | [SD]                                        | [DAHelp/Reports]   |

### **Weekly Progress Report**

We wrote most of the scripts and code for the service, python scripts for parsers, java code for backend and natural language proceeding, telegram api for bot to chat with user.

### **Challenges & Solutions**

We faced with difficulties that is to rewrite logic of parsers into java, since it will be faster and no need to keep them in different docker container. Also we made a forecast, but not all fields can be fulfilled with given information.

### **Conclusions & Next Steps**

We will rewrite parsers into java for faster work, create functionality to save forecast as excel so the user can manually fullfill the needed cells. And now we at the stage of connecting all together
