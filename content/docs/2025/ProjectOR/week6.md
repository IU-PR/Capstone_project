---
title: "Week #6"
---

# **Week #6**

## Links

*Specify here all the necessary links to your website, application installer, final demo, etc.*

- **Deployment**: [link](https://projector-1.onrender.com)
- **API Docs**: [link](https://projector-bp8n.onrender.com/docs)
- **Design**: [link](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design/low-fi.fig)
- **Demo**: [link](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/design)

## Final deliverables

### Project overview

**Key Features:**
- User Registration and Authentication: Secure access to the system through credential-based login.
- Role Selection: Users can choose their role in the system, such as founder or developer.
- Project Creation: Founders can create and manage their own projects.
- Tagging System: Tags can be generated and associated with projects for categorization and filtering.
- Join Requests: Developers can send requests to join projects created by founders.

**Problems Solved:**
- Unstructured Team Collaboration: The system introduces role-based access (founder, developer), which allows for organized collaboration within projects.
- Lack of Project Ownership Control: Only users with the founder role can create projects, ensuring a clear hierarchy and ownership model.
- Difficulty in Developer Onboarding: Developers can send structured join requests to participate in projects, streamlining team formation.
- Unorganized Project Classification: The tagging functionality allows projects to be categorized and filtered, improving discoverability and organization.
- Authentication Gaps: User registration and login ensure that access is controlled and secure.

### Features

- registration and authentication added
- the ability to select a role was added
- the ability to create a project for the founder was added
- tag generation functionality for the project was implemented
- requests for joining the project for developers were created

### Tech stack

This project uses JavaScript Svelte for frontend (UI + static), Python FastApi for backend, GithubActions + Render as CI/CD tools

### Setup instructions

Before running, you need to create and fill variables `backend/app/.env` file. An example of such a file is located in `backend/app/.env.example`. 

Prerestiques: for launching this project locally docker must be installed and docker daemon launched. For launching it's needed to type this command:

```bash
docker compose up --build
```
Then open browser with this url:

```
http://localhost:80
```

Additionally, backend documentation can be found here:

```
http://localhost:8000/docs
```

## Presentation draft

[link](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/ProjectOr.pdf)

# Weekly commitments

## Individual contribution of each participant

**Timur Nabiullin**: 
- created draft presentation,
- made final steps in deployment infrastructure

**Almaz Andukov**:
- Add filtering of projects by tags
- Implement rejection/acceptance of developer's application
- Project closure

**Nikita Timofeev**:
- implemented an interface for sending an application to a project
- added viewing applications (founder only)
- added func to list of projects filtered by tags
- created a displaying the project status

**Kirill Karsakov**: 
- added functionality for deleting an application to join a team
- added generation of project tags based on the description
- added the ability to delete a project for the CEO
- added functionality for sending feedback when a project is approved
- Wrote a report

## Plan for Next Week

- One last run-through of the presentation and demo
- Ensure the demo environment and any required software are working perfectly
- Present project clearly and confidently
- Conduct a smooth live demo of the key functionalities
- Be prepared for a Q&A session

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).