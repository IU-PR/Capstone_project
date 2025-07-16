# EdHub Week 6 Report

<aside>

Capstone Project course

Innopolis University

July 2025

</aside>

## Links

Since surrently we are continue the development process, the final demo video is not ready yet.

- Deployment: [*edhub.space*](http://edhub.space/)
- API Docs: [*edhub.space/api/docs*](https://edhub.space/api/docs)
- Design: [*Figma*](https://www.figma.com/design/dZsl8QQ8ZdJAXhzhCROajk/EdHub?node-id=0-1&p=f&t=lpPrzlTOAAF9SWLW-0)
- Demo: will be availabe at the [*disk*](https://drive.google.com/drive/folders/13HipbNm6YiM1MQjhS-CCmZ_m2YvtPHlp?usp=sharing) later this week

# Final Deliverables

## Project overview

EdHub is a Learning Management System for interaction between teachers, students, and parents. It aims to improve the quality of educational process, simplify the interaction between stakeholders, and improve student engagement in learning.

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

## Management

We formed the final set of features in the project, highlighted the key features that set our project apart from other products on the market and created a draft for the final presentation.

We also added the Built With block to the README to meet the requirements of the project.

## Backend

Since the backend team has been productive for the first 5 weeks and outpaced the frontend team in terms of functionality, this week, in anticipation of the deadline, we decided to slow down and not develop any new functionality.

We decided to refactor our project to create a more rigorous architecture and develop rules for writing code within the team. At the moment we have a draft of the new architecture, which is in the process of being reviewed. We don't want to apply it this week as we are not sure that the system will work without errors, which is crucial in the run-up to the project handover.

During the development of the admin account, at system startup we created a default admin user with a random password that was displayed on the screen. However, when the production server was restarted, this password was erased and the admin account was lost forever. We decided to create a default admin account with `admin` password.

We also noticed that every time we access the database, the system initializes a new connection, which is inefficient. We decided to start using connections from the connection pool instead of creating a new one each time.

Frontenders reported issues when attaching a file to a course element, we found a typo in the file storage connection code and fixed it.

## Frontend

<!-- TODO: достижения фронтенда от Алины -->

## Plan for the Week 7

During week 7, we plan to finilize the developing our project as follows:
- the backend team plans to develop an API commands to support the Grades page;
- the frontend team plans to ;
<!-- TODO: планы фронтенда (можно перечислить незакрытые issues из гитхаба) -->

# Individual contribution

### Gleb Popov
- [`management`]: presentation draft has been created ([*Google Slides*](https://docs.google.com/presentation/d/1j8XrIkxvNVK3x4jq78MH5Uz0QWQk2-JSRoj6kuIVDDY/edit?usp=sharing));
- [`management`]: Built With block has been added to README.md ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/7cd4b9a6b891343f52de67a22aac12a43385932e), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/53ea6d1be1c629060218c8e5ca0fafeefdacc9aa));
- [`backend`]: Default password for admin account has been changed ([*PR #133*](https://github.com/IU-Capstone-Project-2025/edhub/pull/133));
- [`backend`]: Careful review of pull request has been conducted ([*PR #132*](https://github.com/IU-Capstone-Project-2025/edhub/pull/132)).

### Timur Usmanov
- [`backend`]: backend architecture refactoring has been conducted ([*PR #130*](https://github.com/IU-Capstone-Project-2025/edhub/pull/130));
- [`backend`]: typo in the file storage connection code has been found and fixed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/b4f3d3e3242f72cc69469c5cab6a3cabd3901e64));
- [`backend`]: Careful review of pull request has been conducted ([*PR #132*](https://github.com/IU-Capstone-Project-2025/edhub/pull/132), [*PR #133*](https://github.com/IU-Capstone-Project-2025/edhub/pull/133)).

### Askar Dinikeev
- [`backend`]: backend architecture refactoring has been conducted ([*PR #130*](https://github.com/IU-Capstone-Project-2025/edhub/pull/130));
- [`backend`]: database connection creation has been replaced with connection pooling ([*PR #132*](https://github.com/IU-Capstone-Project-2025/edhub/pull/132)).

### Alina Suhoverkova

- [`frontend`]: 
<!-- TODO: достижения Алины -->

### Timur Struchkov

- [`frontend`]: 
<!-- TODO: достижения Тимура -->

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.
