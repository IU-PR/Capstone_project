# EdHub Week 2 Report

<aside>

Capstone Project course

Innopolis University

June 2025

</aside>

# Weekly achievments

## Market Research

After a meeting with TA on June 12, we were recommended to conduct a more detailed market analysis of similar products to identify useful features we want to implement in our project and gaps we want to fill.

We analyzed the 3 popular LMSs (Google Classroom, Moodle, and Stepik) and concluded that none of them are suitable for quick setup and easy use by school teachers. Based on the market, we wrote out the functionality of EdHub and compared it with existing solutions:

- **user-friendly design** (implemented in Google Classroom and Stepik, Moodle is hard to evaluate)
- **easy and quick setup** (implemented in Google Classroom, lacking in Stepik and Moodle)
- **easy customization of criteria for each task** (implemented in Google Classroom and Stepik, lacking in Moodle)
- **completely free functionality** (implemented in Google Classroom and Moodle, lacking in Stepik)
- **parental access** (lacking in Google Classroom, Moodle, and Stepik)
- **flexible customization of the course evaluation formula** (implemented in Moodle and Stepik, lacking in Google Classroom)
- **attendance tracking mechanism** (implemented in Moodle, lacking in Google Classroom and Stepik)
- **global servers** (implemented in in Google Classroom and Stepik, lacking in Moodle)
- **local hosting option** (implemented in Moodle, lacking in Google Classroom and Stepik)

## Acceptance Criteria

In the Week 1 report, we have already described the user stories for the MVP of our project in details, so this week we have focused on defining the acceptance criteria.

### User

- **Given** I'm a new user, **when** I want to create an account and specify the email, name, and password, **then** my account is created in the system.
- **Given** I'm a new user, **when** I want to create an account with email that is already exists, **then** I see an error notice.
- **Given** I'm a new user, **when** I want to create an account with too weak password, **then** I see an error notice.
- **Given** I'm an unauthorized user, **when** I want to log in my account and specify the email and password, **then** I get access to my courses for 30 minutes.
- **Given** I'm an authenticated user, **when** I want to delete my account from the system, **then** my account is deleted from the system with all my assignment submissions, course affiliation and authorship of assignments and materials.
- **Given** I'm an authenticated user, **when** I want to create a course and provide a course title, **then** a new course is created with me as a teacher.

### Teacher

- **Given** I'm a teacher in a course, **when** I enter the course page, **then** I can see all the course materials and assignments.
- **Given** I'm a teacher in a course, **when** I open the material page, **then** I can see the material details.
- **Given** I'm a teacher in a course, **when** I want to invite the student and provide a valid student email, **then** the student gets access to the course.
- **Given** I'm a teacher in a course, **when** I want to invite the teacher and provide a valid teacher email, **then** the teacher gets access to the course.
- **Given** I'm a teacher in a course, **when** I want to invite the student's parent and provide a valid parent email, **then** the parent gets access to observer the student within the course.
- **Given** I'm a teacher in a course, **when** I want to invite the user that does not exists, **then** I see an error notice.
- **Given** I'm a teacher in a course, **when** I want to invite the user that is already part of the course, **then** I see a warning.
- **Given** I'm a teacher in a course, **when** I want to upload/update/remove materials / assignments, **then** changes are immediately visible to all course participants.
- **Given** I'm a teacher in a course, **when** I open the assignment page, **then** I can see the assignment details and the list of students' submissions.
- **Given** I'm a teacher in a course, **when** I grade the student's submission, **then** the student sees this evaluation in their view.
- **Given** I'm a teacher in a course, **when** I want to delete the user from the course and provide a valid user email, **then** the user loses access to the course.
- **Given** I'm a teacher in a course, **when** I want to leave the course and some other teachers remain in the course, **then** I lose access to the course.
- **Given** I'm a teacher in a course, **when** I want to delete the course **then** the course deleted with all its materials, assignments, submissions, students, teachers, parents.
- **Given** I'm a teacher in a course, **when** I want to leave course and some I'm the only teacher left **then** I see a warning.

### Student

- **Given** I'm a student in a course, **when** I enter the course page, **then** I can see all the course materials and assignments.
- **Given** I'm a student in a course, **when** I open the material page, **then** I can see the material details.
- **Given** I'm a student in a course, **when** I open the assignment page, **then** I can see the assignment details and the status of my submission.
- **Given** I'm a student in a course, **when** I want to submit the assignment and specify the submission text, **then** assignment is submitted and teacher can evaluate it.
- **Given** I'm a student in a course with a submitted assignment, **when** the teacher evaluates my submission, **then** I can see my grade and the email of teacher that graded my submission.
- **Given** I'm a student in a course, **when** I want to leave the course, **then** I lose access to the course.

### Parent

- **Given** I'm a parent in a course, **when** I enter the course page, **then** I can see all the course materials and assignments.
- **Given** I'm a parent in a course, **when** I open the material page, **then** I can see the material details.
- **Given** I'm a parent in a course, **when** I open the assignment page, **then** I can see the assignment details and the status of my childrens' submission.
- **Given** I'm a student in a course, **when** I want to leave the course, **then** I lose access to the course.

## Plans & Prioritized backlog

We decided to split our project into several versions, each of which has full self-sufficient functionality. With each version new features are added to the project.

- **Materials**: Teacher can create courses, invite students, parents, or teachers, create materials. Student can enter the course and view the list of available materials. Parent can enter the course and view the list of available materials.
- **Assignment**: Teacher can create assignments, see the list of students' submissions and grade them. Student can submit assignments. Parents can track their students' submissions.
- **Files**: Teacher can attach files up to 5MB to course materials and assignments. Student can attach files up to 5MB to their submissions.

By the end of Week 3, we plan to have an MVP of our product, and the global plan for the week is the following:

| Project Version | Backend | Frontend |
| --- | --- | --- |
| **Materials** | :ballot_box_with_check: Done in Week 1 | :white_check_mark: Done in Week 2 |
| **Assignment** | :white_check_mark: Done in Week 2 | :black_square_button: Planned for Week 3 |
| **Files** | :black_square_button: Planned for Week 3 | :black_square_button: Planned for Week 3 or Week 4 |

During the development process we sometimes change the vision of our product, so we plan to focus on a more detailed backlog and work out the week's plan at the beginning of each week. The backlog for Week 2 [was developed](https://github.com/orgs/IU-Capstone-Project-2025/projects/14/views/1) on June 12. The backlog for Week 3 will be extended after the meeting with TA and discussing the project.

## Backend

The main task of the backend team this week was to work on the API commands to implement the **assignments and grades feature**. A teacher can now create assignments within a course and add a title and description to them. Students can attach their text responses to assignments and submit them to the teacher for review. The teacher can track student submissions and grade them. Parents of students can also track their children's submissions.

We also found that there is no way for a user to **delete their account** on the site. We consider the user's right to delete their account and all data about themselves from the service to be a priority, so we have implemented such an option.

During the review of the account deletion function pull request, we came up with the idea of not deleting all user-related data directly using sql queries, but rather **writing `on delete` functions** into the database initialization script. This way PostrgreSQL will automatically process user data when deleting a user from the `users` table. We also decided to apply this solution to improve the `remove_course` function, which previously had to delete all students, materials, and other related data manually.

We also need to check the correctness of the input data before handling the request. For example, when we receive a request to add a student to a course, we call: 

1. a function to check that the course exists
2. a function to check that the invited user exists
3. a function to check that the user is not already a member of that course
4. a function to check that the sender of the request has teacher privileges

This week we realized that some of these checks overlap and **removed redundant checks** to optimize request handling. For example, we don't need to call the check 2, because this check is implemented within the check 3, which also validates the input parameters.

## Frontend

During Week 2, the frontend team focused on implementing the Materials version of the product — the foundation for our MVP and the teacher interface.

The following features have been completed:

- **Registration page**: Users can register with email, name, and password. Upon successful registration, they receive a JWT token and are redirected to their dashboard.
- **Login page**: Users can log into their account using email and password. The design supports a responsive layout and a visual switch between login and registration modes.
- **Course list page** (teacher view): Displays a list of all teacher’s courses as cards with metadata: title, creation date, and number of students.
- **Course creation page**: Teachers can create a new course by providing a title. The course is immediately added to their list.
- **Layout and routing**: A responsive sidebar navigation is implemented, highlighting the active page. This allows clear and convenient navigation between “My Courses” and “Create Course”.
- **API integration**: All implemented pages use JWT-based authentication. Protected routes attach the token automatically, and user sessions are handled through localStorage.

All implemented functionality is connected to the backend via protected API calls and uses real-time responses from the server. The UI is built with Tailwind CSS and shadcn/ui for styling and layout consistency across components.

At this stage, the frontend is focused on the teacher interface, since most critical operations — such as course creation and participant management — are performed by teachers.

## DevOps

After the TA's recommendation, we fixed the network settings in the `docker-compose.yml` file that previously specified a concrete address.

We also decided to redesign the architecture of the project to break one big `main.py` file into several parts with `logic/`, `models/` and `routers/`. This way the project will be more scalable and it will be easier to work on several functions in parallel.

## Plan for the Week 3

During the Week 3, we plan to fully finalize the MVP of our project: the frontend team will create pages for assignments with their descriptions and the ability to submit students' work. The backend team will work on the ability to attach files to materials and assignments. If the frontend team has time left, they will also develop a frontend for uploading files.

# Individual contribution

### Gleb Popov
- [`backend`]: Backend part of the **Assignment** feature has been developed ([*PR #21*](https://github.com/IU-Capstone-Project-2025/edhub/pull/21));
- [`backend`]: The feature of proper deletion of user account and all their data from the system has been developed ([*PR #22*](https://github.com/IU-Capstone-Project-2025/edhub/pull/22));
- [`management`]: A more detailed market research was carried out after the recommendation of TA;
- [`management`]: Development plan and weekly backlog have been created ([*kanban board*](https://github.com/orgs/IU-Capstone-Project-2025/projects/14/views/1));
- [`management`]: Weekly report has been written ([*PR #493*](https://github.com/IU-PR/Capstone_project/pull/493)).

### Timur Usmanov
- [`backend`]: Docker network bug has been fixed after the recommendation of TA ([*PR #6*](https://github.com/IU-Capstone-Project-2025/edhub/pull/6));
- [`backend`]: The correctness of input arguments of constraint checking functions is now validated ([*PR #23*](https://github.com/IU-Capstone-Project-2025/edhub/pull/23));
- [`backend`]: Careful reviewing of pull request has been conducted ([*PR #21*](https://github.com/IU-Capstone-Project-2025/edhub/pull/21), [*PR #22*](https://github.com/IU-Capstone-Project-2025/edhub/pull/22)).

### Askar Dinikeev
- [`devops`]: Project architecture has been developed, methods have been refactored into new modules ([*PR #25*](https://github.com/IU-Capstone-Project-2025/edhub/pull/30)).

### Alina Suhoverkova
- [`frontend`]: Base structure and main pages have been added, initial routing, login/register pages, and main course page are ready. Basic layout and styles have been added ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/4c02ddb8b12b8a2102bd5b501cf75ac893bd6515));
- [`frontend`]: Project design and style have been createad on [*Figma*](https://www.figma.com/design/dZsl8QQ8ZdJAXhzhCROajk/EdHub?node-id=0-1&p=f&t=yK7vWguu6P4d9RM8-0).

### Timur Struchkov
- [`frontend`]: Course creation page have been modified to include more details, pages for addition of students, materials, and parents have been added, routing for the new pages have been modified ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/d9ddb70a4330eefb9d6759a92db9583072f1b9e1));
- [`frontend`]: Pages for materials and member addition to courses have beed designed in [*Figma*](https://www.figma.com/design/dZsl8QQ8ZdJAXhzhCROajk/EdHub?node-id=0-1&p=f&t=yK7vWguu6P4d9RM8-0).

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition.
- Is runnable via `docker compose`.