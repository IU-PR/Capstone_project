# Week 4
## Testing and QA
### Test Coverage
Implemented comprehensive test suites covering:
- `test_bookings`: Booking lifecycle (create/read/update/delete)
- `test_books`: CRUD operations with library associations  
- `test_libraries`: Location management and city listings  
- `test_managers`: Role-based access control  
- `test_search`: Filtering by title/author/genre  
- `test_users`: Registration, authentication, and profile management  

### Test Types
✅ **Integration Tests**  
- API endpoint validation with status code checks  
- Database interaction testing via `AsyncClient`  
- Cross-entity dependencies (e.g., bookings require users/books)  

✅ **Functional Tests**  
- CRUD workflows for all core entities  
- State transitions (e.g., booking status changes)  
- Edge cases (404 handling, duplicate prevention)  


## Evidence of test execution
### Code coverage report
**Total coverage**: 52% (13/25 test suites)  

| Module          | Coverage | Remarks                                 |
|-----------------|----------|-----------------------------------------|
| `test_bookings` | 33%      | ✅ Basic CRUD operations tested          |
| `test_books`    | 66%      | ✅ CRUD operations + cover upload tested |
| `test_libraries`| 66%      | ✅ CRUD operations                       |
| `test_managers` | 33%      | ✅ Basic role access control tested                                        |
| `test_search`   | 33%      | ✅ Basic search functionality tested                                        |
| `test_users`    | 50%      |  	✅ User registration, login, profile CRUD, and book like/unlike functionality tested                                       |
## CI/CD 
**CI (Continuous Integration)**

For CI, we maintain a dedicated test database, which was migrated from the main production database. This environment is used to verify endpoint functionality. Our backend developer wrote automated tests using pytest. These tests perform actions such as creating or deleting objects and then assert that the returned status codes match the expected values. Sensitive keys required for testing are securely stored in GitHub Secrets.

**CD (Continuous Deployment)**

Continuous deployment is triggered automatically whenever changes are pushed to the main branch. A GitHub Actions job connects to the remote server via SSH, using a private key stored in GitHub Secrets. On the server, the workflow navigates to the project directory, performs a git pull, stops any running containers, and then rebuilds and restarts the application using docker-compose up -d --build.
### Links to CI/CD configuration files 

[CI/CD configuration file (deploy.yml)](https://github.com/IU-Capstone-Project-2025/libnet/blob/main/.github/workflows/deploy.yml
)


## Deployment 
#### Staging Environment
**Process**:  
- Automated CI/CD pipeline via GitHub Actions  
- Trigger: Push to `main` branch  
- Workflow: [`deploy.yml`](https://github.com/IU-Capstone-Project-2025/libnet/blob/main/.github/workflows/deploy.yml)  

**Key Steps**:  
1. GitHub runner executes build/test stages  
2. SSH connection to server using deploy keys  
3. Container orchestration:  
   - Pulls latest Docker images  
   - Graceful container restart  

**Tech Stack**:  
- GitHub Actions (CI/CD)  
- Docker containers  
- SSH key authentication  


## Vibe Check
### Progress  
This week, the team completed key frontend features including the admin login system, dashboard with library management, library editing, dynamic manager loading, and search/filter functionality. Adaptive styling was implemented with responsive breakpoints, and the admin panel interface was refined. The domain name was purchased and configured. On the backend, testing tasks were completed, and a new endpoint was created to display books without duplicates. Additionally, CI was configured, and a logging and monitoring system was set up. 
#### Frontend  
✅ Adaptive styling & breakpoints  
✅ Admin panel: login, dashboard, library editor  
✅ Search/filter UI  

#### Backend  
✅ Search/filter API  
✅ Book deduplication endpoint  

#### DevOps  
✅ Domain configuration  
✅ Logging/monitoring setup  
✅ CI pipeline  

#### Documentation  
✅ Report completion  
✅ README updates  

### Roadblocks
**Skill Gap Adaptation**  
- Team members are encountering role-first challenges due to limited prior experience in:  
  - Specific tech stack implementations  
  - Domain-specific problem solving  
- Current mitigation:  
  - Peer knowledge sharing sessions  

**Novelty Factor**  
- High frequency of first-time scenarios requiring:  
  - Extended research phases  
  - Iterative solution validation 
### Team Dynamics 
**Current State**:  
- High workload, but maintaining delivery pace.
- Shared fatigue with positive attitude. 

**Support Needed**:  
- Prioritization review to balance tasks.
## Weekly commitments 
### Individual contribution of each participant
| Team Member     | Completed Work                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ivan Murzin     | [Implemented adaptive styling.](https://github.com/IU-Capstone-Project-2025/libnet/commit/4f91bcb1d96d49995247de019cb8879b3a2d67af) [Added breakpoints for different screen sizes.](https://github.com/IU-Capstone-Project-2025/libnet/commit/4f91bcb1d96d49995247de019cb8879b3a2d67af) [Styled the admin panel interface. Refined the styling for most pages.](https://github.com/IU-Capstone-Project-2025/libnet/commit/fc6295b7e4e2a87550e3a632f5bc6923f169b25c) [Purchased and configured a domain name.](https://github.com/IU-Capstone-Project-2025/libnet/commit/b6b5ee51ec276c34caf5e341ea2b401e21cdc397) |
| Aliya Sagdieva  | Compiled the complete report. [Updated the information in the README.](https://github.com/IU-Capstone-Project-2025/libnet/commit/e9feefc236c67ba38c16932d71a208f199f22262)                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Alena Averina   | [Set up a logging and monitoring system.](https://github.com/IU-Capstone-Project-2025/libnet/commit/7054ffb582d041bfb056186d6f9453369af1a922) [Сonfigured CI.](https://github.com/IU-Capstone-Project-2025/libnet/commit/e5c8a5e75a3f8fb40f9b2369e84e485e5a751edb)                                                                                                                                                                                                                                                                                                                                                |
| Anna Serova     | Implemented the complete frontend for the following features: [Admin login system; Admin dashboard with libraries section;](https://github.com/IU-Capstone-Project-2025/libnet/commit/b2229567e6557a6c73770c79c8d2574e10319a3c) [Library editing page;](https://github.com/IU-Capstone-Project-2025/libnet/commit/b2229567e6557a6c73770c79c8d2574e10319a3c); [Search and filter functionality.](https://github.com/IU-Capstone-Project-2025/libnet/commit/2aa3a63c3de60472b17516d629126f3257dff8b9)                                                                                                               |
| Artem Ostapenko | [Implemented all the testing tasks assigned for this week.](https://github.com/IU-Capstone-Project-2025/libnet/pull/36) [Developed search and filter functionality.](https://github.com/IU-Capstone-Project-2025/libnet/commit/7781ca7de6b7a610b9a9fd8540d4574d4b147cc4) [Created an endpoint to display books without duplicates.](https://github.com/IU-Capstone-Project-2025/libnet/commit/aaa11c6b58220def3502d18b27f3d010cb7cbbaa) <br/>                                                                                                                                                                     | 
### Plan for Next Week
#### Frontend Development
- [ ] **Feature Completion**
  - Book addition form
  - Library management UI
  - Manager assignment flows

#### Backend Development
- [ ] **Performance & Testing**
  - Load testing script implementation
  - Ollama integration research
- [ ] **Maintenance**
  - Bug fixes (if identified)
### Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md). 

