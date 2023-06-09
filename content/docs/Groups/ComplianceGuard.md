# **ComplianceGuard** 

This is the page for your group to write reports following the lectures and weekly tasks:  
Hi! We a group called "ComplianceGuard" and we are creating an application which will understand if worker is wearing a personal protective equipment or not using Computer Vision model

---
weight: 1
bookFlatSection: true
title: "Week #1"
---

# **Week #1**

# **Introduction**

{{< hint danger >}}
**Important Note**  
This blog serves as a central platform for important updates and information regarding our project journey. It is vital that you regularly check this blog for the latest updates and announcements. The content provided on this blog is intended for informational purposes only and may be subject to change without prior notice.
{{< /hint >}}

**Week #1 is the most crucial week of the entire semester as it sets the foundation for your project**. During this week, your primary tasks are to form your team and select a project. The team formation process should carefully consider the skills, expertise, and compatibility of team members to ensure effective collaboration.

Once your team is formed, it is essential to pitch and discuss project ideas among yourselves. Select a project that aligns with one of the three tiers: web, mobile, or ML (machine learning). The chosen project should be well-defined, feasible, and have a clear problem statement.

Additionally, we expect each team to maintain a weekly progress report blog. These reports are a crucial means of tracking the progress of your projects. Each team is required to submit a report no later than Friday 18:00 of each week. The reports should be informative, substantive, and provide a detailed account of your progress. It is important to clearly explain what you have accomplished, how you have achieved it, and any obstacles or challenges you have encountered.

These weekly reports will be evaluated, and feedback will be provided to assist you in the successful completion of your projects. Therefore, it is crucial to submit your reports on time and ensure they reflect the substantial progress you have made throughout the week.

We encourage you to use this blog as a platform to share your accomplishments, insights, and challenges. It is a valuable opportunity to communicate your ideas, seek feedback, and engage with your peers. By actively participating and sharing your experiences, you contribute to the collaborative learning environment we aim to foster.
{{< hint info >}}
Remember, the success of your projects depends on your commitment, dedication, and effective teamwork. Embrace this opportunity to showcase your skills, innovate, and create impactful projects. Good luck, and let's make this semester a remarkable journey of growth and accomplishment!
{{< /hint >}}
Should you have any questions or require further guidance, please do not hesitate to reach out to us. We are here to support and guide you through this exhilarating process.

## **Team Formation and Project Proposal**

Please provide the following information for your team members and answer the questions listed below. This information will help us understand your team composition and project proposal better.

### **Team Members**

Please list the names and contact details (Telegram and email) of your team members:
{{< expand "Important Note" >}}

When building a team for a software project consisting of 5-7 people, it is crucial to pay attention to the following:

1. **Skills and Expertise**: Ensure that the team members possess the necessary skills and expertise required for the project. Consider their technical knowledge, programming languages, frameworks, and any specific domain expertise relevant to the project.

2. **Collaboration and Communication**: Look for individuals who can effectively collaborate and communicate with one another. Strong teamwork and clear communication channels are essential for seamless coordination and successful project execution.

3. **Roles and Responsibilities**: Clearly define roles and responsibilities for each team member. Assign tasks based on their strengths and expertise to optimize productivity and ensure a well-rounded team composition.

4. **Diversity**: Seek a diverse mix of skills, perspectives, and backgrounds within the team. This can foster creativity, innovation, and a broader range of problem-solving approaches.

5. **Leadership**: Identify a capable team lead or project manager who can provide guidance, set clear goals, and facilitate decision-making processes. Leadership skills are crucial to keeping the team motivated and on track.

6. **Flexibility and Adaptability**: Select team members who are adaptable and comfortable working in a dynamic environment. Software projects often encounter changes, and team members should be open to adjusting their approaches and strategies as required.

7. **Problem-solving Abilities**: Look for individuals with strong problem-solving skills. They should be able to analyze complex issues, propose effective solutions, and work well under pressure.

8. **Team Dynamics**: Consider the overall team dynamics and ensure compatibility among team members. A cohesive and supportive team environment can enhance productivity and foster a positive work culture.

9. **Shared Vision**: Ensure that all team members understand and align with the project's vision and goals. A shared sense of purpose can foster motivation, commitment, and a unified approach to project delivery.

Remember, building a successful software project goes beyond individual skills. It requires a combination of technical expertise, effective communication, collaboration, and a shared commitment to achieving project goals. By paying attention to these aspects, you can lay a strong foundation for your team's success.


{{< /expand >}}
| Team Member            | Telegram ID   | Email Address       |
|------------------------|---------------|---------------------|
| Team Member (Lead) 1          | @BikTracker | d.kuzmin@innopolis.university     |
| Team Member 2          | @Mosiramakata | i.belyaev@innopolis.university     |
| Team Member 3          | @isqisq | i.ishkineev@innopolis.university     |
| Team Member 4          | @dudlas | r.sayfeev@innopolis.university     |
| Team Member 5          | @ADari_Ka | d.kalashnikova@innopolis.university     |
| (Optional) Team Member 6 | @FateeeGW | m.gubaidullin@innopolis.university     |
| (Optional) Team Member 7 | @NoNesmer | v.rublev@innopolis.university     |


### **Value Proposition**

The value proposition of your software project defines the unique benefits and advantages it offers to its users. It highlights the problem your project aims to solve and the positive outcomes it brings. Here's an expanded explanation to help you craft a compelling value proposition:

- Identify the Problem:
Clearly define the problem or pain point that your software project addresses. Analyze the challenges or inefficiencies faced by users in the targeted domain. Consider the specific pain points, bottlenecks, or limitations they encounter.

- Solution Description:
Explain how your software project provides a solution to the identified problem. Outline the key features, functionalities, or services that directly tackle the pain points. Emphasize the unique aspects of your solution that set it apart from existing alternatives.

- Benefits to Users:
Describe the benefits that users will experience by using your software project. Highlight how it enhances their productivity, efficiency, or effectiveness. Identify the positive outcomes, cost savings, time savings, or improved experiences they can expect.

- Differentiation:
Discuss what sets your software project apart from competing solutions. Identify the unique selling points, innovative features, or competitive advantages that make it a superior choice for users. Clearly articulate why users should choose your solution over others available in the market.

- User Impact:
Explain the broader impact your software project has on users and potentially the society or industry as a whole. Highlight any positive changes, transformative effects, or advancements that result from the adoption of your solution. Consider how it improves workflows, empowers users, or drives positive change.

- User Testimonials or Use Cases:
Whenever possible, provide real-world examples, user testimonials, or case studies that demonstrate the value and benefits of your software project. Showcasing tangible results and success stories adds credibility and reinforces the value proposition.

Remember to keep your value proposition concise, clear, and compelling. Focus on the most significant benefits and outcomes that resonate with your target users. A well-crafted value proposition effectively communicates the value and impact of your software project, making it more appealing and compelling to users.

#### We can agree that a builder, a factory worker or an employee of a nuclear power plant are quite dangerous professions. Working, they risk their lives, so to reduce the risk, people have invented special equipment for them. But the problem is that people often neglect precautions, so many workers do their work without special equipment. Such negligence significantly increases the likelihood of an accident, so there must be a way to monitor whether workers are wearing special equipment. Now this is controlled by operators who have to sit next to the cameras all the time and check whether people are wearing special equipment. But this method is unreliable due to the human factor, so we want to create an application that will check whether an employee is wearing special equipment instead of human. How it will work: An artificial intelligence model will receive video from cameras and highlight people in red if they are not wearing equipment, and green otherwise. If the program sees a violation of the rules, it will send a warning message with a screenshot from the camera to the specified location (email, phone message, etc.). Our program will constantly monitor employees, so it will instantly detect violations of safety regulations and report it. By choosing our program, you eliminate the human factor, save your time and money. There  already exists a similar program (EYECONT https://www.mallenom.ru/products/eyecont/kontrol-ispolzovaniya-siz/), but this is just a model of artificial intelligence inside the cameras. Our program is an application, so you can see what is happening on a particular camera, anytime and anywhere. In general, our application can benefit the industry, because by using our program, companies can stop worrying about the safety of their employees.

## **Lean Startup Questionnaire**

Please answer the following questions related to the lean startup methodology:

1. What problem or need does your software project address?
2. Who are your target users or customers?
3. How will you validate and test your assumptions about the project?
4. What metrics will you use to measure the success of your project?
5. How do you plan to iterate and pivot if necessary based on user feedback?

#### 1. The problem of compliance with safety regulations by employees
#### 2. Owners of factories, building companies, seaports, ...
#### 3. Interview our target customers, analyze the number of accidents under different conditions
#### 4. Number of wrong predictions made by the model, wholeness of predictions, application user experience(for better design and functionality)
#### 5. Remove or improve features which doesnt work, add features which users want to have


## **Leveraging AI, Open-Source, and Experts**

Explain how your team plans to leverage the following resources for the development and success of your project:

- AI (Artificial Intelligence):
- Open-Source:
- Experts in relevant domains:

#### AI: our application is build around a CV model
#### Open-Source: Our ML engeneers can use models from Open-Source to study and improve the model in our program
#### Experts in relevant domains: Our developers will ask advices from more experienced specialists to improve quality of the application


## **Inviting Other Students**

Are you open to inviting other students to join your project? If so, it's great to foster collaboration and expand your team. Feel free to discuss the project with your peers and encourage them to join if they are interested and motivated.

When considering inviting other students, you can think about the roles you are looking for and any specific requirements. Be open to diverse skills and expertise that can contribute to the success of your project. Collaboration and teamwork can lead to innovative solutions and a richer learning experience.

Remember, talking to other students and finding potential team members to join your project is not only allowed but also encouraged. Embrace the opportunity to collaborate and create a strong team that can achieve great results together.


#### For now we are not planning to invite other students in our project

## **Defining the Vision for Your Project**

A clear and compelling vision is crucial for successful project planning. When you have a well-defined concept and a shared vision of what you aim to achieve, executing on that vision becomes significantly easier. Therefore, after thorough discussions and settling on a promising idea, it is essential to craft a comprehensive vision with your team. This vision should be detailed, encompassing your chosen tech stack, and anticipate potential future challenges. Below, describe your project using schematic drawings and provide elaborate explanations of all significant components.

- Overview:
Provide a concise summary of your project, highlighting its purpose and value proposition.
Explain how your project addresses a specific problem or need in the chosen domain.
Clearly state the intended benefits and impact on users or stakeholders.

- Schematic Drawings:
Use visual representations such as diagrams, flowcharts, or wireframes to illustrate the structure and flow of your project.
Include all essential components, modules, and interactions within the system.
Ensure the drawings are clear, labeled, and easily understandable by both technical and non-technical stakeholders.

- Tech Stack:
Specify the technologies, frameworks, and programming languages you plan to utilize in your project.
Justify your tech stack choices based on their suitability for the project requirements and team expertise.
Consider scalability, performance, security, and ease of development when selecting your tech stack.

- Anticipating Future Problems:
Foresee potential challenges and obstacles that may arise during the project development and deployment phases.
Identify risks related to technical complexities, resource limitations, time constraints, or external dependencies.
Propose mitigation strategies or alternative approaches to address these anticipated problems.

- Elaborate Explanations:
Provide detailed descriptions of critical components, algorithms, or methodologies employed in your project.
Explain the core functionalities and how they contribute to achieving the project goals.
Highlight any innovative or unique aspects of your solution that differentiate it from existing alternatives.

#### Overview: Our project is designed for managers of companies whose employees must wear special equipment. This is an application that allows you to determine by video whether a person is wearing special equipment or not. If a person is not wearing equipment, he highlights it in red, otherwise - in green. It will allow the manager to receive a notification when workers are at the workplace without special equipment, to view video from cameras in real time.

#### Schematic Drawings: 

![](/static/ComplianceGuard/week1capstonediagram.png)
#### Tech stack: 
##### Desight: Figma
##### Frontend: Javascript, HTML, CSS, ReactJS
##### Backend: Python, FastAPI/aiogttp+async, pydantic
##### AI: OpenCV, PyTorch

#### Anticipating Future Problems: Potential problems are: Big complexity of AI model, time to train the model, limited GPU, unknown dataset(what is dataset itself, how much data in it), pretty complex backend(mainly features like sending messages, connecting to the cameras). How can these problems be solved: Find additional GPU to spend less time on training, improve dataset if necessary(reversing videos, rotating, etc.), ask experienced specialists to help us with problems(with model creation, backend development).

#### Elaborate Explanations: The most critical component is implementation of AI model. It should predict well, but should not be too complicated(otherwise it wont have time to train well). Frontend is going to be pretty simple, and algorithms for additional functionality on backend side(working with cameras, sending messages) are still going to be learned. About flow of the project development - it will be based on Agile and Scrum, due to the fact that in the end we should present only MVP of the project.


