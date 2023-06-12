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