---
title: "Week #5"
---

# **Week #5**

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


## Feedback

### **Sessions**

We conducted structured usability testing sessions with **7 participants**, each representing a distinct user persona (students, developers, designers, project managers, etc.). These sessions involved guided interaction with the MVP, task-based workflows, and post-session interviews.

The feedback was collected using observation, quotes, and structured notes.

> 🔗 Full report available here: [Usability Testing Summary & Feedback Analysis](https://docs.google.com/document/d/1NDk67RHIRa8g-8ofnIPr_558_YmQjkcktEoZAzk3Zyg/edit?usp=sharing)

#### Highlighted Participants

- **Alina (21)** – IT student focused on internships. Requested better filtering and project clarity.
- **Artyom (27)** – Freelance backend developer. Wanted GitHub links and user activity signals.
- **Nadya (24)** – UX designer. Emphasized design visibility and clearer application flow.
- **Sasha (30)** – Startup PM. Needed skill-based filters and team management features.
- **Ilya (23)** – Frontend dev & OSS contributor. Wanted GitHub/CI integration and task filtering.

This feedback played a critical role in identifying and prioritizing platform pain points.


### **Analyze**

Following structured usability tests and interviews, we identified key user concerns and categorized issues based on frequency and impact:

#### 🔥 High Priority Issues (P1)
- **Lack of user activity indicators**: Users couldn’t distinguish between active and inactive users, making the platform feel static.
- **Unclear application flow**: Many users clicked "Apply" without knowing what would happen next.
- **Uninformative project cards**: Cards lacked essential details like team structure, goals, and links to GitHub, which reduced trust.
- **Inadequate filtering in "Find Talent"**: Absence of filters for roles, soft skills, or availability hindered effective team building.
- **Project tags and trust indicators missing**: Users asked for labels like “Hackathon”, “Volunteering”, or “Verified” to better assess projects.

#### 📊 Medium Priority Issues (P2)
- **Lack of automated recommendations** based on user skills and interests.
- **Onboarding experience missing**: Some users were unsure how to begin using the platform.
- **No integration with GitHub/ORCID**: Users wanted validation via external profiles.
- **Proposals vs Invitations unclear**: UX needed clearer visual distinction and interaction cues.
- **No portfolio showcase for non-dev roles**: Designers couldn’t effectively display their work.

#### 🔍 Low Priority Issues (P3)
- **Missing social features**: Some users suggested activity feeds, endorsements, and reviews to foster engagement.

Each of these insights was converted into actionable tasks.

> 🔗 **[View full backlog in our Github](https://github.com/IU-Capstone-Project-2025/InnoSync/issues)** 

## Iteration & Refinement

### Implemented features based on feedback

### ✨ **UX/UI Design Enhancements**

Following the usability testing and feedback analysis, our design team produced a structured improvement document to guide UI refinement. The following actionable items were prioritized for implementation:

1. **Redesigned Project Cards**  
   – Structured layout including project goal, team composition, GitHub link, and project status badge.  
   – Hover effect, clear clickable areas, and consistent visual hierarchy to improve trust and clarity.

2. **User Activity Indicators**  
   – Online/offline badges added to user avatars and project cards.  
   – Tooltips and real-time updates included for enhanced interactivity and user awareness.

3. **Improved Button Feedback and Interaction**  
   – Clear visual states (default, hover, active, disabled) implemented.  
   – Tooltips and microcopy added for buttons like "Apply" and "Chat" to prevent confusion.  
   – Accessibility and contrast ratios reviewed to meet WCAG 2.1 guidelines.

4. **Talent Filter Bar**  
   – Added dropdown-based multi-select filters for Role, Soft Skills, and Availability.  
   – Sticky filter bar with clear tags and a reset button enables more precise team building.  
   – Fully keyboard-navigable and ARIA-compliant for accessibility.

> 🔗 **[View full design enhancement document](https://docs.google.com/document/d/1QbovOKeF6NC5AjKTMk5yNAzkFH6SS1yHW5ipXq_i_VU/edit?tab=t.0)**  

### 🐛 Implemented Bug Fixes in the Frontend

We addressed several key frontend issues to improve user experience, prevent unexpected behaviors, and enhance the application's responsiveness and clarity.

#### ✅ Error Handling & UX Fixes

- **Signup Page**  
  - After successful signup, the user is redirected to the profile initiation page, with a confirmation toast displayed.

- **Profile Initiation Page**  
  - Implemented field validation and individual toasts for missing input fields.  
  - Fixed the technologies input field and improved placeholder consistency across the form.

- **Find Talent Page**  
  - Users can no longer see their own profiles in the "Find Talent" section.  
  - Prevented users from sending invitations to themselves.

- **Find Project Page**  
  - A user’s own project is no longer shown to them in the "Find Project" section.  
  - This prevents users from applying to their own projects.  
  - Added an empty-state message for when no projects are available. (users now see a clear notice instead of a blank screen.)

- **Dashboard → Profile Panel**  
  - Added functionality to modify user positions and skills post-initiation.  
  - Prevented users from removing **all** skills (at least one must remain).  
  - Integrated error handling to guide users when editing skills or positions.

- **Sign-Out Flow**  
  - After signing out, users are now redirected to the **home page**, improving flow clarity and preventing access to restricted routes.

These fixes addressed the critical bugs that were brought to us after the usability testing.
> 🔗 **All the above fixes were implemented in this commit**:  [View Commit on GitHub](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/d3c639179dd7ec17bf874a9dcc551ac456f4aa7f)


### 🧪 Preliminary Performance Metrics (Homepage)

We conducted an initial Lighthouse audit on the **home page** at [https://innosync.duckdns.org](https://innosync.duckdns.org). These results serve as a **preliminary benchmark**, as the current frontend and backend implementations are **not yet finalized or fully optimized**.

| Metric                        | Score/Value       |
|------------------------------|-------------------|
| **Performance Score**        | 67                |
| First Contentful Paint       | 1.8 s             |
| Largest Contentful Paint     | 3.3 s             |
| Total Blocking Time          | 0 ms              |
| Cumulative Layout Shift      | 0.006             |
| Speed Index                  | 3.8 s             |
| **Accessibility**            | 95                |
| **Best Practices**           | 96                |
| **SEO**                      | 100               |

#### ⚠️ Diagnostics & Optimization Opportunities
- Server response time for root document: **~1,090 ms**
- Avoiding render-blocking resources: **~1,120 ms savings**
- Unused JavaScript: **~49 KiB**
- HTTP/2 not used for 34 requests
- Minor layout shifts and legacy JS served to modern browsers

#### ✅ Passed Audits
- JavaScript execution is efficient (0.2s)
- DOM size and network payload are within acceptable limits
- No long third-party blocking

These figures provide a useful baseline for ongoing performance optimization and frontend refinement.

> 📍 *Note: These results are from Lighthouse v12.3.0 run on Jul 9, 2025, and are subject to change as we finalize deployment pipelines, CDN configuration, and frontend refactoring.*

> 🔗 **Full detailed Pdf report**: [View Pdf on GitHub](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/assets/Performance%20Metrics.pdf)


#### 🔧 DevOps Improvements
![Piplines Running](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/photo_2025-07-09_20-39-59.jpg)
![Piplines Success](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/photo_2025-07-09_20-39-59.jpg)

Our DevOps infrastructure has been enhanced to support secure, automated deployment, ensure application uptime, and streamline the development lifecycle.

---

### **CI/CD Pipeline**

- **GitHub Actions** is used for CI/CD, configured in [`main.yml`](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/.github/workflows/main.yml).
- **CI triggers** on push or pull request to `main` and `develop` branches.
- **CD triggers** on push or pull request to `main` branch only.
- **Secrets Management**: GitHub Secrets store all sensitive credentials, including SSH keys, Docker Hub tokens, and production environment variables.
- **Build and Deployment Evidence**: CI/CD pipeline includes build, test, and deploy stages with screenshots of successful executions provided internally.
- **Public Access**: The deployed version is live at [https://innosync.duckdns.org](https://innosync.duckdns.org)

---

### **Server Setup Explanation**

#### 🖥️ **Hosting Provider**
- **Provider**: Yandex Cloud (Virtual Dedicated Server)
- **OS**: Ubuntu 22.04 LTS
- **Access**: SSH access secured via private key authentication, used by GitHub Actions during deployment

#### 🐳 **Docker & Docker Compose**
- **Containers run via Docker Compose**, which orchestrates:
  - `study_buddy_db`: PostgreSQL container
  - `app`: Go backend API
  - `frontend`: Next.js frontend (React)
  - `nginx`: Reverse proxy + SSL termination

- **Improvements**:
  - Health checks and logging added
  - Persistent volumes for database and nginx logs
  - Network isolation between services for better security and integrity

---

### 🌐 **Domain & SSL**

- **Domain Name**: 
  - Frontend: [innosync.duckdns.org](https://innosync.duckdns.org)
  - Backend API: `api.innosync.duckdns.org`
- **DNS**: DuckDNS A-record points to our VDS public IP

- **SSL via Let's Encrypt**:
  - **Certbot** is used to issue and renew HTTPS certificates automatically
  - **NGINX Configuration**:
    - HTTP traffic is redirected to HTTPS
    - Secure reverse proxy forwards requests to respective containers

---

### 🌍 **CORS & Environment Variables**

- All environment variables are defined in `docker-compose.yml` and `.env` files
- **CORS Configurations**:
  - Backend allows requests only from: `https://innosync.duckdns.org`
  - NGINX acts as a gateway that properly forwards headers and manages HTTPS traffic

---

This DevOps setup ensures scalability, security, and fast iteration cycles while supporting the public availability of the project.


### **Documentation**

We maintain the following types of documentation:

- **README.md**:
  - Contains installation instructions, service descriptions, and Docker Compose usage.
  - Includes environment variable templates (`.env.example`) and quickstart guide for contributors.

- **CI/CD Workflow Docs**:
  - GitHub Actions workflows are self-documented with inline comments.
  - Secret management and deployment configuration are described in `docs/devops.md` (internal, WIP).

- **Architecture Diagram (planned)**:
  - A visual representation of the full stack (NGINX, Go, PostgreSQL, React) is in development to support onboarding.

- **API Reference (backend)**:
  - Swagger file generated via Go annotations (auto-hosted on `/api/docs` endpoint).
  - Also a ReadMe file in our project's repo that documents all of the stable endpoints. [API docs](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/assets/API_documentation.md)


### ML Model Refinement

Faced challenges integrating the ML model with the backend due to inconsistencies in request handling and data flow. The existing Dockerized setup for the ML application remained unchanged, but debugging focused on aligning the API contract between the backend and the ML service. Partial progress was made in understanding the bottlenecks, and fixes are ongoing.

# Weekly commitments

- **Ahmed Baha Eddine Alimi:**
    - Updated Issues in Github to ensure that their status are up to date with our progress and added priotrized new ones in accordance with the usablity testing that we did. [View](https://github.com/IU-Capstone-Project-2025/InnoSync/issues)
    - Coordinated work across frontend, backend, and design teams.
    - Implemented major frontend fixes based on usability testing. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/d3c639179dd7ec17bf874a9dcc551ac456f4aa7f)
    - Conducted **preliminary performance and stability testing** using Lighthouse on the deployed application. [View Report](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/assets/Performance%20Metrics.pdf)
    - Wrote the report


- **Yusuf Abudghafforzoda:**
    - Implemented the **chat endpoint and backend logic**. [View PR](https://github.com/IU-Capstone-Project-2025/InnoSync/pull/121)
    - Fixed **CORS configuration** to ensure secure frontend-backend communication. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/51288a80cb40cdce9a3bcd05635bf138a062841d)
    - Added logs for backend [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/c73b6bdc845d1e389731dc77eb09a846fe518f75)
    - Collaborated with frontend to connect API endpoints.


- **Egor Lazutkin:**
    - Led the **usability testing sessions** with the participants.
    - Facilitated **task-based interactions and post-session interviews** to extract actionable feedback.
    - Synthesized findings into **structured feedback notes** used to identify P1–P3 level issues.
    - Creation of the **Usability Testing Summary & Feedback Analysis** document. [View Report](https://docs.google.com/document/d/1NDk67RHIRa8g-8ofnIPr_558_YmQjkcktEoZAzk3Zyg/edit?usp=sharing)


- **Asgat Keruly:**
    - Helped in fixing **CORS** for deployment [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/82e8c0a5dbf28225d61047519faea1016c71dcd7)
    - Designed and refined components for the **Overview** and **Project Details** sections. [View Design](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=xaoT5YfI4T0EnhUi-1)
    - Provided review and feedback for the usability testing. [View Docs](https://docs.google.com/document/d/1QbovOKeF6NC5AjKTMk5yNAzkFH6SS1yHW5ipXq_i_VU/edit?tab=t.0)


- **Anvar Gilmiev:**
    - Linked endpoints of the frontend app of the **Find Talent page**. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/1f404632755997d20ae7310d21877e1de4bd17b8)
    - Linked invitation endpoints in the frontend [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/1f404632755997d20ae7310d21877e1de4bd17b8)

- **Aibek Bakirov:**
    - Set up and maintained the **CI/CD pipeline** using GitHub Actions (`main.yml`).
    - Managed **build, test, and deploy stages** for automatic deployment to production.
    - Secured **secrets management** for environment variables and credentials.
    - Configured **NGINX reverse proxy**, **Let's Encrypt SSL**, and domain routing.
    - Managed **Docker Compose setup** for PostgreSQL, Go backend, and Next.js frontend.
    - Ensured **persistent volumes, health checks, and network isolation** for services.
    [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/0ee0b73b6b361728de14c32841a67a9dbd6490d9)

- **Gurbanberdi Gulladyyev:**
    - Work on resolving the integration issue between the backend and the ML model, specifically ensuring the correct request format and response handling between services.



## Plan for Next Week

## Frontend
- Implement redesigned Project Card components with full interactivity
- Improve responsiveness and layout on mobile devices
- Polish UI for Find Talent filters and apply page transitions
- Begin building onboarding flow screens
- Implement newely usability testing adapted designs

---

## Backend
- Complete and test the Proposal vs Invitation logic
- Add activity indicators (last seen, user status) to API responses
- Enhance the chatting feature
- Work on a solution for ML integration

---

## Machine Learning
- Work on a solution for ML integration.
- Prepare ML part for deployment

---

## DevOps
- Optimize image sizes and compression for frontend performance
- Set up monitoring (logs, CPU/mem usage) for backend services
- Improve CI pipeline speed by caching Docker layers

---

## CustDev
- Conduct 3–5 follow-up interviews with prior test participants
- Collect qualitative feedback on the new Find Talent filters

---

## Product & Design
- Finalize designs for onboarding and verification UI
- Align interface elements across pages for consistency
- Start drafting final feature set for a more stable product release

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [**✔**] In working condition.
- [**✔**] Run via docker-compose (or another alternative described in the `README.md`).