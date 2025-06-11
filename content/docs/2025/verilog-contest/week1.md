---
title: "Week #1"
---

# Week #1

## Project description

### Project name: _Verilog contest system_

**Code repository**: https://github.com/IU-Capstone-Project-2025/verilog-contest

_A contest platform for practicing digital design using hardware description languages, allowing students to solve problems by writing and testing code in a sandboxed environment with automated verification._

### **Team Members**

| Team Member        | Telegram Alias | Email Address                    | Track               | Responsibilities                                                              |
| ------------------ | -------------- | -------------------------------- | ------------------- | ----------------------------------------------------------------------------- |
| Mikhail Panteleev  | @polinanime    | m.panteleev@innopolis.university | Fullstack           | Repository initialization, backend skeleton, frontend development             |
| Vladislav Merkulov | @skibidivladik | v.merkulov@innopolis.university  | Backend             | Backend implementation                                                        |
| Aleksei Fominykh   | @Dangeowbsjw   | a.fominykh@innopolis.university  | DevOps              | Deploy system monitoring, deploy Kubernetes, conterezation                    |
| Sofia Kulagina     | @sofiakulagina | s.kulagina@innopolis.university  | DevOps              | Setting up Dockerfiles, CI/CD                                                 |
| Diana Yakupova     | @dianaia       | d.yakupova@innopolis.university  | Product/Frontend/QA | Technical documentation, reports, menegment, testing and frontend development |

## Brainstorming

### Ideas during brainstorming

**1. Verilog contest system** is a simple contest system where students solve Verilog problems in a sandboxed environment with auto-grading.

**2. Personal drink system** is a mobile app + IoT device where users get recommendations about drinks based on their history, share recipes, and the machine doses ingredients precisely.

**3. Gym tracker** is an app that tracks gym payments and visits, reminds you if you skip, shows a mini calendar, logs calories, and uses AI to tailor workout plans to your goals and fitness level.

### Problem validation for verilog contest system

**The problem**:

- Students need better tools to practice Verilog
- Teachers need an automatic checking for assignments
- Companies need tests for job candidates
- Current tools don't have contest features for Verilog practice
- Verilog is hard to learn without practice

## Basic requirements

### Target users and their primary needs

- **Students**: Practice problems, instant feedback
- **Teachers**: Create contests, see results
- **HR**: Test job candidates, has teacher's features
- **Admins**: Manage the system

### User stories

- As an Instructor, I want to upload Verilog tasks and associated testbenches so participants can submit and validate their designs.

- As a Student, I want to see simulation results and logs immediately after submission to debug my code.

- As an HR Specialist, I want to export contest results to compare candidate performance.

### Initial scope

- User accounts with roles
- Create and run contests
- Submit and check Verilog code
- View results and scores
- Basic leaderboard

## Tech-stack

| Category                   | Technologies                                            |
| -------------------------- | ------------------------------------------------------- |
| **Languages**              | Go (backend), TypeScript (frontend)                     |
| **Framework**              | Fiber (REST & RPC), React                               |
| **Auth & Authorization**   | Supabase Auth (GoTrue, JWT), Casbin (RBAC/ABAC)         |
| **Databases & Storage**    | PostgreSQL, MinIO, Redis                                |
| **Core Libraries & Tools** | GORM (ORM), Asynq (task queue), Viper (config), Swagger |
| **Monitoring & Logging**   | OpenTelemetry, Zap, GoAdmin                             |

## _Something else you want to add_

- **Specifications**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/specifications.md

- **List of links related to the project**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/related-materials.md

- **User flow**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/user-flow.png

# Weekly commitments

## Individual contribution of each participant

| Team Member            | Week #1 Contributions                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| **Mikhail Panteleev**  | Initialized GitHub repo, structured folders in repo, system design.                        |
| **Vladislav Merkulov** | Hard thinking about ideas and stack, exploring backend technologies.                       |
| **Aleksei Fominykh**   | System design, hard thinking about implementation.                                         |
| **Sofia Kulagina**     | Hard thinking about ideas and stack, mapped user-flow, exploring technologies.             |
| **Diana Yakupova**     | Researching an idea, problem, thinking through details, reporting and organizing teamwork. |

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [ ] In working condition.
- [ ] Run via docker-compose.
