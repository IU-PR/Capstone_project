---
title: "Week #4"
---

# **Week #4**


### Project name: **InnoSync**

**Code repository**: https://github.com/IU-Capstone-Project-2025/InnoSync

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| (Lead) Ahmed Baha Eddine Alimi     | @Allimi3 | a.alimi@innopolis.university | [Management/ProductDesign] | Team Management, Frontend & Design Supervision|
| Yusuf Abudghafforzoda| @abdugafforzoda | y.abudghafforzoda@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Egor Lazutkin            | @Johnn_u | e.lazutkin@innopolis.university | [CustDev] | Customer Development & Customer Relation |
| Anvar Gilmiev            | @glmvai | a.gilmiev@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Asgat Keruly            | @east511 | a.keruly@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Aibek Bakirov | @bakirov817 | a.bakirov@innopolis.university | [DevOps] | Infrastructure Automation, CI/CD Setup, Deployment |
| Gurbanberdi Gulladyyev | @gurbangg | g.gulladyyev@innopolis.university | [ML] | ML Model Research & Development for QuickSyncing |


### 🎥 New MVP Demonstration
![Product Testing](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/6fcf3c669b2fea1a6967e7034a55bf4383d683ff/assets/Week4_Capstone.gif)
#### 📁 Google Drive Link to MVP Demo Video
[Drive Link](https://drive.google.com/drive/folders/1VZAhBosnuWQwqZfdrPHZ1adBGzNMDaEO?usp=sharing)
## 🧪 Testing and QA

### Summary of testing strategy and types of tests implemented

Our testing strategy focuses on ensuring functionality at both the unit and integration levels. This week, we implemented the following:

- **Unit Tests:**  
  - Developed using **JUnit 5** to validate isolated components and business logic.  
  - Covered core methods in services and utility classes.

- **Integration Tests:**  
  - Used **Mockito** to mock dependencies where needed.  
  - Verified end-to-end behavior between services, repositories, and the database layer.

- **Test Coverage Strategy:**  
  - Focused on critical logic paths and potential edge cases.  
  - Aimed to detect regressions early during development and integration phases.

- **Tools used:**  
  - `JUnit 5` for testing framework  
  - `Mockito` for mocking and verifying interactions  
  - No static analysis tools were used during this phase.


### Evidence of test execution
## 1. Test Report Structure
![Surefire Test Report Structure](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/1d6743832ddca2c1f7f2640c8720356df5e3f0a7/assets/photo_2025-07-02_22-39-57.jpg)



This image displays the Surefire test report structure within the project directory. It showcases test class coverage across the following layers:

- **Service layer**
- **Controller layer**
- **Repository layer**
- **Security layer**

This layout demonstrates comprehensive modular testing implemented using **JUnit**.

---

## 2. Detailed Execution Logs of Service Tests

![Service Tests Execution Logs](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/1d6743832ddca2c1f7f2640c8720356df5e3f0a7/assets/photo_2025-07-02_22-39-51.jpg)

This screenshot shows detailed execution logs for individual service tests, including but not limited to:

- `JwtUtilTest`
- `ProfileServiceTest`
- `RefreshTokenServiceTest`

All tests have executed successfully with **zero failures or errors**, indicating the correctness and stability of the core business logic.

---

## 3. Test Summary
![Test Summary](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/1d6743832ddca2c1f7f2640c8720356df5e3f0a7/assets/photo_2025-07-02_19-19-49.jpg)

This final image confirms:

- Completion of **164 test cases**
- **No failures, errors, or skipped tests**

## Code Coverage Report

For a detailed view of the code coverage, please refer to the report [View Docs](https://docs.google.com/document/d/1vZfzHo1wp9lLBaQD_VGX64LeBdU6OIWUUwdiZWj5ZFc/edit?usp=sharing).
## CI/CD

We implemented a CI/CD pipeline using GitHub Actions to automate testing and deployment.

- CI (Continuous Integration) runs backend and frontend tests on every push or pull_request to main or develop.
- CD (Continuous Deployment) is triggered only on `main` after tests pass. It securely connects to our Yandex Cloud VDS via SSH and runs docker compose up -d --build to deploy the new version.

### Tools used
- GitHub Actions  
- SSH deployment via [appleboy/ssh-action](https://github.com/appleboy/ssh-action)  
- Docker & Docker Compose  
- Yandex Cloud VM (VDS)

### Challenges faced
- Git remote conflict when tracking long nested branches (resolved with git remote prune origin)  
- SSH deployment required manual key generation and GitHub secrets configuration  
- Ensuring proper test environments across both backend (Java 21, Maven) and frontend (Node.js, Next.js)
- Couldn't find domain name for free, this task in progress yet, to get domain name for free.

### Links to CI/CD configuration files
- [main.yml (GitHub Actions workflow)](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/.github/workflows/main.yml)

---

## Deployment

### Staging

The application is deployed on a Yandex Cloud virtual server (VDS). The server hosts both frontend and backend containers using Docker Compose.

- Backend: Spring Boot (Java 21) running on port 8080  
- Frontend: Next.js app on port 3000  
- Reverse proxy: NGINX to handle routing and public access  
- CI/CD: Deploys automatically from GitHub on every main push  

Public access is available via the server's public IP address [View Here](http://51.250.42.156:3000) . Domain configuration is in progress, because we couldn't find it for free yet.

### Production

⚠️ _Bonus not yet implemented_

Plans for future:
- Assign a custom domain name 
- Add HTTPS using Let's Encrypt and Certbot  
- Separate staging and production environments on different ports or VMs  
- Use Docker and NGINX for robust deployment  

_This section will be updated in a future report._

## Vibe Check

- Held a dedicated team sync to assess workload, morale, and communication.
- Overall team mood is **positive** — members reported strong collaboration and task ownership.
- Main challenge raised: occasional backend-frontend sync delays during integration.
- Agreed on better scheduling of integration checkpoints to avoid blockers.
- Everyone feels aligned with the project goals and comfortable voicing concerns.
- Committed to maintaining transparent, supportive team dynamics.

[📝 View Full Vibe Check Notes](https://docs.google.com/document/d/1nFYXGL0FdrjkT2s4d8_1BGx3LdbUg17ma1MU_Xbd11Q/edit?usp=sharing)

## Machine Learning

Discussed the integration with the backend and updated the data models for both projects and candidates to align with the database schema. Additionally, the ML model application was dockerized to streamline deployment and ensure consistency across environments.

## Product Design

- Refined UI for **Dashboard**, **Find Talents**, and **Find Projects** based on feedback.
- Integrated user feedback from usability tests into Figma updates.
- Maintained alignment between design and code using Cursor + Figma MCP.
- Researched and did QuickSync Design Layout.

[🔗 View Figma](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=xaoT5YfI4T0EnhUi-1)


## CustDev
- Prioritized user hypotheses for testing and interviews.
- Collected early feedback on project/talent discovery flow.
- Analyzed user expectations around filtering and profile setup.
- Updated documentation for upcoming validation sessions.

[🔗 View CustDev Notes](https://docs.google.com/document/d/1rc2LE3dhGeFhPJU2gy640NaoJaA4k-TjfdgD8CtgQzk/edit?usp=sharing)

## AI Agents Utilization: Cursor with Model Context Protocols (MCP)

### Overview

During this week, we utilized **Cursor** in conjunction with **Model Context Protocols (MCP)** to implement several features and tasks — primarily on the frontend.

We specifically used the [Figma Context MCP](https://github.com/GLips/Figma-Context-MCP), a server designed for Cursor. This MCP simplifies and translates Figma API responses into model-relevant layout and styling data, allowing Cursor to generate the structural HTML/CSS for a page directly from Figma designs.

---

### Features and Tasks Completed with Cursor

- Implementation of the **Dashboard Page**
- Implementation of the **Find Project Page**
- Implementation of the **Find Talents Page**
- **Responsiveness implementation** for the **Login** and **Signout Pages**

---

### MCP Integration Workflow

The MCP was used to extract styling and structure data from Figma. Work was conducted **frame by frame** to maximize the effectiveness of Cursor’s code generation. This granular approach helped in maintaining precision and consistency with the original design specifications.

---

### Productivity Impact

#### ✅ Advantages

- **Facilitated straightforward design implementation**: Especially effective for designs with minimal components or simpler structures.
- **Accelerated repetitive frontend tasks**: Tasks like setting up filtering mechanisms, button logic, and basic layout configurations were significantly faster.
- **Motivational boost**: Cursor’s ability to produce near-correct outputs reduced procrastination, making it easier to get started and iterate quickly.

#### ⚠️ Disadvantages

- **Incorrect file placement**: Cursor occasionally placed correct code into the wrong files. If unnoticed early, these issues became hard to track and resolve.
- **Poor adherence to coding conventions**: Solutions sometimes worked technically but did not align with best practices or established code organization guidelines.
- **Duplicate or unnecessary component creation**: Cursor occasionally introduced redundant components or modified unrelated files, potentially causing long-term codebase conflicts.
- **Limited maintainability**: While the generated code often worked, it lacked flexibility and was sometimes hard to refactor or extend later.

---

### Productivity Metrics

- **Responsiveness & Filtering Features**:  
  Cursor provided a **20–25% productivity boost**, significantly reducing development time for UI logic and responsiveness.

- **Complex Page Implementations (Dashboard, Find Talents, Find Project)**:  
  Cursor contributed a **5–10% development boost**. These pages contained numerous components and complex interactions, where Cursor often struggled to accurately replicate the designs. Multiple iterations, developer intervention, and manual refactoring were required to complete the tasks to standard.

---

### Summary

Using Cursor with the Figma MCP delivered a noticeable productivity increase for isolated, straightforward frontend tasks. However, for more complex pages and scalable features, developer supervision and involvement remained critical to ensure maintainable, clean, and well-structured code.
# Weekly commitments

- **Ahmed Baha Eddine Alimi:**
    - Updated Issues in Github to ensure that their status are up to date with our progress [View](https://github.com/IU-Capstone-Project-2025/InnoSync/issues)
    - Implemented the design for Dashboard Page with Layout for (Projects, Invitations, Proposals, Chats, Profile panel) Sections [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f78f0afa97a6f8b375728d261b10923b4a241254)
    - Implemented/Enhanced the design for Find Projects and Implemented the filtering logic for it [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/86a58b21256b0ffe7c342cccdb95ad97c7c1b598)
    - Implemented/Enhanced the design for Find Talents and Implemented the filtering logic for it [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/30c5d059e53342ec1db7599cabef908d00156979)
    - Implemented/Enhanced the navbar styling and Implemented the logic for login/logout and routing for it with dropdown list for available actions [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/097d0a4ce301036fe8d39804745733255c39fe34)
    - Reviewed and merged pull requests in the frontend side [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/ea2bdf95fc63b16e8102c596e113541fb3326859)
    - Conducted Vibe Check with the team, collected their feedback and discussed the overall working environment [View Docs](https://docs.google.com/document/d/1nFYXGL0FdrjkT2s4d8_1BGx3LdbUg17ma1MU_Xbd11Q/edit?tab=t.0)
    - Reviewed and updated the figma design regarding the last usability testing and internal demo [View Design](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=xaoT5YfI4T0EnhUi-1)
    - Wrote the report


- **Yusuf Abudghafforzoda:**
    - Collaborated with frontend team to make endpoints connection
    - Adjusted APIs in the connection process [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/pull/89)
    - Wrote Unit tests for all logic-side of the project [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/pull/89)
    - Wrote Integration tests for Controllers, Repositories, and for connection with Database [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/pull/92)


- **Egor Lazutkin:**
    - Did the Formulation and prioritisation of hypotheses for preparation for user testing [View Docs](https://docs.google.com/document/d/10H6Tt8v1NovJBdq7HSrb2DaduyOAHK03A5K8UY2sXyw/edit?tab=t.0)

- **Asgat Keruly:**
    - Endpoint Connection for Logout [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/e39bfe12b8b5ba21e0dad82c4f597fb7cd6fce2b)
    - JWT Token Logic [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/e39bfe12b8b5ba21e0dad82c4f597fb7cd6fce2b)
    - Profile Panel Endpoint Connection [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/2a611520c1b0b6feead6dd0e7726c31a08959556)
    - Routing for SignUp and Login to dashboard [View Commit](github.com/IU-Capstone-Project-2025/InnoSync/commits/main/?after=1d6743832ddca2c1f7f2640c8720356df5e3f0a7+34)
    - Available projects fetching and representation in the frontend [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/9be7dde722c1bb3a0efdd6517c51ebc4af3ddee0)
    - Code Coverage Report & Screenshots for unit Tests [View Docs](https://docs.google.com/document/d/1vZfzHo1wp9lLBaQD_VGX64LeBdU6OIWUUwdiZWj5ZFc/edit?usp=sharing)
    - Profile initition endpoint connection [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/dd7a3cac194ac4a4bba5b284eae4d016cf5b7631)

- **Anvar Gilmiev:**
  - Project Creation Endpoint Connection [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/d049611f8b2858762c7a8fa8236b203e95a01619)
  - Connected experience level to profile creation [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/d049611f8b2858762c7a8fa8236b203e95a01619)
  - Available Talents fetching and representation in the frontend
  - Designed QuickSync UI [View Design](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=xaoT5YfI4T0EnhUi-1)

- **Aibek Bakirov:**
    - CI/CD pipeline setup [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/08ad686e13c14918b31f97b24f448297485687a2)
    - Enivronment Setup [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/08ad686e13c14918b31f97b24f448297485687a2)
    - Deployed full backend & frontend on a server [View Link](http://51.250.42.156:3000)

- **Gurbanberdi Gulladyyev:**
    - Discussed integration with backend
    - Changed data model for projects and candidates to match database [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/4c882e55f93b0c8989d7200f8efc5d4d1980426b)
    - Dockerized ML model app [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/4c882e55f93b0c8989d7200f8efc5d4d1980426b)

## Plan for Next Week

## Frontend
- Integrate QuickSync in Projects Dashboard
- Finalize Chats, Invitations, Profile Edit, and Projects pages
- Add loading states and error handling
- Refactor components for clarity
- Add basic end-to-end tests

---

## Backend
- Finalize endpoints: Invitations, Chats, Profile Edit
- Connect backend with ML QuickSync service
- Add integration tests for matching flow
- Improve validation and error handling

---

## Machine Learning
- Finish Docker setup for ML inference
- Finalize API for user matching
- Optimize embedding speed
- Test responses with frontend

---

## DevOps
- Add ML service to Docker Compose
- Add health checks to all services
- Improve GitHub Actions for build/test

---

## CustDev
- Collect feedback from early users
- Validate matching results and onboarding flow
- Plan final feedback survey

---

## Product & Design
- Finalize UI for QuickSync and Profile Edit
- Review product flow across mobile & desktop
- Support usability testing


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [**✔**] In working condition.
- [**✔**] Run via docker-compose (or another alternative described in the `README.md`).