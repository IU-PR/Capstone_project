---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

The selection of Golang and gRPC for both the backend server and client components of Semargl C2 ensures a highly efficient and scalable system. Golang is known for its performance, concurrency support, and ease of deployment, making it an ideal choice for a command-and-control server that requires reliability and speed. gRPC, with its strong typing and performance optimizations, facilitates seamless communication between the server and clients, which is crucial for real-time command execution and data transfer. The choice of C and WinAPI for the agent component leverages the low-level access and efficiency of C, which is essential for interacting with the Windows operating system and performing tasks stealthily. Client UI will be built with Golang and Weils.

### **Architecture Design**

1. **Component Breakdown**:

   - **Server (Backend)**: Manages command dispatch, data aggregation, and overall orchestration of the C2 framework.
   - **Client**: Interfaces with the server to receive commands and send back data or status updates.
   - **Agent**: Deployed on target machines, executing commands received from the client, collecting data, and ensuring covert operations.

2. **Data Management**:

   - Use a relational database (e.g., PostgreSQL) for structured data storage, such as logs, command results, and configuration settings.
   - Implement encryption for data at rest and in transit to ensure confidentiality and integrity.

3. **User Interface (UI) Design**:

   - Create CLI interface for ease integration and development
   - Create a GUI interface for collaboration and easy use

4. **Integration and APIs**:

   - Implement gRPC services for internal communication between components, ensuring efficient and reliable data exchange.
   - Support for third-party integrations, such as SIEM systems, threat intelligence feeds, and incident response platforms.

5. **Scalability and Performance**:

   - Utilize Kubernetes for container orchestration, allowing for easy scaling of server and client components.
   - Implement load balancing and auto-scaling policies to handle varying loads and ensure high availability.
   - Optimize gRPC performance with features like connection pooling, and efficient serialization/deserialization methods.

6. **Security and Privacy**:

   - Ensure end-to-end encryption using TLS for all communications between server, client, and agents.
   - Implement robust authentication and authorization mechanisms, including multi-factor authentication (MFA) for users.

7. **Error Handling and Resilience**:

   - Design the system with fault tolerance in mind, using retry mechanisms and circuit breakers to handle transient errors.
   - Implement comprehensive logging and monitoring to quickly detect and diagnose issues.

8. **Deployment and DevOps**:
   - Utilize Ansible for automated deployment and configuration management, ensuring consistent and repeatable setups.
   - Adopt CI/CD pipelines using GitHub Actions to streamline the development and deployment process.

### **Week 2 questionnaire:**

1. **Tech Stack Resources:**

   - **Backend (Server):**
     - **Golang:** Explore resources like the official [Go documentation](https://golang.org/doc/), and books like "The Go Programming Language" by Alan Donovan & Brian Kernighan.
     - **gRPC:** Utilize the [gRPC documentation](https://grpc.io/docs/), and the official [gRPC-Go GitHub repository](https://github.com/grpc/grpc-go) for examples and best practices.
   - **Client:**
     - **Golang:** Same resources as the backend. Additionally, the Go Forum and Golang Slack can be helpful communities.
     - **gRPC:** Same resources as the backend.
   - **Agent:**
     - **C:** Resources include "The C Programming Language" by Kernighan and Ritchie, and websites like [GeeksforGeeks](https://www.geeksforgeeks.org/c-programming-language/) and [TutorialsPoint](https://www.tutorialspoint.com/cprogramming/index.htm).
     - **WinAPI:** Utilize Microsoft's [Windows API documentation](https://docs.microsoft.com/en-us/windows/win32/api/index) and resources like "Programming Windows" by Charles Petzold.

2. **Mentorship Support:**
   Consulations with Information Security Experts from Security Experts Community revealed us important points that should be considered during impelementation. This points include:

   - Legal and Licensing
   - "Defanged" mode for awareness checking

3. **Exploring Alternative Resources:**

4. **Identifying Knowledge Gaps:**
   After alternative resource analysis, we found several knowledge gaps:

   - Understanding of obscure process injection techniques
   - Lack of experience in working with desktop applications in Golang

5. **Engaging with the Tech Community:**

We are using our project on cyber-ranges and consult with experts to gain technical knowledge and deeper understanding.

6. **Learning Objectives:**

   - Achieve proficiency in Golang, gRPC, and C programming by completing small projects and exercises.
   - Understand the architecture and deployment of a command-and-control server using Docker and Ansible.
   - Familiarize with MITRE ATT&CK framework and its application in generating security assessment reports.

7. **Sharing Knowledge with Peers:**
   We conduct regular knowledge-sharing sessions and workshops within our team. We created documentation to help team members and contributors quickly find information and resources. Our documentation is available on: (https://arturlukianov.github.io/semargl/)[https://arturlukianov.github.io/semargl/]

8. **Leveraging AI:**
   Explored AI-driven code review tools to improve code quality and catch potential issues early. We use GigaCode and Copilot for test generation.
   LLMs like ChatGPT and LLaMa will be used to create descriptive paragraphs for MITRE techniques and other technical information to make it more understandable for buisness.

### **Tech Stack and Team Allocation**

| Team Member           | Track             | Responsibilities                          |
| --------------------- | ----------------- | ----------------------------------------- |
| Artur Lukianov (Lead) | Server and Client | Developing server and client, gRPC design |
| Alexander Efremov     | Agent and Modules | Developing agent in C with WinAPI         |
| Vadim Yarullin        | Agent and Modules | Developing agent in C with WinAPI         |
| Andrew Boronin        | DevOps            | Docker, Ansible, CI/CD                    |
| Alexander Tomashov    | UI Client         | Design and implement UI for client        |
| Nika Ckekhonina       | UI Client         | Design and implement UI for client        |
| Viktoria Patrina      | UI Client         | Design and implement UI for client        |

### **Weekly Progress Report**

Our team defined responsibilities of each member and uploaded code with basic functionality. Currently functionality includes:

- Server implementation
- Client implementation
- TCP listeners
- Agent beacon
- Upload file to agent
- Download file from agent
- File system operations (cd, ls, cat, pwd)
- Execute process functionality (without output)

We implemented a CI/CD pipeline to create releases of server and client. Video of current state of our project:
{{< youtube LtkTzyXHPWo >}}

### **Challenges & Solutions**

Ensuring Secure and Reliable Communication with gRPC

Solution: Follow best practices for secure gRPC implementation, such as using SSL/TLS for encryption. Regularly review and update your codebase to incorporate the latest security patches and improvements. Utilize automated testing frameworks to ensure communication reliability.

Challenge: Integration of Multi-Language Agents

Solution: Establish a standardized protocol for communication between the C2 server and agents, regardless of the language they are written in. Develop thorough documentation and examples for each type of agent to ensure consistent implementation and integration.

Challenge: Deployment and Scalability

Solution: Use Docker to containerize the server, client, and agents for easier deployment and scalability. Leverage orchestration tools like Kubernetes to manage the deployment of containers at scale. Implement CI/CD pipelines to automate the deployment process.

Challenge: Keeping Up with MITRE ATT&CK Framework Updates

Solution: Assign a team member to monitor updates to the MITRE ATT&CK framework and disseminate relevant changes to the team. Regularly review and update your reporting mechanisms to align with the latest framework techniques and tactics.

### **Conclusions & Next Steps**

**Conclusions:**

We defined the following key principles:

1. **Comprehensive Learning and Support Systems are Key**
2. **Security and Reliability Must Be Prioritized**
3. **Standardization and Documentation**
4. **Effective Deployment and Scalability**
5. **Continuous Learning and Knowledge Sharing**
6. **Alignment with Industry Standards**

We implemented a basement for our project and now will refine and polish it to match the functional defined.

**Next Steps:**

1. **Set Up Secure Communication Channels:** Ensure that gRPC communication is secure by implementing SSL/TLS and other best practices.
2. **Standardize Protocols for Multi-Language Agents:** Create detailed documentation and examples to facilitate the integration of agents written in different languages.
3. **Deploy Using Docker and Kubernetes:** Containerize all components and set up orchestration for scalable and efficient deployment.
4. **Monitor and Update MITRE ATT&CK Integration:** Assign a team member to keep track of updates to the framework and ensure that your reports and tools are aligned with the latest techniques and tactics.
5. **Integrate AI Tools:** Explore and integrate AI tools into your development and learning workflows to enhance productivity and learning outcomes.
6. **Implement database for server:** Impelement a database on server to store agents, listeners, credentials and loot
7. **Implement process injection and modules for agent**
8. **Implement basic UI for Desktop UI**
