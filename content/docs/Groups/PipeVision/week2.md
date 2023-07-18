---
weight: 1
bookFlatSection: true
title: "Week 2 report"
---

# **Week #2**

### **Architecture Design**

Designing a robust and scalable architecture is crucial for the long-term success and maintainability of your software project. This week, focus on defining the architecture that will serve as the backbone of your application. Consider the following aspects:

1. **Component Breakdown**:
   Our application is divided into four main components:

- Frontend Interface: The frontend interface allows users to upload images and view recognition results. It communicates with the backend server to send and receive data.
- Backend Server: The backend server processes requests from the frontend, uses the trained neural network to process images, stores results in the database, and sends results back to the frontend.
  - Neural Network: The neural network is the heart of our system, responsible for recognizing pipeline markings in the images.
- Database: We're using PostgreSQL for storing recognition results, allowing users to view past results and providing a source of data for further improvement of the neural network.

2. **Data Management**:
   We will use a PostgreSQL database system to store and manage the recognition results. We will also utilize Python libraries such as SQLAlchemy for ORM-based database access, ensuring efficient and secure data transactions.

3. **User Interface (UI) Design**:
   ![UI design](/PipeVision/UIdesign.png "Design").

4. **Integration and APIs**:
   We will have APIs for communication with a model, FastAPI for frontend callings. Documentation of these APIs will be introduced in the document after its development.

5. **Scalability and Performance**:
   We will utilize university servers with CPU and GPU parts. This will ensure that our application can scale to handle increasing user loads. For improving performance, we'll employ efficient neural network models and optimize our database queries.

6. **Security and Privacy**:
   We will use proxing to secure development of our solution. Also, we are planning to use cookies for the login system. All passwords stored in database will be hashed. Tokens and cookies will be generated for each session and stored in local user storage to ensure current authentication of user. Tokens will expire in time to have better security.

7. **Error Handling and Resilience**:
   We will have a robust error handling and logging mechanism in place to ensure that our application can recover gracefully from unexpected issues. This will include error handling at the application level and the system level. Logging mechanism is based on React Auth kit library which has built-in feature for it.

8. **Deployment and DevOps**:
   We will use Git with feature branch workflow for version control, and GitHub actions for continuous integration, testing and deployment. These tools will help us automate the deployment process and maintain a robust development workflow.

## **Week 2 questionnaire:**

1. Tech Stack Resources: Are you utilizing any **project-based books** that specifically cover your tech stack and help you build your project? If yes, please provide the names of these books (name at least 3). How do you anticipate utilizing these materials to enhance your knowledge and expertise in your tech stack?

2. Mentorship Support: Do you currently have a mentor actively involved in your project? If yes, kindly share the name of your mentor and explain how their guidance has positively influenced your project. If you don't have a mentor yet, have you considered seeking one? How do you believe having a mentor could contribute to the success of your project? Remember, having an experienced mentor that can guide you and your team is your responsibility.

3. Exploring Alternative Resources: In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack? This could include online courses, video tutorials, documentation, or any other sources that have been valuable in filling knowledge gaps. Please, name at least 3 resources

4. Identifying Knowledge Gaps: Are there any specific areas within your tech stack where you or your team feel there are knowledge gaps or expertise is lacking? If so, how do you plan to address these gaps and ensure a well-rounded understanding of your chosen technologies? Please name the tech stack division in your team and outline how are you planning to deal with **knowledge gaps**

5. Engaging with the Tech Community: Have you actively engaged with the broader tech community to seek guidance or learn from experienced professionals in your tech stack? This could involve participating in online forums and groups (telegram, discord or any other platform), attending local meetups (Kazan, Innopolis)? Do you have means to engage experts into critical tech stack problems through professional networks?

6. Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week? How do you plan to achieve these objectives, and what strategies or resources will you employ to deepen your understanding?

7. Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates? Have you organized any knowledge-sharing sessions or discussions to facilitate the exchange of insights and experiences related to your tech stack?

8. How have you leveraged AI to compensate for any lacking expertise in your tech stack? Have you utilized AI-powered tools or platforms to expedite the process of acquiring knowledge and expertise in your tech stack?

### Answers

1. We are using the following resources:

   - "Python Machine Learning" by Sebastian Raschka
   - "Clean code" by Martin Robert
   - "Full Stack React" by Anthony Accomazzo

   These books provide in-depth knowledge on our tech stack and will help us in building our project.

2. Our first mentor is Rinat Mullakhmetov, master student from Innopolis University. He is an ML engineer at VTB with great experience at Computer Vision. His guidance in project planning and technical advice has greatly helped in shaping our project. The second one is Mikhail Moshchanetskiy, Robotics master student from Innopolis University. His experience is useful for testing hypothesis and CV development.
3. We have utilized online resources such as OpenCV and React documentation, YouTube tutorials on PostgreSQL and SQLAlchemy, Stack Overflow to solve some problems with code.
4. Our team identified gaps in knowledge about Computer Vision and React best practices. We plan to address these through targeted learning and mentorship.
5. We are engaged with the Gazstroyprom tech community and learn from their professionals. They organize daily meetings with teams working for them, and we share progress of work and tech problems.
6. Our objective for this week is to study OpenCV and start working on the backend server. We plan to achieve these objectives through focused team work and utilizing our resources. Now part of our team is reading articles about CV and searching for similar projects in GitHub.
7. We have organized weekly knowledge sharing sessions where team members share their learnings about the tech stack and work progress.
8. We are using AI for image recognition, which is a major part of our tech stack.

### **Tech Stack and Team Allocation**

We discussed tech stack, tech elective, wishes of each team member. Then we separated tasks for our project and their difficulty. At the end of this discussion, we decided to assign roles correspondingly.

- Frontend (TypeScript, React): Guzel Zakirova and Anastasia Barabanova are responsible for developing the user interface. They are responsible for implementing the layout and user flows according to our UI design.
- Backend (Python): Amirlan Sharipov and Anastasia Smirnova are tasked with developing the server-side logic. They will work on processing the requests, handling the communication with the neural network and the database, and ensuring the performance and security of the server.
- Database (PostgreSQL): Egor Zavrazhnov is our database engineer. He will design the database schema, manage data storage, and ensure efficient data transactions.
- Neural Network (OpenCV): Yakov Dementyev, Darina Merzakreeva, Rinat Mullakhmetov and Mihail Moshchanetsky are in charge of the neural network. Their responsibility includes designing, training, and testing the neural network model to ensure its accuracy and efficiency in recognizing pipeline markings.

We understood that the CV part of our project is the most difficult and time consuming. So, Rinat will manage a group of four people to achieve results more efficiently.

Anastasia Barabanova was chosen to manage other parts of development, communicate with the team and our customer.

{{< hint danger >}}
**Feedback**

The report is generally good. I felt that you need to provide more details in the first section especially in 6, 7 and 8.

Grade 4.5/5

_Feedback by Moofiy_
{{< /hint >}}
