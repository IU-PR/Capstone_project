---
title: "Week #1"
---

# Week #1

## Project description

### Project name: ProjectOR

**Code repository**: https://github.com/IU-Capstone-Project-2025/ProjectOR

This platform allows creators to post startup ideas, developers to explore and join projects, and teams to collaborate
efficiently. It also features a "startup graveyard" to document failed ventures, providing valuable insights for future
innovators.

### **Team Members**

| Team Member            | Telegram Alias | Email Address                    | Track           | Responsibilities                                                    |
|------------------------|----------------|----------------------------------|-----------------|---------------------------------------------------------------------|
| Nikita Timofeev (Lead) | @morisummer    | n.timofeev@innopolis.university  | Frontend        | Develop UI, integrate APIs, design,                                 |
| Almaz Andukov          | @andiazdi      | al.andukov@innopolis.university  | Backend         | Build APIs, manage databases, ensure security                       |
| Kirill Karsakov        | @th1ef0        | k.karsakov@innopolis.university  | Project Manager | Plan and track project progress, manage team                        |
| Timur Nabiullin        | @turbochelik   | t.nabiullin@innopolis.university | DevOps          | Set up CI/CD, automate deployments, monitor infrastructure, testing |

## Brainstorming

### Ideas during brainstorming

1. **Project Matchmaking System**
Automatically recommend projects to developers based on skills, interests, and availability.

2. **Skill Badging & Profile Verification**
Allow users to earn badges for specific skills and verify profiles to build trust within the community.

3. **Startup Graveyard with Analytics**
Analyze reasons for project failures (e.g., lack of funding, team issues, market mismatch) to help others avoid common pitfalls.

4. **Idea Validation Tool**
Enable users to vote, comment, and provide feedback on startup ideas to quickly gauge market interest.

5. **Collaborative Task Boards**
Integrated Kanban boards or task management tools for seamless team collaboration within the platform.

### Brief market research / problem validation

1. **Project Matchmaking System**
    - Platforms like GitHub, Indie Hackers, and AngelList allow developers to discover projects, but lack tailored, skill-based matchmaking.
    - Competitors focus mainly on job placement, not on passion projects or early-stage startups.
2.  **Startup Graveyard with Analytics**
    - The failure rate for startups remains high (~90%), yet there is limited structured learning from these failures in most startup platforms.
    - Aspiring entrepreneurs actively seek real failure stories to avoid common mistakes.


## Basic requirements

### Target users and their primary needs

- Startup Founders
Need: Find skilled developers, validate ideas, document startup journey.

- Developers
Need: Discover interesting projects, join meaningful teams, build portfolio.

- Entrepreneurs / Innovators
Need: Learn from failed startups, avoid common mistakes, get inspiration.

### User stories

- _As a startup founder_, I want to post my project idea so I can attract developers and collaborators.

- _As a developer_, I want to browse and filter projects based on my skills and interests so I can join relevant teams.

- _As a founder or team member_, I want to track project progress and share public roadmaps to increase transparency.

- _As a user_, I want to read and contribute to the startup graveyard to learn from past failures.

### Initial scope

- User authentication and profile creation

- Posting and browsing startup ideas

- Basic project matchmaking (filter by skills, interests)

- Startup graveyard with submission and browsing functionality

## Tech-stack

Frontend: Svelte, TypeScript, pnpm, Vite, shadcn/ui, Tailwind CSS
Backend: Python, uv, FastAPI, SQLAlchemy, Pydantic
Database: PostgreSQL, Redis
DevOps: Docker, GitHub Actions (for CI/CD), k8s

# Weekly commitments

## Individual contribution of each participant

- Almaz Andukov:
Prepared basic structure and boilerplate of the backend project; create a clean architecture layout for the API; created health-check endpoint

[backend boilerplate commit](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/9)

- Timur Nabiullin:
Configured build adapter for svelte; Created nginx configuration; Created Dockerfile for frontend; Created Dockerfile for backend; Created docker compose file; Ensured the boilerplate is runnable; Tested the integration

[Deploy commit](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/12)

- Nikita Timofeev:
Prepared basic structure and boilerplate of the frontend project; configured prettier, eslint, shadcn/ui; added button component and basic page

[Frontend boilerplate commit](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/10)

[Initial repository structure commit](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/2)

- Kirill Karsakov:

Created task board; Created weekly tasks and distributed them among all participants; Conducted research; Defined the initial project scope;  Drafted 3–5 high-level user stories; Wrote the project report

[report images commit](https://github.com/IU-Capstone-Project-2025/ProjectOR/pull/11)

![task_board](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/images/photo_2025-06-11_21-54-42.jpg?raw=true)

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
