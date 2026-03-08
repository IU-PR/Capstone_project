---
title: "Week #4"
---


# **Week #4**


## Testing and QA


### Frontend
Manual testing scenarios were designed and are checked locally before each merge.
### Backend
Integration tests with Testcontainers and an in-memory server were designed and implemented to validate endpoints and interactions with a PostgreSQL database. Tests focus on endpoints with prior known bugs (e.g., storages and recipes retrieval) and security concerns (e.g., leakage of other users' information). Testcontainers spins up PostgreSQL containers for realistic testing, while the in-memory server ensures fast, isolated execution. Tests run automatically in the CI pipeline on every push to dev or main.


### Evidence of test execution


![Image](https://github.com/user-attachments/assets/d1a81483-2640-46a4-bb73-33767421341c)|


![Image](https://github.com/user-attachments/assets/fc42b43d-03fc-4cf4-b38c-00403411b430)


![Image](https://github.com/user-attachments/assets/28d6af67-65a4-48cc-83cf-1dd0f6ea652c)


![Image](https://github.com/user-attachments/assets/8b01da27-24a8-48fd-b352-aae30fb9af23)


## CI/CD


Backend and Frontend source code is stored in separate repositories. For both of them the main and dev branch has a CI workflow, which is triggered on each push. Frontend CI is designed mainly for checking linting with clang-tidy and clang-format. Backend CI runs integration tests. Root repository of our project includes submodules with Frontend and Backend repositories. There, on each push to dev or main, a CD workflow is triggered. It:
- Pulls the last changes from corresponding branches in submodules (either dev or main).
- Builds in parallel the Frontend and Backend images using corresponding Dockerfiles.
- Logs into Dockerhub using credentials from GH Actions Secrets and push created images tagged with the id of commit.
- Connect via ssh to our remote server (Innopolis University Virtual machine).
- Chooses the directory, depending on to which branch the code was pushed. (main branch to /app or dev branch to /app-stage)
- Rewrites the .env file is correct directory with details from GH Actions Secrets (e.g. bot token, DB credentials, images names with newly created tags)
- Runs "docker compose down && docker compose up" command to rebuild the application with updated Frontend and Backend Docker images.


### Links to CI/CD configuration files


- Frontend CI workflow files - https://github.com/Endpool/CookCookhNya-frontend/tree/dev/.github
- Backend CI workflow file - https://github.com/Endpool/CookCookhNya-backend/tree/dev/.github/workflows
- Root repository CD workflow - https://github.com/Endpool/CookCookhNya/blob/dev/.github/workflows/CI-CD.yml


## Deployment
Both stage and production versions of the application are hosted on Innopolis University virtual machine. In ~/rash/app - production version, in ~/rash/app-stage - stage version. Both directories have an .env file which is recreated on each push by GH Action CD workflow. Also both directories have a compose.yaml, with support of pulling images tagged by CD workflow. To ensure applications do not overlap, they use different telegram bot tokens and separate external port mappings (8080 for production and 8081 for staging).




## Vibe Check


Vibe is good. Everyone's opinion matters, except DevOps one((


# Weekly commitments


## Individual contribution of each participant


| Team member                             | Contribution |
|-----------------------------------------|------------------|
|Maxim Fomin (Lead)|Fix linting errors - https://github.com/Endpool/CookCookhNya-frontend/pull/47. Implemented inline ingredient search on frontend- https://github.com/Endpool/CookCookhNya-frontend/pull/45. Implemented the shopping list view - https://github.com/Endpool/CookCookhNya-frontend/pull/50|
|Ilia Kliantsevich|Designed the scenarious for manual Frontend testing - https://github.com/Endpool/CookCookhNya-frontend/blob/dev/Testing.md. Implemented Shopping List creation - https://github.com/Endpool/CookCookhNya-frontend/pull/51. Implemented reciepe view - https://github.com/Endpool/CookCookhNya-frontend/pull/48|
|Amirkhan Kurbanov|Impemented storage members addition/deletion rework & Message edition update - https://github.com/Endpool/CookCookhNya-frontend/pull/49. Contributed to Frontend testing scenarious - https://github.com/Endpool/CookCookhNya-frontend/blob/dev/Testing.md|
|Daniel Gevorgyan|Designed and wrote integration tests for backend - https://github.com/Endpool/CookCookhNya-backend/pull/48|
|Vadim Ksenofontov|Implemented endpoints for shopping list - https://github.com/Endpool/CookCookhNya-backend/pull/45. Implemented DB error handling - https://github.com/Endpool/CookCookhNya-backend/pull/39|
|Aleksandr Gorbanev|Implemented endpoints for Recipe Details - https://github.com/Endpool/CookCookhNya-backend/pull/42. Implemented ingredient search - https://github.com/Endpool/CookCookhNya-backend/pull/43. Fixed storages and getting all ingredients method - https://github.com/Endpool/CookCookhNya-backend/pull/46. Made tests for recipes - https://github.com/Endpool/CookCookhNya-backend/pull/50 |
|Rashid Badamshin|Implemented and optimised the CI pipeline with tests for Backend - https://github.com/Endpool/CookCookhNya-backend/pull/48. Configured the hosting server to deploy a staging version of application from dev branch and updated the CD pipeline accordingly - https://github.com/Endpool/CookCookhNya/pull/34|




## Plan for Next Week


- Adding observability for hosting server
- Adding more tests to the backend
- Feature for users to create custom private ingredients
- Feature for users to create custom private recipes
- Feature for users to publish private ingredients and recipes


## Confirmation of the code's operability


We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).



