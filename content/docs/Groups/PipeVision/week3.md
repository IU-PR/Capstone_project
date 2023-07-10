---
weight: 1
bookFlatSection: true
title: "Week 3 report"
---

# **Week #3**

### **Developing the first prototype, creating the priority list**

1. **Technical Infrastructure**: 
We created a GitHub repository for version control and efficient collaboration within our team. Also, an environment for securing personal data was arranged. Now we  are focused on communicating with Innopolis university about servers with GPU for our neural network. 

2. **Backend Development**:
Our backend developers started code ORM models and functions for database interaction. They use FastAPI to communicate with frontend side. Neural model API  is in the process of creation. ML engineers are busy with exploratory data analysis, literature review for proper model development.

3. **Frontend Development**: 
Frontend developers created Figma prototype which you can see at this [link](https://www.figma.com/file/8GptNZR7FKOFAn1fp20Qth/Untitled?type=design&node-id=0%3A1&mode=design&t=jTJVSX1OCVDesa8g-1)
Now they are working on two pages: login and the main one. The work process can be reviewed at [GitHub](https://github.com/Vikono/PipeVision/tree/Frontend)

4. **Data Management**: 
Our database engineer built a ER-model.
![ER-model](/PipeVision/ER_model.png "ER-model").
Then he created a PostgreSQL database and deployed it on his own server. Implementation of data retrieval functions is under the responsibility of backend developers.

5. **Prototype Testing**: 
We tested our Figma  prototype against the defined user flows and scenarios within our team and customer. They gave feedback about the interface, and upon this information we made corrections to our design. 

### **Progress report**:
1. **Prototype Features**: 
Our prototype has several features at the moment: 
 - user can sign in using predefined login and password
 - user can upload a photo for further recoginition
 - user may log out by clicking the exit button and in pop-up window confirm or deny exiting

2. **User Interface**: 

*Login*: 
User can enter predefined login and password to enter our system. Other pages will be blocked until the user enters.
![Login page](/PipeVision/login_page.png "Login").

*Main page*: 
A user can browse only one file via a special button with a 200 mb upper bound. A window with user files is opened after clicking the button to choose a proper file in the user system. After it, the chosen picture is sent to the backend and the output picture with marking is shown in the answer field.
![Main page](/PipeVision/main_page.png "Main page").

History page is shown in the Figma prototype but it is not included in first MVP feature set. 

3. **Challenges and Solutions**: 
The main challenge is to collect a proper data set. Pictures of pipes with markings are taken in live mode by workers of Gasstroyprom. So, it is a time-consuming and inefficient but unimprovable process. To ensure high quality of photographs we created cloud storage which also is good for cooperative usage within our team and customer.
Another challenge is CV model design due to unstable format of marking and lack of data.

4. **Next Steps**: 
We are planning to implement backend logic firstly. It includes component interaction and ML model development. The next priority is given to history page development. Furthermore, we think to organize several sessions with interface testing and improve desing correspondingly. Another important task is to deploy whole solution to the university servers. All these tasks are decomposed and introduced in our task management system. 



{{< hint danger >}}
**Feedback**  


**Prototype Features**<br>
What your listed in not features

features refer to the distinct functionalities or capabilities provided by a software application. They are the things that an application can do to fulfil user needs and requirements.


**User Interface**<br>
Good design.
But it have a lot of white spaces. Try to utilise this.

**Challenges and Solutions**<br>
Good!

**Next Steps**<br>
Too short. have you considered anything beside development. Like texting with users or unit testing?

**Overall**<br>
Good report

**Grade<br> 4/5**


_Feedback by Moofiy_
{{< /hint >}}