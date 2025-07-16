---
title: "Week #4"
---

# **Week #4**

## 👨‍🔬 **Testing and QA**

Our API endpoints were tested with use of **pytest**. You can see test coverage in our github.com/IU-Capstone-Project-2025/KIZAK/blob/main/README.md. All tests could be found [here](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/README.md)

### Evidence of test execution

We used **pytest** for unit testing testing of our application. [Here](https://github.com/IU-Capstone-Project-2025/KIZAK/tree/main/back/tests) you can find our tests

Our testing workflow could be found [here](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/.github/workflows/test.yml)

All testing logs could be found [here](https://github.com/IU-Capstone-Project-2025/KIZAK/actions/runs/16034374439/job/45242483159)

## ♾️ **CI/CD**

* Continuous Integration
  * Typos check (see [workflow](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/.github/workflows/typos.yml))
  * Backend liniting check (see [workflow](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/.github/workflows/pythonApplication.yml))
  * Testing (see [workflow](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/.github/workflows/pythonApplication.yml))
  * Health check (see [workflow](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/.github/workflows/docker-compose-check.yml))
* Continuous Delivery
  * Deploy on VDS (see [workflow](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/.github/workflows/deploy.yml))

### 🔗 **Links to CI/CD configuration files**

You can check all links in **CI/CD** section, or see [here](https://github.com/IU-Capstone-Project-2025/KIZAK/tree/main/.github/workflows)

## 🖥️ **Deployment**

### 📈 **Staging**

First, clone our project:

```bash
git clone https://github.com/IU-Capstone-Project-2025/KIZAK
cd KIZAK
```

Now set up _.env_ file:

```bash
# Database configuration
DB_HOST=db
DB_PORT=5432
DB_USER=user
DB_PASSWORD=password
DB_NAME=db

# CORS configuration
CORS_ORIGINS=http://localhost

# API configuration
API_HOST=backend
API_PORT=8000

# Frontend configuration
FRONTEND_HOST=frontend
FRONTEND_PORT=3000
FRONTEND_HOST_PORT=3000
```

Then build and run the project using Docker Compose:

```bash
docker-compose up --build
```

Visit [localhost:8000/docs](http://localhost:8000/docs) to access KIZAK API docs or [localhost:3000](http://localhost:3000) to see front part

### 🥒 **Production**

For production we used [TimeWeb](https://timeweb.cloud/) VDS server working on Ubuntu 22.04. To do so we followed the following steps:

* Setup SSL certificate
* Setup Nginx server for SSL and reverse proxy
* Setup PostgreSQL database
* Setup our project (back + front + ml)

Now you can visit our site at [kizak.ru](https://kizak.ru/)

## 😹 **Vibe Check**
* Almost all team members **satisfied** with our project proress
* Almost all core features are implemented in production

# 📝 **Weekly commitments**

## 📊 **Individual contribution of each participant**

* **Marsel Berheev:** m.berheev@innopolis.university
  * Weekly report
  * API Update (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/76))
  * Continuous Delivery (see [commit](https://github.com/IU-Capstone-Project-2025/KIZAK/commit/509e8b5bf0016ff9e86c152827dd99e8342966c9) or [workflow](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/.github/workflows/deploy.yml))

* **Maksim Malov:** m.malov@innopolis.university
  * Added API tests (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/75))
  * Code refactor

* **Makar Egorov:** m.egorov@innopolis.university
  * Added OAuth (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/72))

* **Timur Farizunov:** t.farizunov@innopolis.university
  * Frontend refinement (see [fixes](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/77))

* **Sarmat Lutfullin:** s.lutfullin@innopolis.university
  * Frontend refinement (see [fixes](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/77))
 
* **Ulyana Chaikovskaya:** u.chaikouskaya@innopolis.university
  * Vector search and recomendation ranking (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/78))

* **Kseniia Khudiakova:** k.khudiakova@innopolis.university
  * Vector search and recomendation ranking (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/78))

## 🎯 **Plan for Next Week**

* Add JWT
* Caching support
* Design update

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
