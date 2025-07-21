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

The frontend team focused on expanding user management features, improving assignment interaction for all roles, and unifying design across the platform:

- **Participants Page**: A new page was added displaying all students enrolled in the course. Teachers also see the students’ parents listed next to each student.
- **Role-Specific Views**: While teachers see full participant data (including parents), students and parents only see a basic student list, ensuring privacy and clarity.
- **User Removal**: Teachers can now remove students and parents directly from the participant page via cross icons next to each name. This functionality is hidden from students and parents.
- **File Submission UI**: The submission interface for assignments has been fully redesigned. Students can now upload their solutions with clear visual feedback and see grades after evaluation.
- **Teacher Grading**: Teachers can view and grade submissions in a clean, structured layout. All student submissions are displayed with a consistent component design.
- **Parent Access**: Parents can now view their child’s assignments and grades, promoting better engagement and transparency.
- **Unified Styling**: Assignment and Material pages now follow the same styling guidelines, providing a consistent user experience across roles and sections.

## Plan for the Week 7

During week 7, we plan to finilize the developing our project.

The backend team plans to develop an API commands to support the Grades page.

The frontend team plans to 
- improve UI/UX design across course and assignment pages;
- create a Grades page with student scores;
- implement support for admin users;
- enhance course management by fixing the Add Course button and improving session persistence;
- refine course feed by distinguishing materials and assignments, adding auto-refresh after grading, and updating design of submission buttons.

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

- [`frontend`]: Participants page has been implemented with role-based visibility — teachers see parents, others don’t; removal buttons have been added for teachers;
- [`frontend`]: Assignment submission interface has been redesigned for students — now includes grade display and stylized file upload;
- [`frontend`]: Parent view has been updated — now displays child’s assignments and grades in a clean, minimal format;
- [`frontend`]: Grading interface has been refined — all submissions now appear as consistent UI blocks with improved styling;
- [`frontend`]: Material and Assignment pages have been visually aligned for unified course experience.

### Timur Struchkov

- [`frontend`]: Dynamic Page Title has been added ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/8075751c5e5cde2d87bf94be2d2a1e59d2e6fc7d));
- [`frontend`]: admin support has been added for current pages ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/13762ec93e107e658191dd40b5b9dea650b5a189));
- [`frontend`]: An ability for a parent to view several children's submissions has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/41ba7c4fc3955aa97dac36d6b824ff0f315ce7bf)).
- [`frontend`]: An ability to submit an answer with a file attachment  as a student has been developed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/b40e5ea667f2789d8972c7f2a0426780c5e82a04), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/3da42e4cef789a3559db7e34489b494bbc3926cc));
- [`frontend`]: Service information has been removed from the website ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/bb219777d442c207a80da13dca60bb6333a15c1d));
- [`frontend`]: Several visual and functional bugs have been fixed ([*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/5c2c6433c05eba56912fbe7c53eac6f8510ede9d), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/581fd3a4295b1cc9770d40f03daf353d81328214), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/cd8c9efaaef75020763422862004141d0da937b8), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/7e0e245e48fcdb8f7a611654364762a89575b7c9), [*commit*](https://github.com/IU-Capstone-Project-2025/edhub/commit/e7497f231f484f6e8e6818624cace669a96412a8)).

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.
