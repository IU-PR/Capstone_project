---
title: "Week #4"
---

# **Week #4**

## Testing and QA

We have implemented several tests related to the healthyness of the microservices and the validity of its behaviour. 

*For backend & frontend*

We test endpoints for get requests by checking that each of them returns its own html page.

*For Airflow*

We are testing the availability of the web ui airflow. Since the testing container is launched after the airflow-scheduler is launched, we can be sure that airflow is alive and has started executing tasks, and the healthyness of the web ui allows us to make sure that the executed tasks will be displayed.

*For Postgres*

We check the availability of the database by creating a new connection.

*For Keycloak & LDAP*

We test that person can authenticate in our service by login & password sending POST request to the backend endpoint. (Watch the remark below)

**!Extremely Important Remark!**

One of the test in our pipeline relates to the authentication. And we have remote authentication service located on the same machine as backend. This way we keep the ports related to the authentication service closed and they cannot be reached from the outside (for security reasons.)

That is why the test aimed at checking authentication fails in github-actions ***(this is its valid behavior by our standards)***. This test is intended for testing strictly on the server. That is why in the pipeline script at the stage "Check test results" we skip the error related to authentication test failure.

### Evidence of test execution

Here you can see the screenshot with testing output (Before watching, please pay attention to the remark above)

![Pytest tests report](https://raw.githubusercontent.com/BogGoro/IU-Capstone-Project-2025/refs/heads/main/testing_logs.jpg)

On that screen, there are all the task preparation stages (Each of these stages has more than 100 lines of logs, so we are not able to open and screen them)

![CI Environment Preparation Tasks](https://raw.githubusercontent.com/BogGoro/IU-Capstone-Project-2025/refs/heads/main/ci_preparation_tasks.jpg)

On this screenshot you can see test checking stage and deploying stage.

![CI Logs](https://raw.githubusercontent.com/BogGoro/IU-Capstone-Project-2025/refs/heads/main/ci_logs.jpg)

On the following picture, there is a test coverage report which shows, that our tests cover 48% of code.

![Code Coverage](https://raw.githubusercontent.com/BogGoro/IU-Capstone-Project-2025/refs/heads/main/code_coverage.jpg)

## CI/CD

#### Description of CI/CD setup
CI/CD pipeline consists of several subtasks. First 9 tasks are related to environment configuration. We install docker/docker-compose and build all the required images there. The last stage of the build for the tester container triggers testing script. Thus, at the end of the 9th task, we get a test.log file that is inside the tester container.

At the next stage, we extract this file and, using a bash script, check it for errors other than those related to authorization (see the Remark above)

After which, at the next two stages, we deploy the solution to the server if it has passed all the stages above

#### tools used
During the CI/CD pipeline our code tests using ***pytest*** and builds using ***docker/docker-compose*** which are pre-installed on the runner during several pipeline steps 

#### challenges faced
While testing the pipeline, we encountered the problem that the backend docker image does not pull up the local .env file unless it is explicitly specified in docker compose, even if this problem does not exist locally

### Links to CI/CD configuration files

*[github-actions CI/CD yml](https://github.com/IU-Capstone-Project-2025/Recommendation-System/blob/dev/.github/workflows/pipeline.yml)*

*[Additional Script for testing that is used in the pipeline](https://github.com/IU-Capstone-Project-2025/Recommendation-System/blob/dev/wait_for_services.sh)*

*[Auxiliary Script for deploying](https://github.com/IU-Capstone-Project-2025/Recommendation-System/blob/dev/deploy.sh)*

## Deployment

### Staging

The system uses Docker Compose to deploy 8 containers across 2 networks. There are 3 Airflow containers (webserver, scheduler, and PostgreSQL database), 4 backend containers (main service, tester, PostgreSQL, and ClickHouse), and 2 auth containers (Keycloak and LLDAP). The backend connects to both databases while Airflow uses its own PostgreSQL instance and shared volumes. All components communicate through dedicated bridge networks. The tester verifies backend, Postgres and Airflow integration. Kubernetes deployment with Hadoop support is planned for the next couple of weeks.

Access to the web application is implemented through the nginx balancer. The nginx configuration can be viewed in the project files.


## Vibe Check


We continue to hold regular meetings to discuss task assignments and coordinate who will take on which responsibilities. All team members agree with this approach, as it allows for an even distribution of workload and ensures that no one is assigned tasks beyond their capabilities.
Recently, we began practicing closer collaboration between certain team members, organizing separate sessions for them to work more effectively together. As a result, a PR with contributions from two members was created.

Last week, one of the team members faced challenges with the parser implementation. This week, the team organized a joint brainstorming session to discuss this issue, suggest potential solutions, and collaboratively search for useful resources during the meeting.  Overall, the team communication remains strong, and everyone feels supported.
# Weekly commitments

## Individual contribution of each participant

- **Denis Troegubov:**
    - Replaced greenplum with clickhouse [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/32)
    - Automated airflow and adjusted DB schema [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/36)


  
- **Timur Garifullin**:
    - Refactored environment variable handling, improved code readability, and fixed import and syntax issues in backend [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/39)
    - Enchanced auth system by handling tokens and user data in correct way. Implemented DB stored books display on catalog page. [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/48/)


- **Grigorii Belyaev**:
    -  Implemented a Selenium-based parser with Edge WebDriver and stealth settings to bypass site protection and extract full book metadata into CSV [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/44)

  
- **Peter Zavadskii:**
    - Fixed the connection issues between the backend and Keycloak [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/35)
    - Added logic for sending book data from the user to the database [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/39)
    - Added unit tests and configured CI [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/45)
    - Added deploying stage in CI/CD pipeline, added more unit tests and troubleshooted the whole pipeline. [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/46)



- **Adelina Karavaeva:**
    - Improved book page UI: added animated star rating, status selection, save button with success notification. Fixed comment section layout and book description alignment. [Link to PR](https://github.com/IU-Capstone-Project-2025/Recommendation-System/pull/43)



## Plan for Next Week


Since the priority this week shifted to the CI/CD implementation task, we postponed our previous weekly plans. Additionally, during the process, critical technical issues arose — replacing the database, refactoring the backend, fixing Keycloak integration problems, and improving the parser — which required immediate attention. This also deprioritized the implementation of user feedback features, book listing, and sorting functionality.

Therefore, next week we plan to:



- Implement user feedback features (add support for submitting and displaying comments on book pages)
- Develop book listing and sorting functionality (Top, Popular, Popular per week, Recomendation)
- Continue working on UI improvements


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
