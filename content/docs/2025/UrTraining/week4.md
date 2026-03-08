# Report 4. Testing, CI/CD & Deployment Setup

# UrTraining

**Authors:** Ildar Rakiev, Makar Dyachenko, Salavat Faizullin, Egor Chernobrovkin, Alexandra Starikova, Ilona Dziurava, Anisya Kochetkova

**Date:** July 2025

# Team Members

| **Team Member**     | **Telegram**   | **Email Address**                    | **Role**          |
| ------------------- | -------------- | ------------------------------------ | ----------------- |
| Ildar Rakiev (Lead) | @mescudiway    | i.rakiev@innopolis.university        | Backend / Frontend|
| Makar Dyachenko     | @index099      | m.dyachenko@innopolis.university     | Frontend / Design |
| Salavat Faizullin   | @FSA_2005      | s.faizullin@innopolis.university     | Backend           |
| Egor Chernobrovkin  | @lolyhop       | e.chernobrovkin@innopolis.university | ML                |
| Alexandra Starikova | @lexandrinnn_t | a.nasibullina@innopolis.university   | ML                |
| Ilona Dziurava      | @a_b_r_i_c_o_s | il.dziurava@innopolis.university     | PM                |
| Anisya Kochetkova   | @anis1305      | a.kochetkova@innopolis.university    | Testing           |

---

# Implemented features

**Visualization:**  
The user flow diagram can be seen below, the non-implemented features are highlighted in red:
![Flow1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/flow3.png)
![Flow2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/flow4.png)

## Implemented Features:

### 1. Advanced trainer registration
![Start](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Startoftrainerregistration.gif)
![Step1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Advancedtrainerregistrationform-step1.png)
![Step2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Advancedtrainerregistrationform-step2.png)

### 2. Editing of trainer registration
![edit](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Endingoftrainerregistration.gif)

### 3. Training Uploading

Training uploading:
![upload](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Traininguploading.gif)

Training uploading (success case)
![upload2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/Traininguploading(successcase).gif)


### 4. AI assistants

- An AI Assistant that pops up in the window when choosing courses.
  
**Commits:** [AI Assistant implementation](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/65/commits/f8678dfd6637d5fccb24c1e836a5d3010f47fd0d)
  
- An AI Assistant that pops up in the window after clicking on the course. The main difference between this assistant is that it has a complete description of the program that the user is watching.
  
**Commits:** [AI Assistant implementation](https://github.com/IU-Capstone-Project-2025/UrTraining/tree/main/ml/course-assisstant)

![AI-assistant](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/ai-assistant.png)


---
# CI/CD Pipeline Documentation

### 1. Pipeline Overview

#### Deployment Targets
| Service | Path | Technology | Deployment Method |
|---------|------|------------|-------------------|
| Backend | `backend/` | Docker | SSH + Docker Compose |
| Frontend | `frontend/` | Vite + Nginx | SSH + File Copy |
| Image2Tracker | `ml/image2tracker/` | Docker | SSH + Docker Compose |
| Vector DB | `ml/vector-db/` | Docker | SSH + Docker Compose |

### 2. Workflow Configuration

#### Common Structure
All workflows share the same trigger pattern: pull request with ```main``` branch or push to this branch.
```yaml
on:
  push:
    branches: [ "main" ]
    paths: [ "service_path/**" ]
  pull_request:
    types: [closed]
    branches: [ "main" ]
    paths: [ "service_path/**" ]
```

#### Key Components
1. **Conditional Execution**:
   ```yaml
   if: |
     github.event_name == 'push' ||
     (github.event_name == 'pull_request' && github.event.pull_request.merged)
   ```

2. **SSH Deployment**:
   ```yaml
   uses: appleboy/ssh-action@v1.0.3
   with:
     host: ${{ secrets.SSH_HOST }}
     username: ${{ secrets.SSH_USER }}
     key: ${{ secrets.SSH_KEY }}
   ```

Here's a polished version of the third section with clear technical explanations:

### 3. Deployment Processes

#### For Backend and ML Services (Dockerized)
Each Docker-based service follows this robust deployment sequence:

1. **Code Synchronization**  
   The pipeline first pulls the latest `main` branch to ensure the server has all recent commits:
   ```bash
   cd ~/UrTraining
   git pull origin main
   ```

2. **Container Management**  
   Using Docker Compose for deterministic deployments:
   ```bash
   cd service_directory
   docker-compose down            # Graceful shutdown
   docker-compose build --no-cache # Clean rebuild
   docker-compose up -d           # Daemonized startup
   ```
   Key notes:
   - `--no-cache` prevents cached layers from causing inconsistencies
   - `-d` flag runs containers in detached mode

3. **Atomic Deployment**  
   The entire process is wrapped in a `flock` mutex lock to prevent concurrent deployments:
   ```bash
   flock /tmp/service-deploy.lock -c '...'
   ```

#### For Frontend (Static Assets)
The frontend deployment takes a different approach:

1. **Build Process**  
   Creates production-optimized assets:
   ```bash
   npm install              # Ensures fresh dependencies
   npm run build            # Generates /dist directory
   ```

2. **Atomic File Replacement**  
   Safely updates live assets without downtime:
   ```bash
   sudo rm -rf /var/www/myfrontend/*     # Clean deploy
   sudo cp -r dist/* /var/www/myfrontend # Atomic copy
   sudo systemctl restart nginx          # Graceful reload
   ```

**Critical Design Aspects**:
- All file operations use `sudo` to ensure proper permissions
- Nginx restart is instantaneous to end-users
- The entire process is logged for audit purposes

### 4. Critical Features

#### Deployment Safety Mechanisms
1. **File Locking**:
   ```bash
   flock /tmp/service-deploy.lock -c '...'
   ```
2. **Logging**:
   ```bash
   LOG_FILE=~/deploy-service.log
   {
     # Deployment commands
   } >> $LOG_FILE 2>&1
   ```

#### Error Handling
- `set -e` in scripts fails on first error
- All Docker commands run in sequence with error checking

#### 5. Environment Details

#### Server Requirements
- Docker + Docker Compose installed
- Nginx for frontend
- SSH access configured
- Directory structure:
  ```
  ~/UrTraining/
    ├── backend/
    ├── frontend/
    ├── ml/
    │   ├── image2tracker/
    │   └── vector-db/
  ```

### 6. Troubleshooting

#### Common Issues
1. **SSH Connection Failures**:
   ```bash
   ssh -v $SSH_USER@$SSH_HOST
   ```
2. **Docker Build Errors**:
   ```bash
   docker system prune -a
   docker-compose build --no-cache
   ```

#### Log Locations
```bash
~/deploy-backend.log
~/deploy-vector-db.log
~/deploy-image2tracker.log
/var/log/nginx/error.log
```

### **Problems and solutions**:
| Problem                         | Our solution                                                                 |
|-----------------------------------|-------------------------------------------------------------------------|
| Ports conflicts when deploying | Unique ports are assigned (backend: `8000`, vector-db: `1337`).           |
| Long dependency installation | Added caching for `npm` and `pip`.                               |
| Problems with synchronization of deployment on the server from different pipelines | Special `flock` blocks were added to avoid problems with simultaneous deployment |
| Errors during SSH deployment | A separate SSH user with limited rights is configured.           |
 Errors during frontend deployment (`dist` directory cannot be copied to server correctly) | Local building to avoid copying errors (temporary solution)           |

---

### 7. Maintenance

#### Secret Rotation
1. Updated information GitHub Secrets, especially Actions secrets:
   - `SSH_HOST`
   - `SSH_USER`
   - `SSH_KEY`

#### Update Procedure
1. Modify workflow files in `.github/workflows/`
2. Test via PR to non-main branch (trigger PRs)
3. Merge to main for production deployment

# CI/CD logs

![back](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/backend-cicd.png)
![back1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/backend-cicd-1.png)
![back2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/backend-cicd-2.png)
![back3](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/backend-cicd-3.png)
![back4](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/backend-cicd-4.png)

![front](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/frontend-cicd.png)
![front1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/frontend-cicd-1.png)
![front2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/frontend-cicd-2.png)
![front3](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/frontend-cicd-3.png)
![front4](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/CI-CDlogs/frontend-cicd-4.png)

# Deploy
Fronted part is deployed [HERE](http://31.129.96.182/).

Backend part is deployed [HERE](http://31.129.96.182:8000/).

ML part is deployed [HERE](http://31.129.96.182:1337/).


# Testing

## Unit tests for critical backend logic

These are unit tests that check the correctness of the database models in our application. General principles of testing:
- Checking the creation of records (whether they are saved correctly in the database)
- Checking the relationships between models (for example, the user_id in the Training Profile)
- Checking default values (for example, is_active=True)
- Checking data types (numbers, strings, lists)

**Commit:** [Unit tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/3ce23e02baa0e31776b745baa0a173653345a468)

![Unit](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/unit.png)

## Integration tests for API endpoints

API tests check all sorts of things with the API, mainly for the correct nature of the entered data, for example, that the user can register, log in, and delete the user from the database

**Commit:** [API endpoints tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d319c58bb6ed1d4554b718ad4ab399adb60ce46f)

![API](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/api_test.png)

## Basic end-to-end tests for the core user journey

Tests covering the trainee journey
- Authentication Flow
- Minimum/maximum values, Optional fields, Long text inputs, Empty fields, Country/city validation
- Survey data
- Profile setup
- View workout details

**Commit:** [End-to-end tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/f81b2a4be7f709a6016c4b37c132527db1bb1d7a)

![end-to-end](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/end-to-end.png)

---

# Vibe check

During the team health check meeting, we aimed to assess our collaboration, communication, and overall team well-being. The discussion revealed several areas for improvement, especially from the online team members. One major concern was the lack of coordination meaning that team members often worked in isolation and contacted only the team lead in case of any problems. There was a shared opinion that the development process lacked transparency, with some features being implemented without others being aware. Team members suggested introducing short update sessions to keep everyone informed and aligned. Another key point was the inconsistency in how pull requests were handled. Some were submitted without titles or descriptions, making it hard for others to review or understand the context. It was agreed that improving PR practices and testing each other’s work would strengthen team dynamics, ensure better code quality, and help everyone feel more included. This health check provided a valuable space for honest feedback and reinforced our commitment to working as a more cohesive and communicative team.

---

# Weekly Progress Report

| Team Member (Role)         | Contribution Description                                                                                                                                             | Contribution Link                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Ildar Rakiev (Backend/Frontend Lead) | Led backend and frontend development of key features including CI/CD pipeline setup, advanced trainer registration with integrated survey, and a training course editor interface.          | [Advanced registration for trainer with servey](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/3d65001453ff7605805e6460cda7525e8ba95484), [Training course editor](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/752372b032bf86247a44472901e76099dd0b63cc), [CI/CD pipelines](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/1687e69084d92dc6557648d45de9051838c27350)         |
| Makar Dyachenko (Frontend/Design) | Developed and styled user interface components including navigation and metadata pages.                                           | [Navbar basic routing](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/337fb802e8f8c80201c7657ec86b50ea053465bc), [Metadata page](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/163eb40c319af64743ffac4c0da6297921ec3e4c)         |
| Salavat Faizullin (Backend)   |    Worked on data validation and backend integrity by adding constraints for city and country fields and fixing issues related to training ID management in the system.                                                                     | [City and country values validation add](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/5ebe83cd95ab32391386167fd90ece339e5e2504), [Fix trainings ids](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/1acca638a200558577bcb8f3c3dd64c894fb0a82)        |
| Egor Chernobrovkin (ML)  | Designed and implemented the AI Assistant for course selection. Developed backend services for BM25 indexing, session tracking, prompt engineering, and user query formatting to support a responsive assistant experience. | [Add MVP for image2tracker](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/505199354df488f2cc07eff11a65e1cfcf3edfed), [Simplify dockerfile](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/b62c2c95ff1bb9a9b8aa63aed014620701b9f63e), [Add BM25 indexing](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/a5a9b5fc47abcedcac2198f4d411535172dd60a8), [Choose course assistant chat endpoint](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/65/commits/f8678dfd6637d5fccb24c1e836a5d3010f47fd0d), [Request/response models for choose course assistant API](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/65/commits/f8678dfd6637d5fccb24c1e836a5d3010f47fd0d), [Choose course assistant system prompt](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/65/commits/f8678dfd6637d5fccb24c1e836a5d3010f47fd0d), [Chat service with session tracking](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/65/commits/f8678dfd6637d5fccb24c1e836a5d3010f47fd0d), [Prompt formatting utility for user inputs](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/65/commits/f8678dfd6637d5fccb24c1e836a5d3010f47fd0d)  |
| Alexandra Starikova (ML) | Contributed to data parsing and management by developing a sketch tool for extracting course data from images, implementing mechanisms for dynamic course data updates, and preparing reference files for bulk data uploads. | [A sketch for parsing programs from images](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/0c15de5e5aeaebe9476faf36f24403e5b5da7947), [Interactive updates of course data](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/b5164ca069a114babaf5dffa9c78060f153719ca), [Reference files for uploading data](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/7ad4a4875c0f262d1ff032a2491823b567fc0f0d)        |
| Ilona Dziurava (PM)      | Prepared the project report, facilitated two team meetings, coordinated task distribution, maintained the product backlog, organized and led a retrospective, and structured the team’s workflow for efficient collaboration | This report :)   |
| Anisya Kochetkova (Testing)   | Implemented testing strategies, including unit, API, and end-to-end tests. Created the AI assistant for the specific course.  | [Unit tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/3ce23e02baa0e31776b745baa0a173653345a468), [API endpoints tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/d319c58bb6ed1d4554b718ad4ab399adb60ce46f), [End-to-end tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/f81b2a4be7f709a6016c4b37c132527db1bb1d7a), [Course assistant chat endpoint](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/91dd1c3bb9161cfcba3114786a5d413538f0ab26), [Request/response models for course assistant API](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/5b6334329816d084ae0960f0bfcca43790800d79), [Course assistant system prompt](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/644a5ee06bb3f299975949dea656c17653c12f24), [Chat service with session tracking](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/63ce4bbd3846b2dc4f13c2d0b0390bce56832444), [Prompt formatting utility for user inputs](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/5171330ad9a0bf638fddc7a9ac8ad28b60aa3803) |

## Challenges & Solutions
The most challenging part of this week was setting up the CI/CD pipeline, as none of the team members had prior experience with it. To overcome this, three team members collaborated closely, sharing research, troubleshooting together, and verifying each step of the setup process. This teamwork ensured the pipeline was configured correctly and became a valuable learning experience for everyone involved.

## Conclusions & Next Steps

By the end of Week 4, we had a stable, tested, and deployed version of our application in a staging environment, complete with CI/CD automation. This allows for updates and reliable testing going forward. Additionally, the trainer user flow was successfully implemented.

### Next Steps for Week 5

- **Implement profile pages**
  - Implement personal profile pages for user ans trainer.
  - Add functionality for profile editing.

- **Feedback Collection:**
  - Share the staging app with external testers.
  - Collect structured feedback through forms.

- **Feedback Analysis:**
  - Document feedback and create actionable issues in the backlog.
  - Prioritize bug fixes and usability improvements.

- **Iteration & Refinement:**
  - Address top-priority feedback, focusing on UI/UX and error handling.
  - Improve frontend responsiveness and backend robustness.
  - Polish documentation (README, API reference).

- **ML Enhancements:**
  - Refine model predictions based on validation outcomes.
  - Explore metrics to evaluate prediction quality and fairness.

Week 5 will focus on improving the product based on the the user experience, resolving known bugs, and improving the overall quality and stability of the product in preparation for final presentation and submission.

**We confirm that the code in the main branch:**

In working condition.
Run via docker-compose.
