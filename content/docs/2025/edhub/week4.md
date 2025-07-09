# EdHub Week 4 Report

<aside>

Capstone Project course

Innopolis University

July 2025

</aside>

# CI/CD Setup

## Continuous Integration

We have developed integration tests (`/backend/curltests.sh`) that will allow us to make sure that the new version works when new features are added. The specific tests are:

- Registering users;
- Logging;
- Creating a course;
- Getting available courses;
- Getting course info;
- Inviting student to course;
- Getting enrolled students;
- Inviting parent to student;
- Getting student's parents;
- Inviting second teacher;
- Getting course teachers;
- Creating material;
- Getting course feed;
- Getting material;
- Creating assignment;
- Getting assignment info;
- Submitting assignment;
- Grading assignment.

We also configured a worker instance on the Innopolis University Virtual Machine, which run the tests every time when push or pull request to the `dev` and `main` branches happen. Moreover, it is impossible to merge a pull request into `main` branch without passing all the tests even if the code is successfully reviewed. You can see the example of automatic testing logs [*here*](https://github.com/IU-Capstone-Project-2025/edhub/actions/runs/16027449789/job/45218962473).

## Continuous Delivery

For automatic website deployment we configured two environments: **Staging Environment** for developers to test new versions of the application and **Production Environment** for customers to use the service.

| Environment | Machine        | Provider      | OS           | Network             | SSH Access    | SSH Key Holders |
|------------|-----------------|---------------|--------------|---------------------|---------------|-----------------|
| Staging    | Virtual Machine | Innopolis University     | Ubuntu 22.04 | 10.90.138.154 (local university network)   | Password and PublicKey     | Timur Usmanov, Askar Dinikeev, Gleb Popov  |
| Production | Virtual Dedicated Server | timeweb.cloud | Ubuntu 24.04 | edhub.space (DNS), 82.97.249.54 (public IP)        | PublicKey     | Timur Usmanov, Askar Dinikeev, Gleb Popov  |


### Staging Environment
Staging Environment runs a version of the site on the `dev` branch on the Innopolis University Virtual Machine. We set up public key SSH access, created a new non-sudo user `staging`, installed Docker and a Github Actions runner with a label `edhub-staging`. Now we can manually test new features before merging them into `main` branch. 

You can see the example of automatic deployment logs [*here*](https://github.com/IU-Capstone-Project-2025/edhub/actions/runs/16027449796/job/45218962463).

### Production Environment
Production Environment runs a version of the site on the `main` branch on the globally accessible server. This version is tied to the public domain [*edhub.space*](www.edhub.space) and will be used by our customers.

You can see the example of automatic deployment logs [*here*](https://github.com/IU-Capstone-Project-2025/edhub/actions/runs/16027975047/job/45220777035).

We decided to use [timeweb.cloud](https://timeweb.cloud/) hosting since it provides easily customizable servers located in Russia (which is crucial for storing personal data) with characteristics suitable for our project.

We rented the edhub.space domain for a year. Popular domain zones such as edhub.ru and edhub.com were busy or expensive, and ed-hub.ru seemed awkward to us because of the hyphen in the name. edhub.space balances affordability with a memorable address. We set up A-fields to redirect from http://edhub.space/ and www.edhub.space to our production server.

We disabled password-based SSH authentication, set up public key SSH access, created a new non-sudo user `prod`. Then, we installed Docker and a Github Actions runner with a label `edhub-prod`.

To ensure a secure https connection, we obtained SSL certificates from Let's Encrypt with the `certbot` utility.

# Weekly achievements

## Management

This week we launched a survey about LMS usage among school teachers, university professors, and tutor. Particularly, we contacted the headmaster of a Moscow school (MAI Pre-University school) in order to distribute our survey to the school's teachers. We hope to get their responses soon to identify their needs as educators, and to identify key functions needed. We also hope that the word of mouth effect and the professorial community of teachers will help us distribute this survey to other faculty members.

We also agreed with the principal to possibly integrate EdHub into the school's educational process to test the platform in early fall 2025.

## Backend

After encountering difficulties while developing the feature to add files to course items last week, the backend team decided to rewrite the feature from scratch this week. We created 3 new tables: `material_files`, `assignment_files`, and `submissions_files`. At this point, we decided to save user files to the database in byte format. We set a file size limit of 5MB, we also have the support for incremental file uploads (by chunks), so that a hacker will not be able to overload the server by uploading too large a file before the checks start.

## Frontend

The frontend team focused on improving the visual design, usability, and fixing key issues across the platform:

- **Landing Page**: A new standalone landing page introduces users to the platform before registration.
- **Authentication Improvements**: Added validation for email format, name, and password complexity. Improved user feedback during login/registration.
- **Design & Styling**: Unified styles across all pages using clean CSS. Replaced LMS text with a scalable SVG logo. Updated overall layout for better clarity.
- **Bug Fixes**: Resolved infinite request loop on app start. Fixed navigation buttons like Back to Course Feed and Add Parent. Improved assignment/material creation experience with real-time feedback.
- **Functionality**: Developed ability to leave course as students, parents and teachers. Updated assignment page to include the ability to submit and view the answer as a student, as a parent see child's submission, and as a teacher to see all children's submissions.

## DevOps

This week the devops team has been working on the CI/CD setup detailed above.

## Plan for the Week 5

During week 5, we plan to continue developing our project as follows:
- the backend team plans to develop a course evaluation option, an attendance tracking mechanism, and add an admin account;
- the frontend team plans to improve the UI/UX design of the website and create a journal page (table) with grades.

# Individual contribution

### Gleb Popov
- [`management`]: Agreed to distribute a survey to teachers at MAI Pre-University School;
- [`management`]: Agreed to be able to test the platform in a real school in the fall of 2025;
- [`management`]: edhub.space domain has been rented after discussion with the team;
- [`backend`]: Feature of attachments to course items has been finalized ([*PR #63*](https://github.com/IU-Capstone-Project-2025/edhub/pull/63));
- [`management`]: Weekly report has been written ([*PR #584*](https://github.com/IU-PR/Capstone_project/pull/584)).

### Timur Usmanov
- [`devops`]: Innopolis University Virtual Machine has been configured as a staging environment;
- [`devops`]: TimeWeb.Cloud VDS has been configured as a production environment;
- [`devops`]: Сertificate to support `https` has been configured.
- [`backend`]: Careful review of pull request has been conducted ([*PR #63*](https://github.com/IU-Capstone-Project-2025/edhub/pull/63), [*PR #65*](https://github.com/IU-Capstone-Project-2025/edhub/pull/65), [*PR #67*](https://github.com/IU-Capstone-Project-2025/edhub/pull/67))

### Askar Dinikeev
- [`devops`]: Github Action Workflow running the integration tests has been configured ([*PR #65*](https://github.com/IU-Capstone-Project-2025/edhub/pull/65));
- [`devops`]: Github Action Workflow deploying the staging server has been configured ([*PR #66*](https://github.com/IU-Capstone-Project-2025/edhub/pull/66));
- [`devops`]: Github Action Workflow deploying the production server has been configured ([*PR #67*](https://github.com/IU-Capstone-Project-2025/edhub/pull/67));
- [`backend`]: logging of the attachment creation has been introduced ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/pull/63/commits/825675101d2e70a5de139400b39e18de9b1afa72)).

### Alina Suhoverkova
- [`frontend`]: Form validation and UX issues on auth pages have been fixed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/c3f2eb3ab7a698277d3e9cc6651684470d1e24f6));
- [`frontend`]: GitHub repo link has been added to the landing page for user visibility ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/c3f2eb3ab7a698277d3e9cc6651684470d1e24f6));
- [`frontend`]: Standalone landing page has been implemented, consistent global styling has been applied, routing logic has been updated in App.js for cleaner navigation flow ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/bd9fd6f4ab160132a1ac39f4530135d30c740182));
- [`frontend`]: Email and password validation have been developed, infinite fetch loop on frontend startup have been resolved, EdHub logo has been added, interface styling has been improved ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/dacb695a2588a3d82afc28ef4aa2ff0b40a5ce21)).

### Timur Struchkov
- [`frontend`]: Feature for students to leave a course has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/ffdc3615cda44299ef4aea474cf43b811c3b4d30));
- [`frontend`]: Navigation bugs (e.g., "Back to course feed" button) have been fixed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/9076763ee7614d29e67d1beea5e68f994f3963f2), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/652580425797200519a9f288d816724d9bf0c90d));
- [`frontend`]: Refactoring of assignment detail page has been started for better structure and UX ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/9076763ee7614d29e67d1beea5e68f994f3963f2));
- [`frontend`]: Ability to submit and view the assignment submission as a student has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/652580425797200519a9f288d816724d9bf0c90d));
- [`frontend`]: Ability to view child's assignment submission as a parent and to  and as a teacher to see all submissions has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/0056523ce55adb355ad50ab551002057aa481ae0)).

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.
