---
weight: 1
bookFlatSection: true
title: "InnoMastery"
---
<img src="/InnoMastery/logo.png" alt="Tuxi" width="300"/> \
**Welcome to InnoMastery — a new course platform for everyone!**

# **Week #1 Report**

## Team Members

| Team Member        | Telegram ID                                          | Email Address                       |
| ------------------ | ---------------------------------------------------- | ----------------------------------- |
| Fedor Ivanov       | [@fedor_ivn](https://t.me/fedor_ivn)                 | f.ivanov@innopolis.university       |
| Andrei Markov      | [@markovav_official](https://t.me/markovav_official) | a.markov@innopolis.university       |
| Artem Starikov     | [@snejugal](https://t.me/snejugal)                   | a.starikov@innopolis.university     |
| Dmitrii Alekhin    | [@dmfrpro](https://t.me/dmfrpro)                     | d.alekhin@innopolis.university      |
| Leila Khaertdinova | [@leila1kh](https://t.me/leila1kh)                   | l.khaertdinova@innopolis.university |
| Roman Molochkov    | [@roman_molochkov](https://t.me/roman_molochkov)     | r.molochkov@innopolis.university    |

## Value Proposition

While there are many course platforms with quality offerings, their testing systems are often limited and inflexible. Most of the testing systems provide a simple input/output checking of students’ code, but this approach is inapplicable to courses related to information security, Linux administration, etc.

Our course platform will offer deep and qualified learning and development opportunities for students. We plan to introduce a containerized online IDE based on VSCode that will provide a seamless experience for students. During coding exercises, a GPT-3.5 chatbot will be available to help students overcome obstacles in real-time. Instead of feeling stuck or frustrated with an exercise, they will receive personalized hints and guidance from the chatbot, making the learning experience smoother and more engaging. A testing system with automating grader will be implemented server-side, thus guaranteeing more robust practice tasks evaluation.

In our vision, containerized online IDE will decrease installation requirements for the student as it requires only a browser installed. Both the testing system with hints and the chatbot will prevent the student from getting stuck on difficult parts of exercises. Thus, our course platform will change the world of IT courses.

## Lean Startup Questionnaire

> What problem or need does your software project address?

The application we are designing is made to fulfill the market of online courses, providing flexible ways to customize theoretical material, questions for self-evaluation and practical exercises. Our mission is to take the best out of the existing market solutions such as progress monitoring, course structure, navigation, and introduce a powerful solution by adding what in our opinion is crucially important during the studying process (i.e. practical assignments).

> Who are your target users or customers?

Our target users are IT companies and computer science engineers, willing to acquire new skills, taught via courses on our platform. 

> How will you validate and test your assumptions about the project?

There are many things to test in our project. In particular, articles with theoretical material are subjects to test themselves. We are going to gather feedback about them from the commentary section in order to fix weak points, clarify the theory, share useful resources, etc. Additionally, we will maintain a group of potential clients to test our assumptions about the software component of the course and gather feedback on this part. This will help us to create an objective vision on our product, since the client feedback is a reliable source of features usefulness.

> What metrics will you use to measure the success of your project?

To measure the success of the project, we will use several metrics. Firstly, since our project is a web application, we want to maximize uptime of our website. Secondly, since the project is commercially dependent on the number of people involved in our course, good metrics will be reviews and feedback from the test group. Lastly, when the project will be published, a suitable metric will be our product conversion rate.

> How do you plan to iterate and pivot if necessary based on user feedback?

As previously stated, we plan to thoroughly collect user feedback and consider it during the whole development. To provide an ease of modification, the project will be designed in such a way that it can be decomposed into separate components without disrupting the overall system. For instance, a language-model based chatbot should exist independently from the other parts of the project. To facilitate this, we will incorporate a "global kill" feature for each of the "cool" features, ensuring that they can be safely removed without affecting the entire system.

## Leveraging AI, Open-Source, and Experts

### Leveraging AI

We plan to use AI in both the product development and the product itself.

For software development, we will use:
- Copilot, a tool developed by OpenAI in collaboration with GitHub that will greatly speed up the development of our product. It offers relevant code snippets based on the context, which allows to quickly implement ready-made solutions and ideas.
- ChatGPT, a tool from OpenAI will help us quickly answer questions during development, explain how to work with new libraries and resolve bugs.

In the product itself, we plan to add an AI-powered chatbot that will be able to analyze student solutions, understand their questions and provide appropriate explanations and hints, without providing the correct solution directly. It will also be able to offer additional study materials, tasks that can help students enhance their knowledge in a particular topic.

### Open Source

To accelerate the development of our product, we will use ready-made open source software:
- Coder, an open-source application that can be deployed on your own server and provides students with access to a development environment. Installing and configuring Coder on the server will allow us to create a private development environment where students can write, edit and test their code without the need to install and configure tools on their own machines.

### Experts

For advice on various issues that may arise during development, specifically with implementing AI chatbot, we will refer to:
- Rustam Lukmanov: Capstone Project course instructor, has diverse background in analytical techniques and computational methods;
- Vladimir Ivanov: Professor of Applied Statistics and Practical Machine Learning and Deep Learning courses.

## Defining the Vision for Your Project

### Overview

Our application will have a simple, minimalistic and easy-to-use interface. It will be easy to navigate in the course between lessons and between tasks. Interactive articles will help students to understand the material better and build intuition of the subject. We will put lots of effort into building a useful automatic grader for practical tasks. Overall, our platform will be effective and enjoyable.

### Detailed description

#### User flow

The user starts with visiting our website where they will create an account and sign up for our course. After that, they can start studying right away.

The course consists of chapters which contain several lessons. First, the student studies a particular lesson. If they have a question, they can ask it in the comments where we as well as other students can discuss it. Otherwise, they can continue with solving tasks. The first tasks are short, designed for self-evaluation. Tasks in the end are bigger and oriented for applying new knowledge in practice. They require writing code, and meant to be solved in our online IDE with an autograder and a linter. 
Whenever the student gets stuck, they can ask our chatbot for help.

Below is a graphical illustration of the user flow.

![User flow](/InnoMastery/user_flow.svg)

Several aspects will make our platform distinct among others. First, the student will be asked small questions while reading an article before going on (similar to how a TA can ask questions during a class). These questions are aimed to improve the student’s intuition, and will make studying more interactive.

Second, we will implement an automatic grader for practical tasks designed to help the student learn. Grading criteria will be descriptive, with hints in case a particular criterion failed. Moreover, the student’s solution will be linted to guide them to writing clear and concise code.

#### Architecture
Our project consists of four major components. The first component is a website for our course platform. We’re going to use TypeScript and React.js to build it. These technologies have been in wide use for a long time, and our team is already familiar with these.

The second component is the backend server for the course platform. We will build it using Python. For the database, we will use PostgreSQL. Our website will communicate with the server using GraphQL. To implement the GraphQL API, we will utilize the Strawberry framework.

The third component is the online IDE. We’re going to use Coder, an open-source remote development platform. With a simple Docker configuration, it provides a ready-made platform for managing users, workspaces and workspace templates. Moreover, it allows users to open their workspace in an online VSCode instance. We will only need to prepare our template with preconfigured extensions and editor settings, so students can start to solve tasks right away.

The fourth component is our chatbot. We’re planning to use language models, which will allow our educators to have personalized support 24/7. We haven’t decided yet on a particular language model or the way we are going to integrate it in our project, however we have several directions to research:
1. Prompt engineering using existing market solutions (e.g. GPT-3.5);
2. Fine-tuning open-source models for our purposes (e.g. LLaMA);
3. Training existing architectures entirely on our dataset followed by the usage of specific prompt techniques such as chain of thoughts or tree of thoughts.

Overall, our project will have the following architecture.

![Architecture](/InnoMastery/architecture.svg)

### Anticipating Future Problems

Despite our preparations, there are still potential future problems that we may face during the development and deployment phases. Firstly, one of the biggest obstacles could be the lack of experience in developing such a platform. To mitigate this, we will conduct thorough research and seek mentorship from experts to ensure that we are on the right path.

Secondly, we may encounter security issues as we store user data and sensitive information. Our team will work together, adhering to encryption standards and best practices, such as double checking the code during peer reviews, to ensure the platform's security and integrity.

Thirdly, we will need a plan in place for unexpected technical issues, such as server or database failures or system crashes, which might disrupt the platform's operation. By developing a comprehensive disaster recovery plan that includes backup solutions and redundancy measures, we will be able to ensure that the system continues to operate smoothly even under difficult circumstances.

Overall, we are committed to delivering a high-quality platform for our Linux courses and will work on overcoming any future challenges that may arise during the entire development and deployment phases.

{{< hint danger >}}
**Feedback by Rustam**  

I think this project is in very good hands - you have a sound vision and well-thought design of the product.
Strongest section - Architecture. Perhaps, you can have a look for good solutions on Yandex Practicum and some other major e-learning platforms  
Overall, 5/5
P.S. I've changed the structure of the reports, please write following reports in the same file
{{< /hint >}}



# **Week #2 Report**

## Architecture Design

1. **Component Breakdown:** \
![Architecture](/InnoMastery/architecture.svg) \
According to the diagram above, we have 5 major components: Course platform’s frontend, Course platform’s backend, Coder platform, Database, and AI chatbot. Their functionality is as follows:
    - The frontend provides a user-friendly interface for students of our courses (uses backend to build the UI, and our AI chatbot to help participants throughout the course)
    - The backend connects all components together (fetches the necessary data from the database, provides this data to frontend, acts as an OpenID provider for Coder)
    - Coder provides an online IDE and access to our grader for practical tasks (the grader is not part of our current project).
    - The database reliably stores and provides access to data.
    - The AI-powered chatbot suggests further reading and helps with task solving based on the current user progress.

2. **Data Management:** \
We are going to use PostgreSQL as our main database to ensure high data security as well as scalability of our project. In Python, we use SLQAlchemy as an ORM.

3. **User Interface (UI) Design:** \
![UI](/InnoMastery/UI.png)

4. **Integration and APIs:** \
In our project, we plan to integrate with Coder, an open-source platform for remote development. Using this platform, students will solve practical tasks from our platform.

5. **Scalability and Performance:** \
For better service performance, we plan to utilize microservice architecture. It will allow our platform to be scalable, maintainable and performant.

6. **Security and Privacy:** \
In our project, we will implement HyperText Transfer Protocol Secure (HTTPS) technology to protect data during client communication with our server. Security will also be provided through password hashing and an authentication system, guaranteeing the protection of user accounts.

7. **Error Handling and Resilience:** \
For tracking bugs that may occur during production, we plan to use a tool called Sentry. It will help us to ensure more stable and reliable software, as well as respond quickly to problems and increase user satisfaction.

8. **Deployment and DevOps:** \
On GitLab, we set up several rules for our project. First of all, before merging to master, all the auto checks must pass and at least 2 people must review incoming pull requests. Second, for faster deployment, all of our services are going to be in Docker containers. Third, all Docker images and deployment will be done by GitLab CI/CD.

## Questionnaire

1. **Tech Stack Resources:** \
We are not utilizing any project-based books dedicated to our tech stack. However, we actively consider exploring relevant online resources and documentation to enhance our knowledge and expertise in our tech stack.

2. **Mentorship Support:** \
As we had already mentioned in our previous report, we reached out to Rustam Lukmanov, who is the instructor for the Capstone Project course, and Vladimir Ivanov, who teaches the Applied Statistics and Deep Learning courses at our university. \
Our goal was to consult with them regarding the development of an AI-powered chatbot based on a language model. So, they provided us with remarkable insights and techniques that we can utilize during the development process. We strongly believe that having such mentorship from our teaching staff can greatly assist our team. This can help us identify new opportunities and overcome challenges by sharing their knowledge and expertise in this particular domain.

3. **Exploring Alternative Resources:** \
We explored the documentation and tutorials of the technologies that we plan to use in our project. One of these resources is [<ins>Coder API documentation</ins>](https://coder.com/docs/v2/latest/api), which we need since we need to connect our platform with Coder (e.g. to allow users to sign in to Coder with their account on our platform). Since Coder uses OpenID for authentication, we also need to study its specification. In addition, the [<ins>How to GraphQL</ins>](https://www.howtographql.com/) tutorial is relevant for us because most of our team is not familiar with this technology. Last but not least is [<ins>OpenAI’s documentation</ins>](https://platform.openai.com/docs/guides/gpt), which we need to build our assistant chatbot.

4. **Identifying Knowledge Gaps:** \
While we’re going to use GraphQL for building our API, only a couple teammates have worked with it in the past. Hence, our frontend and backend developers have skimmed through GraphQL tutorials and looked into libraries that they can use with GraphQL: [<ins>Apollo Client</ins>](https://www.apollographql.com/apollo-client/) for using the API on frontend and [<ins>strawberry</ins>](https://strawberry.rocks/) for building it on the backend. Moreover, our backend developers are currently learning how to use [<ins>FastAPI</ins>](https://fastapi.tiangolo.com/) for building the server and [<ins>SQLAlchemy</ins>](https://www.sqlalchemy.org/) for communicating with the database. Of course, our teammates share their experience with others in the team.

5. **Engaging with the Tech Community:** \
For now, we do not attend any community meetings or forums because they are not organized frequently.

{{< hint danger >}}
**Feedback by Rustam**  
One of the reason for having on open blog was that students can see which tech others are using. Generally speaking, you can organize such events yourself - professional networks are among major factors of success for tech projects.
{{< /hint >}}

6. **Learning Objectives:** \
Our backend developers decided to learn popular Python libraries such as FastAPI, SQLAlchemy, and strawberry, as these libraries are used for building lightweight projects. For now, in most cases, technical documentations cover the problems we face. Furthermore, we watch introductory guides on YouTube for quick start, especially for understanding the syntax.

7. **Sharing Knowledge with Peers:** \
For our team, we decided to hold weekly meetings on Wednesdays. At these meetings, we usually discuss upcoming tasks together, thereby getting ideas from each other on how to perform these tasks in the most efficient way. Each participant has its own view on the task and it is important to share this view with the peers. \
Besides, during the week, we keep in touch in our team's chat and call on teammates who are better versed in a certain topic to help cope with difficulties. This helps us quickly solve various issues at any time in our chat.

8. **How have you leveraged AI to compensate for any lacking expertise in your tech stack? Have you utilized AI-powered tools or platforms to expedite the process of acquiring knowledge and expertise in your tech stack?** \
Yes, we leverage AI to compensate for any lacking expertise in our tech stack. For example:
    - We have used ChatGPT often on various issues, from studying the framework to finding a new one that will suit our needs better. We also want to mention that it was more pleasant to work with ChatGPT since it did not have a limit on sending messages, as well as the length of the message. One can also note the fast speed of the answer, which was in turn correct.
    - Using various tools such as Logoai and Midjourney, we tried to create our logo, as well as get some images from them that we could add to our platform.
    - We use Copilot in development, for the most part it helps a lot with new frameworks, in which we are not particularly strong yet.
    - You.com simplifies searching for new information, thus getting it faster.

## Tech Stack and Team Allocation

After our first team meeting, we took into account each team member's strengths and preferences and used that to assign them to one of our three units: Frontend, Backend, and ML. Each unit has a designated lead responsible for overseeing its tasks. While team members primarily work on tasks related to their unit, they are not limited to those tasks only.

To give a better understanding of our project structure and information on our technology stack, please refer to sections above.

We have divided the areas of responsibility within the team according to the following table:

| Team Member | Role | Responsibilities |
| - | - | - |
| Fedor Ivanov | Team Lead, DevOps | Meetings facilitation, Project & People management, Participation in System Design. <br> DevOps and System Administration. |
| Andrei Markov | Frontend developer, Architect | Frontend development, System Design. |
| Artem Starikov | System Designer, Lead Frontend | System Design, Building layouts in Figma, Frontend development. |
| Dmitrii Alekhin | Backend developer | Database administration, building interaction with PostgreSQL. |
| Leila Khaertdinova | Lead ML engineer | Prompt-engineering, research. |
| Roman Molochkov | Lead Backend | Management within Backend Unit, Backend development. |
| Timofey Sedov | Backend developer, ML engineer | Backend development, Docker-related chores, Expertise in ML. |


{{< hint danger >}}
**Feedback by Rustam**  
Frontend design and overall project handling is outstanding. Keep up the pace and make sure to quickly iterate and pivot on technologies if necessary.
{{< /hint >}}


{{< hint danger >}}
**Feedback**  


**1. Component Breakdown**

Good, but the component isn’t really connected. I mean what is the difference between AI chatbot and Backend?  Different services or same backend? 

**2. Data Management**

Good

**3. UI Design**

I like the design very much.

**4. Integration and APIs**

Missing

**5. Scalability and Performance**
Good

**6. Security and Privacy**
Good

**7. Error handling and Resillience**
Good

**8. Deployment and DevOps**
Good

**Answering questioner**
Answering for the questioner is ok, but no need to write sentences with no actual meaningful information like the one below:  

> we actively consider exploring relevant online resources and documentation to enhance our knowledge and expertise in our tech stack.

It’s ok, if you not using any book, but don’t say you are actively looking for a recourses and without mentioning what are they. 


In learning objective, you should discuss what have you learned from this experience as a whole. Not what technologies you are learning now.

what did you learn for thinking about a project and implement it, working with teams, writing reports you should reflect on all of that. 


**Overall**
The report is good, I like your understanding of the project. I think you will produce an outstanding results!!! 

Grade 5/5


_Feedback by Moofiy_
{{< /hint >}}



# **Week #3 Report**

## Prototype

The course platform is available at [<ins>innomastery.ru</ins>](https://innomastery.ru). You may also check Coder, our Self-hosted Remote Development Environment, at [<ins>coder.innomastery.ru</ins>](https://coder.innomastery.ru).

### Prototype Features

The features that we have successfully integrated into our prototype are the following:
- Authentication via JWT tokens
- Authorization
- A table of contents for the course
- A self-hosted Remote Development Environment [<ins>Coder</ins>](https://coder.com/)

### User Interface

1. When the user visits our website, they see our landing page that tells them about our course. From here, the user can sign up for our course or continue their studies if they are already signed in.
![Index page](/InnoMastery/pages/index.jpeg)

2. After signing up, the student sees a table of contents for the course. Here, they can pick a lesson they want to study. The lessons are organized into chapters for easier navigation.
![Table of contents page](/InnoMastery/pages/table-of-contents.jpeg)

3. Each lesson consists of several steps of three kinds: theory, questions, and coding tasks. Theory steps are articles for the student to study, with each step dedicated to a single topic.
![Article page](/InnoMastery/pages/article.jpeg)

4. Question steps let the student evaluate the knowledge gained from the theoretical material.
![Question page](/InnoMastery/pages/question.jpeg)

5. By solving coding tasks, the student can apply new knowledge to solve real-world tasks. These tasks are solved in Coder. In Coder, the student can create their workspace from a template:
![Coder workspaces](/InnoMastery/pages/coder-workspaces.jpeg)
![Coder create workspace](/InnoMastery/pages/coder-create-workspace.jpeg)

6. Once they create a workspace, the student can access it using either VS Code in the browser or a locally installed VS Code.
![Coder access workspace](/InnoMastery/pages/coder-access-workspace.jpeg)
![Coder vscode online](/InnoMastery/pages/coder-vscode-online.jpeg)

## Challenges and Solutions

We faced challenges related to: 

1. *Authentication and Authorization.* JWT (JSON Web Tokens) is commonly used for authentication and authorization purposes. One of the challenges of implementing JWT is effectively managing tokens for people who have logged in. This can be addressed by implementing token revocation for logging out, token expiration, and refreshing tokens.

2. *Proper design mappings from sqlalchemy classes to strawberry classes.* It wasn’t so obvious at first, but then we managed to find a [<ins>relevant resource</ins>](https://blog.logrocket.com/using-graphql-strawberry-fastapi-next-js/) on the topic and resolved the issues with the database whatsoever.

## Next Steps

1. **Parsing course material.** So far, the table of contents is hard-coded into the prototype. We intend to implement a parser for all the material we already have, organized in Markdown files. This will give us an easy and automated way to deploy our course.

2. **Viewing course material on the website.** The lesson viewer isn’t in the working prototype yet. We plan to implement it during the next week.

3. **Grading questions.** Once we have the lesson viewer working, we’ll start implementing questions. Hopefully, we will do it during the fifth week.

4. **Integrating with Coder.** We also plan to integrate with Coder for the MVP. We want to implement authentication via OAuth and redirection to Coder for coding tasks.


{{< hint danger >}}
**Feedback** 


Note:
I couldn’t log into my account. Please don’t make the registration and using your service hard on first time users. It will make them run away.
Let me use the service once. If I like it then I will register.

**Prototype Features**<br>
You should list her all features you will provide. This is too short


**User Interface**<br>
AMAZING!!!
Very nice design. But did you test it with users?

**Challenges and Solutions**<br>
Good!,
**Next Steps**<br>
Good. You should relay think of testing (Usability testing)

**Overall**<br>
Good report, you should focus more on finalising the project. and test it with real users.
**Grade<br> 5/5**


_Feedback by Moofiy_
{{< /hint >}}



# **Week #4 Report**

## External Feedback

The feedback we received from our friends was overall positive. They appreciated the idea of the course platform and really liked the website design.

However, they pointed out several issues with our UX. For example, one person suggested to swap the buttons `I want a hint` and `Check` in question steps, as the check button is harder to reach than necessary.

![Hint and check buttons](/InnoMastery/hint-and-check-buttons.jpg)

Another issue is that Chrome does not suggest an auto-generated password on the sign-up page. We will need to improve the page markup with hints for browser autocompletion.

![Password auto generation](/InnoMastery/password-auto-generation.jpg)

Despite the issues mentioned above, the feedback shows that our project is going in the right direction.

## Testing

We tested the platform internally and discovered several issues. For example, the sign-up form didn’t accept the Russian letter `Ё`.

![Registration problem](/InnoMastery/registration-problem.jpg)

In addition, the password was checked against a regular expression that was hard to satisfy. For example, Firefox’s automatically generated password did not validate.

![Invalid password](/InnoMastery/invalid-password.jpg)

Once discovered, we relaxed the restrictions on the name and the password. We don’t really care about the user’s name, and putting many restrictions on the password often only leads to easier brute-force, hence is insecure.

Besides these issues with the sign-up form, testing didn’t reveal any other bugs in our prototype.

## Iteration and refinement

After collecting feedback and thoroughly testing our prototype, we created the appropriate issues and organized a retro session.

![Gitlab issues](/InnoMastery/gitlab-issues.jpg)

We noticed a lack of synchronization in our team, so we clarified several points about the project. For example, we discussed how different entities (namely, chapters, lessons, and three kinds of steps) should relate to each other in the database. This question is important for several interlinked issues. First, it affects how these entities are retrieved via the API and the API performance. Second, it affects how our URLs are composed, because it must be possible to fetch a particular step using only the information provided in the URL. Third, URLs matter for SEO, as search engines deprioritize ugly links in favor of simple and human-readable ones.

![URL structure](/InnoMastery/url-structure.jpg)

Second, we refined and agreed on our git flow. We also eliminated all stale branches. Third, we clarified further steps and noticed once again that it is important not to overcomplicate things and focus only on the features that are most important right now. Based on discussions during our meeting, we plan to implement these features during the next two weeks for our MVP:
- Viewing course material on the website
- Grading questions

{{< hint danger >}}
**Feedback**  
**External Feedback**<br>
Very Good, but maybe better to follow some kind of User statisifaction metrics like NPS to better utilise this feedback.

Now how will you adapt to this feedback?


**Testing**<br>
Good

Have you considered unit testing also?


**Iteration**<br>
Good iteration plan but keep in mind:

An iteration plan is essentially the plan for an upcoming iteration. It would typically outline:
* The goals and objectives for the iteration: what the team aims to achieve.
* The features to be developed.
* The tasks needed to develop these features. This might include coding, testing, design tasks, etc.
* Any assumptions or dependencies.
* A timeline for the iteration.


**Overall**<br>
The report is good.

**Grade: 5/5**


_Feedback by Moofiy_
{{< /hint >}}



# **Week #5 Report**

## Feedback

This week, we wanted to gather feedback not just from our friends but from a wider audience. We already had it: a few months ago, we gathered a focus group to collect feedback about our course. Now we have asked them to review the platform that we are building for this course.

![Course beta-test telegram chat](/InnoMastery/telegram-chat.png)

To collect feedback in a more convenient and insightful way, we have created a survey of user satisfaction with our product. By doing this survey, we hoped to learn more about our product from the user’s perspective. We asked about the feelings about our platform, UI/UX, as well as any encountered issues or bugs. For those interested, here is the [<ins>survey</ins>](https://forms.gle/n6DHyqRf7VgJJ6cV7).

As a result, we have collected a lot of useful feedback. From the responses, we have gathered the following observations:

- Our name and domain are catchy, which is great. Almost 70% of users can easily type the domain into a browser.
![Name feedback](/InnoMastery/name-feedback.jpeg)
- The majority of users are satisfied with the color palette used in the product.
![Colors feedback](/InnoMastery/colors-feedback.jpeg)
- Users have no trouble signing up.
- Some users did not like the font used in the UI, as the numbers "3" and "6" are shifted downwards from the rest of the text.
- Certain uses have raised concerns about how images are loaded and how some of them are too big.
- Luckily, our platform is considered reliable by the majority of users.
![Trustworthy feedback](/InnoMastery/trustworthy-feedback.jpeg)

If the respondent wanted to provide their contacts, they could do so in the survey. Some of the people did, and we’re going to reach out to those who provided insightful feedback soon. This will let us ask them additional questions through which we’ll learn more about how users want to interact with our product.

Now that we conducted the feedback survey, we have evaluated the user satisfaction and identified areas for improvements that we will prioritize in the remaining time.

## Improvement

Before the final presentation of our MVP, we will focus on the details of the platform, so the platform feels complete and ready for production. Based on the feedback received, we decided on the following improvements:

1. Change the sign-up flow until we implement email verification;
2. Finish implementing automatic question grading;
3. Add navigation between steps;
4. Improve the design of the website so it responds to user interaction (hovering over elements, clicking them, etc.).

## Reflection

We strive to release our course on our own platform in the next few months. In the current state, the prototype mostly replaces Stepik for our needs. However, we have to put more effort before publishing the course: we must bring in features that will distinguish our platform among already popular ones and bring the best experience to our students.

First, integration with Coder remains our biggest priority. With Coder, our coding tasks will bloom at their finest. The coding tasks are the strength of our course, as they show students how their new knowledge is applied in practice. Coder will let the student focus on solving the task, removing the hassle of setting up a local environment.

Second, we will focus on polishing the platform. For students to understand the material better, we need to support videos as well as animated terminal sessions in the theoretical material. In addition, the platform should remember where the student stopped the last time so that students can jump right back in when they come back. Last but not least, we will adapt the website for mobile screens, add PWA support, and fix discovered bugs to ensure the best possible UX for our students.

{{< hint danger >}}

**Collecting and documenting feedback**<br>
Very good!


**Feedback analysis**<br>
Very good!

**Roadmap and enhancement**<br>
Missing Roadmap. bit's genraly written what will you do. but this is could not be considered as a roadmap 


**Grade: 5/5**

{{< /hint >}}



# **Week #6 report**

This week, we primarily focused on polishing our website to improve the UX and make it feel like a complete product. Nonetheless, we’ve also finalized a new big feature that we started working on a few weeks ago: a chatbot to help students learn.

## Chatbot

When you open a lesson, you can now see a button to open the chatbot in the bottom-right corner of the screen.

![Tuxibot closed](/InnoMastery/tuxi-bot-closed.png)

When you click it, you’re presented with a chat with our Tuxibot. You can ask it any question that comes up to your mind while studying the material.

![Tuxibot opened](/InnoMastery/tuxi-bot-opened.png)

Moreover, you can ask it for hints when you get stuck answering a question or solving a coding task. Tuxibot is available on those steps as well—but it won’t give you the solution away.

Our tuxibot is powered by ChatGPT, a model from OpenAI. We utilized their API to implement our own chatbot for the platform.

## Polishing the website

While our ML engineers were building the chatbot, the rest of the team focused on finalizing features in development and ensuring a smooth user experience before the MVP.

Some articles include videos or GIFs to better illustrate a particular point, e.g. what happens when running the exit command. This week, we added support for videos in the article viewer.

![GIFs on site](/InnoMastery/gifs-on-site.png)

Although one could already switch between articles and questions, trying to open a coding task showed a white screen. Now coding tasks are supported on the website.

![Coding tasks](/InnoMastery/coding-tasks.png)

Moreover, we added a button at the bottom of the page to take you to the next step. This significantly simplifies navigation between steps.

![Next step button](/InnoMastery/next-step-button.png)

Last but not least, we hid features that are still in development. For example, after signing up, the user can start studying right away, no longer waiting for a confirmation email that will never arrive.

![No email confirmation](/InnoMastery/no-email-confirmation.png)

Likewise, the “Last time, you stopped at…” message on the landing page is removed too, waiting for the times to get better.

Overall, our platform is now viable for wider use, and we can’t wait to show it on the Final presentation and tell more about the course we’re building upon it.
