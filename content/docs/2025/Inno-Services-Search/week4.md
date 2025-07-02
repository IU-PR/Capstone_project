---
title: "Week #4"
---

# **Week #4**

## Testing and QA

**Vladimir** wrote tests and generated test coverage for core functionality of the project:
- minio(needed as core moodle files storage)
- search flow - ensure proper processing results from ml, proper fallback to mongo search, proper mongo results processing.
Also he implemented github workflow to run tests in push/PR, so only tested code can be placed in the repository (see [commit](https://github.com/one-zero-eight/search/commit/82e1b48d850e63fd94bb7ce5f9fcdb58ba884b20)).

### Evidence of test execution

![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week4/tests1.png?raw=true)
![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week4/tests2.png?raw=true)

CI logs [link](https://github.com/one-zero-eight/search/actions/runs/16025185230/job/45211261584)
## CI/CD

The project uses GitHub Actions for automated building, testing, and deployment of all components:

### Website (Frontend)
- Build & Deploy:

  Workflow: [.github/workflows/deploy.yaml](https://github.com/one-zero-eight/website/blob/capstone/.github/workflows/deploy.yaml)

  - Builds static files with pnpm

  - Deploys via appleboy/scp-action to Innohassle server

  - Supports:

    - staging deployment by default

    - capstone deployment from a specific branch

  - Files served via Nginx under:

    https://search.innohassle.ru

- Lint & Format Checks:

  Workflow: [.github/workflows/lint.yaml](https://github.com/one-zero-eight/website/blob/capstone/.github/workflows/lint.yaml)

  - Runs ESLint and Prettier on every push and pull request

### Search (Backend)
- Build & Deploy (Docker):

  Workflow: [.github/workflows/build-docker.yaml](https://github.com/one-zero-eight/search/blob/main/.github/workflows/build-docker.yaml)

  - Builds Docker image and publishes to GitHub Container Registry (ghcr.io)

  - Manual or main branch deploy triggers SSH-based deployment to Innohassle server

  - Runs a custom server-side deployment script to restart API

  - API accessible via:

    https://api.innohassle.ru/search/staging-v0

- Pre-commit Checks:

  Workflow: [.github/workflows/pre-commit.yaml](https://github.com/one-zero-eight/search/blob/main/.github/workflows/pre-commit.yaml)

  - Runs pre-commit hooks with ruff.

  - Uses Poetry with local virtual environments

- Automated Tests:

  Workflow: [.github/workflows/run-tests.yaml](https://github.com/one-zero-eight/search/blob/main/.github/workflows/run-tests.yaml)

  - Runs pytest on push and pull requests

  - Uses Poetry for dependency management

  - Copies settings.example.yaml for test configuration

### ML Component
- Deployment:

  Workflow: [.github/workflows/build-docker.yaml](https://github.com/one-zero-eight/search/blob/main/.github/workflows/build-docker.yaml) (deploy-ml job)

  - SSH deployment to a GPU-enabled server

  - Runs server-side deployment script to restart Python processes

## Links to CI/CD configuration files

Backend workflow [link](https://github.com/one-zero-eight/search/tree/main/.github/workflows)

Frontend workflow [link](https://github.com/one-zero-eight/website/tree/capstone/.github/workflows)

## Deployment

### Staging and production

Our staging environment meets production requirements: domain name, public access, real data, integration with real external services

- Website: https://search.innohassle.ru

- API: https://api.innohassle.ru/search/staging-v0

- Static files and API deployed to the Innohassle server (Innopolis)

- ML service connects to a separate GPU server, restarts after updates

The project launch for end users will be available at https://innohassle.ru

## Backend

**Azaliia** implemented the handling of maps resources along with a dedicated MongoDB schema, added a specialized function to handle the unique transformation of maps data into LanceDB attachments (see [commit](https://github.com/one-zero-eight/search/commit/f203020ba5fe9b07ea35bd9d95b5badc9123ff71)). **Azaliia** also made changes to the backend so that by default the search occurs across all resources (see [commit](https://github.com/one-zero-eight/search/commit/cb65c581df9d179063f6f7e5d76bd0b42a44b284))

To make search results more specific, it was necessary to refactor the parsers so that mongo entries were small parts of the site pages, namely anchors. To do this, **Anna** refactored the clubs parser for campuslife (see [commit](https://github.com/one-zero-eight/search/commit/824f68a44ae09e645f5a6ad680398807b4bb3168)), the campuslife general information parser (see [commit](https://github.com/one-zero-eight/search/commit/8766201563bc82e0dc8672f977d16b333e19576a)), and the eduwiki parser (see [commit](https://github.com/one-zero-eight/search/commit/1348f4b085440f2c81c8a7da85182dd77bb00071)). **Anna** also did team management (see the [kanban board](https://github.com/orgs/one-zero-eight/projects/4), `search` project), and reviewed all the PRs, merging them into the main (debug commit [#1](https://github.com/one-zero-eight/search/pull/98/commits/0fdb59eaf29ddc4d640cfe9e74c5902f4127cbf8), [#2](https://github.com/one-zero-eight/search/commit/bcdb426ac8d46c3f34a8dcf756e8f12761d3fff2), for example).

**Aliia** added a new resource to the search pipeline: wrote a parser for the [Innopolis residents' website](https://sez-innopolis.ru/residents/), added its processing to the backend and ml (see [commit](https://github.com/one-zero-eight/search/commit/a3d9d71a7f8b798c20c3da71d9b98c472b44f4f4))

## Frontend

**Aliia** added search example below the search field (see [commit](https://github.com/one-zero-eight/website/commit/741697dc4d4b4c0d91882567831f1986f6837004)) and added `response_types` filtration and preview text in `SearchResult` (see commits [#1](https://github.com/one-zero-eight/website/commit/e55efb2a04aae4b00d1f9ad2832f27c4f1ea0087#diff-07ff1bddf1a165691ab50b17df460fd91338557bf254b17cc7bc44d9e08c3b22) and [#2](https://github.com/one-zero-eight/website/pull/213))


## ML

**Sofia** fixed the duplication of fragments during the search (see [commit](https://github.com/one-zero-eight/search/commit/03a846592dedafbfbc859c1d984c341eed68833e) and [commit](https://github.com/one-zero-eight/search/commit/b818d684480098bf506c3e097cd11f178b6f0036)), and the text preview was also optimized for XML tags (see [commit](https://github.com/one-zero-eight/search/commit/994c1171b7841e81684fc415ec088ba88b96fe83)). In addition, a full-fledged stack for `ask` was created, including the definition of Pydantic models, the implementation of a FastAPI endpoint, integration with the RAG search system, and interaction with an external LLM via OpenRouter (see [commit](https://github.com/one-zero-eight/search/commit/e0f06f0274b09920e2b3fa70674f4b49148da60c)).

**Azaliia** also created a [dataset](https://docs.google.com/spreadsheets/d/1Q9SwNH2yBCkL_TCIoj3L1JRfgEZlX-Zc5eADguABHoQ/edit?usp=sharing) to evaluate the performance of the search.

## Overall progress
Overall, this week we improved the user experience (see the hints for entering the search bar; the link to the resource is valid on the entire area of ​​the search answer card; the design is adapted for intuitive clicking on the link), clarified the resources (divided the sites into different cards using anchors), added previews to the sites (see the description of the site at the bottom of the card)

![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week4/progress.png?raw=true)

## Vibe Check

The team is happy with the current progress of the project, we have done a lot of work and our results are even ahead of our initial expectations. Need: We should make sure that all areas of development are covered and think about lightweight features that we can implement to make our progress more visible. Communication within the team is effective and we all feel heard.

# Weekly commitments

## Individual contribution of each participant

| Team Member           | Contribution                                       |
|-----------------------|----------------------------------------------------|
| Anna Belyakova (Lead) | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week4/#backend) section     |
| Vladimir Paskal       | See [testing and QA](https://capstone.innopolis.university/docs/2025/inno-services-search/week4/#testing-and-qa) section                           |
| Azaliia Alisheva      | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week4/#backend) and [ML](https://capstone.innopolis.university/docs/2025/inno-services-search/week4/#ml) sections|
| Aliia Bashirova       | See [frontend](https://capstone.innopolis.university/docs/2025/inno-services-search/week4/#design--frontend) and [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week4/#backend) sections |
| Sofia Pushkareva      | See [ML](https://capstone.innopolis.university/docs/2025/inno-services-search/week4/#ml) section                              |


## Plan for Next Week

- Improve search for new resources (we will need to make changes to the parsers, perhaps clarify the model prompt)
- Link the frontend of the `ask` functionality with the backend
- Rewrite the project to uv (faster than poetry, better resolves dependencies, more convenient CI/CD)
- Continue to expand the list of resources for search
- Start working on `act` (write more specific user stories with resources and interaction architecture, explore available technologies)

## Confirmation of the code's operability

**!!!** The working code in the backend repository is in the `main` branch, and in the frontend repository in the `capstone` branch (difficulties due to automatic deployment)
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).