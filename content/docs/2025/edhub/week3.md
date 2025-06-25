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

| Project Version | Backend                                    | Frontend                                           |
| --------------- | ------------------------------------------ | -------------------------------------------------- |
| **Materials**   | :ballot_box_with_check: Done in Week 1     | :ballot_box_with_check: Done in Week 2             |
| **Assignment**  | :ballot_box_with_check: Done in Week 2     | :white_check_mark: Done in Week 3                  |
| **Files**       | :white_check_mark: Rescheduled for Week 4  | :black_square_button: Planned for Week 4           |

Our MVP implements the **Assignment** version of EdHub. 

## Demonstation Video

<!-- Discuss with Timur 
- записать демо видео
- перечислить список функционала
-  -->

# Weekly achievments

## Management

Last week we conducted a market research to explore the existing LMS solutions, and for each platform we identified the pros that we want to implement in EdHub and the cons that we want to cover. However, our view is an outsider's view, and no one can provide us with real experience of using the platforms with students in a real educational process. We decided to launch a survey among teachers to find out what existing LMSs they use, what they like and dislike about these systems, what is important to them and what they would like to fix.

We plan to send this survey to our high school teachers as well as university professors and TAs in hopes of getting more responses through the word of mouth effect. We hope the real-life experiences of teachers will help us shape a set of features that are important in a real educational process.

## Backend

The main task of the backend team this week was to explore the possibility of attaching files to course materials, course assignments, and students' submits. After we have explored how to implement this, we realized that this task is more complex than we expected. To implement attachments feature, we need to think about the format for storing files, which would be better implemented in a separate database, think about the validation of files (size and type restrictions), and develop functions to send a file to the server and to retrieve a file from the server. We realized that we don't have time to do this task in full by the end of the third week, so we started it and plan to finish until the end of the 4th week.

Until this week, when registering for an account, users could type any strings into the email and password fields. We decided to add email format check and password complexity check to protect user accounts from hacking. Password must be longer than 8 characters and contain letters, numbers and special characters.

We also decided to improve the syntax of the script for creating the database by adding clearer formatting, prescribing string length limits, and specifying NULLABLE objects.

<!-- логи -->

## Frontend

<!-- Алина + Тимур -->

## DevOps

<!-- добавлен nginx -->

## Plan for the Week 3

<!-- планы для week3 -->

# Individual contribution

### Gleb Popov
- [`management`]: a survey on LMS use among teachers have been created and launched ([*Google Forms*](https://docs.google.com/forms/d/e/1FAIpQLSdGK2YzXT6FeVMh_rijGg2B2ln3wn6vbr1_aDDqQ53i8DtPuw/viewform?usp=sharing&ouid=112650036002060911245));
- [`backend`]: sketches of functions for attaching files to course objects have been developed in the [*attachments*](https://github.com/IU-Capstone-Project-2025/edhub/tree/attachments) branch;
- [`backend`]: validation of email format and password complexity has been developed ([*PR*](https://github.com/IU-Capstone-Project-2025/edhub/pull/46)).

### Timur Usmanov
- [`backend`]: database creation script has been improved ([*PR*](https://github.com/IU-Capstone-Project-2025/edhub/pull/50));
- [`devops`]: nginx reverse proxy has been installed ([*PR*](https://github.com/IU-Capstone-Project-2025/edhub/pull/48)).

### Askar Dinikeev
- [`backend`]: LMS logging has been developed ([*PR*](pull request)).

### Alina Suhoverkova
- [`frontend`]: 

### Timur Struchkov
- [`frontend`]: 

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition.
- Is runnable via `docker compose`.