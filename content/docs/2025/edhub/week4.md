# EdHub Week 4 Report

<aside>

Capstone Project course

Innopolis University

July 2025

</aside>

# CI/CD Setup

## Continuous Integration

We have developed integration tests (`/backend/curltests.sh`) that will allow us to make sure that the new version works when new features are added. The specific tests are:

- Registering users;
- Logging in as Alice;
- Creating a course;
- Getting available courses;
- Getting course info;
- Inviting student to course;
- Getting enrolled students;
- Inviting parent to student;
- Getting student's parents;
- Inviting second teacher;
- Getting course teachers;
- Creating material;
- Getting course feed;
- Getting material;
- Creating assignment;
- Getting assignment info;
- Submitting assignment;
- Grading assignment.

We also configured a worker instance on the Innopolis University Virtual Machine, which run the tests every time when push or pull request to the `dev` and `main` branches happen. Moreover, it is impossible to merge a pull request into `main` branch without passing all the tests even if the code is successfully reviewed. You can see the example of automatic testing logs [*here*](https://github.com/IU-Capstone-Project-2025/edhub/actions/runs/16027449789/job/45218962473).

## Continuous Delivery

### Staging Environment
- привязана к деву
- на той же инновской машине
- ручная тестировка

### Production Environment
- берется из мейна
- хостинг timeweb.cloud в России
- привязали домен edhub.space
- сертификат от Let's Encrypt

# Weekly achievements

## Management

- закинули опрос челикам из пума
- договорились с директором о тестировании едхаба в пуме осенью

## Backend

- переписали фичу с ассайментами, теперь готово 

## Frontend

на Тимура

## DevOps

прописано выше в CI/CD Setup

## Plan for the Week 4

During week 4, we plan to continue developing our project as follows:
- the backend team plans to ;
- the frontend team plans to ;
- the devops team plans to .

# Individual contribution

### Gleb Popov
- [`management`]: запустил опрос в пум
- [`management`]: договорился с аветисом по поводу тестирования
- [`backend`]: прописал фичу с аттачментами ([*PR #63*](https://github.com/IU-Capstone-Project-2025/edhub/pull/63))

### Timur Usmanov
- [`devops`]: настроил сервера

### Askar Dinikeev
- [`devops`]: настроил CI ([*PR #65*](https://github.com/IU-Capstone-Project-2025/edhub/pull/65))
- [`devops`]: настроил деплой стейджинг сервера (https://github.com/IU-Capstone-Project-2025/edhub/pull/66/files)
- [`devops`]: настроил деплой продакшен сервера (https://github.com/IU-Capstone-Project-2025/edhub/pull/67)
- [`backend`]: добавил логи для аттачментов

### Alina Suhoverkova
- [`frontend`]: 

### Timur Struchkov
- [`frontend`]: 

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

We confirm that the code in the main branch:

- Is in working condition;
- Is runnable via `docker compose`.