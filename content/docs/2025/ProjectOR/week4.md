---
title: "Week #4"
---

# **Week #4**

## Testing and QA

#### By level of testing
1. Unit Testing
2. Integration Testing
3. Mock Strategy

##### Frontend Testing Infrastructure
- **Vitest** configuration with jsdom environment
- **Global test setup** with mocked localStorage and environment variables
- **Test scripts** in package.json for running tests in different modes
- **Path aliases** support for clean imports in tests

### Evidence of test execution

### Frontned
[Frontend Test Action](https://github.com/IU-Capstone-Project-2025/ProjectOR/actions/workflows/frontend-test.yml)
![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/images/frontend_test_cicd.png?raw=true)
![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/images/frontend_tests_results.png?raw=true)

### Backend
[Backend Test Action](https://github.com/IU-Capstone-Project-2025/ProjectOR/actions/workflows/backend_prod.yml)
![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/images/backend_tests_results.png?raw=true)

## CI/CD

We used `render.com` as a primary cloud-based platform for deploying and hosting our code. Also, we used GitHub actions as a CI/CD tool. One of the most tough challenge was to deploy frontend with environment variables. We overcame that using first build then deploy method.

### Links to CI/CD configuration files

[backend develop](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/.github/workflows/backend-develop.yml) \
[backend prod](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/.github/workflows/backend_prod.yml) \
[frontend develop](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/.github/workflows/frontend-develop.yml) \
[frontend test](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/.github/workflows/frontend-test.yml) \
[frontend prod](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/.github/workflows/frontend_prod.yml) \
[migrate](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/.github/workflows/migrate.yml)

## Deployment

### Staging

For staging environment we use render.com, we have github actions triggers
(`backend develop` and `frontend develop` pipelines). These helps create preview environments of services, 
these actions trigger on creating PR to the main branch, so we can preview all changes without redeploying 
the production build.

[backend dev](https://projector-backend-dev.onrender.com)
[frontend dev](https://frontend-develop-132n.onrender.com)

### Production
For production we also use render.com. Deploy pipelines triggers on push to the `main` branch

[frontend](https://projector-1.onrender.com)
[backend](https://projector-bp8n.onrender.com)

## Vibe Check

The team is on track with current goals and deliverables. Milestones are being met as planned, and overall velocity is consistent. No major blockers have been reported.

No critical roadblocks at the moment. Minor issues are being handled within the team without escalation. We’re maintaining good communication to catch any potential risks early.

# Weekly commitments

## Individual contribution of each participant

**Timur Nabiullin**: 
- Configured platform for application deployment and host
- Wrote CI/CD workflows 
- Fetched user feedback of our application

**Almaz Andukov**:
- Added a schema for changing the role
- Added /api/user/set-role to change the role of the current user
- Changed the user model in the database, added a role column (Enum)
- Added unit tests for the project router
- Added unit tests for the project service

**Nikita Timofeev**:
- Working on the MVP v1 redesign
- Added unit tests in the frontend side
- Added integration tests in the frontend side
- Implemented CI/CD action for the frontend

**Kirill Karsakov**: 
- Wrote a report
- Added new tasks to task board

## Plan for Next Week

- Conduct usability testing sessions
- Share your deployed application and solicit feedback
- Create new issues/user stories in the backlog for improvements and bug fixes
- Implement changes based on feedback
- Optimize performance where needed

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).