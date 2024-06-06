---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Evgeny Bobkunov     | [@eugengold](https://t.me/eugengold) | e.bobkunov@innopolis.university |
| Matvey Korinenko            | [@m0t9_tg](https://t.me/m0t9_tg) | m.korinenko@innopolis.university |
| Artur Mukhutdinov            | [@CatOrLeader](https://t.me/CatOrLeader) | a.mukhutdinov@innopolis.university |
| Daniil Prostiruk            | [@daniil_prostiruk](https://t.me/daniil_prostiruk) | d.prostiruk@innopolis.university |
| Rufina Gafiiatullina            | [@R_ufina](https://t.me/R_ufina) | r.gafiiatullina@innopolis.university |

### **Value Proposition**

{{<details "Identify the Problem">}}
Technical issues frequently occur in the dormitories, such as internet and electricity outages, or water supply interruptions. These failures adversely affect the quality of life for students. One significant challenge is the difficulty in determining whether a technical failure is local or more widespread. This ambiguity impedes the speed of problem resolution, leading to inefficiencies in maintenance and response times. The project aims to address these issues through improved monitoring of dormitory infrastructure at Innopolis University.
{{</details>}}

{{<details "Solution Description">}}
The proposed solution is to develop a public service where users can report technical failures by specifying the type of issue, its location, and other relevant details. The service will analyze these reports to determine if the problem is local or widespread. It will also notify other students and stakeholders, such as dormitory management, about the issues. This will help speed up the identification and resolution of problems. Users will interact with the service through a Telegram bot, which will allow them to report issues and receive notifications about common problems.
 {{</details>}}

{{<details "Benefits to Users">}}
...
 {{</details>}}

{{<details "Differentiation">}} **Existing Solutions**<br/>
There are similar projects for infrastructure monitoring in Russia. For example, a government information system for housing and utilitie "ГИС ЖКХ" that allows residents to report problems and track the status of their maintenance requests. An initiative by the Moscow government "Активный гражданин" allows citizens to report and vote on issues related to city improvements, including infrastructure and maintenance needs. There are also similar ideas abroad. A platform "SeeClickFix" allows citizens to report non-emergency issues in their communities, such as potholes or broken streetlights. It integrates with government systems to facilitate quicker responses. One more web-based application "FixMyStreet" enables residents to report local problems like graffiti or road damage to the appropriate authorities.

**Unique points of our software project**<br/>
The project is specifically designed for <u>dormitory infrastructure</u> at Innopolis University. Our solution incorporates <u>real-time feedback</u> from the student community, enabling a faster and more accurate assessment of whether an issue is local or widespread. Unlike traditional facility management systems, our platform relies on <u>crowd-sourced data</u> to improve response times and accuracy. Moreover, the Telegram-bot provides a simple, <u>intuitive interface</u> for users to report issues and receive updates without the need for a separate app or complex navigation. This simplicity and ease of access encourage higher user engagement and quicker reporting, which is critical for timely issue resolution.
 {{</details>}}

{{<details "User Impact">}} 
...
 {{</details>}}

{{<details "User Testimonials or Use Cases">}} 
...
 {{</details>}}

## **Lean Questionnaire**

### 1. What problem or need does your software project address?

Our project aims to solve the problem of identifying breakdowns and malfunctions in a dormitory building. It is designed to simplify the process of reporting breakdowns and identifying the area where they occur. This will solve the problem of people not realizing whether a breakdown is local or general. An example of a breakdown: the internet is not working and it is not clear whether it is only in one room or in the whole building, or maybe in all buildings.

### 2. Who are your target users or customers?

Our target users are the people who live on campus. This includes students, university staff, visitors and guests. In addition, our platform can be useful for dormitory and admissions staff as a support tool to quickly repair issues that have arisen

### 3. How will you validate and test your assumptions about the project?

To validate and test our assumptions firstly, we will conduct a UX research on “How comfortable are you with finding out about breakdowns and failures in the dormitory building”. This research will include a survey and interviews with students who live in the dorm.

### 4. What metrics will you use to measure the success of your project?

We will measure the success of our project based on the following metrics:

- User trust factor: How users trust our service, do they share actual issues. Will they provide us information about their rooms.

- Number of Users: The more users our service has, the more efficiently and quickly faults will be detected.

- Failure detection accuracy: We will collect big amount of reports and compare them with actual issues. This ratio will be one of crutial metrics.

### 5. How do you plan to iterate and pivot if necessary based on user feedback?

As our workflow is based on Agile, Lean and Scrum principles, We can adapt to any changes in requirements very easily. Among other things, we are going to develop the project based on feedback from users and survey participants.

## **Leveraging AI, Open-Source, and Experts**

### AI (Artifitial Intelligence)

Our team will use generative AI models like ChatGPT and Github Copilot to increase our development speed.

### Open-Source

For a Telegram bot we will use popular open-source libraries like Aiogram etc.

### Experts

At the moment we have not involved any experts yet.

## **Defining the Vision for Your Project**

- Overview: our microservice architecture features a Telegram bot as the front-end, an API to handle user-submitted reports, a database to store report details, and an admin panel for monitoring outages and creating graphs.

- Schematic Drawings:

#### Backend architecture scheme

<img src="/2024/Monidorm/backend_architecture.drawio.png"> 

- Tech Stack:
   - Backend:
      - API server: Java, Golang
   - Frontend:
      - Telegram bot: Python
      - Admin-panel: Svelte, Graphana, Prometheus
   - Database: Postgres, MongoDB

## **Distribution of roles in the team**

- Evgeny: Project Manager, GitLab environment maintainer (Issues, Milestones, Time Tracking), CI/CD, Reports

- Matvey: Team Lead, Backend (GoLang), Telegram-Bot (Python), Docker

- Artur: Deputy Team Lead, Backend (Java), GitLab environment maintainer

- Daniil: Frontend (Svelte), CI/CD, Reports

- Rufina: Data Science, Python, Reports
