---
title: "Week #1"
---

# Week #1

## Project description

### Project name: **InnoSync**

**Code repository**: https://github.com/IU-Capstone-Project-2025/InnoSync

**Problem Statement:**
Currently, students, freelancers, academics, and specialists face challenges in finding relevant project opportunities, assembling teams for their projects, and collaborating effectively with them after finding them. Job and talent searches are often fragmented across different platforms, communication is spread across other tools, and forming a full project team requires juggling between profiles, spreadsheets, and messages. This scattered approach makes the recruitment and collaboration process time-consuming, inefficient, and difficult to manage—especially in an academic or innovation-focused environment.
InnoSync solves this problem by offering a centralized platform where users can either find roles or recruit individuals and teams, with built-in tools for AI-powered matchmaking, team formation, and simplified collaboration, all in one place.

**Detailed description:**
InnoSync is a smart collaboration and talent-matching platform developed for the Innopolis community (for now, we plan to expand to the public in future), designed to simplifie the process of finding jobs, joining projects, and building teams. As a Student/Academic/Specialist/Freelancer, InnoSync allows you to create a detailed profile and browse open opportunities based on your skills and interests. If you have a project idea or a paid job and are looking to recruit, you can create a project and either manually search for talent or use QuickSyncing, our AI-powered auto-matching feature, to assemble an ideal team. The platform supports both individual and team-based recruitment, making it equally useful for hiring one developer or forming an entire project group. Beyond recruitment, InnoSync offers integrated collaboration tools—like group chat and one-on-one messaging—to simplify onboarding, communication, and ongoing teamwork. Unlike generic freelancer platforms, InnoSync is tailored specifically for academic and innovation environments, offering a centralized, efficient, and community-focused space to match, connect, and collaborate.

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| (Lead) Ahmed Baha Eddine Alimi     | @Allimi3 | a.alimi@innopolis.university | [Frontend/DevOps] | Team Management, Frontend & Design Supervision, DevOps |
| Yusuf Abudghafforzoda| @abdugafforzoda | y.abudghafforzoda@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Egor Lazutkin            | @Johnn_u | e.lazutkin@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Anvar Gilmiev            | @glmvai | a.gilmiev@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Asgat Keruly            | @east511 | a.keruly@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Aibek Bakirov | @bakirov817 | a.bakirov@innopolis.university | [DevOps] | Infrastructure Automation, CI/CD Setup, Deployment |
| Gurbanberdi Gulladyyev | @gurbangg | g.gulladyyev@innopolis.university | [ML] | ML Model Research & Development for QuickSyncing |


## Brainstorming

### Ideas during brainstorming

1. **InnoSync (Selected)** – Smart collaboration & team-matching platform for our community
1. **InnoCivic** - A web platform that centralizes public and user-contributed datasets across Russia

### Brief market research / problem validation

**InnoSync (Selected):** We noticed that:
- Existing platforms (LinkedIn, Upwork, Fiverr) aren't tailored for structured project-based recruitment.
- Toptal and other freelancing sites are too skill-focused and lack academic onboarding processes.
- Students and researchers need structured, skill-level-specific recruiting with academic context.
- InnoSync fills these gaps by providing a simple, centralized solution that allows all work to be done in one platform.

**InnoCivic:** We noticed that:
- Existing platforms lack good search, visualization, or user-contributed content..
- No current solution combines official data with community contributions in one place.
- InnoCivic fills this gap with centralized access, modern visualizations, and open collaboration.

**Why we selected InnoSync: We chose InnoSync because it simply addresses a common challenge many of us face, finding work or side projects to learn from, participating in research, or finding teammates/speacilists for paid, passion-driven, or academic projects. We believe InnoSync’s impact will be immediately visible in our community.**

*Interviews with IT specialists asking them questions about their problems with InnoSync Like platforms*
\
**Link:** https://docs.google.com/document/d/1qv_p7PXtwwLyW7-LFDWodbcnnmXI9BD-D75tksvxJgY/edit?tab=t.0#heading=h.5mzoqgecvopb
## Basic requirements

### Target users and their primary needs

1. **Recruitees (Students/Specialists/Academics):**
    - Showcase skills and experience
    - Discover and apply to relevant projects
    - Receive curated project invitations
1. **Recruiters (Team Leads/Project Creators):**
    - Define roles and required skills for a project
    - Discover or auto-match suitable team memberes
    - Use built-in tools to form and manage teams

### User stories

- As a recruiter, I want to create a project and define role needs so that I can recruit the right team.
- As a recruiter, I want to receive automated candidate suggestions (QuickSyncing) so that I can speed up the recruitment process.
- As a recruiter, I want to manage my team and communicate with members directly on the platform so that collaboration is simplifiyed.
- As a recruitee, I want to browse and filter projects based on my interests and skills so that I can find relevant opportunities.
- As a recruitee, I want to communicate with my team members on the platform so that I can collaborate efficiently after joining a project.

### Initial scope

- User authentication and role selection

- Recruiter: project creation, manual search, QuickSyncing

- Recruitee: profile builder, project browser, application management

- Basic chat system for team members

- Frontend and backend integration with basic DevOps pipeline

**User Case Diagram**
![User Case Diagram](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/userdiagram.jpg)

## Tech-stack

- **Frontend:**
  - Tools & Technologies: React, Next.js, TypeScript, Figma
  - Reasons for choice:
    - React for building dynamic and reusable UI components.
    - Next.js for server-side rendering (SSR), better SEO, and fast page loads.
    - TypeScript for type safety and more maintainable, scalable frontend code.
    - Figma for collaborative UI/UX design and prototyping.
- **Backend:**
    - Language & Framework: Java with Spring Boot
    - Reasons for choice:
        - Strong ecosystem and community support.
        - Scalable and well-suited for long-term production systems.
        - Enables rapid development with auto-configuration and starter dependencies.
        - Built-in support for creating secure RESTful APIs (Spring Security).
        - Seamless integration with PostgreSQL for robust data storage and management.
        - Simplified data handling using Spring Data JPA.
        - Well-documented and maintainable architecture.
- **DevOps**
    - Tools & Technologies: Docker, Nginx, Terraform, GitLab CI/CD or GitHub Actions, ELK Stack (Elasticsearch, Logstash, Kibana)
    - Reasons for choice:
        - Docker for consistent containerized deployments across all environments.
        - Nginx as a reliable reverse proxy and load balancer.
        - Terraform for reproducible, code-based infrastructure provisioning.
        - GitHub Actions for automating testing and deployment pipelines.
        - ELK Stack for centralized logging, monitoring, and alerting.
- **Machine Learning**
    - Language & Tools: Python, scikit-learn, PyTorch, HuggingFace (maybe BERT)
    - Reasons for choice:
        - PyTorch is a good and flexible framework for ML models and will be used for hybrid recommender
        - Scikit-learn will be used for tranditional ML 
        - HuggingFace will be used for pre-trained NLP models for skill/resume parsing


# Weekly commitments

## Individual contribution of each participant

- **Ahmed Baha Eddine Alimi:**: Project planning and team coordination, Report, frontend and design stack research, frontend testing and api trials.
\
https://github.com/IU-Capstone-Project-2025/InnoSync/commit/0f145b6cc8bc54bbd59c22152737fe233e455218

- **Yusuf Abudghafforzoda:**: Backend Initialization, backend stack research.
\
https://github.com/IU-Capstone-Project-2025/InnoSync/commit/614e2eda694b9ac07ede1e47913733304d3bc3fd
- **Egor Lazutkin:**: Backend stack research, user study and interviews.
https://docs.google.com/document/d/1qv_p7PXtwwLyW7-LFDWodbcnnmXI9BD-D75tksvxJgY/edit?tab=t.0#heading=h.5mzoqgecvopb
- **Anvar Gilmiev:**: Frontend stack research, writing readme/documentation.
\
https://github.com/IU-Capstone-Project-2025/InnoSync/commit/848a5489267836d61965bb6629ec8f782c20b686
- **Asgat Keruly:**: Frontend stack research, frontend initialiazation.
\
https://github.com/IU-Capstone-Project-2025/InnoSync/commit/be70bb246944ebe0df428e2d9263618d50b6c9a8
- **Aibek Bakirov**: DevOps Tech-stack research, Frontend dockerization.
\
https://github.com/IU-Capstone-Project-2025/InnoSync/commit/513ac2cc918c6751167447a52108721accd9af98
- **Gurbanberdi Gulladyyev**: Researched ML tech-stack and started outlining the ML approach for QuickSyncing, did the user case diagram.
\
https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/userdiagram.jpg
## Confirmation of the code's operability

We confirm that the code in the main branch:
- [**✔**] In working condition.
- [**✔**] Run via docker-compose (or another alternative described in the `README.md`)