---
title: "Week #6"
---

# **Week #6**

## Links


- **Deployment**: [link](https://open-labs-share.online/)
- **API Docs**: [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/main/services/api-gateway/API_README.md)
- **Design**: [link](https://www.figma.com/design/mvegZwCxX8KHxhtI2PeMHQ/OpenLabsShare?node-id=0-1&t=PUeTUEP2kqgkivvL-1)
- **Repository**: [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/tree/main)
- **Presentation**: [link](https://drive.google.com/file/d/1FqYL6P8XjxFMd0Js4gpTUDguJRbYfAvn/view)

## Final deliverables

### Project overview

Open Labs Share is an innovative educational platform that combines structured learning with academic collaboration, addressing the fragmented nature of educational resources and lack of constructive feedback mechanisms for students and researchers. Our platform bridges the gap between practical learning and academic discourse by creating a dual-environment system that facilitates both guided learning through practical assignments (labs) and open academic collaboration through research publication (articles) and peer review. Also, it supports Marimo, a reactive Python notebook environment for interactive computational education, which allows users to write and execute code in a notebook-like interface to create more interactive and engaging learning experiences. Chat assistant, powered by RAG-based intelligent chat system using FAISS vector storage and BGE embeddings, context-aware responses with memory persistence, and educational content integration, can be accessed by users to get answers to their questions without leaving the platform. The platform is designed to be scalable and modular, allowing for easy integration of new features and services.

The platform solves critical problems in modern education: students struggling to get meaningful feedback on their work early in their careers, early-stage researchers lacking accessible platforms to share knowledge with learners, and the disconnect between theoretical learning and practical application. Our solution provides structured learning paths with practical assignments, comprehensive feedback systems, and tools for educators to guide students effectively.

### Features

**Implemented Core Features:**

- **Authentication & User Management**: Complete JWT-based authentication service with secure session management across all microservices, user registration, and comprehensive profile management.
- **Labs Management System**: Full lab creation, browsing, and submission workflow with file upload capabilities, lab resource management via MinIO storage, and submission tracking with cost-based game-like point system.
- **Search & Discovery**: Advanced search functionality with tag-based filtering, comprehensive and flexible tagging system for content categorization, and efficient content discovery mechanisms.
- **Feedback & Review System**: Complete comment system for detailed discussions, submission feedback workflows, and reviewer assignment logic with notification systems.
- **User Interface & Experience**: Dark/light theme switching with persistent preferences, intuitive navigation with sidebar and header components, search integration across platform, and consistent design system with reusable components.
- **File Storage & Management**: Robust file upload system with MinIO integration, concurrent upload handling, file versioning support, and metadata storage with validation.

**Advanced Features:**

- **ML-Powered Chat Assistant**: RAG-based intelligent chat system using FAISS vector storage and BGE embeddings, context-aware responses with memory persistence, and educational content integration
- **Code Auto-Grading Pipeline**: Automated code evaluation system using fine-tuned Qwen2.5-Coder model, Redis queue-based job processing, and comprehensive assessment rubrics
- **Marimo Integration**: Reactive Python notebook environment for interactive computational education, component independence with session isolation, and stateless architecture for scalability

### Tech stack

**Frontend**
- **UI & Framework:** React, Vite, Tailwind CSS, PostCSS
- **Routing:** React Router DOM

**Backend Microservices**


- **Java (Spring Boot) Services:**
  - **API Gateway:**
    - *Language:* Java, Spring Boot
    - *Communication:* REST (for external API), gRPC (for internal communication)
    - *Tools:* SpringDoc OpenAPI, Lombok, Gradle
  - **Auth Service:**
    - *Language:* Java, Spring Boot, Spring Security
    - *Storage:* PostgreSQL (via Spring Data JPA)
    - *Security:* JWT
    - *Communication:* gRPC (for internal communication)
  - **Users Service:**
    - *Language:* Java, Spring Boot, Spring Security
    - *Storage:* PostgreSQL (via Spring Data JPA)
    - *Communication:* gRPC (for internal communication)
  - **Marimo Manager Service:**
    - *Language:* Java, Spring Boot
    - *Storage:* PostgreSQL, MinIO
    - *Communication:* gRPC

- **Python Services:**
  - **Labs Service:**
    - *Language:* Python 3.12
    - *Storage:* PostgreSQL (via SQLAlchemy), MongoDB, MinIO
    - *Communication:* gRPC (for internal communication)
  - **Articles Service:**
    - *Language:* Python 3.12
    - *Storage:* PostgreSQL (via SQLAlchemy), MinIO
    - *Communication:* gRPC (for internal communication)
  - **ML Service:**
    - *Language:* Python, FastAPI
    - *AI/ML:* Langchain, Langgraph, Huggingface, Groq
    - *Storage:* Qdrant (vector), PostgreSQL
    - *Async:* Celery (message broker)
  - **Marimo Executor Service:**
    - *Language:* Python
    - *Communication:* gRPC

- **Go Service:**
  - **Feedback Service:**
    - *Language:* Go
    - *Storage:* PostgreSQL, MongoDB, MinIO
    - *Communication:* gRPC (for internal communication)

**Databases & Global Storage**
- **Relational:** PostgreSQL
- **Document:** MongoDB
- **Vector:** Qdrant
- **Object Storage:** MinIO
- **Message Broker:** Celery
- **In-Memory Cache:** Redis

**Infrastructure & DevOps**
- **Containerization:** Docker, Docker Compose, Docker Bake
- **CI/CD:** GitHub Actions & GitHub Container Registry
- **Deployment:** Self-hosted runner, Blue/Green Strategy
- **Networking:** NGINX, HAProxy, CloudPub (ngrok alternative)

### Setup instructions

**Prerequisites:**
- Docker and Docker Compose installed
- Git for repository cloning
- Hardware (used for build from zero):
  - Minimal Hardware: ~40GB of disk space
  - Recommended hardware: 8 CPU, 16GB RAM, 40GB of disk space

**Quick Start (Recommended):**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/IU-Capstone-Project-2025/open-labs-share
   cd open-labs-share
   ```

2. **Environment Configuration:**
   ```bash
   cp .env.example .env
   # Configure environment variables for your setup
   ```

3. **Launch Frontend+Backend services with Docker Compose:**
   ```bash
   docker-compose --profile test up -d --build
   ```

4. **Launch ML service with Docker Compose:**
   ```bash
   docker-compose --profile ml up -d --build
   ```
**Important note: these steps may change, since there is 2 days left before meeting with TA at moment of writing this. Actual steps will be updated in the repository `README.md`: [link](https://github.com/IU-Capstone-Project-2025/open-labs-share)**

## Presentation draft

Can be found in the [presentation draft](https://drive.google.com/file/d/1FqYL6P8XjxFMd0Js4gpTUDguJRbYfAvn/view)

# Weekly commitments

## Individual contribution of each participant

- **Kirill Efimovich (PM / DevOps):**

**Kanban board (clickable):** [link](https://github.com/orgs/IU-Capstone-Project-2025/projects/6/views/1) \
**Milestone (clickable):** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/milestone/5) \
**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/255), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/213), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/268), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/254) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/269), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/267), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/241) \
**Summary of TA feedback:** Great impact during previous week, frontend connection needed, also futher work with new features is needed. ML service is not connected as expected and need optimizations. \
**Weekly contribution:** Revised and optimized CI pipelines, stabilized containerization and Green-Blue deployment process, improved documentation, actively participated in the code review process, coordinated team sprint planning based on feedback analysis, wrote comprehensive Week 5 report with detailed technical analysis.

- **Mikhail Trifonov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/247), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/268), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/248) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/270), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/249) \
**Weekly contribution:** Completed full backend and frontend implementation for Marimo service and developed comprehensive frontend integration for Marimo notebooks.
  
- **Nikita Maksimenko (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/268), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/265) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/266) \
**Weekly contribution:** Performed code quality review and security audit for API Gateway, enhanced documentation including deployment guides and environment variable specifications, updated service architecture documentation, and established presentation structure with implementation concepts and design elements.

- **Timur Salakhov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/190), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/190) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/261) \
**Weekly contribution:** Developed comprehensive testing for Articles Service functionality and documented the technical stack for both Articles and Labs Services, ensuring proper integration with the overall system architecture.

- **Ravil Kazeev (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/260), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/268), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/257) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/263) \
**Weekly contribution:** Fixed file upload functionality on both frontend and backend, implemented certificate integration for secure downloads, and made critical fixes to the feedback and labs services to ensure proper file handling and download capabilities.

- **Kirill Shumskiy (ML):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/268), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/256), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/56), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/252) \
**Weekly contribution:** Migrated vector database from FAISS to Qdrant for improved performance, fixed Docker container configurations for ML services, implemented frontend integration for the chat assistant, and performed code refactoring and polishing to enhance overall system stability and maintainability.

- **Aleliya Turushkina (Designer / Frontend):**

**Figma board (clickable):** [link](https://www.figma.com/design/mvegZwCxX8KHxhtI2PeMHQ/OpenLabsShare?node-id=0-1&t=PUeTUEP2kqgkivvL-1) \
**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/206), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/260), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/248), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/268), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/134), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/258), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/271) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/272), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/264), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/263), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/259), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/246), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/245), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/244), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/242) \
**Weekly contribution:** Implemented file download functionality for submissions and feedback, added Marp and LaTeX support on frontend, enhanced image display from assets and URLs, improved error handling for lab/article creation, developed responsive design for registration pages, updated dark theme support, improved frontend documentation, fixed display issues for titles and dates, and added deletion functionality for labs, articles, and submissions.

**More detailed descriptions of services and technical implementations can be found in the project repository [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/tree/main).**

## Plan for Next Week

### Week #7: Final Presentation & Project Showcase

**Tasks:**
- **Presentation preparation:** Finalize the presentation slides and demo environment.
- **Final Rehearsal:** One last run-through of the presentation and demo.
- **Technical Check:** Ensured that the demo environment and any required software are working perfectly.
- **Deliver Final Presentation:**
  - Present our project clearly and confidently.
  - Conduct a smooth live demo of the key functionalities.
  - Be prepared for a Q&A session.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).