---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

As a Team Seeker, I want to see only high-quality and vetted projects, so I can avoid wasting time on low-effort posts.
**Acceptance Criteria**: Content moderation, rating system, reporting feature.

As an Idea Founder, I want a space to discuss and refine my idea with potential team members, so I can better evaluate whether to collaborate with them.
**Acceptance Criteria**: Built-in chat or forum for idea discussion.

As a Developer, I want a search tool with advanced filters (e.g., tech stack), so I can find projects efficiently.
**Acceptance Criteria**: Customizable filters, saved search preferences.

As a Recruiter for my project, I want to filter applicants by skills, so I can ensure qualified team members join.
**Acceptance Criteria**: Skill-based filtering.

As someone unsure how to start my idea, I want templates or guides for pitching my idea or recruiting a team, so I can reduce uncertainty.
**Acceptance Criteria**: Step-by-step onboarding, example project pitches, clear and simple instructions for beginners.

As a founder, I want to create a public roadmap with milestones (e.g., MVP by Q3), so potential collaborators see progress.
**Acceptance Criteria**: Timeline editor, Option to mark milestones as "completed."

As a reader, I want to filter graveyard posts by industry/failure reason (e.g., "ran out of funding," "poor marketing"), so I find relevant cases.
**Acceptance Criteria**: Filter by tags like "failure reason" or "year."

As a founder, I want to create a structured project post with required fields (title, description, tech stack, roles needed), so my idea is clear and appealing.
**Acceptance Criteria**: Form includes mandatory fields (title, description, skills needed), preview option before posting.

## Idea collaboration survey

### How often do you look for new projects or ideas to work on?

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/survey_results/photo_1_2025-06-18_22-55-43.jpg?raw=true)

### Where do you typically search for projects or teams to join?

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/survey_results/photo_7_2025-06-18_22-55-43.jpg?raw=true)

### What’s the biggest pain point when searching for projects/teams?


![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/survey_results/photo_6_2025-06-18_22-55-43.jpg?raw=true)

### Have you ever had an idea you wanted to execute but lacked a team?

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/survey_results/photo_4_2025-06-18_22-55-43.jpg?raw=true)

### What matters most when recruiting a team for your idea?

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/survey_results/photo_2_2025-06-18_22-55-43.jpg?raw=true)

### What discourages you from joining startups? 

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/survey_results/photo_5_2025-06-18_22-55-43.jpg?raw=true)

### Which features would be most valuable in finding projects to join?

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/survey_results/photo_3_2025-06-18_22-55-43.jpg?raw=true)

### Prioritized backlog

[Task board](https://github.com/orgs/IU-Capstone-Project-2025/projects/8)

## Project specific progress

### Frontend

#### New components

Implemented several new components in the frontend, which are essential for the user interface. These components
include:

- Button component
  ![Button component](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/components/button.png?raw=true)
- Input component
  ![Input component](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/components/input.png?raw=true)
- Card component
  ![Card component](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/components/card.png?raw=true)
- Label component
  ![Label component](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/components/label.png?raw=true)
- Skeleton component
  ![Skeleton component](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/components/skeleton.png?raw=true)
- Avatar component
  ![Avatar component](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/components/avatar.png?raw=true)

#### New pages

Implemented following pages in the frontend:

- Sign Up page
  ![Sign Up page](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/pages/register.png?raw=true)
- Sign In page
  ![Sign In page](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/pages/login.png?raw=true)
- Demo main page with skeleton projects
  ![Demo main page](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/pages/demo_main_page.png?raw=true)

#### Routing

Implemented routing in the frontend using Svelte Router. This allows users to navigate between different pages of the
application seamlessly

### Backend

[Add endpoints for project and add create project model with migrations](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/42)

### Design

[Figma design PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/43)

[Figma file](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/low-fi.fig)

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/low-fi.png?raw=true)

#### User flows

##### Developer

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/user-flows/developer.png?raw=true)

##### Founder

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/user-flows/founder_user.png?raw=true)

##### Investor

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/user-flows/investor.png?raw=true)

##### Universal user

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/user-flows/universal_user.png?raw=true)

# Weekly commitments

## Individual contribution of each participant

**Timur Nabiullin**: Conducted survey about people experience in finding or creating projects; expanded and added user stories based on the survey

**Almaz Andukov**: Reorganized the backend structure and implemented API endpoints with Pydantic schemas for project management; added a Project model to represent the corresponding database table; integrated Alembic for database migrations; Updated docker-compose to include a PostgreSQL service and automatically apply migrations on startup ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/42))

**Nikita Timofeev**: 
- Added input, card, input, avatar, skeleton components ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/45))
- Added login page ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/45))
- Added register page ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/45))
- Added root demo page with components present ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/45))
- Add main projects explore skeleton page ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/45))
- Added routing ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/45))
- Developed basic user flow diagrams for key interactions ([PR](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/46), [Figma link](https://www.figma.com/board/ir1uLWIdiewKIPPVO3TMtn/ProjectOR-User-Flows?node-id=0-1&t=v5rlwgM4sItXTl0W-1))

**Kirill Karsakov**: Created an initial backlog with prioritized features/tasks; thought about questions for the survey; wrote the project report

## Plan for Next Week

1. Core Feature Implementation:
    * Frontend and Backend developers collaborate to implement the highest priority features from the backlog.
    * Focus on making at least one end-to-end user journey functional.
    * Implement basic error handling.
    * User authentication/authorization.
2. API Integration: Connect frontend components to backend APIs.
3. Data Persistence: Ensure data is being correctly stored and retrieved from the database.
4. Internal Demo & Feedback: Conduct an internal team demo of the current state. Identify bugs and areas for immediate
   improvement.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).