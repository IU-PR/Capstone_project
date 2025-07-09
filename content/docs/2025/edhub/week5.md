# EdHub Week 5 Report

<aside>

Capstone Project course

Innopolis University

July 2025

</aside>

# Usability testing sessions

This week we conducted several usability testing sessions to collect feedback about using EdHub from external people, detect bugs, and find out the features for future development.

## Sessions

All users with whom we discussed our project mostly noticed the minuses of our project and gave suggestions for its improvement, which was quite useful for us.

#### Session 1 
<!-- Рия -->
- there is no option to delete materials / assignments within the course
- nothing happens when the user clicks on the logo in the upper left corner of the page
- there is no option to log out from the account
- after the creation of course / material / assignment, the user has to refresh the page manually

#### Session 2
<!-- Дамир -->
- default browser pop-up windows look ugly
- the option to see a list of students in a course will be useful
- it is possible that one users will be both a teacher and a parent at one course while the platform does not allow that
- after the creation of course / material / assignment, the user has to refresh the page manually

#### Session 3 
<!-- Глеб -->
- when entering the auth page, an authorized user is prompted to re-enter login and password, although the token has already been provided
- two separate columns for course materials and course assignments looks ugly
- after the creation of course / material / assignment, the user has to refresh the page manually

#### Session 4 
<!-- Маша -->
- when registering an account, the system writes that the password is too easy, and the criteria are not clear
- in the Add Course button, the second word wraps to the next line, which disrupts the layout
- the field for material/assignment description can be stretched beyond the pop-up window frame
- after the creation of course / material / assignment, the user has to refresh the page manually
- if user enter line break characters in the material / assignment description, then on the material / assignment page they disappear and become a single line
- when inviting a student, submitting the form with the Enter key does not work

## Analysis

The meetings with independent users were very useful for our project. Although most of the issues they reported were already known to us and being worked on, we discovered a few new issues that we had not noticed before and plan to fix them in near future.

### Frontend

<!-- создать issues по итогам фидбека -->

- [x] develop an option to log out from the account
- [x] add automatic refresh when the course / material / assignment is created
- [x] clarify the criteria for evaluating password complexity
- [ ] add an option to delete materials / assignments within the course
- [ ] add a redirect to the main page when clicking on the logo
- [ ] replace default browser pop-up windows with the designed ones
- [ ] add the page with the list of students enrolled in the course
- [ ] add a redirect to the main page when an authorized user accesses the auth page
- [ ] add two separate columns for course materials and course assignments
- [ ] fix the "Add Course" button so that all words will be on the same line
- [ ] fix the field for material/assignment description so that it can be stretched only vertically
- [ ] add an option to submit the inviting user form (and other forms) by pushing an Enter key

### Backend

- [ ] add an option to delete materials / assignments within the course
- [ ] think about how user can be both a teacher and a parent at one course

# Iteration & Refinement

### Implemented features based on feedback

Since we already had our work plans lined up for the week 5, this week we mostly dealt with them. However, as described above, some of the feedback overlapped with this week's plans, so a few features were developed:
- an option to log out from the account has been developed
- an automatic refresh when the course / material / assignment is created has been developed
- the criteria for evaluating password complexity have been clarified

### Performance & Stability

To measure how stable and performant our web service is, we propose the following:

- Set up a program on our staging server to randomly `curl` our production server and count how many times the request has failed or succeeded.
- Make a script that would stress-test the staging version of the service and measure the number of requests per second it can handle.

We were unable to implement these ideas this week but plan to do so next week.


### Documentation

For the backend part we use the Swagger documentation generated automatically by FastAPI. Such documentation provides a convenient interface for the frontend team to describe the meaning of the function and input parameters and is used universally in many projects with APIs.

For the frontend part, we use the auto-generated README.md from Create React App, supplemented with inline JSDoc comments for key components. This documentation provides essential setup instructions, script explanations, and component-level details, ensuring smooth onboarding and maintenance while following React’s standardized conventions.

# Weekly achievements

## Management

On Saturday, July 5, we held a meeting with administrators of the Sberclass platform in a Moscow school. As the platform is in beta testing, access to it is limited, but at this meeting we had a unique opportunity to see the platform's interface from the administrator and teacher's side, as well as get feedback on its usability from a real teacher. This meeting was extremely useful for our team, as it helped us compile a list of features to implement in the near future.

## Backend

At the beginning of week 5, the backend team separated the files into a separate database and a separate Docker container. This will allow to run the database container on a separate disk in the future to physically separate the files from the service information.

The main task for the backend team for this week was to develop the concept of admin account. Administrator is able to:

- give admin rights to any user
- see the list of existing users
- delete the any of existing users
- access any course and edit all the course data
- invite users to courses and remove users from courses
- access and edit any course material / assignment / submission

When the system is started, a default admin account is created with the following parameters:

```
user: admin
name: admin
password: *generated randomly and printed to console*
```

After that, the system administrator can continue to use the current account (insecure) or create his personal account with correct data, give himself admin access from the default account and then delete the default user.

Also, this week we developed an option to export all the course grades to a csv file. Now teacher can export grades of all students in the course, parent can export grades of all their children, and student can export their grades.

## Frontend

The frontend team focused on improving error handling, design consistency, and interactive functionality across the platform:

- **Authentication Feedback**: Detailed validation messages have been added to the login and registration forms, helping users correct email format and password complexity in real time.
- **Styling & UI Improvements**: Course page layout and components have been visually refined, including unified styling for materials and assignments blocks.
- **Dynamic Course Feed**: A flexible layout toggle between single and dual column views has been introduced, streamlining the display of both materials and assignments.
- **Live Content Refresh**: The course feed now updates in real time after adding new materials or assignments, enhancing user responsiveness.
- **Session Management**: A logout feature has been implemented, allowing users to securely exit their accounts.
- **Grading Interface**: Teachers can now view and grade student submissions, with input validation added for grading accuracy.
- **Course Feed Styling**: Unified dual-column layout for materials and assignments with consistent green design.

## DevOps

During the development of new features, we often write `TODO` comments in the code, marking places to think about / fix in the near future. Sometimes we may forget about such comments, so we have added a GitHub Action checker that checks that there are no `TODO` comments left in the code. This check is triggered on both push and pull requests. Failure on push does not limit the developer but shows them that the function is not ready yet while failure on pull request will limit the developer's ability to merge into the `main` branch, since all functionality must be completed at that moment.

Last week we added a feature to log all events that occur (post requests). The logs will allow administrators to keep track of what is happening on the site, but can take up an abnormally large amount of disk space. We have developed a TTL mechanism that periodically deletes logs older than 7 days.

Also, the frontend team had a problem with docker compose running very slowly because it requires compilation. We split the docker-compose file into two versions: one that runs the dev version of the site with the `dev` version of the frontend (warnings about the code are displayed, no compilation required, and runs fast), and one that runs the site with the `main` version of the frontend (requires compilation, takes a long time to run, but is optimized). Also the frontend Dockerfile has been optimized so that unless the nodejs package list has changed, then startup is 2x faster on `main` and instant on `dev`.

The backend team developed the consept of admin account. We added new curl tests to check this feature.

We also made minor improvements to README.md, adding information about production server, setting badges and making the overall design more readable.

## Plan for the Week 6

During week 6, we plan to continue developing our project as follows:
- the frontend team plans to fix the issues found during the usability testing sessions, add the page with the list of students and implement the option to attach the files to course materials, assignments, and submissions;
- the backend team plans to implement course-wide grading, attendance tracking mechanism and endpoints for the gradebook page;

# Individual contribution

### Gleb Popov
- [`management`]: A meeting with the administrator of the Sberclass platform have been organized;
- [`backend`]: The separate database for the attachments has been developed ([*PR #83*](https://github.com/IU-Capstone-Project-2025/edhub/pull/83));
- [`backend`]: The concept of admin account has been developed ([*PR #88*](https://github.com/IU-Capstone-Project-2025/edhub/pull/88));
- [`devops`]: README.md has been improved ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/86f79530e454658dc327a077093e93f2bffce13b));
- [`management`]: Weekly report has been written ([*PR #620*](https://github.com/IU-PR/Capstone_project/pull/620));
- [`backend`]: Careful review of pull request has been conducted ([*PR #84*](https://github.com/IU-Capstone-Project-2025/edhub/pull/84), [*PR #92*](https://github.com/IU-Capstone-Project-2025/edhub/pull/92), [*PR #94*](https://github.com/IU-Capstone-Project-2025/edhub/pull/94), [*PR #95*](https://github.com/IU-Capstone-Project-2025/edhub/pull/95), [*PR #97*](https://github.com/IU-Capstone-Project-2025/edhub/pull/97)).

### Timur Usmanov
- [`backend`]: The separate database for the attachments has been developed ([*PR #83*](https://github.com/IU-Capstone-Project-2025/edhub/pull/83));
- [`backend`]: An option to export course grade as `csv` file has been developed ([*PR #94*](https://github.com/IU-Capstone-Project-2025/edhub/pull/94));
- [`devops`]:  Docker Compose file has been spliited on two files for debug and production ([*PR #84*](https://github.com/IU-Capstone-Project-2025/edhub/pull/84));
- [`devops`]: The frontend Dockerfile has been optimized ([*PR #85*](https://github.com/IU-Capstone-Project-2025/edhub/pull/85));
- [`backend`]: Careful review of pull request has been conducted ([*PR #83*](https://github.com/IU-Capstone-Project-2025/edhub/pull/83), [*PR #88*](https://github.com/IU-Capstone-Project-2025/edhub/pull/88), [*PR #92*](https://github.com/IU-Capstone-Project-2025/edhub/pull/92), [*PR #95*](https://github.com/IU-Capstone-Project-2025/edhub/pull/95), [*PR #97*](https://github.com/IU-Capstone-Project-2025/edhub/pull/97)).

### Askar Dinikeev
- [`devops`]: GitHub Action to check the code for TODO comments has been set up ([*PR #92*](https://github.com/IU-Capstone-Project-2025/edhub/pull/92));
- [`devops`]: TTL mechanism to remove old logs has been developed ([*PR #95*](https://github.com/IU-Capstone-Project-2025/edhub/pull/95));
- [`devops`]: Curl tests for the admin account have been developed ([*PR #97*](https://github.com/IU-Capstone-Project-2025/edhub/pull/97)).

### Alina Suhoverkova

- [`frontend`]: Detailed validation messages for email and password fields has been added to improve authentication feedback ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/5d433b566b50fde9bf557e621531e922cb0feb58));
- [`frontend`]: UI/UX design on the Course page has been improved, including styling updates for Materials and Assignments sections ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/4b449d77ba80c31c7e414cc3238c3c8efa593ea9));
- [`frontend`]: Real-time refreshing for Materials and Assignments after creation has been fixed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/627b43b8860a8c26cc3feab2ac09b8f21760afc3));
- [`frontend`]: CourseFeed layout has been updated to match dual-section (Materials & Assignments) style ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/422c10c6404b551581b7d7d8a5ffb5306e5d73b5)).

### Timur Struchkov

- [`frontend`]: Ability to grade and view results has been added ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/4ccb7c23a183cae5e96bc2fb03564686e2cbe657));
- [`frontend`]: Ability to logout has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/c0b939436c60c982e6f9e27ade3376fee3dc654f));
- [`frontend`]: A check for grade number validity has been added ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/5bf3ac1a71424374420530d37e4a956599690ae6));
- [`frontend`]: An ability to switch between single and double column feeds has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/a0b4c1b4f13344f9bead30e74098da11b37818a1), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/8d2ed6f7c81cffef6cdcf95e316461d74d29f4be)).

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.
