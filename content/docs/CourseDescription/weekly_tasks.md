---
weight: -1000
bookFlatSection: true
title: "Weekly tasks"
---

# Weekly Tasks & Project Guidelines

Each week, your team will tackle specific tasks, culminating in a functional project and a comprehensive report of your
work. Some tasks are common for all, while TAs will tailor others to your specific project. Important note:
delivering a well-structured, clear report is as crucial as writing functional code.

## Core Requirements (Applicable Every Week):

1. Master Branch Stability: Your `master` (or `main`) branch must contain working, runnable code at all times.
2. Reproducibility:
    * Package your solution in Docker containers and create a docker-compose file to run your project in one command.
    * Alternatively, provide crystal-clear documentation (e.g., a `README.md` with precise setup and run commands) to
      allow TAs to reproduce your solution easily.
    * If a TA cannot run your solution (locally, in Google Colab, Docker, or via a provided link), the implementation
      part for that week will receive 0 points.
3. Trackable Progress: Your progress must be visibly trackable week-over-week. This could be through:
    * More endpoints in Swagger/OpenAPI documentation.
    * Improved or new UI elements in the frontend.
    * New pages/flows in Figma designs.
    * An evolving Kanban board with completed tasks.
    * Expanded datasets or refined ML models.
4. Individual Contributions in Reports: Each weekly report *must* clearly list tasks completed by *each team member*
   with specific deliverables:
    * Designers: Screenshots of new/updated designs, links to Figma files (specific pages/frames), user flow diagrams.
    * Frontend Developers: Links to merged Pull Requests (PRs) or closed issues. Screenshots/GIFs of new UI components
      or functionality.
    * Backend Developers: Links to merged PRs or closed issues. Links to updated API documentation (e.g.,
      Swagger/OpenAPI).
    * Project Managers: Links to created/assigned issues, updated Kanban board (e.g., Trello, Jira, GitHub Projects),
      summary of customer/TA feedback and action items.
    * Analytics Specialists: Links to `.ipynb` notebooks, dashboards, datasets used/generated, key insights derived.
    * ML Developers: Links to source code (e.g., specific commits/PRs), model artifacts (e.g., Hugging Face model page,
      `.pkl` files in a repo), relevant research papers or techniques explored.
5. Plan for Next Week: Each report must include a clear plan for the next week, detailing:
    * What tasks will be tackled.
    * Expected deliverables.
6. Report Submission:
    * Reports should be submitted as a `Markdown` file in the [Report repository](https://github.com/IU-PR/Capstone_project).
    * An example weekly report template can be found here: [Example Reports](/docs/2025/exampleproject/week1/)

<hr/>

## Weekly Breakdown:

### Week #1: Foundation & Planning

*Goal: Form a team, define a clear project vision, and set up the basic infrastructure.*

#### Tasks:

1. Course Familiarization: Thoroughly review the project guidelines, and grading rubric.
2. Team Formation: Find teammates. Establish team name and communication channels.
3. Role Assignment (Initial): Define initial roles and responsibilities for each team member.
4. Project Brainstorming & Selection:
    * Brainstorm at least 3–5 project ideas.
    * Conduct brief market research/problem validation for top 1–2 ideas.
    * Select one project idea and define a clear Problem Statement.
5. Basic Requirements Gathering:
    * Identify target users and their primary needs.
    * Draft 3–5 high-level User Stories (e.g., "As a [user type], I want to [action] so that [benefit]").
    * Define the initial Scope (what's IN for the MVP, what's OUT).
6. Repository Setup:
    * Fork the provided [Report repository](https://github.com/IU-PR/Capstone_project).
    * Create a new repository for your project code in [organization](https://github.com/IU-Capstone-Project-2025).
    * Initialize with a basic boilerplate structure (e.g., `frontend/`, `backend/`, `docs/`, `README.md`, `.gitignore`).
    * Ensure the boilerplate is runnable (e.g., a simple "Hello World" app).
    * Prepare Docker support (or a **crystal-clear** documentation to run the project):
        * Create a `Dockerfile` for each component of your project.
        * Create a `docker-compose.yml` file to run all components together (frontend, backend, database, S3, etc.).
7. Tech Stack Selection:
    * Choose a viable project stack (frontend, backend, database, ML libraries if applicable).
    * Briefly justify your choices in your report.

#### Deliverables (in Report):

* Team members and assigned roles.
* Chosen project idea, problem statement, target users.
* List of high-level user stories and initial scope.
* Link to your project code repository (with runnable boilerplate).
* Chosen tech stack with justification.

### Week #2: Initial Design & Elaboration

*Goal: Translate requirements into initial designs and backend structures, and refine project details.*

#### Tasks:

1. Detailed Requirements Elaboration:
    * Expand high-level user stories into more detailed ones for the MVP.
    * Define Acceptance Criteria for key user stories.
    * Create an initial backlog with prioritized features/tasks (using your chosen PM tool).
2. Design (Designers):
    * Create low-fidelity wireframes or mockups for core application screens/pages.
    * Develop basic user flow diagrams for key interactions.
3. Frontend (Frontend Developers):
    * Set up the frontend project structure.
    * Implement skeleton components/pages based on initial designs (no backend integration yet).
    * Basic routing if applicable.
4. Backend (Backend Developers):
    * Define the initial API contract (e.g., using OpenAPI/Swagger for MVP endpoints).
    * Set up the backend project structure and initial database schema (if applicable).
    * Implement one or two basic, non-functional (dummy data) endpoints.
5. ML (ML Developers, if applicable):
    * Research potential models/algorithms.
    * Identify or start collecting/preparing a dataset.

#### Deliverables (in Report):

* Updated/detailed user stories with acceptance criteria.
* Link to prioritized backlog (Kanban board).
* (Designers) Wireframes/mockups, user flow diagrams (.fig files, screenshots).
* (Frontend) Links to PRs/Issues for skeleton pages/components.
* (Backend) Links to PRs/Issues for initial endpoints, link to API documentation.
* (ML) Summary of research, link to dataset or data collection plan.

### Week #3: MVP Development

*Goal: Implement the core functionality of your Minimum Viable Product (MVP).*

#### Tasks:

1. Core Feature Implementation:
    * Frontend and Backend developers collaborate to implement the highest priority features from the backlog.
    * Focus on making at least one end-to-end user journey functional.
    * Implement basic error handling.
    * User authentication/authorization (if critical for MVP).
2. API Integration: Connect frontend components to backend APIs.
3. Data Persistence: Ensure data is being correctly stored and retrieved from the database.
4. ML Model (ML Developers, if applicable):
    * Train an initial version of your model.
    * Develop a simple way to integrate the model's predictions into the backend (e.g., a basic API endpoint).
5. Internal Demo & Feedback: Conduct an internal team demo of the current state. Identify bugs and areas for immediate
   improvement.

#### Deliverables (in Report):

* Description of implemented MVP features and the functional user journey(s).
* Screenshots/GIFs demonstrating the working MVP.
* Links to relevant PRs/Issues for implemented features.
* Updated API documentation.
* (ML) Link to model training code/notebook, any initial model artifacts.
* Notes from internal demo and identified next steps.

### Week #4: Testing, CI/CD & Deployment Setup

*Goal: Ensure quality through testing, automate processes, and prepare for deployment.*

#### Tasks:

1. Test Coverage:
    * Write unit tests for critical backend logic and frontend components.
    * Write integration tests for API endpoints.
    * Aim for basic end-to-end tests for the core user journey.
    * (ML) Implement basic model validation/testing.
2. CI/CD Pipeline Setup:
    * Set up Continuous Integration (CI) to automatically build and run tests on every push/PR to `main`/`develop`
      branches (using GitHub Actions, GitLab CI, etc.).
    * (Bonus: 5 points for Continuous Delivery) Set up Continuous Deployment (CD) to automatically deploy to a staging
      environment upon successful merge to `main`.
3. Environment Setup:
    * Set up a staging environment (e.g., Heroku, AWS EC2, Google App Engine free tier).
    * (If aiming for bonus) Set up a production environment (VDS server).
4. Deployment: Deploy the current version of your application to the staging environment.
5. Public Domain Name (Optional but good practice): If reasonable, acquire and configure a public domain name for your
   staging/production environment.
6. Vibe Check (PMs): Facilitate a team health check. Discuss progress, roadblocks, and team dynamics. Ensure everyone
   feels heard.

#### Deliverables (in Report):

* Summary of testing strategy and types of tests implemented.
* Evidence of test execution (e.g., screenshots of test reports, CI logs). Code coverage report if available.
* Link to CI/CD configuration files (e.g., `.github/workflows/main.yml`).
* Link to the live, deployed application on the staging environment.
* Description of your staging (and production, if applicable) environment setup.
* (PMs) Summary of vibe check discussion and any action items.

### Week #5: Feedback, Iteration & Polishing

Week #5: Feedback, Iteration & Polishing
*Goal: Gather user feedback, iterate on the MVP, and improve overall project quality.*

#### Tasks:

1. Feedback Collection:
    * Conduct usability testing sessions (e.g., with peers, TAs, or a small group of potential users).
    * Share your deployed application and solicit feedback.
2. Feedback Analysis & Prioritization (PMs):
    * Analyze collected feedback.
    * Create new issues/user stories in the backlog for improvements and bug fixes.
    * Prioritize these new tasks with the team.
3. Iteration & Refinement:
    * Implement changes based on feedback (UI/UX improvements, bug fixes, minor feature enhancements).
    * Improve error handling and application stability.
    * Optimize performance where needed.
    * Enhance documentation (README, API docs, inline code comments).
4. ML Model Refinement (ML Developers, if applicable):
    * Iterate on the model based on performance or new data.
    * Explore techniques for improving accuracy, fairness, or efficiency.

#### Deliverables (in Report):

* Summary of feedback collection methods and key findings.
* Link to updated backlog reflecting feedback.
* Description and demonstration (screenshots/GIFs, links to PRs) of implemented improvements and bug fixes.
* Updated link to the deployed application.
* (ML) Summary of model improvements, updated model artifacts.

### Week #6: Final Touches & Presentation Preparation

*Goal: Finalize the project, prepare all deliverables, and craft a compelling presentation.*

#### Tasks:

1. Final Project Polish:
    * Complete any remaining high-priority features or bug fixes.
    * Conduct thorough final testing.
    * Ensure all code is well-commented and clean.
    * Code Freeze: Announce a code freeze date, after which only critical bug fixes are allowed.
2. Documentation Finalization:
    * Ensure `README.md` is comprehensive: project overview, features, tech stack, setup instructions, deployment link.
    * Finalize API documentation.
    * Ensure design documents (Figma) are up to date and reflect the final product.
3. Presentation Preparation:
    * Develop presentation slides covering:
        * Problem Statement & Solution
        * Target Audience
        * Key Features & Technology Stack
        * Live Demo
        * Challenges Faced & Lessons Learned
        * Future Work
        * Team Contributions
    * Assign speaking roles for the presentation.
    * Rehearse the presentation and demo multiple times.

#### Deliverables (in Report):

* Link to the final, deployed version of the project.
* Link to the final code repository state.
* Link to comprehensive final documentation (README, API docs, Figma).
* Draft of presentation slides.
* Plan for the live demo.

### Week #7: Final Presentation & Project Showcase

*Goal: Successfully present your project to TAs and peers.*

#### Tasks:

1. Final Rehearsal: One last run-through of the presentation and demo.
2. Technical Check: Ensure the demo environment and any required software are working perfectly.
3. Deliver Final Presentation:
    * Present your project clearly and confidently.
    * Conduct a smooth live demo of the key functionalities.
    * Be prepared for a Q&A session.

#### Deliverables (Post-Presentation, if required by TAs):

* Final version of presentation slides.
* Link to a recording of the presentation (if applicable).
* Any post-presentation reflections or feedback.