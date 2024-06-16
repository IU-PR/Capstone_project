---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

   Our project is powered by a streamlined tech stack featuring Python and FastAPI for backend development, complemented by React for frontend interfaces. Kubernetes serves as our robust container orchestration platform, ensuring scalable and efficient deployment of applications. Prometheus and Splunk enhance our monitoring capabilities, providing real-time insights into application performance and resource utilization.

### **Architecture Design**

1. **Component Breakdown**: 
* User Interface (UI): The front-end part where users interact with the system. This includes pages for registration, login, form submission, and displaying results.
* Authorization Service: Manages user authentication and authorization, communicating with the PostgreSQL database.
* PostgreSQL Database: Stores user information and other necessary data.
* Manifest Builder Service: Processes the form data and interacts with the Cluster Manager to create configuration files.
* Cluster Manager: Manages the Kubernetes cluster, takes into operations resources requested by user.
* Kubernetes cluster: Orchestration platform.
* Monitoring System: Utilizes Splunk/Prometheus to collect logs and metrics from the Kubernetes cluster.
* Grafana: Visualizes metrics collected by Splunk.


2. **Data Management**:
* Data is stored in a PostgreSQL database, including user credentials and application configurations.
* Logs and metrics from the user’s namespace are collected by Splunk and visualized in Grafana are stored in TSDB.

3. **User Interface (UI) Design**: 
* A responsive and intuitive UI that guides users through registration, login, form submission, and accessing their namespace metrics.
* Uses modern web technologies to ensure a smooth and efficient user experience.

4. **Integration and APIs**: 
* Authorization Service built with Python and FastAPI provides APIs for authentication and authorization.
* Kube-API communicate with k8s cluster.
* Manifest Builder Service exposes APIs to handle form submissions and interact with the Cluster Manager.
* Splunk APIs for collecting and sending metrics to Grafana.

5. **Scalability and Performance**:
* Efficient resource allocation within the cluster to maintain performance.

6. **Security and Privacy**:
* Secure authentication and authorization mechanisms via the Authorization Server.
* Data encryption in transit and at rest to protect user information.
* Isolated namespaces to ensure user applications and data are separated.

7. **Error Handling and Resilience**: 
* Using Kubernetes orchestration ensures that if any component fails, playbooks will automatically recover it.
* Monitoring both within and outside containers ensures we quickly detect and address any errors.
* We have Sentry that track errors and recieve alerts on code failures.

8. **Deployment and DevOps**: 
* CI/CD pipelines using GitLab CI/CD for automated build, testing and deployment.
* Continuous monitoring and logging via Prometheus for proactive issue resolution.



### **Week 2 questionnaire:**

1) Tech Stack Resources: 

   The project uses Python and FastAPI for backend services, Splunk/Prometheus for monitoring, React.js for frontend development, Kubernetes for container orchestration, PostgreSQL for database management, and Grafana for metrics visualization.

2) Exploring Alternative Resources: 
* During the planning phase, we considered using MongoDB for our database, but determined that PostgreSQL better suited our needs for structured data and complex queries.
* Initially, we attempted to use Graylog for monitoring, but its resources were not available in Russia, leading us to choose Splunk instead.

3) Identifying Knowledge Gaps: 

   The first week was dedicated to research in the areas that each team member would develop. During team meetings, our architect provided basic information about Kubernetes, ensuring everyone understood what we were working on.

4) Engaging with the Tech Community: 
* Our target audience is developers, so we conducted interviews with several developers to understand how useful our project will be and gather feedback.
* Contributing to open-source projects related to our tech stack.

5) Learning Objectives:
* Deepening knowledge in Kubernetes management.
* Enhancing skills in monitoring and observability using Splunk.
* Mastering CI/CD pipelines and automation.

6) Sharing Knowledge with Peers: 

   During team meetings, each member shares what they have worked on, what they have learned, and explains their work to the rest of the team. We have regular meeting where we review each other and share difficulties.

7) Leveraging AI: 

   Using AI tools like ChatGPT to ask questions during development, solving problems faster and gaining insights into complex issues.


### **Tech Stack and Team Allocation**

| Team Member              | Track    | Responsibilities   |
|--------------------------|----------|--------------------|
| Darya Tolmacheva         | Design   | Team coordination, project management, design, reports|
| Iskander Shamsutdinov    | Backend  | Infrastructure operations, k8s manifests constraction, CI/CD |
| Nikita Bagrov            | Backend  | Configuration of unified monitoring, vizualization of collected metrics |
| Saveliy Lekhtin          | Backend  | Supevizing development process, backlog grooming, architectural setup |
| Egor Salnikov            | Backend  | Development of core business-logic, management cluster entities |
| Egor Solodovnikov        | Backend  | Development of authorization services and role-based access control |
| Evgeniy Spiridonov       | Frontend | Development of user side (frontend), UI/UX enhancement |

### **Weekly Progress Report**

Our team made significant strides this week. We successfully claimed the designs for the main page and the login/registration pages, and have already implemented the main page as a frontend. Additionally, we deployed a PostgreSQL database, Prometheus, API services, and staging clusters. Every service is now monitored using Splunk and Grafana. We've initialized the project skeleton and begun developing the base business logic. Moreover, we've been concurrently working on product management and branding in other courses.

### **Challenges & Solutions**

Challenge: 
* Frequent re-deployments of monitoring due to issues with virtual machines used as nodes.

Solution: 
* Developed a playbook to automate the deployment process. This ensures that in case of an error with the monitoring machine connection, everything can be easily re-deployed.

Challenge: 
* Initially, the frontend entry point was set as the manifest builder, that is not logically correct.

Solution: 
* Realigned the frontend entry point to the cluster manager for better logical flow.

Challenge:
* We need load balancer to expose services inside k8s cluster, but it is very expensive.

Solution:
* Used virtual private network out of the box ready k8s operator for exposing services.

### **Conclusions & Next Steps**

This week marked significant advancements in both design and backend development, positioning us well for the next phases of development. Looking ahead, our priority is to finalize the remaining page designs for consistent user interaction. Simultaneously, completing the frontend implementation will bring our designs to life with a polished user interface. Setting up the cluster manager is critical for efficient infrastructure management and deployment. Continuing to develop the core business logic remains essential to enhance our product's functionality and prepare for future features. These steps will ensure we stay on course to meet our project objectives and deliver a robust solution for our users.