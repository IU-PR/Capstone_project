---
weight: 2
bookFlatSection: true
title: "Week #2"
---

# **Week #2**

## **Choosing the Tech Stack, Designing the Architecture**

Welcome to Week 2 of our project! This week holds immense value as we delve into two critical aspects that will shape the trajectory of our software solution: selecting the appropriate tech stack and designing a robust architecture.

Choosing the right tech stack is essential for the success of our project. It empowers us to leverage the most suitable technologies, frameworks, and programming languages that align with our objectives and the expertise of our team members. By carefully evaluating scalability, performance, security, and development efficiency, we can ensure that our chosen tech stack provides a solid foundation for the development process.

Equally important is designing an architecture that not only meets our current requirements but also supports the long-term vision of our software solution. A well-thought-out architecture forms the backbone of our application, providing scalability, maintainability, and extensibility. This week, we will focus on defining the architecture by considering the component breakdown, data management, user interface design, integration with external systems, scalability, security, error handling, and deployment strategies.

As we proceed with these crucial tasks, let us bear in mind that the decisions we make in Week 2 will significantly impact our project's trajectory. Thoughtful consideration, collaboration, and thorough planning will pave the way for a successful and impactful software solution. Remember, we have a remarkable opportunity to demonstrate our skills, creativity, and problem-solving abilities as we craft a solution that surpasses expectations.

Throughout Week 2, we encourage open communication, sharing of ideas, and active collaboration within the team. Embrace this chance to learn from each other, leverage diverse perspectives, and foster an environment of innovation. Let us approach Week 2 with enthusiasm, dedication, and a shared commitment to creating a software solution that not only meets our project goals but also leaves a lasting impact in the domain we are targeting.

### **Tech Stack Selection**

Choosing the right tech stack is crucial for the successful execution of our project, LearnQuest. We need to evaluate the project's requirements and objectives to determine the most suitable technologies, frameworks, and programming languages. Factors such as scalability, performance, security, and the expertise of our team members should guide our decision-making process.

After careful consideration and discussions within our team, we have selected the following tech stack for LearnQuest:

**Next.js:** We have chosen Next.js as our frontend framework. It provides server-side rendering (SSR) capabilities, which will improve performance and SEO. Additionally, Next.js offers a smooth development experience and has excellent scalability features. 

**Django:** As our backend framework, we have selected Django, a high-level Python web framework. Django offers a robust and secure environment for building web applications. Its batteries-included approach provides built-in authentication, database ORM (Object-Relational Mapping), and a powerful admin interface.

**PostgreSQL:** As our database solution, we have chosen PostgreSQL, a powerful and widely used open-source relational database management system (RDBMS). PostgreSQL offers robust features, data integrity, and support for complex queries, making it suitable for our project's data management needs.

**Figma:** For design and collaboration purposes, we will utilize Figma. Figma is a powerful design tool that enables seamless collaboration among team members, facilitating efficient UI/UX design and prototyping.

Considering these technologies, we believe our chosen tech stack aligns well with the project's objectives and requirements. Next.js will provide a solid foundation for the frontend, while Django and PostgreSQL will handle the backend and data management effectively. Figma will support the design process and ensure a cohesive and visually appealing user interface.

Furthermore, our team members possess expertise in these technologies, which will contribute to efficient development and maintenance. Their familiarity with Next.js, Django, PostgreSQL, and Figma will facilitate a smoother workflow and faster development cycles.

As we move forward, we will continue to evaluate and refine our tech stack to ensure it remains optimal for the project's needs. We will also keep an eye on emerging technologies and industry best practices to stay up-to-date and leverage any advancements that can enhance our solution.

In conclusion, the selected tech stack comprising Next.js, Django, PostgreSQL, and Figma provides us with a solid foundation to develop LearnQuest. We are confident that these technologies, combined with our team's expertise, will enable us to deliver a high-quality and successful educational platform.

### **Architecture Design**

During the second week of our capstone project, we continued refining the architecture design for LearnQuest. Based on further evaluation and discussions, we have made an important adjustment to our tech stack. Instead of MongoDB, we have decided to use PostgreSQL as our database solution. This change was made considering the project's requirements and the benefits offered by PostgreSQL in terms of data management and scalability.

Here's an updated overview of the architecture design for LearnQuest:

1. **Component Breakdown**: We have identified the major components and modules that will form our software solution. The frontend component will be developed using Next.js, a popular React framework that provides server-side rendering and improved performance. The backend component will utilize Django, a powerful Python framework, for handling server-side logic and data processing. PostgreSQL will serve as the database management system to store and manage application data. Additionally, we will use Figma, a design tool, for UI/UX design and prototyping.

2. **Data Management**: PostgreSQL has been selected as our database solution. It is a powerful and widely used open-source relational database management system (RDBMS) known for its scalability, reliability, and extensive features. PostgreSQL's support for complex queries and data integrity aligns well with our project's data management needs.

3. **User Interface (UI) Design**: We have considered the user experience (UX) and design principles when planning the UI for LearnQuest. Wireframes and mockups have been created to visualize the layout and flow of our application. Figma will continue to be used as the design tool to create visually appealing and user-friendly interfaces.

4. **Integration and APIs**: While there are no specific integrations planned for this phase, we have designed our architecture to be easily extensible to accommodate future integrations. We will consider integrating external systems or APIs based on the project's requirements.

5. **Scalability and Performance**: Scalability and performance remain important considerations in our architecture design. Next.js, being a highly scalable framework, will help us handle increasing user loads efficiently. PostgreSQL's robustness and scalability will support our application's growing data volumes and ensure optimal performance.

6. **Security and Privacy**: To ensure the security and privacy of our application, we will incorporate appropriate security measures such as encryption. We will follow industry best practices to protect user data and safeguard against potential vulnerabilities.

7. **Error Handling and Resilience**: We have planned strategies for handling errors and exceptions to maintain a reliable and resilient application. Error logging and monitoring mechanisms will be implemented to track and diagnose issues. We will also focus on graceful error recovery to minimize disruptions for users.

8. **Deployment and DevOps**: We have considered the deployment process and DevOps practices aligned with our chosen tech stack. Automating deployment tasks using CI/CD pipelines and leveraging version control systems like Git will ensure efficient collaboration and a robust development workflow.

With this updated architecture design, we are confident that LearnQuest will be developed as a scalable, secure, and user-friendly educational platform. By utilizing Next.js for frontend development, PostgreSQL for data management, and Figma for design, we are leveraging technologies that align with our project's requirements. Our team's expertise in these technologies will contribute to a successful implementation.

## **Week 2 questionnaire:**  

1) Tech Stack Resources: 

    - We plan to utilize the following project-based books to help us build our project:

        - "Django for Beginners" by William S. Vincent - This book offers detailed, step-by-step instructions on preparing your application for deployment, configuring your web server, and successfully deploying it in a production environment. Additionally, it covers important topics such as security, scalability, and performance optimization.

        - "Full Stack React Projects" by Shama Hoque - While primarily focusing on the MERN stack, this book covers concepts applicable to our project. It provides guidance on building full-stack web applications using React.js and Node.js. By studying and adapting the book's concepts to our Django and Next.js tech stack, we aim to enhance our understanding of full-stack development and leverage modern technologies to create a dynamic and engaging website.

        - "Next.js Quick Start Guide: Server-Side Rendering Done Right" by Kirill Konshin - Although Next.js is primarily associated with React.js, this book focuses on Next.js specifically and its capabilities for server-side rendering. It covers topics like routing, data fetching, and deploying Next.js applications. By applying the principles from this book to our project, we expect to leverage Next.js effectively in combination with Django, enabling server-side rendering and providing a seamless user experience.


2) Mentorship Support: Currently, we don't have an official mentor for our project. However, we have a group of supportive friends who we can turn to for help. They possess knowledge and skills in relevant areas and are willing to provide guidance when needed. While they may not have extensive experience as formal mentors, their support can still positively impact the success of our project.

3) Exploring Alternative Resources: 

    -  In addition to project-based books, we have also explored various other resources to expand our understanding of our tech stack. These include:
        - "Django for Everybody" on Coursera: This course by Dr. Charles Severance covers the fundamentals of Django development, including working with models, views, templates, and deploying applications. The course also explores advanced topics like authentication, security, and handling forms.

        - "Next.js - The Complete Guide" on Udemy: This course by Maximilian Schwarzmüller provides a thorough overview of Next.js, including its features and advanced topics like authentication and API integration. 

        - Django’s Official Documentation.

4) Identifying Knowledge Gaps:
    - We will divide the work based on our skills. If we encounter problems, we will try to find solutions online. If that doesn't work, we will seek help from someone experienced in that area in our team. 

5) Engaging with the Tech Community: 

    - We actively look for solutions to problems that arise on websites and forums like StackOverFlow and Dev.to in order to increase the pace of development. 

6) Learning Objectives: Our learning objectives for this week are to:

    - Defining the architecture of the project
    - Decide an efficient and effective tech stack
    - Write some boilerplate code for the project to get up and running
    
    We will achieve these objectives by actively working on the project, collaborating as a team, and utilizing online resources for research and learning.


7) Sharing Knowledge with Peers: 

    We have regular meetings (as close to AGILE as possible) to stay informed about our project's progress. These interactions help us work together efficiently and ensure a solid understanding of our technologies as a team. Additionally, we share useful resources among ourselves, such as links to materials that may be helpful for our project.

8) Leveraging AI:
    - Live Doubt Resolution: Instructors can upload transcripts of their courses, which can be leveraged by AI plug-ins employing Large Language Model (LLM) techniques, such as GPT-3.5 to answer queries raised by the course takers.

### **Tech Stack and Team Allocation**

- After finalizing the tech stack and team allocation, we ensured that each team member was effectively assigned to appropriate tasks and responsibilities within the project. Here is a detailed explanation of how our project is structured, including the specific technologies being utilized and the corresponding team members responsible for each component:
    - Backend Development (Using Postgres and Django):
    	- Abu Huraira: Leads the backend development team, responsible for implementing database schema, configuring Postgres, and developing RESTful APIs using Django. 
    	- Wesam Naseer: Collaborates with Abu Huraira in backend development, focusing on implementing business logic, handling authentication and authorization, and optimizing database queries.
    - Frontend Development (Using Next.js):
    	- Laith Alebrahim: Works on frontend components, implements responsive design, and ensures cross-browser compatibility.
    	- Ali Mansour: Responsible for implementing frontend features, creating user interfaces, and ensuring a seamless user experience.
    	- Chibuoyim Ogbonna Faith Wilson: Supports the frontend team by assisting with frontend development tasks and contributing to the overall UI/UX improvement. 
   	 
- By dividing responsibilities in this manner, we ensure efficient collaboration and effective utilization of team members' expertise. The frontend team focuses on creating a visually appealing and user-friendly interface using Next.js, while the backend team handles the data management, APIs, and business logic using Postgres and Django. Regular communication and coordination among team members are maintained through meetings, calls, and online collaboration tools to ensure smooth progress and successful completion of the project.