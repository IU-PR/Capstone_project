---
weight: 2
bookFlatSection: true
title: "Week #2"
---

# Week #2 Report

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

