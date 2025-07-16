---
title: "Week #6"
---

# **Week #6**

## Links


- **Deployment**: https://capstone2.cybertoad.ru
- **API Docs**: [Link](https://capstone2.cybertoad.ru/docs)
- **Design**: [Figma project](https://www.figma.com/design/xNFLKEMXjPU4oMtQYabylN/Updated-version-of-capstone-design?t=xbY9QV8L2pccg2hS-0), [Figma Prototype](https://www.figma.com/proto/xNFLKEMXjPU4oMtQYabylN/Updated-version-of-capstone-design?node-id=0-1&t=xbY9QV8L2pccg2hS-1)
- **Demo**: [Link](https://drive.google.com/file/d/1H-P_QaxrbGD5bL2pDW7EJ1dNtjW-X16a/view?usp=sharing)


## Final deliverables

### Project overview


---

Our project is a **personalized book recommendation platform** that helps users discover new books based on their reading history and preferences. It addresses a common problem for both avid and occasional readers: the time-consuming and sometimes discouraging process of choosing the next book to read.

For **frequent readers**, the system reduces decision fatigue by offering tailored recommendations, allowing them to spend more time reading and less time searching — an important benefit, as they make such choices often and therefore spend a significant amount of time on this task overall. For **occasional readers**, it lowers the barrier to engagement by simplifying the book selection process, encouraging more consistent reading habits.

The recommendations are based on **user-provided ratings (1–5 stars)**, ensuring relevance and accuracy. Additionally, users can leave comments on books, enabling others to quickly gauge community opinions and make informed decisions about recommended books. Our platform also features a **weekly trending list** and a **Top Books chart**, which appeal to users who want to stay current with popular titles and participate in broader conversations on social media and in reading communities.

To support personal tracking, the platform includes a reading list management system with three categories: **Already Read**, **In Progress**, and **Planned**.

---


### Features

*List of all implemented features in your project.*
- Personalized book recommendations
- Reading list management (Already read/In progress/Planned)
- 1-5 star rating system
- Comments on books
- Weekly trending books
- Books Top

### Tech stack


| Component           | Technology               |
|---------------------|--------------------------|
| Backend             | FastAPI                  |
| Frontend            | Jinja2 + HTML + CSS + JS |
| Auth                | Keycloak + LDAP          |
| Orchestration       | Airflow                  |
| Transactional DB    | PostgreSQL               |
| Analytical DB       | ClickHouse               |
| Infrastructure      | Docker/Kubernetes        |

## Setup instructions

### 1. Clone the repository

```bash
git clone https://github.com/IU-Capstone-Project-2025/Recommendation-System.git
cd Recommendation-System
````



### 2. Prepare environment configuration

Rename the example environment file:

```bash
cp .env.example .env
```



### 3. Start Keycloak and LDAP (manual step)


*  The official Keycloak and LDAP containers are run simultaneously via Docker using official guides, and are manually synchronized via user interfaces.


### 4. Build and run project components using Docker Compose

```bash
docker compose up --build -d tester
```

> Alternatively, you may use Kubernetes for orchestration


---

### 5. Access the application

#### Access Points

| Environment | Service                        | URL                           | Credentials       |
|-------------|--------------------------------|-------------------------------|-------------------|
| Local       | Web UI                         | http://localhost:8000         | -                 |
| Local       | Airflow                        | http://localhost:8080         | admin/admin       |
| Local       | Keycloak                       | http://localhost:8081         | admin/admin       |
| Local       | Postgres (backend)             | http://localhost:5432         | admin/admin       |
| Local       | Postgres (airflow)             | http://localhost:5433         | admin/admin       |
| Local       | Clickhouse   (HTTP connection) | http://localhost:8124         | admin/admin       |
| Local       | Clickhouse   (TCP connection)  | http://localhost:9001         | admin/admin       |
| Production  | Live Site                      | https://capstone2.cybertoad.ru | -                 |
| Production  | Authentication servises        | https://capstone.cybertoad.ru | -                 |



## Presentation draft

[Link to Presentation draft in Figma](https://www.figma.com/design/ughJVRINrdGOumdGw9g6ja/Capstone_Presentation_Slides?node-id=0-1&t=zhxaBj53Z3G9SHrI-1)


## <span style="color:green">Bonus</span>

### Deployment

Our service accessible at: https://capstone2.cybertoad.ru

We deployed the frontend, backend, data engineering pipeline, and databases on a server.

There is also a second server that hosts the authentication system. This was done to avoid compromising user data by fully copying and decoding data from RAM.

Everything is orchestrated using Docker Compose. The web server is Nginx, which forwards the traffic to the containers, where it is processed and sent back.

## Weekly commitments

## Individual contribution of each participant

- **Denis Troegubov:**
    - Added comments and fix problem with data overflow [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/94)

  
- **Timur Garifullin**:
    - Fixed catalog error when ClickHouse is down [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/88)
    - Fixed status drop, added button to drop rating [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/88)
    - Converted usernames to lowercase to prevent LDAP issues [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/88)
    - Applied a 404 error template [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/88)


- **Grigorii Belyaev**:
    - Improved mobile search input and fixed minor UI issues on the home page (duplicate sign-in button) [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/89)
    -  Unified status case and fix comment word-break [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/86)
    -  Hided 3D model and adapt auth pages for mobile [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/85)

- **Peter Zavadskii:**
    - Documented the endpoints in Swagger [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/93)
    - Tested two search approaches: one based on machine learning and one using an algorithm. 

  > We decided to go with the algorithmic approach, as the ML-based solution requires too many resources and our server cannot handle it efficiently.

    - Checked the ML-based approach [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/91)
    - Restored the Levenshtein distance algorithm for search [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/92)


- **Adelina Karavaeva:**
    - Report
    - Created presentation [Link to  Figma](https://www.figma.com/design/ughJVRINrdGOumdGw9g6ja/Capstone_Presentation_Slides?node-id=0-1&t=zhxaBj53Z3G9SHrI-1)
    - Renamed inconsistent "Sign in" text to "Log in" across the UI for clarity and consistency.
Added an animated SVG avatar to the user profile [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/90)
    - Updated design document to be up to date with final project [Link to  Figma](https://www.figma.com/design/xNFLKEMXjPU4oMtQYabylN/Updated-version-of-capstone-design?t=3SqWYiqJ3LkUnnK2-0)

## Plan for Next Week

Next week we plan to:

- Do a final walkthrough of the website to ensure everything works as expected.

- Complete and polish the final version of the presentation slides.

- Rehearse the full presentation






## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
