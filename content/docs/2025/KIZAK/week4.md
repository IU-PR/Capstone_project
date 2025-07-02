---
title: "Week #4"
---

# **Week #4**

## 👨‍🔬 **Testing and QA**

Our API endpoints were tested with use of **pytest**. You can see test coverage in our github.com/IU-Capstone-Project-2025/KIZAK/blob/main/README.md. All tests could be found [here](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/README.md)

### Evidence of test execution

*Screenshots of test reports, CI logs, code coverage report.*

## ♾️ **CI/CD**

* Continuous Integration
  * Typos check (see workflow)
  * Backend liniting check (see workflow)
  * Frontend liniting check (see workflow)
  * Testing (see workflow)
  * Health check (see workflow)
* Continuous Delivery
  * Deploy on VDS (see workflow)

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

## Vibe Check

*Facilitate a team health check. Discuss progress, roadblocks, and team dynamics. Ensure everyone feels heard.*

# Weekly commitments

## Individual contribution of each participant

*...*

## Plan for Next Week

*...*

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
