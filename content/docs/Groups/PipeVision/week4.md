---
weight: 1
bookFlatSection: true
title: "Week 4 report"
---

# **Week #4**

### **External Feedback**

We decided to organize user acceptance testing to make sure users are satisfied with our interface. 
According to the UAT requirements, conduction criteria were described:
 - the prototype has the first features set - the starting point for the UAT
 - the interface is accepted by the client - the end point for the testing 

We designed the acceptance tests and sent them to the client. 
![User acceptance test](/PipeVision/user_testing.jpeg "User test").

Then, feedback was collected. 

**Feedback:**
 -  meaning of all buttons is intuitively understandable 
 -  all use actions can be done easily and fast 
 -  no error message when login or password were typed incorrectly
 -  no strictly defined boundaries for file extensions
 -  only english language is available 


 Overall, the client is satisfied by our design except for small details. Also, the company underlines the importance of minimalistic interface because of possibility of further integration of it in more massive projects with some changes to features. All negative remarks were proiritiesed and included in current and following development iterations.

 ### **Testing**
 As was stated before, we estimated the drawbacks in our design by UAT.

 Moreover, our developers of software part of the project conducted manual testing with further correction of errors by themselves. Mostly there were sessions to check communication between frontend and backend parts for correct message passing. Also, backend developers tested the communication with database and correct data representation separately.

 We refined scope of our project and understood that we chose the right vector of project development. The feautures, which should be introduced in given 7 weeks, are agreed with the customer and introduced in the task management system.  We are able to implement all required features in time. So, there is no necessity to narrow the scope of the project.  

 ### **Iteration**
Based on the feedback from the client we enhanced user interface. We designed and added error message in login form.

![Login page](/PipeVision/login_with_error.png "Login"). 

Another change was made in browse file description. Now it includes information about possible file extensions.

![Browse file](/PipeVision/browse_file.png "File browsing").

Also, we redesigned the database and models for it in backend. Now the database is more readable and formalized. During integration of frontend in backend, we made the project more structured to make cooperative development more efficient. For user acceptance testing our team deployed the testing version of project on our own server temporarily. We plan to start utilizing the university servers as soon as possible.  


{{< hint danger >}}
**Feedback**  

**External Feedback**<br>
Very Good!!


**Testing**<br>
You should explain more about the testing you did.
How did you mange bug reporting / fixing / documenting?
Do you have a process for that?

**Iteration**<br>
Good but keep in mind:

An iteration plan is essentially the plan for an upcoming iteration. It would typically outline:
* The goals and objectives for the iteration: what the team aims to achieve.
* The features to be developed.
* The tasks needed to develop these features. This might include coding, testing, design tasks, etc.
* Any assumptions or dependencies.
* A timeline for the iteration.



**Overall**<br>
Report is good. But you need to take extra care for Testing and refining the iteration plan

**Grade: 4/5**


_Feedback by Moofiy_
{{< /hint >}}
