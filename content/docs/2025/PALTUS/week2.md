# Practicum Project  
PALTUS team. Report 2

## Detailed Requirements Elaboration

### 1. User Management & Progress Tracking
  - Users can mark subtopics as completed.
  - Display user’s course progress (e.g., completed 5/10 lessons).

### 2. Course Management
  - Fetch all user's courses (ID + name) for course selection.
  - Fetch course content - lessons, subtopics, etc.
  - Users can delete courses.
  - Save LLM-generated courses to the database.

### 3. Frontend Application
  - MVP pages: Home, Course View (with lessons), Course Creation View, Login View.
  - Persist progress data in browser storage (local/session).
  - HTTP requests to backend endpoints.

### 4. Backend Services
  - Enable cross-origin requests for frontend-backend communication.
  - Process user inputs via LLM API to generate courses.
  - Optimize database queries for course/lesson retrieval.

### 5. Non-Functional Requirements
  - Responsive layouts
  - In future, code formatting enforced via CI/CD.
  - Docker Compose setup for single-command execution.

### 6. Dependencies & Risks
*Dependencies* 
  - LLM API reliability.
  - Asana backlog prioritization for task alignment.

*Risks* 
  - Inconsistent progress tracking if subtopic/lesson logic fails.
  - CORS misconfiguration blocking frontend requests.



### Prioritized backlog

[Asana board](https://app.asana.com/1/1210531224311325/project/1210531182984698/board/1210531325851441)

## Project specific progress

### *Frontend*

Finished layout for neccessary pages for MVP, configured some libraries for needed functionalities.

### *Backend*

Created functions for getting the course with all the content inside, to get IDs and names of all courses, deleting a course, getting a certain lesson, saving generated course in database.

### *Other*

Created README.md for the project, fixed prompt for LLM-model, finished design of an app in Figma, discussed gamification ideas, set up task board in Asana.

# Weekly commitments

## Individual contribution of each participant

**Sergey Knyazkin** 
  - [Created layout for all the pages of MVP](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/f3610ba3e6ecf9af1958984c41c45421a01a1f09)
  - [Configured Pinia to maintain global state of an app](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/44e1432efe8e2b1c1f9111e6310f3a980b50ef36)
  - [Configured Vue router](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/cf79f3b41754b2128faf1c2b526ccb6dec820ce0)
  - [Configured Axios for HTTP requests](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/79eb047173a76e57f7ff7c4f15195105b94d96d7)

**Ramazan Gizamov** 
  - Added [README.md](https://github.com/IU-Capstone-Project-2025/PALTUS/blob/main/README.md)
  - [Report for week 2](https://github.com/poeticlama/PALTUS/edit/master/content/docs/2025/PALTUS/week2.md)
  - Finished [Figma](https://www.figma.com/design/rvNoC6oOC2Xe5y7yWIhLuN/Demo-visuals) design with working prototype

**Aidar Sarvartdinov** 
  - [Created database structure](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/901bc8cfeab41232e42effdb5354fb21a869eb64)
  - [Configured interactions with database](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/85ddc9723916b237dacaf0caa6dc3f0fdba1ddc5))
  - [Database request optimization](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/0c327b1c3414826d79ea8e07554a7d0f84cf0b04)
    
**Igor Dubrovsky**
  - [Docker configuration](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/9893206f896f0bcd8ad35a0e6ddf6045e1cbdd33)
  - Added [LLM API integration](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/2675a740064904d786bcc62b7ad4fd7853ed0b44) to communicate with the user

**Amir Fayzullin** 
  - Fixed [prompt](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/8ced1df87a7b4e2edfc3ca007eaffc050fe62d1e) for LLM model 
  - Added [system prompt](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/8ced1df87a7b4e2edfc3ca007eaffc050fe62d1e) for validation of user's inputs

**Danil Demin** 
  - Introduced [gamification ideas](https://github.com/IU-Capstone-Project-2025/PALTUS/blob/main/notes/meetings/week2meet1.md) for the app

## Plan for Next Week

### *Frontend*
  - Set up requests
  - Configure storage for a course to track learning
  - Develop a logic for a few frontend features

### *Backend*
  - Add ability to mark subtopic as finished
  - Mark lesson as completed if all subtopics finished
  - Get request for dashboard
  - Calculate last unfinished lesson(for dashboard)
  - Configure CORS for request
  - Refactor books and links entity as just array of values

## Confirmation of the code’s operability

We confirm that the code in the main branch:
Run via docker-compose.



