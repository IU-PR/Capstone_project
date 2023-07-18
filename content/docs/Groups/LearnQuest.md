---
weight: 1
bookFlatSection: true
title: "LearnQuest"
---


{{< embed-pdf url="/LearnQuest/Final_Presentation.pdf" >}}

### [The Application 🔗 in action](https://learnquest.vercel.app)

### [API specification 🔗 in action](https://learnquest-backend.vercel.app) 

![Landing page](https://i.ibb.co/4N06RyW/image.png)

{{< expand "Week 1 Report" >}}


# **Week 1**

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member                       | Telegram ID                                       | Email Address                      |
|-----------------------------------|---------------------------------------------------|------------------------------------|
| Abu Huraira (Lead)                | [@huraira](https://t.me/huraira)                  | a.huraira@innopolis.university     |
| Wesam Naseer                      | [@W_Naseer](https://t.me/W_Naseer)                | w.naseer@innopolis.university      |
| Chibuoyim Ogbonna Faith Wilson    | [@willithemenace](https://t.me/willithemenace)    | c.ogbonna@innopolis.university     |
| Laith Alebrahim                   | [@friday234](https://t.me/friday234)              | l.alebrahim@innopolis.university   |
| Ali Mansour                       | [@XmtossX](https://t.me/XmtossX)                  | a.mansour@innopolis.university     |


### **Value Proposition**

- **The Problem:**
Limited access to quality education, high costs, and inflexible schedules restrict individuals from pursuing further learning and personal development. Traditional educational systems often come with barriers, such as financial constraints, limited availability, and rigid schedules, which hinder educational opportunities for many.

- **Solution Description:**
LearnQuest provides a global platform that offers a wide range of courses on various subjects, making education accessible to individuals who may not have access to traditional educational institutions or who prefer flexible learning options. 

- **Benefits to Users:**
    - Access to high-quality educational content
    - Flexible and convenient learning options
    - Cost savings on educational expenses
    - Collaborative learning with other users  
    - Opportunities for lifelong learning to stay up to date with the latest trends and technologies

- **Differentiation:**
    - Focus on innovative and emerging technologies
    - User-friendly interface and multimedia resources
    - Collaborative learning opportunities
    - Engaging and effective educational experience

- **User Impact:**
    - LearnQuest fosters innovation by empowering users with tools and knowledge to create new solutions. 
    - LearnQuest democratizes education by increasing accessibility and affordability for a wider audience. 
    - By providing users with the knowledge and skills they need to excel in their jobs, LearnQuest can help to improve overall job performance and productivity, leading to better outcomes for organizations and industries as a whole. 

- **User Testimonials or Use Cases:** 
    - Individuals seeking to develop new skills or enhance their existing knowledge can benefit from the wide variety of courses available on our platform
    - LearnQuest can be used by professionals who are seeking to stay up-to-date with the latest trends and developments in their fields in order to maintain their certifications or licenses

## **Lean Startup Questionnaire**
1. The problem or need our software project addresses:
    - The software project addresses the problem of limited access to quality education and high costs by providing a cheaper and accessible platform for open online courses, catering to the needs of students and anyone who wants to learn.

2. Our target users or customers:
    - Individual learners
    - Working professionals
    - Entrepreneurs and business owners
    - Instructors and experts

3. How we will validate and test our assumptions about the project:
    - Conducting surveys, interviews, and user testing with a diverse group of users
    - Including students from different educational backgrounds and individuals with varying learning needs.

4. Metrics we will use to measure the success of your project:
    - User feedback and reviews
    - Course ratings and engagement metrics
    - A/B testing and experimentation

5. How we plan to iterate and pivot if necessary based on user feedback: 
    - Based on user feedback, the plan is to actively listen and analyze feedback from diverse users. This feedback will guide iterations and pivots in the project, ensuring the platform evolves to meet the needs of students and other learners effectively. Regular updates, improvements in course offerings, and enhancements to the user experience will be made based on user feedback.
    - Regarding the methodologies to be used, Agile has been selected as the preferable and effective one to handle the dynamic and fast-paced development process:
    ![Agile Approach](/LearnQuest/agile-approach.svg)

## **Leveraging AI, Open-Source, and Experts**
Our plan includes using the following solutions and resources to speed up the process of development

- AI: We plan to integrate GPT-3.5 to answer course specific questions of enrolled students. 
- Open-Source: [Python](https://python.org), [Django](https://docs.djangoproject.com/en/4.2/) docs
- Experts in relevant domains: Professors, academics at the university, and software engineers in order to follow best practices.

## **LearnQuest's Vision**
- **Overview:**
LearnQuest will provide high-quality course materials. The platform offers flexible and convenient learning options that fit into busy schedules and promote lifelong learning. LearnQuest aims to enhance users' productivity, efficiency, and effectiveness by providing relevant course materials.

- **Schematic Drawings:** 
The Object Model of the platform will look something like this: 
![The Object Model of LearnQuest](/LearnQuest/the-object-model.svg)

- **Tech Stack:**
We plan to use the following technologies/frameworks, but they are subject to change:
    - Django
    - PostgreSQL
    - Next.js
    - HTML
    - CSS
    - Bootstrap

- **Anticipating Future Problems:**
Challenges such as technical complexities, resource limitations, time constraints, user adoption, and security/privacy issues may arise during the development and deployment of LearnQuest. To mitigate these challenges, we'll prioritize agile development, regular testing, and effective communication.

- **Elaborate Explanations:**
LearnQuest will be similar to the project by MIT (called MITOCW) and will include a user interface for browsing and searching courses, a detailed course catalog, and multimedia resources like videos, animations, and interactive exercises. Collaborative learning tools like discussion forums and peer review systems will facilitate teamwork and knowledge sharing. LearnQuest aims to provide an engaging educational experience that promotes lifelong learning and enhances productivity.

{{< /expand >}}

{{< expand "Week 2 Report" >}}

# **Week 2**

## **Choosing the Tech Stack, Designing the Architecture**

Welcome to Week 2 of our project! This week holds immense value as we delve into two critical aspects that will shape the trajectory of our software solution: selecting the appropriate tech stack and designing a robust architecture.

### **Tech Stack Selection**

Choosing the right tech stack is crucial for the successful execution of our project, LearnQuest. We need to evaluate the project's requirements and objectives to determine the most suitable technologies, frameworks, and programming languages. Factors such as scalability, performance, security, and the expertise of our team members should guide our decision-making process.

After careful consideration and discussions within our team, we have selected the following tech stack for LearnQuest:

**Next.js:** We have chosen Next.js as our frontend framework. It provides server-side rendering (SSR) capabilities, which will improve performance and SEO. 

**Django:** As our backend framework, we have selected Django, a high-level Python web framework. Django offers a robust and secure environment for building web applications. Its batteries-included approach provides built-in authentication, database ORM (Object-Relational Mapping), and a powerful admin interface.

**PostgreSQL:** As our database solution, we have chosen PostgreSQL, a powerful and widely used open-source relational database management system (RDBMS). PostgreSQL offers robust features, data integrity, and support for complex queries, making it suitable for our project's data management needs.

**Figma:** For design and collaboration purposes, we will utilize Figma. Figma is a powerful design tool that enables seamless collaboration among team members, facilitating efficient UI/UX design and prototyping.

### **Architecture Design**

During the second week of our capstone project, we continued refining the architecture design for LearnQuest. Based on further evaluation and discussions, we have made an important adjustment to our tech stack. Instead of MongoDB, we have decided to use PostgreSQL as our database solution. This change was made considering the project's requirements and the benefits offered by PostgreSQL in terms of data management and scalability.

Here's an updated overview of the architecture design for LearnQuest:

1. **Component Breakdown**: We have identified the major components and modules that will form our software solution. The frontend component will be developed using Next.js, a popular React framework that provides server-side rendering and improved performance. The backend component will utilize Django, a powerful Python framework, for handling server-side logic and data processing. PostgreSQL will serve as the database management system to store and manage application data. Additionally, we will use Figma, a design tool, for UI/UX design and prototyping.

2. **Data Management**: PostgreSQL has been selected as our database solution. It is a powerful and widely used open-source relational database management system (RDBMS) known for its scalability, reliability, and extensive features. PostgreSQL's support for complex queries and data integrity aligns well with our project's data management needs.

3. **User Interface (UI) Design**: We have considered the user experience (UX) and design principles when planning the UI for LearnQuest. Wireframes and mockups have been created to visualize the layout and flow of our application. Figma will continue to be used as the design tool to create visually appealing and user-friendly interfaces.

4. **Integration and APIs**: While there are no specific integrations planned for this phase, we have designed our architecture to be easily extensible to accommodate future integrations. We will consider integrating external systems or APIs based on the project's requirements.

5. **Scalability and Performance**: Scalability and performance remain important considerations in our architecture design. Next.js, being a highly scalable framework, will help us handle increasing user loads efficiently. PostgreSQL's robustness and scalability will support our application's growing data volumes and ensure optimal performance.

6. **Security and Privacy**: Token based authorization to prevent access to locked pages

7. **Error Handling and Resilience**: Testing using Pytest

8. **Deployment and DevOps**: Docker, Vercel, GitHub Integration, etc. 

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
    	- Ali Mansour: Responsible for implementing frontend features, creating user interfaces, and ensuring a seamless user experience.
    	- Laith Alebrahim: Works on frontend components, implements responsive design, and ensures cross-browser compatibility.
    	- Chibuoyim Ogbonna Faith Wilson: Supports the frontend team by assisting with frontend development tasks and contributing to the overall UI/UX improvement. 
   	 
- By dividing responsibilities in this manner, we ensure efficient collaboration and effective utilization of team members' expertise. The frontend team focuses on creating a visually appealing and user-friendly interface using Next.js, while the backend team handles the data management, APIs, and business logic using Postgres and Django. Regular communication and coordination among team members are maintained through meetings, calls, and online collaboration tools to ensure smooth progress and successful completion of the project.

{{< /expand >}}

{{< expand "Week 3 Report" >}}

# **Week 3**

## **Developing the first prototype, creating the priority list**

## **Progress report**:

- **Prototype Features**: 
- The project is available on [GitHub](https://github.com/abuwho/LearnQuest). All instructions to run the application have been included in the `README` files for frontend and backend. 

- **Backend**: 
- The endpoints that have been implemented using Django/Python: 
    - Authentication endpoints
        ![Authentication endpoints](/LearnQuest/authentication-endpoints.png)
    - Courses endpoints
        ![Courses endpoints](/LearnQuest/courses-endpoints.png)

 - **User Interface**: 
 - **Frontend**: 
- A list of components and pages that have been developed
    - Logo ![Logo](/LearnQuest/logo.svg)
    - Register ![Register page demo](/LearnQuest/register-demo.jpg)
    - Sign in ![Sign in page demo](/LearnQuest/sign-in-demo.jpg)
    - Landing ![Landing page demo](/LearnQuest/landing-page-demo.png)
    - Courses ![Courses page demo](/LearnQuest/courses-demo.jpg)
    - Checkout ![Checkout page demo](/LearnQuest/checkout-demo.jpg)
    - Reviews ![Reviews page demo](/LearnQuest/reviews-demo.jpg)
    - Lessons ![Lessons page demo](/LearnQuest/lessons-demo.jpg)
    - Newsletter ![Newsletter page demo](/LearnQuest/newsletter-demo.jpg)

 - **Challenges and Solutions**: 
 - Confusions regarding the switch between `sqlite` to `PostGres` from development to production. We decided that we are going to fix it by using `sqlite` in the development environment (which is used by default on Django) and later we will use `Postgres` in deployment. 
 - We had some difficulties in building components in Next.js/React.js. However, we solved it by getting help online. 

- **Next Steps**: 
- Implement more endpoints for applications such as User Profiles, Cart, Checkout, etc. 
- Implement testing in backend
- Making sure the frontend and backend integrations are more seamless. 
- Implement GitHub's build tools to effectively monitor successful deploying. 

{{< /expand >}}

{{< expand "Week 4 Report" >}}

# **Week 4**

Welcome to Week 4 of our Capstone Project! This week is dedicated to the crucial phases of testing, feedback integration, and continuous iteration.

## **Progress report**  

## **External Feedback**
We have received feedback from a survey based on our first prototype in dev environment [here](https://docs.google.com/forms/d/e/1FAIpQLSe4_dGe32kgBBy1LTaD1mpZg3FaW119kB_nNCoxNZNY8eOW3g/viewform). 

The responses we received are displayed below: 

1. ![Result 1](/LearnQuest/survey-result-1.png)
2. ![Result 2](/LearnQuest/survey-result-2.png)
3. ![Result 3](/LearnQuest/survey-result-3.png)
4. ![Result 4](/LearnQuest/survey-result-4.png)
5. ![Result 5](/LearnQuest/survey-result-5.png)
6. ![Result 6](/LearnQuest/survey-result-6.png)

## **Testing**

We have written unit tests for testing our Models, Serializers and Utility Functions in the Django backend. The tests can be viewed on [GitHub repo](https://github.com/abuwho/LearnQuest).

Also, we have conducted end-to-end testing for our API endpoints using [drf-yasj](https://drf-yasg.readthedocs.io/en/stable/readme.html). It helped us identify potential loopholes in the backend request-response model, related to authentication and HTTP response codes. Moreover, it helped us test the robustness of our backend. 

Furthermore, we have conducted end-to-end testing for the frontend components and make relevant changes based on any potentially broken components in the UI. 

During the testing process, we tried to follow the [TDD](https://en.wikipedia.org/wiki/Test-driven_development) guidelines. 


## **Iteration**

Based on the feedback received from the [survey](https://docs.google.com/forms/d/e/1FAIpQLSe4_dGe32kgBBy1LTaD1mpZg3FaW119kB_nNCoxNZNY8eOW3g/viewform), we have added some features to develop after the release of our MVP by the end of the course. 

Key features include: 
1. Adding Russian payment gateways such as (Mir, Yoomoney, SberPay, etc.)
2. Feature to gift a course to a friend
3. Free trial

However, it is important to note that abovementioned features will be implemented after the release of the MVP for future iterations. 


{{< /expand >}}

{{< expand "Week 5 Report" >}}


# **Week 5**

Welcome to Week 5 of our Capstone Project! 

- The first and the foremost part of our development efforts of the solution is the implementation of necessary changes. In this case, we refactored our business logic, polished it, and dockerized our backend service for easier setup. Along this process, we also made sure to fix logical faults in our application so the business logic is implemented correctly. The code repository can be found on [GitHub](https://github.com/abuwho/LearnQuest).

- Regarding stakeholders: we came up with the idea of the capstone project on our own. Therefore, there is not an existing stakeholder for this project as for business. However, we are keen on collaborating with people experienced/interested in Product Analysis, Product Management, and UX Research. 

- Regarding analytics: As our application is currently running on our development server, we do not have an analytics collection system in place. Also, it hasn't been planned by our team to make this solution as a business solution in the market. Therefore, the necessity of creating analytics functionalities has been downplayed. 

- Future potential UX Research: At the moment, our web application has core functionalities such as authentication, CRUD operations on existing entities, such as Profile, User, Course, CourseEnrollment, Lesson, Review, InstructorApplication, Wallet, Cart. These functionalities offered with a user-friendly interface should be enough for a user for successful interaction. However, based on User Experience (UX) Research, we are open to enhance the usefulness of our application even more in the future. Just like the feedback we had received on our prototype on 3rd week, these tools (like user interviews and surveys) will keep on helping us in improvement the experience of the users. It is important to note that creation of UX research from the point of view of product management requires at least 2 weeks. As a result, we have decided it would be a good idea to present our findings in the end of the project if time allows it. This procedure has been included in our backlog. 

- As for documentation of feedback, we have the data available in the form of Google sheets for the feedback we have received from early testers of our application, which can be viewed [here](https://docs.google.com/spreadsheets/d/1XDbv9b7W85yxISFLbOUFtVZne6LUJuX-/edit?usp=sharing).

- Feedback analyzing has been tricky because the responses we have received in a early stage of the product has a relatively small sample size (n = 27). For this reason, we did not find too many recurring issues in our implementation. 

- For prioritizing our tasks, we paid attention to the scope of the product at the MVP stage. In this regard, we have tried to follow the impact/effort matrix, as shown below: 
![Impact Effort Matrix](/LearnQuest/impact-effort-matrix.png)
Following this method has helped us prioritize in a short-term project. 



{{< expand "Week 5 Report" >}}


# **Week 6**

Welcome to Week 6 of our Capstone Project! 

This week we have polished up our application and fixed bugs. Also, we have deployed our [application](https://learnquest.vercel.app) and [API](https://learnquest-backend.vercel.app) on Vercel. 

{{< /expand >}}