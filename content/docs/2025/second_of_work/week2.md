---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

Mobile App
- **UseCases**: Start a workout. Dynamically change it during session. Save it locally in database.
- **AI**: See review of the workout. (Might be additions)
- **UI**: Pages and widgets related to workout session. Graphs for tracking progress (exercise analytics, workout calendar)
- **Datasources**: Prepopulated exercise information. Sql-based Database for local memory.
- **Design**: Following clean architectures principles
- **Backend**: For Synchronisation and AI endpoints usage.

Admin panel:
- **UseCases**: Admins see analytics in the app
- **What Exactly?**: Last Seen in Application; How often is usage; What is user doing in app (and more).
- **UI**: Graphs, tables, logs
- **Backend**: Endpoints for collecting data.
- **DataSource**: Database for tracking UID of User with related data to it.

### Prioritized backlog

https://nodoser.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog
(Some tasks are omitted, for detailed contribution check weekly commits)

## Project specific progress

### Mobile App

- Workout-related data (pictures; json) was created.
- Model for exercise-information was designed. 
- Basic CI/CD (linting) was built and tested. 

### Main Backend (for mobile app)

- Based architecture was created (see more in personal contribution)

### Frontend (Admin Panel)

- UI based on static data was created (see more in personal contribution).

### Backend (Admin Panel)

- Based architecture was created (see more in personal contribution)

# Weekly commitments

## Individual contribution of each participant

**Ivan Chabanov**:
1) Build basic CI/CD pipeline (linting)

2) Implement model for exercise and generate a json of 30 exercises.

3) Find a model for picture gen (SORA). Generate most of gym exercise pictures.

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/7
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/8
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/9
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/10

**Vlad Kuznetsov**:

1. с нуля изучил голанг; роутер chi, орм gorm
2. описал базовую архитектуру приложения

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/5

**Egor Dushin**:
1) изучал документацию Nuxt 3

2) выбирал архитектурное решение - выбрал atomic design архитектуру из-за возможности быстрой навигации в компонентном дереве

3) Выбирал ui kit, остановился на Nuxt UI из-за его стабильности и лаконичности

4)  Выбирал стек для графиков, взял ChartJS, как самую популярную либу для графиков

5) Реализовал график активности пользователей с возможностью переключать интервал времени. На статических данных, естественно

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/6

**Kirill Nosov**

1) Создание структуры бекенда на админке
2) Подключение фреймворка для api (fiber)
3) Инициализация бд (подключение gorm)
4) Имплементация метода для получения и записи активности пользователей
5) Имплементация метода отправки активности пользователей для фронта (в процессе)

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/11

**Aleksandr Mihailov**

- Research Go docs
- Research Fiber, Gorm libraries for backend
- Decided whether to use cloud-based AI models or lightweight local ones.
- Researched a cloud-based AI models services and pick model for application
- Thought of where to use AI solutions in Mobile App

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/12

## Plan for Next Week

Continue working on our features. Some of the tasks can be seen in backlog already:
https://nodoser.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
