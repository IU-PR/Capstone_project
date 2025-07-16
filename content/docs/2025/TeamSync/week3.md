# Week 3

## **Implemented MVP features**

1. As a student, I want to post a new project with a description and required skills, so that I can find teammates who match my needs.
    
    > Given I am logged in and have completed my profile, when I click “My projects→Create project,” then I see a form with fields: title, description, required skills, status, project link.
    Given I have submitted the form, then the project appears in the public project feed.
    Given I return to “My projects”, then I can see, edit, or delete my posted project.
    > 
    
    | Implemented | PR (link) | Jira task |
    | --- | --- | --- |
    | Authorized user can create a project, choose skills and roles needed, add title, status, description of the project, optional link to project description.  | [https://github.com/IU-Capstone-Project-2025/team-sync/pull/23](https://github.com/IU-Capstone-Project-2025/team-sync/pull/23) | TS-105 (backend), TS-96 (backend) |
    | Authorized user can view the projects they created. | [https://github.com/IU-Capstone-Project-2025/team-sync/pull/23](https://github.com/IU-Capstone-Project-2025/team-sync/pull/23) | TS-94 (backend), TS-96 (backend) |
    | Authorized users can view all created projects in the public project feed. |  |  |
    | Authorized users can view their projects in “my projects” |  |  |
2. As a student, I want to apply to projects that match my interests, so that I can participate in projects relevant to my skills and goals.
    
    > Given I see a project in the feed, when I click “Apply,” then I can submit the request.
    Given I applied to a project, then I can see my application status in the “My responses” tab.
    > 
    
    | Implemented | PR (link) | Jira task |
    | --- | --- | --- |
    | Authorised users can apply to projects. They can see all their applications with their status at some page. | [https://github.com/IU-Capstone-Project-2025/team-sync/pull/23](https://github.com/IU-Capstone-Project-2025/team-sync/pull/23) | TS-98 (backend) |
    
3. As a student, I want to see suggestions and filters when browsing projects, so that I can efficiently choose which projects to join.
    
    > Given I open the project feed, then I see filters like tech stack and tag.
    > 
    
    | Implemented | PR (link) | Jira task |
    | --- | --- | --- |
    | On Home Page user can see all projects and can filter them with course, roles, and skills. | [https://github.com/IU-Capstone-Project-2025/team-sync/pull/23](https://github.com/IU-Capstone-Project-2025/team-sync/pull/23) | TS-93 (backend) |
    |  |  |  |

## **Demonstration of the working MVP**

[Link to the video](https://drive.google.com/drive/folders/1SdpeE8VrxILX4vvuD1bGbwB2zZ1zWtPQ?usp=sharing)


## **ML**

This week, the ML team implemented a basic data migration to test the functionality of both the project and individual microservices [TS-57] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/24). Core classes for interacting with the databases were also developed [TS-55][[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/18). We encountered some problems here because there are essential fields which we didn’t have in previous dataset, so we got to lead to a single format. Airflow was integrated for periodic recommendation updates. Additionally, a dummy recommendation service was created [TS-84][[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/25), and baseline models were added in two parts: Tag-based, including BoW + Cosine similarity [TS-72] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/34), and Description-based, using the AllMini-v6 Transformer and Cosine similarity [TS-73] [[PR]](https://github.com/IU-Capstone-Project-2025/team-sync/pull/32). Also we decided to use KeyDB instead of Redis because it works faster and uses the same clients for connection.

## **Internal demo**

During our internal MVP demo, we realized that the main problems currently lie in backend authorization and poor data quality in the database. The login system isn’t functioning properly, which causes issues with role resolution and protected routes. Additionally, the database contains inconsistent or incomplete data, particularly for user roles and skills, which results in crashes when the frontend tries to access that information. The home page appears stable and works as expected, but the project page fails to load because it’s trying to fetch roles and skills that aren’t correctly set up. Some course data is also broken or missing, which further affects project-related functionality. Overall, our next priority should be stabilizing backend auth logic, cleaning up or reseeding the database, and ensuring that key data like roles, skills, and courses are reliably connected to support the core user flow.

## Reflection

Looking back at this sprint, we weren’t able to implement all of the planned user stories as originally intended. Although we had clear priorities and a structured backlog, several unexpected issues arose during the integration of the backend and frontend. Many of the API connections didn’t work as expected due to mismatches in data structure, unstable authorization, and inconsistencies in the database. These integration problems significantly slowed down our ability to deliver a complete end-to-end user flow. As a result, we had to shift focus from implementing new features to debugging and stabilizing the core system. Moving forward, we’ll need to improve coordination between frontend and backend, double-check our API contracts, and ensure data consistency early in the development process.

# **Weekly commitments**

## **Individual contribution of each participant**

| Team member | Contribution | Jira tasks |
| --- | --- | --- |
| Diana MInnakhmetova (Lead) | Held 2 meetings + 2 with stakeholders + 2 interviews, made design of “create project” and “project feed” | TS-75, TS-76, TS-77, TS-78 |
| Danis Sharafiev | [Dataset synthesis](https://github.com/IU-Capstone-Project-2025/team-sync/pull/17), [add connection with Database](https://github.com/IU-Capstone-Project-2025/team-sync/pull/18), [KeyDB and Airflow containers added](https://github.com/IU-Capstone-Project-2025/team-sync/pull/19), [dummy recommendation system](https://github.com/IU-Capstone-Project-2025/team-sync/pull/25),  | TS-70, TS-71, TS-84, TS-73, TS-87 |
| Daria Alexandrova | [Microsoft entra initialization](https://github.com/IU-Capstone-Project-2025/team-sync/pull/20), [project view page created](https://github.com/IU-Capstone-Project-2025/team-sync/pull/26),  | TS-81, TS-65, TS-82, TS-80 |
| Stepan Dementev | [Initial auth service](https://github.com/IU-Capstone-Project-2025/team-sync/pull/21), [Initial recommendations service](https://github.com/IU-Capstone-Project-2025/team-sync/pull/27), [nginx set up](https://github.com/IU-Capstone-Project-2025/team-sync/pull/31), bugfixes | TS-64, TS-86, TS-54, TS-59, TS-104, TS-107, TS-106 |
| Elizaveta Zagurskih | [Project service created](https://github.com/IU-Capstone-Project-2025/team-sync/pull/23), completed API for resume service,  | TS-58, TS-52, TS-93, TS-94, TS-95, TS-96, TS-97, TS-98, TS-105 |
| Kamilya Shakirova | Database migrations (*she was mostly sick and still sick, legal excuse will be provided)* | TS-57 |

## **Plan for Next Week**

### Backend

- Refactoring of the code
- Refine the APIs

### Design

- “Student dashboard” page
- “Onboarding” page
- “Notification” page
- “Favorite projects” page
- “My responses” page

### Frontend

- “My responses” page
- Animations

### ML

- Algorithm enhancement

### Management

- Analysis of interviews and meetings with stakeholders

### CI/CD

- Write unit tests for critical backend logic and frontend components.
- Write integration tests for API endpoints.
- Aim for basic end-to-end tests for the core user journey.
- (ML) Implement basic model validation/testing.
- Deployment

**Confirmation of the code's operability**

We confirm that the code in the main branch:

- [ ]  In working condition.
- [ ]  Run via docker-compose (or another alternative described in the `README.md`).