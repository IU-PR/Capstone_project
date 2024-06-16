---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member      | Telegram ID | Email Address                     |
|------------------|-------------|-----------------------------------|
| Fedor Smirnov    | @tedor49    | f.smirnov@innopolis.university    |
| Ivan Lishchenko  | @Magel0n    | i.lishchenko@innopolis.university |
| Aleksei Morozov  | @Moroz0517  | al.morozov@innopolis.university   |
| Ivan Sannikov    | @ivasan1    | i.sannikov@innopolis.university   |
| Timur Suleymanov | @tjann7     | t.suleymanov@innopolis.university |

### **Value Proposition**

- Identify the Problem:
  In the field of programming we often use such online judging websites
  such as [informatics](https://informatics.msk.ru/), [Timus](https://acm.timus.ru/) or
  [CodeForces](https://codeforces.com/).
  All of their contests follow ACM/ICPC format with some slight variation, which we believe negatively impacts
  engagement and that makes the new generation of students disinterested in olympiad-programming.

- Solution Description:
  Our project aims to create a distinct website that would allow for an engaging experience for solving tasks.
  The teachers can create contests of many different types or maybe even make up some activities themselves, while the
  students can solve the tasks while interacting with each other, the teacher and the system in a gamified way.

- Benefits to Users:
  It is well-known what benefits an Interactive Learning Environment (ILE) brings gamification of education.
  We have found two articles to support us about
  [ILE](https://londoncollegept.co.uk/the-advantages-of-interactive-learning) and
  [gamification](https://www.sciencedirect.com/science/article/abs/pii/S1747938X19301058),
  but to summarize: since we are in an era of small attention span, we need to make the learning as engaging as possible
  to catch attention, but for programming this topic requires a special touch which was not fully utilized before this
  project.
  The students get to interact with the system in fun ways, for example, get extra points for specific actions or ask a
  friend for help, make a collaboration together, etc.
  The teachers get to have a friendly interface that allows to manage the possible activities for any part of the
  contest, but could also use the same tools and more to make for a better class activity.
  This enhances the experience, makes it so that a teacher just resets or starts a copy of a contest, which saves time,
  but as said prior, it creates a playground for any actions from both sides.

- Differentiation:
  Our platform provides a user-friendly, yet powerful interface for the administrative side which even ordinary school
  teachers with next to no knowledge of programming can utilize. Moreover, we provide an engaging, interactive
  environment that facilitates a more gamified interaction between students and code, which is not present in most
  contemporary solutions.
  The closest alternative to our project is EJudge, but they only allow for 7 types of contests, from which there are
  only 4 unique rulesets, whilst we wish to create a platform that has orders of magnitude more.

- User Impact:
  The students get to practice programming (or maybe even more) in a friendly and engaging environment,
  meaning that the participation and perception of the classes improve. Moreover, since many olympiads are taking
  place on such websites, all students would be familiar with the interface, just lacking some of the activities that
  could create opportunities for cheating.
  It is possible that some of aforementioned websites will pivot to provide a similar diversity.

- User Testimonials or Use Cases:
  One of our team members and saw many interesting contests, but for most of them there were different and often poor
  systems, and now he wants to create a website that would unite such creative activities and make them more popular.

## **Lean Questionnaire**

Please answer the following questions related to the lean methodology:

1. What problem or need does your software project address?

The problem of a user-friendly and engaging website for judging programming that would insensitive learning of
olympiad-level programming.

2. Who are your target users or customers?

For the customers we expect to see schools and universities and their students, above 12 years old.

3. How will you validate and test your assumptions about the project?

After we have our MVP we would finish the project to a more workable state and try to integrate it in our university
labs. In the future we would try to find more costumers such as private schools and other universities, possibly
abroad.

4. What metrics will you use to measure the success of your project?

This project should not require any significant measurements of CPU and GPU usage, but we will optimize where necessary.
For the main metrics we will use user satisfaction, engagement and possibly more.
For this we would probably need an expert to create questions that would be asked on our platform.

5. How do you plan to iterate and pivot if necessary based on user feedback?

We are more that happy to listen for more possible activities (the actions in the contests) and any interface changes.
For now, we do not know what else could require us to change something, but perhaps we could allow users to choose
their own theme.

## **Leveraging AI, Open-Source, and Experts**

**AI**: Our team is yet uncertain of using AI, but it is possible that we will create an activity that will center
around AI. Additionally, it is possible that we will use ChatGPT for possible activities if we ever run out of ideas.

**Open-source**: We will most likely check the implementation of our nearest competitor,
[EJudge](https://ejudge.ru/wiki/index.php/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_ejudge) as they may have
useful insights in their [repository](https://github.com/blackav/ejudge).

**Experts**: Once we will require to measure the success of our project, we will have to find an expert that could
help us measure the user satisfaction and engagement.

## **Defining the Vision for Your Project**

- Overview:
  Our project aims to create a judging website that could engage the students with olympiad level programming.
  For that we plan to add a variety of extra activities in the system that would gamify user experience.
  The teachers benefit since their students will be more involved with the class,
  whilst the students get a friendly environment for educational activities.

- Schematic Drawings: ![Diagram.png](/2024/code_battle_advanced/Diagram.png)
  The user (both teacher and student types) logs in the website, where Web-app servers are handling all actions and
  Nodeport distributes the workload.
  The tasks, checkers, solutions and results are stored on our database MongoDB.
  When we get a new solution that needs testing, we send that to WorkQueue server to distribute the workload between
  Judge Servers.

- Tech Stack:
  
  Python for code that distributes workload.
  
  Redis for distributing workload between Judge Servers.
  
  Mongo for database handling (Subject to change).

  Kubernetes for dockerizing the project.

  Flask for the web application.
