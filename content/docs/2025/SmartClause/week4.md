---
title: "Week #4"
---
## Testing and QA

**Testing Methodology:**
- Isolated test environment using an in-memory SQLite database
- Response structure validation to ensure API contracts are maintained
- Mock data approach for testing without external dependencies
- File upload simulation using BytesIO for document processing tests
- Both happy path and error path testing to ensure robust error handling

**Test Types implemented:**
- API Health Tests
- Functional API Tests
- Input Validation Tests

### Evidence of test execution

**Coverage by Endpoint**

| Endpoint                      | Coverage Status                        |
|-------------------------------|----------------------------------------|
| `/` (root)                    | ✅ Tested                              |
| `/health`                     | ✅ Tested                              |
| `/api/v1/retrieve-chunk`      | ✅ Tested (happy path + validation)    |
| `/api/v1/retrieve-rules`      | ✅ Tested (happy path)                 |
| `/api/v1/analyze`             | ✅ Tested (happy path + validation)    |


**Coverage by Test Type:**
- Functional tests: All main endpoints tested for expected responses
- Input validation: Basic validation tests for key endpoints
- Response structure: Validation of response formats for all endpoints
- Database integration: Basic setup with SQLite test DB

![cicd](https://github.com/IU-Capstone-Project-2025/SmartClause/blob/course-metadata/course-metadata/week4/cicd.png?raw=true)

## CI/CD

**Implemented stages in CI/CD:**
- Checkout - Jenkins pulls source code from git to the server
- Test - runs tests on all microservices
- Deploy - final build of the code, if the previous stages didn't break

**Tools used:**
- Jenkins
- Docker 
- Github

**Challenges:**
During my first experience with CI/CD configuration, I encountered a number of difficulties:
there were difficulties with organizing the pipelines and setting up communication between servers.
Automating the deployment and setting up a test environment proved to be challenging, and testing without a raised environment proved difficult.
In addition, the Jenkins container lacked a Docker client, which interfered with working with containers.
In addition, I encountered many other difficulties. All this made it very difficult to build a convenient and reliable Pipeline. - Vladimir Zhidkov

### Links to CI/CD configuration files

https://github.com/IU-Capstone-Project-2025/SmartClause/blob/dev/Jenkinsfile

## Vibe Check

This week was hard to work on the project due to several reasons:
- All team members had deadlines for their other courses
- Main backender/devopser got really sick and was unable to work on the project
- The load needed to be distributed between the other team members
- Some tasks from this week were postponed to the next week due to the above reasons
- Despite all the difficulties, we continue our R&D process and try to find the best way to implement the final product

# Weekly commitments

## Individual contribution of each participant


**Alexander Malyy:** 
- Defined the final user flow [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/68)
- Defined the final API endpoints [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/99)
- Implemented part of the API for spaces and documents management [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/101)
- Partially created a report for week 4

**Arthur Babkin:**
- Evaluated different embedding models and studied optimal parameters for RAG [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/102)
- Evaluated indexing algorithms for RAG and improved microservice throughput [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/103)

**Vladimir Zhidkov:**
- Implemented CI/CD pipeline [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/100)
- Partially created a report for week 4

**Ilsaf Abdulkhakov:**
- Designed the final UI/UX [(issue)](https://github.com/IU-Capstone-Project-2025/SmartClause/issues/97)

**Nikita Tsukanov:**
- Polished the retrieval pipeline and added comperehensive evaluation and metrics to compare different retrieval techniques [(PR)](https://github.com/IU-Capstone-Project-2025/SmartClause/pull/111)

## Plan for Next Week

1. Implement registration and login system
2. Implement chat microservice
3. Link frontend to backend
4. Gather user feedback and improve the product

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
