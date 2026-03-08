---
title: "Week #2"
---

# **Week #2**

### Project name: **InnoSync**

**Code repository**: https://github.com/IU-Capstone-Project-2025/InnoSync

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| (Lead) Ahmed Baha Eddine Alimi     | @Allimi3 | a.alimi@innopolis.university | [Frontend/DevOps] | Team Management, Frontend & Design Supervision|
| Yusuf Abudghafforzoda| @abdugafforzoda | y.abudghafforzoda@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Egor Lazutkin            | @Johnn_u | e.lazutkin@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Anvar Gilmiev            | @glmvai | a.gilmiev@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Asgat Keruly            | @east511 | a.keruly@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Aibek Bakirov | @bakirov817 | a.bakirov@innopolis.university | [DevOps] | Infrastructure Automation, CI/CD Setup, Deployment |
| Gurbanberdi Gulladyyev | @gurbangg | g.gulladyyev@innopolis.university | [ML] | ML Model Research & Development for QuickSyncing |

## Detailed Requirements Elaboration

## **MVP Detailed User Stories & Acceptance Criteria**

### 1. Unified User Registration & Profile
**User Stories:**
- As a new user, I want to register once with a complete profile so I can later choose my mode (Talent/Recruiter).
- As a returning user, I want to switch between Talent and Recruiter dashboards based on my current needs.

**Acceptance Criteria:**
- Single registration form collects:
  - Core profile info (name, email, bio)
  - Skills (tag-based input)
  - Expertise level (Entry/Junior/Mid/Senior)
  - Experience level (Less than a year/ 1 to 2 years/ 2 to 4 years/ more than 4 years)
  - Resume upload (optional)
  - Education
  - Work Experience (optional)
- Post-login dashboard selector appears with:
  - "Talent Mode" (for seeking projects, managing proposals)
  - "Recruiter Mode" (for managing/creating projects)
- Users can switch modes via an option in the navbar

---

### 2. Talent Mode Features
**User Stories:**
- As a Talent, I want to browse projects matching my skills so I can apply.
- As a Talent, I want to manage applications and invitations in one place.

**Acceptance Criteria:**
- Talent dashboard shows:
  - Project recommendations (based on profile)
  - Application status tracker
  - Invitation inbox
- Search filters for projects:
  - Required skills
  - Project type (paid/academic)
  - Time commitment

---

### 3. Recruiter Mode Features
**User Stories:**
- As a Recruiter, I want to create projects and define needs so I can build teams.
- As a Recruiter, I want to discover talents and manage invitations.
- As a Recruiter, I want to can collaborate with my team memebers in one place.

**Acceptance Criteria:**
- Recruiter dashboard includes:
  - Project creation wizard
  - Talent discovery panel
  - Team management section
  - Group chat for each project with all the team memebers
- Project creation allows:
  - Role definitions (with required skills)
  - Team size settings
  - Project timeline

---

### 4. QuickSyncing (Recruiter Auto-Matching)
**User Story:**
- As a Recruiter, I want the system to automatically suggest suitable candidates for my project so I can quickly build my team.

**Acceptance Criteria:**
- Only available in Recruiter mode
- Generates candidate suggestions based on:
  - Skills matching project requirements
  - Alignment with required roles
  - Compatible expertise levels
- "Reroll" button provides new suggestions while maintaining:
  - Current project criteria
  - Applied filters

---

### Key Changes from Previous Version
1. **Single Profile Creation**: Eliminates role selection during signup
2. **Mode Switching**: Users aren't locked into one role
3. **Shared Core Data**: Skills/experience used for both modes
4. **Dual Dashboard UI**: Consistent navigation between modes


### **Prioritized Backlog**

**Asana Board:** [[View Backlog]](https://app.asana.com/1/1210534032818449/project/1210533915397443/board/1210533959405717)

## **Project Specific Progress**

### Frontend
- Initialized Next.js project with TypeScript configuration
- Implemented skeleton components based on initial designs
- Implemented the navbar and landing page design in the react 

### Backend
- Made the Database conception 
- Made a swagger documentations for the endpoints
- Impelemneted User Authentication APIs (Logout/Login/SignUp APIs)
- Impelemented API to create/update talent profile
- Impelemented the security layer:Protecting endpoints with JWT Validation Filter
### Machine Learning
- Created mock job/candidate data.
- Wrote simple model using TF/IDF and cosine similarity for team recommendation.
- ReadMe for the ML work [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/662de0a195b84260c0bd269c21c1509ce5f6317a)

### DevOps
- Defined Infrastructure plan
- Research Project DevOps Requirments

### Management:
- Defined MVP goals and scope [[View Docs Link]](https://docs.google.com/document/d/1k7yiHy8y-ZioPbZ6eZcaMPgFsjLnU5j6D55uELiVFr8/edit?usp=sharing)
- Fed the backlog and orginized it using a PM tool (we used Asana board) [[View board]](https://app.asana.com/1/1210534032818449/project/1210533915397443/board/1210533959405717)
- Distributed Tasks between roles, and then distributed them between team memebers.

### Product Design
- Researched similar products designs, refined the user stories and added acceptance criteria for each, refined the mvp goals.
- Created low-fidelity and wireframe mockups [[View Figma File]](https://www.figma.com/design/fY5ZJ8P4bacAdBqnyqhllN/Low-Fi-Design-InnoSync?node-id=0-1&t=l156qcYKInDeYg2X-1)
- Created user flow diagrams for key interactions [[View Figma File]](https://www.figma.com/design/anoj5o3g9OTlcoA6vtiUu0/User-flow-diagrams-InnoSync?node-id=0-1&t=Jk4bQmZ6MyPPjd0X-1)
- Started the high-fidelity designing for the web application [[View Figma File]](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=2LRuSQRB1dTt6pKe-1)

### CustDev
- Researched and formulated user pain points [[View Docs Link]](https://docs.google.com/document/d/1HlvEzdK_1SqD2897v1px_rMfg5cDnx8KY4yLWlCAaBw/edit?tab=t.0#heading=h.ta3epewq5m2a)

# Weekly Commitments

## **Individual Contribution of Each Participant**

- **Ahmed Baha Eddine Alimi:**
  - Revised and enhanced user stories, added acceptance criteria and refined the mvp goals [Present in the report]
  - Coordinated sprint planning, and tasks distribution
  - Reviewed and merged PRs for the frontend team [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/659d078fe7343fc989b732c27495373e7bf79a4f)
  - Created Low-Fi, High-Fi and User flow diagrams in Figma. 
    - [View Low-Fi Figma File](https://www.figma.com/design/fY5ZJ8P4bacAdBqnyqhllN/Low-Fi-Design-InnoSync?node-id=0-1&t=l156qcYKInDeYg2X-1)
    - [View UFD Figma File](https://www.figma.com/design/anoj5o3g9OTlcoA6vtiUu0/User-flow-diagrams-InnoSync?node-id=0-1&t=Jk4bQmZ6MyPPjd0X-1)
    - [View High-Fi Figma File](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=2LRuSQRB1dTt6pKe-1)
  - Wrote the report


- **Yusuf Abudghafforzoda:**
  - Implemented Backend authentication APIs [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/aee6692a19dbff2ef4670ca17aead5a28ce8a517)
  - Database coneception and schema
    - [View DB description](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/assets/DB_design.md)
    - [View DB Schema](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/DB_diagram.png)
  - Made the swagger documentations for the endpoints
  - Impelemented the security layer in the backend authentication [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/aee6692a19dbff2ef4670ca17aead5a28ce8a517) 

- **Egor Lazutkin:**
  - Impelemented API to create/update recruitee profile [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/15d7caeaab5abb26e672be86baecb5e04272b9f1)
  - Researched and formulated user pain points [[View Docs Link]](https://docs.google.com/document/d/1HlvEzdK_1SqD2897v1px_rMfg5cDnx8KY4yLWlCAaBw/edit?tab=t.0#heading=h.ta3epewq5m2a)
- **Anvar Gilmiev:**
  - Set up routing for the project [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/dd453a8293f07f1aaa73d7308e2d519bdb46a4fc)
  - Implemented the profile creation page [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/d2c9321d5e49a7c7a7785e8560e1cde7d26615c3)

- **Asgat Keruly:**
  - Implemented skeleton components based on initial designs [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f470d7696b9f052effe52f1ef311ed176bc047ab)
  - Impelemented the early version of the navbar and landing page [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/7a68128bc8ad8e8b882636e2641501e42106a36c)

- **Aibek Bakirov:**
    - Defined Infrastructure plan [[View Docs Link]](https://docs.google.com/document/d/1inji-c-n2KHe5R-PxcqPwq9v0tphDdvpUhKw1ize89k/edit?tab=t.0)
    - Researched Project DevOps Requirments

- **Gurbanberdi Gulladyyev:**
    - Created mock job/candidate data. [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f48f806244ff123db7fb947142c68e6794cd9bb0)
    - Wrote simple model using TF/IDF and cosine similarity for team recommendation. [[View Commit]](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f48f806244ff123db7fb947142c68e6794cd9bb0)

## Plan for Next Week
1. **Frontend:**
   - Finish the implementation of the page designs
   - Implement basic button functionionalites and basic features
   - Connect to backend APIs

2. **Backend:**
   - Develop project creation endpoint
   - Implement API for recruiters to send invitations to talents
   - Implement API for talents to apply to projects

3. **Machine Learning:**
   - Finalize dataset collection
   - Train preliminary recommendation model
   - plan intergration witrh backend

4. **DevOps:**
   - Configure GitHub Actions
   - Set up basic CI pipeline
   - Research deployment strategies
   - Create docker-compose.yml to run full stack locally

5. **Product Design:**
   - Finish High-Fi design
   - Meet with the CustDev to discuss costumer needs
   - Adapt design to costumer needs  
5. **CustDev:**
   - Prepare for UX testing
   - Generating and prioritizing hypotheses
   - Building a customer journey map


## Confirmation of the Code's Operability

We confirm that the code in the main branch:
- [**✔**] In working condition (local development)
- [**✔**] Run via docker-compose (in progress)