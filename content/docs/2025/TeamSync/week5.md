# Week 5

## Feedback

### Sessions

**Damir, 24 years, alumni**

Recent graduate seeking project collaborators

> "When browsing projects, I can't see who's already on the team. This is crucial - I don't want to apply if there's already 5 developers. Also, I need to bookmark interesting projects to revisit later."
> 

**Pain points:**

- Zero visibility into existing team composition
- No way to save/track preferred projects

**Aliya, 20 years, 2nd year bachelor student**

Frontend developer seeking team roles

> "How exactly does my profile appear to project owners? Can I update my skills after creating my profile? Having multiple resumes for different goals would be perfect."
> 

**Pain points:**

- Uncertainty about profile presentation
- Profile fields locked after initial setup
- Need for specialized profiles

**Alyona, 20 years, 2nd year bachelor student**

Student exploring projects where she can be DevOps

> "Is there any search function? Usually my friends make project and then we all in it. I dont want to waste a lot of time to search project, so search system would be perfect"
> 

**Pain points:**

- No search system
- Manual discovery is time-consuming

### Analyze

**Fundamental feature gaps**

- Missing project search blocks core discovery
- Locked profiles prevent skill updates
- Hidden team members cause misaligned applications

**High-impact workflow issues:**

- No project bookmarking reduces re-engagement
- Single-profile limitation hinders role flexibility
- Unclear profile visibility creates anxiety

| **Issue** | **Priority** | **User impact** |
| --- | --- | --- |
| Unlock profile editing | Critical | Allows skill/role updates |
| Show team members | Critical | Prevents wasted applications |
| Favorite projects | Medium | Improves re-engagement |
| Profile visibility docs | Medium | Clarifies privacy concerns |
| Multi-resume system | Low | Supports different goals |
| Add project search | Low | Enables efficient discovery |

## Iteration & Refinement

### Implemented features based on feedback

We did not implemented fully, but pasted to the closest plans the following:

- Unlock profile editing (backend already has logic, design also)
- Show team members
- Favorite projects (backend already has logic)
- Profile visibility docs
- Add project search

### Documentation

To keep our project organized and accessible, we maintain a structured Notion workspace. It includes dedicated sections for product planning, development, documentation, and communication. Here’s a breakdown of the key categories:

**Concept & Planning**

- Idea – problem statement and target audience
- User Stories – all current user stories and acceptance criteria

**Rules & Guidelines**

- Правила ведения репозитория – Team agreement on how to manage branches, commits, and pull requests
- Работа с SSO – Instructions for integrating Microsoft Entra (SSO)
- Submissions – Capstone report submission links

**Developer Sections**

- ML notes
- Frontend notes
- Backend notes

**Management & Coordination**

- Future Improvements – brainstorming and feature backlog beyond MVP
- Requirements – system and functional requirements documentation (will be soon)
- Meeting with Stakeholders – interview notes and next steps from meetings with Potyomkin, Marko, Mansur, and others.

For the ML part we use Swagger (via FastAPI) because it’s auto-generated and helpful for quick testing and integration. It documents input/output formats, lets us test endpoints right in the browser, and keeps backend/ML/frontend aligned without writing extra docs

### ML Model Refinement

We added new part of RecSys that depends on the roles of users and projects. This helps us to recommend more relevant projects to users. As an improvements: we still have to implement researched tag-based algorithm and we could somehow combine tag-based and role-based parts to find complex connections among them and improve recsys more. For description-based we could use another embedder: much powerful and which takes more tokens, but for now we can’t afford it because of poor system requirements.

# Weekly commitments

## ML

During this week, we realized that we need to make our ML services lighter, since their dependencies took up around 30GB [TS-179] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/69). To address this, we found an ONNX model in open repositories and removed heavy libraries such as sentence-transformers and PyTorch. This also solved another problem: previously, model loading relied on an ethernet connection and always took too long to download, but ONNX resolves this [TS-110].

Additionally, we isolated the embedder into a separate service, so we can use one embedder for different services: Recsys and the future search system [TS-193].

Moreover, we designed the first prototype of the search system [TS-164]. It consists of two algorithmic parts: BM25 and Semantic embeddings, with reciprocal rank fusion and a reranker. We are also planning to implement smart pagination for it. We have already created a Qdrant image, but we still need to develop an interface to communicate with it [TS-191] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/80).

![изображение.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/изображение.png?raw=true)

On the other side, we create a new module in the recommendation system for role-based matching. Role-based model includes BoW + Cosine similarity [TS-206]. [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/83) We have developed a recommendation algorithm for new users who have incomplete data (cold start problem) [TS-74], so we could improve the users experience on the next week. We also faced the problem of a lack of necessary methods in the database class, so we added them [TS-210].

## Backend

During this week, we have implemented several important features and improvements to the project management system:

1. **Add Desired Team Size for Project Owners [TS-92] [PR-76](https://github.com/IU-Capstone-Project-2025/team-sync/pull/76)**
    - Updated the database structure by adding a new field for specifying the desired team size during project creation.
    - Implemented a restriction: project owners cannot add more members to their team than the specified limit.
2. **Change `courseName` Field to Entity Reference [TS-190] [PR-68](https://github.com/IU-Capstone-Project-2025/team-sync/pull/68)**
    - Replaced the `courseName` string field in the project entity with a reference to the `Course` entity.
    - Now project owners can select a course from the existing list or create a new course if it doesn't exist in the system.
3. **Add Exceptions for Project Applications [TS-186] [PR-68](https://github.com/IU-Capstone-Project-2025/team-sync/pull/68)**
    - Added validation to prevent project owners from applying to their own projects.
4. **Implement Application Deletion for Students [TS-178] [PR-68](https://github.com/IU-Capstone-Project-2025/team-sync/pull/68)**
    - Students are now able to delete their own applications for projects.
5. **Application Status Management for Project Owners [TS-89] [PR-76](https://github.com/IU-Capstone-Project-2025/team-sync/pull/76)**
    - Added functionality allowing project owners to manage the status of applications to their projects.
    - Project owners can now accept or reject applications directly from the “My Projects” page.
6. **Implement Application Review Interface for Project Owners [TS-88] [PR-76](https://github.com/IU-Capstone-Project-2025/team-sync/pull/76)**
    - Created a feature where project owners can view applications to their projects in the form of applicant user profiles.
7. Implement Favourite Project logic [TS-90] [PR-81](https://github.com/IU-Capstone-Project-2025/team-sync/pull/81) 
    - Now user can add project to favourites, delete it from that list, and view their favourite projects.

Also, in collaboration with our frontend developer, we updated the project application response format [TS-196] [PR-71.](https://github.com/IU-Capstone-Project-2025/team-sync/pull/71) 

If you see some info below from the info above, it’s just explanation, why we did it.

There were multiple clarifications and changes regarding how project-related data should be structured and returned in API responses. Additionally, a fix was applied to enforce a rule preventing project owners from adding more team members than the specified team size. Early on, this constraint was missing, and it was added after internal review and testing. On top of that, throughout the week, we maintained active communication with our frontend developer to quickly resolve integration mismatches, clarify endpoint behaviors, and adapt backend responses to frontend UI needs. This collaborative approach helped avoid potential blockers and ensured consistent progress on both sides.

## Design

This week I reorganized the Figma file to align with our User Stories. Each set of frames is now grouped according to a specific User Story making the design more structured and easier to navigate.

Instead of inserting multiple screenshots here:
Link to Figma – [LINK](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=Tv75bgJoMgN6eCPm-1)

My responces

![Снимок экрана 2025-07-09 в 21.21.20.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/Снимок_экрана_2025-07-09_в_21.21.20.png?raw=true)

Favorite projects

![Снимок экрана 2025-07-09 в 21.21.10.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/Снимок_экрана_2025-07-09_в_21.21.10.png?raw=true)

Student dashboard and “settings” with “log out”

![Снимок экрана 2025-07-09 в 21.21.39.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/Снимок_экрана_2025-07-09_в_21.21.39.png?raw=true)

Responses to project

![Снимок экрана 2025-07-09 в 21.22.04.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/Снимок_экрана_2025-07-09_в_21.22.04.png?raw=true)

## Frontend

This week, I made it possible for users to send their responses to certain projects, created the response page so users can see their responses ([https://team-sync-capstone.atlassian.net/browse/TS-198](https://team-sync-capstone.atlassian.net/browse/TS-198)) ([https://github.com/IU-Capstone-Project-2025/team-sync/pull/84](https://github.com/IU-Capstone-Project-2025/team-sync/pull/84)) , the project view so that the user can see the information about a project before applying to it ([https://team-sync-capstone.atlassian.net/browse/TS-197) (](https://team-sync-capstone.atlassian.net/browse/TS-197)[https://github.com/IU-Capstone-Project-2025/team-sync/pull/72](https://github.com/IU-Capstone-Project-2025/team-sync/pull/72)), as well as started work on the “My projects page” so that requests can be seen, accepted or denied ([https://team-sync-capstone.atlassian.net/browse/TS-101](https://team-sync-capstone.atlassian.net/browse/TS-101)). 

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/image.png?raw=true)

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/image%201.png?raw=true)

![image.png](https://github.com/mnkhmtv/project-screenshots/blob/main/week5/image%202.png?raw=true)

## Individual contribution of each participant

| Team member | Contribution | Jira tasks |
| --- | --- | --- |
| Diana MInnakhmetova (Lead) | held 2 meetings, wrote report, took 3 interviews, [updated design with “favorite project”, “my responses”, “student dashboard” pages and made little improvements for better view in other pages](https://www.figma.com/design/H76U45VUArQSuD5ev0anDV/TeamSync-Design?node-id=0-1&t=Tv75bgJoMgN6eCPm-1)  | TS-168, TS-170, TS-171, TS-172 |
| Danis Sharafiev | Made ML services lighter, Added loading transformers from local repository, Separated embedders logic, Developed an architecture for search system, added Qdrant image in compose. | TS-179, TS-110, TS-193, TS-164, TS-191  |
| Daria Alexandrova | Created project view on main page, response page, started working on “my projects” page | TS-198, TS-197, TS-101 |
| Stepan Dementev | Fixed lots of bugs, related to backend endpoints of resume and projects service: [project filltering](https://github.com/IU-Capstone-Project-2025/team-sync/pull/63), [user registration](https://github.com/IU-Capstone-Project-2025/team-sync/pull/64), [added config to frontend nginx container](https://github.com/IU-Capstone-Project-2025/team-sync/pull/65), [duplicate roles and skills for users](https://github.com/IU-Capstone-Project-2025/team-sync/pull/73), [data types serialization](https://github.com/IU-Capstone-Project-2025/team-sync/pull/74), [resume service jwt security filtering](https://github.com/IU-Capstone-Project-2025/team-sync/pull/75), [response bodies fields names](https://github.com/IU-Capstone-Project-2025/team-sync/pull/77), [student profile update](https://github.com/IU-Capstone-Project-2025/team-sync/pull/77)
[Implemented profile page with logout on frontend](https://github.com/IU-Capstone-Project-2025/team-sync/pull/79) | TS-195, TS-187, TS-188, TS-189, TS-202, TS-203, TS-205, TS-207, TS-209 |
| Elizaveta Zagurskih | [Added team size limit for projects](https://github.com/IU-Capstone-Project-2025/team-sync/pull/76/files), [replaced `courseName` field with a `Course` entity reference](https://github.com/IU-Capstone-Project-2025/team-sync/pull/68), [added validation to prevent project owners from applying to their own projects](https://github.com/IU-Capstone-Project-2025/team-sync/pull/68/files), [implemented application deletion for students](https://github.com/IU-Capstone-Project-2025/team-sync/pull/76), [added application viewing and status management for project owners](https://github.com/IU-Capstone-Project-2025/team-sync/pull/76), [refactored responses according to frontend developer request](https://github.com/IU-Capstone-Project-2025/team-sync/pull/71), [add favourite project logic](https://github.com/IU-Capstone-Project-2025/team-sync/pull/81) | TS-88, TS-89, TS-92, TS-190, TS-186, TS-178, TS-196, TS-90 |
| Kamilya Shakirova | Implemented role-based matching part, developed an algorithm to solve cold start, Added methods in DB model, Developed an architecture for search system. | TS-206, TS-74, TS-210, TS-164 |

## Plan for Next Week

### ML

- Implement Search system and smart pagination.
- Enhance tag-based and role-based.

### Design

- Enhance pages
- Add detailed info considering feedback
- Make onboarding pages

### Backend

- Deploy and connect ml services and provide recommendations for frontend.
- Enhance deploying, so docker images will be build on github runners and pushed to ghcr, and then pulled and raised on remote machine

### Frontend

- Continue work on “my projects” page
- Implement “likes”
- Start on registration

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [ ]  In working condition.
- [ ]  Run via docker-compose (or another alternative described in the `README.md`).