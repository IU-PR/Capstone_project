---
title: "Week #4"
---

# <p style="text-align: center;">**Capstone Project**</p>

# <p style="text-align: center;">*Team GymGuru*</p>

## **Week 4 - External Feedback, testing and Iteration**


## **Week's focus and importance**

&nbsp;&nbsp;&nbsp;&nbsp;This week, we have been focusing on testing and incorporating feedback, which is important because we need to see independent reviews from third parties in order to identify any potential issues and plan our next steps. To do this, we have gone through several stages.
&nbsp;&nbsp;&nbsp;&nbsp;Our plan was to conduct continuous integration/continuous delivery (CI/CD) testing, user interface (UI) testing, and user acceptance testing (UAT) to gather user feedback. We also continued integrating our initial ideas for the project that we didn't have time to finish last week.



## **Feedback from TA**

&nbsp;&nbsp;&nbsp;&nbsp;

1. 

2. 

3. 


## **External Feedback**

&nbsp;&nbsp;&nbsp;&nbsp;We have conducted a survey among the students of our university and have collected feedback on our product. We let interviewees to use GymGuru and asked them to evaluate the aesthetic component of the app, usability and usefulness of the idea itself on a 10-point scale, and also asked what they liked and what they didn't.

|Student|Aesthetic|Usability|Usefulness|Like|Dislike|
|---|---|---|---|---|---|
|Azaliya Alisheva, 1st year|10|5|10|Page with exercises, the ability to take the exercise from any angle, minimalistic design|You need to turn your head to see the result|
|Nazgul Salikhova, 2nd year|5|5|10|The idea of taking the test online|I want to see more “sporty” design, some photos on the pages. It will be nice to have a system of some prizes for progress|
|Iskander Nafikov, 4th year|7|7|8|It is convenient to take a test from another city|No way to cheat|
|Vagif Khalilov, 4th year|7|6|7|It is cool to take a test remotely|As for me ML algorithms are not accurate|
|Artem Murashko, 4th year|7|9|9|The demonstration is great|The design is outdated|
|Eduard Zaripov, 4th year|7|7|10|I like the idea of renting from another city|It would be convenient to see the hints in the UI|
|Vsevolod Klushev, 4th year|10|8|2|The design is nice|It is not clear whether the registration was completed, whether the password was entered correctly - we need prompting labels|
|Matvey Korinenko, 2nd year|9|7|6|It's very cool that it really recognizes exercises, and quite accurately|Immediately after registering and logging in, there was a blank page|
|Dmitry Okoneshnikov, 2nd year|8|4|2|I really like the idea of using a pose|It is worth adding an inscription that the download /initialization is in progress|
|Overall|7.8|6.4|7.1|Most of interviewees highlighted the design and the main idea|Respondents noted that they want to see more hints and alerts of success/fail|


## **Testing**

&nbsp;&nbsp;&nbsp;&nbsp;Through the whole development process we conducted and will conduct thorough testing to find any bugs and/or parts that work in different way we planned. For the UI aspect this testing is a "manual hand-testing" that allow to explore all parts of web application according to user flow diagram (presented in Week 2 Report).

&nbsp;&nbsp;&nbsp;&nbsp;During this week, our team set up a CI/CD pipeline in GitHub by using GitHub actions and creating our own GitHub runner on the application server. This will allow us to conduct different tests automatically after each push to the main branch, and also to automate the deployment process.

&nbsp;&nbsp;&nbsp;&nbsp;The list of things that we can test with CI/CD includes:

- User flow (to which page the user will go after some action)

- Sending the correct POST request with user data

- Receiving the correct html from the current web pages

- Correctness of the registration form validation (for example, password with not less that 6 symbols)

- Connection to the Database

&nbsp;&nbsp;&nbsp;&nbsp;Moreover, regarding the recognition of the physical exercise performance correctness, we trying to find any ways how to cheat the system. This allow us to refine the rules of checking the correctness of exercise done by a person. It includes different camera angles, clothes, backgrounds and so on.


## **Iteration**

&nbsp;&nbsp;&nbsp;&nbsp;During the whole working process, our team adhere an iterative strategy of software development. After each iteration (each week for this project) we conduct a testing and feedback sessions (for the team members and external users from this week). On the base of collected feedback and development plan we define the aspects of a project that should be invented/expanded/fixed.

&nbsp;&nbsp;&nbsp;&nbsp;For this week, according to the iterative development process strategy, we determined the following plan of work:

1. Refine a main page

2. Edit a headers of web site

3. Expand a number of supported physical exercises

4. Set up a CI/CD using GitHub actions

5. Add a rating functionality

&nbsp;&nbsp;&nbsp;&nbsp;As can be seen from the tasks listed above, all of them are refinement or expanding a base of web application, representing this week's iteration.


## **Challenges & Solutions**

&nbsp;&nbsp;&nbsp;&nbsp;This week we had a number of difficulties, mainly consisting of testing:

1. When testing the correctness of counting the number of completed approaches of one exercise. For each exercise, it is necessary to think through all possible tricks that will help to wind up the counter, and because of this, the testing person spent days squatting, doing push-ups, and so on. Also, new tricks are being invented every day, also thanks to the feedback of users.

2. During the CI/CD testing, we encountered some difficulties due to a lack of experience in implementing this feature on the GitHub platform. Specifically, there was an issue with the runner not being installed not with user, nor with root permission on our rented server. We solved it by setting up several environment variables.


## **Conclusions & Next Steps**

&nbsp;&nbsp;&nbsp;&nbsp;This week we are done with feedback, manual and automated testing, and several features and refinements of the web application itself. And this is a list of our expected next steps:

1. Continue searching for tricks in calculating exercise approaches and correcting them;

2. Continue collecting, analyzing and implementing user and experts feedbaсk;

3. Implementing fitness test functionality.
