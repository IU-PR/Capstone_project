# **Pantomime** 


{{< hint danger >}}

**Feedback**  
Write concise and well-written project description here. To enhance it further, we recommend incorporating additional details that provide an overview of your project. Consider including elements such as a project logo, a link to your project's webpage, or any other relevant visual materials that can help showcase your work effectively.  
As we plan to promote your work, it's crucial to ensure that this file serves as a compelling introduction that captures the attention of the potential reader. 
{{< /hint >}}
# **Week 1 report**

## **Team Formation and Project Proposal**


### **Team Members**

| Team Member            | Telegram ID   | Email Address                     |
|------------------------|---------------|-----------------------------------|
| Alexander Kudasov          | @nertsal | a.kudasov@innopolis.university    |
| Anastasia Palashkina      | @skylemn07 | a.palashkina@innopolis.university |
| Daniel Satarov      | @danielpancake | d.satarov@innopolis.university    |
| Daria Verevkina     | @dar_verda     | d.verevkina@innopolis.university  |
| Ivan Chernakov       | @ivanchgram | i.chernakov@innopolis.university  |
| Vitaliy Alifanov       | @adis_forever | v.alifanov@innopolis.university   |
| Vladislav Kulikov     | @slewie | v.kulikov@innopolis.university    |

### **Value Proposition**

* **Problem**: Hand gesture recognition is a wide problem that is a hot topic for research, even to this day. Gesture recognition can be used in many fields, including: medicine, robotics, e-commerce, smart homes, and the internet of things. Just by using your hands, you can manage devices, give commands to computers, and, most importantly, deaf people can communicate with others using the camera and AI gesture-text translation algorithms.

* **Solution**: By recognizing sign language gestures and translating them into text or speech, our software project offers a resolution to this problem. Our solution's major components include real-time video recording, machine learning models for gesture recognition, and translation into text or speech of identified gestures. Our solution is unique because it supports Russian Sign Language(RSL).

* **Benefits to Users**: Users of our software project will get a variety of advantages, such as better interaction with others who do not understand sign language, more independence, and a decreased need for human interpreters. By quickly and accurately translating sign language motions into text or speech, our system increases their productivity, efficiency, and effectiveness. Users can anticipate better user experiences and a more welcoming setting.

* **Differentiation**: In the open source, there are no projects that support RSL and have good UI. By creating a project that supports RSL, we can bridge this gap and ensure that everyone has equal access to technology. In addition, our project will provide an API that can be used by other developers to integrate RSL into their own projects. The interface of our project will be easy to use and intuitive, making it accessible to a wide range of users. By prioritizing accessibility, we can ensure that our technology serves the needs of the deaf community.

* **User Impact**: Our software project's wider impact is that it enhances inclusion and communication for those with hearing impairments. It enables them to interact with people more efficiently and lessens the demand for human interpreters. The way that persons with hearing loss engage and communicate with one another could be changed by our approach.

* **Use Cases**: 
  - educational service
  - video conferencing service
  - service for finance and government companies


## **Lean Startup Questionnaire**

1. **What problem or need does our software project address?**

Our project is planned to solve problems with understanding deaf and hard-of-hearing people.

2. **Who are our target users or customers?**

Our project will be accessible for everyone. It should help communicate with people who have problems with speaking or/and listening.

3. **How will we validate and test our assumptions about the project?**

We need to train and test our machine learning models on the collected dataset to ensure that they are accurate and can recognize sign language gestures with a high degree of accuracy. We can create test our project with user knowing sign language. Based on the user feedback, we can iterate on the design and functionality of the system and make any necessary pivots. Once we have made changes to the system, we can test it again with a larger group of users to validate our assumptions and ensure that the changes we made have improved the system.

4. **What metrics will we use to measure the success of your project?**

We decide that metrics will be accuracy in the translation and correct compilation of sentences.

5. **How do we plan to iterate and pivot if necessary based on user feedback?**

Users who have used the sign recognition system to translate sign language motions can provide feedback, which can be analyzed to find any areas that could use improvement or prospective pivots.
We can enhance the machine learning models to improve the translation accuracy based on user feedback. To enhance the accuracy and utility of the sign recognition system, modifications can be made. This can entail including fresh features, enhancing the user experience, or fixing any accuracy problems that emerged during testing.
After making adjustments to the sign recognition system, we can test it again with a broader user base to confirm our hypotheses and make sure the system has been made better. This cycle of gathering feedback, evaluating it, enhancing the machine learning models, putting modifications into place, and testing once more may be repeated until we have a sign recognition system that satisfies the requirements of our users and offers precise translations.

## **Leveraging AI, Open-Source, and Experts**

### **AI (Artificial Intelligence)**

Artificial Intelligence is a crucial aspect of the project. Our team will develop or use machine learning algorithms that recognise and translate sign language into text in real-time. We plan to design or find and train an AI model with a large dataset of videos using sign language.

### **Open-Source**

Open-source solutions can be used to reduce work-load and overall development time. Popular platforms such as GitHub, Kaggle, and others have an extensive list of projects, datasets, and pre-trained models related to sign language recognition and real-time captioning, all of which will be useful to our team. Our team also aims to contribute with the project to hopefully improve the quality of the software.

### **Experts**

Our team hopes to get valuable feedback for the experts in relevant domains, such as sign language linguists and computer vision engineers.

## **Inviting Other Students**

We are looking forward to any help in the area of sign languages (especially Russian at the moment). If the student has any experience or knowledge, we would be glad to invite them to maintain proper understanding of sign gestures and their meaning.

## **Defining the Vision for Your Project**

### **Overview**

The goal of this project is to create a sign recognition system that can instantly identify any sign language motions. The system will be created to specifically address the issue of communication hurdles that those who are deaf or hard of hearing experience. This initiative aims to provide a more effective and accurate method of sign language interpretation, while also increasing communication accessibility and inclusivity for the deaf and hard of hearing community.

### **Schematic Drawings**

```
        +------------------+
        |                  |       
        |                  |      
        |   User's Video   |      
        |                  |      
        |                  |
        +------------------+
                 |
                 |
                 |                        
        +-----------------+      +--------+--------+      +-----------------+
        |                 |      |                 |      |                 |
        |                 |      |                 |      |    Query for    |
        |     Frontend    +------+     Backend     +------+                 |
        |                 |      |                 |      |  Neural Network |
        |                 |      |                 |      |                 |
        +--------+--------+      +-----------------+      +-----------------+
```

### **Tech Stack**

This project is mainly a computer vision task, so the stack is going to be Python with PyTorch, Rust with Axum for backend

### **Anticipating Future Problems**

The need for a sizable dataset of sign language gestures for training the machine learning model could provide a problem during the project development phase. Real-time gesture processing is another potential issue, which would necessitate performance tuning of the computer vision system.

### **Elaborate Explanations**

The core functionality of the system will be the computer vision algorithm that recognizes sign language gestures. To recognize the gestures, the program will combine machine learning with image processing methods. PyTorch will be used to train the machine learning model using a dataset of sign language motions. The system will also have a user interface that shows the movements that have been recognized and outputs text or audio. One distinctive feature of our approach is the application of machine learning to enhance the precision of gesture detection, which will offer a more effective and precise method of deciphering sign language.


{{< hint danger >}}

**Feedback**  
You have a strong team and a brilliant project idea. It is also clear that you have a vision of the project.
However, I think success of your project will heavily depend on the availability of data to train and deploy your model. So, for me it's not clear yet how are you planning to solve this.

Since this course aims to finish the semester with an MVP - minimal viable product, consider scaling your project down to creating a model that does core/main things - perhaps 5-10 sign words, but does that with speed and can translate in real time. Therefore, I would advice you to focus on collecting a dataset of few signs, training a model and building the core of the web app (remember, we have only 7 weeks). Put the main emphasis on the technology core that you need to showcase: fast (near-real time) recognition of signs. Also, consider collaborating with relevant communities for data collection, i.e.: https://www.tatvog.ru/  
{{< /hint >}}

# **Week 2 report**

## **Architecture Design**

1. **Component Breakdown**

  - Video Input (web development division). This module will take in the video (or, in prospect, capture it from the user’s device) and pass it on to the next module. 
  - Image Processing (back-end division). This module will process the input and pass processed data further.
  - Sign Language Recognition (machine learning division). This module will recognise the hand gestures and convert them into text.
  - Captioning Module (web development division). This module will take recognised text and display it back as an output on the user’s side.

2. **Data Management**

In our project, there is no need to store data, because Pantomime only recognize sign language

3. **User Interface (UI) Design**

The main struggle in our product is ML and CV algorithms, to understand sign language. So, for UI we decided not to go too complicated. It will be a common 1-page web layout, with an explanation of our product, a window to send  a video or activate camera streaming for further translation and information related to our team.

4. **Integration and APIs**

We are not going to use anything external.

5. **Scalability and Performance**

For better scalability and performance, we plan to deploy all parts of the project on different servers. It allows simplifying scale or improve the performance of the Pantomime.

6. **Security and Privacy**

We are not going to store any user data, so we only need to have a secure connection to the web server which is provided by https.

7. **Error Handling and Resilience**

We plan to log results of the model’s inference in order to understand the quality of the model and calculate real metrics.

8. **Deployment and DevOps**

We have established development and operations processes as follows: in our GitHub page, we have three repositories for each team, and each team member has to create a new branch with their additions or changes to the main branch. After that goes pull request and review of changes by the team. If the pull request satisfies the corresponding team, they merge it.

Changes of the backend and frontend could be seen automatically on the server, where we host the platform.


## **Week 2 questionnaire**

1. **Tech Stack Resources: Are you utilizing any project-based books that specifically cover your tech stack and help you build your project? If yes, please provide the names of these books (name at least 3). How do you anticipate utilizing these materials to enhance your knowledge and expertise in your tech stack?**

No, we don’t use any project-based books.

2. **Mentorship Support: Do you currently have a mentor actively involved in your project? If yes, kindly share the name of your mentor and explain how their guidance has positively influenced your project. If you don’t have a mentor yet, have you considered seeking one? How do you believe having a mentor could contribute to the success of your project? Remember, having an experienced mentor that can guide you and your team is your responsibility.**

Now, we don’t have a mentor, but we consider seeking one. Having a mentor can provide valuable guidance and support, share their experiences and knowledge, and help you navigate challenges and roadblocks. A mentor can also provide a fresh perspective on your project and help you identify areas for improvement.

3. **Exploring Alternative Resources: In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack? This could include online courses, video tutorials, documentation, or any other sources that have been valuable in filling knowledge gaps. Please, name at least 3 resources**

To expand our understanding of the technology stack, we have explored the following resources:
  - Online courses. To refresh and brush up our knowledge on Python, CV, and NLP, we have explored some free courses on online platforms like YouTube, Coursera, Udemy, and edX.
  - Video lectures and tutorials. We have watched video materials on YouTube to study basic ASL and RSL signs and how facial expressions, and body language are used.
  - Documentation. We have read documentation of libraries and frameworks that we are using or going to use to understand capabilities of each one. So far, we have looked into docs of such libraries as OpenCV, TensorFlow, and PyTorch

4. **Identifying Knowledge Gaps: Are there any specific areas within your tech stack where you or your team feel there are knowledge gaps or expertise is lacking? If so, how do you plan to address these gaps and ensure a well-rounded understanding of your chosen technologies? Please name the tech stack division in your team and outline how are you planning to deal with knowledge gaps**

Our team consists of three divisions: machine learning, back-end, and web development.

In the machine learning division, we feel that we yet lack expertise in advanced image and video processing and natural language processing. To address these gaps, we plan to use resources like free online courses, and video lectures and tutorials. We also plan to improve our understanding of ASL and RSL grammar and syntax by consulting ASL and RSL signers and studying available materials online.

In the web development division, we feel that we need to improve our knowledge of async and real-time (in prospect) web applications. To address this gap, we plan to study available materials online.

5. **Engaging with the Tech Community: Have you actively engaged with the broader tech community to seek guidance or learn from experienced professionals in your tech stack? This could involve participating in online forums and groups (telegram, discord or any other platform), attending local meetups (Kazan, Innopolis)? Do you have means to engage experts into critical tech stack problems through professional networks?**

For now, we do not attend any community meetings or forums because our idea is new and not very common

6. **Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week? How do you plan to achieve these objectives, and what strategies or resources will you employ to deepen your understanding?**

Our ML engineers decided to learn how to create a model that can recognize sign languages in a real-time. For this purpose, they checked existed solution for ASL and took some data preprocessing features to our project.

7. **Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates? Have you organized any knowledge-sharing sessions or discussions to facilitate the exchange of insights and experiences related to your tech stack?**

Yes, we have organised team sessions, where each part of the team (frontend, backend, and ML) shared their ideas and knowledge and came up with a plan for making the final product.

Moreover, at the end of each week we hold team sessions, where we discuss difficulties, thoughts, and any suggestions that one of us could come across during the week.

8. **How have you leveraged AI to compensate for any lacking expertise in your tech stack? Have you utilized AI-powered tools or platforms to expedite the process of acquiring knowledge and expertise in your tech stack?**

For the prototype version of our platform, we will be using a pre-existing model for Russian Sign Language (RSL) detection that was trained on over 16 GB of RGB videos. This approach allows us to test both the backend and frontend parts of our product without relying from the start on our own model. Furthermore, when our team was brainstorming project ideas, we used ChatGPT to consider more options to choose from.

## **Tech Stack and Team Allocation**

After our first team meeting, we divided the team into three groups: frontend, backend, and ML, taking into consideration each person's preferences and strengths. Each unit has a designated lead who is in charge of supervising its activities. Team members are not limited to those responsibilities alone, even if they tend to focus on those that are specific to their unit.

| Team Member            | Role                           | 
|------------------------|--------------------------------|
| Alexander Kudasov          | Backend Developer              | 
| Anastasia Palashkina      | Frontend Developer             | 
| Daniel Satarov      | Frontend Developr, ML engineer |
| Daria Verevkina     | Designer, Frontend Developer   | 
| Ivan Chernakov       | Designer, ML engineer          | 
| Vitaliy Alifanov       | ML engineer                    | 
| Vladislav Kulikov     | Team Lead, ML engineer         | 