---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

### User journey 

#### Developer

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/user-flows/developer.png?raw=true)

#### Founder

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/user-flows/founder_user.png?raw=true)

### Features

- Added authentication and registration from backend
- Added creation of project cards form backend
- Added Create Project Dialog windows with backend connection
- Connected projects explore page with the backend
- Implemented new components: Alert, Dialog, Dropdown Menu, Sonner, Textarea
- Implemented API client with backend with automatic API schema pulling using openapi

## Demonstration of the working MVP

[Demo of MVP](https://github.com/IU-Capstone-Project-2025/ProjectOR/raw/refs/heads/main/docs/videos/mvp0_demo.mp4)

## Internal demo

Bugs Identified:
- “View Project” buttons are inconsistently aligned within cards of different heights.
- Typing in the search box yields no results even for exact project titles.
- Missing owner property of the project entity, no security policies on project manipulations
- No mobile devices support

Areas for Immediate Improvement:
- Add user roles, justify access to several endpoint in respect of user role
- Implement live filtering, display a clear “No projects found” message, and support partial matches.
- Add backend unit tests

# Weekly commitments

## Individual contribution of each participant

**Timur Nabiullin**: 

- Created user journey
- Found ways to solve dangerous bugs

**Almaz Andukov**:
- JWT token authorization is configured using OAuth2 Password Flow.
- User model is implemented, migrations and a table in the database are added.

- Routes are created:
    - POST /register — user registration
    - POST /token — receiving an access token

- Endpoints are protected by authorization, access to them is possible only with a valid JWT

[Link to PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/48)

**Nikita Timofeev**:

- Implemented new components: Alert, Dialog, Dropdown Menu, Sonner, Textarea
- Implemented API client with backend with automatic API schema pulling using openapi
- Implemented shared store for user authentication state
- Implemented authorization and registration handling with JWT token
- Connected projects explore page with the backend
- Added Create Project Dialog windows with backend connection
- Recorded and added MVP0 demo video
[Link to the PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/51)


**Kirill Karsakov**: 
- Wrote a report
- Added new tasks to task board
- Found new bugs in internal demo


## Plan for Next Week

- Write unit tests for critical backend logic and frontend components.
- Write integration tests for API endpoints
- Aim for basic end-to-end tests for the core user journey
- Set up Continuous Integration (CI) to automatically build and run tests on every push/PR
- Deploy the current version of your application to the staging environment

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).