---
title: "Week #4"
---

# **Week #4**

## End-to-end MVP testing results

End-to-end testing was conducted this week. Several bugs were identified. Some of them were already fixed, other added to TODO list of the project.
1. **Frontend:** 
    - during registration tags are not sent to the backend (fixed)  
    - sometimes the registration page resizes (to be fixed)
2. **Backend:**
    - error in the response format while matching (fixed)
3. **ML (matchmaking):**
    - Docker build fails (fixed)

## Testing and QA

### 1. Mapper Layer

- **Purpose:** Tests mapping between `Profile`, `ProfileDto`, and `ProfileRequest` objects.

---

### 2. Controller Layer

- **Purpose:** Tests the REST controller endpoints for profile management.

---

### 3. Exception Handling

- **Purpose:** Tests custom exception classes for correct behavior.

---

### 4. Facade Layer

- **Purpose:** Tests the business logic layer that coordinates between service and mapper.

---

### 5. Service Layer

- **Purpose:** Tests the core profile service logic and the tag management service logic.

---

### 6. Integration Layer

- **Purpose:** Integration tests for the interaction between service, facade, and mapper layers (using mocks, not a real DB).
- **Key Test Cases:**
  - Full workflow for creating, retrieving, updating, and deleting profiles.
  - Ensuring correct propagation of exceptions and validation logic.
  - Verifying that peer IDs are set and validated correctly across layers.

---

**Note:**
- All tests use JUnit 5 and Mockito for mocking dependencies.
- Assertions are performed using AssertJ for fluent and readable test code.
- The tests cover both positive (success) and negative (error/exception) scenarios for robust validation.

### Evidence of test execution

Tests logs can be found [here](https://drive.google.com/drive/folders/1dqZ3wRcBZBEANc1QK3rzZCHOV1X0PUOW?usp=sharing)

## CI/CD

### Tools Used

- **GitHub Actions**: Automates CI/CD workflows.
- **Docker & Docker Compose**: Containerizes and orchestrates all services.
- **Docker Buildx**: Enables advanced and multi-platform Docker builds.
- **Docker Hub**: Stores and distributes Docker images.
- **appleboy/ssh-action**: Executes remote deployment commands over SSH.
- **GitHub Secrets**: Securely manages credentials and sensitive data.

---

### CI Workflow

**File:** `.github/workflows/CI.yml`  
**Trigger:** On pull requests to `main` or `dev` branches.

#### Steps

1. **Checkout code** from the repository.
2. **Set up Docker Buildx** for advanced image building.
3. **Create `.env` file** using secrets for environment variables.
4. **Build and start containers** with `docker compose -f compose-dev.yaml up -d --build`.
5. **Wait for containers** to initialize.
6. **Show logs** for all services to aid debugging.
7. **Validate containers**:
    - Ensure all critical containers are running.
    - Check that required ports are exposed.
    - Fail if any container exited with a non-zero status.

[Example of CI test log](https://github.com/IU-Capstone-Project-2025/RandomCoffee/actions/runs/16030019156/job/45227885961?pr=33)

---

### CD Workflows

#### Production Deployment

**File:** `.github/workflows/CD.yml`  
**Trigger:** On push to `main` branch.

Steps
1. **Checkout code**.
2. **Set up Docker Buildx**.
3. **Login to Docker Hub** using secrets.
4. **Build and push Docker images** for all services with `latest` tags.
5. **Deploy to production server**:
    - SSH into the server using `appleboy/ssh-action`.
    - Pull the latest images.
    - Restart services with `docker compose up -d`.

---

#### Staging Deployment

**File:** `.github/workflows/CD-stage.yml`  
**Trigger:** On push to `dev` branch.

Steps
1. **Checkout code**.
2. **Set up Docker Buildx**.
3. **Login to Docker Hub** using secrets.
4. **Build and push Docker images** for all services with `-stage:latest` tags.
5. **Deploy to staging server**:
    - SSH into the server using `appleboy/ssh-action`.
    - Pull the latest images.
    - Restart services with `docker compose up -d`.

---

### Security

- All sensitive data (Docker Hub credentials, SSH keys, environment variables) are managed securely using **GitHub Secrets**.

---

### Challenges faced

- At first, we have rent a virtual machine with not enough memory capaсity. As we use memory-intensive libraries, images consume a lot of memory. That's why we had to rent another virtual machine.

---

#### Links to CI/CD configuration files

- [CI](https://github.com/IU-Capstone-Project-2025/RandomCoffee/blob/main/.github/workflows/CI.yml)  
- [CD production](https://github.com/IU-Capstone-Project-2025/RandomCoffee/blob/main/.github/workflows/CD.yml)
- [CD staging](https://github.com/IU-Capstone-Project-2025/RandomCoffee/blob/main/.github/workflows/CD-stage.yml)

## Deployment

### Production

#### Virtual machine on linux setup
- Docker & Docker Compose have been installed and configured on the server.
- Created directory `/prod`.
- The private/public key pair has been generated.
- The public key has been added to the server’s `~/.ssh/authorized_keys`.
- The private key has been added to GitHub Secrets.
- `PROD_HOST`, `PROD_USER`, and `PROD_PORT` have been added to GitHub Secrets for server connection details.
- On the server in directory `/prod` file `compose.yaml` has been created.
- `.env` file has been created in the same directory.
- Staging CD was set up to restart containers on every push to main 

### Staging
- On server created directory `/stage`.
- `STAGE_HOST`, `STAGE_USER`, and `STAGE_PORT` have been added to GitHub Secrets for server connection details.
- On the server in directory `/stage` file `compose.yaml` has been created.
- `.env` file has been created in the same directory.
- Staging CD was set up to restart containers on every push to dev 

Staging and production environment setups are similar: they both represent containers on the same virtual machine. Stage environment is useful when we need to check how will the project look like on production and find and fix bugs in advance.

### Public domain name
We have bought public domain name on `reg.ru`. Domain name (`therandomcoffee.ru`) allows us to issue an SSL cetrificate for the mini-app, but still the website will be availabale only through Telegram.  


---

Telegram bot: [@random_coffee_iu_bot](https://t.me/random_coffee_iu_bot)


## Vibe Check

Vibe check was conducted on June, 30.

### 1. General Overview

We’re currently at the end of **Week 4 out of 7** in our practicum project. The team has made significant progress after a slightly delayed MVP delivery. Originally planned for Week 3, the MVP was finalized and submitted in Week 4. Everyone is adapting to new responsibilities outside their comfort zones, and despite the learning curve, overall engagement remains strong.

---

### 2. MVP Status

- **MVP completed** on Week 4 (1 week later than planned).
- Delay was due to the technical uncertainty.
- Everyone contributed to the MVP and now has a clearer understanding of the next iteration.

---

### 3. Team Dynamics

#### What’s Working
- **Collaboration**: Communication within sub-teams (backend/frontend and DS pair) is improving.
- **Initiative**: Team members have shown ownership, e.g., proposing better matching algorithms, frontend UI tweaks.
- **Morale**: Despite some hiccups, morale is fairly positive, with people excited about moving forward.

#### Areas to Improve
- **Cross-role alignment**: Miscommunication between frontend/backend and DS on data flow/API expectations.
- **Planning detail**: Tasks are sometimes too vaguely defined, leading to different interpretations.
- **Time estimation**: Underestimated time needed for MVP features, especially on backend + ML integration.

---

### 5. Roadblocks

- Integration between components (especially ML → Backend → Frontend) still needs clearer protocols and division of responsibilities.
- Syncing availability across different schedules has made meatups more difficult.

---

### 6. Action Points (Going Forward)

1. **Clarify Interfaces**: Set up short 30-min alignment meetings between DS, Backend, and Frontend to define API/data formats clearly (Done).
2. **Break Down Tasks**: Smaller, more specific tickets with clearer DoD (Definition of Done).
3. **Adjust Expectations**: Accept that some scope trimming might be needed in the final two weeks to ensure polish.
4. **Celebrate Small Wins**: MVP is a major milestone—take a moment to appreciate the progress before charging ahead.
5. **Retrospective Session**: Plan for a mid-week informal retro + planning combo to re-scope remaining work (Done).

---

### 7. Mood Check (Informal Poll)

We did a quick vibe check using an anonymous 1–5 scale in our telegram group:

- **Team Stress Level**: Avg. 3.4  
- **Team Motivation**: Avg. 4.6  
- **Confidence in Delivering**: Avg. 5.0  

Overall, the team is motivated but slightly stressed. This is expected for mid-project crunch. Main stressors are integration challenges and tight deadlines.


# Weekly commitments

## Individual contribution of each participant

1. **Anastasia Mitiutneva**:  
Reviewed each pull request  
Conducted the second internal demo of the MVP  
Set up CI/CD  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/10)  
Set up deployment for production and staging environment (see section "Deployment")  
[Pull Request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/33)  
Conducted a Vibe Check (see section "Vibe Check")  
Identifed future plans for each team.  
2. **Maksim Al Dandan**:  
Bug fixes after the internal testing  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/30)  
Added API integration with ML service  
[Pull Request 2](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/31)  
Unit/Integration tests implementation  
[Pull Request 3](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/38)
3. **Aleksandr Andreev**:  
Added API integration with backend services  
[Pull Request 1](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/32)  
Bug fixes after the internal demo  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/34)  
Rented a virtual machine, set it up for our project (installed docker, opened ports), configured public domain name   
4. **Ivan Ilyichev**:  
Huge bug fixes after the internal testing and Matchmaking models validation, metrics creation, visualizations with Rail  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/31)
5. **Rail Sabirov**:  
Matchmaking models validation, metrics creation, visualizations with Ivan. Relevant `.ipynb` file can be found <u>[here](https://github.com/IU-Capstone-Project-2025/RandomCoffee/tree/main/ml/match_making/models_validation)</u>  
[Pull Request](https://github.com/IU-Capstone-Project-2025/RandomCoffee/pull/37)



## Plan for Next Week

### Each team:  
 - Conduct usability testing session  

### Backend:  
 -  Start implementing Scheduler (algorithm that will start matchmaking weekly and send notifications to user)
 - Store information about user participation and a goal for the meeting

### Frontend:  
- Questionnaire about user participation and goal for the week
- "View partner's profile" page
-  Add alias and avatar for partner user

### ML/Data Science:  
- Matchmaking algorithm considers user goal
- Tags validation model

### Product manager
- Feedback Analysis & Prioritization


## Confirmation of the code's operability

We confirm that the code in the main branch:  
✅ In working condition.  
✅ Run via docker-compose (see `README.md`).  