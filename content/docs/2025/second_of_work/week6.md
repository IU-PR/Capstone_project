---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: 
admin panel: http://admin.xn--b1ab5acc.site
mobile app: will be deployed via TestFlight on Demo-Day and provide invitation access via QR-code.

- **API Docs**:
https://api.xn--b1ab5acc.site/swagger/index.html
- **Logs**:
http://grafana.xn--b1ab5acc.site
login -- password
admin -- capstone
http://grafana.xn--b1ab5acc.site/d/000000039/postgresql-database?orgId=1&refresh=10s

## Final deliverables

### Project overview

Our project is GymGenius.

There is a problem - people go to the gym, but do not have an easy way to track their progress and get a training to do. With the rolling out AI powers, new solutions might be implemented.

### Features

Project is divided into 2 parts:
Mobile app & Admin Panel

On mobile app:
1. Do a training via compact UI.
2. Track your workouts and analyze your activity via graph and other related-widgets.
3. Authenticate to synchronize your progress in cloud.

On Admin:
1. Admin authentication
2. User management (banning, subscription providing)
3. User's activity. User's database. Short user information.


### Tech stack

Mobile app:
Flutter application. Dio, Sqflite, Bloc

Admin panel:
Vue3, Nuxt3, Typescript, Pinia, NuxtUI, chartJS

Backend:
Go; Fiber v2 with Swagger docs; GORM + PostgreSQL for persistence, JWT + SHA-256 auth.

DevOps:


### Setup instructions

## Getting Started

### Mobile App

#### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your machine

#### Build and Run
```bash
# Build the Flutter web app
docker build -t gym-genius-mobile -f mobile/Dockerfile .

# Run the container
docker run -p 8080:80 gym-genius-mobile

# Access the app at http://localhost:8080
```
# Weekly commitments

## Individual contribution of each participant

Ivan Chabanov:
- Added backend to application: Auth and CRUDs
- Wired state managers and datasources.

Egor Dushin:
- Added backend for authentication, dashboard and statistics.

Kirill Nosov:
- Updated User schema to keep user stats
- Updated User creation to fill empty fields
- Added method to get user monthly stats
- Added static users and workouts initialization for DB
- Added in handlers checking for user role
- Added image loading for exercises from Minio

Vlad Kuznetsov:
- Add observability for postges (logs+metrics), data collected via promtail, saved to loki, and displayed in grafana

https://github.com/IU-Capstone-Project-2025/gym-genius/pull/37

Aleksandr Mihailov:
- Fixed database schemas (relationships between tables)
- Added responses models for better swagger docs
- Added loading of static exercises on backend start
- Added welcome page to the api
- Improved logging with new library and request id tracking, cleaned up production logs
- Added count users endpoint
- Added filtering by status, subscription plan, and subscription status options with query params in GET /users


## Plan for Next Week

Prepare demo, deploy to testflight.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
