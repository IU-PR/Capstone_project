---
title: "Week #3"
---

# <p style="text-align: center;">**Capstone Project**</p>

# <p style="text-align: center;">*Team GymGuru*</p>

## **Week 3 - Developing the first prototype, creating the priority list**


## **Week's focus and importance**

&nbsp;&nbsp;&nbsp;&nbsp;This week we have been working on turning our idea into a real working prototype, and this is important because it is necessary to create a high-quality prototype, since it allows to check the initial concept and identify any technical or design issues early, allowing us to address them before fully completing the work. To achieve this, we had to complete several intermediate stages and link them together. Our plan was to complete a section with verification of the accuracy of physical exercises, finalize the design of the website, find a platform for deployment, integrate all the parts, connect the database, and run the first prototype tests.


## **Web application**

&nbsp;&nbsp;&nbsp;&nbsp;This is a link to our web application GymGuru - https://gymgu.ru/

&nbsp;&nbsp;&nbsp;&nbsp;You could registed, login, сhose a physical exercise (for the first prototype, only push-ups are avilable) and see how it recognizes the correctness of performing a physical exercise.

&nbsp;&nbsp;&nbsp;&nbsp;**Important note:** Testing is preferable on Google Chrome browser, and we do not recommend to use Yandex Browser for now. Because of some reasons, there can be issues with registration and camera permission.

## **Prototype Features**

&nbsp;&nbsp;&nbsp;&nbsp;Our current version allows the user to register and authenticate, add his data (height and weight), switch the camera on and do exercises. Our service recognises a user`s body, builds a dot skeleton on it and shows it to the user. Moreover, it recognises if the exercise technique is correct, now only for push-ups.

&nbsp;&nbsp;&nbsp;&nbsp;That is our project architecture, red elements are not implemented yet. Others are implemented and they are the base of our first prototype:

<img src="/2024/GymGuru/Week3_ImplementedParts.jpg" width="880" height="1050">

## **User Interface**

&nbsp;&nbsp;&nbsp;&nbsp;These are the UI (Web Pages) that we implemented on this week:

- Main page

<img src="/2024/GymGuru/Week3_UI_1.png" width="880" height="520">

- Registration page

<img src="/2024/GymGuru/Week3_UI_2.png" width="880" height="520">

- Login page

<img src="/2024/GymGuru/Week3_UI_3.png" width="880" height="520">

- Rating page (Buttons “Next” and “Previous” are clickable to see other exercises rating)

<img src="/2024/GymGuru/Week3_UI_4.png" width="880" height="520">

- Exercises page

<img src="/2024/GymGuru/Week3_UI_5.png" width="880" height="520">

- Exercises` buttons are clickable, user can see the videos of a correct performing (now it is done for Push-Ups)

<img src="/2024/GymGuru/Week3_UI_6.png" width="880" height="520">

- Recognition page

<img src="/2024/GymGuru/Week3_UI_7.png" width="880" height="520">

- Fitness test page

<img src="/2024/GymGuru/Week3_UI_8.png" width="880" height="520">



## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

Before the working process of this week we organized all necessary technical infrastructure for convenient development process. We set up a GitHub Project with backlog, roadmap, milestones and issues to control features development process. Also, as a deployment platform we chose and rent a server with satisfactory parameters to maintain the main application logic and database. Of course, each team member has a software for the coding customized specifically for his/her preferences. In addition, since our team has 2 reporters, we creates a shared document for each report where all team members could see the progress in report writting and suggest any additions or recommendations.

- **Backend Development**:

&nbsp;&nbsp;&nbsp;&nbsp;During this week our team was focused on the following tasks: recognition of a body by using MoveNet (pose detection model) was implemented, then correct execution checking was developed for some exercises. Moreover, we chose a domain name, rented a server and hosted our web application.

- **Frontend Development**:

&nbsp;&nbsp;&nbsp;&nbsp;As about our progress on fronted: we have finished with all important pages: main page, registration and login page, rating page with possibility to flipping through pages with exercises results, page with exercises, where user can click on the exercise preview and see the page with the video of a correct technique and can train with the help of video model assistant. Also, we have implemented a fitness test page, where users can see the necessary thresholds to pass for each exercise. 

- **Data Management**:

During this week we set up a PostgreSQL database on a rented server. For now, this database is connected to the web application GymGuru and support the main operation - authorization. A user can create new account, if he/she has no it yet, log in, or log out. It is worth noting that the password is transmitted only in hashed form. For the creating of a new account, the name, surname, email and password are required, while for login user should enter the email and the password. During a testing session by all team members, there were detected no problems with this functionality of the database.

- **Prototype Testing**:

Right after the deployment of the first prototype of our web application to the rented server and the fixing of several bugs, we conduct a testing session by all team members. In general, the web application is quite satisfactory for each of us, have a good UI and functionality as for the prototype. However, we found several more bugs and parts that we can improve during the next weeks. This is a list of them:

- In the mobie version of a web site the video from the camera of a smartphone has wrong size, it expands to the whole width of a screen;

- The main page is not complete yet, several improvements will be delivered in a week;

- The main page is not fully adapted for the mobile version of a web site.

## **Challenges & Solutions**

1) When writing the part of the code related to recognizing the correctness of an exercise, a problem arose: how to evaluate the correctness, and which parts of the body to look at specifically. We were able to solve this problem with the help of additional resources, including YouTube.

2) Our main problem was finding a place to deploy the project. During the last review session, we were recommended the Github platform, but we could not use it due to special registration requirements for a foreign bank card. We resolved this issue by using a rented server instead.

## **Conclusions & Next Steps**

&nbsp;&nbsp;&nbsp;&nbsp;This week, the team managed to make a working prototype, having previously completed all the intermediate stages, such as recognizing points on the body, recognizing the correctness of the exercise, and embedding the project on a server with a database connection with authorization.

&nbsp;&nbsp;&nbsp;&nbsp;Our next steps will be:

- To add more supported physical exercises;

- Fix several bugs that we found during testing session;

- Finish UI with respect to fixing all inaccuracies and adaptation for the mobile version;

- Expand the list of supported database operations according to the data flow diagram.
