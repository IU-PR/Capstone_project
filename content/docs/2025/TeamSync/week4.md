# Week 4

## Testing and QA

Most of the test are unit tests to validate implementation of a single class or method. It is easy and fast to implement, what’s more it will be usefull, if we broke something in code and we need to know what exactly gone wrong. We also added some intergation tests that launch whole service with some other servies (for example, PostgreSQL in container). We need them to validate global user flow on concreate endpoint. For the beginning, we decided to reach 20% of line coverage, we will increase this floor in future. 

### Evidence of test execution

We used JacocoTest Report for test coverage report. It generates some xml file that contains needed info. But anyways, we can always use the IDE’s built-in instruments to check the coverage:
 

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week4/image.png?raw=true)

Regarding CI, we run test on each push to merge request and provide some report as comment:

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week4/image%201.png?raw=true)

We also added docker-compose validation

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week4/image%202.png?raw=true)

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week4/image%203.png?raw=true)

The worflow prints the coverage to logs:

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week4/image%204.png?raw=true)

## CI/CD

We are using GitHub Actions to run the pipelines:

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week4/image%205.png?raw=true)

We have a remote machine to deploy **prod** and **dev** version. Deploy workflows do not run automatically, because our machine can be downed if we  will spam it. So, we run these scripts manually to prevent spamming. In deploy scipts we connect to the remote machine via ssh and use special .sh scripts. Script stops the docker compose,  switch to the needed branch, and starts docker compose again.

**test-*** workflows run on every push to merge request and master branch. We described them before. 

LINK: [CI/CD workflows](https://github.com/IU-Capstone-Project-2025/team-sync/tree/main/.github/workflows)

## Deployment

Globally, we described the process of deployment before.

We have two docker compose files - for prod and dev versions to run different containers with different volumes and networks. We also added .env files to repository’s clone in remote machine to store secrets and other environment dependent stuff. 

After all, we have [team-sync.online](http://team-sync.online) for production, [dev.team-sync.online](http://dev.team-sync.online) for testing (staging), and [pgadmin.team-sync.online](http://pgadmin.team-sync.online) for database administration.

## **ML**

This week, the ML team researched which metrics are the most relevant for our project [TS-156]. We chose MAP@10 (easy to interpret and calculate), nDCG@10 (shows how good the ranking in the list is), and MRR@10 (shows when the first relevant item occurs). We also implemented a class for these metrics [TS-146-163]: [PR-51](https://github.com/IU-Capstone-Project-2025/team-sync/pull/51). However, we encountered some problems with automating it.

The first issue is that indexes can change, so we are not sure whether a certain project will still belong to the user. The second issue is that the current dataset will be deleted when we publish our project to production, so we can’t use it in this way right now. So we took 3 different users,  and tried to manually predict if project is relevant or not. At the end of this manipulation we got the following results: (MAP): 0.7653439153439153, (NDCG): 0.8729514321708831, (MRR): 0.8333333333333334.

Nevertheless, the ML team slightly refactored the tag-based part of the recommender system [TS-111]. We also researched algorithms for it [TS-165]. We considered different models: neural networks are not suitable at this point since skills are addable and it is very expensive to retrain them every time; boosting algorithms could be used as predictors for what skill will be taken next given the current state, but they also require retraining, so they are still a bad option.

The best option for now is clustering + TF-IDF: we plan to treat clusters as documents. Our hypothesis is the following: every cluster corresponds to one role - e.g., the first cluster for ML engineers, the second for backend developers, etc.

## Frontend

Over the course of this week, I made tests for the crucial components of the frontend and the authorization configuration script ([TS-167](https://team-sync-capstone.atlassian.net/browse/TS-167)), fixed projects not showing up on the main page ([TS-102](https://team-sync-capstone.atlassian.net/browse/TS-102)), made it so the frontend works with the newly deployed website and fixed other bugs (impossible to go back to the home page from the create project page ([TS-175](https://team-sync-capstone.atlassian.net/browse/TS-175)), impossible to reload home page([TS-174](https://team-sync-capstone.atlassian.net/browse/TS-174)). Most of the week was spent debugging, since several bugs made it impossible to display the MVP the week before. The projects not showing up on the home page was the main problem of the week, since it was an issue with asynchronous functions. 

## Transcript and summary of meeting with stakeholders

### **Current Challenges & Workflow**

1. **Manual Process**:
    - Relies on Google Forms for student preferences, followed by manual clustering/assignment.
    - 10-20% of students remain unassigned due to mismatched preferences ("50 people with all different choices").
2. **Imbalance Issues**:
    - High demand disparity: Some projects get 10+ team requests, while others get zero, risking customer dissatisfaction.
    - Customers have team limits (e.g., "customer A can take only three teams").
3. **Limited Analysis**:
    - No capacity to balance teams by skills, gender, or background.
    - Student skill data (e.g., technical stacks) is collected but ignored due to lack of analysis tools.
4. **Student Frustration**:
    - "Students would cry if not in the team they want."

### **Expected Solutions from TeamSync**

1. **Automation & Matching**:
    - Fully automate team formation to replace manual clustering.
    - Prioritize **skill-based matching** over preference-only:*"Match students and projects based on technical skills and project wishes, not team preferences."*
2. **Analytics & Alerts**:
    - Highlight unassigned students, skill gaps, or role mismatches.
    - Flag inconsistencies (e.g., if a student claims C++ proficiency but has a poor grade in related courses).
3. **Integration**:
    - Sync with the university’s **digital profile** for skills, grades, and project history (e.g., thesis/capstone projects).*"Show grades near claimed skills (e.g., Databases course grade next to SQL skill)."*
    - Allow skill data to be **editable** by students (as digital profiles may be outdated).
4. **Flexibility**:
    - Let instructors "lock" or manually adjust teams post-automation.
    - Support non-technical projects (some "don’t require any skills").

### **Critical Requirements**

- **Core Value**:
    
    > "Reasonable and correct suggestions/solutions" based on student inputs (preferences + skills).
    > 
- **Features**:
    - Student-facing input forms + admin-facing assignment dashboard.
    - Filters for courses/skills/roles (with fallbacks for skill-agnostic projects).
    - Web-based (not local) for accessibility.
- **Privacy/Technical**:
    - Minimal data: Email suffices; no sensitive data needed.
    - No stack restrictions ("doesn’t matter for us").
- **Pilot Support**: Stakeholder willing to test an internal version.

### **Additional Insights**

- **Unified Platform**: Interest in merging SWP/capstone/thesis projects into one system.
- **Skill Validation**: Use course grades to surface warnings (not auto-exclusions) for manual verification.*Example: "If a student claims C++ but has a low grade, alert teachers to confirm proficiency."*
- **Stakeholder Pain Point**:
    
    > "Today was my non-working day... turned into a fully working day" → Emphasizes need for efficiency gains.
    > 

### **Next Steps Supported**

- Pilot testing and integration with university systems (digital profile).
- Collaboration to refine skill-matching algorithms and analytics.

## Management changes

Following the MVP development week, we recognized the need to improve our workflow. As a result, we began managing our User Stories and Acceptance Criteria directly in Jira, organizing them into structured subtasks. This change provided greater clarity, improved task ownership, and helped us better understand the overall project structure.

## Vibe Check

Overall, the team is feeling positive and motivated. Most members are in a good working rhythm, though there were some temporary setbacks: one of our frontend developers was sick, and our ML developer is just recovering after being unwell. Other team members are currently facing multiple academic deadlines, which added some pressure during the sprint.

Despite that, we made a strong effort to complete as much work as possible. To lift the mood after a not-so-smooth MVP demo, we had a relaxed team meeting with tea and sweets kindly brought by Liza — it helped us reset and support each other.

# Weekly commitments

## Individual contribution of each participant

| Team member | Contribution | Jira tasks |
| --- | --- | --- |
| Diana MInnakhmetova (Lead) | Held 3 meetings, made design improvements, analyzed meetings with stakeholders, managed improvements in team work | TS-176, TS-170, TS-171, TS-172 |
| Danis Sharafiev | Implement basic model validation/testing, Define a set of metrics, research algorithms to improve tag-based, Create a tool to calculate metrics (all info in ML paragraph) | TS-146, TS-156, TS-163. TS-165 |
| Daria Alexandrova | Unit tests, make it possible to go back to the home page from the project creation page, fixing problems from the previous week
*(She was sick for 4 days of the sprint)* | TS-167, TS-175, TS-174. [PR-54](https://github.com/IU-Capstone-Project-2025/team-sync/pull/54), [PR-55,](https://github.com/IU-Capstone-Project-2025/team-sync/pull/55) [PR-56](https://github.com/IU-Capstone-Project-2025/team-sync/pull/56) |
| Stepan Dementev | [Updated security filtering](https://github.com/IU-Capstone-Project-2025/team-sync/pull/44/files), [Added sample tests for Liza](https://github.com/IU-Capstone-Project-2025/team-sync/pull/45), [Initialized CI/CD + prepared nginx on remote machine for deployment](https://github.com/IU-Capstone-Project-2025/team-sync/pull/46), [Created template for tests in CI](https://github.com/IU-Capstone-Project-2025/team-sync/pull/49), [Released new resume service](https://github.com/IU-Capstone-Project-2025/team-sync/pull/57) + bugfixing | TS-110, TS-115, TS-116, TS-173, TS-161, TS-147, TS-153, TS-162, TS-154, TS-160 |
| Elizaveta Zagurskih | Added custom logging to backend services ([PR-43](https://github.com/IU-Capstone-Project-2025/team-sync/pull/43), [PR-52](https://github.com/IU-Capstone-Project-2025/team-sync/pull/52)), implemented integrated and unit tests for resume service ([PR-53](https://github.com/IU-Capstone-Project-2025/team-sync/pull/53)), refactored the auth service registration to delegate all user creation to the Resume service via HTTP calls ([PR-43](https://github.com/IU-Capstone-Project-2025/team-sync/pull/43)) | TS-159, TS-166, TS-113, TS-112 |
| Kamilya Shakirova | Fix methods in DB class, Fix redis in models( all info in ML paragraph) | TS-108, TS-109 |

## Plan for Next Week

### Backend

- Complete logic for applications for project owners in Projects service
- Add tests
- Release recommendation service

### Design

- “Student dashboard” page
- “Onboarding” page
- “Notification” page
- “Favorite projects” page

### Frontend

- "My projects" page
- "My responces" page
- Applying for project
- Decline/Approve project request
- "Favorite projects" page
- "Student dashboard" page

### ML

- Optimization of Docker containers
- Replacing FAISS with Qdrant for vector search
- Integrating Airflow and Postgres into the main database
- Adding caching for description-based recommendations
- Implementing the researched algorithm for tag-based recommendations
- Creating a new module in the recommendation system for role-based matching
- Adding a basic search system to the platform

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [ ]  In working condition.
- [ ]  Run via docker-compose (or another alternative described in the `README.md`).