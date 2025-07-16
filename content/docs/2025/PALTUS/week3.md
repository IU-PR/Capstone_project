# Practicum Project  
PALTUS team. Report 3

## Description of implemented MVP features and the functional user journey(s).

### Features

- An ability to generate and save a course based on user's parameters and willings.
- An ability to walkthrough generated course.
- An ability to track progress through marking subtopics as done/undone.
- An ability to delete a course.
- Error hadling:
  - *frontend* - validation in form.
  - *backend* - global exception handler, error response DTO, `EntityNotFoundException`.
  - System prompt handles incorrect user's input.
 
### Functional user journeys

**1. Course Creation Journey**

User Goal: Generate and save a personalized course based on their inputs.
  - User opens the website and get on the home page.
  - User clicks on "Create New Course".    
  - User provides inputs (e.g., topic, difficulty level, duration).    
  - Frontend validation ensures required fields are filled correctly (error handling).
  - User submits the form -> the system processes inputs and generates a structured course.    
  - User reviews the generated course and clicks "Save."    
  - The course is stored in their dashboard.<br><br>

**2. Course Progress Tracking Journey**
   
User Goal: Track learning progress.
 - User navigates to their dashboard and selects a saved course.
 - Course displays lessons in a sidebar and subtopics in lesson page.  
 - User clicks a checkbox next to a subtopic to toggle completion status.  
 - Backend updates progress and last activity time.<br><br>

**3. Course Deletion Journey**

User Goal: Remove an unwanted/completed course.
 - User views their list of saved courses.
 - User clicks a "Delete" button on the bottom of the course page.  
 - Frontend confirms the action.  
 - Backend processes the DELETE request -> course is removed from the dashboard.
  

## Demonstration of the working MVP.

Link to the video of a demo: [Google Drive](https://drive.google.com/file/d/1U965BjmcHg4k0Sn7m1Pr5RkGVyV-7cxI/view?usp=sharing) or [YouTube](https://youtu.be/WMYTLf23UPk)

## ML

API of LLM model was used, special prompt is used to implement necessary functionality.

## Internal demo.

For the current state of our product, we have only basic functionality, for areas of immediate improvement we defined the following:

  - Advanced error handling.
  - Add description for subtopics.
  - Add ability to add notes for subtopics.
  - Add ability to scroll the sidebar in course view.
  - Add navigation buttons for course view.
  - Mark lesson as finished in course view.
  - Add adaptive layout.
  - Add authorization (probably).
  - Add ability to edit course before saving it into user's courses.
  - Add CI/CD for tests.

## Weekly commitments

### Individual contribution of each participant

- Sergey Knyazkin
  - [Logic of a home page](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/c11f3d1324c9db4cff5e4e5c3c7bcfd43d35f76e).
  - Added requests [for course view](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/57d271bbe3c2ebf6e503cbe3ebcc0099793197e2), [for adding a course](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/7dc93b718e3ceace5ea73d48ed83a435c98dfbbe), [for Home page information](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/e09d4525c02e72133946fa43c7ae7d26ec4069ad), [for deleting a course](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/1c278f2e9226aa63fcb884c6665f31a5bcd869c6).
  - Updated [frontend Dockerfile](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/a0fce64b15569d9f3f5b95aa02351079cbc2d001).
  - [Fixed bug with a course topic prop](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/02216e4b396aa40ca29d0b4404903c257752354c).
- Ramazan Gizamov
  - Added relative font-sizing [commit](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/bfc99b9f9874fbe8acb8704685ea62427faa64b3).
  - [Report for week 3](https://github.com/poeticlama/PALTUS/new/master/content/docs/2025/PALTUS/week3.md).
- Aidar Sarvartdinov
  - [Added CORS](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/c4c6b3e3d4af33f4f3a71083c3e26024c0b4462a).
  - [Error handling on backend side](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/317176addc83722d5b4eab24d5ff5ca4a035cc09).
- Igor Dubrovsky
  - [GET request for dashboard](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/3e25acefe019224f2c3f7f80e8fd80099bc54c63).
  - [Save last activity time for course then subtopic finished or course created](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/4180d299f0c2029c59cf42b51fec42fae83cc5c1).
  - [Add ability to mark subtopic as finished](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/216c1df7ad858227e762a7847cad717c2a6082de).
- Amir Fayzullin
  - [Unit test for StringListConverter ensure reliable data conversion](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/71f73d268275970df0de77fa17566944fa61007a).
  - [Unit test Validates entity-DTO transformation logic in CourseMapper](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/6099af7a4109b346a7e472fe6ab0885adaed4b49)

## Plan for Next Week

### *Frontend*

- Add ability to scroll the sidebar in course view.
- Add navigation buttons for course view.
- Mark lesson as finished in course view.
- Add adaptive layout.
- Add description for subtopics.

### *Backend*
  - Add ability to edit course before saving it into user's courses.
  - Advanced error handling.
  - Add description for subtopics.
  - Add authorization.

### *DevOps*
  - Configure frontend Dockerfile for build version
  - Configure CI/CD

## Confirmation of the code’s operability

We confirm that the code in the main branch:
Run via docker-compose.



