# EdHub Week 5 Report

<aside>

Capstone Project course

Innopolis University

July 2025

</aside>

# Feedback

This week we conducted several usability testing sessions to collect feedback about using EdHub from external people, detect bugs, and find out the features for future development.

### Sessions

All users with whom we discussed our project mostly noticed the minuses of our project and gave suggestions for its improvement, which was quite useful for us.

#### Session 1 
<!-- Рия -->
- there is no option to delete materials / assignments within the course
- material_id does not start with one (the first material has ID = 3)
- nothing happens when the user clicks on the logo in the upper left corner of the page (in other websites the main page opens)
- there is no option to log out from the account
- after the creation of course / material / assignment, the page doesn't refresh, and user have to refresh it manually

#### Session 2
<!-- Дамир -->
- default browser pop-up windows look ugly
- the option to see a list of students in a course will be useful
- it is possible that one users will be both a teacher and a parent at one course while the platform does not allow that
- after the creation of course / material / assignment, the page doesn't refresh, and user have to refresh it manually

#### Session 3 
<!-- Глеб -->
- when entering the auth page, an authorized user is prompted to re-enter login and password, although the token has already been issued; you can redirect user to the main page if they are authorized
- two separate columns for course materials and course assignments looks ugly
- after the creation of course / material / assignment, the page doesn't refresh, and user have to refresh it manually

#### Session 4 
<!-- Маша -->
- when registering an account, the system writes that the password is too easy, and the criteria are not clear
- in the Add Course button, the second word moves to the next line, which looks ugly
- the field for material/assignment description can be stretched beyond the pop-up window frame
- after the creation of course / material / assignment, the page doesn't refresh, and user have to refresh it manually
- if user enter line break characters in the material / assignment description, then on the material / assignment page they disappear and become a single line
- when inviting a student, submitting the form with the Enter key does not work

### Analysis

Meetings with independent users have been very useful for our project. Although most of the problems they reported were known to us and were in the process of development, we discovered a few new issues that we had not noticed before and plan to fix them in near future.

# Iteration & Refinement

### Implemented features based on feedback

fdsfds

### Documentation

fgdf

# Weekly achievements

## Management

<!-- встреча с юлей -->
<!-- репорт написан -->

## Backend

<!-- админ аккаунт -->
<!-- экспорт в csv -->
<!-- что тимур делал в начале неделе -->
<!-- посмотреть пул реквесты (кто что делал)
посмотреть пул реквесты (кто какие ревью) -->

## Frontend

<!-- комменты от Алёны и Тимура -->

## DevOps

<!-- README.MD improved -->

## Plan for the Week 5

During week 5, we plan to continue developing our project as follows:
- the backend team plans to ;
- the frontend team plans to .

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
