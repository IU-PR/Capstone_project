# Practicum Project  
PALTUS team. Report 6

## Links

- Deployment:
- Docs: [README.md](https://github.com/IU-Capstone-Project-2025/PALTUS/blob/main/README.md), [api docs](https://github.com/IU-Capstone-Project-2025/PALTUS/tree/docs/backend/src/main/java/com/paltus/backend)
- Design: [Figma](https://www.figma.com/proto/rvNoC6oOC2Xe5y7yWIhLuN/Demo-visuals?node-id=0-1&t=DavTpLzLzLBFOWSe-1)
- Demo: [Google Drive](https://drive.google.com/file/d/1V9wfvfOaQE4dwFPFoQbJqLrLlIAixLil/view?usp=sharing)
- Kaiten board: [Screenshots of the board](https://drive.google.com/drive/folders/16Y-MQXpZghhkoxADxd6L7syHdWsxzkpA?usp=sharing)
  

## Final deliverables

### Project overview
PALTUS is an AI-powered self-learning platform designed to change the way of personalized education. The platform addresses key challenges in modern e-learning by providing:

- Adaptive Learning: AI-driven personalization that adjusts content and pace based on user choices and preferences.
- Flexible Course Creation: Intuitive tools for educators and users to build, modify, and delete custom courses.
- Gamification: Reward systems, achievements, and daily streaks to maintain motivation and track progress.
- Knowledge Review Tools: Repetition and quizzes to enhance long-term retention of learned material.

By combining AI-powered recommendations with user-aimed design, PALTUS creates a learning experience that adapts to individual needs while keeping users engaged through interactive and gamified elements.
### Features
- Authorization
- Registration
- Add course
- Edit course
- Delete course
- Mark subtopics as done/undone
- Progress bar for course completion
- Add notes for subtopics
- Interaction with AI-model for questions and misundrstandings
- Learnt material revise through quizzes
- User experience level via achievements
- Awards for completing challenges
### Tech stack
**Frontend**

- Vue.js: Reactive framework for building intuitive interfaces
- Pinia: To mantain a global state of a frontend app
- Axios: For HTTP requests

**Backend**

- Spring Boot: Robust backend framework for RESTful APIs
- PostgreSQL: Relational database for structured data storage
### Setup instructions
Run project via `docker compose --profile front-dev up`. You should get [GigaChat API key](https://developers.sber.ru/portal/gigachat-and-api) to run the application. See [.env.example](https://github.com/IU-Capstone-Project-2025/PALTUS/tree/main/.env.example) for configuration.

## Presentation draft

[Google Presentation](https://docs.google.com/presentation/d/1lrC7sYqLeRxuk9y8BXHxn9HLMQ02L2u9C7xS4bjsmcU/edit?usp=sharing)

## Weekly commitments

### Individual contribution of each participant

- Sergey Knyazkin
  - [Added chat interaction inside the lesson](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/9cd3840af830e49dcf6965eb5afd0723a54de098)
  - [Added quizzes](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/aaaecb7161e1f6a3a343d6b1261cbb3ea094bf26)
  - [Configured nginx for build version of frontend](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/bef3dfa67b6538eb760132294d46d8bcc8ff7828)
  - [Fixed bugs](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/9ad8177251a6b4068a9156674820555c231117f8)
- Ramazan Gizamov
  - Design finished - [Figma](https://www.figma.com/proto/rvNoC6oOC2Xe5y7yWIhLuN/Demo-visuals?node-id=0-1&t=DavTpLzLzLBFOWSe-1).
  - [Report for week 5](https://github.com/poeticlama/PALTUS/new/master/content/docs/2025/PALTUS/week5.md).
  - [Google Presentation](https://docs.google.com/presentation/d/1lrC7sYqLeRxuk9y8BXHxn9HLMQ02L2u9C7xS4bjsmcU/edit?usp=sharing).
- Aidar Sarvartdinov
  - [Added gamification features](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/4bc7b5cf26ab5319737d7662a2aaf55ad0d94446)
  - [Configured library for backend docs](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/6a2a092124026798261dd7e88b64b499084dc942)
- Igor Dubrovsky
  - [Configured library for fixing bad LLM responses](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/182c683ce51d310aecd854166bd3f083d897c8f7)
  - [Quiz functionality for backend](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/add999bb7f44ecc903529df3162b2a9a01e4c8a9)
  - [Fixed bugs](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/d4decc594ae5f05af518ec783bce3eb6ac10c39c)
- Amir Fayzullin
  - [Fix overall documentation](https://github.com/IU-Capstone-Project-2025/PALTUS/commit/976fcc9a0e8432b4d231d39181180677924666b0)
  - Balanced gamification features

## Plan for Next Week

- Code cleaning
- Fix bugs
- Finish presentation
- Add adaptive layouts

## Confirmation of the code’s operability

We confirm that the code in the main branch:
Run via docker-compose.
