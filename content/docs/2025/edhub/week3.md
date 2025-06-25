# EdHub Week 3 Report

<aside>

Capstone Project course

Innopolis University

June 2025

</aside>

# MVP

## Development Process

Last week we decided to split our project into several versions, each of which has full self-sufficient functionality. With each version new features are added to the project.

- **Materials**: Teacher can create courses, invite students, parents, or teachers, create materials. Student can enter the course and view the list of available materials. Parent can enter the course and view the list of available materials.
- **Assignment**: Teacher can create assignments, see the list of students' submissions and grade them. Student can submit assignments. Parents can track their students' submissions.
- **Files**: Teacher can attach files up to 5MB to course materials and assignments. Student can attach files up to 5MB to their submissions.

The global plan is the following:

| Project Version | Backend                                       | Frontend                                           |
| --------------- | --------------------------------------------- | -------------------------------------------------- |
| **Materials**   | :ballot_box_with_check: Done in Week 1        | :ballot_box_with_check: Done in Week 2             |
| **Assignment**  | :ballot_box_with_check: Done in Week 2        | :white_check_mark: Done in Week 3                  |
| **Files**       | :black_square_button: Rescheduled for Week 4  | :black_square_button: Planned for Week 4           |

Our MVP implements the **Assignment** version of EdHub. 

## Demonstation Video

Demo Video is available via the [*link*](https://youtu.be/CRFHnUxSeHU).

# Weekly achievments

## Management

Last week we conducted a market research to explore the existing LMS solutions, and for each platform we identified the pros that we want to implement in EdHub and the cons that we want to cover. However, our view is an outsider's view, and no one can provide us with real experience of using the platforms with students in a real educational process. We decided to launch a survey among teachers to find out what existing LMSs they use, what they like and dislike about these systems, what is important to them and what they would like to fix.

We plan to send this survey to our high school teachers as well as university professors and TAs in hopes of getting more responses through the word of mouth effect. We hope the real-life experiences of teachers will help us shape a set of features that are important in a real educational process.

## Backend

The main task of the backend team this week was to explore the possibility of attaching files to course materials, course assignments, and students' submissions. After we have explored how to implement this, we realized that this task is more complex than we expected. To implement attachments feature, we need to think about the format for storing files, which would be better implemented in a separate database, think about the validation of files (size and type restrictions), and develop functions to send a file to the server and to retrieve a file from the server. We realized that we don't have time to do this task in full by the end of the third week, so we started it and plan to finish until the end of the 4th week.

The main task of the backend team this week was to explore the possibility of attaching files to course materials, course assignments, and students' submissions. After we have explored how to implement this, we realized that this task is more complex than we expected. To implement attachments feature, we need to think about the format for storing files, which would be better implemented in a separate database, think about the validation of files (size and type restrictions), and develop functions to send a file to the server and to retrieve a file from the server. We realized that we don't have time to do this task in full by the end of the third week, so we started it and plan to finish until the end of the 4th week.

Until this week, when registering for an account, users could type any strings into the email and password fields. We decided to add email format check and password complexity check to protect user accounts from hacking. Password must be longer than 8 characters and contain letters, numbers and special characters.

Previously, the teacher had full rights to invite and remove users on the course. In particular with the `remove_teacher` command they could remove any teacher on the course, including themselves (so the teacher could leave the course). This feature was not previously available for students and parents, so we improved the `remove_student` and `remote_parent` commands to allow parents and students to remove themselves from the course if they wanted to.

We also decided to improve the syntax of the script for creating the database by adding clearer formatting, prescribing string length limits, and specifying NULLABLE objects.

We added a logging feature to the backend that logs all actions that teachers and LMS administrators may be interested in, e.g., creating or deleting a course, adding a student/parent/teacher to a course. Logs are stored in a separate database table named "logs" in the PostgreSQL database.

## Frontend

<!-- Алина + Тимур -->

## DevOps

We have added an nginx reverse proxy for our project that allows to host both the API endpoints and the frontend server under one domain name. We put the API endpoints under the `/api/` path.

## Plan for the Week 4

During week 4, we plan to continue developing our project as follows:
- the backend team plans to finalize the feature of attaching files to course objects, and to develop tests for automatic code checking (CI/CD);
- the frontend team plans to fix some bugs in the current version, improve performance and develop a landing page;
- the devops team plans to run EdHub on a permanent server.

# Individual contribution

### Gleb Popov
- [`management`]: A survey on LMS use among teachers have been created and launched ([*Google Forms*](https://docs.google.com/forms/d/e/1FAIpQLSdGK2YzXT6FeVMh_rijGg2B2ln3wn6vbr1_aDDqQ53i8DtPuw/viewform?usp=sharing&ouid=112650036002060911245));
- [`backend`]: Sketches of functions for attaching files to course objects have been developed in the [*attachments*](https://github.com/IU-Capstone-Project-2025/edhub/tree/attachments) branch;
- [`backend`]: Validation of email format and password complexity has been developed ([*PR #46*](https://github.com/IU-Capstone-Project-2025/edhub/pull/46));
- [`backend`]: An option to exit the course has been added to `remove_student` and `remove_parent` functions ([*PR #45*](https://github.com/IU-Capstone-Project-2025/edhub/pull/45));
- [`backend`]: Careful review of pull request has been conducted ([*PR #48*](https://github.com/IU-Capstone-Project-2025/edhub/pull/48), [*PR #49*](https://github.com/IU-Capstone-Project-2025/edhub/pull/49), [*PR #50*](https://github.com/IU-Capstone-Project-2025/edhub/pull/50));
- [`management`]: Weekly report has been written ([*PR #493*](https://github.com/IU-PR/Capstone_project/pull/493)).

### Timur Usmanov
- [`backend`]: work on ORM implementation has begun in the [`oop_overhaul`](https://github.com/IU-Capstone-Project-2025/edhub/tree/oop_overhaul) branch;
- [`backend`]: database creation script has been improved ([*PR #50*](https://github.com/IU-Capstone-Project-2025/edhub/pull/50));
- [`devops`]: nginx reverse proxy has been installed ([*PR #48*](https://github.com/IU-Capstone-Project-2025/edhub/pull/48));
- [`backend`]: Careful review of pull request has been conducted ([*PR #45*](https://github.com/IU-Capstone-Project-2025/edhub/pull/45), [*PR #46*](https://github.com/IU-Capstone-Project-2025/edhub/pull/46), [*PR #49*](https://github.com/IU-Capstone-Project-2025/edhub/pull/49)).

### Askar Dinikeev
- [`backend`]: LMS logging has been developed ([*PR #49*](https://github.com/IU-Capstone-Project-2025/edhub/pull/49)).

### Alina Suhoverkova
- [`frontend`]: 

### Timur Struchkov
- [`frontend`]: 
- [`frontend`]: Careful review of pull request has been conducted ([*PR #48*](https://github.com/IU-Capstone-Project-2025/edhub/pull/48)).

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.