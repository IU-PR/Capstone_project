# Practicum Project  
PALTUS team. Report 4

## Testing and QA

### Testing Approach
1. Unit Testing Layer:
- Converters (Tested StringListConverter):
  - Null/empty inputs
  - Single/multi-item handling
  - Whitespace trimming
  - Bidirectional conversion

- Mappers (CourseMapper transformations):
  - Course <-> DTO conversions
  - Lesson/Subtopic mappings
  - Data integrity checks

2. Integration Testing Layer:
- Spring Context Test (application context loading):
  - Spring bean initialization
  - Profile-based configuration
  - Dependency wiring
    
3. API Controller Testing:
- CourseController (Mock-tested REST endpoints):
  - GET /courses (dashboard)
  - GET /courses/{id} (course details)
  - DELETE /courses/{id}
  - POST /courses/saveCourse
 
### Evidence
[Screenshot folder in Google Drive](https://drive.google.com/file/d/19Ylxnkw9g5e4c_-syTJ1TetXSx5ajJ79/view?usp=sharing)
  

## CI/CD
1. Trigger: On push/pull request to main or dev
2. Environment:

   - Ubuntu latest runner
   - Java 17 (Temurin distribution)
   - Spring test profile activation
3. Test Execution:

   - Isolated H2 database for tests
   - Surefire plugin for test reporting
   - Parallel-safe test configuration
4. Quality Gates:

   - Block merge on test failures
   - Artifact upload for test reports
5. Self-hosted CD

### Links to CI/CD configuration files
[Tests folder](https://github.com/IU-Capstone-Project-2025/PALTUS/tree/main/backend/src/test)

[CI/CD](https://github.com/IU-Capstone-Project-2025/PALTUS/blob/main/.github/workflows/ci.yml)

## Deployment

### Staging Environment

The staging environment is built by using Docker Compose, providing a setup for final testing before release.

Infrastructure Provisioning:
- PostgreSQL 15 database container
- Spring Boot backend service container
- Frontend application container
- All services connected via Docker network



| Service             | Port Mapping   | Configuration               | Dependencies        |
|---------------------|----------------|-----------------------------|---------------------|
| PostgreSQL 15       | 5432:5432      | .env variables              | Persistent volume   |
| Frontend            | 5175:5173      | Hot-reload enabled          | Backend service     |
| Backend             | 8081:8080      | Spring profiles, DB config  | PostgreSQL          |

### Access 

- http://10.90.137.167:5175/

This staging environment provides:

- Final integration testing
- User acceptance testing (UAT)
- Performance benchmarking
- Security validation


## Vibe Check

The discussion was done during the least meeting of the 4th week, we are a bit behind the plan and our ambitions and also the tasks are not clearly splitted in a proper way, so we decided to fix that during next meetings.

## Weekly commitments

### Individual contribution of each participant

- Sergey Knyazkin
  - [Add registration page](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/24bf50bdfe00fdbfc8776402149b3b9e3bebc3ad).
  - [Add expansion panel with profile settings](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/3aa5809ae0d69c7070c1a333944d0617a976692a).
  - [Refactor CourseView](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/9a70e90f43f6ce7d05484bc269e4d45b7558e76b).
  - [Make scroll only on a sidebar](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/5102a5c8df8831013327ba5e989469175fa382d1).
  - [Configure VM on vm.innopolis.university/](http://10.90.137.167:5175/)
- Ramazan Gizamov
  - [CD configuration](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/47d41ba67590b14d458220864074ab30dbdc2b01)
  - [Figma design for Quiz and Achievements pages](https://www.figma.com/proto/rvNoC6oOC2Xe5y7yWIhLuN/Demo-visuals?node-id=0-1&t=lkMobF4VojzpdDli-1).
  - [Report for week 4](https://github.com/poeticlama/PALTUS/new/master/content/docs/2025/PALTUS/week4.md).
- Aidar Sarvartdinov
  - [Add connection between user and his courses](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/c4c6b3e3d4af33f4f3a71083c3e26024c0b4462a).
  - [Authorization](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/05c6667c6561bdf36bb5c7a38bad6413c8fcfa9a).
- Igor Dubrovsky
  - [Exception logger as aspect](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/44adbb2e711ad8a88ec12f821f176d086d7e0d5a).
  - [Ability to change course during its creation](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/2122028a405931147213f3c8306ee94f15fa41a8).
  - [Add otes that user can edit and content generation for subtopic](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/108c6fb84f58798eb4bb15220138b10e6ab93440).
- Amir Fayzullin
  - [Fixed tests](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/1492366198120431bc02dd71f990179c05f6580b).
  - [Add CourseControllerTest](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/0ea7c16fe1c9d3c31c9cf31d73660cdbd48f643e).
  - [Configure CI](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/cef58cb62486169ff81735848f481558d393c068)

## Plan for Next Week

### *Frontend*
- Request fot authorization and registration.
- Add possibilities to change the course.
- Add design features (navigation, scroll bars, etc).
- Add tests.

### *Backend*
- Quizzes generation.
- Acceptance of a created course.
- Generation of additional content for subtopics.
- Daily streak.

### *DevOps*
- Update Dockerfile for the frontend application.

## Confirmation of the code’s operability

We confirm that the code in the main branch:
Run via docker-compose.
