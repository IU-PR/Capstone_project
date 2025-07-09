# Week #4

## Summary of testing strategy and types of tests implemented.

### Backend

#### 1. Overall Testing Strategy

The backend of the project is tested using a comprehensive, multi-layered approach to ensure correctness, stability, and security of the API and business logic. The primary testing framework is Django’s built-in test runner (leveraging unittest), supplemented by **pytest** and **coverage.py** for enhanced flexibility and reporting. Tests are seamlessly integrated into the CI/CD pipeline, enabling early detection of regressions and ensuring a robust backend.

#### 2. Types of Tests Implemented

##### 2.1. Unit Tests

- **Purpose:** Validate individual components such as models, views, serializers, and utility functions in isolation.
- **Tools:** Django TestCase, unittest, pytest.
- **Examples:**
  - Testing model methods and signals.
  - Testing custom utility functions and helpers.
  - Testing serializer validation and output.

**Example files:**
- `backend/goalsight/matches/tests.py`
- `backend/goalsight/predictions.test_ml_service.py`
- `backend/galsight/predictions/tests/test_prediction.py`

##### 2.2. Integration Tests

- **Purpose:** Verify interactions between multiple components, including models, views, and the database.
- **Tools:** Django TestCase, pytest-django.
- **Examples:**
  - Testing API endpoints using the Django test client.
  - Verifying authentication and permission workflows.
  - Testing multi-model or multi-service workflows.

**Example files:**
- `backend/goalsight/predictions/tests.py`
- `backend/goalsight/predictions/tests/test_prediction.py`

##### 2.3. Mocks and Fixtures

- **Purpose:** Isolate tests from external dependencies and ensure consistent test data.
- **Tools:** Django fixtures, pytest fixtures, unittest.mock.
- **Examples:**
  - Mocking external API calls.
  - Using fixtures for predictable database setups.
- **Example files:**
  - `backend/goalsight/predictions/tests/test_data/X_test.csv`
  - `backend/goalsight/predictions/tests/test_data/Y_test.csv` 

#### 3. Test Coverage

- **Unit and integration tests** cover all critical models, views, serializers, and business logic.
- The goal is to achieve high coverage of the backend codebase, ensuring all major API endpoints and workflows are thoroughly tested.
- Coverage reports are generated using **coverage.py** and uploaded as CI artifacts for review.
- **Result for unit tests:** [To be filled based on actual results]
- **Result for integration tests:** [To be filled based on actual results]

#### 4. Configuration and Test Execution

- **Django’s test runner** is used by default, with **pytest** for advanced testing scenarios.
- Tests are executed in the CI pipeline using **Docker Compose** to replicate a production-like environment (e.g., PostgreSQL, Redis).
- Environment variables and secrets are injected via the CI workflow, eliminating the need for a local `.env` file.

#### Conclusion

The backend testing strategy encompasses unit, integration, ensuring comprehensive coverage of business logic and API endpoints. This approach guarantees the stability, reliability, and security of backend services, providing confidence in the system’s performance under diverse scenarios.

### Frontend

#### 1. Overall Testing Strategy

The frontend of the project is covered by a multi-layered testing approach to ensure reliability, correctness, and a high-quality user experience. Modern testing tools such as **Jest**, **React Testing Library**, and **Cypress** are used. Tests are integrated into the development and CI/CD process, enabling early detection and resolution of issues.

#### 2. Types of Tests Implemented

##### 2.1. Unit Tests

- **Purpose:** Validate individual components, functions, and hooks in isolation.
- **Tools:** Jest, React Testing Library.
- **Examples:**
  - Testing UI components (e.g., `MatchCard`, `TeamItem`, `NextMatchCard`).
  - Testing custom hooks (`useAllTeamInfo`, `useMatchForecast`, `useUpcomingMatches`).
  - Testing utility functions and API calls (using mocked servers and data).

**Example files:**
- `frontend/__tests__/component_tests/MatchCard.test.tsx` [Link to file](https://github.com/IU-Capstone-Project-2025/GoalSight/blob/main/frontend/__tests__/component_tests/MatchCard.test.tsx)
- `frontend/__tests__/component_tests/TeamStatsPanel.test.tsx` [Link to file](https://github.com/IU-Capstone-Project-2025/GoalSight/blob/main/frontend/__tests__/component_tests/TeamStatsPanel.test.tsx)
- `frontend/__tests__/component_tests/useAllTeamInfo.test.ts` [Link to file](https://github.com/IU-Capstone-Project-2025/GoalSight/blob/main/frontend/__tests__/component_tests/useAllTeamInfo.test.ts)

##### 2.2. Integration Tests

- **Purpose:** Verify the interaction between multiple components, hooks, and APIs.
- **Tools:** Jest, React Testing Library.
- **Examples:**
  - Ensuring correct rendering of data fetched from the server.
  - Testing components working together (e.g., match forecast panel with real data).
  - Verifying routing and prop passing between components.

**Example files:**
- `frontend/__tests__/api/api.test.tsx` [Link to file](https://github.com/IU-Capstone-Project-2025/GoalSight/blob/main/frontend/__tests__/api/api.test.ts)
- `frontend/__tests__/api/tournamentApi.test.tsx` [Link to file](https://github.com/IU-Capstone-Project-2025/GoalSight/blob/main/frontend/__tests__/api/tournamentApi.test.ts)

##### 2.3. End-to-End (E2E) Tests

- **Purpose:** Test complete user scenarios in a real browser environment.
- **Tools:** Cypress.
- **Examples:**
  - Testing full user journeys (e.g., browsing tournaments, viewing matches, interacting with the UI).
  - Verifying navigation, forms, error handling, and success flows.

**Example files:**
- `frontend/__tests__/cypress/e2e/userJourney.cy.ts` [Link to file](https://github.com/IU-Capstone-Project-2025/GoalSight/blob/main/frontend/__tests__/cypress/e2e/userJourney.cy.ts)

##### 2.4. Mocks and Helpers

- Mock servers (`frontend/__tests__/mocks/server.ts`) and data are used to isolate tests from the backend.
- File mocks (`fileMock.js`) ensure asset imports work correctly in tests.

#### 3. Test Coverage

- **Unit and integration tests** are written to cover the main logic, UI components, custom hooks, and their interactions.
- The goal is to achieve high coverage of critical user interface elements and business logic, ensuring that most user scenarios and edge cases are tested.
- Coverage reports generated by the test runner Jest are used to monitor which parts of the codebase are tested and to identify areas that may require additional tests.
- Result for unit tests:
- Result for API integration tests:
- Result for e2e tests:

#### 4. Configuration and Test Execution

- **Jest** is used for unit and integration tests, with separate configs for different test types (`jest.config.api.js`, `jest.config.components.js`).
- **Cypress** is used for E2E tests, configured via `cypress.config.ts`.
- All tests can be run locally and in the CI/CD pipeline.

#### Conclusion

The frontend testing strategy includes unit, integration, and end-to-end tests, which ensures high reliability and user interface quality. Unit tests cover almost everything in components in all parameters, integration tests cover everything 100%.

### ML

This test suite verifies the functionality and performance of a machine learning prediction service integrated into a Django backend.

#### Testing Strategy

**The testing strategy combines unit tests and integration tests to validate both**:
  - Correctness of the prediction logic 
  - Reliability of the model's performance metrics 
  - Proper model loading and error handling

**The tests are organized into two key modules**:
  - test_metrics.py — validation of training quality metrics 
  - test_prediction.py — validation of prediction service behavior

#### Types of Tests Implemented
  1. Model Loading and Configuration Tests
  **Ensures that all necessary artifacts (model.pkl, scaler.pkl, features.json, class_mapping.json) are correctly loaded**:
    - test_model_loading() checks object integrity and presence of all expected components. 

  2. Prediction Output Tests
  **Validate the structure, correctness, and consistency of the prediction output**:
  - test_prediction_success() verifies prediction is made, has all required fields, and that probability values are valid (sum to 1, confidence in range [0,1], etc.).

    3. Metric Threshold Tests
  **Located in test_metrics.py, these ensure model quality is above minimum accepted levels**:
  - test_cv_accuracy_threshold() checks if cross-validation accuracy is ≥ 0.40. 
  - test_f1_macro_threshold() ensures F1 macro average ≥ 0.40.

#### Manual Test Execution

```
cd .\backend\goalsight\predictions\
pytest .\tests\
```

## Evidence of test execution (e.g., screenshots of test reports, CI logs). Code coverage report if available.
[Unit tests for Frontend](https://drive.google.com/file/d/1SPwN_haX9n9_83K5G__17Sy5iqmldZLE/view?usp=sharing)

[Test coverage for Unit Tests](https://drive.google.com/file/d/1xifL5IglDN7CbCUQqBImROKpYvhncBLj/view?usp=sharing)

[API integration](https://drive.google.com/file/d/1cIQLwcvgHDA0sJrrqF4m5I1bJIp6rGTB/view?usp=sharing)   

[E2E test](https://drive.google.com/file/d/1lMFzXqpCEfyMDvP6k5FybVf_ORmg5JGN/view?usp=sharing)   

## Link to CI/CD configuration files (e.g., .github/workflows/main.yml).
`.github/workflows/`
## Link to the live, deployed application on the staging environment.
[link to deployed application](http://goalsight.ru) [link to the staging enviroment](http://staging.goalsight.ru:8080/)
## Description of your staging (and production, if applicable) environment setup.

### Infrastructure

- The project is containerized using Docker and orchestrated with Docker Compose. 
- Both backend (Django) and frontend (React) services, as well as the PostgreSQL database and Nginx reverse proxy, are defined in docker-compose.yml. 
- The environment can be run locally or on any server supporting Docker (e.g., cloud VM, local server).

- ### Services and Dependencies  

- **Backend**: Django (Python 3.11), served via Gunicorn. 
- **Frontend**: React (Node.js 18), built and served via Node. 
- **Database**: PostgreSQL 15. 
- **Web Server**: Nginx as a reverse proxy. 
- **ML/Analytics**: Python-based ML models in ml_models. 
- **Testing**: Uses Jest, Cypress, and Django’s test runner. 
- No Redis or other external services are currently configured.

### Configuration

- Environment variables for database credentials, Django secrets, and allowed hosts are injected via GitHub Actions secrets in the CI workflow.
- Docker Compose files reference these variables and .env files for local development.
- No sensitive configuration is committed; secrets are managed through the CI/CD pipeline.

### Deployment Process

- Deployment and testing are automated via GitHub Actions.
- The CI pipeline builds Docker images, runs containers, applies migrations, and executes backend and frontend tests.
- The same process can be used for both staging and production by switching the Docker Compose file.

### Differences Between Staging and Production

- Staging: Uses docker-compose.yml, may run on different ports (e.g., Nginx on 8080), and can use mock or test data.
- Production: Uses docker-compose.yml, runs on standard ports (80/443), and is configured for full security and performance.
- Both environments are otherwise similar to ensure parity.

### Access and Monitoring

- Access is typically limited to developers and QA testers for staging; production is public or restricted as needed.
- Monitoring is handled via container logs; no external error tracking or monitoring service is currently configured.
- No public staging URL is provided in the repo, but Nginx is configured to serve both frontend and backend.

### Testing Context
**The CI pipeline runs**:

- Django backend unit and integration tests.
- React frontend component and API integration.
- Code coverage is collected for both frontend and backend.The environment closely mirrors production, ensuring reliable validation of new features and bug fixes.

## Summary of vibe check discussion and any action items. (PMs)

The Vibe Check took place in the format of a conversation, each team member could calmly speak out and complement what others had said earlier. The results presented here are an aggregation of the discussion results.

### First part - fast vibe check. (5 min)

**Question:**

- Please give grade by your vibe on the previous sprint(week) in range from 1 to 10.

**Results:**

- **Arina Zimina**: 8

- **Artem Panov**: 7

- **Karina Siniatullina**: 6.5

- **Egor Sergeev**: 7

- **Egor Agapov**: 8

### Second part - Achievements and blockers. (10 - 15 min)

**Questions:**

- What achievements have we achieved this week?

- What difficulties have you had this week?

**Results**:
- **Achievements**:
  - The entire website design is fully implemented.
  - All APIs are enabled.
  - The backend handles requests correctly.
- **Blockers**:
  - Discomfort due to the fact that everything was completed on the last day of the sprint.
  - Problems with matching tasks from the Week with commits from GitHub.
  - Problems with insufficient data for processing by the model.
  - Low model metrics.
### Third part - Questions about teamwork. (10 - 15 min)

**Questions:**

- How are you in general?

- What difficulties have you had this week?

- How do you like the atmosphere in the team?

- Is it easy for you to express your opinion in the team?

- Are you able to handle the volume of tasks?

- Is the help you receive from the team sufficient?

- Are you getting help from the team fast enough?

**Results:**

- Everything is not bad, the MVP was done.

- Yes, it's easy to express an opinion. There is an understanding that they will always listen carefully and then discuss.

- Sometimes AI tools help with a large amount of tasks.

- Yes, there is enough help and it comes quickly when needed.

### Forth part - "Start-Stop-Continue". (10 - 15 min)

**Results:**

-**Start**:
  - Write about changes in any part of the project (frontend/backend/ML) as soon as possible to avoid conflicts when building the project.
  - Write about the start of the work and attach a plan in the morning, report the results in the evening.

-**Stop**:
  - Postponing the main tasks for the last 2 days of the sprint.

-**Continue**:
  - Open communication between team members.

### Conclusion

Strong team dynamics and a culture of open communication provide a solid foundation for the implementation of the planned actions. The main focus should be on solving time management and last-minute work issues while maintaining a positive collaborative atmosphere that allows for effective problem solving.

## Individual Contribution of Each Participant

- **Arina Zimina**: 
  - Integration tests for the API. | Creating endpoints performance tests | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/bbd302677326161d3035f502fd5a8d2e7c3a01d5) 
  - Unit tests for models. | Creating tests that verify that the model is filled in correctly | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/bbd302677326161d3035f502fd5a8d2e7c3a01d5) 
  - Configuring servers and domain for deployment | Finding optimal servers for production and staging environments and linking a domain name to a production server | [Link to production environment](http://goalsight.ru) | [Link to staging environment](http://staging.goalsight.ru:8080) 
  - Implemented the deployment process in 2 environments (production and staging) | Installing secrets in the actions github, configuring docker files, docker-compose files, nginx configurations, and generating ssh keys to access the server | [After this commit, the production started working](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/d65c238226004873665e6d350abd280e8cd7fb5c) | [After this commit, the staging started working](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f86204bb69af80acf7e0c09a84b5f81b2e2d89b3) 
  - Specified CI/CD pipelines for two environments | Created a copy of the CI/CD pipeline and corrected the copy for staging environment | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f75c3e1361196dc3e82d22926ec828180b4a32c7)

- **Artem Panov**:
  - PM:
    - Template for individual contribution of each participant part in report.
    - Meeting organization and Task distribution | [Link to Kanban board in Weeek](https://app.weeek.net/ws/809762/shared/board/9EzSZCfNpJ1cEVKXROUAmIuRNIFZt8Rj)
    - VibeCheck - part in report.

  - ML:
    - ML Model Validation. | 
      - Implementation of cross-validation to improve the reliability of the model
      - Create a confusion matrix for performance analysis 
      - Add precision/recall/F1 metrics | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c03de2821c4a757b7d103ef19b0a1c7785279bd7)
    - Tests for ML endpoints. | 
      - Unit tests for prediction endpoint
      - Tests for model loading and initialization
      - Testing the model for compliance with the minimum threshold for accuracy and f1 metrics | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c03de2821c4a757b7d103ef19b0a1c7785279bd7)


- **Karina Siniatullina**:
  - Unit tests for react components. | Implemented unit tests of design, display, and error tolerance for all react components | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/1b899e86b7a56b3584bb7d6d1d0aa81c7a6abd8c)
  - Setting up test coverage for unit tests. | Implemented test coverage for unit tests and improved coverage | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c0a034b6be627ae4c117ea19f92ba09e37742145)
  - Setting up test coverage for API integration tests. | Implemented test coverage for API integration tests and improved coverage | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c0a034b6be627ae4c117ea19f92ba09e37742145)
  - Frontend part in README.md and report. | Added a description of running the tests in README.md for the frontend and wrote a description of all the tests for the frontend for the report | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/66792573671f77eca255b5d026bb7d34fa79d5cd)


- **Egor Sergeev**:
  - GitHub Actions CI Pipeline. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f75c3e1361196dc3e82d22926ec828180b4a32c7)
  - Write a weekly report.

- **Egor Agapov**: 
  - Integration of tests with API. | Implemented API integration tests of rendering of data fetched from the server, components working together,  and outing and prop passing between components. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/7191fe86d52a5926d9d503db907bdb82afc58d5d) 
  - E2E tests of the main user journey. | Implemented E2E tests of full user journeys and verifying navigation, forms, error handling, and success flows. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/26ff656f6f86264573dff4bfe179fa447ef0165a) 
  - Configuring servers and domain for deployment | Finding optimal servers for production and staging environments and linking a domain name to a production server | [Link to production environment](http://goalsight.ru) | [Link to staging environment](http://staging.goalsight.ru:8080) 
  - Implemented the deployment process in 2 environments (production and staging) | Installing secrets in the actions github, configuring docker files, docker-compose files, nginx configurations, and generating ssh keys to access the server | [After this commit, the production started working](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/d65c238226004873665e6d350abd280e8cd7fb5c) | [After this commit, the staging started working](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f86204bb69af80acf7e0c09a84b5f81b2e2d89b3) 
  - Specified CI/CD pipelines for two environments | Created a copy of the CI/CD pipeline and corrected the copy for staging environment | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f75c3e1361196dc3e82d22926ec828180b4a32c7)
## Weekly Commitments
### Plan for Next Week

#### Sprint Goal

Feedback, Iteration & Polishing _Goal: Gather user feedback, iterate on the MVP, and improve overall project quality._
#### Frontend

**High priority**:
- Transitions between pages - Egor A, Karina
- Solve bugs with outdated stuff - Karina
- Fix the loader on both pages - Egor A
- Fix the tab display in the browser - Egor A
- Improve integration tests for working with the backend - Egor A
- Improve Cypress test - Egor A
- Fix the hover on the header - Egor A
- In the mobile version, adapt heder - Egor A
- Add more statistics - Karina
- Improve the display of statistics - Karina
- Redo tournament queries for statistics - Karina
- Fix the clickability of checkboxes - Karina
- Add instructions to the forecast -  Karina
- Pin the forecast at the top - Karina

**Medium**:
- Add coverage for cypress - Egor, Karina
- Create an About us page - Egor, Karina
#### Backend

**High priority**:
- Provide database updates every week - Arina Zimina
- Search for new APIs to get data - Arina Zimina
#### ML

**High priority**:
- Exploring approaches and ideas to improve the ML part - Artem Panov
- Development of new model designs - Artem Panov
- Prioritization of features and the use of those features that we can receive through the API on the backend - Artem Panov

#### Feedback

**High priority**:
- Find at least 10 people from different user types who agree to participate in the survey - Egor S
- Create a checklist for the survey to make it easier to collect feedback - Egor S
- Conduct surveys - Egor S
- Aggregate survey results and create a list of improvements for the project based on this - Egor S


#### Sprint acceptance criteria

Feedback has been collected and an improvement plan based on it has been drawn up, improvements have been implemented on the frontend that improve performance and usability, research has been conducted on the ML part and several prototypes of model designs have been created, data is loaded into the DB automatically via the API.