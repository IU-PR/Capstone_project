---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

- **Code repository**: https://github.com/IU-Capstone-Project-2025/verilog-contest

- **Specifications**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/specifications.md

- **List of links related to the project**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/related-materials.md

- **User flow**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/user-flow.png

- **Architecture diagram**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/architecture-diagram.png

- **System architecture specification**: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/system-architecture.md


### Prioritized backlog

Non-public kanban-board in Linear.
Here is screenshot: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/dev/docs/docs/kanban.png

## Project specific progress

### Frontend

Now we have basic design of pages: auth, personal account, contest list and description. 

### Backend

We have CRUD for users and tasks backend service and Swagger spec.

### DevOps
We have Dockerfiles, docker-compose with GoTrue, CI/CD.



# Weekly commitments

## Individual contribution of each participant

| Team Member            | Week #1 Contributions                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| **Mikhail Panteleev**  | Basic design of all pages for frontend, start backend integration, architecture diagram.                        |
| **Vladislav Merkulov** | CRUD in backend and tests for them.                       |
| **Aleksei Fominykh**   | Docker-compose and .env set up, Dockerfiles, add Redis, MinIO, PostgreSQL.                                  |
| **Sofia Kulagina**     | Set up .env, CI/CD for backend and frontend.             |
| **Diana Yakupova**     | New user flow, architecture diagram, prioretized backlog with acceptance criteria, organize 2 meetings. |


## Plan for Next Week

We plan to deploy out MVP with login and sign up, auth in backend and frontend, with solving and sending contest's solution without result of tests, to start Kuber setting up and after this to check CI/CD.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).