
---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features


### Backend & infrastructure
- Deployed LDAP service [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/23)
- Backend service integrated into the `docker-compose` configuration [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/21)
- Deployed Keycloak [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/21)
- Implemented **base Jinja template** (`base.html`) to provide a consistent layout across all pages [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/17)
- **All services successfully connected and deployed on the server side**

### Authentication & Authorization
- **Authentication via Keycloak + LDAP is fully functional** [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/30)


### Data engineering
- Completed data transition pipeline for recommendation generation [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/25)
- Implemented automatic refresh of materialized views with recommendations [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/25)
- Created DDL for Greenplum [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/19)
- All recommendation datamarts created [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/19)


### Frontend
- **All pages planned in the design, including the user profile, book detail page, catalog, sign-in, and registration pages, have been implemented** [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/27), [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/10), [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/4)
- Implemented responsive design with mobile support [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/22)
- An interactive 3D model has been added to the title  page [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/4)

## Functional user journeys

### User Authentication
- The user visits the login page and authenticates via Keycloak (backed by LDAP)


### Book Exploration
- After logging in, the user sees a list of available books


### Book Information
- The user selects a book and views its details, including the author, rating, and description




## Demonstration of the working MVP

**Video demonstrating the working airflow:** [Link](https://drive.google.com/file/d/12dB2fDw0xZnjCmIe2suwLhnL3ZEbrYDR/view?usp=sharing)

**Video demonstrating the connection between LDAP and Keycloak for authorization:** [Link](https://drive.google.com/file/d/1ssLXgtIZPWdcSrpa8z8cKkkJ14basXkK/view?usp=sharing)

![Title_page](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/title-page.png)
![Catalog](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/catalog.png)
![Book-info](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/book-info.png)
![login](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/log%20in.png)
![register](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/register.png)
![personal](https://raw.githubusercontent.com/ElinaNotElina/IU-Capstone-Project-2025/refs/heads/main/personal.png)

## Internal demo

- Showed the deployed web interface running on the server, with all designed pages implemented
- Demonstrated working user authentication via Keycloak with LDAP
- Presented completed data pipeline for recommendation generation and automatic materialized view refresh
- Discussed next priorities: implementing commenting functionality, developing book listing and sorting, and adjusting frontend layout for new features

# Weekly commitments

## Individual contribution of each participant



- **Denis Troegubov:**
    - Completed data transition pipeline and refresh materialized views with recommendations [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/25)
    - Added ddl for greenplum, created all recommendation datamarts, and fixed docker compose [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/19)
    - Added initial books loading [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/29)

  
- **Timur Garifullin**:
    - Implemented basic Keycloak integration to enable centralized authentication [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/30)
    - Added error reporting functionality during user registration [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/30)
 

- **Grigorii Belyaev**:
    - Added mobile support with responsive design [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/22)

  
- **Peter Zavadskii:**
    - Deployed the LDAP service [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/23)
    - Deployed Keycloak and added the backend service to the `docker-compose` configuration [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/21)
    - Connected all services on the server side


- **Adelina Karavaeva:**
    - Updated the book info page UI and added interactive lists to the account page. [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/24)
    - Added regiatration page [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/27)

    
## Plan for Next Week



- Implement user feedback features (add support for submitting and displaying comments on book pages)
- Develop book listing and sorting functionality (Top, Popular, Popular per week, Recomendation)
- Refactor and adjust frontend layout to accommodate newly implemented features

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
