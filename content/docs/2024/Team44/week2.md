---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**



### **Architecture Design**


1. **Component Breakdown**: 

Our project architecture consists of several key components, each with distinct responsibilities to ensure a cohesive and robust system:

- Frontend:
    - User Interface for Interaction
    - User authentication and profile management
- Backend:
    - Initial data parsing and processing
    - Integration with ML/NLP functionalities without independent servers to reduce costs and simplify deployment
- Machine Learning (ML):
    - Action Router: Directs requests to appropriate ML modules
    - Quiz Generator: Creates quizzes based on user notes
    - Summary Generator: Summarizes user notes
    - Search Engine: Searches through user notes using NLP
- Databases:
    - Vector Database: Stores user notes and serves as the primary data repository
    - Postgres Database: Manages user data, including authentication details
- Future Possibilities:
    - Telegram Bot: Not prioritized due to time constraints but can be considered if core components are completed ahead of schedule


2. **Data Management**: 

 Data management strategies are critical for ensuring efficient storage, access, and manipulation, here is a description of them:  
 - User's Data: stored in a Postgres database and includes email, username, password, telegram ID (for future use), and potentially uploaded data files. 
 - User's Notes Data: stored in a shared Vector Database for fast retrieval and efficient storage. 
 - Caching Database (optional): may be introduced to cache frequently accessed data, improving performance. 

3. **User Interface (UI) Design**:

User experience is central to our application’s success. The UI should be intuitive and easy to navigate, featuring a clear layout and seamless flow. Visual design elements will be employed to enhance usability, ensuring that users can interact with the system efficiently and effectively.
  

4. **Integration and APIs**:

External integrations and APIs are essential for extending our application’s functionality. While we are considering the use of open-source LLM APIs for machine learning tasks, we will evaluate the trade-offs between data security and the cost-effectiveness of using external APIs versus hosting models in-house. Our priority is to ensure secure and reliable data flow between systems, and we will only use external APIs if they meet our stringent security and cost requirements.

5. **Scalability and Performance**:

Designing for scalability and performance ensures long-term viability. To handle user requests, we plan to implement a queue system for embedding, quiz, and summary generation. Potential solutions include parallel/async processing to distribute the load, upgrading server capabilities to reduce operation time, storing pre-generated quizzes/summaries for quick access, and exploring caching layers for frequently requested data.

6. **Security and Privacy**:

Protecting user data is paramount. We will implement authentication and authorization protocols, and establish user agreements that outline data sharing in the shared Vector Database. These measures will safeguard against potential vulnerabilities and ensure compliance with privacy standards.


7. **Error Handling and Resilience**:

Ensuring reliability through robust error handling is essential. Therefore,  We will implement comprehensive error logging and monitoring, consider developing strategies for graceful error recovery, and mitigate against DDoS attacks using API gateways and firewalls. Optimizing frontend-backend communication will also help to minimize vulnerabilities and enhance system resilience.

8. **Deployment and DevOps**:

Since streamlined deployment and continuous integration are crucial we are aiming to establish automated deployment pipelines, utilize version control through Git, and implement a robust development workflow with continuous integration and continuous deployment (CI/CD) practices. These steps will ensure smooth and efficient deployment processes, facilitating ongoing development and maintenance.

This architecture design provides a comprehensive framework for developing a robust, scalable, and maintainable application, ensuring all critical aspects are covered, from data management to deployment.

### **Week 2 questionnaire:**

1) Tech Stack Resources: We are not utilizing project-based books that cover our stack

2) Mentorship Support: We do not have a mentor and will handle frontend development, backend development, machine learning, and DevOps responsibilities ourselves.

3) Exploring Alternative Resources: 

To stay adaptable and informed, we will explore alternative resources. Here is the description below:

- Machine Learning:
    - LangChain/LangGraph Tutorials: The [LangGraph Docs and LangChain Docs](https://langchain-ai.github.io/langgraph/) have provided comprehensive guidance on implementing and optimizing our ML models.
    - Community Examples: [The Pinecone examples on GitHub](https://github.com/pinecone-io/examples/tree/master) have been invaluable in demonstrating practical applications and best practices for vector databases (excluding fact of using the Pinecone Vector Database).
    - Machine Learning Models and Documentation, [Hugging Face](https://huggingface.co): We regularly refer to Hugging Face for models and the transformer's documentation to keep up with the latest advancements and integrate cutting-edge NLP techniques into our project.

- Backend Development:
    - GeeksforGeeks Videos: Specifically, videos such as "How to Create a Login System in Python Using Django?" have helped us understand practical implementations.
    - Django REST Framework Documentation: The [official DRF documentation](https://www.django-rest-framework.org/) is a go-to resource for mastering RESTful API development.
    - DRF Video Course: The [DRF video-course playlist](https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs) offers structured and in-depth tutorials on the Django REST Framework.

- Frontend Development:
    - The previous year's Svelte course from Innopolis University has enhanced our understanding of modern front-end development.
    - Official documentation of the SvelteKit framework
    - We used the [official SvelteKit documentation](https://kit.svelte.dev/docs/) for a better understanding and more proficient usage of the framework

These resources are vital in filling our knowledge gaps by offering structured learning paths, practical examples, and detailed technical explanations.


4) Identifying Knowledge Gaps:

We will identify and address knowledge gaps in the following areas: 

- ML:
    - Gaps: 
        - No previous knowledge of work with NLP, having some knowledge of general ideas behind how RAG works. 
    - Closing gap:
        - The elective course (Deep Learning for Search) provides detailed materials for exploring NLP: basic concepts, embedding, transformers, search methods, and similarity metrics, and a general idea of creating RAG and ML app pipelines. The course provides practical tasks and requests reading papers on these topics.
        - Learning using docs of LangChain and HuggingFace tutorials.

- Backend:
    - Gaps: 
        To connect the ML model with the backend in Django, integrate the model within a Django view or API endpoint. To connect the backend with the front end using APIs, implement Django Rest Framework (DRF) to create API endpoints that handle requests, invoke the ML model, and return responses to the front end.
    - Closing gaps: 
        Online resources and practice: go through tutorials carefully and enhance knowledge by analyzing documentation. In addition, be in active contact with other non-backend components

- Frontend:
    - Gaps:
        - Lack of experience in doing interactive UI and pleasant UX for the user; no experience at all using Django framework
    - Closing gaps:
        - The hum elective course "UX/UI Design" allows for achieving sufficient experience in order to make comprehensive frontend; as for Django - the frontend team will learn about it online via Youtube courses or official documentation.


5) Engaging with the Tech Community: We have not yet actively engaged with the broader tech community for this project. 

6) Learning Objectives:

- Mastering the integration of ML models into a backend system.
- Understanding and implementing scalable and secure API designs.
- Gaining proficiency in deploying applications using Docker.
- Enhancing UI/UX design skills for creating intuitive and responsive user interfaces.


7) Sharing Knowledge with Peers:

We will share knowledge with peers through the documentation and tutorials that allow us to create the comprehensive guides and documentation for key components of the tech stack.

8) Leveraging AI:

We will leverage AI to enhance our project in the following ways:

- Improving Development Processes: Utilizing AI-Powered Tools for Code Analysis, Error Detection, and Performance Optimization.


### **Tech Stack and Team Allocation**



| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
|Aruzhan Shinbayeva    | [product manager]                               | [writing reports/leading the team]  |
| Anushervon Qodirzoda | [backend]                                       | [tg bot/databases/authorization]      |
| Ilia Mistiurin       | [ML]                                            | [working with LLM models]      |
|Ivan Smirnov          | [frontend]                                      | [creation of the website] |
|Muhammad Allayarov    | [backend]                                       | [tg bot/api]         |


### **Weekly Progress Report**

This week, we successfully closed two key issues: creating templates for the Quiz Generator and Summary Generator in our machine learning module. Currently, our main focus is configuring the PostgreSQL database for secure storage of user authentication details. Moving forward, our immediate goals are to complete the database setup, ensuring clarity and robust data management for the project. Overall, we are making solid progress and remain on track with our development milestones.

### **Challenges & Solutions**

1. **Establishing Inter-Application Communication:**

During the process of setting up communication between different applications (as depicted in the Excalidraw diagram), challenges arose in ensuring seamless transitions between pages based on user actions. Through careful planning and diagramming, we clarified the flow of interactions and implemented necessary technical configurations to achieve cohesive application integration.

2.  **Integration of Gmail for Registration Confirmation:**

Addressing the integration of Gmail for registration confirmation involved selecting a dedicated Gmail account to send emails and confirmations.In the 'settings.py' file, the configuration for sending emails is crucial as it defines how the application sends messasges to users. This includes specifying the SMTP backend, server details, and authentication requirements. All sensitive information, such as the Gmail account's username and password used to send confirmation links, is securely stored in the '.env' file. This approach ensured reliable email delivery and seamless user verification processes.

3.  **Continuous Search and Optimization of Models:**

Addressing the challenge of continuous search and optimization of models, especially as we progress into weeks 6-7, involves implementing strategies for ongoing model refinement and performance enhancement. This includes leveraging techniques such as hyperparameter tuning, iterative training cycles, and monitoring model performance metrics. By dedicating time to regularly review and update our models based on real-world data and feedback, we ensure that our application maintains high accuracy and efficiency in delivering results.

Throughout our development process, we have successfully navigated challenges including establishing seamless inter-application communication and integrating Gmail for registration confirmation. Looking ahead into weeks 6-7, our focus will be on continuously optimizing and refining our models to ensure they deliver accurate and efficient results.

### **Conclusions & Next Steps**
Concluding Week 2, we have successfully closed milestones related to machine learning templates and initiated the setup of a secure PostgreSQL database for user data storage. Looking ahead to Week 3 and beyond, our focus will shift to key tasks: developing the basic Embedder + Vector Database module to enhance data management capabilities, creating an evaluation module for application quality assessment, integrating frontend and backend components to prototype the project, and linking machine learning models with backend data pipelines for streamlined processing. Finalizing the PostgreSQL database configuration remains critical for ensuring robustness and security. These tasks are pivotal as we progress towards project milestones, aiming for comprehensive and efficient implementation.

