---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

|      Team Member     |                     Telegram ID                    |            Email Address             |
|----------------------|----------------------------------------------------|--------------------------------------|
| Evgeny Bobkunov      | [@eugengold](https://t.me/eugengold)               | e.bobkunov@innopolis.university      |
| Matvey Korinenko     | [@m0t9_tg](https://t.me/m0t9_tg)                   | m.korinenko@innopolis.university     |
| Artur Mukhutdinov    | [@CatOrLeader](https://t.me/CatOrLeader)           | a.mukhutdinov@innopolis.university   |
| Daniil Prostiruk     | [@daniil_prostiruk](https://t.me/daniil_prostiruk) | d.prostiruk@innopolis.university     |
| Rufina Gafiiatullina | [@R_ufina](https://t.me/R_ufina)                   | r.gafiiatullina@innopolis.university |

### **Value Proposition**

{{<details "Identify the Problem">}}
Technical issues frequently occur in the dormitories, such as internet and electricity outages, or water supply interruptions. These failures adversely affect the quality of life for students. One significant challenge is the difficulty in determining whether a technical failure is local or more widespread. This ambiguity impedes the speed of problem resolution, leading to inefficiencies in maintenance and response times. The project aims to address these issues through improved monitoring of dormitory infrastructure at Innopolis University.
{{</details>}}

{{<details "Solution Description">}}
The proposed solution is to develop a public service where users can report technical failures by specifying the type of issue, its location, and other relevant details. The service will analyze these reports to determine if the problem is local or widespread. It will also notify other students and stakeholders, such as dormitory management, about the issues. This will help speed up the identification and resolution of problems. Users will interact with the service through a Telegram bot, which will allow them to report issues and receive notifications about common problems.
 {{</details>}}

{{<details "Benefits to Users">}}
**Real-time Reporting:** Users can instantly report technical issues via the Telegram-bot, eliminating the need to navigate through complex systems or wait for office hours. This immediacy streamlines the reporting process, allowing students to quickly notify dorm management of problems without disrupting their schedules.<br/>
**Automated Notifications:** Once a problem is reported, the system automatically notifies other affected users and relevant stakeholders. This reduces the lag time between identifying an issue and beginning the resolution process, ensuring that maintenance teams can address problems more swiftly.<br/>
**Local vs. General Issue Identification:** The service's ability to analyze reports and distinguish between local and widespread issues helps prioritize responses.<br/>
**Crowd-sourced Data:** Leveraging community input provides a more accurate picture of dormitory infrastructure status, ensuring that even minor issues are brought to attention before they escalate.<br/>
**Reduced Downtime:** Faster identification and resolution of issues mean less downtime for critical services like internet, electricity, and water. This improves the overall living conditions for students.<br/>
**Efficient Resource Allocation:** By distinguishing between local and general issues, maintenance teams can allocate their resources more effectively, focusing on urgent problems first and optimizing repair schedules. This leads to cost savings in labor and materials.<br/>
**Communication Convenience:** The use of a Telegram bot simplifies the communication process. Users can quickly report problems and receive updates without needing to check multiple platforms or contact multiple parties. This efficiency saves time for both students and maintenance staff.<br/>
**User-Friendly Interface:** The familiar and intuitive interface of Telegram ensures that students can easily interact with the service. This accessibility encourages more consistent use and reporting.
 {{</details>}}

{{<details "Differentiation">}} **Existing Solutions**<br/>
There are similar projects for infrastructure monitoring in Russia. For example, a government information system for housing and utilitie ["ГИС ЖКХ"](https://giszhkh.ru) that allows residents to report problems and track the status of their maintenance requests. An initiative by the Moscow government ["Активный гражданин"](https://ag.mos.ru) allows citizens to report and vote on issues related to city improvements, including infrastructure and maintenance needs. There are also similar ideas abroad. A platform ["SeeClickFix"](https://seeclickfix.com) allows citizens to report non-emergency issues in their communities, such as potholes or broken streetlights. It integrates with government systems to facilitate quicker responses. One more web-based application ["FixMyStreet"](https://www.fixmystreet.com) enables residents to report local problems like graffiti or road damage to the appropriate authorities.

**Unique points of our software project**<br/>
The project is specifically designed for <u>dormitory infrastructure</u> at Innopolis University. Our solution incorporates <u>real-time feedback</u> from the student community, enabling a faster and more accurate assessment of whether an issue is local or widespread. Unlike traditional facility management systems, our platform relies on <u>crowd-sourced data</u> to improve response times and accuracy. Moreover, the Telegram-bot provides a simple, <u>intuitive interface</u> for users to report issues and receive updates without the need for a separate app or complex navigation. This simplicity and ease of access encourage higher user engagement and quicker reporting, which is critical for timely issue resolution.
 {{</details>}}

{{<details "User Impact">}} 
**Enhanced Living Conditions:** By ensuring timely resolution of infrastructure issues, the project directly improves the quality of life for students.<br/>
**Reduced Stress:** Students are less likely to experience stress related to unresolved technical issues. This contributes to better mental well-being and allows students to focus more on their studies and personal development.<br/>
**Model for Other Universities:** The success of this project at Innopolis University can serve as a model for other educational institutions. It demonstrates the potential of integrating community feedback and technology to enhance facility management.<br/>
**Flexibility:** The solution's design allows it to be adapted for various settings beyond dormitories, such as office buildings, residential complexes, and public facilities.<br/>
**Better Resource Management:** The data collected through user reports enables more accurate forecasting and planning. This leads to better allocation of resources and improved long-term infrastructure planning.
 {{</details>}}

{{<details "User Testimonials or Use Cases">}} 
To demonstrate the utility and relevance of our project, we examined the [use case](https://seeclickfix.com/media/seeslickfix_case_study.pdf) of the SeeClickFix application. The integration of Cityworks and SeeClickFix in New Haven has revolutionized the city's response to infrastructure problems by automating issue routing and communication, resulting in improved response times and operational efficiency. Since its implementation in 2008, the system has managed over 20,000 pothole reports and nearly 38,000 resident inquiries, enabling departments such as Transportation, Traffic and Parking, and Public Works to better prioritize and resolve issues with less work time. This streamlined process has increased public engagement, transparency, and data-driven decision-making, significantly enhancing the overall quality of public service delivery.

Similarly, our service can improve the quality of life for students in dormitories.
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

- We will use these programming languages with open-source code: [Python](https://github.com/python/cpython) , [Go](https://github.com/golang)
- For a Telegram bot we will use popular open-source libraries like [Aiogram](https://github.com/aiogram/aiogram)
- For writing code and reports - [Visual Studio Code](https://github.com/microsoft/vscode)

### Experts

At the moment we have not involved any experts yet.

## **Defining the Vision for Your Project**

- Overview: our microservice architecture features a Telegram bot as the front-end, an API to handle user-submitted reports, a database to store report details, and an admin panel for monitoring outages and creating graphs.

- Schematic Drawings:

#### Backend architecture scheme

<img src="/2024/Monidorm/backend_architecture.drawio.png"> 

- Possible Tech Stack:
   - Backend:
      - API server: Java, Golang
   - Frontend:
      - Telegram bot: Python
      - Admin-panel: Svelte, Grafana, Prometheus
   - Database: Postgres, MongoDB

## **Distribution of roles in the team**

- **Evgeny**: Project Manager, Reports writer

- **Matvey**: Team Lead, Backend & Telegram-Bot Developer

- **Artur**: Deputy Team Lead, Backend Developer, Manager

- **Daniil**: Frontend Developer, Reports writer

- **Rufina**: Data Science engineer, Reports writer

## **UX Research**

To confirm the assumptions about the demand for the product, we decided to do a little UX research.

### Interview

Firstly, we compiled a list of interview questions and found candidates that fit the target audience

{{<details "List of interview questions">}}
- How often do you have breakdowns/failures?
- How do you find out about them? 
- How/where do you report them? 
- Are you comfortable with it? 
- Would you like to know about breakdowns? (Where they happen). 
- Do you know any services like [downdetector](https://downdetector.com/)?
{{</details>}}

Then We conducted a one-on-one interviews, with a recording of the conversation:

{{< audio src="/2024/MoniDorm/monidorm_interview_1.mp3" >}}


{{< audio src="/2024/MoniDorm/monidorm_interview_2.mp3" >}}

From these interviews, we confirmed a few hunches regarding user needs and pains:
1. They do not like the system of reports about breakdowns
2. They faced with situations, when they do not understand region of failure

### Research among student chats
We've often noticed that students ask about outages in chats — this means that there is a problem and needs a more user-friendly solution:
<img src="/2024/Monidorm/chat_research_1.jpg"> 


> "- Has everyone's internet stopped working? - Everything seems to be fine."

## **Conclusion**

This week we built a team and came up with an idea for a project. As part of the sprint, we held two large-scale meetings with the whole team. We set up a [GitLab](https://gitlab.pg.innopolis.university/capstone-project/monidorm) environment right away, but later migrated to [GitHub](https://github.com/IU-Capstone-Project-2024/MoniDorm) due to requirements. We started using the tasks, issues and milestones system to work efficiently. We also maintain a [wiki](https://github.com/IU-Capstone-Project-2024/MoniDorm/wiki) page with all the artefacts from the collaborative work in the remote repository. Also we have started doing UX research to get user feedback. Next week we plan to develop a prototype, create a codebase for the project, and think about design and style.
