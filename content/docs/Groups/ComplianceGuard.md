---
weight: 1
bookFlatSection: true
title: "ComplianceGuard"
---
# **ComplianceGuard** 

{{< hint danger >}}

**Feedback**  
Write concise and well-written project description here. To enhance it further, we recommend incorporating additional details that provide an overview of your project. Consider including elements such as a project logo, a link to your project's webpage, or any other relevant visual materials that can help showcase your work effectively.  
As we plan to promote your work, it's crucial to ensure that this file serves as a compelling introduction that captures the attention of potential readers. 
{{< /hint >}}

# **Week #1**


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

We can agree that a builder, a factory worker or an employee of a nuclear power plant are quite dangerous professions. Working, they risk their lives, so to reduce the risk, people have invented special equipment for them. But the problem is that people often neglect precautions, so many workers do their work without special equipment. Such negligence significantly increases the likelihood of an accident, so there must be a way to monitor whether workers are wearing special equipment. Now this is controlled by operators who have to sit next to the cameras all the time and check whether people are wearing special equipment. But this method is unreliable due to the human factor, so we want to create an application that will check whether an employee is wearing special equipment instead of human. How it will work: An artificial intelligence model will receive video from cameras and highlight people in red if they are not wearing equipment, and green otherwise. If the program sees a violation of the rules, it will send a warning message with a screenshot from the camera to the specified location (email, phone message, etc.). Our program will constantly monitor employees, so it will instantly detect violations of safety regulations and report it. By choosing our program, you eliminate the human factor, save your time and money. There  already exists a similar program [**EYECONT**](https://www.mallenom.ru/products/eyecont/kontrol-ispolzovaniya-siz/), but this is just a model of artificial intelligence inside the cameras. Our program is an application, so you can see what is happening on a particular camera, anytime and anywhere. In general, our application can benefit the industry, because by using our program, companies can stop worrying about the safety of their employees.

## **Lean Startup Questionnaire**

1. The problem of compliance with safety regulations by employees
2. Owners of factories, building companies, seaports, ...
3. Interview our target customers, analyze the number of accidents under different conditions
4. Number of wrong predictions made by the model, wholeness of predictions, application user experience(for better design and functionality)
5. Remove or improve features which doesn't work, add features which users want to have


## **Leveraging AI, Open-Source, and Experts**

Explain how your team plans to leverage the following resources for the development and success of your project:

- AI (Artificial Intelligence):
- Open-Source:
- Experts in relevant domains:

AI: our application is build around a CV model
Open-Source: Our ML engeneers can use models from Open-Source to study and improve the model in our program
Experts in relevant domains: Our developers will ask advices from more experienced specialists to improve quality of the application

## **Inviting Other Students**

For now we are not planning to invite other students in our project

## **Defining the Vision for Your Project**

Overview: Our project is designed for managers of companies whose employees must wear special equipment. This is an application that allows you to determine by video whether a person is wearing special equipment or not. If a person is not wearing equipment, he highlights it in red, otherwise - in green. It will allow the manager to receive a notification when workers are at the workplace without special equipment, to view video from cameras in real time.

**Schematic Drawings:** 
![image](/ComplianceGuard/week1capstonediagram.png)

{{< hint danger >}}

**Feedback**  
This chart is more of a platitude than actual description of the project. Consider using more specific charts explaining something 
{{< /hint >}}
#### Tech stack: 
- Desight: Figma
- Frontend: Javascript, HTML, CSS, ReactJS
- Backend: Python, FastAPI/aiogttp+async, pydantic
- AI: OpenCV, PyTorch

Anticipating Future Problems: Potential problems are: Big complexity of AI model, time to train the model, limited GPU, unknown dataset(what is dataset itself, how much data in it), pretty complex backend(mainly features like sending messages, connecting to the cameras). How can these problems be solved: Find additional GPU to spend less time on training, improve dataset if necessary(reversing videos, rotating, etc.), ask experienced specialists to help us with problems(with model creation, backend development).

Elaborate Explanations: The most critical component is implementation of AI model. It should predict well, but should not be too complicated(otherwise it wont have time to train well). Frontend is going to be pretty simple, and algorithms for additional functionality on backend side(working with cameras, sending messages) are still going to be learned. About flow of the project development - it will be based on Agile and Scrum, due to the fact that in the end we should present only MVP of the project.

{{< hint danger >}}

**Feedback**  
Unfortunately, this report was poorly formatted and written and I had to reformat most of the text. The weekly tasks are there to give you the general structure - there is no need to copy all the text. Also, consider using the guide here -  https://www.markdownguide.org/basic-syntax/. Regarding the project, it seems that you have a good team and guidance from the AI institute. However, consider scaling some of the aspect of the project to fit into Capstone project. All that you will promise has to be delivered at the end of the course - therefore, be more specific about what are you building and how are you planning to build it.
{{< /hint >}}
