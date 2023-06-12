---
weight: 1
bookFlatSection: true
title: "MockMentor"
---
# **MockMentor**
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
