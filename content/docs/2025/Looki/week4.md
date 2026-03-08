# Testing and QA

## Summary of testing strategy and types of tests implemented
- Implemented unit tests for core modules to verify business logic.
- Added integration tests to ensure modules interact correctly.
- Conducted end-to-end tests simulating user workflows.
- Manual exploratory testing performed for UI and edge cases.

---

# Evidence of test execution
- [CI/CD](https://github.com/IU-Capstone-Project-2025/Looki/actions)
- [Screenshots](https://drive.google.com/drive/folders/1jCK4jX5jlidUjQF9Jl1yiYNp3QU5pGQE?usp=sharing)
- All tests passed successfully on the latest CI run.

---

# CI/CD

## Description of CI/CD setup, tools used, and challenges faced
### Pipeline stages include
- Running unit and integration tests for both backend and frontend on every push.
- Verifying the correctness of the application code.
- Automatically deploying the updated version of the app to a rented server after successful tests.
- Deployment is triggered on every push to the main branch, keeping the production environment up-to-date.

### Tools and technologies used
- GitHub Actions for managing CI/CD workflows.
- SSH access to the rented server for deployment.
- Automation scripts for updating code, installing dependencies, and restarting services on the server.

### Challenges and solutions
- Initial issues with dependency synchronization during deployment were resolved by properly managing environment updates on the server.
- Secrets and access keys are securely managed through GitHub Secrets.
- Automated testing helped quickly catch and fix errors before deployment.

---

## Links to CI/CD configuration files
- [GitHub Actions workflow](https://github.com/IU-Capstone-Project-2025/Looki/tree/main/.github/workflows)
- [Docker Compose file](https://github.com/IU-Capstone-Project-2025/Looki/blob/main/docker-compose.yml)

---

# Deployment

## Staging
- Staging environment is hosted on a dedicated rented virtual server.
- Environment closely mirrors production setup for reliable testing.
- Automated deployment occurs on every successful merge.
- Deployment scripts handle code update, dependency installation, and service restart.

## Production
- Production environment runs on the same rented VPS with Ubuntu 22.04.
- Deployment is automatically triggered on every push to the main branch after passing tests and code review.

---

# Vibe Check
- Team progress is on track, with weekly goals being met consistently.
- Roadblocks include minor delays caused by API changes and external dependencies.
- Team dynamics are positive, with good communication and collaboration among members.
- Everyone feels heard and supported despite the team currently having 3 active members out of a total of 7.

---

# Weekly commitments

Nikita Shiyanov - developed comprehensive automated tests for backend and frontend; architected and implemented Docker Compose setup with separate containers for production, development, and isolated test environments including dedicated test database; configured CI pipelines to build, run tests inside containers, and deploy to rented VPS server with automated rebuilds on main branch pushes, wrote report
Aleksandr Gavkovski — refactored the architecture, fixed registration bugs, migrated the project to more modern technologies, and wrote tests for the frontend.
Ilya Maksimov - created try_on screen: displayed 3d-model and added card with clothes; implemented a change of 3d model in makehuman by parameters that are sent via http request and exported 3d model with new parameters

---

# Plan for Next Week
- Finalize the production deployment process.
- Complete the generation of the personalized 3D human model.
- Fix bugs and improve error handling.
- Update and improve the UI/UX design.
- Work on integrating 3D clothing models.

---

# Confirmation of the code’s operability

We confirm that the code in the main branch:
- [x] Is in working condition.
- [x] Can be run via Docker Compose as described in the README.md.
