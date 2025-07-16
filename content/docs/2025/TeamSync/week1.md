# Week 1

# Project description

---

**Project name:** TeamSync

**Code repository:** [link](https://github.com/IU-Capstone-Project-2025/team-sync/tree/main)

**TeamSync** is a smart university team-matching platform that helps students quickly and effectively find teammates for academic projects. It streamlines the team formation process through AI-based matchmaking, smart user and project profiles.

# Team

---

| Team member | Telegram alias | Innopolis Email | Responcibilities |
| --- | --- | --- | --- |
| Diana MInnakhmetova (Lead) | @diana_minn | d.minnakhmetova@innopolis.university | Product management, design, Report writing |
| Danis Sharafiev | @HarneMer | d.sharafiev@innopolis.university | ML + MLOps |
| Daria Alexandrova | @ae_quor | d.alexandrova@innopolis.university | Frontend |
| Stepan Dementev | @dementevssstepan | s.dementev@innopolis.university | Backend + DevOps |
| Elizaveta Zagurskih | @wkwthigo | e.zagurskih@innopolis.university | Backend |
| Kamilya Shakirova | @hugecatwithacheburek | k.shakirova@innopolis.university | ML |

# Brainstorming

---

### **Ideas during brainstorming**

| Rank | Idea |
| --- | --- |
| **1** | Smart university team-matching platform that helps students quickly and effectively find teammates for academic projects |
| **2** | Dynamic resource allocation between services by means of time series. For example, allocate a little more RAM to one or another service, give more cores, etc. Formalize as SaaS |
| **3** | AI-powered habit tracking application designed to help users develop and maintain positive habits through personalized recommendations and consistent tracking. |

### Problem validation

**1. Smart University Team-Matching Platform**

**Problem**: Students spend 5–10 hours forming teams manually, often leading to mismatches and delays.

**Validation**:

- Most use unstructured *Telegram* chats, *spreadsheets*. One of the more or less same sevice is already not working ([Pet-Plat](https://www.notion.so/48a5ad2acca54b06a08cd8edd14307a3?pvs=21))
- Professors report frequent issues with unbalanced teams.

**2. Dynamic Resource Allocation SaaS**

**Problem**: Cloud services often over- or under-use resources due to static allocation.

**Validation**:

- Time-series-based autoscaling is complex and costly to configure manually.
- Existing tools like *Cast.ai* are powerful but too advanced for small teams.

**3. AI-Powered Habit Tracking App**

**Problem**: Current habit trackers lack personalization, causing low long-term engagement.

**Validation**:

- Popular apps use generic reminders, not behavior-based adaptation.
- Users want smarter, context-aware support.

# Basic Requirements

---

## Problem Statement

Students of Innopolis University currently face the inefficiencies and time-consuming manual efforts when forming teams for academic projects, particularly during Capstone and elective-based collaborations. This results in suboptimal groups and delayed project starts.

## Solution

**TeamSync** aims to improve the quality and balance of student teams by offering a data-driven, user-friendly experience for discovering, evaluating, and matching with potential teammates.

## Target Users

**Primary Customers:** Innopolis University or other organizations.

**Primary Users:** Students of Innopolis University.

**Secondary Users:** Professors.

## User Stories

1. As a student, I want to create a personal profile with my skills, interests, and past projects so that I can be discovered by project creators or teammates.
2. As a student, I want to post a new project with a description and required skills, so that I can find teammates who match my needs.
3. As a student, I want to receive AI-generated teammate recommendations based on my skills and preferences, so that I can build a balanced and effective team faster.
4. As a student, I want to apply to projects that match my interests, so that I can participate in projects relevant to my skills and goals.
5. As a project owner, I want to accept or reject team applications and manage my team members, so that I can control who joins my project and maintain a good team structure.
6. As a student, I want to see suggestions and filters when browsing projects (similarity), so that I can efficiently choose which projects to join.
7. As a professor, I want to make a page only for my course, so that I can manage the team formation between my students.


## **Main Functionalities**

---

### **Smart Profiles**

A system that allows students to create detailed profiles with skills, interests, availability, and academic background.

- Students can input relevant information including tech stack, preferred project types, and availability.
- Students can make tags for better search and matching.
- The system supports real-time updates as students gain experience or complete courses.

### **Project Hub**

A centralized interface to browse, create, and manage project listings.

- Students can post project ideas with descriptions, required roles, and deadlines.
- Other users can browse available projects, filter by tags or requirements, and submit join requests.
- Each project shows team composition, required skills, and current progress status.

### **AI Matchmaking**

An intelligent recommendation engine for finding optimal team compositions.

- Recommends teammates or projects.
- Search engine.

### **Team Management Tools**

Features to organize and manage project teams effectively.

- Project owners can accept/reject applications and manage current team members.
- Team dashboards display role distribution, availability conflicts, and overall skill coverage.
- Notification system for team activity and status updates.

### **Analytics for Instructors**

 A dashboard for faculty to monitor team formation patterns.

- Includes ungrouped students, skill demand gaps, and team distributions.
- Helps professors support team-building proactively.

### **Search & Tagging System**

Enhanced discoverability through structured filtering and semantic tagging.

- Projects and profiles are enriched with tags based on content.
- Students can search based on interests, tools, tech stacks, or availability windows.
- Search results are ranked by relevance and user preferences.

### **User Feedback & Improvement Loop**

- Users can rate or flag recommendations to improve accuracy.
- Users can share feedback to the telegram of this project (will be created soon)

## System Architecture

---

Link to the Figma Board with system architecture:

[https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/Untitled?node-id=0-1&t=GFqAGJxXii04Q0gK-1](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/Untitled?node-id=0-1&t=GFqAGJxXii04Q0gK-1)

## **Initial Scope (MVP)**

---

| **IN Scope (W1–W3)** | **OUT (Post-MVP)** |
| --- | --- |
| User auth (signup/login) | Team invitation/management |
| Profile creation (skills, availability) | Profile dashboard |
| Project creation  | Advanced analytics dashboard |
| Search engine  |  |
| Basic recommendation system | Advanced recommendation system |

## Tech Stack

---

|  | **Choice** | **Justification** |
| --- | --- | --- |
| **Frontend** | React | For building dynamic and high-performance user interfaces and server-side rendering capabilities. |
|  | TypeScript | A strongly typed programming language that builds on JavaScript, providing better tooling at any scale. |
|  | Tailwind CSS | A utility-first CSS framework for rapid UI development with consistent and responsive design. |
| **Backend** | Java/Spring Boot | Robust REST APIs, team expertise |
| **Database** | PostgreSQL | ACID compliance for user/project data |
|  | Redis | Fast session/matching-cache access |
| **ML** | Python  | For its simplicity and extensive libraries for data processing and machine learning. |
|  | Airflow | Pipeline orchestration |
| **Infra** | Docker + Docker Compose | Environment consistency, TA reproducibility |
|  | GitHub Actions (CI/CD) | Automated testing/deployment |

## Individual commitments

---


| Team member | Telegram alias | Contribution |
| --- | --- | --- |
| Diana MInnakhmetova (Lead) | @diana_minn | Wrote report, hold 3 meetings, [organized workflow in Jira](https://team-sync-capstone.atlassian.net/jira/software/projects/TS/boards/1?atlOrigin=eyJpIjoiYmI0NWVhYzIzYjRhNGU0Nzg1MmFiOThhMzYzYTEzMjYiLCJwIjoiaiJ9) and [Figma, made mind map and user flow,](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=gQIeFCN7V1ofyRcI-1) [wrote README](https://github.com/IU-Capstone-Project-2025/team-sync/commit/9e7b52a1551b2697ddc29238f3538a83350073c2), [made logo and design](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=XYQ72DvnYNk9TxrL-1) |
| Danis Sharafiev | @HarneMer | [Made system architecture](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=gQIeFCN7V1ofyRcI-1), [helped with initializing ML](https://github.com/IU-Capstone-Project-2025/team-sync/commit/94e3cf517f0cf25bcac11e3f596be86ef9bb5bb6) |
| Daria Alexandrova | @ae_quor | [Initialized basic Frontend](https://github.com/IU-Capstone-Project-2025/team-sync/commit/17e62f6f13d34932597a383923279f8b7c340848), [made design](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=XYQ72DvnYNk9TxrL-1) |
| Stepan Dementev | @dementevssstepan | [Organised GitHub workflow](https://github.com/IU-Capstone-Project-2025/team-sync/commit/41e17628b54ae0f896ccb300402e758e24961f62), [helped with system architecture,](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/Untitled?node-id=0-1&t=GFqAGJxXii04Q0gK-1) [made Docker compose,](https://github.com/IU-Capstone-Project-2025/team-sync/commit/dc7206eb6653d517da876229f6edb5c81cc2f3a3) [initialized basic backend](https://github.com/IU-Capstone-Project-2025/team-sync/commit/2e6e3143c35df5956edc7063da050345889d61ec) |
| Elizaveta Zagurskih | @wkwthigo | [Made ERD diagram](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=gQIeFCN7V1ofyRcI-1), [Initialized basic backend](https://github.com/IU-Capstone-Project-2025/team-sync/commit/2e6e3143c35df5956edc7063da050345889d61ec) |
| Kamilya Shakirova | @hugecatwithacheburek | [Initialized basic ML](https://github.com/IU-Capstone-Project-2025/team-sync/commit/94e3cf517f0cf25bcac11e3f596be86ef9bb5bb6) |

# Links

---

- [Jira](https://team-sync-capstone.atlassian.net/jira/software/projects/TS/boards/1?atlOrigin=eyJpIjoiYmI0NWVhYzIzYjRhNGU0Nzg1MmFiOThhMzYzYTEzMjYiLCJwIjoiaiJ9) (for Backlog)
- [Figma Board (mind map and architecture)](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/Untitled?node-id=0-1&t=GFqAGJxXii04Q0gK-1)
- [GitHub](https://github.com/IU-Capstone-Project-2025/team-sync/tree/main)
- [Notion Organization page](https://www.notion.so/TeamSync-209c1c5fc56980deaf6ddbe76a41b803?pvs=21)
- [Figma Design](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=XYQ72DvnYNk9TxrL-1)

### **Confirmation of the code's operability**

We confirm that the code in the main branch:

- [ ]  In working condition.
- [ ]  Run via docker-compose (or another alternative described in the `README.md`).