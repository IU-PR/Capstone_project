---
title: "Week #2"
---

# <p style="text-align: center;">**Capstone Project**</p>

# <p style="text-align: center;">*Team GymGuru*</p>

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

## **Tech Stack Selection**

After several discussions our team defined a final at this moment Tech Stack that will allow us to implement all stated tasks for GymGuru project:

- MoveNet: Open-Source ML Tool that allow us to determine coordinates of a human body

- HTML + CSS + JS: base of a frontend, also JS allow to integrate MoveNet into the client side of application

- TailwindCSS: open-source CSS framework used to add styles to HTML elements that helps to adapt the app for different devices

- Flask: convenient for creating web applications on Python, we can use it to quickly obtain sufficient results

- PostgreSQL: for database of the application

## **Architecture Design**

1. **Component Breakdown**:

&nbsp;&nbsp;&nbsp;&nbsp;Overall, our system architecture consists of web-interface, backend and database:

1) In the web-interface the main component is exercise control manager, it do all functionality: tells user if his pose is correct, shows the picture of user with dots skeleton, on the fitness test mode it tells the time left and maintains other user-included features.

2) The backed part components are login manager (for user registration), rating manager (for user personal statistics collecting), profile manager (for defining that user is not an other student to avoid cheating), fitness test manager (for timing, calculating passing etc.)

3) In the database there are user personal information and exercises results.

<img src="/2024/GymGuru/Week2_Architecture.jpg" width="780" height="990">

2. **Data Management**:

&nbsp;&nbsp;&nbsp;&nbsp;The concept of data management of GymGuru is presented on the diagram below:

<img src="/2024/GymGuru/Week2_DataFlow.png" width="600" height="540">

&nbsp;&nbsp;&nbsp;&nbsp;Data flow is organised the following way: video from user’s camera is processed in the web interface, MoveNet adds skeleton to the video, then in the web interface results are calculating and translating to the user. Web interface sends user results or user credentials for log in to the backend and gets user data. Backend communicates with database to store or request user data.

&nbsp;&nbsp;&nbsp;&nbsp;As is was stated above, in **Tech Stack Selection** section, PostgreSQL RDBMS is chosen for creating a database of GymGuru web application. The reasons of this decision are:

- PostgreSQL is a powerful client-server relational database management system that is fully sufficient for our project;
- We already have an experience in creating PostgreSQL database for the web application;
- PostgreSQL is known by each team member, as we all passed the DataBases course in the previous semester.

3. **User Interface (UI) Design**:

&nbsp;&nbsp;&nbsp;&nbsp;Over the past week, we have developed prototypes of the user interface using Figma. You can view some of the pages below in the screenshots, as well as the full prototype at [this link](https://www.figma.com/design/JWNuJgSjWY8XHJ4CfsVzB6/Untitled?node-id=0-1&t=60raqLQQw0dLg9PE-1).

<img src="/2024/GymGuru/Week2_UI1.jpg" width="780" height="480">

<img src="/2024/GymGuru/Week2_UI2.jpg" width="780" height="440">

&nbsp;&nbsp;&nbsp;&nbsp;Moreover, that is a User Flow Diagram of our web application (and its text description below):

<img src="/2024/GymGuru/Week2_UserFlow.jpg" width="1050" height="825">

&nbsp;&nbsp;&nbsp;&nbsp;Entering the site the user gets to the main page where the general information about the product is presented. Then, in order to use the offered functionality, the user must log in to his account (if he has already registered before) or register and set up account (specify info, such as first name, last name, e-mail, password and type of account: student or coach). Both student and coach can perform the exercises and view the rating of the chosen exercise. To do the exercise it is necessary to choose it from the list, allow access to the camera and start performing it. When completed, click on the finish button to save the statistics and display it in the rating page and in the profile. The student additionally can pass the fitness test. The procedure is similar to performing a single exercise, except that in this mode it is necessary to perform in sequence all 3 types of exercises included in the fitness test list and the time of doing them is limited. The coach has the ability to download fitness test results by selecting the desired group or course.

4. **Integration and APIs**:

&nbsp;&nbsp;&nbsp;&nbsp;Our team is planning to use several external services, such as Prometheus and Grafana for collecting and visualizing the statistics. We will integrate it using Docker Compose, creating one Docker container for each service connecting with the main application container. These services will take information from special file(s), which are stored on the server and updated by the application (this is the standard way of information flow for Prometheus and Grafana).

5. **Scalability and Performance**:

&nbsp;&nbsp;&nbsp;&nbsp;We can consider two sides of growth and scalability: functionality and number of users. Growth from the functionality side is in adding different physical exercises support and expanding the database server. These points will not cause any problems in performance.
&nbsp;&nbsp;&nbsp;&nbsp;Scalability in terms of the number of users also will not cause any problems since we will use the strategy of “fat clients”. It means that all calculations and the work of the ML model will happen on the client side. The main reason for this decision is the huge cost of sending the stream of images from the camera to the remote server. Summarizing, while growing the number of users the performance will not suffer. The only point of increasing load will be the connection to the database server. However, the packets sent between user and database are relatively small (several numbers or credentials), so the load will grow very slightly.


6. **Security and Privacy**:

&nbsp;&nbsp;&nbsp;&nbsp;Security aspect: only the hashed version of the password will be stored on the database server to prevent accessing of accounts by other people in case of information theft.
&nbsp;&nbsp;&nbsp;&nbsp;Privacy aspect: the service will now process or store a video from the user’s camera, since the whole processing part is on the client side. So, this information cannot be stolen from the server or during the sending process. 


7. **Error Handling and Resilience**:

&nbsp;&nbsp;&nbsp;&nbsp;To prevent and properly catch any errors we will:
1) Use checking during login process (hashed password)
2) Make logs before and after each operation related to login, video processing, database server connection, etc.
3) Use Rsyslog for the work with logs
4) Use Prometheus + Grafana to visualize statistics about errors, stability, performance, etc.


8. **Deployment and DevOps**:

&nbsp;&nbsp;&nbsp;&nbsp;We decided to use Docker and Docker Compose to deploy our web application to the server. Docker will allow us to deploy different systems (for example: main application, nginx, rsyslog, prometheus, grafana, etc.) at once conveniently and not to configure the environment.
&nbsp;&nbsp;&nbsp;&nbsp;Moreover, we will use GitHub Actions to configure proper CI/CD for automatic testing of availability to access all services of the project and automatic deployment to the server after each pull request to the master branch.


## **Week 2 questionnaire:**

1) **Tech Stack Resources:**

&nbsp;&nbsp;&nbsp;&nbsp;In our project, we require the use of several programming languages with which we do not have sufficient experience or knowledge. Therefore, we have selected a number of books to assist us with this endeavor. These books will help us expand our knowledge and gain first-hand experience in the fields.

List of books:
- [HTML and CSS using examples](https://docs.yandex.ru/docs/view?tm=1718275506&tld=ru&lang=ru&name=html_i_css_na_primerakh_3642805.pdf&text=HTML%20Css%20book&url=https%3A%2F%2Fbooks.4nmv.ru%2Fbooks%2Fhtml_i_css_na_primerakh_3642805.pdf&lr=121642&mime=pdf&l10n=ru&sign=d252d2ecfe359e5088c1d978ed6ca0df&keyno=0&nosw=1&serpParams=tm%3D1718275506%26tld%3Dru%26lang%3Dru%26name%3Dhtml_i_css_na_primerakh_3642805.pdf%26text%3DHTML%2BCss%2Bbook%26url%3Dhttps%253A%2F%2Fbooks.4nmv.ru%2Fbooks%2Fhtml_i_css_na_primerakh_3642805.pdf%26lr%3D121642%26mime%3Dpdf%26l10n%3Dru%26sign%3Dd252d2ecfe359e5088c1d978ed6ca0df%26keyno%3D0%26nosw%3D1)
- [Fluent Python: Clear, Concise, and Effective Programming](https://zlib.pub/book/fluent-python-clear-concise-and-effective-programming-6hf31q1i8010)
- [Flask Web Development](https://coddyschool.com/upload/Flask_Web_Development_Developing.pdf)

2) **Mentorship Support:**

&nbsp;&nbsp;&nbsp;&nbsp;Our team currently does not have a mentor. We have considered the possibility of finding one in the past, but have not found a suitable candidate at this time and have decided to proceed without one. A mentor may be able to assist us in making certain decisions regarding our technical stack or provide guidance in the right direction, however, we have chosen to manage without this support at this point.

3) **Exploring Alternative Resources:**

&nbsp;&nbsp;&nbsp;&nbsp;In addition to reading books on the subject, we also viewed several video tutorials and reviewed documentation in order to gain a better understanding of the technology stack relevant to our project. This approach proved to be highly beneficial in terms of our learning.

List of resources:
- [Flask Course - Python Web Application Development](https://www.youtube.com/watch?v=Qr4QMBUPxWo)
- [JavaScript Tutorial for Beginners](https://youtu.be/W6NZfCO5SIk?si=yjpexvOJmwgxQZpW)
- [Pose Detection using MoveNet](https://github.com/tensorflow/tfjs-models/blob/master/pose-detection/src/movenet/README.md)


4) **Identifying Knowledge Gaps:**

&nbsp;&nbsp;&nbsp;&nbsp;We use JavaScript to recognize body position, but we have gaps in knowledge and experience in this technical stack. To fill the skills gap, we reviewed courses, books and documentation in this area, but the documentation was more useful than the rest in our opinion.

5) **Engaging with the Tech Community:**

&nbsp;&nbsp;&nbsp;&nbsp;At this stage, we have not actively engaged with the broader tech community to seek guidance or learn from experienced professionals in our tech stack. There is still much to learn and understand in our field. However, for now, we rely on resources such as books and online materials to expand our knowledge. Nonetheless, if our team comes across a relevant event or opportunity to connect with experienced professionals, we would definitely consider attending or participating to enhance our understanding.

6) **Learning Objectives:**

&nbsp;&nbsp;&nbsp;&nbsp;This week, our learning objectives are focused on deepening our knowledge of Mediapipe and other similar computer vision instruments. We aim to learn how to work with these instruments and explore other projects available on the internet that utilize them. We also want to learn the basics of JavaScript to begin implementing computer vision techniques using online learning materials. To achieve these objectives, we plan to research and study the documentation and tutorials mentioned in resources.

7) **Sharing Knowledge with Peers:**

&nbsp;&nbsp;&nbsp;&nbsp;We regularly allocate time during our weekly meetings to discuss and exchange insights and experiences related to our tech stack. These knowledge-sharing sessions enable us to distribute tasks more efficiently. By sharing our knowledge and expertise, we strengthen collaboration and provide an opportunity for team members to learn from each other. These discussions also allow us to brainstorm ideas, troubleshoot challenges, and collectively find effective solutions.

8) **Leveraging AI:**

&nbsp;&nbsp;&nbsp;&nbsp;We have used AI-powered tools for the process of acquiring knowledge and expertise for our project. We have utilized AI to find the most useful resources that align with our learning goals, enabling us to learn efficiently and effectively. Additionally, we have relied on AI to provide explanations and insights on specific aspects of our tech stack that we may not fully understand.

## **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
| Gleb Bugaev      | Management (TeamLead) | Control of the working process, GitHub management (Backlog, Milestones, Issues) | 
| Mariia Shmakova  | Reporter              | Report Writting |
| Milana Sirozhova | Reporter              | Report Writting |
| Anna Gromova     | Backend               | Pose detection, Conditions for the correct performance of exercises |
| Nail Minnemullin | Backend               | MoveNet connection, Database, Deployment with Docker, Prometheus + Grafana |
| Arina Goncharova | Frontend              | Web Pages Development |
| Liana Mardanova  | Frontend              | Web Pages Development |

&nbsp;&nbsp;&nbsp;&nbsp;In addition to the table above, it is necessary to describe the division of work between reporters and frontenders.

- There are 2 frontenders who are responsible for the different web pages development and supporting:
    - Arina Goncharova - Main, Profile, Login, Registration pages
    - Liana Mardanova - Exercises (preview + performing), Fittest, Rating pages
- There are 2 reporters who responsible for the different parts of each weekly report:
    - Mariia Shmakova - Desctiption of the necessary for report parts of project
    - Milana Sirozhova - Diagrams and descriptions of project concepts

## **Weekly Progress Report**

&nbsp;&nbsp;&nbsp;&nbsp;Throughout the week, our team was engaged in one of the main steps for the project - designing the structure of the web application. We have developed an application structure that includes all its components and a data management scheme. In addition, the team began implementing web pages and working with MoveNet to recognize the position of the human body.

## **Challenges & Solutions**

&nbsp;&nbsp;&nbsp;&nbsp;Our team faced with several problems during the working process on this week. However, all of them are successfully solved:

- We discussed the different types of project structure, trying to figure out which one would best meet the needs of the project. After planning and several tests, the team decided that the best option would be to use the "fat client" approach, which will minimize the impact of Internet quality on the result and the load on the main server (this solution is described in more detail in the chapter **Scalability and Performance**).

- We were faced with the choice of ML-tool for determining the position of the human body: the known ones  were MoveNet and MediaPipe. We tested both models with the simplest implementation on the server, which helped us choose MoveNet among these options. This model was characterized by a higher speed of human "skeleton" construction and it was more convenient for us to work with it to integrate into the client part using JavaScript.

## **Conclusions & Next Steps**

&nbsp;&nbsp;&nbsp;&nbsp;This week we have implemented all the tasks set for planning the architecture of the project, searching for the necessary literature and resources, distributing areas of responsibility among team members, as well as determining such important aspects of the project as Scalability, Security, Deployment and so on for the future.

&nbsp;&nbsp;&nbsp;&nbsp;This is a list of the next steps that our team is going to follow:

- Create a Database for application
- Code a checker of correctness of the performing physical exercises
- Finish the main web pages
