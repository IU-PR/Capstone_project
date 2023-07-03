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
