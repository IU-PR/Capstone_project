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

For automatic website deployment we configured two environments: **Staging Environment** for developers to test new versions of the application and **Production Environment** for customers to use the service.

+------------+-----------------+---------------+--------------+---------------------+---------------+-----------------+
| Deployment | Machine Type    | Provider      | OS           | Network             | SSH Access    | SSH Key Holders |
+------------+-----------------+---------------+--------------+---------------------+---------------+-----------------+
| Staging    | Virtual Machine | Innopolis     | Ubuntu 22.04 | 10.90.138.154 on    | Password      | Timur Usmanov,  |
|            |                 | University    |              | University networks | and PublicKey | Askar Dinikeev, |
|            |                 |               |              |                     |               | Gleb Popov      |
+------------+-----------------+---------------+--------------+---------------------+---------------+-----------------+
| Production | Virtual         | timeweb.cloud | Ubuntu 24.04 | edhub.space,        | PublicKey     | Timur Usmanov,  |
|            | Dedicated       |               |              | 82.97.249.54        |               | Askar Dinikeev, |
|            | Server          |               |              | (public IP)         |               | Gleb Popov      |
+------------+-----------------+---------------+--------------+---------------------+---------------+-----------------+


### Staging Environment
Staging Environment runs a version of the site on the `dev` branch on the Innopolis University Virtual Machine. We as a development team can open the site and manually test the developed innovations before merging it into the `main` branch.

### Production Environment
Production Environment runs a version of the site on the `main` branch on the globally accessible server. This version is tied to the public domain [*edhub.space*](www.edhub.space) and will be used by our customers.

We decided to use timeweb.cloud hosting because it is easy to set up, has suitable characteristics and provides servers in Russia.

We bought the domain edhub.space on REG.RU because it seemed to us the most suitable and memorable among all available domains. 

We bought the domain edhub.space on REG.RU because it seemed to us the most suitable and memorable among all available domains. We configured A-address forwarding (IPv4) and subdomain www.

To ensure a secure https connection, we configured a certificate from Let's Encrypt.

<!-- - берется из мейна
- хостинг timeweb.cloud в России
- привязали домен edhub.space
- сертификат от Let's Encrypt -->

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