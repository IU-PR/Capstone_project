
# **Week #4**

## Testing and QA

Our testing strategy primarily involved manual testing of all functionalities to ensure the absence of bugs. However,
due to time constraints, we were unable to fully test the new features—authorization and collections—manually. To
compensate, we developed cURL-based tests for API validation. Additionally, we have implemented frontend unit tests to
cover key components.

## CI/CD

### Links to CI/CD configuration files

Link to Continuous Deployment (CD) configuration file for the staging server:
https://github.com/IU-Capstone-Project-2025/Read-Tracker/blob/main/.github/workflows/docker-publish.yml

Link to CD configuration file for the production server:
https://github.com/IU-Capstone-Project-2025/Read-Tracker/blob/main/.github/workflows/docker-deploy.yml

## Deployment

Both environments were set up on virtual machines of Yandex Cloud. To deploy changes we use docker compose and for
continuous deployment we use GitHub Actions

### Staging

The staging server automatically receives all changes pushed to the main branch. This environment is used for internal
testing and validation before tagging for production. No domain name is assigned to the staging server, as it is not
intended for external or user-facing access.
It serves as a live preview of the most current state of development, enabling the team to catch issues early and verify
integration across components.

### Production

The production environment is updated by deploying the latest tagged commit from the main branch. It has a dedicated
domain name, as it is intended for end users and public access. Only stable, tested versions are released to production
to ensure reliability.

## Vibe Check

We conducted an informal online meeting where we discussed health and overall vibe. Everything is going well.

# Weekly commitments

## Individual contribution of each participant

- Batraz created a data dump containing 100 records and developed backend functions for user authentication and for
  handling collections in the database (/data_dump_books)

- Ivan Isakov implemented user authentication mechanisms. Also, he developed and conducted tests related to
  authentication
  and collections. (/auth-backend and /collection-testing)

- Darya worked on the collections feature and report. (/collections_backend)

- Ivan Savelyev developed frontend components for user registration and authentication.
  Moreover, he implemented frontend functionality for collections and wrote tests for the frontend. (/frontend)

- Andrey set up and configured CI/CD pipelines and collaborated on configuring the project domain. (/pipeline)

- Andrey & Darya jointly worked on setting up the domain for the project and environment setup for staging environment

## Plan for Next Week

- Implement the ability for users to read reviews from other users, including developing the necessary pages for this
  feature.

- Conduct user interviews to gather feedback on the user experience of our project.

- Perform small fixes and polish the existing functionality.

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
