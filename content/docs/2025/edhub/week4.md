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
- Logging in as Alice;
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

| Deployment | Machine Type    | Provider      | OS           | Network             | SSH Access    | SSH Key Holders |
|------------|-----------------|---------------|--------------|---------------------|---------------|-----------------|
| Staging    | Virtual Machine | Innopolis University     | Ubuntu 22.04 | 10.90.138.154 on a local university network   | Password and PublicKey     | Timur Usmanov, Askar Dinikeev, Gleb Popov  |
| Production | Virtual Dedicated Server | timeweb.cloud | Ubuntu 24.04 | edhub.space, 82.97.249.54 (public IP)        | PublicKey     | Timur Usmanov, Askar Dinikeev, Gleb Popov  |


### Staging Environment
Staging Environment runs a version of the site on the `dev` branch on the Innopolis University Virtual Machine. We as a development team can open the site and manually test the developed innovations before merging it into the `main` branch. 

You can see the example of automatic deployment logs [*here*](https://github.com/IU-Capstone-Project-2025/edhub/actions/runs/16027449796/job/45218962463).

### Production Environment
Production Environment runs a version of the site on the `main` branch on the globally accessible server. This version is tied to the public domain [*edhub.space*](www.edhub.space) and will be used by our customers.

You can see the example of automatic deployment logs [*here*](https://github.com/IU-Capstone-Project-2025/edhub/actions/runs/16027975047/job/45220777035).

We decided to use timeweb.cloud hosting because it is easy to set up, has suitable characteristics and provides servers in Russia.

We bought the domain edhub.space on REG.RU because it seemed to us the most suitable and memorable among all available domains. 

We bought the domain edhub.space on REG.RU because it seemed to us the most suitable and memorable among all available domains. We configured A-address forwarding (IPv4) and subdomain www.

To ensure a secure https connection, we configured a certificate from Let's Encrypt.

<!-- - берется из мейна
- хостинг timeweb.cloud в России
- привязали домен edhub.space
- сертификат от Let's Encrypt -->

# Weekly achievements

## Management

This week we finalized the creation of a survey about LMS usage among faculty. Since we have an MAI Pre-University school graduate in our team, we contacted the school's headmaster in order to distribute our survey to the school's teachers. We hope that the word of mouth effect and the professorial community of teachers will help us distribute this survey to other teachers.

We also agreed on the possibility of testing EdHub within the real educational process in MAI Pre-University school in the fall of 2025.

## Backend

This week, the backend team completely rewrote and finalized the feature of attachments to course elements. Teachers can now attach files to materials and assignments, and students can attach files to their submissions.

## Frontend

The frontend team focused on improving the visual design, usability, and fixing key issues across the platform:

- **Landing Page**: A new standalone landing page introduces users to the platform before registration;
- **Authentication Improvements**: Added validation for email format, name, and password complexity. Improved user feedback during login/registration;
- **Design & Styling**: Unified styles across all pages using clean CSS. Replaced LMS text with a scalable SVG logo. Updated overall layout for better clarity;
- **Bug Fixes**: Resolved infinite request loop on app start. Fixed navigation buttons like Back to Course Feed and Add Parent. Improved assignment/material creation experience with real-time feedback.

## DevOps

This week the devops team has been working on the CI/CD setup detailed above.

## Plan for the Week 4

During week 4, we plan to continue developing our project as follows:
- the backend team plans to develop a course evaluation option, an attendance tracking mechanism, and add an admin account;
- the frontend team plans to improve the UI/UX design of the website and create a journal page (table) with grades.

# Individual contribution

### Gleb Popov
- [`management`]: agreed to distribute a survey to teachers at MAI Pre-University School;
- [`management`]: agreed to be able to test the platform in a real school in the fall of 2025;
- [`management`]: edhub.space domain has been acquired after discussion with the team;
- [`backend`]: feature of attachments to course items has been finalized ([*PR #63*](https://github.com/IU-Capstone-Project-2025/edhub/pull/63)).

### Timur Usmanov
- [`devops`]: Innopolis University Virtual Machine has been configured as a staging environment;
- [`devops`]: TimeWeb.Cloud VDS has been configured as a production environment;
- [`devops`]: Сertificate to support `https` has been configured.
<!-- ревью пул-реквестов -->

### Askar Dinikeev
- [`devops`]: Github Action Workflow running the integration tests has been configured ([*PR #65*](https://github.com/IU-Capstone-Project-2025/edhub/pull/65));
- [`devops`]: Github Action Workflow deploying the staging server has been configured ([*PR #66*](https://github.com/IU-Capstone-Project-2025/edhub/pull/66));
- [`devops`]: Github Action Workflow deploying the production server has been configured ([*PR #67*](https://github.com/IU-Capstone-Project-2025/edhub/pull/67));
- [`backend`]: logging of the attachment creation has been introduced ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/pull/63/commits/825675101d2e70a5de139400b39e18de9b1afa72)).

### Alina Suhoverkova
- [`frontend`]: Form validation and UX issues on auth pages have been fixed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/c3f2eb3ab7a698277d3e9cc6651684470d1e24f6));
- [`frontend`]: GitHub repo link have been added to the landing page for user visibility ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/c3f2eb3ab7a698277d3e9cc6651684470d1e24f6));
- [`frontend`]: Standalone landing page has been implemented, consistent global styling has been applied, routing logic has been updated in App.js for cleaner navigation flow ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/bd9fd6f4ab160132a1ac39f4530135d30c740182));
- [`frontend`]: Email and password validation have been developed, infinite fetch loop on frontend startup have been resolved, EdHub logo has been added, interface styling has been improved ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/dacb695a2588a3d82afc28ef4aa2ff0b40a5ce21)).

### Timur Struchkov
- [`frontend`]: Feature for students to leave a course has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/ffdc3615cda44299ef4aea474cf43b811c3b4d30));
- [`frontend`]: Navigation bugs (e.g., "Back to course feed" button) have been fixed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/9076763ee7614d29e67d1beea5e68f994f3963f2));
- [`frontend`]: Refactoring of assignment detail page has been started for better structure and UX ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/9076763ee7614d29e67d1beea5e68f994f3963f2)).

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.