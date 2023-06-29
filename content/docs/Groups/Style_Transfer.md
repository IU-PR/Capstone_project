---
weight: 1
bookFlatSection: true
title: "Style Transfer"
---
# **Style Transfer**
# **Introduction**

{{< hint danger >}}

**Feedback**  
Write concise and well-written project description here. To enhance it further, we recommend incorporating additional details that provide an overview of your project. Consider including elements such as a project logo, a link to your project's webpage, or any other relevant visual materials that can help showcase your work effectively.  
As we plan to promote your work, it's crucial to ensure that this file serves as a compelling introduction that captures the attention of potential readers. 
{{< /hint >}}

# Week 1

| Team Member            | Telegram ID   | Email Address       |
|------------------------|---------------|---------------------|
| Muhammadjon Hokimiyon (Lead)          | [Muhammad_Hokimiyon](https://t.me/Muhammad_Hokimiyon) | m.hokimiyon@innopolis.university     |
| Sadi Toirov          | [Toirov Sadi](https://t.me/Toirov_Sadi) | s.toirov@innopolis.university     |


### **Value Proposition**

- Identify the Problem:
Our project helps people who want to make their pictures look like paintings or have a different artistic style. Before our project, it was difficult and time-consuming to do this manually or without any art knowledge.

- Solution Description:
Our project makes it easy for anyone to change the style of their pictures using a simple computer program. You just need to choose the style you like, and our program will automatically apply it to your picture. It's fast, user-friendly, and doesn't require any special skills.

- Benefits to Users:
Our software project saves users time by quickly transforming the style of their pictures without needing any art skills. It also allows users to explore different creative options, saves costs by avoiding hiring professionals, enhances the visual appeal of their images, and can be used in various fields like art, design, and social media.

- Differentiation:
By offering a user-friendly interface, a diverse style library, high-quality results, efficiency, and broad applications.

- User Impact:
Our software project has a positive impact on users' creativity, workflows, and the broader society. It fosters artistic expression, drives innovation, advances industry practices, and contributes to the preservation and appreciation of diverse artistic styles and cultural heritage.

- User Testimonials or Use Cases:
They illustrate how users can benefit from the time savings, enhanced visual appeal, and increased creative possibilities offered by our software project.


## **Lean Startup Questionnaire**

Please answer the following questions related to the lean startup methodology:

1. What problem or need does your software project address?
2. Who are your target users or customers?
3. How will you validate and test your assumptions about the project?
4. What metrics will you use to measure the success of your project?
5. How do you plan to iterate and pivot if necessary based on user feedback?

### Answers: 

1. Our software project addresses the need for an efficient and accessible solution for style transfer, allowing users to easily apply artistic styles to their images without the need for manual editing or artistic expertise.

2. Our target users or customers include individuals and professionals in various domains such as digital art, graphic design, advertising, and social media. We aim to cater to users who want to enhance the visual appeal of their images by incorporating different artistic styles.

3. To validate and test our assumptions about the project, we will engage in user testing and gather feedback from our target users. We will conduct surveys, interviews, and usability tests to understand their needs, pain points, and preferences. This feedback will help us refine and improve our software project.

4. The success of our project will be measured using several metrics, including user engagement metrics such as the number of active users, frequency of usage, and user satisfaction ratings. We will also consider the conversion rate of free trial users to paying customers, as well as any positive impact on the users' creative output and productivity.

5. Based on user feedback, we will iterate and pivot if necessary to address any identified pain points or areas for improvement. We will closely analyze user feedback and data, identify patterns or common requests, and prioritize the most impactful changes. This iterative approach will allow us to continuously refine our software project, ensuring it meets the evolving needs of our users. If necessary, we are open to pivoting our project direction to better align with user preferences and market demands.


## **Leveraging AI, Open-Source, and Experts**

Explain how your team plans to leverage the following resources for the development and success of your project:

- AI (Artificial Intelligence):
- Open-Source:
- Experts in relevant domains:

Our team plans to leverage AI techniques, open-source resources. By utilizing AI, open-source technologies, and expert knowledge, we aim to deliver high-quality results and optimize the development and success of our project.


- Overview:
Our project is a user-friendly software solution that automates style transfer, allowing users to apply artistic styles to their images effortlessly. By addressing the time-consuming and challenging nature of manual editing, our project saves users valuable time and eliminates the need for artistic expertise. The intended benefits include enhanced creativity, improved visual appeal, and increased efficiency in various domains such as digital art, design, and social media. Our project empowers users to transform their images with ease, driving positive impact and value for both individual users and stakeholders in the chosen domain.

- Schematic Drawings: Website / Telegram_bot (accept images) --send_to---> API (which accepts images, and returns the generated image) --reply---> Website / Telegram_bot (display the received image)

- Tech Stack:
Our project will utilize Python as the programming language, TensorFlow or PyTorch as the deep learning framework, and Flask or Django for backend development. These technologies were chosen for their suitability to project requirements, team expertise, and factors such as scalability, performance, and ease of development.


- Anticipating Future Problems:
Anticipating future problems, we acknowledge potential challenges in technical complexities, resource limitations, time constraints, and external dependencies.

- Elaborate Explanations:
Our project utilizes style transfer algorithms and a user-friendly interface to enable users to apply artistic styles to their images. The core functionalities involve image preprocessing, feature extraction, style representation, and image synthesis. Our solution stands out with its high-quality results, user-friendliness, and potential incorporation of advanced techniques, providing a compelling alternative in the style transfer domain.

{{< hint danger >}}
Unfortunately, this report was poorly formatted and I had to reformat most of the text. The weekly tasks are there to give you the general structure - there is no need to copy all the text. Also, consider using the guide here -  https://www.markdownguide.org/basic-syntax/. The project page do not describe much other than saying that you will do style transfer (which is already solved problem in machine learning). Please, provide more detailed view of your project, outline your group contribution on top of available ML solutions and how are you planing to do that. Will it be a web app and a telegram bot?
{{< /hint >}}

## **Defining the Vision for Your Project**
We decided to devide our project into four main parts:
1. Train the model to transfer style from one image to another from scratch, choosing the proper architerture and optimize it.
2. Integrate this model to API, so that it could accept two needed images and do all computations and return resulting image.
3. Build a human friendly interface with web app to take images and send it to the API and receive transfered image.
4. Add some new features (optional):
    - Take one image and name of the famous artist, and transfer style of the artist image to the given image
    - Take instead of the image a video, and return a video in given style (image, name of the artist)
    - Add new option of choose **best** which search for best style amoung famous artist, for the given image (need further investigation to find a way to measure style of the image)
    - Anime or other unusual styles 

{{< hint danger >}}
No Week 2 progress report?  
0/5
{{< /hint >}}

# Week 2
## **Week 2 - Choosing the Tech Stack, Designing the Architecture**
### **Tech Stack Selection**
1. Train the Model
    - Python as a base language
    - PyTorch as a framework for implementing the model

2. Build an API
    - FastAPI - to create an API

3. Build an Interface
    - Django 

### **Architecture Design**
1. **Component Breakdown:** We have three Major components: 
    - Choose proper architerture for the model, so it could transfer style properly
    - Backend connected to the created API
    - Frontend to interact and display images

2. **Data Management:** No need for database, store everything localy (not to much data to be stored)

3. **User Interface (UI) Design:** Our UI is just simply one paged web site where you upload two images and receive one image and display it.

<img alt="img" src="/StyleTransfer/week2_ui.png"> 

4. **Integration and APIs:** We will use our own created API, which communicates to backend to receive and send images.

5. **Scalability and Performance:** Our main and hardest task is to create a good model and it runs on API which can be integrated in any system.

6. **Security and Privacy:** For now we don't have any security or privacy plans to implement, may consider it in future when it will be necessary.

7. **Error Handling and Resilience:** The only thing that can be go down is API when it is overloaded. If our API will be overloaded we may consider to move to bigger server with powerfull machines and GPUs.

8. **Deployment and DevOps:** In future we may create some program to monitor if our API is down or not.

## **Week 2 questionnaire:**
1. **Tech Stack Resources: Are you utilizing any project-based books that specifically cover your tech stack and help you build your project? If yes, please provide the names of these books (name at least 3). How do you anticipate utilizing these materials to enhance your knowledge and expertise in your tech stack?**
    - Our main idea is based in **[this](https://arxiv.org/pdf/1508.06576v2.pdf)** article.

2. **Mentorship Support: Do you currently have a mentor actively involved in your project? If yes, kindly share the name of your mentor and explain how their guidance has positively influenced your project. If you don’t have a mentor yet, have you considered seeking one? How do you believe having a mentor could contribute to the success of your project? Remember, having an experienced mentor that can guide you and your team is your responsibility.**
    - No, we don't have any mentorship support.

3. **Exploring Alternative Resources: In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack? This could include online courses, video tutorials, documentation, or any other sources that have been valuable in filling knowledge gaps. Please, name at least 3 resources**
    - YouTube
    - Github
    - Kaggle

4. **Identifying Knowledge Gaps: Are there any specific areas within your tech stack where you or your team feel there are knowledge gaps or expertise is lacking? If so, how do you plan to address these gaps and ensure a well-rounded understanding of your chosen technologies? Please name the tech stack division in your team and outline how are you planning to deal with knowledge gaps**
    - Not enough knowledge in Backend and Frontend fields.

5. **Engaging with the Tech Community: Have you actively engaged with the broader tech community to seek guidance or learn from experienced professionals in your tech stack? This could involve participating in online forums and groups (telegram, discord or any other platform), attending local meetups (Kazan, Innopolis)? Do you have means to engage experts into critical tech stack problems through professional networks?**
    - No

6. **Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week? How do you plan to achieve these objectives, and what strategies or resources will you employ to deepen your understanding?**
    - Implement model to make style transfer, using architecture provived in research **[paper](https://arxiv.org/pdf/1508.06576v2.pdf)**.

7. **Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates? Have you organized any knowledge-sharing sessions or discussions to facilitate the exchange of insights and experiences related to your tech stack?**
    - Yes, we organize meetings with my teammate to discuss the project progress.

8. **How have you leveraged AI to compensate for any lacking expertise in your tech stack? Have you utilized AI-powered tools or platforms to expedite the process of acquiring knowledge and expertise in your tech stack?**
    - No

### **Tech Stack and Team Allocation**
In our project we have ML, frontend, backend.
Here is the team responsibilities for these tasks:
- Muhammadjon Hokimiyon - ML, frontend/backend
- Toirov Sadi - ML, API, backend


### **Weekly Progress Report**
Main goal of this week is to understand the architecture of the model.