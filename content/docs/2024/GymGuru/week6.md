---
title: "Week #6"
---

# <p style="text-align: center;">**Capstone Project**</p>

# <p style="text-align: center;">*Team GymGuru*</p>

## **Week 6 - Project Completion and Final Presentation**


## **Week's focus and importance**

&nbsp;&nbsp;&nbsp;&nbsp;This week is one of the most important since now we need to finalize the work on MVP of GymGuru web application and present it. The main focuses of this week are:

1. Complete all parts of the project, fix several bugs in UI and fitness test functionality;

2. Create a final presentation of GymGuru project that shows all important aspects of our web application (problems we tried to solve, main functionality of the project, team members impact to the obtained solution, and so on).


## **Feedback from TA**

&nbsp;&nbsp;&nbsp;&nbsp;During the meeting with TA on the previous week we discusted our Week 5 report and final presentation of the project. This is a list of main points that we received from the feedback:

1. About the report - everything is correct;

2. About the presentation - he gave an advice to add a slide with exploting existing solutions in this or nearest fields, and also to fix one slide by changing roadmap dimension (to increase a visibility and readability of that slide).


## **Week's progress**

&nbsp;&nbsp;&nbsp;&nbsp;During this week we have accomplished the following features:

- we completed the functionality for downloading the file with the results of the fitness test;
- we redone the "tilt" exercise using MediaPipe, due to the inaccuracy of recognition using MoveNet;
- fixed the score counter in the fitness test;
- written several tests and tested our app;
- corrected inaccuracies in recognition when a user`s body is not completely in the frame;
- added an indication of the field in the profile;
- fixed v-up crunches in the mobile version in the rating displaying;
- added the description of how a person should be positioned in the frame before each exercise;
- added a rating with a drop-down list.


## **Project Conclusion**

&nbsp;&nbsp;&nbsp;&nbsp;In conclusion, we have created an application that is able to accurately recognize the position of a user`s body and determine the correctness of the exercise, as well as report on necessary adjustments by voice assistant. Moreover, we have added functionality for conducting a fitness test, which will free up both students and coaches and allow them to take the test anytime and anywhere. You can also track your rating in the app and see your position among other users. The resulting application completely coincided with our expectations, we did absolutely everything that we planned and even more.

&nbsp;&nbsp;&nbsp;&nbsp;We want to emphasise that all components of this project architecture diagram are completed:

<img src="/2024/GymGuru/Week6_Architecture.jpg" width="720" height="940">

&nbsp;&nbsp;&nbsp;&nbsp;Except the database configuration. After the development of all parts we defined that initial database configuration should be changed into 3 tables connected by user_id field:

<img src="/2024/GymGuru/Week6_Database.jpeg" width="720" height="350">


## **Challenges & Solutions**

&nbsp;&nbsp;&nbsp;&nbsp;This week we had a number of difficulties:

1. We found some minor bugs with inaccurate scoring and UI. These bugs were found due to collected feedback and thorough testing of a system, and promptly fixed.

2. There was a problem to succinctly describe a large amount of information for the entire project in the final presentation. We defined only the main points and include it into the slides, and we will accompany it by supportive information regarding different aspects.


## **Conclusions & Next Steps**

&nbsp;&nbsp;&nbsp;&nbsp;This week we finished fixing the latest bugs in our product, completed everything we wanted and made the final presentation. Next, we plan to:

1. Prepare for the presentation of the project;

2. Discuss the possible future development of the project.
