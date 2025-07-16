---
title: "Week #4"
---

# **Week #4**

## Testing and QA

As part of our testing strategy, we focused initially on implementing unit tests for the service layer of the backend. This decision was made to ensure that the core business logic is thoroughly tested in isolation, without external dependencies like databases or web layers. Unit testing the service layer allows us to catch logical errors early and keep our codebase maintainable and reliable.

At this stage, only unit tests for service and controller parts have been written. In the next steps, we plan to extend test coverage to other layers of the application. For example, integration tests will be added to cover the controller layer and verify the interaction between components and the overall system behavior.

We used JaCoCo to generate a code coverage report, providing visibility into the extent of test coverage and helping us identify untested code areas.

### Evidence of test execution

JaCoCo test coverage report is stored in backend directory after mvn verify task in target/site/jacoco/index.html.
Links to the screenshots: [Screenshot_1](https://drive.google.com/file/d/1PezSuEzlJIsuwtLHXf4dA4E_SDbjIJ29/view?usp=sharing), [Screenshot_2](https://drive.google.com/file/d/1yaP8O-qFJMpdRRGn4mW_JnXKMBjwy9Ja/view?usp=sharing), [Screenshot_3](https://drive.google.com/file/d/103hh47OBhJwlS9T68P3b2CyYt30KJJPA/view?usp=sharing)


## CI/CD
The project uses a complete CI/CD pipeline powered by GitHub Actions. The
pipeline includes the following key stages:

### Continuous Integration (CI)
- Docker builds: All Dockerfiles in the repository — both for the machine learning services and the backend — are built and tested to ensure they work correctly.
- Flutter: The Flutter frontend is linted and built as part of the pipeline to catch issues early.
- Linting & static analysis: Code quality checks are applied to ensure clean and maintainable code across all components.
- `jaCoCo` in target directory in backend part for detection of code coverage by tests

### Continuous Deployment (CD)
- Self-hosted GitHub Actions runners are used to execute deployment jobs.
- These runners automatically deploy the latest versions of the application using docker-compose, based on the branch or environment.
- The deployment includes the backend, ML models, and all related services as defined in the docker-compose.yml.

### Environment separation
- Different environments (e.g., stage and production) are handled via branch-based deployments and environment-specific configurations.
- Secrets and environment variables are managed through GitHub Environments and Actions secrets.

### Challenges
Some of the challenges faced during CI/CD setup included:

- Configuring self-hosted runners with proper systemd services to ensure stability.
- Ensuring consistency across Docker builds and networking in docker-compose.
- Syncing main and stage branches
- Allowing the PR's to main only from main (resolve it within some CI workflow)

### Links to CI/CD configuration files

- [Build Docker images](https://github.com/IU-Capstone-Project-2025/FishMasters/blob/main/.github/workflows/build-backend.yaml)
- [Build & linting for flutter](https://github.com/IU-Capstone-Project-2025/FishMasters/blob/main/.github/workflows/flutter-ci.yaml)
- [Checker for PR in main (it is allowed only from stage)](https://github.com/IU-Capstone-Project-2025/FishMasters/blob/main/.github/workflows/branch-checker.yaml)
- [Deployment by button for STAGE](https://github.com/IU-Capstone-Project-2025/FishMasters/blob/main/.github/workflows/deploy-stage.yaml)
- [Deployment by button for PROD](https://github.com/IU-Capstone-Project-2025/FishMasters/blob/main/.github/workflows/deploy-prod.yaml)
- [Java CI](https://github.com/IU-Capstone-Project-2025/FishMasters/blob/stage/.github/workflows/java-tests.yaml)

### Staging
- From now on, a dedicated staging environment has been introduced for pre-production testing.
- It is deployed manually (by button) from the stage branch using the same CI/CD pipeline.
- Staging has its own domain name and infrastructure, isolated from the production environment.
- This allows testing new features, integration, and deployments in a safe and reproducible environment before promoting them to production.
- All services — backend, ML components, and frontend — are deployed via docker-compose on a separate self-hosted runner.
- Environment-specific secrets and configuration are managed independently using GitHub Environments and Actions secrets.
- This separation ensures safer deployments, early detection of integration issues, and a more reliable development lifecycle.


## Production
The production environment has been set up on a dedicated Virtual Dedicated Server (VDS) and swagger for backend is publicly accessible at:

[https://capstone.aquaf1na.fun/swagger-ui/index.html#/](https://capstone.aquaf1na.fun/swagger-ui/index.html#/)

This environment is fully separated from staging and represents the live version of the application. It is used for final delivery, testing under real conditions, and demonstration purposes.

### Infrastructure and Deployment
- Each major component (backend, ML services, etc.) is containerized and deployed using docker-compose.
- The production backend is hosted on a separate VDS from the staging environment to ensure isolation, security, and performance.
- Both the staging and production servers are set up with reverse proxies (nginx) that route incoming HTTPS traffic to the appropriate internal services.
- SSL/TLS certificates are configured using Let's Encrypt, ensuring secure HTTPS connections.



## Vibe Check

The team is functioning well with strong collaboration, all members actively contributing to their assigned areas without major problems

# Weekly commitments

## Individual contribution of each participant


Stepan Vagin:
- Started Qdrant cluster, link to the screenshot provided, since it is needed to use API-key to access dashboard,[Screenshot](https://drive.google.com/file/d/1Zt6cU66snqOMZ2Fjb1N17vwUcxWGeXGb/view?usp=sharing)
- Wrote program, that uploaded all fish enteries into the Qdrant, [Screenshot](https://drive.google.com/file/d/1qsouVIjhrjfhHAiXzb4yEFVGYR8bULBn/view?usp=sharing)
- Build faiss indexing, qwen text embedding, debugged system, build CLI for usage, build Qdrant access for faiss and much more, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/75)
- Task distribution


Kostya Zimin:
- Realize endpoints with service logic for getting fishes, fish, fishings, fishing. Create new exceptions and solve bugs, [issue](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/70)
- Create Testing structure, add JaCoCo for test coverage checking with automatic generated html file in target directory at backend. Create tests for service logic, [issue](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/76)

Ivan Vasiliev:
- rebuild embeddings (cleaned the input descriptions, used another embedding model) datasets can be found here https://disk.yandex.ru/d/1UGiENnMIG0OSg
- fixed the base model that find relevant fish
- executed experiments with 3 different models and fine-tuned their parameters to achieve the fastest the most accurate model, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/75)

Kirill Greshnov:

- Add functionality to 'My Catch' Page and connect with backend, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/92)
- Connect photo upload, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/97)

Egor Belozerov:
- Setup stage environment fully, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/78)
- Configure stage VDS server + setup stage gh runner + configure stage nginx
- Create CI for ensuring that PR to main can be only from STAGE, commited into main, so no pr, [Commit](https://github.com/IU-Capstone-Project-2025/FishMasters/commit/8e03c71659f6ab3f5890607d3664a72624b1cd64)
- Introduce java tests into CI pipeline, [Link](https://github.com/IU-Capstone-Project-2025/FishMasters/blob/stage/.github/workflows/java-tests.yaml)

Damir Sadykov:
- Change the fishing event, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/87/)
 - Add real counting of catches
 - Fix connection bugs for start / end of event
 - Reconstruct the Fishing page
 - Add some drafts for future improvement (catches gallery with editing)

Adel Gaznanov:
- Wrote few mock tests, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/85)
- Fix bugs related to endpoints and openAPI naming, [PR_1](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/74), [PR_2](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/89), [PR_3](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/91)
- Add possibility for users to upload photos of caught fish during fishing, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/93)


## Plan for Next Week
- Write more tests
- Continue connecting backend and frontend
- Integrate ready ml system into the project
- Fixing bugs
- Implementing new features 

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).