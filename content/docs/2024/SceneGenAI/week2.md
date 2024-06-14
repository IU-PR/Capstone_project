---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

> Copied from last week report  
> need to find any new changes in plans/tools (translator, whatever else there is)
 
Tech Stack:
- Backend: Docker, Python, FastAPI, Uvicorn
- Frontend: React, Vite, TypeScript
- Database: MongoDB
- ML: Python, PyTorch, probably MLFlow/AirFlow
- HuggingFace libraries: Diffusers, Transformers

### **Architecture Design**

1. **Component Breakdown**: 
   
    > вайбы так себе, мне кажется я неправильно что-то в дизайне понял. красиво было бы сюда схемку вставить кстати по типу ![link](https://capstone.innopolis.university/2023/LeetForces/LFreport2.png), но не знаю как там запарно это или нет.
   - Frontend:

        Main purpose of this section is software to client communication. This is accomplished by getting the image from user, prompt for background, and other parameters requiered for the models.

        *Interactions*: The frontend section is connected to the backend for sending and receiving image generation or login requests.
   - Backend:

        This section serves as a link between the remaining parts of the software, as well as finalizing the image generation process.

        *Interactions*:
        - Frontend: exchanging user-defined information
        - Database: confirming the identity of the user and getting the assosiated data
        - ML: sending the user-defined data to the ML section to receive the generated image with background.
   - Machine Learning services:

        The objective of this section is to apply background to the image considering some other parameters that may be either user-defined or derived from the context.

        *Interactions*: The incoming data is sent from the Backend module to the ML, and after the completion it is sent back.
   - Database

        Database section serves as a way to keep track of different users and their requests.

        *Interactions*: Database module answers requests from the backend.

2. **Data Management**:
    > включает ли это датасет?

    The data of user interactions will be stored in a MongoDB database, as it provides needed functionality and the team members are familiar with its features.

3. **User Interface (UI) Design**:
    As intuitive design is one of the major criterias of our project's success, we want it to be easily understandable, while being customizable to utilize the potential of the AI tools. Using Figma, we created a number of possible web pages for the project that can be seen [here](https://www.figma.com/design/08ygt4wuUzztZRmX9QrrJY/cpp.py?node-id=1-4639&t=pdLMvUIkO8mFpCVT-0)

4. **Integration and APIs**:
    > я не знаю как эта часть работает...

5. **Scalability and Performance**:
    Using pretrained models from open sources allows us to reach fast image generation times with good quality. As for scalability, the use of Docker allows us to scale parts of the system based on the demand

6. **Security and Privacy**:
    Among the current security measures we have authentication for protecting user data and separate Docker installations for protecting the software itself.

7. **Error Handling and Resilience**:

    > не знаю

8. **Deployment and DevOps**:

    > тоже не уверен

### **Week 2 questionnaire:**

> ...

1) Tech Stack Resources: 
    > Are you utilizing any **project-based books** that specifically cover your tech stack and help you build your project?
    непонятно
   
2) Mentorship Support: 
    > Name of the TA (i forgot (if you're the TA reading this: im deeply sorry))

    In the scope of the hackathon, we are guided by representatives from Leroy Merlen. Through the course of the hackathon they helped us to identify the key points of the product that will make it better in the end. Additionally, our TA for the project has a lot of experience with generative AIs and we intend to ask for help if any questions arise.

3) Exploring Alternative Resources:
    > опять же, не отвечу

4) Identifying Knowledge Gaps:
    > :|
    > Rephrase the Error Handling and Resilience

5) Engaging with the Tech Community:
    > List of useful reddit posts, youtube videos, https://anvilproject.org/guides for creating a proper markdown idk

6) Learning Objectives:
    > только основа, может ещё что-то

    Learn how to operate large pretrained models and use them in conjunction with other helpful tools.

7) Sharing Knowledge with Peers:

    Our team has an open discussion in a Telegram chat, which allows for members of different responsibilities to share information and experience. This communication is happening on a daily basis, and includes anything from design and parameter changes to creating connections between sections of the project.

8) Leveraging AI:

    > не уверен, возможно надо дополнить опять же модельками из проекта, https://capstone.innopolis.university/docs/2023/innoshop/#1-component-breakdown

    In the writing of this report, a number of different AI tools were used to make the writing quick and correct:
    - LanguageTool: a browser extension for checking the spelling of words and the punctuation in a sentence;
    - TabnineAI: a VSCode extension that predicts and autocompletes a few next words based on the context, which saves time.

> ### **Tech Stack and Team Allocation**

| Team Member          | Track                                       | Responsibilities   |
| -------------------- | ------------------------------------------- | ------------------ |
| Bulat Akhmatov       | [Backend/Frontend/Fullstack/ML/Design/etc.] | [Responsibilities] |
| Alexandra Vabnits    |                                             |                    |
| Amir Nigmatullin     |                                             |                    |
| Mintimer Karimov     |                                             |                    |
| Nurislam Zinnatullin |                                             |                    |
| Bahdan Shah          |                                             |                    |
| Daniil Tiuftin       |                                             |                    |

### **Weekly Progress Report**

> Можно написать про сделанный в фигме фронт, и что-то про склеивание моделей. Про склейку фронта и бэка явно стоит писать не сейчас, да и другие важные приколы по типу добавления моделей тоже лучше оставить на потом.

### **Challenges & Solutions**

...

### **Conclusions & Next Steps**

...