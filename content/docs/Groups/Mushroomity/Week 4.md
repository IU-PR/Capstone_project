# Week 4 #

## External Feedback ##

We have found testers from the Russian community who are ready to start using our application and provide feedback. We
hope that they will be of great assistance, especially since some of them are experts in mycology. Unfortunately, our
prototype is not yet complete, but we are working diligently to finish it as quickly as possible so that we can provide
the application to our testers next week.

---

## Testing ##

In general, we did not dedicate a significant amount of time to testing the app due to a lack of available resources.
Here are some details regarding this matter.

### Flutter ###

This week, we only connected the linter for the project. Our plan for next week is to include automated tests for the
project, focusing on the app's core functionality while our friends use the prototype.

### ML ###

This week, our focus was on creating the dataset. Therefore, we did not spend much time considering how to test our AI
model.

---

## Iteration ##

As you may recall, this week can be considered as the first iteration of our project.

### Design ###

We made some minor changes to the design (refer to the week 3 report). There are changes in colors only.

### Flutter ###

We focused on the main functionality of the application. One team member worked on integrating the model and deploying
the server, while another teammate worked on creating the main page of the application with the "Upload photo"
functionality. Since we aim to provide the prototype to our testers as soon as possible, we are dedicating a significant
amount of time to implementing the main functions and creating the server for storing photos and adding users.

### Data ###

We finished the dataset, which now contains around 40,000 photos of mushrooms (with no augmentation) of 400 types of the
most popular mushrooms in Russia. Here's
a [link](https://drive.google.com/drive/folders/11xssHFrwALQwNvw5jEcmnGDOt6MaOKWW) to a part of the dataset you can see
right now.

### Model ###

For analyzing photos, we used [Xception](https://keras.io/api/applications/xception/) and added our own layers. This
model will be used in the prototype, and next week we will enhance the model to request additional information (not from
the photo) for better determination.



{{< hint danger >}}
### Dear Mushroomity, I already graded you last week, but it seems like that something wrong happened with the push

**Feedback** 

**External Feedback**<br>
So you don't have feedback.
It's week 4, and your prototype is not ready yet? Why?
It's super easy to create a prototype and get feedback from it.
A lot of students have already done that.

**Testing**<br>
Okay, setting up a linter is good, but this is not testing.

A linter checks your code for potential issues and style consistency without executing it, while testing involves executing your code and verifying that it works as expected under different conditions.

Besides, any Flutter project comes with a built-in linter. So basically, you did nothing?

**Iteration**<br>
Okay, it's good that you are thinking of the iteration. Also, keep in mind:

An iteration plan is essentially the plan for an upcoming iteration. It would typically outline:
* The goals and objectives for the iteration: what the team aims to achieve.
* The features to be developed.
* The tasks needed to develop these features. This might include coding, testing, design tasks, etc.
* Any assumptions or dependencies.
* A timeline for the iteration.

**Overall**<br>
The report is weak. It's clear that you haven't made much progress. If you don't have a prototype and didn’t started development. You are approaching week 6. At this pace, you might fail the course.

Please pay attention to the development and progress of your project.

**Grade: 2/5**

_Feedback by Moofiy_
{{< /hint >}}