# Week #1
## Project: Healthy Based Productivity

### Team members


|Team member|Telegram ID|Email Address|
| :- | :- | :- |
|Sofi Zaitseva (TeamLead)|@sofi12321|s.zaitseva@innopolis.university|
|Danila Shulepin|@Mr_Ketch|d.shulepin@innopolis.university|
|Leon Parepko|@Leon_Parepko|l.parepko@innopolis.university|
|Yaroslav Sokolov|@buiniy_yarik|ya.sokolov@innopolis.university|
|Ilnur Khadiev|@Ilnur_ha|i.khadiev@innopolis.university|

## Value Proposition 

### Identify the Problem 

Every day the pace of our life becomes increasingly fast. A great number of people often attempts to accomplish as many tasks as possible in the shortest amount of time, which can have a negative impact on their health and social relationships. This issue can even lead to burnout.
For this reason, people use planners to organize their work and personal time, however they often idealize their schedules. A schedule meticulously planned down to the minute appears highly unrealistic because it does not account for rest and transitions between tasks. Moreover, when such a plan is disrupted, it becomes a source of even more stress, irritability, lowered self-esteem, and motivation. Hence, there exists the problem of idealistic task planning by people.

### Solution Description 

Our product offers the opportunity to optimize a person's schedule based on his or her activity history.
Let's consider an example where the user systematically estimates his capabilities too optimistically and allocates less time to tasks than he or she actually spends on them. In this case, the system notes this issue and generates a more objective schedule for the day. The ability to create a schedule based on activity history is an innovation of our project.
The project implementation will be a chatbot in Telegram. In it, users will be able to work with the list of tasks - add, modify, delete, as well as mark their execution and receive the generated day schedule.

### Benefits to Users

Our project offers many benefits to users, such as
* avoiding mistakes made by people in the planning process;
* saving time, as there is no need to analyze and schedule schedules yourself;
* improved wellness due to the absence of worries about failed plans.

### Differentiation 

The main competitive advantage of our solution is its personalization. Unlike existing competitors, our project will take into account not only the user's preferences when creating a schedule, but also their work habits analyzed through activity history. Additionally, our project will be developed in the format of a Telegram chatbot that makes it simple, convenient, and likely more cost-effective compared to competitors' solutions.

### User Impact

One of the most valuable resources people have is time, some of which goes into making a schedule for the day. At the same time, plans can be idealistic, which may lead to burnout and loss of schedule value. Our project allows users to save time and nerves easily and efficiently.

### User Testimonials or Use Cases

We can take a student of Innopolis University as an example. Student
compiles a list of various tasks (personal, school, work) and then receives a schedule from the chatbot with the exact order of the tasks and the allocated time for each task.
Another example: a company distributes tasks among employees, but in order not to overload them, it takes into account the possible schedule and changes the workload and priorities

## Lean Startup Questionnaire 

1. What problem or need does your software project address?

Our project solves a problem of idealistic task planning and saving time for this process. 

2. Who are your target users or customers?
 
The target audience of our startup is people of the intellectual labor aged 18 to 60 years. They make a daily schedule, but sometimes it is unrealistic and they do not follow it. Additionally, they want to devote less time to the planning process.

3. How will you validate and test your assumptions about the project?

Our project may have both technical and user-related assumptions. First of all, we will test technical assumptions by checking the work of the system and its parts on real data and evaluate by accuracy of the built schedule. Usability will be evaluated with feedback from potential users, and the remaining user-related hypotheses will be tested through interviews with them.

4. What metrics will you use to measure the success of your project?

First of all, the output of our system should be an adequate resulting schedule, i.e. no overlapping, no shifts for fixed tasks or events (such as lectures, meetings, etc.), and adjustments based on the experience of the user's previous activity. In addition, our project will be successful if it is useful and user-friendly, so we plan to test our solution among potential users. 

6. How do you plan to iterate and pivot if necessary based on user feedback?

Primarily, we plan to analyze user feedback and extract possible changes in the system. Then we will implement the modifications, test the system on the real data and evaluate changes by user feedback. If the improvements made the system more efficient, we will accept them, otherwise our team will find another way to realize user feedback.

## Leveraging AI, Open-Source, and Experts

We will use a pre-trained NLP model for task’s names analysis, build our own ML model for scheduling, and use Chat-GPT and GitHub Copilot to help us during the working process. We also may use open-source code to make our project more efficient, and we will share our results in GitHub. Finally, we will consult with AI-lab at Innopolis University about the data collection and model building processes.

## Inviting Other Students
This project idea is a part of a startup idea that was invented before the capstone project. So several team members have already been gathered. In the last few days we have found some more teammates, that is why now our skills are enough to implement the MVP. Although we don't need more people in the team, our project is open to comments, ideas and suggestions as we want to make it cool.

## Defining the Vision for Your Project
1. Overview

In summary, our project aims to solve the problem of idealistic task planning by providing users with a personalized and optimized schedule based on their activity history. Current planners often fail to account for the rest and transitions between tasks, causing additional stress and lowered motivation when plans are disrupted.

Our chatbot in Telegram allows users to add, modify, and delete tasks while marking their completion. The innovative feature of our product is the ability to generate a more objective schedule by analyzing the user's activity history. This personalized approach sets us apart from existing competitors.

By using our solution, users can avoid the mistakes and unrealistic expectations often associated with manual planning. This saves them time and eliminates the worry of failed plans, which ultimately contributes to better well-being.

2. Schematic Drawings

![image](https://github.com/sofi12321/healthy-based-productivity/assets/71354878/4a568260-ac67-479b-9bb0-ab2a8b4c415a)

3. Tech Stack

We will use Python as our programming language because it has a large number of different libraries and frameworks, which can be very useful in the development process. In addition, the Python programming community is quite large, which makes it possible to find a large amount of open source code.

We plan to use PyTorch as our main framework, as one of the most popular and scalable. 
So far, we have not fully decided which NLP model to handle task names, as well as which frameworks to write the chatbot we will use.

Our team has enough experience and qualifications to use the right tools to develop the project.

4. Anticipating Future Problems

So far, we have identified several potential future problems:
- lack of data;
- difficulties with model building and evaluating;
- how to store user’s history of activity;
- how to track the end of the task;
- how to filter the output in case of “outlier” schedule;
- user-unfriendly input.

5. Elaborate Explanations

Our project involves building an application to create a day's schedule based on the list of tasks entered by the user. We plan to use machine learning models, which will take into account not only the current tasks, but also the user's activity history, which is an innovative solution. In addition, we will implement our project in the form of a chatbot in Telegram, which is a cheap, but also simple and elegant solution.
