---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration



After revising the user stories, we decided to keep almost all of them in the MVP scope. One user story was removed from the MVP (**As a user**, I want to see brief descriptions of recommended books so I can quickly  understand if the book suits me) — we chose to keep only the author, title, and cover for now and plan to expand it with descriptions in the final product.

### User stories

-   **As a user**, I want to receive a list of recommended books that match my interests based on past ratings so I can quickly decide what to read.
-   **As a user**, I want to rate a book I've read so that the system can better understand my preferences.

- **As a user**, I want to maintain a personal reading list (Read, Reading, Planned) so I can organize my reading journey.
- **As a user**, I want to leave and read comments on books so I can share opinions and discover what others think.
- **As an author**, I want to see aggregated feedback (ratings and comments) on my books so I can understand reader reception.
- **As an author**, I want to view the "Most Popular This Week" list so I can understand current reader interests and trends to better align my future writing.
    
 ### Acceptance Criteria for Key User Stories

1. **As a user**, I want to receive a list of recommended books that match my interests based on past ratings.
At least 5 book recommendations are displayed.

- Recommendations are updated after the user rates new books.

- Each recommended book includes a title, author, and cover.

- Only books not already in the user's reading list are shown.

2. **As a user**, I want to rate a book I've read so that the system can better understand my preferences.
- Rating is possible with one click (e.g. 1–5 stars or thumbs up/down).

- Rated books are saved in the user’s profile.

- The system updates recommendations after rating is submitted.

- The same book cannot be rated multiple times.

3. **As a user**, I want to maintain a personal reading list (Read, Reading, Planned).
- User can assign each book to one of the three statuses.

- Books can be moved between statuses.

- The reading list persists between sessions.

- A book cannot belong to more than one status at the same time.

4. **As a user**, I want to leave and read comments on books.
- Any user can leave a comment on a book they have rated or marked as “Read”.

- Comments display the username and timestamp.

- Users can read comments left by others on a book’s detail page.

- Comments are sorted by newest first.

5. **As an author**, I want to see aggregated feedback (ratings and comments) on my books.
- Author can view average rating per book.

- Author sees total number of ratings and comments.

- Author can read all public comments on their books.

6. As an author, I want to view the "Most Popular This Week" list.
- List updates weekly.

- List includes top 10 books with the highest interaction (reads, ratings, comments).






### Prioritized backlog

![Backlog Screenshot](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/08f035edef54f1a2e3ce5ecb06c6719ecff2bb25/backlog.png)


| Task                                                                 | Status | Deadline | Priority |
|----------------------------------------------------------------------|------|----------|----------|
| Database schema design & data ingestion                              | Done | ~~Jun 18~~    | High     |
| Docker compose for airflow                                           | Done | ~~Jun 18~~    | High     |
| Create initial design for core pages in                              | Done | ~~Jun 18~~    | High     |
| Book listing & sorting (Top Rated, Most Popular, Trending, ...)      | To Do | Jun 25   | High     |
| User feedback features                                               | To Do | Jun 25   | High     |
| Mobile optimization for web                                          | To Do | Jun 25   | Low      |
| Develop basic user flow diagrams for key interactions                | Done | ~~Jun 18~~    | High     |
| DevOps and deployment (Containerization/Orchestration + Nginx + CI/CD)| To Do | Jun 25   | High     |
| Scrape data from sites with book datasets                            | To Do | Jun 25   | Medium   |


## Project specific progress

### Frontend

We set up the basic web interface using FastAPI with Jinja2 templates and implemented skeleton pages based on initial designs. During the development process, we added an interactive title page with 3d model to the original idea.

### Backend

We initialized the FastAPI application and implemented initial API routes for user and book data. The backend is integrated with Jinja2 for page rendering. Core modules for user authentication and request handling have been stubbed out. The server configuration supports environment variables for database connections and is aligned with the planned Python/FastAPI stack.

### Design
[Figma Prototype Link](https://www.figma.com/proto/Mwvp1KHcgJLSX74uZ36Cbe/Capstone_project?node-id=0-1&t=rDT8jORPTw5Y25U6-1)

[Figma Project Link](https://www.figma.com/design/Mwvp1KHcgJLSX74uZ36Cbe/Capstone_project?node-id=0-1&t=rDT8jORPTw5Y25U6-1)

[Spline Scene Link](https://app.spline.design/file/cbb403aa-b9cb-4d97-9646-0f270f06749c)

Model was initially created in Blender and then imported into Spline.

**User Flow:**

![User Flow](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/user%20flow.png)

### Data-engineering
We designed the database schemas for the transactional PostgreSQL and analytical Greenplum databases, as shown in Figure 1. The ER diagram includes tables for users, books, scores, comments, genres, tags, and types, matching the planned database architecture. On the data pipeline side, Apache Airflow has been configured, and we have begun defining the initial DAG for ingesting and processing book and user activity data. These components lay the groundwork for the future recommendation data marts and analytics.

**PostgreSQL and Greenplum Database Schema**

![PostgreSQL and Greenplum Database Schema](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/image2.png)

### Deployment/DevOps
We created Dockerfiles for each service component and a docker-compose.yml to launch the system locally. Kubernetes deployment manifests have been drafted to orchestrate the containers. Nginx has been configured as a reverse proxy for the FastAPI backend. These efforts align with our infrastructure plan for container orchestration and load balancing. The container images build successfully and preliminary integration tests (e.g. an API health-check endpoint and static content routing) have passed.


# Weekly commitments

## Individual contribution of each participant


- **Denis Troegubov**
    - Working init-db.sql and docker-compose for airflow, airflow-db (postgres), backend-db (postgres) and greenplum [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/8)

  
- **Timur Garifullin**:ы
    - Implemented endpoints for multiple pages, added navigation links between them, and extracted the common page layout into a separate template. [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/17)
 

- **Grigorii Belyaev**:
    - Report
    - User flow
    - Expand User stories and defined acceptance criteria for key user stories.


- **Peter Zavadskii:**
    - Сontainerized the backend using Docker and configured Nginx. [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/9)
    - Set up the backend directory structure and implemented the first endpoint. [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/5)
    - Deployed the entire system on a remote server. It is available at:
http://176.119.159.108 (note: the server is accessible via HTTP only, not HTTPS).
  
  
  

- **Adelina Karavaeva:**
    - Developed a clickable figma prototype: [Figma Prototype Link](https://www.figma.com/proto/Mwvp1KHcgJLSX74uZ36Cbe/Capstone_project?node-id=0-1&t=rDT8jORPTw5Y25U6-1)
    - Implemented skeleton components based on initial designs [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/10)
    - Modeled bookshelf for title web page [Spline Scene Link](https://app.spline.design/file/cbb403aa-b9cb-4d97-9646-0f270f06749c)


## Plan for Next Week

Our key goals for the next week include:

- Completing integration of frontend and backend, including implementing remaining API endpoints (user registration, book listing, rating submission, etc.).

- Finalizing the personalized recommendation algorithm and connecting it to the user data model.

- Extending Airflow pipelines to load and preprocess data (e.g. book meta-data ingestion, user activity logs).

- Writing automated tests (unit and integration) and setting up a CI/CD pipeline for continuous integration.

- Finalizing the Kubernetes deployment: applying manifests in a cluster environment and configuring Nginx for full production routing.


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
