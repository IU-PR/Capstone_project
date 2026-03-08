---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *Vanguard*

**Code repository**: https://github.com/IU-Capstone-Project-2025/Vanguard

*Put here a detailed description of your project and your Problem Statement*

### **Team Members**

| Team Member            | Telegram Alias  | Email Address                      | Track           | Responsibilities   |
| ---------------------- | --------------- | ---------------------------------- | --------------- | ------------------ |
| Ramazan Nazmiev (Lead) | @ssstaticmethod | r.nazmiev@innopolis.university     | Backend         | [Responsibilities] |
| Niyaz Gubaidullin      | @NetOtveto      | n.gubaidullin@innopolis.university | Backend         | [Responsibilities] |
| Nurmukhammet Adagamov  | @selnastol      | n.adagamov@innopolis.university    | Backend/DevOps  | [Responsibilities] |
| Ramil Aminov           | @kolsmer        | r.aminov@innopolis.university      | Frontend        | [Responsibilities] |
| Dmitriy Lukiyanov      | @hntlvr         | d.lukiyanov@innopolis.university   | Frontend/Design | [Responsibilities] |

## Brainstorming

### Ideas during brainstorming

#### 1. Kahoot Alternative

A real-time quiz and polling platform for interactive classrooms, corporate training, or events.  
**Features:** Live quiz sessions, leaderboards, customizable questions, real-time feedback.  
**Why:** Familiar format, clear user base, strong engagement potential.

---

#### 2. No-Code API Generator

A visual tool for generating RESTful APIs from a database schema or config file—no coding required.  
**Features:** CRUD generation, authentication support, exportable OpenAPI spec.  
**Why:** Solves a real pain point for non-developers and rapid prototyping.

---

#### 3. URL Shortener with Analytics

A minimalistic URL shortener with added analytics for tracking usage and behavior.  
**Features:** Short URL creation, click tracking, geolocation, referral source.  
**Why:** Good scope for MVP; useful for marketing and content tracking.

---

#### 4. Personal Task Manager with Kanban Board

A task management system with Kanban interface for individuals or small teams.  
**Features:** Drag-and-drop tasks, deadlines, priorities, tags.  
**Why:** Highly relatable, strong UX focus, potential for expansion (e.g., reminders, calendar view).

---

#### 5. Freelance Marketplace

A platform connecting freelancers and clients for short-term gigs or long-term projects.  
**Features:** User profiles, job posting, bidding system, chat.  
**Why:** Ambitious and complex, great challenge but requires more time and planning.

---

### Brief market research / problem validation

#### Kahoot Alternative

**Problem:**  
Kahoot is a popular platform for live quizzes and interactive learning, but it is currently not available in Russia. This creates a gap for educators, trainers, and event organizers who need similar tools for engagement and assessment.

**Market Signals:**  

- High demand for interactive quiz tools in education and corporate training.  
- Alternative platforms (e.g., Quizizz, Mentimeter) exist but may also have access or pricing limitations.  
- Russian users are actively searching for local or open-source alternatives.

**Conclusion:**  
There's a clear opportunity to build a Kahoot-like tool tailored for the Russian-speaking market with full accessibility and localization.

## Basic requirements

### Target users and their primary needs

- **School teachers** — Need engaging tools for classroom quizzes and student feedback.
- **University lecturers** — Want quick polling and assessment during lectures.
- **Corporate trainers** — Require interactive tools for employee learning sessions.
- **Event hosts (as InnoQuiz club's events)** — Use quizzes to energize and engage audiences.

##### Primary needs:

- Ability to create and host live quizzes easily.

- Simple and fast participation for users, as well as fast connections to the room.

- Real-time leaderboard and results display.

- Support for Russian language and availability in Russia.

### User stories

1. **As a teacher**, I want to create a quiz with multiple-choice questions so that I can assess my students interactively.  
2. **As a student**, I want to join a quiz via a simple code so that I can participate without needing to register.  
3. **As a trainer**, I want to see real-time responses so that I can adapt my session accordingly.  
4. **As an event host**, I want to display a leaderboard after each round so that the audience stays engaged, maintaining the competition atmosphere.  
5. **As an educator in Russia**, I want access to a quiz platform without VPN so that I can use it in class smoothly.

### Initial scope

**IN for MVP:**

- Quiz creation
- Game lobby with join code
- Basic admin UI to manage quizzes
- Player UI with question view and answer buttons
- Dockerized deployment

**OUT for MVP:**

- Real-time answer tracking and leaderboard
- User registration and login
- Analytics dashboard
- Timer-based scoring
- Mobile app (only responsive web)
- Russian language support

## Tech-stack

**Frontend:**

- **React + Next.js** — For building a modern, server-rendered web interface with good SEO and performance.
  
  

**Backend:**

- **Golang** — For performance-critical components, such as handling real-time connections.
- **FastAPI (Python)** 
- **gPRC** — To divide a platform on microservices and effectively communicate throug each other. 

**Database:**

- **MongoDB** — Flexible document-based database suitable for storing quizzes, users, and results.

**DevOps & Deployment:**

- **Docker** — To containerize all components for consistent development and deployment.
- **Docker Compose** — To orchestrate frontend, backend, and database services locally and in staging.
- **GitHub Actions** — For automated CI/CD pipelines.

# Weekly commitments

## Individual contribution of each participant

##### Ramazan Nazmiev:

- [Initialized](https://github.com/IU-Capstone-Project-2025/Vanguard/commit/69a23101a1a16d595971caa7570cd2a6cc5c6d5c) the main branch of the repo with `.gitignore` and `README.md`.

- [Added](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/5) the enter point of the Go-backend part.

- Wrote the report.
  
  

##### Niyaz Gubaidullin:

* [Added](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/1) shared models for go-backend part: structures Admin and User.
  
  

##### Nurmukhammet Adagamov:

* [Initiated](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/2) the structure of python-backend part by configuring `FastAPI` and configured `Dockerfile` for it.

* 

##### Ramil Aminov:

* [Added](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/7) boilerplate code for methods for Admin and User structure, responsible for joining and creating the game 
  
  

##### Dmitriy Lukiyanov:

* [Created](https://www.figma.com/design/D82E6kH1Kquc3ImEO8IHto/InnoQuiz?node-id=0-1&p=f) the UI of several web-site pages.

* [Initialized](https://github.com/IU-Capstone-Project-2025/Vanguard/pull/6) the fronted-part folders structure and essential files and configs.
  
  

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
