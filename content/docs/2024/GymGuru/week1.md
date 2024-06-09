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

&nbsp;&nbsp;&nbsp;&nbsp;In the Innopolis University the Sport exam flows in the following way: at the end of the semester students choose the timeslot to take the fitness test, then come to the sport complex and take a tilt one-by-one, then take crunches in pairs and do push-ups without trainer control. At the end students say the results to the trainer one-by-one. 
&nbsp;&nbsp;&nbsp;&nbsp;There is a possibility that the following problems could emerge in this situation: during the exams students have to come to the SC, moreover, the time slots could be inconvenient. Additionally, coaches are not able to supervise everyone simultaneously, hence students may do exercises in the wrong way or cheat. Incorrect exercise technique may cause injuries. Summarizing, students and trainers must visit SC just to do monotonic work. 
&nbsp;&nbsp;&nbsp;&nbsp;We conducted a survey among students to identify existing problems and to gather students' opinions on the feasibility of conducting fitness tests online


<p float="left">
  <img src="/2024/GymGuru/Week1_Pool1.png" width="320" height="480">
  <img src="/2024/GymGuru/Week1_Pool2.png" width="320" height="320">
</p>




- **Solution Description:**

&nbsp;&nbsp;&nbsp;&nbsp;Our solution leverages pose estimation and exercise recognition to evaluate students' fitness performances in real-time, providing immediate feedback and ensuring correct exercise execution. By allowing remote participation, our software eliminates the need for students to visit the sports complex, offering flexibility and convenience. Nowadays, the alternative can be for example an online conference with a trainer, but it will not solve the problem of timing: students still can not take a test at any time. Moreover, coaches still have no chance to oversee everyone, which may give rise to the following issue: students' trauma due to the incorrect technique. Our product will allow students to take an exam in a convenient time and the exam will be fair.


- **Benefits to Users:**

&nbsp;&nbsp;&nbsp;&nbsp;Our software project offers significant benefits for trainers by eliminating the need for physical presence at the sports complex and simplifying the process of collecting results. 
&nbsp;&nbsp;&nbsp;&nbsp;Students stand to gain numerous benefits from our software project, including the flexibility to take the fitness test at any time and the elimination of the need to visit the sports complex. This flexibility enables students to focus more effectively on their preparations. Moreover, our application ensures the correct execution of exercises, reducing the risk of injury.



- **Differentiation:**

&nbsp;&nbsp;&nbsp;&nbsp;Researching for the similar applications we found out [[1]](https://apps.apple.com/ru/app/skill-yoga-train-mind-body/id1462051533) an app for yoga, which defines points on the user's body and evaluates if the pose is correct. However, this application is in English, and it is not intended for fitness and cannot be launched from a browser.. The main feature of our solution is a possibility to use it for the fitness test taking and checking the correctness of physical exercises. Our web application is a unique product on the Russian market, it will be free and will provide significant benefits to those who want to exercise safely. GymGURU will correct the technique of performing exercises and help achieve the desired result faster, as well as give Innopolis students the opportunity to take a fitness test without the need for full-time presence in the sports complex.

- **User Impact:**

&nbsp;&nbsp;&nbsp;&nbsp;Overall, our product will save time for students and trainers, because they have no need to visit the sport complex. IU will save money for renting the SC and trainers` salary.  Moreover, students will be able to save a lot of time preparing for exams or to go home earlier. Also, students will have feedback about their technique and the risk of getting injured will be lower.


- **User Testimonials or Use Cases:**

&nbsp;&nbsp;&nbsp;&nbsp;According to a All-Russian Center for the Study of Public Opinion study, more than half of Russians are engaged in sports or physical education, and fitness ranks second in popularity [[2]](https://wciom.ru/analytical-reviews/analiticheskii-obzor/sportivnaja-rossija). Self-training is the most popular training format [[2]](https://wciom.ru/analytical-reviews/analiticheskii-obzor/sportivnaja-rossija), however, such training is often not supervised by professional trainers, which can lead to incorrect exercise technique. Coach Tansu Sungatova notes that incorrect technique can make exercises useless or even lead to injuries [[3]](https://entermedia.io/people/15-glupyh-voprosov-o-trenirovkah-doma/). Using the GymGURU could prevent the wrong technique of performing the exercise and save you from getting seriously injured.

## **Lean Questionnaire**

**1. What problem or need does your software project address?**
   
&nbsp;&nbsp;&nbsp;&nbsp;Self-training is the most popular training format, however, such training is often not supervised by professional trainers, which can lead to incorrect exercise technique. In turn, improper technique of performing exercises with additional weights can lead to the development of muscle imbalance and postural abnormalities, which can lead to injury and negatively affect health and performance in the long term. This application allows for independent monitoring of the accuracy of exercises in order to prevent potential consequences. GymGURU will also help students take fitness tests without having to stand in queue while participating in the test in the sports complex.


**2. Who are your target users or customers?**

&nbsp;&nbsp;&nbsp;&nbsp;People who practice sports without the supervision of professional coaches, students who want to take a fitness test out of turn and get a return on the correctness of the exercises.

**3. How will you validate and test your assumptions about the project?**

&nbsp;&nbsp;&nbsp;&nbsp;Surveys were conducted among students to identify specific needs in the field of sports. It is also planned to conduct interviews with trainers (experts in the field) to clarify the correctness of exercises and work with a fitness test.

**4. What metrics will you use to measure the success of your project?**

&nbsp;&nbsp;&nbsp;&nbsp; We defined several metrics, such as:

- The accuracy of recognizing the quality and quantity of exercises performed
- The speed of recognition
- The number of users of the web application

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

-- TailwindCSS: open-source CSS framework used to style each element by mixing and matching, by using that we can adopt the app for different devices

-- Mediapipe: Open-Source ML Tool that allow us to determine coordinates of a human body, and then use it for the app purposes

**Important note:**

Tech stack can change during the working process because of different reasons, such as finding more sufficient language/framework/model or changing/appending features of a product we developing.

## **Reflection**

**What was done**

- During this week we create a team consisting of 7 members, each of us ready to work on the presented project and use our hard and soft skills in programming and team communication.
- We defined a project that will be implemented during summer semester
- We determined a roles of each team member
- Also, we conducted an analysis of existing solutions and created an expected view of MVP, which we will strive for

**Challenges**

We faced several troubles during this week, such as:

- Creating a team of 7 members, only after Wednesday we had a full team. Initially we organized a team of friends and classmates that already worked together, and then we found remaining members using google spreadsheet.

- Idea of a project came to our minds relatively quickly. However, to define all aspects we spent a lot of time. Well-organized teamwork and communication helped to solve all the issues and difficulties.

- We have encountered difficulties in writing a report that is quite voluminous and fully discloses the essence of the project. However, we were able to distribute the work so that we could quickly and accurately finish the report before the deadline.

**Next Steps**

- Start to code the main logic of a web application, as well as frontend part

- Define a convenient flow of work with GitHub, create a list of issues depending on the tasks for the next week sprint

- Learn all principles of working with MediaPipe

## **References**

[1] - https://apps.apple.com/ru/app/skill-yoga-train-mind-body/id1462051533

[2] - https://wciom.ru/analytical-reviews/analiticheskii-obzor/sportivnaja-rossija

[3] - https://entermedia.io/people/15-glupyh-voprosov-o-trenirovkah-doma/

