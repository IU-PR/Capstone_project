---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

Backend Tech Stack: Python, FastAPI, Aiogram, MongoDB, Beanie  
Frontend Tech Stack: React  
UX/UI Design: Figma  
DevOps: GitHub CI/CD
Deployment: Docker

- Python with FastAPI: Python, known for its versatility and large community support, combined with FastAPI's asynchronous nature, provides the necessary performance and real-time capabilities required for managing offline games.
- Aiogram: Asynchronous framework for integrating Telegram API, essential for authorization of game organizers and participants.
- MongoDB with Beanie: MongoDB's flexibility and scalability, combined with Beanie's asynchronous ODM for MongoDB, offer efficient data storage and interaction capabilities suitable for the application's requirements.
- React: React's popularity, flexibility, and component-based architecture make it a suitable choice for building a seamless and intuitive user interface for the application.  

### **Architecture Design**

1. **Component Breakdown**:  
Components:

   - Authorization in the system
     - Token creation
     - Token validation
   - Bridge
     - Game creation
     - Joining a game
       - Link generation
       - Navigating the link
   - Game
     - Preparing for the game
       - Preparing the players
       - Preparing game props
     - Game process
     - Game completion

2. **Data Management**:  
   We have determined that the web application will utilize MongoDB as the database solution. To work with MongoDB, we have chosen to use Beanie, a Python library that provides an intuitive interface for interacting with the database. We will organize data into collections, including 'users' and 'games'. This organization allows for efficient storage, retrieval, and manipulation of user and game data, contributing to a seamless and dynamic experience for managing offline team-building games.

   - User data: stores user information such as usernames, passwords, and other relevant details.
   - Game data: contains information that applies to all games and a separate place to store specific games' data.

3. **User Interface (UI) Design**:  
   Our team prioritizes UX/UI design principles to create an intuitive and user-friendly interface for our web application. We focus on simplicity, consistency, and usability to ensure a seamless user experience. Our Figma design incorporates effective information architecture, visual hierarchy, and intuitive navigation to enhance user satisfaction and promote efficient interaction.  

   Figma design: [Link](https://www.figma.com/design/qw7g4wyOzcCV0dF3UBWqIh/Rooma?node-id=0-1&t=dC2UpF3ilmBeeJh9-1)

   Wireframes:  
  
  ![img1](/2024/Rooma/image-1.png)
  Selecting a game from the list (e.g. Public Chat game)  

  ![img2](/2024/Rooma/image-2.png)
  Game customization  

  ![img3](/2024/Rooma/image-3.png)
  Participants joining the game (e.g. by QR code)  

  ![img4](/2024/Rooma/image-4.png)
  Process of the game

  ![img5](/2024/Rooma/image-5.png)
  When the game is over, the player statistics are displayed

4. **Integration and APIs**:  
   We will be integrating the Telegram API via Aiogram to encapsulate Telegram and manage the data flow. Additionally, the application will integrate with external AI APIs through separate modules, the specific AI APIs of which have not been determined yet.
   - Telegram API via Aiogram: The application leverages the Telegram API through the Aiogram framework. Aiogram fully encapsulates the Telegram integration and manages the data flow between the application and the Telegram platform. It provides a seamless and efficient way to interact with Telegram's features, such as sending messages, receiving updates, and managing user interactions.
   - External AI APIs: The application integrates with external AI APIs through separate modules. These modules facilitate the interaction between the application and various AI services. We can use these AI APIs for natural language processing, sentiment analysis, recommendation systems, or other AI-related functionalities that enhance the user experience and game management process.

5. **Scalability and Performance**:  
   - Server Cluster: The application utilizes a server cluster to handle increased traffic and ensure scalability. By distributing the workload across multiple servers, the application can accommodate a growing number of users and maintain optimal performance.
   - Nginx Access: Nginx will manage access to the server cluster. This web server acts as a reverse proxy, efficiently routing incoming requests to the appropriate server in the cluster, enhancing performance and load balancing.
   - MongoDB with Replication: The application leverages MongoDB with replication for data storage. Replication ensures data redundancy and availability by maintaining multiple copies of the data across multiple servers, improving scalability and fault tolerance.

6. **Security and Privacy**:  
   - Authorization via Telegram: The application utilizes Telegram's robust authorization system for user authentication. Leveraging Telegram's resources ensures a reliable and secure authentication process.
   - Database Protection: The application implements login and password authentication mechanisms to protect data. This process ensures that only authorized users can access and modify the database, enhancing data security and privacy.
   - DDOS Protection: Rate limiting implemented in Nginx will protect the system against Distributed Denial of Service (DDOS) attacks. This guard helps mitigate the risk of overwhelming the system with excessive requests and ensures its availability and performance.
   - Injection Prevention: The application employs Beanie to help avoid common injection vulnerabilities. The application can protect against potential security threats and ensure its integrity by utilizing Beanie.

7. **Error Handling and Resilience**:  
   - Monitoring with Prometheus and Grafana: The application employs Prometheus and Grafana for monitoring various metrics and system health. This data allows the team to proactively identify and address issues, ensuring the application's resilience and minimizing downtime.
   - Docker with Auto Restart: Docker is utilized in the application for containerization, providing isolation and portability. Additionally, we configure the app with auto restart functionality, which automatically restarts failed containers, allowing for quick recovery from failures and maintaining system availability.

8. **Deployment and DevOps**:  
   - CI/CD: The team has chosen to implement a Continuous Integration and Continuous Deployment (CI/CD) approach. This path allows for automated building, testing, and deployment of code changes, ensuring a streamlined and efficient development process.
   - Git: Our team uses Git for version control and collaboration. Git provides a structured and reliable way to track code changes, manage different branches, and facilitate seamless collaboration among team members.

### **Week 2 questionnaire:**

1) Tech Stack Resources: Our team prefers alternative resources over books. This choice is driven by the fact that they often provide more up-to-date information and can be learned faster. We can efficiently acquire the knowledge needed for our project by utilizing online documentation, tutorials, and forums.  

2) Mentorship Support: Considering the valuable tips our teacher assistant has provided to enhance our project, the team is contemplating leveraging his mentorship support. With his guidance, we aim to enhance our project's development and achieve greater success.  

3) Exploring Alternative Resources: Our team is exploring alternative resources to broaden our knowledge and gather diverse perspectives. We are leveraging the experience and expertise of team members, consulting documentation and video guides on YouTube, and utilizing platforms like Stack Overflow.  

4) Identifying Knowledge Gaps: Our team has limited experience in AI integration. We are reviewing information and addressing knowledge gaps to ensure a successful project with AI integration for matchmaking and chat moderation.  

5) Engaging with the Tech Community: Our team actively engages with the technology community through various channels to overcome implementation challenges. We collaborate within the team to leverage collective knowledge and experience. Also, some team members may ask for the guidance they need from their colleagues at work. In addition, we participate in forums and online communities where we can seek advice, share experiences, and learn from those who have faced similar challenges.  

6) Learning Objectives: Throughout this week, our team has been diving into our chosen technology stack. We've been actively seeking knowledge and guidance by exploring various online resources. Our main objective for this week was to gain a solid understanding of working with AI and how to integrate it into our project. Additionally, we've been investing time to familiarize ourselves with React, a prominent framework for front-end development.  

7) Sharing Knowledge with Peers: To promote sharing knowledge, we utilize a Telegram chat for real-time communication, hold team meetings for updates and discussions, and arrange separate meetings for front-end and back-end development teams to focus on specific areas.  

8) Leveraging AI: While our team has experienced contributors, we occasionally leverage AI to address knowledge gaps or obtain quick answers to specific questions related to AI. Additionally, we utilize AI to generate images for application design, enabling us to enhance visual elements. While human expertise remains our primary resource, AI serves as a valuable tool to complement and add to our capabilities.  

### **Tech Stack and Team Allocation**

| Team Member          | Track            | Responsibilities   |
|----------------------|------------------|--------------------|
| Vlad Bolshakov       | Backend          | Lead the team, monitor progress and set tasks, backend development |
| Dmitriy Okoneshnikov | Backend          | Backend development, Database design |
| Darya Koncheva       | Frontend         | Frontend development, game logic |
| Sofia Bakina         | Frontend, Design | Frontend development, UX/UI design, game logic |
| Azamat Bayramov      | Backend          | Backend development, Architecture design, DevOps |
| Anna Rylova          | Frontend, Design | Frontend development, UX/UI design, report writing |
| Sofya Ivanova        | Frontend         | Frontend development, report writing |

### **Weekly Progress Report**

This week, our team engaged in backend and frontend development of our application. In backend, our team focused on implementing crucial features, including system authorization, establishing a bridge, and integrating DevOps practices. On the frontend side, we made significant progress on components, including the main page of the app, the authorization page, and the page for adding participants to the game. We have completed the preliminary design of the application using Figma, providing a solid foundation for the visual aspects of our project. Furthermore, our team has completed the architecture of the web application. We meticulously designed and structured the framework and components to ensure scalability, efficiency, and maintainability.

### **Challenges & Solutions**

This week, our team encountered some challenges primarily related to front-end development. Initially, we had difficulties with configuring the project due to incompatibility with a specific library. To overcome this challenge, we had to explore alternative options and make the necessary configuration changes to ensure smooth functionality.
Furthermore, we identified that traditional CSS styling was time-consuming and cumbersome. To address this, we decided to switch to Tailwind CSS, which significantly accelerated our development process. The utility classes provided by Tailwind CSS enabled more efficient and streamlined styling of components.
Conversely, the backend development process was relatively straightforward, thanks to the expertise of our experienced team members who efficiently handled all backend-related tasks.

### **Conclusions & Next Steps**

Reflecting on the progress made this week, our team successfully tackled challenges related to front-end development and effectively managed back-end tasks. Due to our positive experience this week, we are confident in our ability to accomplish further objectives.
Looking ahead to the next week, our primary focus will be on completing pending work and finalizing the prototype. As part of this process, we plan to create additional pages for the web application, expanding its functionality and enhancing user experience. Moreover, we aim to implement a feedback collection to configure the AI responsible for delivering personalized recommendations and facilitating matchmaking.
In conclusion, the dedication and collaboration of our team members have contributed to a smooth workflow and significant advancements in our project. We look forward to building upon our project and continuing to push forward to our goals.
