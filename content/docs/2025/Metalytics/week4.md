---
title: "Week #4"
---

# **Week #4**

## Testing and QA

- We implemented automated API tests for the backend using pytest and FastAPI’s TestClient.
- The tests cover all main endpoints: root, metals list, historical data, and forecast endpoints.
- Linting is enforced with flake8 to ensure code quality and style consistency.
- Manual QA was performed for the frontend by opening the site in a browser and verifying all UI features and interactions.

### Evidence of test execution

- [Tests with linting screenshot](https://raw.githubusercontent.com/IU-Capstone-Project-2025/Metalytics/refs/heads/main/Assets/backend-test.png) or [link to job](https://github.com/IU-Capstone-Project-2025/Metalytics/actions/runs/16028126489/job/45221300532).
- [Docker test screenshot](https://raw.githubusercontent.com/IU-Capstone-Project-2025/Metalytics/refs/heads/main/Assets/docker-test.png) or [direct link](https://github.com/IU-Capstone-Project-2025/Metalytics/actions/runs/16028126489/job/45221300559).
- [Frontend UI screenshot](https://raw.githubusercontent.com/IU-Capstone-Project-2025/Metalytics/refs/heads/main/Assets/front-test.png).

## CI/CD

- We used GitHub Actions for continuous integration.
- The workflow installs dependencies, runs linting (flake8), runs backend tests (pytest), and builds the backend Docker image.
- The workflow also runs the backend Docker container and checks the /health endpoint to ensure the app starts correctly.

Challenges faced:
- We encountered a ModuleNotFoundError for main in tests, which was fixed by setting PYTHONPATH=. in the workflow.
- Docker health checks required a sleep to allow the container to start before testing the endpoint.

### Links to CI/CD configuration files

- [Backend CI workflow](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/main/.github/workflows/ci.yml).
- [Backend Dockerfile](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/main/backend/Dockerfile).
- [Frontend Dockerfile](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/main/frontend/Dockerfile).

## Deployment

### Staging

In our workflow, the staging environment is set up on our local machines using Docker. This allows us to test the application in an environment that closely mimics production, but without any risk to real users or data.


**Staging process**:
- The development team runs the application locally using Docker Compose.
- All services are started with *docker compose build* command.
- The application is accessed via localhost.
- This environment is used for development, integration, and testing before deploying to the production server.

### Production

After successful testing in the local (staging) environment, the application is deployed to a production server on Timeweb Cloud.

**Production process**:
- The project repository is cloned to the Timeweb Cloud VDS.
- Docker and Docker Compose are installed on the server.
- The same Docker Compose command is used to build and start the services (*docker compose build*).
- The application is then accessible via the server’s [public IP](http://89.223.121.67:3000/).

## Vibe Check

This week, we conducted a team health check to discuss our progress, address any roadblocks, and ensure positive team dynamics.

- Progress:
The team is making steady progress on backend, frontend and ml components. We successfully set up local and cloud deployments using Docker and resolved several integration issues.

- Roadblocks:
Some challenges were encountered with Docker networking and frontend-backend communication, but these were collaboratively resolved. No major blockers remain at this time.

- Team Dynamics:
Communication within the team has been open and supportive. Everyone feels comfortable sharing ideas and concerns. We regularly check in during meetings to make sure all voices are heard.


- Action Items:
   * Continue regular check-ins to maintain transparency.
   * Support any team members who encounter technical or personal challenges.
 
The team vibe is positive and collaborative. Everyone feels heard and motivated to continue working towards our goals.

# Weekly commitments

## Individual contribution of each participant

- **Vladimir Toporkov** - Added [animations to the webpage](https://github.com/IU-Capstone-Project-2025/Metalytics/commit/0e8d990952db8ab85a38941f7d96954413e731d0), added [tests for backend](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/936dc038116398eea63810f5e6ceaa0e500dba04), wrote report.
- **Farit Sharafutdinov** -  Added multivariate regression and time-based features to LSTM. [Commit link](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/0814ab63b24b23ce95055ed8b84202a9e9b3913e/ml/forecasting_models.py).
- **Ilya Grigorev** - [Wrote model evaluation report](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/6311a671ca1baf7a37ca58a880782bee760606d8/ml/reports/Model_Evaluation_Report.pdf), added [hyperparameter tuning](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/9000cfe3991593ddfb8077ce4da19e382a90f8c5/ml/tuning_models.py) and [evaluation with cross-validation functionality](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/e90667180f4b1d7ad7bc7040fbdf19027a076d38/ml).
- **Rail Sharipov** - [Train model](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/d66d809cfb1fc3005da5e249bd125cefcd5ffd39/backend/train_lstm_model.py).
- **Askar Kadyrgulov** - [Deployed the project](http://89.223.121.67:3000/) and updated [backend to work with LSTM](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/f91dac1b0df03919a4b8188b04da08dbbe7e2e53/backend).
-  **Nikita Solomennikov** - Added [additional screen resolutions](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/6fd29df97c1c60fdd5f093f375d784f1981ff2b3/Assets/Metalytics.fig) in figma design. [Link to figma](https://www.figma.com/design/oqrwNbnmT7rRQNl58pdCmO/Metalytics?node-id=0-1&p=f&t=MYuHCdiiNLfEbW31-0).

## Plan for Next Week

- Start working on a long-term price prediction.
- Configure the database to automatically update the dataset.
- In figma add additional screen resolutions waypoints.
- Start working on implementation of different screen resolutions in HTML.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✓] In working condition.
- [✓] Run via docker-compose (or another alternative described in the `README.md`).
