---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**
 
Tech Stack:
- Backend: Docker, Python, FastAPI, Uvicorn
- Frontend: React, Vite, TypeScript
- Database: MongoDB
- ML: Python, PyTorch, probably MLFlow/AirFlow
- HuggingFace libraries: Diffusers, Transformers
- Yandex Cloud: YandexGPT Pro, Yandex Translator


### **Architecture Design**

1. **Component Breakdown**: 
   - Frontend:

        Main purpose of this section is software to client communication. This is accomplished by getting the image from user, prompt for background, and other parameters such as style (e.g. "Minimalistic") and number of images to generate.

        *Interactions*: The frontend section sends to the backend requests to authenticate, generate prompts, generate an image, etc. On the other side, it receives authentication, background prompts, generated images, etc.
     
   - Backend:

        This section serves as a link between the remaining parts of the software, as well as finalizing the image generation process.

        *Interactions*:
        - Frontend: exchanging user-defined information
        - Database: confirming the identity of the user and getting the assosiated data
        - ML: sending the user-defined data to the ML section to receive the generated image with background.
          
   - Machine Learning services:

        The objective of this section is to apply background to the image considering some other parameters that may be either user-defined or derived from the context.

        *Interactions*: The incoming data is sent from the Backend module to the ML, and after the completion it is sent back.
     
   - Database:

        Database section serves as a way to keep track of different users and their requests. Main purpose is to track accounts with prompts and images history.

        *Interactions*: Database module answers requests from the backend. 

2. **Data Management**:
    The data of user interactions will be stored in a MongoDB database, as it provides needed functionality and the team members are familiar with its features.

3. **User Interface (UI) Design**:
    As intuitive design is one of the major criterias of our project's success, we want it to be easily understandable, while being customizable to utilize the potential of the AI tools. Using Figma, we created a number of possible web pages for the project that can be seen [here](https://www.figma.com/design/08ygt4wuUzztZRmX9QrrJY/cpp.py?node-id=1-4639&t=pdLMvUIkO8mFpCVT-0)

4. **Integration and APIs**:
    Our application ensures efficient communication between the frontend and backend via REST APIs. This architecture facilitates seamless interaction and data exchange, enabling smooth operation of the application.

    For machine learning tasks, most models are executed locally to optimize performance and latency. However, we leverage external services for specific functionalities. YandexGPT Pro and Yandex Translator are integrated using Yandex's provided APIs. YandexGPT Pro generates prompts, while Yandex Translator translates these prompts from English to Russian, enhancing our application's ability to handle multilingual tasks effectively.

5. **Scalability and Performance**:
    Using pretrained models from open sources allows us to reach fast image generation times with good quality. As for scalability, the use of Docker allows us to scale parts of the system based on the demand.

6. **Security and Privacy**:
    Among the current security measures we have authentication for protecting user data and separate Docker installations for protecting the software itself. Regarding to user privacy, we intend to store prompts user used, images they uploaded and generated images they got. We think that it is minimal data we need to store to provide essential user experience.

7. **Error Handling and Resilience**:

   To ensure a reliable and resilient application we are goind to make:

- Logging: We log errors and general events to facilitate manual debugging.
- Monitoring: Continuous monitoring detects and alerts on anomalies in real-time.
- Graceful Recovery: Implementing retry mechanisms and user-friendly error messages.
- Testing: Conduct comprehensive testing, including unit tests, integration tests, and end-to-end tests to maintain code quality and prevent errors from reaching production.

8. **Deployment and DevOps**:
    To streamline the deployment process and establish robust DevOps practices:

- Automated Deployment: Use CI/CD pipelines with Git for automated build, test, and deployment processes. Tests are run during push/merge to the main branch.
- Workflow Management: Integrate MLFlow or Airflow to manage and orchestrate machine learning workflows and data pipelines efficiently.

### **Week 2 questionnaire:**

1) Tech Stack Resources: 
    Given our extensive research on the tech stack, we are confident in our knowledge and do not need to refer to additional books on the subject, except that we lack knowledge on fine tuning diffusers. However, since literature on diffusers is scarce due to its specialized nature, we will rely on articles and consultations with experts to obtain the necessary information.
   
2) Mentorship Support: 
    In the scope of the hackathon, we are guided by representatives from Leroy Merlen. Through the course of the hackathon they helped us to identify the key points of the product that will make it better in the end. Additionally, our TA (Kamil Sabbagh) for the project has a lot of experience with generative AIs and we intend to ask for help if any questions arise.

3) Exploring Alternative Resources:
     To help us look for possible ways to structure and develop our project, we use a variety of information-seeking techniques, looking at sources such as HuggingFace, Kaggle, Medium, and some articles that we can find in Google Scholar.

4) Identifying Knowledge Gaps:
    Within our tech stack, we've pinpointed a knowledge gap regarding fine-tuning diffusers. To address this, we'll prioritize seeking expertise through articles and consultations to ensure a comprehensive understanding of this specialized area.

5) Engaging with the Tech Community:
    Our team actively engages with various experts, including specialists from Leroy Merlin and organizers of the AI Product Hackathon. Through Zoom meetings and Telegram chats, we facilitate meaningful discussions, seek guidance, and learn from their experiences. Additionally, regular interactions with our TA, Kamil Sabbagh, occur through scheduled meetings and ongoing discussions in Telegram.
   
6) Learning Objectives:
    Our team's learning objectives for the week encompass enhancing understanding of our tech stack, particularly in fine-tuning diffusers, and refining our project's development roadmap. To achieve these objectives, we'll leverage various strategies, including targeted research, expert consultations, and active engagement with the tech community.

7) Sharing Knowledge with Peers:

    Our team has an open discussion in a Telegram chat, which allows for members of different responsibilities to share information and experience. This communication is happening on a daily basis, and includes anything from design and parameter changes to creating connections between sections of the project. Additionally, we sometimes do telegram calls to discuss some topics in more detail.

8) Leveraging AI:

    In the writing of this report, a number of different AI tools were used to make the writing quick and correct:
    - LanguageTool: a browser extension for checking the spelling of words and the punctuation in a sentence;
    - TabnineAI: a VSCode extension that predicts and autocompletes a few next words based on the context, which saves time;
    - DeepL Translate: an ML-based service that helps to translate from Russian to English;
    - ChatGPT 4o and 3.5-Turbo: an ML-based service that helps us to rephrase text, fix bugs in code and write comments for code.

> ### **Tech Stack and Team Allocation**

| Team Member          | Track                                       | Responsibilities   |
| -------------------- | ------------------------------------------- | ------------------ |
| Bulat Akhmatov       | Team Lead and ML engineer                   | Coordinate team activities, oversee project progress, guide ML development |
| Alexandra Vabnits    | Product Manager and ML engineer             | Define product vision, align with business goals, guide ML development                  |
| Amir Nigmatullin     | Backend Developer                           | Develop backend systems, implement APIs, ensure system scalability                   |
| Mintimer Karimov     | Data Scientist                              | Build machine learning models, optimize algorithms                   |
| Nurislam Zinnatullin | Frontend Developer and UX/UI Designer       | Design user interfaces, develop frontend components, ensure UX/UI coherence                   |
| Bahdan Shah          | Technical Writer                            | Document project requirements, create technical documentation and reports                |
| Daniil Tiuftin       | Backend Developer                           | Collaborate on backend development tasks, assist with system architecture design                   |

### **Weekly Progress Report**

 Accomplishments:

- developed a prototype in Figma;
- collaboratively designed and refined the machine learning pipeline, exploring alternative solutions for best performance;
- curated and preprocessed the dataset by using manual parsing and neural network-based preprocessing techniques to ensure data quality.

 Challenges faced:

- designing an intuitive user interface proved to be a significant challenge, requiring extensive iteration;
- determining the optimal behavior of the machine learning pipeline in various scenarios;
- data collection and preprocessing involved manual parsing, demanding additional time and effort.
  
 Steps taken to overcome challenges:

- used the collective expertise of team members to continuously refine the user interface;
- analyzed a number of different open source machine learning models and collectively decided on the best approach.

 **Result**: confirmed the importance of collaborative design and development.
