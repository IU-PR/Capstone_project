# EdHub Week 6 Report

<aside>

Capstone Project course

Innopolis University

July 2025

</aside>

## Links

- Deployment: [*edhub.space*](http://edhub.space/)
- API Docs: [*edhub.space/api/docs*](https://edhub.space/api/docs)
- Design: [*Figma*](https://www.figma.com/design/dZsl8QQ8ZdJAXhzhCROajk/EdHub?node-id=0-1&p=f&t=lpPrzlTOAAF9SWLW-0)
- Demo: …
<!-- TODO: demo -->

# Final Deliverables

## Project overview

EdHub is a Learning Management System for interaction between teachers, students, and parents. It aims to improve the quality of an educational process, simplify the interaction between stakeholders, and improve student engagement in learning.

Any user can create a course becoming a **Teacher**, invite students and their parents, upload materials, create assignments, see student submissions, and grade them based on criteria. User can also join the course as a **Student** to see the study materials and submit their homework or as a **Parent** to track the academic performance of their children.

Most existing LMSs either have limited functionality or have awkward website design and cause difficulties in everyday use. EdHub combines a self-contained and clear design, supporting all the necessary features but not bogging the user down with complex customizations.

## Key Features

### Parental Access

None of the LMSs we explored supports parental access to the course. Parents often want to keep abreast of their children's academic progress; since the child usually does not want to give them their account, parents start contacting the teacher and clarifying questions about each individual grade.

EdHub supports a separate role for the parent to keep track of their student's grades.

### Quick Setup

Many of the LMSs we explored (e.g. Moodle or Stepik) require a long time to configure a large number of parameters before a course can be created.

To start using EdHub, one need to register and create a course by entering a title.

### Open Source

Many LMSs store data on company servers, including foreign ones, and do not support local hosting because the LMS is commercial.

EdHub is an open source project and any school can run their own version of EdHub and store their student and staff data locally.

## Tech stack

- React framework was chosen as the main **frontend stack** for its component-based architecture, rich ecosystem, and strong community support, enabling rapid UI development.
- FastAPI Python framework was chosen as the main **backend stack** for its high development speed and extensive documentation
- PostgreSQL was chosen as the main **database** for its reliability and extensibility.
- Docker Compose is chosen for the **deployment process** as it is the industry standard for service deployment using containers.

## Setup instructions

Since our project consist of Docker containers and does not require complex instructions, to download a copy of the project and run it on your local machine, you can type:
```bash
# Clone repository
git clone https://github.com/IU-Capstone-Project-2025/edhub.git
cd edhub

# Build and start containers
docker compose up --build

# To run in detached mode:
# docker compose up --build -d

# To stop all services
# docker compose down

# To stop and remove volumes
# docker compose down -v
```

## Presentation draft

The presentation draft is available via the [*link*](https://docs.google.com/presentation/d/1j8XrIkxvNVK3x4jq78MH5Uz0QWQk2-JSRoj6kuIVDDY/edit?usp=sharing).

# Weekly achievements

## Backend

## Frontend

## DevOps

## Plan for the Week 7

During week 7, we plan to continue developing our project as follows:
- the frontend team plans to ;
- the backend team plans to ;

# Individual contribution

### Gleb Popov
- [`management`]: A meeting with the administrator of the Sberclass platform have been organized;
- [`backend`]: The separate database for the attachments has been developed ([*PR #83*](https://github.com/IU-Capstone-Project-2025/edhub/pull/83));
- [`backend`]: The concept of admin account has been developed ([*PR #88*](https://github.com/IU-Capstone-Project-2025/edhub/pull/88));
- [`devops`]: README.md has been improved ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/86f79530e454658dc327a077093e93f2bffce13b));
- [`management`]: Weekly report has been written ([*PR #663*](https://github.com/IU-PR/Capstone_project/pull/663));
- [`backend`]: Careful review of pull request has been conducted ([*PR #84*](https://github.com/IU-Capstone-Project-2025/edhub/pull/84), [*PR #92*](https://github.com/IU-Capstone-Project-2025/edhub/pull/92), [*PR #94*](https://github.com/IU-Capstone-Project-2025/edhub/pull/94), [*PR #95*](https://github.com/IU-Capstone-Project-2025/edhub/pull/95), [*PR #97*](https://github.com/IU-Capstone-Project-2025/edhub/pull/97)).

### Timur Usmanov
- [`backend`]: 

### Askar Dinikeev
- [`devops`]: 

### Alina Suhoverkova

- [`frontend`]: 

### Timur Struchkov

- [`frontend`]: 

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.
