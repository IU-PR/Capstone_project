---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

 - Workout execution feature completed – users can now start, pause and finish training sessions.
 - MVP declared READY
 - Introduced clean-architecture layers (Data ➜ Domain ➜ Presentation).
 - Added light & dark themes.
 - Implemented robust state-management and UI for the workout flow.
 - Set up full navigation / routing logic.

## Demonstration of the working MVP

*Screenshots/GIFs/PDF presentation/Videos demonstrating the working MVP*

## Internal demo

*Notes from internal demo*

# Weekly commitments

## Individual contribution of each participant

Ivan Chabanov:
- added Data, Domain, Presentation layers
- added dark/bright themes to application
- implemented state management and created UI for working out process
- made navigation/routes logic

https://github.com/IU-Capstone-Project-2025/gym-genius/commit/5cfaed1ffed3558977cf2db08081f7919062317b

Kirill Nosov:
- Added method for JWT-token generation.
- Added method for password hashing.
- Made the Swagger for the admin panel backend.
- Created models of the user and user activity for database.
- Tested basic scenarious of the API.

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/13 (check personal commits)

Aleksandr Mikhailov:
- Added proper config to backend
- Added docker files for deployment
- Fully implemented get active users and post user activity endpoints
- Added README.md to backend

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/13 (check personal commits)

Egor Dushin
- Authorization form in admin panel interface - [PR](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/14)
- CI/CD for admin panel frontend - [PR](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/15)

Vladislav Kuznetsov:
- Added production-docker compose for mobile deployment - [PR](https://github.com/IU-Capstone-Project-2025/gym-genius/pull/16)
- Setup ubuntu server, setup network configuration, firewall, dependencies. Deployed mobile app. [URL](http://213.171.25.183/)


## Plan for Next Week

Continue working on our features. Some of the tasks can be seen in backlog already:
https://nodoser.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [*] In working condition.
- [*] Run via docker-compose (or another alternative described in the `README.md`).