---
weight: 1
bookFlatSection: true
title: "Week #1"
---

# Week #1 Report

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
