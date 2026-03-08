---
title: "Week #4"
---

# **Week #4**

## Testing and QA

This week we focused on implementing testing strategy across our application to ensure reliability and maintainability of our Open Labs Share platform.

### Testing Strategy Implementation

- **Unit Tests**: Implemented unit tests for all microservices using Gradle testing framework
- **Integration Tests**: Created tests for fetching data from database to service and back
- **Cross-browser Testing**: Validated functionality across Chrome, Firefox, and Safari
- **Model Validation**: Implemented tests for RAG system accuracy and response quality

### Evidence of test execution

**Docker Build Test:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/actions/workflows/docker-build-test.yml)

**Service Tests:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/actions/workflows/service-tests.yml)

**Backend Services Build Validation:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/actions/workflows/build-validation.yml)

**Protocol Validation:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/actions/workflows/proto-validation.yml)


## CI/CD

This week we successfully implemented a complete CI/CD pipeline using GitHub Actions to automate our build, test, and deployment processes.

### CI/CD Pipeline Implementation

**Continuous Integration Setup:**

- **Build Validation Workflow**: Validates code builds and application compilation
- **Docker Validation Workflow**: Validates Docker containers functionality
- **Deployment Workflow**: Handles automated deployments to staging environment
- **Kanban Automation**: Automatically updates project boards based on PR status
- **PR Notification System**: Sends notifications in chat for pull request activities
- **Protocol Validation**: Validates gRPC protocol buffer definitions
- **Service Testing**: Runs service-level tests

**Continuous Deployment Setup:**

- **Staging Deployment**: Automatic deployment to staging environment on main branch merges
- **Production Deployment**: In progress
- **Rollback Capability**: In progress

**Pipeline Architecture:**
- **Multi-stage Pipeline in Deployment Workflow**: Test → Build and push Docker image → Deploy on `self-hosted` server
- **Parallel Test Execution**: Optimized for speed with parallel job execution
- **Caching Strategy**: Implemented Docker layer caching and dependency caching

### Links to CI/CD configuration files

**Build Validation Workflow:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/dev/.github/workflows/build-validation.yml)

**Docker Build Test Workflow:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/dev/.github/workflows/docker-build-test.yml)

**Deployment Workflow:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/dev/.github/workflows/deploy.yml)

**Kanban Automation Workflow:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/dev/.github/workflows/kanban-automation.yml)

**PR Notification Workflow:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/dev/.github/workflows/pr-notify.yml)

**Service Tests Workflow:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/dev/.github/workflows/service-tests.yml)

**Docker Configurations:** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/dev/docker-compose.yml)

## Deployment (Staging)

**Staging Deployment Process:**
1. Code push triggers GitHub Actions workflow
2. Automated testing
3. Docker images built and pushed to Docker Hub
4. Staging environment automatically updated via CI/CD
5. Health checks and executed

**Infrastructure:**
- `self-hosted` server (6/6 CPU, 16 GB RAM, 240 GB SSD)
- Cloudflare enabled
- CloudPub enabled (for redidrection `self-hosted` server's IP beyond university network NAT router)
- SSL certificate
- 2 domains: `open-labs-share.online` (active) and `open-labs-share.ru` (inactive)

**Working Environment URL:** [link](https://open-labs-share.online/)

**Important note: Current deployment is not production-ready. Since it is a new experience for us, we are not stopping on current strategy, plans and infrastructure and planning to improve it in the next weeks. This is not a final version of our deployment.**

## Vibe Check

**Team Health Assessment:**

**Progress Discussion:**
The team is performing pretty good this week. We've successfully tackled all major Week #4 objectives including testing, CI/CD implementation, and deployment setup. Correct team meetings, sprint planning, and other offline activities are working well.

**Roadblocks Addressed:**
1. **Testing Infrastructure**: Initially struggled with test environment setup due to lack of time, but resolved through collaborative debugging sessions.
2. **CI/CD Complexity**: GitHub Actions configuration required multiple idaeas to be handled and many-many iterations to make it work, but we successfully implemented it.
3. **Deployment Challenges**: `self-hosted` server configuration had one major issue: we were unable to access it from outside of university network because of university network NAT router. So, our first idea was to use Cloudflare to redirect requests to our server, but it was not working due to unable to proceed payment. So, we had to use CloudPub to redirect requests to our server. That is still require manual work to be done, but with aquired domain name and SSL certificate we are able to access our server from outside of university network successfully.

**Team Dynamics:**
- **Communication**: Our daily texts and in-person meetings have been really effective. Everyone speaking up, sharing their issues and ideas.
- **Code Review Process**: Peer review quality has improved significantly: we are checking each others code in our fields (Backend, Frontend, ML, Frontend) to better understand each other's work and to find potential issues and improvements.
- **Issue Management**: We've embraced GitHub's project management tools and they're really clicking for us. Our Kanban board gives everyone a clear view of what's in progress, while milestones help us stay focused on sprint goals. The labeling system makes it easy to filter and find specific types of work, and having clear assignees means no one's wondering who's handling what.
- **Work-Life Balance**: Unfortunately, we are libing with minor burnout issues. Also, Aleliya has been dealing with some serious health issues over the past couple weeks that have made it really tough for her to spend time at the computer. Despite this, she's been staying involved through our text chats and has even managed to help out with some design work.

**Action Items:**
- Continue weekly team retrospectives and planning sessions
- Continue team or semi-team offline coding sessions
- Continue to improve our time management and to be more efficient

# Weekly commitments

## Individual contribution of each participant

- **Kirill Efimovich (PM / DevOps):**

**Kanban board (clickable):** [link](https://github.com/orgs/IU-Capstone-Project-2025/projects/6/views/1) \
**Milestone (clickable):** [link](https://github.com/IU-Capstone-Project-2025/open-labs-share/milestone/4) \
**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/152), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/135), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/138), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/150), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/162), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/180) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/182), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/168) \
**Summary of TA feedback:** Nice MVP progress. Suggestions to improve our project and add cherry on top for our product (Marimo elements for example). Also, if the member of our team is ill, then we should reassign and rearrange tasks to other team members. \
**Weekly contribution:** Created ideas and implemented them in CI/CD pipeline for services, created deployment scripts, configured `self-hosted` server, worked with Cloudflare and CloudPub for redirection, expanded Kanban board and milestones, added multi-stage CI/CD pipeline, added staging deployment, fixed frontend bugs, written this report.
**Important note:** We are conducting sprints on Friday, so current week is not fully completed. Full result can be seen on Friday.

- **Mikhail Trifonov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/175), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/162), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/167), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/163), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/141), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/45) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/181), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/178), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/173), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/169), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/165), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/161), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/154) \
**Weekly contribution:** Implemented CI build verification script for all backend services, added proper username change handling with JWT token updates, achieved comprehensive test coverage for User Service with unit and integration tests, developed points system with balance tracking and lab counters including automatic balance management, created frontend balance display in profile and user panels with real-time updates across all pages, added submission cost notifications and disabled submit buttons for insufficient balance, conducted code reviews and fixed bugs including cleanup of teammates' code.
  
- **Nikita Maksimenko (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/136), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/159), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/146), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/124), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/184) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/183), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/179), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/171), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/129) \
**Weekly contribution:** Enhanced API Gateway service with comprehensive unit testing for service logic and input models, implemented all REST endpoints and gRPC service logic for submissions, comments, and feedback, updated documentation, participated in code review and bug fixing, closely work with backend team to fully connect the services.

- **Timur Salakhov (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/87), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/160), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/174) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/166), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/157), [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/155) \
**Weekly contribution:** Enhanced labs service with submissions loading functionality and implemented comprehensive testing suite for labs service.

- **Ravil Kazeev (Backend):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/170) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/183) \
**Weekly contribution:** Updated feedback service with new gRPC methods, refactored existing code, and migrated comments section from PostgreSQL to MongoDB.

- **Kirill Shumskiy (ML):**

**Closed issues (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/148) \
**Closed PR's (clickable):** [PR](https://github.com/IU-Capstone-Project-2025/open-labs-share/pull/133)\
**Weekly contribution:** Conducted auto-grading experiments, implemented inference API for large models, designed auto-grading architecture, validated baseline on test dataset, and wrote tests.

- **Aleliya Turushkina (Designer / Frontend):**

**Closed issues (with her assist) (clickable):** [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/142), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/136), [Issue](https://github.com/IU-Capstone-Project-2025/open-labs-share/issues/146) \
**Weekly contribution:** Sadly, was not able to contribute much this week due to health issues. Was able to help with some design work and joined team discussions.

**More detailed descriptions of services can be found by links from project `README.md` file [(link)](https://github.com/IU-Capstone-Project-2025/open-labs-share/blob/main/README.md).**

## Plan for Next Week

**Feedback Collection & User Testing:**
- Get our deployed app in front of actual users (classmates, TAs, and prof. Ivanov)
- Run some informal usability sessions - see where people get confused or stuck
- Collect and analyze feedback
- Document what works and what definitely doesn't

**Code Quality & Stability:**
- Fix the bugs we know about (and the new ones users will find)
- Improve error handling - make failures less catastrophic and more user-friendly  
- Clean up our codebase - better comments, remove dead code, consistent formatting

**Performance & Polish:**
- Make the UI more responsive
- Improve our CI/CD pipeline based on what we learned this week
- Better deployment stability - automate current manual CloudPub work

**Expected Reality Check:**
- A more stable, user-friendly version of our app
- Better deployment process that doesn't require manual intervention
- Start preparation for final demo with real user feedback incorporated

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).