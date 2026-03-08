---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

We received the following feedback from lawyers:

1.  The application is "definitely useful for analyzing a large (multi-page) document. For novice lawyers or non-lawyers, it will be useful as a tool for highlighting problem areas, for more experienced ones - for parallel analysis and verification of problem areas with their subsequent manual analysis."
2.  Another user "liked the visualization - risk analysis on the principle of a traffic light." They also mentioned that they would have liked to see "a final summary of the contract, i.e. what is the overall degree of risk, and the ability to download the analysis as a file."
3.  A third user found the interface to be "very simple: uploaded the document, got the result in a fairly short period of time. Everything is concise, nothing superfluous, it didn't take long to figure it out." They particularly liked that "the service immediately highlighted the weak points: fines, unilateral changes in conditions, unfavorable terms." However, they wished for a "checklist for the main risks." They also expressed concerns about the completeness of the analysis and the security of data storage.

### Analyze

Based on the feedback from the lawyers, we have identified the following key points and have prioritized the implementation of new features accordingly.

**Summary of User Feedback:**
- **Positive:** Users praised the application's core value in analyzing large documents, its simple and fast interface, and the effectiveness of the "traffic light" risk visualization. They found the identification of weak points (fines, unilateral changes) to be particularly useful.
- **Negative:** The main concerns revolved around trust and utility. Users expressed a need for better data security, questioned the completeness of the analysis, and noted the inability to export the results.

**Issues and Priorities:**

Based on this feedback, we have created the following issues:

- **High Priority:**
    - **Downloadable Reports:** Implement a feature to allow users to download the risk analysis as a file (e.g., PDF). This addresses a direct request and improves the tool's utility
    - **Overall Risk Summary:** Add a section at the beginning of the analysis that provides a high-level summary of the contract's overall risk level
- **To Be Investigated:**
    - **Security and Trust:** We need to address user concerns about data security and the comprehensiveness of the analysis. This will likely involve creating a public-facing document detailing our security practices and being more transparent about the scope and limitations of our analysis model. This is crucial for building long-term user trust.

## Iteration & Refinement

### Implemented features based on feedback

- **Downloadable Reports:** Have been implemented by Arthur Babkin in [pr](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/123):

- **Overall Risk Summary:** Plan for next week [issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/129)

### Performance & Stability

- **Vector Search Optimization:** Successfully reduced search response time from approximately 12 seconds to 4 seconds, representing a 66% performance improvement that significantly enhances user experience
- **Enhanced Analysis Accuracy:** Implemented a new validation step in the agent analysis pipeline, resulting in more reliable and precise risk identification with reduced false positives
- **Frontend Modernization:** Redesigned the user interface with a cohesive design system, improving overall user experience through better visual consistency and intuitive navigation
- **Security Enhancement:** Implemented comprehensive JWT token authentication across all API endpoints, ensuring secure access control and protecting user data throughout the platform

### Documentation

Our project's documentation is consolidated within a comprehensive `README.md` file, which is structured to cater to various stakeholders, from end-users to developers. The key types of documentation included are:

1.  **User and Onboarding Documentation**: This includes a "Quick Start" guide that offers step-by-step instructions for cloning the repository, downloading the required legal datasets, configuring the environment, and launching the entire platform using Docker Compose. The purpose is to streamline the setup process for new developers and users, ensuring they can get the application running with minimal friction.

2.  **Architectural Documentation**: We provide a clear overview of our microservices architecture, detailing the roles of the Frontend (Vue.js), Backend API Gateway (Spring Boot), Analyzer service (FastAPI), and Chat service (FastAPI). This section also describes the technology stack and the database schema, which is essential for developers to understand the system's design, data flow, and how the components interact.

3.  **API Documentation**: The `README` includes extensive documentation for our REST APIs. It lists all available endpoints for user authentication, document and workspace management, AI analysis, and chat functionalities. Each endpoint description is accompanied by example `curl` commands, which serves as a practical guide for frontend development and for any third-party developers wishing to integrate with our platform.

4.  **Operational Documentation**: A dedicated troubleshooting section addresses common issues that may arise during setup or runtime, such as dataset download failures, database connection problems, and service startup errors. This is vital for operational efficiency, as it allows developers to quickly diagnose and resolve problems, ensuring the platform's stability.

# Weekly commitments

## Individual contribution of each participant


**Alexander Malyy:** 
- Implemented full chat microservice ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/61))
- Implemented the registration and authentication functionality, including: cookie-based authentication, JWT token generation, and user session management ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/93))
- Conducted an interview with a target user and collected feedback 
- Created a report for week 5

**Arthur Babkin:**
- Implemented the route for exporting the analysis as a PDF (as requested by users) ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/120))
- Added agent to validate found risks in analyzer microservice ([pr](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/124))

**Vladimir Zhidkov:**
- Conducted an interview with a target user and collected feedback 
- Helped with the backend authentication development
- Helped with report for week 5image.png

**Ilsaf Abdulkhakov:**
- Implemented comprehensive frontend development including layout design, user interface logic, and overall visual design system ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/59))
- Linked frontend with backend ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/112))

**Nikita Tsukanov:**
- Improved the retrieval speed and optimized the database queries ([issue](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/118))


## Plan for Next Week
- Continue working on improving the RAG pipeline
- Add the summary of the analysis to the report
- Ensure hosting robustness and resource availability
- Link domain name to the hosting


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
