# Week 2

# Requirements Elaboration

---

## User stories with acceptance criterias

1. As a student, I want to login to the system using Microsoft Entra, so that I can be sure about security of my data
    
    **Acceptance criterias:**
    
    - **Given** I am a student with a valid Innopolis University Microsoft account, **when** I click the “Login” button, **then** I am redirected to the Microsoft Entra sign-in page.
    - **Given** I enter correct credentials, **when** authentication is successful, **then** I am redirected to the projects dashboard.
    - **Given** I attempt to log in with an invalid or unrecognized account, **then** access is denied with an appropriate error message.
2. As a student, I want to create a personal profile with my skills, interests, and past projects so that I can be discovered by project creators or teammates.
    
    **Acceptance criterias:**
    
    - **Given** I’m logged in, **when** I visit the profile page, **then** I can fill in fields name, description, skills, project position, telegram alias, study group, and resume.
    - **Given** I’ve filled out my profile, **when** I return to the profile page, **then** the information is pre-filled and editable.
    - **Given** another user views my profile, **then** they can see a read-only version of my public details.
3. As a student, I want to post a new project with a description and required skills, so that I can find teammates who match my needs.
    
    **Acceptance criterias:**
    
    - **Given** I am logged in and have completed my profile, **when** I click “My projects→Create project,” **then** I see a form with fields: title, description, required skills, status, project link.
    - **Given** I have submitted the form, **then** the project appears in the public project feed.
    - **Given** I return to “My projects”, **then** I can see, edit, or delete my posted project.
4. As a student, I want to receive AI-generated project recommendations based on my skills and preferences, so that I can join relevant and high-fit teams more efficiently.
    
    **Acceptance criterias:**
    
    - **Given** I have completed my profile with skills, interests, and availability, **when** I open the feed, **then** I see a list of projects ranked by relevance to my profile.
    - **Given** I have edited my skills or interests, **when** I open the homepage, **then** the list of suggested projects updates.
5. As a student, I want to apply to projects that match my interests, so that I can participate in projects relevant to my skills and goals.
    
    **Acceptance criterias:**
    
    - **Given** I see a project in the feed, **when** I click “Apply,” **then** I can submit the request.
    - **Given** I applied to a project, **then** I can see my application status in the “My responces” tab.
    - **Given** my application was accepted, **then** I receive a notification and the project appears in “My responces” as “Active.”
6. As a project owner, I want to accept or reject team applications and manage my team members, so that I can control who joins my project and maintain a good team structure.
    
    **Acceptance criterias:**
    
    - **Given** I own a project, **when** someone applies, **then** I see their profile and can click “Accept” or “Reject.”
    - **Given** I accept a student, **then** they appear in my team list.
    - **Given** I view the “Manage Team” section, **then** I can remove members and see their profiles.
7. As a student, I want to see suggestions and filters when browsing projects, so that I can efficiently choose which projects to join.
    
    **Acceptance criterias:**
    
    - **Given** I open the project feed, **then** I see filters like tech stack and tag.
    - **Given** a project closely matches my profile, **then** it is ranked higher or labeled as “Recommended.”
    - **Given** I select filters, **then** only matching projects are shown.
8. As a teacher, I want to login to the system using Microsoft Entra, so that I can be sure about security of my data
    
    **Acceptance criterias:**
    
    - **Given** I am a teacher with a valid Innopolis University Microsoft account, **when** I click the “Login” button, **then** I am redirected to the Microsoft Entra sign-in page.
    - **Given** I enter correct credentials, **when** authentication is successful, **then** I am redirected to the projects dashboard.
    - **Given** I attempt to log in with an invalid or unrecognized account, **then** access is denied with an appropriate error message.
9. As a teacher, I want to make a page only for my course, so that I can manage the team formation between my students.
    
    **Acceptance criterias:**
    
    - **Given** I am logged in as a professor, **when** I create a course room, **then** students can see/create projects on this board.
    - **Given** students created projects, **then** they can only see and interact with projects from this course.
10. As a teacher, I want to upload the spreadsheet with teams, so that students do not need to write it manually
    
    **Acceptance criterias:**
    
    - **Given** I access the course room dashboard, **when** I upload a CSV/Excel file with team data, **then** the system parses it and creates corresponding projects and team assignments.

# Backlog

---

[🔗 Link to prioritized backlog](https://team-sync-capstone.atlassian.net/jira/software/projects/TS/boards/1?atlOrigin=eyJpIjoiMzBkNTBiMTQ3MWRmNDU1YmJhMzJhZDAxZTE5MjM3NmUiLCJwIjoiaiJ9) 

*if you want to get access to it, log in to Jira with VPN and Innopolis University account*

We have three basic columns in our  board: **“To Do”**, **“In Progress”**, and **“Done”**. Additionally, we’ve added a **“Trashed”** column to store tasks that are no longer relevant.

# Reflection after meeting with TA

---

- We need to schedule a meeting with Alexey Potyomkin to discuss potential collaboration since he is planning to do almost the same service for our university
- We need to research Microsoft Entra capabilities to make login secure

# Reflection after meeting with Alexey Potyomkin

---

### **1.Strategic planning for long-term growth**

- A brainstorming table should be created to track and organize future improvement ideas for the platform. This will support strategic planning beyond the MVP phase.
- The focus in the short term should remain on the core university use case, ensuring we deliver functional value to students and faculty first.
- Once the academic version is validated, the platform can be extended for commercial and external use cases.

### **2. Customer discovery (CustDev) & Hypothesis testing**

- We will initiate a CustDev process to validate assumptions and gather structured feedback from real users (students, teachers).
- Based on collected insights, we’ll formulate and prioritize hypotheses for improvement and potential product extensions.


### **3.Stakeholder alignment**

Schedule conversations with the following stakeholders to align the platform with broader institutional goals:

- **Marko Pezer** – regarding team distribution in SWP (Software Project) coordination.
- **Mansur Khazeev** – to explore potential involvement in industrial projects and corporate collaboration scenarios.


### **4.Integration with digital profile ecosystem**

- A strategic suggestion was made to explore integration of TeamSync into the Innopolis Digital Profile system, enabling richer personalization, centralized data use, and long-term scalability.
- Next step: determine the technical requirements and institutional process for this integration.

# **Project specific progress**


## Design

---

During last week Sign-Up process (adding Roles, Skills, Project position, and Personal information) and  Homepage (with projects) were designed. Also, User Flow was updated and divided by two parts: “For Students” and “For Teachers”. We will implement for MVP only “For Students”.

[🔗 Link to User Flow](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1)

![User flow](https://github.com/mnkhmtv/project-screenshots/blob/main/week2/user_flow.png?raw=true)

[🔗 Link to Design](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=eFfwdjWTMholcFaF-1)

## Frontend

---

This week, the basic frontend structure was made [TS-28], two skeleton pages were made (splash and home) [TS-29] and a simple route was set up between them. There weren’t many significant issues with the front end of the project, the only issue was dynamic page layouts. This issue will be fixed by the end of the week, after the design is updated with new mobile layouts, dropdown menus and hover button styles. Next week, the focus will be on SSO functionality via Microsoft Entra and integration with the backend.

## Backend

---

During the last week we developed initial database scheme [TS-36] and wrote liquibase migrations [TS-39]. Also defined the backend architecture [TS-45] and created APIs for the services (RestAPI and gRPC): [TS-50], [TS-51], [TS-56], [TS-59]. Studied the SSO that we are using (Microsoft Entra ID) and described how to work with it at our [team’s notion site](https://www.notion.so/SSO-210c1c5fc56980f294fdf65cb817ed65?pvs=21). And the last one - started the development of auth service [TS-59].

During the week we faced some problems, related to overall architecture and contracts, but we spoke about it together and decided to do it how it done now. The biggest problem was about filtering recommendation that were calculated by ML services. It was not clear what services should do it and how (backend or ML services). We decided to leave that feature and return to it later, but anyways, during the discussion , there were some important notes and takes related to the problem and we will definitely return to them later!

You can check out services’ api’s at the back/*some service* directory in our github repository. Some of them are RestAPI conrtacts (api.yaml), written in openApi format and can be viewed at online swagger editor, others are *.proto gRPC contracts

[🔗 Page “how to work with SSO”](https://www.notion.so/SSO-210c1c5fc56980f294fdf65cb817ed65?pvs=21)

[🔗 Link to the Backend architecture](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1)

![Backend Architecture](https://github.com/mnkhmtv/project-screenshots/blob/main/week2/system%20architecture.png?raw=true)

[🔗 Link to ER diagram](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1)

![ER Diagram](https://github.com/mnkhmtv/project-screenshots/blob/main/week2/er_diagram.png?raw=true)

[🔗 Link to Tables](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1) 

![tables](https://github.com/mnkhmtv/project-screenshots/blob/main/week2/tables.png?raw=true)

## ML

---

During the last week, we discussed baseline models and project architecture [TS-34]. We collected basic datasets for roles and tools [TS-35]. We wanted to collect a dataset of projects from the Capstone project organization, but the task turned out to be too difficult because it is hard to understand who knows what, who does what, and who is who from the participant table. It is easier to synthesize the data ourselves, but we took project names and descriptions from the Capstone project table and added people to them with roles and skills [TS-56].

🔗 [Dataset table](https://docs.google.com/spreadsheets/d/1tUttYmSKzev1PhMxKsig-9HHMoh4L8T4_GKKNqlkhNY/edit?usp=sharing)

[🔗 Link to ML architecture](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1)

![ML architecture](https://github.com/mnkhmtv/project-screenshots/blob/main/week2/ml_arch.png?raw=true)

# **Weekly commitments**

---

## **Individual contribution of each participant**

| Team member | Contribution |
| --- | --- |
| Diana MInnakhmetova (Lead) | held 3 meetings, [designed authorization and home pages](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=eFfwdjWTMholcFaF-1), updated user stories with acceptance criterias, [updated user flow](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1) |
| Danis Sharafiev | [made ML system architecture](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1), researched potential models/algorithms for baseline, [collected dataset](https://docs.google.com/spreadsheets/d/1tUttYmSKzev1PhMxKsig-9HHMoh4L8T4_GKKNqlkhNY/edit?usp=sharing) |
| Daria Alexandrova | [implemented skeleton components/pages based on initial designs](https://github.com/IU-Capstone-Project-2025/team-sync/commit/bb4750efc855892f70ccb1741f66b9e39bd6b1e2), [helped with design](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=eFfwdjWTMholcFaF-1) |
| Stepan Dementev | [created API for auth service](https://github.com/IU-Capstone-Project-2025/team-sync/pull/12), [wrote database migrations](https://github.com/IU-Capstone-Project-2025/team-sync/pull/10), [made system architecture](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1), [create API for recomendation](https://github.com/IU-Capstone-Project-2025/team-sync/pull/14) |
| Elizaveta Zagurskih | [create API for projects service](https://github.com/IU-Capstone-Project-2025/team-sync/pull/11),[create API for resume](https://github.com/IU-Capstone-Project-2025/team-sync/pull/13), [identified entity-relation diagram for backend, made system architecture](https://www.figma.com/board/se6mmoDbUnNADLcPqSszQE/TeamSync-sys-design?node-id=0-1&t=Mak6NzMutwl0n0Nf-1)  |
| Kamilya Shakirova | [collected dataset for ML](https://docs.google.com/spreadsheets/d/1tUttYmSKzev1PhMxKsig-9HHMoh4L8T4_GKKNqlkhNY/edit?usp=sharing) |

## **Plan for Next Week**

- Continue implementing backend services for authentication, resume submission, project creation, and the recommendation engine, following the defined API structure
- Develop a baseline model for the project recommendation system
- Enhance the user interface by adding button animations for both default and active (pressed) states
- Explore and evaluate pagination approaches for handling long project or user lists on the frontend
- Configure Nginx on the backend to manage routing and API gateway functionality
- Hold a meeting with potential customers and/or stackeholders

**Confirmation of the code's operability**

We confirm that the code in the main branch:

- [ ]  In working condition.
- [ ]  Run via docker-compose (or another alternative described in the `README.md`).