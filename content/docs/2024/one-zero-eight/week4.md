---
title: "Week #4"
---

# Week 4 - External Feedback

### **External Feedback**

To collect feedback on our product, we deployed current version of website and backend to our staging servers, so that
users could access it without problems.

During User Acceptance Testing, we interviewed a group of students to gather feedback on our software. Based on their
feedback, certain features require refinement and revision to enhance usability. For example, the website’s search
functionality across university information resources could be modified to improve usability, given the large variety of
sources and files. In particular, adding filters for information sources to choose between Moodle, Telegram, etc.,
adding filters for courses to select only relevant study materials.

At the same time, the browser extension designed for easier navigation of courses in Moodle received extremely positive
feedback. This is once again confirms that the product aligns with user needs and that it is ready for deployment.
However, it could be enhanced by introducing modern design, and adding more useful features related to university
services.

### **Testing**

Our team tested multiple different scenarios of search queries manually to obtain the correctness of resulting output
documents. Moreover, we are in the process of gathering queries validation set to be able to cross-validate search
parameters and enhance pipeline. We also monitor the API speed and the status of our servers.

### **Iteration**

**Continuous iteration** is the backbone of successful project development. It involves a constant cycle of evaluation,
adjustment, and refinement based on feedback and testing results

In the development of our search system for the InnoHassle service, we have adhered to a rigorous iterative process from
the outset. Our multidisciplinary team, comprising backend developers, frontend developers, and machine learning
specialists, has worked collaboratively to ensure continuous assessment and enhancement of our project.

As example, we identified the need to split our search system into two distinct components: a simple search for relevant
responses and a query to a model trained on our dataset to provide answers, accompanied by relevant sources. This
decision necessitated partial overhauls of all services

Moreover, our team members responsible for ML part frequently brainstorms new ideas and methods to enhance the model
training process. This ongoing dialogue and experimentation ensure that our model will be the most appropriate and best
one

In the near future, we plan to offer our service to students for testing. This will allow us to identify any remaining
issues and take necessary measures to further improve the product

Through these iterative steps, we have not only aligned our progress with the project's initial vision but have also
been able to refine our system significantly. This process has allowed us to eliminate early-stage mistakes and
continuously enhance the service's quality and performance

## **Weekly Progress Report**

Throughout this week, we continued our work on the project, making significant progress and achieving several successes.

**Team Communication:**

Our team continues to actively communicate and assist each other with assigned tasks. After our meeting with the TA on
Wednesday, we held a mini team meeting where we summarized and updated tasks for the week and scheduled individual
meetings to address specific tasks.

**Moodle Browser Extension:**

The Moodle extension has been refined and adapted for the Firefox browser. Now, anyone can download the extension from
the official stores, Chrome Web Store and Mozilla Addons. Our team has tested this functionality and is actively using
the extension while simultaneously searching for bugs (if any).

**Frontend Development:**

Significant work has been done to improve the user design for search usage. The design of slides and the structure of
source/title display have been updated.

**Telegram Bot:**

A README.md has been written with detailed instructions on how to launch the bot. Work has been done to finalize the
deployment of the bot on the server using best practices. Work continues on the method of uploading data to the server
using FastAPI and MongoDB.

**DevOps:**

MinIO database was deployed for storing large volumes of information. CI has been configured for each repository of our
project's components, and a staging environment has been deployed on the server to test the functionality and
interaction of the frontend and backend by different team members.

**Backend:**

Significant work has been done on the project's backend:

- Improved the file upload method to allow multiple file uploads and clean up existing files.
- Redesigned the search schema to respond to user queries, which will enhance user interaction with generated responses.
- File metadata is uploaded to MongoDB, while the files themselves are stored in MinIO. Data search by file metadata has
  been implemented.