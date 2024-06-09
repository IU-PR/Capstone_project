---
title: "Week #1"
---

# <p style="text-align: center;">**Capstone Project**</p>

## <p style="text-align: center;">*Team GymGuru*</p>


## **Team Formation and Project Proposal**

#### **Team Members**

| Team Member              | Telegram ID   | Email Address   | Role |
|--------------------------|---------------|-----------------|-----------------|
| Gleb Bugaev              | @BugaevGleb | g.bugaev@innopolis.university | Team Leader |
| Mariia Shmakova          | @marishmak | m.shmakova@innopolis.university | Reporter |
| Nail Minnemullin         | @nai1ka | n.minnemullin@innopolis.university | Backend |
| Arina Goncharova         | @peachellyy | a.goncharova@innopolis.university | Frontend |
| Anna Gromova             | @anngrosha | an.gromova@innopolis.university | Backend |
| Liana Mardanova          | @liaaaaaana | l.mardanova@innopolis.university | Frontend |
| Milana Sirozhova         | @milana_sirozhova | m.sirozhova@innopolis.university | Reporter |

#### **Team Members' Background and Expected Impact**

- Gleb Bugaev - has an experience in team leading and product management, supposed to control project flow, formal elements (reports, contact with TAs) and GitHub issues.
- Mariia Shmakova - responsible for weekly reports, good skills in statistics and ML
- Nail Minnemullin - worked with backend parts of several projects, experienced in creating web applications
- Arina Goncharova - frontend, has experience working with the ML tool that we plan to use
- Anna Gromova - worked with backend parts of several projects, ML engeneer
- Liana Mardanova - frontend, has experience working with the ML tool that we plan to use
- Milana Sirozhova - system design, will focus on various graphs/schemas/descriptions of weekly reports.

## **Value Proposition**

- **Identify the Problem:**

&nbsp;&nbsp;&nbsp;&nbsp;Self-training is a popular format of exercise, but it often lacks professional supervision, leading to incorrect techniques that may cause injuries and reduce the effectiveness of the training. Proper guidance on performing exercises correctly can be highly beneficial.

&nbsp;&nbsp;&nbsp;&nbsp;At Innopolis University, the Sport exam is conducted as follows: at the end of the semester, students select a time slot to take the fitness test. They then go to the sports complex where they perform a tilt, do crunches in pairs, and complete push-ups. Finally, students report their results to the trainer one by one.

&nbsp;&nbsp;&nbsp;&nbsp;This process presents several potential issues: students must physically come to the sports complex, the available time slots may be inconvenient, and there are other problems highlighted in the survey results below. Additionally, coaches are unable to supervise all students simultaneously, which could lead to improper exercise execution or cheating.

&nbsp;&nbsp;&nbsp;&nbsp;To address these concerns, we conducted a survey among students to identify existing problems and gather their opinions on the feasibility of conducting fitness tests online.

&nbsp;&nbsp;&nbsp;&nbsp;Based on the survey results, we see that a significant portion of students encounter challenges related to the current fitness test process. Given these challenges, an IT solution may offer a more flexible and efficient approach. An online platform could allow students to complete their exercises at their convenience while ensuring proper technique through virtual supervision. Additionally, students could use the platform for regular training, benefiting from continuous virtual guidance. Implementing such a solution could streamline the fitness test process, making it more accessible and effective for both students and coaches.

<p float="left">
  <img src="/2024/GymGuru/Week1_Pool1.png" width="320" height="480">
  <img src="/2024/GymGuru/Week1_Pool2.png" width="320" height="320">
</p>

- **Solution Description:**

&nbsp;&nbsp;&nbsp;&nbsp;Our solution leverages pose estimation and exercise recognition to evaluate students' fitness performances in real-time, providing immediate feedback and ensuring correct exercise execution. By allowing remote participation, our software eliminates the need for students to visit the sports complex, offering flexibility and convenience. Nowadays, the alternative can be for example an online conference with a trainer, but it will not solve the problem of timing: students still can not take a test at any time. Moreover, coaches still have no chance to oversee everyone. Our product will allow students to take an exam in a convenient time and the exam will be fair.


- **Benefits to Users:**

&nbsp;&nbsp;&nbsp;&nbsp;Our software project offers significant benefits for trainers by eliminating the need for physical presence at the sports complex and simplifying the process of collecting results. 

&nbsp;&nbsp;&nbsp;&nbsp;Students stand to gain numerous benefits from our software project, including the flexibility to take the fitness test at any time and the elimination of the need to visit the sports complex. This flexibility enables students to focus more effectively on their preparations. Moreover, our application ensures the correct execution of exercises, reducing the risk of injury.


- **Differentiation:**

&nbsp;&nbsp;&nbsp;&nbsp;Researching for the similar applications we found out an [app for yoga](https://apps.apple.com/ru/app/skill-yoga-train-mind-body/id1462051533), which defines points on the user's body and evaluates if the pose is correct. However, this application is not intended for fitness and cannot be launched from a browser. The main feature of our solution is a possibility to use it for the fitness test taking and checking the correctness of physical exercises. Our web application is a unique product on the Russian market, it will be free and will provide significant benefits to those who want to exercise safely. GymGuru will correct the technique of performing exercises and help achieve the desired result faster, as well as give Innopolis students the opportunity to take a fitness test without the need for presence in the sports complex.

- **User Impact:**

&nbsp;&nbsp;&nbsp;&nbsp;Overall, our product will save time for students and trainers, because they have no need to visit the sport complex. IU will save money for renting the SC and trainers` salary.  Moreover, students will be able to save a lot of time preparing for exams or to go home earlier. Also, students will have feedback about their technique and the risk of getting injured will be lower.


- **User Testimonials or Use Cases:**

Our web application will be useful for:
- Self-trainings: monitoring exercise techniques and enhancing the effectiveness of sports training.
- Fitness test: simplifying the examination process for both students and coaches.

We created the following Use Cases Diagram that shows possible use cases from user side and trainer side:

<img src="/2024/GymGuru/Week1_UseCases.jpg" width="640" height="720">

To describe the diagram above there are several user stories:

- As a student, I want to create an account or log in to existing one, so that I can view statistics on previous exercises performe .
- As a student, I want to receive tips on how to correct exercise technique, so that I can avoid injuries during the trainings and perform exercises more efficiently.
- As a student, I want to see video from camera, so that I can understand tips and correct mistakes immediately.
- As a student, I want to see the number of repetitions of an exercise, so that I can focus on the proper technique without worrying about counting.
- As a student, I want to review the correct exercise technique before starting my training, so that I can ensure I perform it correctly.
- As a student, I want to see the rating of users and understand my place, so that I can see the progress.
- As a student, I want to perform the exercises required for the fitness test, so that I can pass it without attending sport complex.
- As a coach, I want to create an account or log in to existing one, so that I can see the fitness test results for each student.
- As a coach, I want to download fitness test results for each student, so that I can upload them on the sport website and to the grade sheet.

## **Lean Questionnaire**

**1. What problem or need does your software project address?**
   
&nbsp;&nbsp;&nbsp;&nbsp;Self-training is the most popular training format, however, such training is often not supervised by professional trainers, which can lead to incorrect exercise technique. In turn, improper technique of performing exercises with additional weights can lead to the development of muscle imbalance and postural abnormalities, which can lead to injury and negatively affect health and performance in the long term. This application allows for independent monitoring of the accuracy of exercises in order to prevent potential consequences.

&nbsp;&nbsp;&nbsp;&nbsp;During the fitness test at the sports complex, students have to wait several times for their turn to enter their results at the table with the coach.  GymGURU will also help students take a fitness test without having to be present in person, which will help save time and make it easier to pass.

**2. Who are your target users or customers?**

&nbsp;&nbsp;&nbsp;&nbsp;People who practice sports without the supervision of professional coaches, students who want to take a fitness test out of turn and get a return on the correctness of the exercises.

**3. How will you validate and test your assumptions about the project?**

&nbsp;&nbsp;&nbsp;&nbsp;Surveys were conducted among students to identify specific needs in the field of sports. It is also planned to conduct interviews with trainers (experts in the field) to clarify the correctness of exercises and work with a fitness test.

**4. What metrics will you use to measure the success of your project?**

&nbsp;&nbsp;&nbsp;&nbsp; We defined several metrics, such as:

- The speed of recognition
- The number of supported physical exercises
- The satisfaction of a users during testing sessions (scales of assessment for convenience, ease of use, as well as suggestions/discontents)
- The correctness of advices given to improve the technique of performing physical exercises

**5. How do you plan to iterate and pivot if necessary based on user feedback?**

&nbsp;&nbsp;&nbsp;&nbsp;During the work process we are planning to conduct polls and testing sessions. Depending on the feedback from users, we will focus on the weak parts of our project and fix any bugs. Moreover, our team will conduct a meeting with experts to collect professional opinion about everything that will be done, and about missing by their view features that we will try to create.

## **Leveraging AI, Open-Source, and Experts**

&nbsp;&nbsp;&nbsp;&nbsp;Our team plans to leverage the following resources for the development and success of our project:

- **Artificial Intelligence (AI) and Open-Source:**

&nbsp;&nbsp;&nbsp;&nbsp;MediaPipe is the open source solution that provides  a suite of ML libraries and AI tools for multiple needs. For example we will use pose landmark detection that is human body position in sport exercises.

- **Experts:**

&nbsp;&nbsp;&nbsp;&nbsp;We are planning to contact Innopolis Sport Complex coaches to address several questions regarding correctness of physical exercises and the intricacies of passing physical standards (fitness test) in Innopolis. Moreover, we already have a deal with Yana Bogdanovich (teacher of the School of physical education and healthy lifestyle / Institute of Humanities and Social Sciences of Innopolis University) about QA session.

## **Defining the Vision for Your Project**

- **Overview:**

&nbsp;&nbsp;&nbsp;&nbsp;GymGURU is a web application for evaluating the correctness of performing physical exercises. Users put their device with an enabled camera in front of them during the exercise and receive feedback and tips on improving the technique from the application.

&nbsp;&nbsp;&nbsp;&nbsp;A large number of people, unaware of this, due to the incorrect technique perform useless or dangerous exercises during self training. This application makes it possible to independently monitor the correctness of the exercises in order to avoid injury.

&nbsp;&nbsp;&nbsp;&nbsp;In addition, it can be used to meet fitness tests in online format without the need for a coach. The web app determines the type of exercise, automatically records the quantity and quality of performance, and after completing the test compiles a table with results for all students and submits it to the coach instead of manually entering each person's information on a first come, first served basis during the gym test. 


- **Schematic Drawings:**

Schema of a flow of GymGuru working process:

<img src="/2024/GymGuru/Week1_SchematicDrawing.png" width="620" height="450">

We will use ML tool that determines a position of a human body, creating a simplified version of a skeleton:

<img src="/2024/GymGuru/Week1_MediaPipe.png" width="380" height="450">

After that, service will define a correctness of a physical exercise by calculating angles between lines and relative position of points.

- **Tech Stack:** 

*Frontend:* HTML, CSS, JavaScript, TailwindCSS
*Backend:* Python, Flask
*Database:* SQLite
*Open-Source ML Tool:* MediaPipe

**Why we use it:**

-- Flask: convenient for creating web applications on Python, we can use it to quickly obtain sufficient results

-- HTML + CSS + JS: base of a frontend

-- TailwindCSS: open-source CSS framework used to add styles to HTML elements that helps to adapt the app for different devices

-- Mediapipe: Open-Source ML Tool that allow us to determine coordinates of a human body, and then use it for the app purposes

**Important note:**

Tech stack can change during the working process because of different reasons, such as finding more sufficient language/framework/model or changing/appending features of a product we developing.

## **Reflection**

**Conclusions**

- During this week we create a team consisting of 7 members, each of us ready to work on the presented project and use our hard and soft skills in programming and team communication.
- We defined a project that will be implemented during summer semester
- We determined a roles of each team member
- Also, we conducted an analysis of existing solutions and created an expected view of MVP, which we will strive for

**Next Steps**

- Start to code the main logic of a web application, as well as frontend part

- Define a convenient flow of work with GitHub, create a list of issues depending on the tasks for the next week sprint

- Learn all principles of working with MediaPipe

**Challenges & Solutions**

We faced several troubles during this week, such as:

- Creating a team of 7 members, only after Wednesday we had a full team. Initially we organized a team of friends and classmates that already worked together, and then we found remaining members using google spreadsheet.

- Idea of a project came to our minds relatively quickly. However, to define all aspects we spent a lot of time. Well-organized teamwork and communication helped to solve all the issues and difficulties.

- We have encountered difficulties in writing a report that is quite voluminous and fully discloses the essence of the project. However, we were able to distribute the work so that we could quickly and accurately finish the report before the deadline.

The main lesson learned through these challenges is that through communication and the engagement of team members, we can solve our problems.
