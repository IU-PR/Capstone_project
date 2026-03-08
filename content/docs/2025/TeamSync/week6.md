# Week 6

## Links

- **Deployment**: team-sync.online
- **API Docs**
    
    team-sync.online/projects/api/v1/swagger-ui/index.html
    
    team-sync.online/resume/api/v1/swagger-ui/index.html
    
    team-sync.online/auth/api/v1/swagger-ui/index.html
    
- **Design**: [https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=Tv75bgJoMgN6eCPm-1](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=Tv75bgJoMgN6eCPm-1)
- **Demo**: [https://drive.google.com/drive/folders/1SdpeE8VrxILX4vvuD1bGbwB2zZ1zWtPQ?usp=sharing](https://drive.google.com/drive/folders/1SdpeE8VrxILX4vvuD1bGbwB2zZ1zWtPQ?usp=sharing)

## Final deliverables

### **Current implementation**

**Problem**

> Students struggle with inefficient, time-consuming team formation for Capstone/elective projects, leading to unbalanced teams and delayed project starts. Manual searches via Telegram groups cause outdated information, unclear progress, and social barriers to outreach.
> 

**Solution**

> A centralized platform that streamlines team formation through AI-driven matchmaking, transparent project discovery, and structured applications.
> 

### **Key features implemented**

1. **Project hub**
    - Create/view projects with descriptions, required skills, and open roles
    - Real-time visibility into team composition
2. **Profiles**
    - Students highlight their skills and interests
3. **AI Matchmaking**
    - Recommends projects to students based on skill compatibility
4. **Application system**
    - 1-click applications for open roles
    - Accept/reject workflow
5. **Team dashboard**
    - Track accepted members
6. **Search & filters**
    - Find projects by skills, roles or course

## **Future expansion plans**

### **Product vision**

Scale TeamSync into a cross-ecosystem platform for universities, hackathons, and corporate projects within 3–5 years.

### **Strategic priorities**

1. **Teammate matching** 
    
    **User profiles**
    
    - Skills/experience showcase + availability calendars
    
    **AI teammate recommendations**
    
    - "Find Teammates" tab suggesting compatible peers
    
    **Direct collaboration tools**
    
    - Icebreaker chats for pre-team formation
2. **Ecosystem integration**
    - **Universities**
        
        Sync with LMS to auto-import courses/skills
        
    - **Hackathons**
        
        Partner with platforms for event team formation
        
3. **Enhanced AI capabilities**
    - **Predictive team balancing**
    - **Bias reduction**
        
        Anonymous applications to prioritize skills over demographics
        
4. **Monetization**
    - **B2B licensing**:
        - Universities: Paid access for Capstone/elective course management
        - Hackathons: Tiered pricing for analytics
    - **Premium features**:
        - Resume builder with verified project experience

5. **User experience rvolution**
    - **Research hub** – publish/find academic research opportunities

### Tech stack

|  | **Choice** | **Justification** |
| --- | --- | --- |
| **Frontend** | React | For building dynamic and high-performance user interfaces and server-side rendering capabilities. |
|  | TypeScript | A strongly typed programming language that builds on JavaScript, providing better tooling at any scale. |
|  | Tailwind CSS | A utility-first CSS framework for rapid UI development with consistent and responsive design. |
| **Backend** | Java/Spring Boot | Robust REST APIs, team expertise |
| **Database** | PostgreSQL | ACID compliance for user/project data |
|  | KeyDB | Fast session/matching-cache access |
| **ML** | Python | For its simplicity and extensive libraries for data processing and machine learning. |
| **Infra** | Docker + Docker Compose | Environment consistency, TA reproducibility |
|  | GitHub Actions (CI/CD) | Automated testing/deployment |

## Presentation draft

[LINK](https://miro.com/app/board/uXjVJdA5G0Q=/?share_link_id=352339515758)

# Plan for live demo

| 1st browser | 2nd browser (or incognito mode) |
| --- | --- |
| Registration | - |
| Project creation | - |
| - | Filter projects |
| - | Find created project |
|  | Apply to it |
| See application |  |
| Accept/reject |  |
| - | Change skills/project positions |
| - | Reload page, see that recommendations are changes |

# Weekly commitments

## ML

### ML model refinement

We introduced a collaborative filtering component into our recommendation system using the ALS (Alternating Least Squares) algorithm. This allows us to use implicit user feedback (favorites, clicks, applications) to provide more personalized recommendations. We also added Qdrant integration for vector-based embeddings and improved its logic for better stability. Furthermore, dynamic coefficient configuration was implemented to make the recommendation process more flexible and tunable.

### ML progress description

During this week, we introduced a collaborative filtering approach to our recommendation system using the ALS (Alternating Least Squares) algorithm. This allowed us to leverage implicit user feedback such as favorites, clicks, and applications for generating personalized recommendations [TS-233] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/4c95131883f7021533a867090d7de7063d244146).

We also introduced a dynamic coefficient specifically for the ALS component. This coefficient is calculated based on the number of user interactions across all projects using the formula `sqrt(x / 100)` for `0 <= x <= 100`, capped at `1` if `x > 100`, and set to `0` otherwise. The goal of this adjustment is to prevent projects from skyrocketing in recommendations after just one interaction. Instead, the influence of ALS grows gradually as we gather more behavioral data from the user, providing a smoother and more balanced recommendation experience. [TS-234] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/a3121cdb5644a2cdb7d1990f86b1912e71319f9a).

To enhance vector-based search and improve efficiency, we integrated Qdrant to cache embeddings generated by the transformer instead of recalculating them every time during recommendation processing. Additionally, we implemented an endpoint for the backend to trigger re-embedding when a project description is updated. On top of that, we introduced base logic for interacting with Qdrant, including collection existence checks, error handling, and methods for retrieving vectors by ID and table [TS-229] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/9f87fdecd5f2da80c99ea5e61aba4d75df6233ed), [TS-262, TS-263] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/2e241e7e4a3fe9ec477143e78d69b96495275419).

On the database side, we extended the schema to include a new clicks table and additional fields for handling user-project interactions used by ALS [TS-230] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/e03717cc22d2627c684f175bc210d8e099d1cbdd), [TS-232] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/67bf3021674d6eb1b2e8362c43b842041dd53fb4).

Additionally, we replaced Airflow with a lightweight job scheduler (APScheduler) to reduce overhead and simplify deployment, to reduce usage memory [TS-204] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/3319830ea4aeb442ca062668360e71bcfe48186a). We also performed minor refactoring such as renaming project names for proper displaying on the site [TS-214] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/commit/a416ffb9b8634d9060eedc3a45205ea12c96580d).

Moreover, we enhanced tag-based and role-based models with two other formulas, so now it consists of inner product, euclidean distance, and intersection over union combination calculated on bag of words embedding [TS-158] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/111). Also we finished creating the testing flow by manually creating relevance dataset and writting the script to calculate ranking metrics on model results [TS-183] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/112).

## Backend

**Features:**

- Add project view tracking: Implemented click logic in the project details endpoint to track project views to improve AI recommendations [TS-246], [PR-99](https://github.com/IU-Capstone-Project-2025/team-sync/pull/99).
- Team member removal by project owner: Added support for project owners to remove already accepted team members [TS-194], [PR-86](https://github.com/IU-Capstone-Project-2025/team-sync/pull/86).
- Dynamic roles and skills filters: Filters now display only roles and skills that are actually used in existing projects [TS-213], [PR-88](https://github.com/IU-Capstone-Project-2025/team-sync/pull/88).
- Started integration of ML project recommendations to backend [TS-104], [PR-110](https://github.com/IU-Capstone-Project-2025/team-sync/pull/110)

**Improvements:**

- Team size display logic: Updated project response to return both required team members count and overall members in the project [TS-238], [PR-101](https://github.com/IU-Capstone-Project-2025/team-sync/pull/101).
- Input validations: Added checks for input data [TS-228], [PR-93](https://github.com/IU-Capstone-Project-2025/team-sync/pull/93).
- Added exceptions: Improved exception handling for better error reporting [TS-259] [PR-102](https://github.com/IU-Capstone-Project-2025/team-sync/pull/102).
- Updated student registration endpoint, so it now takes initial roles and skills [TS-261] [PR-105](https://github.com/IU-Capstone-Project-2025/team-sync/pull/105).

**Bug fixes**

- Fix project application deletion [TS-248], [PR-97](https://github.com/IU-Capstone-Project-2025/team-sync/pull/97).
- Fix foreign keys in student_favourite_project table [TS-251], [PR-93](https://github.com/IU-Capstone-Project-2025/team-sync/pull/93).

## Frontend

This week, registration pages were added to the frontend (TS-79), the course filtration logic was fixed (TS-267) and many bugs were fixed based on user experience (TS-215, TS-216, TS-217, TS-220, TS-221, TS-239, TS-240, TS-241, TS-242, TS-243, TS-244, TS-247). Registration pages took a while to create due to backend bugs. A lot of time was spent on the wheel animation on the registration page. 
[https://github.com/IU-Capstone-Project-2025/team-sync/pull/107](https://github.com/IU-Capstone-Project-2025/team-sync/pull/107)

[https://github.com/IU-Capstone-Project-2025/team-sync/pull/98](https://github.com/IU-Capstone-Project-2025/team-sync/pull/98)

[https://github.com/IU-Capstone-Project-2025/team-sync/tree/front/fix/TS-267-fix-course-filtration](https://github.com/IU-Capstone-Project-2025/team-sync/tree/front/fix/TS-267-fix-course-filtration)

## Design

This week landing page was made and project view on project hub was fixed.

## DevOps

Updated ci/cd, so now it pushes docker images to docker hub.

**DEV environment**: docker images of every service being build (on github runners) on every push to pull_request (then the tag would be code of according jira task, for example, *ts-250*) and to main branch (then tag would be *main*). If we want to deploy something to dev, we need to manually trigger deployment of needed service and branch in github actions tab

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week%206/image.png?raw=true)

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week%206/image%201.png?raw=true)

**PROD environment**: we simply can create git tag (it’s better to create new github release) named like vX.X.X (X - any number) and it will automatically trigger workflow that will build and push images (image tag will be simply name of git tag - version) and deploy it to VDS

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week%206/image%202.png?raw=true)

Deploy happens via connecting to the remote via ssh and lauching scipts that pull updates for needed branc (migrations for example) and run docker compose files

## Individual contribution of each participant

| Team member | Contribution | Jira tasks |
| --- | --- | --- |
| Diana MInnakhmetova (Lead) | wrote report, held 2 meetings, made draft for presentation slides, made plan for live demo, fixed design issues, [made product strategy for future work](https://miro.com/app/board/uXjVJdA5G0Q=/?share_link_id=534302895217), [made landing page](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=q9Js5bd4HpF30mWq-1) | TS-226. TS-227, TS-237 |
| Danis Sharafiev | rename project names, replace airflow, add base qdrant model, add click table, extend db model, updated qdrant logic**,** add dynamic coeff**,** add als model | TS-214, TS-204, TS-229, TS-230, TS-232, TS-262, TS-263, TS-234, TS-233 |
| Daria Alexandrova | registration pages ([PR-107](https://github.com/IU-Capstone-Project-2025/team-sync/pull/107)), course filtration logic fix ([TS-267](https://github.com/IU-Capstone-Project-2025/team-sync/tree/front/fix/TS-267-fix-course-filtration)), bug fixes ([PR-98](https://github.com/IU-Capstone-Project-2025/team-sync/pull/98)) | TS-79, TS-267, TS-215, TS-216, TS-217, TS-220, TS-221, TS-239, TS-240, TS-241, TS-242, TS-243, TS-244, TS-247 |
| Stepan Dementev | Updated ci/cd workflwlows ([PR 103](https://github.com/IU-Capstone-Project-2025/team-sync/pull/103), [PR 104](https://github.com/IU-Capstone-Project-2025/team-sync/pull/104)), [updated registration endpoint](https://github.com/IU-Capstone-Project-2025/team-sync/pull/105), [connected ml services to backend](https://github.com/IU-Capstone-Project-2025/team-sync/pull/110), watched demo | TS-104, TS-192 TS-261 |
| Elizaveta Zagurskih | fixed bugs ([delete application function](https://github.com/IU-Capstone-Project-2025/team-sync/pull/97), [foreign keys in table](https://github.com/IU-Capstone-Project-2025/team-sync/pull/93)), add several features ([project click tracking](https://github.com/IU-Capstone-Project-2025/team-sync/pull/99), [delete team member](https://github.com/IU-Capstone-Project-2025/team-sync/pull/86), [dynamic filters for projects](https://github.com/IU-Capstone-Project-2025/team-sync/pull/88)), did some improvements ([change team size logic](https://github.com/IU-Capstone-Project-2025/team-sync/pull/101), [add input validations](https://github.com/IU-Capstone-Project-2025/team-sync/pull/93), [add exceptions](https://github.com/IU-Capstone-Project-2025/team-sync/pull/102)) | TS-246, TS-194, TS-213, TS-238, TS-228, TS-259, TS-248, TS-251 |
| Kamilya Shakirova | enhanced recsys using different similarity metrics, created testing flow on the self-labeled testing set | TS-158, TS-183, TS-268 |

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [ ]  In working condition.
- [ ]  Run via docker-compose (or another alternative described in the `README.md`).

**PROD environment**: we simply can create git tag (it’s better to create new github release) named like vX.X.