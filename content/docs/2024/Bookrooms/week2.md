---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

Backend: Go

We've chosen Go as the foundation for our backend, driven by its strength in handling high-load services and its developer-friendly nature.  

- High-Performance and Scalability: Go is renowned for its ability to handle demanding workloads. Its concurrency features and efficient memory management make it an ideal choice for a service that will likely experience high traffic, especially during peak booking periods.

- Developer Productivity: Go's simple syntax and clear structure make development faster and more efficient. It provides a streamlined workflow that minimizes complexity and allows developers to focus on building robust and scalable functionality.

Database: PostgreSQL

Our database of choice is PostgreSQL, a mature and feature-rich SQL database that offers exceptional flexibility and performance:

- Advanced SQL Capabilities: PostgreSQL is widely recognized for its advanced SQL capabilities, providing robust data management and querying features. It's a reliable foundation for handling the complex data relationships involved in a room booking system.

- Object-Oriented Features: PostgreSQL stands out with its object-oriented features, allowing us to create custom data types tailored to the specific needs of our application. This flexibility empowers us to model our data more effectively and improve database efficiency.

- Performance and Scalability: PostgreSQL is known for its scalability and performance, capable of handling large volumes of data and complex queries with speed and reliability. 

Frontend: Vanilla JavaScript

For our frontend development, we've chosen to embrace the simplicity and flexibility of pure JavaScript.  We believe this framework-free approach offers several key advantages:

- Performance: By eliminating the overhead of additional dependencies, we achieve faster load times, creating a smoother experience for users.  This is especially important for a user interface that needs to be responsive, particularly when displaying the 3D campus model. 

- Maintainability:  A lean and focused codebase using plain JavaScript is easier to understand and maintain. This ensures the long-term stability and sustainability of the project.

- Compatibility:  Pure JavaScript enjoys widespread support across all modern browsers, minimizing the need for complex compatibility workarounds. This guarantees a consistent experience for users on different devices and platforms.

- Flexibility:  Directly working with core JavaScript gives us maximum control over the frontend implementation. We can tailor our code specifically to the project's needs and adapt to evolving requirements without being bound by framework limitations. 

3D Graphics: Three.js

For creating the 3D graphics, we've chosen JavaScript with the Three.js framework.  This strategic decision combines seamless integration with powerful capabilities:

- Easy Integration: Three.js works flawlessly with our JavaScript frontend, minimizing integration overhead and creating a cohesive development workflow.

- Necessary Tools: Three.js provides the tools we need to create the 3D campus model, and potentially other 3D elements in the future.

### **Architecture Design**

1. **Component Breakdown**:


User Management Module:

- Registration/Authentication: Handle user registration and authentication using Google SSO, including storing user information and handling password resets.

- User Roles: Define different user roles (Student, Faculty, Admin) and manage permissions accordingly.

- Contact Information: The profile information (email) can be used by users to communicate with each other.

Room Management Module:

- Room Data Storage:  Store room details (name, capacity, location, facilities, type) in the PostgreSQL database.

- Availability Management: Track room availability in real-time, considering existing bookings and room capacity. Use a time-based scheduling system to manage room availability.

- Room Visualization:  Use Three.js to create the interactive 3D model of the university, allowing users to easily identify room locations.

Booking Management Module:

- Booking Requests: Handle user booking requests, including date/time selection, room selection, and number of participants.

- Cancellation Handling: Allow users to cancel bookings within a specific timeframe and update room availability accordingly. 

Data Analytics Module:

- Usage Reporting:  Collect data on room bookings and usage to provide insights on room utilization and identify potential improvements.

2. **Data Management**: 

Database Schema: Design a relational database schema (using PostgreSQL) to store all data effectively. 

- Tables: Create tables for users, rooms, bookings, and potential other tables for room features, room types, and event categories.

- Relationships: Define relationships between tables (e.g., one-to-many relationship between users and bookings, many-to-many relationship between rooms and bookings). 

Data Validation: Implement data validation rules (e.g. ensure booking dates are valid, user inputs are correct) to maintain data integrity.

Query Optimization: Optimize database queries for efficient data retrieval, especially for room availability searches.

3. **User Interface (UI) Design**:

- Responsive Web Design:  Create a user-friendly and visually appealing web-based interface.

- 3D University Model: Use Three.js to create an interactive 3D model of the university campus that allows users to explore room locations visually.

- Room Search: Design a clear and intuitive search interface for users to easily find rooms based on criteria (time, room type, capacity, location). 

- Booking Flow: Create a streamlined booking process, allowing users to select rooms, specify booking times, and confirm their bookings.

![Design](/2024/Bookrooms/design.jpg "Design").

4. **Integration and APIs**:

- Google SSO Integration: Implement API calls to integrate with Google's SSO system for user authentication.

5. **Scalability and Performance**:

- Database Scalability:  Use PostgreSQL's features (e.g., indexes, database clustering, query optimization) to ensure the database can handle increasing user volume and booking requests.

6. **Security and Privacy**:

- Google SSO Security: Utilize the inherent security features of Google SSO to protect user information.

- Data Encryption: Encrypt sensitive user data (e.g., passwords, personal details) in transit and at rest.

- Authentication and Authorization:  Implement strong authentication and authorization controls to ensure only authorized users can access specific functionalities and data. 

7. **Error Handling and Resilience**:

- Error Logging: Implement comprehensive error logging mechanisms to track and analyze system errors and identify potential issues.

- User-Friendly Error Messages:  Provide clear and concise error messages to users in a way that is easy to understand and helps them troubleshoot problems.

- Exception Handling: Handle exceptions gracefully to prevent unexpected application crashes and ensure system stability. 


8. **Deployment and DevOps**:

- Deployment Strategies:  Choose a deployment strategy (e.g., continuous integration and delivery (CI/CD), infrastructure as code) for deploying and updating the system.

- Infrastructure Management:  Decide on the hosting environment (e.g., on-premises, cloud-based, hybrid).

- Monitoring and Logging: Implement monitoring tools to track system performance, identify potential bottlenecks, and ensure overall system health.

### **Week 2 questionnaire:**

1) Tech Stack Resources:

- Go: Go Documentation (https://golang.org/doc/)

- PostgreSQL: PostgreSQL Documentation (https://www.postgresql.org/docs/)

- JavaScript: JavaScript Documentation (https://developer.mozilla.org/en-US/docs/Web/JavaScript)

- Three.js: Three.js Documentation (https://threejs.org/docs/)

- Google SSO: Google Sign-In (https://developers.google.com/identity/sign-in/web) 

2) Mentorship Support:

- We plan to reach out to the University Development Department to discuss our project and seek their guidance. Additionally, we will connect with the previous year's team (Bookinng) for insights and advice. 

3) Exploring Alternative Resources:

- Open Source Projects: Explore relevant projects to learn from others' code.

- Books/Articles:  Refer to books/articles on chosen technologies.


4) Identifying Knowledge Gaps:

- 3D Web Development: We need to improve our understanding of WebGL and Three.js for creating and integrating 3D models in web applications.

- Frontend Pipeline: We need to strengthen our knowledge of efficient frontend development workflows, including build processes, testing, and code optimization. 

- Communication & Collaboration: We need to enhance our communication strategies, particularly around technical aspects and task management.

5) Engaging with the Tech Community:

Seek out mentors within the tech community: Platforms like Stack Overflow can help connect us with experienced developers.

6) Learning Objectives:

- Go Proficiency:  Master Go syntax, data structures, concurrency, best practices.

- JavaScript: Become proficient in core JavaScript concepts, asynchronous programming, and modern JavaScript features to build interactive and dynamic web interfaces.

- PostgreSQL Database Development:  Learn database design, queries, optimization.

- Google APIs Integration:  Familiarize yourself with Google SSO and Calendar API. 

- Three.js for Visualization:  Acquire skills in Three.js for 3D models and interactions.

7) Sharing Knowledge with Peers:

- We plan to share documentation between internal teams on how to interconnect services.

8) Leveraging AI:

- Code Completion Tools:  Utilize tools like ChatGPT.

### **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
| Ismagil Iskakov (Lead)    | Frontend/Design/3D modeling | • Overall project leadership and coordination. <br> • Guiding the design and visual direction of the user interface. <br> • Overseeing the development of the 3D campus model, including its integration with the frontend.• Managing team communication and workflow. |
| Mikhail Gladyshev            | Backend/Database | • Developing the backend API using Go. <br> • Designing and implementing the PostgreSQL database schema. <br> • Ensuring efficient and secure data management.  |
| Alexander Sevastyanov            | Frontend | • Assistance and RND in frontend |
| Vladislav Kishkovskiy           | Backend | • Assisting in backend API development using Go. <br> • Implementing specific API endpoints and logic for handling data requests. <br> • Working closely with Mikhail to ensure seamless data integration.  |
| Said Nurullin             | Reports | • Writing progress reports and other documentation. <br> • Communicating project updates to stakeholders. |
| Matvey Platonov | Frontend | • Building user interface components, including search, booking, and user profile features. <br> • Implementing the frontend logic for interactions with the backend API. <br> • Ensuring responsiveness and cross-browser compatibility. |
| Aleksandr Ryabov | Frontend/3D graphics | • Developing the 3D campus model using Three.js. <br> • Integrating the 3D model with the frontend user interface. <br> • Ensuring visual consistency and engaging interaction with the 3D environment. |

### **Weekly Progress Report**

This week, our team has made significant strides in laying the foundation for our room booking system. We've moved from concept to concrete plans, establishing a solid framework for future development. Here's a breakdown of our key accomplishments:

Architecture & Tech Stack:
- Conceptual Blueprint: We've meticulously designed the overall architecture of the system, outlining the key components and their interactions. This provides a clear roadmap for building a robust and scalable solution. 

- Tech Stack Selection: We've carefully chosen our technology stack, selecting Go for the backend, PostgreSQL for the database, and JavaScript with Three.js for the interactive 3D campus model. These technologies offer a powerful combination of performance, flexibility, and ease of development.

Development Environment & Collaboration:

- Dockerized Deployment: We've successfully deployed our initial backend and frontend code to a Docker container, creating a standardized and reproducible development environment for the team. This ensures consistency and ease of collaboration.

- Task Management & Collaboration: We've established GitLab as our platform for task management and code collaboration. We've defined roles, assigned tasks, and outlined a clear workflow for seamless team interaction.

Initial Prototyping and Visualization:

- 3D Model Prototyping: We've crafted a test 3D model using Blender, showcasing our ability to create an interactive and engaging visual representation of the university campus. This serves as a visual proof-of-concept and a starting point for future refinements.

- Simple Demo: We've built a basic demo integrating our 3D model with a simple user interface. This provides a tangible demonstration of the system's potential and allows for early user feedback.

### **Challenges & Solutions**

One of the primary challenges we face is the learning curve associated with new technologies. As a team, we're actively dedicating time to mastering Go, JavaScript, and Three.js. To overcome this challenge, we're:

- Leveraging Resources: We're utilizing online documentation, tutorials, and community forums to accelerate our learning process.

- Peer Learning: We're sharing knowledge within the team and learning from each other's experiences.

### **Conclusions & Next Steps**

Our initial work has laid a solid foundation. Now, we focus on building key functionalities and refining our approach:

1. 3D Rendering Structure:

- Exploring Separation: We'll decide if the 3D code should be in a separate repo, connected as a submodule to the frontend. This could improve modularity and reusability.

- Testing Interaction: We'll test interaction between UI and 3D to see if separating the code is beneficial. 

2. Site Layout:

- Basic Implementation: We'll create a basic layout mirroring our Figma design, providing a visual framework for the user interface.

3. Google SSO Integration:

- User Authentication Testing: We'll integrate Google SSO for testing user authentication workflow.

4. Advanced Database Schema:

- Robust Data Structure: We'll design a comprehensive database schema for rooms, users, bookings, and more.
