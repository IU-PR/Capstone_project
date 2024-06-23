# —
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

The technology stack for **SayNoMore** will include:
1. **Backend:**
   - **Python:** Core programming language for building the application logic and integrating AI functionalities.
   - **Flask/Django:** ***(Potential future integration)*** Web frameworks for developing the backend API and managing server-side operations.
   - **LLaMA (Language Model) Library:** Utilized for natural language processing to interpret user queries and extract necessary information.
   - **PostgreSQL:** Database for storing user data, travel details, and system logs.
2. **Frontend:**
   - **Telegram Bot API:** Interface for user interaction, allowing seamless communication and engagement with the chatbot.
   - **HTML/CSS/JavaScript:** ***(Potential future integration)*** Basic frontend technologies for any web components or user interface elements required.
3. **APIs and Integrations:**
   - **Aviasales API:** For retrieving comprehensive flight and hotel data, ensuring users have access to the latest travel information.
   - **Google Maps API:** ***(Potential future integration)*** For providing location-based services and visualizing travel routes and destinations.
4. **AI and Machine Learning:**
   - **LLaMA (Language Model) Library:** Core library for developing NLP capabilities to understand and process user inputs.
   - **Scikit-learn/TensorFlow/PyTorch**: ***(Potential future integration)*** Machine learning frameworks for implementing recommendation algorithms and personalized travel suggestions.
5. **DevOps and Deployment:**
   - **Docker:** For containerizing the application to ensure consistent environments across development and production.
   - **AWS/GCP/Azure/YaCloud:** Cloud platforms for hosting the application, providing scalability, and managing storage and computing resources.
   - **CI/CD Tools:** Jenkins/GitHub Actions for automating deployment and ensuring continuous integration and delivery.
TechStack requied for the Proof of Concept:
- Python
- LLaMa
- AviaSales API, Telegram Bot API
- Docker, GitHub Actions

### **Architecture Design**
1. **Component Breakdown**:
   The **SayNoMore** project is structured into three main modules, each responsible for different aspects of the system:
   - **Module A: Request Analyzer**
     - **Purpose**: Handles the extraction and verification of user inputs.
     - **Key Components**: 
       - **RequestAnalyzer Class**: Orchestrates the overall request processing.
       - **InformationRetrieval Classes**: Extract specific travel details like destination, dates, and budget.
       - **RequestVerification Classes**: Validate the accuracy and relevancy of the extracted information.
   ![Request Analyzer](https://hackmd.io/_uploads/S1C5TOtSA.svg)
  
   - **Module B: API Collector**
     - **Purpose**: Fetches real-time data on flights and hotels from external APIs.
     - **Key Components**:
       - **AirTicketsApi Class**: Retrieves flight information, including prices and availability.
       - **HotelApi Class**: Retrieves hotel data, including room availability and pricing.
       ![ApiCollector UML](https://hackmd.io/_uploads/rkIiTOtBR.svg)
   - **Module C: Telegram Bot Interface**
     - **Purpose**: Facilitates user interaction through the Telegram Bot API.
     - **Key Components**:
       - **Telegram Bot**: Acts as the main user interface, handling communication with users.
       - **Conversation Handler**: Manages the dialogue flow and collects user information.
Graphical representation and interconection of those 3 modules:
![FirstProtoUML](https://hackmd.io/_uploads/BJ5BSg7BA.png)
2. **Data Management**:
   Efficient data management is critical for the **SayNoMore** project, particularly in leveraging the Telegram system’s data organization and management capabilities. Here’s how we plan to handle data:
   - **Database**:
     - **PostgreSQL**: 
       - Centralized storage for user profiles, travel details, and system logs.
       - Selected for its scalability and robustness in managing structured data.
     - **Telegram Data Storage**:
       - Utilizes Telegram’s built-in data organization for managing user interactions and session states.
       - Ensures efficient handling and retrieval of user messages and session information.
   - **Data Storage**:
     - **User Data**: 
       - Stores user preferences, profiles, and interaction histories.
       - Integrates with Telegram's system to maintain session continuity and user state across interactions.
     - **Travel Information**:
       - Caches flight and hotel data fetched from external APIs to enhance response times.
       - Ensures up-to-date travel options are readily available for user queries.
   - **Data Flow**:
     - **Retrieval and Processing**:
       - Module B collects travel data from external APIs.
       - Module C captures user inputs via Telegram, with data processed and verified by Module A.
     - **Synchronization**:
       - Maintains consistent and synchronized data across modules and the Telegram bot interface.
       - Ensures seamless integration of user inputs and travel data, leveraging Telegram’s real-time data management.
   - **Data Security**:
     - **Encryption**:
       - Uses HTTPS/SSL to secure data transmission between users, the backend, and external APIs.
       - Utilizes Telegram’s built-in security features to protect data in transit.
     - **Authentication**:
       - Integrates Telegram’s authentication mechanisms for verifying user sessions.
   - **Backup and Recovery**:
     - **Regular Backups**:
       - Performs routine backups of PostgreSQL data to safeguard against data loss.
       - Leverages Telegram’s reliable session management to maintain continuity.
     - **Recovery Plans**:
       - Develops strategies to quickly restore operations in case of data disruptions.
   - **Logging and Monitoring**:
     - **Activity Logs**:
       - Logs user interactions and system events for auditing and troubleshooting.
       - Incorporates Telegram’s logging capabilities to track session activities.
     - **Performance Monitoring**:
       - Monitors Telegram’s performance metrics to ensure smooth data handling and user interactions.
3. **User Interface (UI) Design**:
   Currently, **SayNoMore** uses the Telegram Bot UI for user interactions, providing a straightforward and familiar way to plan travel. We also have plans to expand to web and mobile platforms for a richer user experience. 
   - **Telegram Bot Interface**:
     - **Main Interaction Platform**:
       - Utilizes Telegram’s chatbot to guide users through travel planning with a text-based interface.
       - Users can input details, get recommendations, and interact seamlessly.
     - **User-Friendly Features**:
       - Supports quick replies and interactive messages for easy navigation.
       - Integrates with Telegram’s conversation flow for smooth interactions.
     - **Session Management**:
       - Maintains continuity and context using Telegram’s session management.
       - Allows users to start, pause, and resume planning without losing progress.
   - **Future Web and Mobile Platforms**:
     - **Transition to Web and Mobile**:
       - Plans to develop a responsive web interface using React and native mobile apps for iOS and Android using frameworks like React Native or Flutter.
       - Aims to provide a more comprehensive and visually rich experience.
     - **Enhanced User Experience**:
       - The web and mobile platforms will include features like graphical travel route visualization, interactive maps, and detailed itinerary management.
       - Leverages mobile capabilities such as push notifications and location services for better user engagement.
     - **Consistency Across Platforms**:
       - Ensures a unified and seamless experience across Telegram, web, and mobile platforms.
       - Maintains consistent functionality and design principles across all interfaces.
4. **Integration and APIs**:
   * **External APIs**:
     * **Aviasales API**: Fetches real-time data on flights and hotels, ensuring users receive the most relevant and current travel options.
     * **Google Maps API** (Future): Potential integration for geolocation services and travel route visualization.
   * **Internal APIs**:
     * Ensures smooth data exchange between different modules within the system.
     * Facilitates seamless integration of the Telegram bot with backend services.

5. **Scalability and Performance**:
   - **Containerization**:
     * **Docker**: Used for packaging applications into containers, ensuring consistency across different environments.
   * **Cloud Services**:
     * **AWS/YaCoud/ VKCloud**: Chosen cloud platforms for hosting and scaling the application based on user demand.
   * **Load Balancing**:
     * Strategies to distribute traffic and maintain optimal performance under varying loads.

6. **Security and Privacy**:
   - **HTTPS/SSL/TLS**: Ensures secure data transmission between users and the system.

7. **Error Handling and Resilience**:
   * **Robust Error Handling**:
     * Strategies to manage and log errors gracefully, providing clear feedback to users and maintaining system stability.
   * **Resilience**:
     * Designs to ensure the system remains functional and responsive under various failure conditions.

8. **Deployment and DevOps**:
   * **Continuous Integration/Continuous Deployment (CI/CD)**:
     * **GitHub Actions**: Automates testing and deployment processes to ensure reliable updates and integrations.

### **Week 2 questionnaire:**
1. **Tech Stack Resources**:
   - **Backend**: Python (Flask/FastAPI) for developing APIs and handling server logic, PostgreSQL for database management, and Docker for containerization.
   - **Frontend**: Telegram Bot for immediate user interaction; future plans for React for web interfaces and React Native/Flutter for mobile applications.
   - **APIs**: Aviasales for fetching travel data, with potential integrations for Google Maps.
   - **Machine Learning**: LLaMA Library for NLP, TensorFlow/PyTorch for model development.
   - **DevOps**: GitHub Actions for CI/CD and cloud services like AWS/YaCloud/VKCloud for deployment.
2. **Mentorship Support**:
   - **Zamira Kholmatova**: Our mentor who provides guidance and expert advice throughout the project. She oversees our work, offers insights on complex issues, and helps us align our efforts with industry best practices.
3. **Exploring Alternative Resources**:
   - **Open-Source Libraries**: We continuously explore and integrate open-source libraries and frameworks that can enhance our development process, such as using different NLP tools or alternative API services.
   - **Online Courses and Documentation**: Team members utilize online resources like Coursera, Udemy, and official documentation to stay updated on new technologies and methodologies.
4. **Identifying Knowledge Gaps**:
   - **API Integration**: Gaps identified in understanding complex API interactions and data synchronization.
   - **Machine Learning**: Need for deeper knowledge in implementing and optimizing machine learning models, particularly for NLP tasks.
   - **Security**: Enhancing our understanding of data security practices and privacy regulations.
5. **Learning Objectives**:
   - **Master API Integrations**: Gain proficiency in integrating and managing data from multiple APIs.
   - **Advance in NLP**: Enhance skills in natural language processing to accurately interpret and process user inputs.
   - **Develop Robust Backend Systems**: Build a scalable and secure backend architecture that supports complex operations and data management.
6. **Sharing Knowledge with Peers**:
   - **Regular Team Meetings**: Weekly sync-ups to discuss progress, share learnings, and address challenges collectively.
   - **Documentation and Wiki Updates**: Keeping our project documentation and GitHub Wiki up-to-date with new insights, code snippets, and tutorials for easy reference by all team members.
   - **Code Reviews**: Conducting regular code reviews to share feedback, improve code quality, and promote best practices.
7. **Leveraging AI**:
   - **Natural Language Processing**: Using the LLaMA Library to parse and understand user inputs effectively.
   - **Machine Learning Models**: Applying TensorFlow/PyTorch to develop and refine models that can recommend optimal travel options.
   - **AI in Data Analysis**: Utilizing AI tools to analyze and predict user preferences and trends, enabling more personalized travel recommendations.
   
### **Tech Stack and Team Allocation**
| Team Member         | Role             | Responsibilities                                             |
|---------------------|------------------|--------------------------------------------------------------|
| Maxim Martyshov     | DevOps, PM, Lead | - Leading the project<br>- Managing CI/CD pipelines<br>- Maintaining GitHub repository<br>- Writing and breaking down tasks and issues<br>- Writing and overseeing reports<br>- Conceptual development<br>- Developing the Telegram bot |
| Elisei Smirnov      | Machine Learning | - Overseeing all ML development<br>- Developing machine learning models |
| Roman Makeev        | Fullstack        | - Integrating external APIs<br>- Developing core algorithms<br>- Future fullstack development for the website |
| Ilia Mitrokhin      | ML, Backend      | - Integrating LLMs into the application<br>- Developing the Telegram bot<br>- Potential backend development for the website |
| Anastasia Pichugina | ML, Fullstack    | - Integrating LLMs into the application<br>- Developing the Telegram bot<br>- Potential frontend development for the website |

### **Weekly Progress Report**
#### Overview
This week, we made significant strides in finalizing the architecture and defining the tech stack for the **SayNoMore** project. These foundational decisions have provided us with a clear roadmap for the development process and have set the stage for efficient team collaboration and task management.
#### Key Achievements
1. **Finalized Project Architecture**:
   - We have completed the design and documentation of the project’s architecture, outlining the structure and interactions of the three main modules:
     - **Module A: Request Analyzer** – Handles user input processing and data verification.
     - **Module B: API Collector** – Fetches real-time travel data from external APIs.
     - **Module C: Telegram Bot Interface** – Manages user interactions through the Telegram Bot API.
   - Detailed component breakdowns and workflow diagrams were created to ensure a comprehensive understanding of each module’s functionality and integration points.
2. **Defined Tech Stack**:
   - We have chosen the technologies and tools that will form the backbone of our project:
3. **Sub-Team Formation and Task Allocation**:
   - We have organized our team into sub-teams aligned with the project modules to focus on specific areas of development:
     - **Module A Team**: Focuses on user input processing and verification.
     - **Module B Team**: Specializes in integrating and fetching data from external APIs.
     - **Module C Team**: Handles the development and enhancement of the Telegram Bot interface.
   - Roles and responsibilities were distributed within each sub-team to leverage individual strengths and expertise, ensuring efficient progress and accountability.
4. **Streamlined Coding Process**:
   - With the architecture and tech stack in place, we have streamlined our coding process.
   - Clear module definitions and task allocations have enabled us to start implementing core functionalities systematically.
   - This alignment has brought us closer to our goal of developing the first prototype of **SayNoMore**.
#### Next Steps

- **Module Development**: Continue coding and integrating functionalities within each module, focusing on completing the initial versions of Module A and B.
- **Prototype Assembly**: Begin assembling the components to form the first prototype, enabling initial end-to-end testing.
- **Testing and Refinement**: Plan and execute unit tests and integration tests to ensure the stability and reliability of each module.
We are excited about the progress made this week and are confident that with our structured approach and dedicated sub-teams, we are well on our way to developing a robust and user-friendly travel planning assistant.

### **Challenges & Solutions**
As we advance in the development of **SayNoMore**, several challenges have emerged. Here are the key obstacles we've encountered this week and the solutions we have implemented to address them:
1. **Challenge: Complex Data Extraction and Validation**
   - **Description**: Extracting and validating accurate travel details from user inputs, especially in natural language, proved to be more complex than initially anticipated. Users may provide incomplete or ambiguous information that needs to be parsed and understood accurately by the system.
   - **Solution**:
     - **Advanced NLP Techniques**: We decided to employ more sophisticated natural language processing techniques using the LLaMA Library. This allows for better interpretation of varied user inputs and helps in extracting relevant travel details more effectively.
     - **Incremental Data Collection**: Implementing an iterative approach where the system asks for missing details step-by-step has helped in gathering comprehensive information from users. This also simplifies the user’s input process, making it more interactive and manageable.

2. **Challenge: API Integration and Data Synchronization**
   - **Description**: Integrating multiple external APIs, such as Aviasales and potential future APIs like Google Maps, posed difficulties in ensuring consistent and synchronized data retrieval. Variations in data formats and API response times also added to the complexity.
   - **Solution**:
     - **Standardized Data Handling**: We developed a unified data handling framework within the API Collector module to standardize the data retrieved from various sources. This framework ensures that all API responses are processed into a consistent format before being used by the system.
     - **Caching and Data Refresh Mechanisms**: Implementing caching mechanisms to store frequently accessed data and periodically refreshing this data has helped in managing API response times and ensuring the availability of up-to-date information.

3. **Challenge: Ensuring Seamless User Experience Across Platforms**
   - **Description**: With plans to transition from the Telegram Bot interface to web and mobile platforms, maintaining a seamless and cohesive user experience across these different interfaces is a significant challenge.
   - **Solution**:
     - **Unified Design Principles**: We established unified design principles that will guide the development of the web and mobile interfaces. These principles focus on maintaining consistency in functionality and user interaction patterns across all platforms.
     - **Incremental Rollout**: Our approach involves incrementally rolling out features first on the Telegram Bot and then extending them to the web and mobile platforms. This allows us to refine the user experience iteratively and gather feedback early on.

4. **Challenge: Team Coordination and Task Management**
   - **Description**: Coordinating tasks and ensuring effective communication among sub-teams, especially with the division of responsibilities, has been challenging. Misalignment in understanding or delays in one team can impact overall project progress.
   - **Solution**:
     - **Regular Synchronization Meetings**: We have instituted regular synchronization meetings to align on progress, share updates, and address any blockers promptly. These meetings ensure that all sub-teams are on the same page and can coordinate their efforts effectively.
     - **Clear Documentation and Task Tracking**: Using detailed documentation and task tracking tools like GitHub Issues and Project boards has helped in clarifying responsibilities and tracking progress transparently. Each team member has a clear view of their tasks and how they contribute to the larger project goals.
By addressing these challenges with strategic solutions, we are enhancing the robustness and user-friendliness of **SayNoMore** and are confident in our ability to deliver a reliable and effective travel planning assistant.

### **Conclusions & Next Steps**

### Conclusions & Next Steps
#### Conclusions
This week has been pivotal for the **SayNoMore** project as we made significant progress in several critical areas:
1. **Architecture Finalization**:
   - We have clearly defined the system’s architecture, outlining the roles and interactions of the three main modules: Request Analyzer, API Collector, and Telegram Bot Interface. This provides a strong foundation for our development efforts.
2. **Tech Stack Selection**:
   - By finalizing our tech stack, we now have a well-structured set of tools and technologies that align with our project’s needs. This decision streamlines our development process and ensures we are equipped with the best resources to build a scalable and efficient system.
3. **Team Coordination and Task Allocation**:
   - Forming sub-teams based on the project modules and distributing tasks has enhanced our focus and efficiency. Each team member now has a clear understanding of their responsibilities and how they contribute to the overall project.
4. **Streamlined Development Process**:
   - The alignment on architecture and technology has enabled us to streamline the coding process. We have started implementing core functionalities, bringing us closer to developing our first prototype.
#### Next Steps
With our foundational work in place, we are now ready to advance to the next stages of our project:
1. **Module Development**:
   - Continue coding and integrating functionalities within each module:
     - **Module A (Request Analyzer)**: Complete the development of user input processing and validation features.
     - **Module B (API Collector)**: Finalize the integration with external APIs for fetching travel data.
     - **Module C (Telegram Bot Interface)**: Enhance the Telegram bot’s capabilities to handle complex user interactions smoothly.
2. **Prototype Assembly**:
   - Begin assembling the components of each module to form the first working prototype. This involves:
     - Ensuring seamless communication between modules.
     - Validating the end-to-end functionality from user input to travel recommendation.
     - Integrating core features to provide a basic but complete travel planning experience.
3. **Testing and Refinement**:
   - Develop and execute comprehensive testing strategies to ensure the stability and reliability of each module:
     - **Unit Testing**: Verify that individual components and classes function correctly.
     - **Integration Testing**: Test the interaction between modules and external APIs.
     - **User Acceptance Testing**: Validate that the system meets user needs and expectations.
   - Use feedback from testing to refine features and fix any identified issues.
4. **Documentation and Knowledge Sharing**:
   - Continue updating our project documentation to reflect new developments and decisions.
   - Share knowledge and insights across sub-teams to maintain alignment and ensure everyone is up-to-date with the latest progress.
5. **Planning for Future Expansion**:
   - Start conceptualizing the transition to web and mobile platforms. Outline the necessary steps and requirements to expand beyond the Telegram Bot interface.
   - Explore additional data sources and API integrations to enhance the system’s capabilities.
