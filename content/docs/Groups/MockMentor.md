---
weight: 1
bookFlatSection: true
title: "MockMentor"
---
# **MockMentor**

- https://docs.google.com/presentation/d/1zovQb_PR696bnXYWAZnWumElyF3NsTbc4F1QvEJkTNw/edit#slide=id.p

# **Introduction**
 
{{< hint danger >}}

**Feedback**  
Write concise and well-written project description here. To enhance it further, we recommend incorporating additional details that provide an overview of your project. Consider including elements such as a project logo, a link to your project's webpage, or any other relevant visual materials that can help showcase your work effectively.  
As we plan to promote your work, it's crucial to ensure that this file serves as a compelling introduction that captures the attention of the potential reader. 
{{< /hint >}}

# **Week #1 Report**

### **Team Members**

| Team Member        | Telegram ID                                          | Email Address                       |
| ------------------ | ---------------------------------------------------- | ----------------------------------- |
| Elaman Turekulov   | [@bal1an](https://t.me/bal1an)                       | e.turekulov@innopolis.university    |
| Dmitry Naumov      | [@DmitryNau](https://t.me/DmitryNau)                 | d.naumov@innopolis.university       |
| Albert Avkhadeev   | [@tatarinalba](https://t.me/tatarinalba)             | a.avkhadeev@innopolis.university    |
| Albert Khazipov    | [@drxelt](https://t.me/drxelt)                       | a.khazipov@innopolis.university     |
| Ivan Orekhov       | [@iorekhov](https://t.me/iorekhov)                   | i.orekhov@innopolis.university      |
| Oleg Hlopcev       | [@maintheme](https://t.me/maintheme)                 | o.hlopcev@innopolis.university      |
| Maksim Oinoshev    | [@Macoyshev](https://t.me/Macoyshev)                 | m.oinoshev@innopolis.university     |

### **Value Proposition**

- Identifying the Problem:
While tools like leetcode allows people to prepare for test questions in job interviews, candidates still do not know the whole process of the interview and lack the experience of a real interview. They often feel stress and nervousness. The lack of experience is one of the main reasons for these emotions.

- Solution Description:
Our project allows candidates not only to solve practice questions, the main function is ability to pass mock interviews with an AI. Questions that are similar to those that are usually asked in real interviews and then provided with feedback. Moreover, to imitate the real interview, the candidate will be able to answer through his microphone and receive questions via audio too.

- Benefits to Users:
Users will be able to prepare for future job interviews. Understand the skills that are needed to secure the job and go through the interviews being ready and not to be nervous.

- Differentiation:
Our product is going to imitate the real interview using AI. Interviews will include the candidate answering through their microphone and getting questions via audio too. Give the user detailed feedback and show the room for improvement.

- User Impact:
Our project in a broader sense will allow people to easily get ready for interviews and get a glimpse and experience of going through an interview. 

- User Testimonials or Use Cases:
People often do not know what to expect from a job interview, especially if they never did it. They tend to get nervous and the lack of experience makes them even more nervous. Our project will allow such people to get near real experience of a job interview.

## **Lean Startup Questionnaire**

1. What problem or need does your software project address?
The need for people to experience what a real interview is like and how to successfully go through it.
2. Who are your target users or customers?
People who want to get ready for a job interview.
3. How will you validate and test your assumptions about the project?
Our team will ask other students to pass through a mock interview and give their feedback.
4. What metrics will you use to measure the success of your project?
Again, the main metric will be the feedback of other people and our team’s subject opinion.
5. How do you plan to iterate and pivot if necessary based on user feedback?
Our team will try to adapt to the feedback and adjust the product for targeted audience

## **Leveraging AI, Open-Source, and Experts**

- AI (Artificial Intelligence):
    - Voice the question to the candidate;
    - Recognize the voice of a candidate and convert it to text for an AI;
    - Rate the correctness of the candidates answer.
- Open-Source:
    - OpenAI
    - [coqui-ai](https://github.com/coqui-ai/TTS) - translates text into sound with high quality and the voice sounds like a human voice
    - speech_recognition lib - translates sound into text with high quality
    - Hugging face - extremely powerful and large system. It will be really helpful for our project
    - Transformers - for comparing semantic similarity of the texts. Our team use this open source solution because our team needs powerful pretrained models
- Experts in relevant domains:
    - Rustam Lukmanov: instructor of Capstone Project course, to address the issues our team might face during development of the project.

## **Inviting Other Students**

For now, our team does not think it will need any collaboration in developing the software from other students. However, for validation and metrics the feedback and opinion of other students will be needed.

## **Defining the Vision for Your Project**

- Overview:
The project is about creating mock job interviews with an AI that functions as an interviewer. It allows people to get ready to future job interviews via near-real job interview experience.

- Schematic Drawing:

![Schematic Drawing](/MockMentor/schematic_drawing.svg)

- Tech Stack:
For now, we decided to use these stacks/frameworks for our project:
    - Frontend: 
        - React, react-dom, Redux - frameworks that our team is the most familiar with
    - Backend: 
        - FastAPI - simle and asynchronic, has a swagger and can integrate with pydantic
        - PostgreSQL - because our model have a clear and simple structure 
    - ML: 
        - Python - because its the easiest tool that our team is familiar with
        - Pytorch - because it is extremely popular and powerful and  our machine learning engineers are well known with this framework

- Anticipating Future Problems:
The testing and validating of an AI to successfully rate and give useful feedback will be needed to thoroughly parameterized. Therefore, other students will be asked to test the product and give feedback.

- Elaborate Explanations:
Our team will use Scrum and Agile methodology. Core functionality of the project is to provide a client a mock interview with an AI with feedback. The unique aspect of our solution is that client is able to go through interview by talking and receiving a voiced answer from an AI.

{{< hint danger >}}

**Feedback**  
It is an interesting project! Great job on identifying the problem that candidates face in job interviews and proposing a solution to address it. Your project aims to bridge the gap between traditional practice questions and real interview experience, providing users with an opportunity to simulate mock interviews with an AI. This approach can greatly benefit candidates by allowing them to practice in a more realistic setting and receive valuable feedback, and perhaps, will make Innopolis students the most in-demand among other University graduates.

To further enhance your project, consider expanding on the specific features and functionalities that will be offered to users. How will the AI simulate real interview questions? Will it adapt based on the candidate's responses? Additionally, highlighting the personalized feedback aspect can emphasize the value users will gain from the platform.

Will it be a language model with a dedicated persona? Which language model you want to use? In general, I think you can contact Vladimir Ivanov, as far as I know, he works on a similar topic
{{< /hint >}}

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

- Tech Stack:
For now, we decided to use these stacks/frameworks for our project:
    - Frontend: 
        - React — powerful JS/TS library for building UI based on components
        - react-dom — simple library for creating routing on the website
        - Redux — library for making and switching between states on the website
        - Typescript — language that helps us prevent problems in JS and adds static typing
    - Backend: 
        - FastAPI - simle and asynchronic, has a swagger and can integrate with pydantic
        - PostgreSQL - because our model have a clear and simple structure 
        - pydantic - fast and supports type annotation
        - sqlMolde - new ORM that support type annotation, with total compatibility with pydantic and sqlAlchemy
    - ML: 
        - Python - and most of ML related libraries
        - Pytorch - because it is extremely popular and powerful and  our machine learning engineers are well known with this framework

### **Architecture Design**

1. **Component Breakdown**: There're three major components that will form our software solution: frontend, backend and ML. As can be expected, 
    - Frontend interacts with the user;
    - Backend serves as a bridge between frontend and ML, focuses on API and back-end logic;
    - ML performs three main functions: 
        - Converts the questions and feedback of an interviewer text-to-speech;
        - Converts the answers of the user speech-to-text;
        - Using NLP model will rate the correctness of user's answer and highlight the errors of the user.

2. **Data Management**: Data will be stored in a postrgres Database. There the questions, answers and a REFERENCE to audio files(questions and answers) will be stored.

3. **User Interface (UI) Design**: Our UI will be a simple chat-looking page with additional feature to write and compile user's code. Below you can see how it will look like.
![webpage_ex1](/MockMentor/webpage_ex1.jpg)
![webpage_ex2](/MockMentor/webpage_ex2.jpg)

4. **Integration and APIs**: RestAPI will be used for communication between frontend and backend. Backend and ML service will communicate through grpc. 

5. **Scalability and Performance**: Our project is built on microsystems, therefore it will be easily scalable. For example, we can just increase the number of instances of ML service. As each part of the project is done separately, we can increase the power of each part distinctively.

6. **Security and Privacy**: Right now, there is no security measures. There's no authentication, authorization and encryption. In future we are planning to add all of this and use jwt token.

7. **Error Handling and Resilience**: For now, there is no monetoring system but in future we are planning to add sentry to monitor the errors. All important events in the system will be logged.

8. **Deployment and DevOps**: Right now, there is now deployment and DevOps. In future, we are planning to add CI/CD and deploy via Kubernetes.

## **Week 2 questionnaire:**  

1) Tech Stack Resources: Are you utilizing any **project-based books** that specifically cover your tech stack and help you build your project? If yes, please provide the names of these books (name at least 3). How do you anticipate utilizing these materials to enhance your knowledge and expertise in your tech stack?
Right now, we do not utilize any project-based books.

2) Mentorship Support: Do you currently have a mentor actively involved in your project? If yes, kindly share the name of your mentor and explain how their guidance has positively influenced your project. If you don't have a mentor yet, have you considered seeking one? How do you believe having a mentor could contribute to the success of your project? Remember, having an experienced mentor that can guide you and your team is your responsibility.
Right now, we do not feel a need in a mentor. However, if problems will arise, our team is planning on contacting professor Vladimir Ivanov for help as a mentor.

3) Exploring Alternative Resources: In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack? This could include online courses, video tutorials, documentation, or any other sources that have been valuable in filling knowledge gaps. Please, name at least 3 resources
- Design: To create a decent 'material' style design, we used sites to browse palettes and find appropriate colors. Mainly, Design team followed the guide on https://m3.material.io/. Our designer also mastered the basics of working with Figma, including how to make prototypes and animations. To complete this task, they watched several videos on YouTube: https://www.youtube.com/watch?v=gofICZUqltY&t=155s and https://www.youtube.com/watch?v=20IfkyJigKg.
- Frontend: For learning typescript and react frontend team watched videos on UlbiTV YouTube channel and read the official documentation. 
- Backend: Stepik and hexplet is where our Backend learned their stack from. Official documentantion of frameworks and libraries also helped
- ML: ML team used stepik course(https://stepik.org/course/92488/promo?search=2283969634) for a general understanding of neural networks and for working with audio. Also this course(https://stepik.org/course/54098/syllabus) was used understanding what is NLP and how it works. Our ML team used this documentation (https://huggingface.co/) to understand how transformers work.

4) Identifying Knowledge Gaps: Are there any specific areas within your tech stack where you or your team feel there are knowledge gaps or expertise is lacking? If so, how do you plan to address these gaps and ensure a well-rounded understanding of your chosen technologies? Please name the tech stack division in your team and outline how are you planning to deal with **knowledge gaps**
- Design: For now, our designer has no problems with working on project. However, if there will be any technical issues he is planning to use video guides and courses.
- Frontend: Our team is planning to read the documentation, watch video guides and if error occurs - find answers via StackOverflow
- Backend: Our backend team is struggling with working in a cloud. To deal with it, they are planning to pass the Yandex course about using their cloud service.
- ML: There is need to deepen the understanding of some models and embeddings. To deal with this our team is planning to read some articles and documentation (https://huggingface.co/docs/transformers/model_doc/roberta
https://www.kdnuggets.com/2021/11/guide-word-embedding-techniques-nlp.html
https://medium.com/nlplanet/two-minutes-nlp-11-word-embeddings-models-you-should-know-a0581763b9a9)

5) Engaging with the Tech Community: Have you actively engaged with the broader tech community to seek guidance or learn from experienced professionals in your tech stack? This could involve participating in online forums and groups (telegram, discord or any other platform), attending local meetups (Kazan, Innopolis)? Do you have means to engage experts into critical tech stack problems through professional networks?
Not really, right now, we do not face any problems and see no need in such guidance.

6) Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week? How do you plan to achieve these objectives, and what strategies or resources will you employ to deepen your understanding?
There is a list of learning objectives and things that our team learned this week.
- Design: How to design websites and use Figma for designing them. Also, basic animation skills in Figma
- Front: How to work with components in react, how to make routing in react 18. 
- ML: Our ML team have learnt how to work with TTS library (https://github.com/coqui-ai/TTS) and how to convert speech to text using different approaches. Now we want to learn about semantic comparison of 2 texts. (https://towardsdatascience.com/semantic-textual-similarity-83b3ca4a840e) (https://huggingface.co/tasks/sentence-similarity)
- Backend: For now, backend team is building an architecture of our project and making and decomposing tasks

7) Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates? Have you organized any knowledge-sharing sessions or discussions to facilitate the exchange of insights and experiences related to your tech stack?
Yes, our team organizes several meetings throughout the week to discuss both objectives and results of each week and sessions to discuss every stack in particular.

8) How have you leveraged AI to compensate for any lacking expertise in your tech stack? Have you utilized AI-powered tools or platforms to expedite the process of acquiring knowledge and expertise in your tech stack?
Right now, we do not use any ChatGPT-like products. However, we use several AI libraries and open source materials that might help in our project including text-to-speech, speech-to-text and others.

### **Tech Stack and Team Allocation**

As mentioned above, our development process is divided into three major components: ML, frontend and backend. To ensure efficiency and responsibilities of each team member we host at least 2 online sessions each week to peer review each member of our team. Here are responsibilities of each member:
- Elaman Turekulov - team lead and tech writer. Writes reports, hosts meetings, also functions as a PM asking every member of the team about their weekly goals, tasks and the result of work of each person in the end of each week.
- Dmitry Naumov - Data Scientist, right now works on text-to-speech, later is going to work on NLP model with Albert Khazipov
- Albert Khazipov - Data Scientist, right now works on speech-to-text, later is going to work on NLP model with Dmitry Naumov
- Albert Avkhadeev - backend developer and PM
- Ivan Orekhov - frontend developer. Develops the frontend for the whole project.
- Oleg Hlopcev - Data Engineer and designer. Developed the design of our website through figma.com. Responsible for writing a PostgreSQL database. 
- Maksim Oinoshev - backend developer.
---

### **Weekly Progress Report**

Below you can see the tasks that we finished this week:

- ML - Discussed the process of synchronising with backend. Rough version of text-to-speech and speech-to-text model is done.
- Frontend - made the design for our website and wrote the frontend in Typescript from design made. 
- Backend - Chose the architecture(domen driving design) and got familiarized with documentation of libraries and frameworks. Formed and broke down the tasks.
- Design - made the design for the website, right now the logo is being made

# **Week #3**


- **Technical Infrastructure**: All of the necessary technical infrastructure required to support your prototype development should be ready to use. If this is still not done, make it a priority number one. This may involve creating a shared development environment, including all necessary frameworks and platforms (i.e., GPU servers). Ensure that your development environment is ready for efficient coding and testing. Make sure all team members can efficiently utilize the development infrastructure, if not - organize learning sessions explaining the process. This is an absolute priority for the success of the project.
    - Frameworks: 
        - backend: FastAPI
        - frontend: React
        - ML: pytorch
    - Platforms: server on Arch, upload from Github, use PM2(allows to track processes, support them, kill them), everything is wrapped with docker. 

- **Backend Development**: 
    - ML: text-to-speech and speech-to-text is already done, semantical comparison of text in process. ML model is already merged with backend.
    - APIs: RestAPI, grpc are already nastroeny and function
    - Server-side logic: PM2 - visor that checks whether everything is functioning. 

- **Frontend Development**: UI and the website itself is ready, messages between server and user are already possible. Right now, backend and frontend are merging

- **Data Management**: Scheme and database are already done. Dataset writing is in progress.

- **Prototype Testing**: Right now our team uses manual testing. We are going to write tests later

---

## **Progress report**:  

 - Prototype Features: speech-to-text, text-to-speech. ML is connected to back. frontend is almost connected to backend.

 - User Interface: 
    ![ui1](/MockMentor/ui1.jpg)
    ![ui2](/MockMentor/ui2.jpg)

 - Challenges and Solutions: Share any challenges or obstacles you encountered during the development of your prototype. Describe how you addressed these challenges and provide insights into the solutions you implemented.
    - ML: some models can not handle big texts - changed models to those that can handle big texts. while merging with backend problems with dependencies occured - upgraded the versions of libraries
    - backend: backend did not set up on server - wrapped with docker. problems with cors(backend and frontend couldn't communicate) - turned off cors. Code did not correspond to PEP8: downloaded formators, lintr - nastroili and formatted the whole code.  
    - frontend: problems with interacting with backend. Solved by using docker.

- Next Steps: 
    - ML: finish a model to compare semantiacal similarity of texts
    - backend: merge with frontend, adjust the server
    - frontend: merge with backend, code window
    - database: write dataset for testing 


{{< hint danger >}}

**Feedback**  
Hi, glad to see good progress on the project! Your idea is already taking shape, as it's evident by the first prototype that you have shown in the report. 
In general, I think this project can be very influential, as virtually everyone who ever applied to a job would be better off by using this service. Also, job search portals like HH.ru and others don't have such a feature, so you are truly on the frontier! 
I think this project is innovative and exciting - and I am sure backend integration with the frontend will be timely completed. I also like that you decided to keep simple UI with only basic features. 
Keep up the pace and continue the good work!
5/5 for both weeks.
{{< /hint >}}


# **Week #4**

## **External Feedback**
We asked our collegues and friends to test and give feedback on our prototype. Right now, frontend and backend are not merged, therefore testing was done on each part separately. Overall, the feedback was mostly positive, but there were some moments that testing group found lacking and gave us some suggestions.

Testing group liked the simplicity of the frontend, but the ML part still needs adjustments. NLP and text-to-speech were the parts with most problems. Ranking the correctness of the user's answer still needs some adjustments and parametrisation. For now, our team also needs to enlargen the dataset of answers (which are used to check correctness of user's answer to a question) for interview questions. Also, generating voiced questions takes longer than desired and needs optimising.

## **Testing**
We used manual testing to test our prototype and found bugs and parts that still need adjustments.

Right now, NLP and text-to-speech are continuously tested and improved. Still, it needs improvements: text-to-speech still needs more human-like voice(more intonations and less memos and empty spaces), NLP that is used to check the correctness(the similarity between received and one of expected answers) is not yet perfected and needs adjustments. 

In frontend some bugs were found related to showing the message to the user. Also, the voiced question sometimes took too long.

## **Iteration**
Throughout the development several points of our project were reconsidered and changed. The desing was firstly a bit different, but then more simple desing with more contrast coloring were used. For backend, our team got rid of some libraries and decided to use others. Also, our team considered voicing the questions in interview ourselves, but then decided to go for text-to-speech. Moreover, the use of answers by voice was introduced from beginning, it was a decision we made to make the interview closer to real life job interview. For frontend, it was decided not to use redux, since the frontend part was not that large.


{{< hint danger >}}

**Feedback**  
Good, we still have some time to integrate the front with the backend. Make it a priority for the next week!
5/5 for both weeks.
{{< /hint >}}

---


# **Week #5**

## **Weekly tasks**

- Regarding stakeholders, our team came up with the idea ourselves and do not have any funding or stakeholders. 

- Our target audience is people looking for a job. Therefore, Innopolis students are ideal users to test our product. 

- We used the Google Forms to receive feedback from our peers. The feedback showed that there were several points that users liked:
    - the simplicity of the UI
    - the idea of a project 
    - the ability to use voice mesages that are translated into text on the fly. 
- However, there were also some drawbacks that users faced. The main problems that users highlighted:
    - the number of questions, there are still not enough of them, our team is planning to add more
    - the absence of feedback (because right now, our product only gives you the percent of how correct your answer is) 
    - problem with recognizing the voice (especially with different accents)
    - users wanted some summary of the interview, showing how well the users performed it, and which themes

- As for the documentation of the feedback, we used Google Docs to assign importance of each problem. The areas of improvement and enhacement were written down and are currently being either fixed or improved. 

- Right now, our team finally merged frontend and backend. We faced several problems (our hosting banned us, one of our team members left), we finally merged all parts and our project can at least function. For now, some functions are not fully implemented and few problems occured.


# **Week #6**

## **Presentation**

- https://docs.google.com/presentation/d/1zovQb_PR696bnXYWAZnWumElyF3NsTbc4F1QvEJkTNw/edit#slide=id.p

{{< hint danger >}}

I am pleased to see that project is rapidly taking shape! Merging the front and back is a great leap forward. 
Moved the presentation to the top. You guys have accomplished a lot! Thank you for the hard work and dedication.
5/5 for the week, and see you soon! Cheers, Rustam
{{< /hint >}}