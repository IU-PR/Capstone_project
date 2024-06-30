---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

- **Frontend**
  - **Technologies**: React, Next.js, Figma

- **Backend**
  - **Technologies**: FastAPI, MongoDB

- **Machine Learning (ML)**
  - **Technologies**: PyTorch, Python libraries, IPython Notebook

- **DevOps**
  - **Technologies**: Docker, Docker Compose

### **Architecture Design**

This week, our team made significant strides in defining a robust and scalable architecture, crucial for the long-term success and maintainability of our project. Below is a breakdown of the core components of our software solution, along with their primary responsibilities and interactions:

1. **Component Breakdown**: 

- **Frontend**
  - **Technologies**: React, Next.js, Figma
  - **Responsibilities**: Provides the user interface and handles client-side interactions.
  - **Interactions**: Communicates with the backend via HTTP requests to fetch and display data.

- **Backend**
  - **Technologies**: FastAPI, MongoDB
  - **Responsibilities**: Manages server-side logic, database operations, and API endpoints.
  - **Interactions**: Serves data to the frontend and interfaces with the ML component through HTTP requests for data processing.

- **Machine Learning (ML)**
  - **Technologies**: PyTorch, Python libraries, IPython Notebook
  - **Responsibilities**: Performs data analysis and predictive modeling.
  - **Interactions**: Receives processed data from the backend via HTTP requests, performs analyses, and sends insights back to the backend through HTTP responses.

- **DevOps**
  - **Technologies**: Docker, Docker Compose
  - **Responsibilities**: Ensures smooth deployment, scalability, and maintenance of software components.
  - **Interactions**: Supports continuous integration and deployment pipelines, facilitating seamless interaction between different components through Docker networking.

Each component is encapsulated within its own Docker image, enhancing the scalability and maintainability of our system. These images communicate with each other using HTTP requests, ensuring efficient and secure data exchange.

### Product Management

- **Tool**: Height
- **Usage**: Manages project tasks and product development sprints, aiding in tracking progress and coordinating team efforts efficiently.

This architecture and product management setup are designed to ensure that our software can adapt to future requirements and growth efficiently.

2. **Data Management**: 

For storing, accessing, and manipulating data within our application, we have selected **MongoDB** as our primary database. MongoDB is a NoSQL database known for its high performance, high availability, and easy scalability, making it an excellent choice for applications that require the ability to handle large volumes of diverse data types. This flexibility is particularly beneficial for our dynamic datasets and rapid development cycle.

3. **User Interface (UI) Design**: 

In the planning and design of our user interface, we have chosen **Figma** as our primary tool for creating wireframes and mockups. Figma enables real-time collaboration, which is crucial for our distributed team to iterate quickly and efficiently. Additionally, its comprehensive design features and user-friendly interface allow us to visualize the layout and flow of our application effectively, ensuring a seamless and intuitive user experience.

4. **Integration and APIs**:

Our application will integrate the **YaGPT API** for advanced natural language processing. We are also considering the potential integration of **Llama70B** for enhanced data analytics capabilities.

- **YaGPT API**: Enhances dialogue management and content generation.
- **Potential Llama70B Integration**: Could significantly improve large dataset processing.

These integrations will be managed through secure API calls, optimizing data flow and functionality within our application.

5. **Scalability and Performance**: 

To ensure our application can accommodate future growth and maintain high performance under increased user loads and data volumes, we've designed our architecture with scalability in mind:

- **Containerization**: Utilizing four different containers allows for modular updates and scaling. Each component (Frontend, Backend, ML Model, Database) operates independently, enhancing maintainability and scalability.
  
- **ML Model to Inference Server**: By deploying our ML model to a dedicated inference server, we can manage resource-intensive tasks more effectively, ensuring swift data processing even under high demand.
  
- **Kubernetes for ML and Database**: Wrapping Kubernetes around our ML model and database components ensures automated scaling and load balancing, crucial for handling spikes in usage without performance degradation.
  
- **Next.js for Frontend**: Leveraging Next.js in our frontend development offers built-in scalability features, supporting increased traffic and dynamic content rendering with minimal overhead.

These strategies collectively ensure that our application remains robust and responsive as it scales.

6. **Security and Privacy**:

Our application's architecture incorporates essential security measures to ensure user data protection and mitigate potential vulnerabilities:

- **Security Isolation with Independent Containers**: Each component of our application (Frontend, Backend, ML Model, Database) is housed in separate Docker containers. This structure prevents single points of failure, providing a level of security isolation that protects against cross-component vulnerabilities.

- **Simplified Security Needs**: Given that our project does not handle sensitive user information, complex encryption and authorization mechanisms are not required. This reduces the potential attack surface and simplifies our security architecture while maintaining adequate protection for the data we do process.

These strategies are tailored to our application's specific security needs, ensuring effective protection without unnecessary complexity.

7. **Error Handling and Resilience**:

To maintain a reliable and resilient application, our error handling strategy includes:

- **Continuous Integration Mechanisms**: Ensures that errors are caught early during the development process, reducing the risk of bugs making it to production. This includes automated builds and tests run against every code commit, providing immediate feedback on the system's health.

- **Unit Testing**: Each component is rigorously tested in isolation to ensure that individual functions perform as expected under various conditions. This helps in identifying and fixing errors quickly before they affect other parts of the application.

- **User Testing**: Engages real users in testing to identify unforeseen errors and usability issues in a real-world scenario. This feedback is crucial for adjusting and improving the application's error handling capabilities and user experience.

Together, these strategies enhance our application’s reliability by enabling efficient error detection, logging, monitoring, and recovery, ensuring that the system remains robust even under unexpected conditions.

8. **Deployment and DevOps**:

Our deployment process and DevOps practices are designed to ensure smooth, continuous operations and alignment with our tech stack:

- **Containerized Deployment**: We utilize four separate Docker images for each major component of the application (Frontend, Backend, ML Model, Database). This approach facilitates independent scaling, updates, and management, enhancing the flexibility and resilience of our deployment strategy.

- **Continuous Deployment (CD)**: Automated deployment processes ensure that new code changes are smoothly and reliably pushed to production after passing set testing protocols. This minimizes downtime and accelerates the pace of continuous improvement.

- **Version Control**: Implementing strict version control using tools like Git allows us to track changes, revert to previous states if necessary, and efficiently manage concurrent development efforts. This is essential for maintaining code integrity and facilitating collaborative development.

These practices are integral to our robust DevOps culture, driving efficient, reliable, and scalable software delivery.

### **Week 2 questionnaire:**

1) Tech Stack Resources: 

   - **Books:**
     - *Practical Natural Language Processing* by Sowmya Vajjala, Bodhisattwa Majumder, Anuj Gupta, Harshit Surana

   **Utilization:**
   - We are leveraging *Practical Natural Language Processing* to deepen our understanding of NLP techniques, which are crucial for our project's development. The book provides practical insights and hands-on examples that are directly applicable to our work, enabling us to implement effective NLP solutions and improve our technical proficiency.


2) Mentorship Support: 

   - **Mentor:** Rustam Lukmanov
   - **Influence:** Rustam Lukmanov has provided valuable guidance on machine learning issues from an ethical perspective. His insights have helped us refine our focus and determine our next steps, positively influencing our project's direction and ethical considerations.

3) Exploring Alternative Resources: 

- **NLP Course for You by Lena Voita:** This course offers in-depth coverage of NLP techniques and practical applications, enhancing our technical skills and understanding.
- **Yandex ML Handbook:** A comprehensive guide that provides valuable insights into machine learning practices and principles, helping us address specific technical challenges.
- **Papers on arXiv:** Access to the latest research and developments in our field allows us to stay updated with cutting-edge advancements and integrate innovative solutions into our project.

4) Identifying Knowledge Gaps: 

- **Knowledge Gaps and Plans:**
  - **Practical NLP:** We are focusing on enhancing our practical NLP skills by studying *Practical Natural Language Processing* and other educational resources.
  - **Writing Optimized Code:** To improve our coding efficiency, we are reading documentation and best practices on writing optimized code.
  - **Parsing:** Minor issues in parsing are being addressed by consulting relevant tutorials and documentation.
  - **Backend Development:** For minor backend issues, we are continually referring to technical books and online resources to ensure a comprehensive understanding.

Our approach involves a consistent effort to read educational resources, books, and documentation to fill these knowledge gaps and ensure a well-rounded expertise within our team.

5) Engaging with the Tech Community: 

As part of our professional and educational growth inspired by the broader tech community, our team member Ruslan Izmailov will undertake an educational trip to Saint Petersburg at the end of June on the Yandex Software Engineering Student Camp. This trip aims to gain experience in the architecture of high-load systems, DevOps, and computer networks. The unique insights and expertise gained from this experience will significantly benefit our project.

6) Learning Objectives: 

- **Back-end:**
  - **Objectives:**
    - Parsing mechanism
    - API design
    - Logic of backend submission
    - Problems with enums on microservices
    - User/unit test scenarios
  - **Strategies:**
    - Study relevant documentation and tutorials
    - Implement small projects to practice concepts
    - Conduct code reviews and pair programming sessions

- **Frontend:**
  - **Objectives:**
    - Document upload page
    - Questions pages
    - Figma prototype
    - Playground page
  - **Strategies:**
    - Follow design guidelines and best practices
    - Use Figma for prototyping and feedback collection
    - Develop and test UI components iteratively

- **ML:**
  - **Objectives:**
    - Embeddings + classical ML models
    - Experiment notebook templates
    - YaGPT fine-tuning and inference
  - **Strategies:**
    - Review academic papers and online courses on embeddings and ML models
    - Create and maintain detailed experiment notebooks
    - Perform fine-tuning and inference tests on YaGPT, documenting results and improvements

7) Sharing Knowledge with Peers: 

Yes, we held a meeting to discuss insights about the project direction and progress. This session facilitated the exchange of ideas and experiences, ensuring that all team members are aligned and informed about the latest developments and strategies related to our tech stack.

8) Leveraging AI: 

No, we have not leveraged AI to compensate for any lacking expertise in our tech stack, as the tasks can currently be managed without it.

### **Tech Stack and Team Allocation**

| Team Member               | Track                                   | Responsibilities                               |
|---------------------------|-----------------------------------------|------------------------------------------------|
| Nursultan Abdullaev       | ML, Management                          | Report, Planning, LLM API Inference, Data      |
| Ruslan Izmailov           | ML, Backend                             | Planning, Parsing Mechanism, Embeddings, Data  |
| Alisher Kabardiyadi       | Backend, DevOps                         | API Design, Unit/User Tests, Parsing Mechanism |
| Kira Strelnikova          | Frontend, Design                        | Figma Prototype, Analysis & Framework choosing |
| Ammar Meslmani            | Frontend, Design                        | Figma Prototype, Analysis & Framework choosing |


# Project Progress Report
## Week Summary

This week, our team held two pivotal meetings to solidify the project's foundation and refine our ongoing tasks. We've made significant strides in setting up our technical environment, developing initial models, and laying the groundwork for future developments.

### Meetings Overview

- **First Meeting**: Focused on establishing the technical stack and project architecture, which will underpin our development efforts.
- **Second Meeting**: Aimed at reviewing and adjusting our initial tasks and discussing the current progress with the project.

## Achievements

Here's a summary of our key accomplishments this week:

- **Research Notebook Template**: Created to ensure consistency and high quality across experiments.
- **Question Parsing Mechanism**: Developed a comprehensive mechanism for retrieving exam problems, which underwent multiple adjustments this week.
- **Word2Vec Implementation**: Successfully implemented and tested an initial embedding model using Word2Vec to analyze text data.
- **YaGPT API Exploration**: Engaged with the YaGPT API to evaluate inference quality, which highlighted some challenges.
- **Data Sourcing**: Researched and identified potential sources for existing exam problems to build our dataset.
- **Mentor Meeting**: Gained valuable insights and advice during our discussion, helping to steer our project direction.
- **GitHub Repository Setup**: Started and organized our code repository, ensuring clear documentation and structure with a README.md.
- **Figma Prototype**: Developed an initial draft prototype of our project on Figma to visualize the user interface.
- **API Design**: Drafted the initial API endpoints, planning for scalable and efficient data handling.

## Challenges and Solutions

### Insufficient Data Volume

- **Current Status**: The available dataset size is currently below our requirements for robust model training.
- **Solution**: Planned strategies to augment our dataset by including synthesized data and exploring additional data sources.

### Question Parsing Adjustments

- **Current Status**: The initial versions of our parsing mechanism required significant refinements to meet accuracy expectations.
- **Solution**: Iterated on the parsing algorithm, incorporating feedback from testing phases to enhance its reliability and accuracy.

### YaGPT API Performance

- **Current Status**: Encountered lower than expected test quality in initial trials with the YaGPT API.
- **Solution**: Engaged in parameter tuning and explored alternative model configurations to improve performance.

### Data Ethics Concerns

- **Current Status**: Addressed ethical considerations regarding the use of educational data.
- **Solution**: Implemented strict data handling protocols and initiated a review with our ethics board to ensure compliance.

## Lessons Learned

- The importance of iterative testing early in the development process to identify and address technical issues.
- Engaging with experts, such as our project mentor, provides critical insights that can significantly redirect our strategic approach.
- Ethical considerations must be integrated into the project's lifecycle from the start to avoid future complications.

## Next Steps

- Continue data augmentation strategies to build a comprehensive dataset.
- Further refine our parsing mechanisms based on upcoming test results.
- Enhance the integration and functionality of our API in preparation for deployment.