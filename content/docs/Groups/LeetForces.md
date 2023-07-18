# **LeetForces**



Hi! We a group called "LeetForces" and we do the `LeetForces` project.

{{< embed-pdf url="/LeetForcesResources/LeetForces.pdf" >}}

# **Weekly reports**



{{< expand "Week 1 report" >}}



## **Team Formation and Project Proposal**





### **Team Members**



| Team Member            | Telegram ID   | Email Address       |

|------------------------|---------------|---------------------|

| Anton Nekhaev          | @anekhaev | a.nekhaev@innopolis.university     |

| Alexander Buchnev      | @pwn0id | a.buchnev@innopolis.university     |

| Vladislav Danshov      | @vladislav_danshov | v.danshov@innopolis.university     |

| Elina Akimchenkova     | @akmchnkv     | e.akimchenkova@innopolis.university     |

| Vladimir Surikov       | @MasterLogick | v.surikov@innopolis.university    |

| Georgiy Sapronov       | @qexik | g.sapronov@innopolis.university     |



### **Value Proposition**



- **Problem**: During the first-year of study at Innopolis University we (as students) faced a problem with the local code submission system called "codetest".

    It had some fatal flaws in its implementation regarding the security aspects, as well as stability, so we decided to give our version of codetest a try.

- **Solution**: As a solution, we propose a microservice architecture system which is oriented for easier scalability, management and security.

    The architecture consists of  several independent microservices.

- **Benefits to Users**: Our system is beneficial to future Innopolis University students and professors in the sense that the proposed system is secure (as far as

    we are informed about existing software flaws), reliable, easy to maintain and use, scalable, and provides neat UX/UI.

- **Differentiation**: The system we develop offers Innopolis University a more secure and convenient way to check and generate assignments for students.

    It ensures security by addressing known software vulnerabilities and offers reliability, easy maintenance and usability, scalability, and a user-friendly interface for a seamless experience.

- **User impact**: Our software project at Innopolis University has a significant impact on users, educational society, and the industry. It improves workflows

    by offering a scalable and secure microservice architecture system for assignment submission and grading. Users are empowered with a reliable and user-friendly interface, allowing them to focus on their tasks with confidence.

- **Use cases**:

    - Assignment Submissions

    - Plagiarism Detection

    - Grading and Evaluation

    - Academic Progress Tracking



## **Lean Startup Questionnaire**

1. **What problem or need does your software project address?**

Our software project addresses the need for a secure and stable code submission system, addressing flaws in the existing

"codetest" system at Innopolis University.



2. **Who are your target users or customers?**

Our target users are the students and professors at Innopolis University who require a reliable and user-friendly

platform for assignment submission, grading, and feedback.



3. **How will you validate and test your assumptions about the project?**

We will validate our assumptions through user interviews and usability testing gathering feedback from students and

professors to analyze their experiences and suggestions.



4. **What metrics will you use to measure the success of your project?**

We will measure success through metrics such as user satisfaction, adoption rate, security incidents, system stability,

assignment turnaround time, and improvements in assignment quality based on professor feedback.



5. **How do you plan to iterate and pivot if necessary based on user feedback?**

We will gather user feedback through direct communication, identifying areas for improvement and prioritizing them for

subsequent iterations. We are open to pivoting our approach based on user feedback, ensuring the system meets the needs

and preferences of our users.



## **Leveraging AI, Open-Source, and Experts**



1. **AI (Artificial Intelligence)**:  We will leverage AI technology to improve the code submission system through

plagiarism detection enhancing efficiency and accuracy for students and professors.



2. **Open-Source**: By utilizing open-source libraries, frameworks, and tools, we can expedite development, reduce

costs, and tap into the collective knowledge and contributions of the open-source community, allowing us to focus on

customization and integration for our specific project needs.



3. **Experts in Relevant Domains**: Our team will ask for help from experts in relevant domains to achieve the best possible

solution.



## **Defining the Vision for Your Project**

1. Summary: Our project addresses the need for a secure and reliable code submission system at Innopolis University. It

    offers a streamlined workflow, improved security, and enhanced user experience, benefiting students and

    professors by simplifying assignment submission and grading processes. The project fosters a culture of excellence

    and innovation within the university community.

2. Schematic drawing:

```

                                   +-----------------+

                                   |                 |

                                   |   Database      |

                                   |  (PostgreSQL)   |

                                   |                 |

                                   +--------+--------+

                                            |

                                            |

                                            |

          +-----------------+      +--------+--------+      +-----------------+

          |                 |      |                 |      |                 |

          |                 |      |                 |      |                 |

          |  Orchestrator   +------+     Backend     +------+    Frontend     |

          |                 |      |                 |      |                 |

          |                 |      |                 |      |                 |

          +--------+--------+      +-----------------+      +-----------------+

                   |

       +-----------+-----------+

       |                       |

+------+-------+       +-------+------+

|              |       |              |

| Test runner  |       | Test         |

|              |       |  generator   |

|              |       |              |

+--------------+       +--------------+

```



As depicted above, the project consists of several modules:

- Frontend - the service which provides interaction with the user

- Backend - the service which handles requests from bot and forwards them according to their destination

- Orchestrator - the service which manages test generation and user submission execution and checking

3. **Tech stack**: Docker, docker-compose, GitHub actions CI/CD, Prometheus, Grafana, postgreSQL, Flutter, Python,

XMLRPC.



4. **Anticipating Future Problems**:

Potential challenges during project development and deployment include technical complexities, resource limitations,

time constraints, and dependencies on external systems. To mitigate these risks, we will plan meticulously, maintain

open communication within the team, leverage scalable cloud services and prioritize essential functionalities.



5. **Elaborate explanations**:

- Our project utilizes a microservice architecture, enabling scalability, management, and security. Independent

    microservices handle user authentication, assignment submission, plagiarism detection, and communication via well-defined

    APIs.



- One of the critical components is the plagiarism detection algorithm, employing advanced code analysis techniques and similarity

    algorithms to identify instances of plagiarism accurately.



- The user interface (UI) and user experience (UX) design focus on simplicity, responsiveness, and clear navigation,

    ensuring an intuitive and visually appealing interface for assignment submission, feedback review, and grade tracking.



- We integrate AI algorithms for automated code analysis and grading, leveraging machine learning techniques to save time

    for professors and ensure consistent evaluations.



- Our solution differentiates itself by offering a comprehensive and secure platform tailored specifically for Innopolis

    University, providing reliability, efficiency, and a user-friendly experience for code submission and grading while

    maintaining high standards of security and usability.



{{< /expand >}}



{{< hint danger >}}

**Feedback**







**Value Proposition**



Good explanation. But in the use cases you have to elaborate more. You need to give details cases how your app will be used and by whom?



**Lean startup question**



Good



**AI**



Good! But how will you do the plagiarism detection. What will you use



**Vision Of The Project**



Very good



**Overall**



The report is great, short but to the point.



5/5



_Feedback by Moofiy_

{{< /hint >}}



{{< expand "Week 2 report" >}}



**Important Note**

As the team discussions went by, we expanded our views of the project, hereby proposing new statements:



Terminology used below:



- Admin/Professor - a trusted user who can upload tasks, create contests, and view submissions from other users.

- Super-admin - part of the support team with all the admin's capabilities, plus the ability to add and remove new admins.

- Learner/User/Student - the non-privileged part of the population, who have the ability to submit tasks available to them or submit tasks from accessible contests.

- University - educational organization



**Key points about the project vision:**



 1. Provide the ability to deploy an instance of the entire project locally within the University.

    - As a subpoint, enable the creation of a zero-level admin, also known as  root, or a super-admin when deploying a custom instance.

    - Allow the integration of University's or any SSO (Single Sign-On) technology, if available, but studying the SSO technology is worthwhile.

    - Enable the option to make the project instance completely private, allowing only a limited number of users/learners from the University to access and submit tasks on the site.

    - Conversely, provide the ability to create an open platform where anyone can register and submit tasks, with super-admins adding administrators.

    - Allow the admin to add student lists with their email and group for more convenient user management. It is assumed that the University has a list of learners with their group assignments. The import format is to be discussed.

2. Create a unified configuration file for setting up the instance launch.





**Tech Stack Selection**

For stack selection it is important to note that our system is built using a microservice architecture, so we are not bound to a certain technology stack for the whole project. Now we are going to briefly explain the stack selection for the specific parts of our system:

- The service associated with testing user solutions (**orchestrator**) is built using Python, XMLRPC, Flask

- The mediator backend service (**juggler**) is build using Python, Flask, SQLAlchemy, JWT

- The database service is a standalone docker container used for storing user data - PostgreSQL

- The frontend consists of 2 services:

    - The Telegram bot - Java, Java Spring Boot

    - The on-site part - Dart, Flutter

The inter-service communication is achieved by exposing APIs. Code submission testing is believed to be secure since we are using Docker as sandboxing system.



The whole system is easily scalable and maintainable due to usage of Docker and docker-compose as build and deployment systems, also we use Prometheus and Grafana for log scrapping and visualization.



**Architecture Design**

1. Component Breakdown:

- **Orchestrator:**

    - *Responsibilities:* The orchestrator component is responsible for managing the execution of assignment submissions, test generation, and result checking.

    - *Interactions:* The orchestrator interacts with the juggler to receive assignment tasks, submissions, trigger test generation, and retrieve results.

- **Juggler (Mediator Backend Service):**

    - *Responsibilities:* The juggler component acts as a mediator between the orchestrator and other services. It handles user authentication, assignment routing, and manages communication between services.

    - *Interactions:* The juggler interacts with the orchestrator, database service, and frontend services. It receives user requests from the frontend, authenticates users, and routes the requests to the appropriate services for further processing.

- **Database Service:**

    - *Responsibilities:* The database service component is responsible for storing and retrieving user data, assignment details and other relevant information.

    - *Interactions:* The database service interacts with the juggler.

- **Frontend Services:**

    - **Telegram Bot Service:**

        - *Responsibilities:* The Telegram Bot service provides a user interface through the Telegram messaging platform. It allows users to submit assignments, receive feedback

        - *Interactions:* The Telegram Bot service interacts with the juggler. It receives assignment submissions from users, sends them to the juggler for further processing, and recieves feedback.

    - **On-Site Part:**

        - *Responsibilities:* The On-Site Part service offers an intuitive and visually appealing user interface. It allows students to submit assignments, take part in contests and access other features.

        - *Interactions:* The On-Site Part service interacts with the juggler. It receives assignment submissions, sends them to the juggler for processing, and retrieves relevant information.



![](/LeetForcesResources/LFreport2.png)

*Reference architecture diagram*



2. Data Management:

- The juggler uses databases implemented using PostgreSQL, that is responsible for storing user data and other relevant information. It ensures data integrity and provides efficient data retrieval capabilities.

3. User Interface (UI) Design:

- The frontend of the system consists of two services:

    - **The Telegram Bot Service:** Developed using Java and Java Spring Boot, this service handles user interactions through the Telegram messaging platform. It provides a user-friendly interface for users to submit assignments, receive feedback, and track their progress.

    - **The On-Site Part:** Built with Dart and Flutter, this service offers an intuitive and visually appealing interface for users to interact with the system. It allows students to submit assignments, take part in contests and access other features.



![](/LeetForcesResources/SiteDesign.jpeg)

*Site design in Figma*, [link to the design](https://www.figma.com/proto/kXwTmif6geaaXD5AuSVp1S/CODETEST?page-id=0%3A1&type=design&node-id=13-158&viewport=-3269%2C-203%2C0.57&scaling=scale-down&starting-point-node-id=13%3A158)



4. Integration and APIs:

- The microservices within the system communicate with each other through exposed APIs. This allows seamless integration and data exchange between the orchestrator, juggler, and other services, enabling efficient workflow management and assignment processing

- The integration with the Telegram API enables users to conveniently interact with the system through the Telegram messaging platform, providing a seamless user experience.

5. Scalability and Performance:

- The microservice architecture, combined with Docker and docker-compose, provides scalability and performance advantages. Each microservice can be independently scaled based on demand, ensuring optimal resource utilization and responsiveness, even under high user loads.

6. Security and Privacy:

- Security measures are incorporated into the system to protect user data and ensure privacy. Key security considerations include:

    - Authentication and authorization mechanisms to verify the identity and access rights of users and ensure secure access to sensitive data.

    - To ensure the security and stability of the system, custom processes, such as code submissions, are isolated within separate Docker sandbox containers. This isolation prevents potential malicious code or vulnerabilities from impacting the underlying system or compromising user data.

7. Error Handling and Resilience:

- The system includes robust error handling mechanisms to maintain reliability and resilience. Strategies for error logging, monitoring are implemented to ensure the system can recover from failures and maintain uninterrupted operation.

8. Deployment and DevOps:

- DevOps practices are employed to streamline the deployment process and ensure efficient collaboration among team members. Key aspects include:

    - Deployment Process:

        - *Automation:* The deployment process is automated using tools such as Docker and docker-compose. These tools enable the creation of containerized environments, making it easier to deploy the system consistently across different environments.

        - *Continuous Integration/Continuous Deployment (CI/CD):* GitHub Actions CI/CD is utilized to automate the build, testing, and deployment processes. This ensures that changes made to the codebase are thoroughly tested and seamlessly deployed to production or staging environments.

    -  Version control is managed using Git and the codebase is hosted on GitHub. This allows for efficient collaboration among team members, version tracking, and easy rollback in case of issues.

    - Monitoring and log scraping are implemented using Prometheus and Grafana. These tools provide insights into the system's performance, resource utilization, and error tracking, helping identify and resolve issues promptly.

    - Development Workflow:

        - *Collaboration:* The team follows collaborative development practices, utilizing Git branches, pull requests, dashboard and code reviews to ensure code quality and prevent conflicts.

        - *Agile and Iterative Approach:* An agile methodology is adopted, enabling iterative development, frequent releases, and the incorporation of user feedback into subsequent iterations.

{{< /expand >}}



{{< hint danger >}}



**Feedback**



**1. Component Breakdown**



Good,



**2. Data Management**



Good!!



**3. UI Design**



Nice designs

But the design in desktop-8 you should show how will you present the contests



**4. Integration and APIs**



But you integrate with your own API :)



**5. Scalability and Performance**

Good



**6. Security and Privacy**

Good



**7. Error handling and Resillience**

You will do all of that? I highly doubt that it’s manageable.

Maybe pick one or tow and focus to perfect them.



**8. Deployment and DevOps**

Very Good



**Answering questioner**

Missing?



**Overall**

The report is  good. But you didn’t answer the questioner



Grade 4/5





_Feedback by Moofiy_

{{< /hint >}}



{{< expand "Week 3 report" >}}



## **Developing the first prototype, creating the priority list**

As we conclude the third week of our project, we are thrilled to share the development milestones and insights gained from our journey so far. This week, we focused on creating a prototype of our system and are happy to present its main features and functionalities.





#### **Technical Infrastructure**

Speaking of technical infrastructure, setting up a robust technical infrastructure is crucial for the success of our project. The development part of our project does not require renting additional computational resources, so we can use our laptops since they provide enough computational power. We ensured that team members have efficient access to the infrastructure.



#### **Backend development**

We have designed the first iteration of our internal APIs (for Juggler and Orchestrator) and have written descriptive documentation for them using OpenAPI Specifications. You can find file with specifications [here](https://drive.google.com/drive/folders/1AuQu-GkGnGx5MI5kP3T2BLo-n5bvH5W_), after download you need to import configuration files into  your favourite OpenAPI editor, fer the development part we used the following [resource](https://editor.swagger.io). And we have already implemented all of them, then we will expand our internal APIs based on demand.



#### **Frontend development**

We started the development process of the frontend part using Flutter framework. We have successfully developed the first iteration of the frontend. We have started to implement the busyness logic of the project, including authentication.



#### **Data Management**

For the data management we set up the PostgreSQL database. We have developed necessary entities for the first iteration of the development.



#### **Prototype Testing**

Speaking of testing, we sent our first prototype to our student friends, also we used cross-testing technique, i.e. the team member who developed the juggler tests the orchestrator and the one who wrote the frontend part tests the juggler.



<!-- гера молодец -->

### **Prototype Features**

In our first prototype, we have implemented core functionalities to make our project practical for early testing and getting user feedback. Here are the features that we managed to successfully implement:

1. User registration

- The Juggler API now supports registering to our system. In the future, it will enable the project and our users to hold a full-fledged web session using the on-site frontend and to implement authorization.

2. Adding tasks

- The users can create tasks using the API and telegram bot frontend. The problem statement, tests, reference answers, time and memory limits are all available for the authors to set.

3. Grading system

- The users can submit their solutions to the system and consequently receive the submission status.

4. Telegram frontend

- The communications with the API can be done using the telegram bot frontend. It supports all the basic commands in our prototype.



### **User interfaces**

1. On-site interface

- The on-site part has a minimalistic design, focusing on usability and clean, visually appealing interfaces. The prototype allows users to navigate through the registration and login pages and partially represents the interface of the main page. However, the interface is still work in progress as the team is designing the interface alongside implementing the web frontend.



2. Telegram bot

- Users can interact with our service directly from Telegram. The bot is capable of guiding users through problem submission, feedback, and progress tracking.



### **Challenges and solutions**

During the development of the prototype, we encountered some challenges:



1. **Telegram frontend**

- Integrating the Telegram API into our system was a complex task. We had to ensure that our Telegram bot was able to receive tasks from users, forward them to the Juggler for processing, and return the feedback. We overcame this challenge by thoroughly studying the Telegram API documentation and consulting online forums for specific implementation questions.

2. **Orchestrator Service**

- Setting up a reliable, secure, and efficient grading system was another challenge. We had to ensure that user submissions are run in an isolated environment to prevent any malicious activities. Docker provided us with the sandboxing capabilities we needed.

3. **User Authentication**

- As we were trying to make the user registration and authentication as secure as possible, we found it challenging to correctly implement JWT token-based authentication. We overcome this issue by studying more about the JWT tokens, their creation, validation, and best practices for this technology.



### **Next steps**

Looking ahead, we are excited to continue improving our system. Our plans for the upcoming weeks in the order of priorities include:

1. **Web frontend implementation**

- The web frontend implementation is underway and currently the number one priority for our project.

2. **Feature Additions**

- We plan to introduce additional features such as authorization, contest system and a user profile page.

3. **UI/UX Improvements**

- We plan to refine the user interface and enhance user experience based on user feedback and usability testing.

4. **Improving Test Generation and Result Checking**

- We will work on the Orchestrator to ensure it can handle a wider variety of tasks and produce more comprehensive test results.



{{< /expand >}}



{{< expand "Week 4 report" >}}



In the fourth week of developing our project during the Capstone project course, we



### External Feedback



To gather feedback we asked the InnoMastery team to share their thoughts on our project and give us some valuable tips that can only be given by a project observer and they did not disappoint us. Here is their feedback:



> Hello! We are really happy to be the first testers of your project. In our opinion, LeetForces project is a very relevant idea for our university because the existing system for task submission and automatic testing - CodeTest - does not meet the expectations of the students. The latter site suffers from numerous problems, such as lack of server security, dated interface and frequent downtimes. With the prototype you supplied us there was a Telegram interface as the main frontend. Because of the Telegram being a messenger and not a full-fledged platform, it cannot provide a complete user experience. Even though the Telegram bot enables the user to use almost all features of the system, the command-based communication model does not seem to be convenient. Therefore, our team thinks that you should direct more forces into developing a Web Frontend for your project. You also provided us with the incomplete build of your web interface that already contains most of the screens. We really liked your idea to use Material Design in your project. As for your question regarding the effective usage of Machine Learning in your project, we do not see any potential on this stage of development. Right now the implementatino of the main functions should be a higher priority.





### Testing and narrowing the scope of the project



#### Testing

As already mentioned in previous project reports, we continue to employ a cross-testing method where every team member tests the components of other group members. This approached proved to be effective during the course as it helped to prevent a lot of bugs on the early stages of the development of our project.



#### Narrowing the scope of the project

Based on the feedback, we changed our focus from supporting the Telegram bot by updating it to our backend API specifications to rapidly developing the web frontend with all our forces. Moreover, the Machine Learning applications are no longer a priority and will be implemented only after the main parts of the project are done.



### Iteration

In the current iteration, we decided to drop some features based on the advice we got from the InnoMastery team. Namely, we are no longer updating the Telegram bot frontend interface. Also, we have developed all internal back-end requirements features that were so far needed by front-end part of our team. In the next iteration, we are going to mainly test the existing functionality and bring the frontend to the usable state.



{{< /expand >}}





{{< hint danger >}}

**Feedback**



**External Feedback**<br>

Good, but only 1 feedback?

Do you think it’s enough?



**Testing**<br>

Ok you have a testing process, can you show results?



>As already mentioned in previous project reports



What exactly was mentioned? You should state it explicitly what you mentioned in order to understand, beside write in what report you talked about testing



If you have a testing process, how do you documents bug finding / fixing?



Please show proof of what you are saying that you were doing.





**Iteration**<br>

So you decided to change your project, just because of one feedback!!!!!



This design should be made on a more stronger basis rather than 1 feedback form other students.





Also you didn’t mention an iteration plan:

An iteration plan is essentially the plan for an upcoming iteration. It would typically outline:

* The goals and objectives for the iteration: what the team aims to achieve.

* The features to be developed.

* The tasks needed to develop these features. This might include coding, testing, design tasks, etc.

* Any assumptions or dependencies.

* A timeline for the iteration.



**Overall**<br>

The report is ok. You should be more focused on your ideas, and do more feedback iteration to see other students opinion



**Grade: 2/5**



_Feedback by Moofiy_

{{< /hint >}}


{{< expand "Week 5 report" >}}

## User suggestions
**We gathered feedback from 10 users regarding our web application, and here is
a summary of the key feedback points and suggestions provided by the users:**
- **User Interface**: The majority of users found the user interface to be
clean, intuitive, and visually appealing. They appreciated the minimalist
design and easy navigation throughout the application.
![](/LeetForcesResources/SiteDesign3.jpeg)
![](/LeetForcesResources/SiteDesign2.jpeg)
![](/LeetForcesResources/SiteDesign4.jpeg)
- **Functionality**: Users expressed satisfaction with the core
functionality of the web application. They found it reliable and efficient
in submitting tasks, receiving feedback, and tracking their progress.
- **Feature Requests**: Several users suggested the addition of a contest
system, allowing them to participate in coding challenges against other
users. They believed it would enhance the competitiveness and engagement
within the platform.
- **Usability**: While most users found the application easy to use, a few
mentioned minor usability issues. They suggested providing more prominent
buttons and clearer instructions for certain actions to improve the overall
user experience.
- **Mobile Responsiveness**: A couple of users highlighted the importance
of mobile responsiveness, as they often accessed the web application on
their smartphones. They suggested optimizing the interface for mobile
devices to ensure a seamless user experience across different platforms.
- **Performance and Speed**: Users generally appreciated the performance of
the web application, but a few mentioned occasional delays when loading
pages or submitting tasks. They recommended optimizing the system to
enhance speed and responsiveness.
- **Collaboration and Social Features**: Some users expressed interest in
features that would enable collaboration and interaction with other users.
They suggested incorporating discussion forums, chat functionality, or a
social feed to foster a sense of community and facilitate knowledge sharing.
- **Documentation and Help Resources**: A few users emphasized the
importance of comprehensive documentation and easily accessible help
resources within the web application. They suggested providing clear
instructions, tutorials, and FAQs to assist users in understanding the
platform's features and functionalities.
- **Security and Privacy**: Users valued the importance of data security
and privacy within the web application. They emphasized the need for robust
security measures, including encryption of user data, secure login
procedures, and protection against potential vulnerabilities.
- **Performance Metrics**: Some users expressed interest in having access
to performance metrics, such as assignment completion times, accuracy rates,
and progress tracking. They believed that having these metrics would allow
them to gauge their performance and set personal goals.

## Feedback Collection Plan

To collect feedback from users, we implemented the following strategies:
- **One-on-One Interviews**: Scheduled meetings with users to discuss their
experience using the web application and gather detailed feedback.
- **Online Questionnaires**: Created online questionnaires with a
standardized format to collect quantitative feedback on specific aspects of
the application.

We administered user surveys and conducted feedback sessions to gather input on
the following areas:
- **User Interface**:
    • How would you rate the overall design and aesthetics of the user
    interface?
    • Are the navigation and layout of the application intuitive and easy
    to use?
    • Is the color scheme and typography visually appealing and consistent?
- **Functionality**:
    • Are you able to easily complete the desired tasks and actions within
    the application?
    • Do you encounter any errors or issues while using the different
    features of the application?
    • Are there any additional features or functionalities you would like
    to see implemented?
- **Usability**:
    • Do you find the application easy to learn and use, even without prior
    instructions or guidance?
    • Are the buttons, icons, and menus clearly labeled and understandable?
    • Is the overall user experience smooth and seamless?
- **Performance**:
    • Does the application load quickly and respond promptly to user
    interactions?
    • Have you experienced any delays or lags while using the application?
    • Are there any specific areas where you noticed a need for performance
    improvements?
- **Mobile Responsiveness**:
    • Have you accessed the web application on a mobile device? If yes, how
    would you rate its responsiveness and usability on mobile?
    • Is the content and layout adapted effectively to different screen
    sizes?
- **Collaboration and Social Features**:
    • Would you find it valuable to have features that enable collaboration
    and interaction with other users?
    • What specific collaboration features would you like to see implemented
    (e.g., discussion forums, chat functionality, social feed)?
- **Documentation and Help Resources**:
    • Are there sufficient instructions, tutorials, or FAQs available to
    help you understand and navigate the application?
    • Do you have any suggestions for improving the documentation or making
    it more accessible?
- **Security and Privacy**:
    • How confident are you in the security measures implemented within the
    application to protect your data?
    • Are there any specific security or privacy concerns you would like to
    address?
- **Performance Metrics**:
    • Would you find it beneficial to have access to performance metrics,
    such as assignment completion times or accuracy rates?
    • Are there any specific performance metrics you would like to track?
- **Overall Satisfaction**:
    • On a scale of 1 to 10, how satisfied are you with the overall
    experience of using the web application?
    • Do you have any additional comments, suggestions, or feedback to
    share?

## Product roadmap refinement
- Although some users suggested adding the competitive contests, our team
decided not to implement this feature, since that would potentially increase
the competitiveness in the student environment, and we are against this.
- Some users said that we should improve the UX and UI of our front-end
part, our team members who are responsible for the frontend have already
started working on this problem.
- Speaking of the mobile responsiveness, the frontend team is already
aware of this problem, but they consider this issue as less important for
the stage of MVP, since our target audience (students of Innopolis
University) are writing code on laptops, not on the mobile phones with
small screen size.
- The backend team knows about performance issues, and they are looking for
the opportunities to improve the performance through code refactoring and
consulting with each other.
- Other users suggested adding the forum/task discussion section and
performance metrics. We think that this are important features, and we will
try to add it if we have enough time to accomplish this task.

{{< /expand >}}



{{< hint danger >}}
**Feedback**

**Collecting and documenting feedback**<br>
good plan, but how did you collect? and how did you documented?
where are the results?


**Feedback analysis**<br>
missing

**Roadmap and enhancement**<br>
Refinement part is good
missing Roadmap


**Grade: 2/5**


_Feedback by Moofiy_
{{< /hint >}}

