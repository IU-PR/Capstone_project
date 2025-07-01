---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

- **Onboarding with 3 Hardcoded Questions:**

  Users are prompted with three fixed, free-form questions to gather their learning goal, current skill level, and preferred study time. Inputs are accepted as plain text.

- **Personalized Course Search:**

  The backend uses a simple vector search (via Qdrant) to match user input with relevant courses, returning a linear list of recommended resources based on the provided answers.

- **Popular Courses:**

  An additional endpoint provides a list of popular courses, available regardless of user input.

- **Simple Linear Output:**

  Recommendations are displayed as a list. Each recommended course includes a title, image, and all available metadata (e.g., duration, difficulty, rating). If some of the metadata or image is missing, it is omitted.


## Demonstration of the working MVP

Link to the MVP demo video: https://disk.yandex.ru/i/by0dt3znwI9tFQ


## Internal demo

### Good parts:

Implemented all features planned for MVP

Enhansed search & productivity


### To be improved as MVP:

Add a trashhold, to make the number of cards dynamic & improve search precision

Add similarity threshold to suggest courses or return fallback message on low match


#### +Implement new features planned for the final product 

# Weekly commitments

## Individual contribution of each participant

| Team Member                         | Telegram Alias    | Email Address                        | Track                                   | Responsibilities                                                                                                                                                                                                                                                        |
|-------------------------------------|-------------------|--------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lana Ermolaeva (lead)               | @oELYAo           | l.ermolaeva@innopolis.university     | Project and Product Management           | Backlog: https://app.clickup.com/9015876757/v/s/90155186012; Report writing; Project evolution planning: [Click-up whiteboard](https://app.clickup.com/9015876757/whiteboards/8cp6q4n-395)                                                                                                                                               |
| Adilya Saifetdiarova                | @sayfetik         | a.saifetdiarova@innopolis.university | Front-end and UX/UI design               | Design: Design roadmaps page, Update chat page design, Update userflow [week 3 Assets](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/tree/master/assets/week3), [new designs in Figma](https://www.figma.com/design/JjmqRt1Tr5xyc9X3vRJN5L/SkillsNavigator?node-id=0-1&p=f&t=xk3mK3r3PvSluAkJ-0); Frontend: Connect frontend and backend, Add error handling [Pull request 6](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/6)                                                                                         |
| Ivan Ershov                         | @spiritonchiс     | i.ershov@innopolis.university        | ML                                       | Made the parser asynchronous and run as a background task [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/7aef911722cfb9ff707f32a82787b20315828943), Completed the course search endpoint [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/b321bdf85f0590da2bc2cb62300809ba80bdd8c9), Fixed frontend launch bug [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/4ebcee9429bc5b86f51cf25c8155e9215a2cda3c), Added support for running the encoder on the GPU [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/589c3d42596b17ec313867c2a76037363393e1cc), Refactored model saving: removed redundant folder creation and checks by using proper function argument [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/b15c2b059652d92544ddb8bdfbdce34bdc8c5248), Allow passing null values for certain course parameters from frontend [Commit 1](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/7dde82e9c1e466743573fb31e4c60d3b84e7778d), [Commit 2](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/961e56a9ba00e0c536c995d85b177a276dd13a6e)|
| Bulat Gazizov                       | @BulatGazizov0    | b.gazizov@innopolis.university       | Back-end working with Front-end, DevOps  | Refactored the course-fetching logic, Added functionality to retrieve author information and their ratings (requires additional requests to Stepik), Made the "popular courses" endpoint functional, Fixed validation-related bugs, Reworked Docker settings to enable communication between frontend and backend, Removed the CORS workaround (made possible by the Docker changes above) [Pull request 6](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/6)|
| Arthur Popov                        | @ee_boooy         | ar.popov@innopolis.university        | Back-end working with ML, MLOps,         | Add logging, Backend code refactoring [Commit](https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/commit/87b5e4594b2d9d0d5ba5faccede3a202cc5b5ac5)|

## Plan for Next Week
Select & start implementing the model of advanced search, show the roadmap, add signing in via Stepik, deploy the service to the server.


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose (or another alternative described in the `README.md`).
