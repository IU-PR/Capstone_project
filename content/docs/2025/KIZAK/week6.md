---
title: "Week #6"
---

# **Week #6**

## 🌐 **Links**

- **Deployment**:
  - [kizak.ru](https://kizak.ru/)
- **API Docs**:
  - While deployed **SwaggerAPI** docs could be accesed at [localhost:8000/docs](http://localhost:8000/docs)
  - **Simple** documentation could be accessed [here](https://github.com/IU-Capstone-Project-2025/KIZAK/tree/main/docs)
- **Design**:
  - Our design could be found on [figma](https://www.figma.com/design/Ew8Vmgzn739HYN2aAaVb1s/Untitled?node-id=0-1&t=PmAtopxNZMf728gX-1)
- **Demo**:
  - [Here](https://youtu.be/OahfLI8mL7E) you can find demo video of our project
- **GitHub Repository**:
  - [Here](https://github.com/IU-Capstone-Project-2025/KIZAK) you can find all source codes
- **Kanban Board**:
  - [Here](https://github.com/orgs/IU-Capstone-Project-2025/projects/11) you can find our backlog with all tasks
- **Final Presentation Preview**:
  - [Here](https://docs.google.com/presentation/d/1f-YpWAxS1KFvssm4z3-SoOicyxynLU4HUSK-ntVu4fI/edit?usp=sharing) you can find our final presentaion
- **Final Presentation Plan**:
  - [Here](https://docs.google.com/document/d/1hR4DLrVlalvpKOJ_cdbv7ykV1taozR3tFScrN3r3x8Y/edit?usp=sharing) you can find our script

## 🏁 **Final deliverables**

### 🔎 **Project overview**

**KIZAK** is an AI-powered learning assistant designed to guide users through their journey in the IT field. It builds **personalized learning paths**, recommends daily and weekly tasks, and supports users  while keeping track of their skills and progress.

### 🚀 **Features**

- **Onboarding:** Personalized user profile creation with topic selection and skill assessment  
- **Personal Recommendations:** Daily/weekly curated courses and tasks from platforms like Coursera, Stepik or EDX
- **Personal Roadmaps** generated specially for each user
  
### 🛠️ **Tech Stack**  

### **Backend**  
- **FastAPI**  🐍  - A **lightweight** Python web framework for building scalable APIs and backend services.
- **PostgreSQL** 🐘 - A **powerful**, open-source relational database with strong extensibility and SQL compliance.

### **Frontend**  
- **React** ⚛️ - **Fast and popular** JavaScript library for building dynamic, component-based user interfaces.
- **Next.js** ▲ - React framework for **server-side renderin**g, static sites, and **scalable web apps**.
- **Tailwind CSS** 🎨 - Utility-first CSS framework for **rapid UI development** with minimal custom CSS.
- **Redux** 🔄 - **State management** library for predictable global state in JavaScript apps.

### **ML / AI**  
- **Transformers** 🤗 - Hugging Face’s library for state-of-the-art NLP models

### ⚡ **Setup instructions**

#### Requirements

**To run this project make sure that your docker-compose version is 2.24.0 or higher**
```
docker-compose -v
# Docker Compose version v2.24.0-desktop.1
```
**Note that your locally deployed database will not have any data. You can run [db_populate](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/db/db_populate.py) script that will fill up data with our courses**

**In case if you used our application, make sure that your DB have an actual schema. To update schema, delete db/pg_data folder**

#### Deploy

First, clone the project:

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

QD_API_KEY=1234apikey
QD_URL=url

# CORS configuration
CORS_ORIGINS=http://localhost

# API configuration
API_HOST=backend
API_PORT=8000

# Frontend configuration
FRONTEND_HOST=frontend
FRONTEND_PORT=3000
FRONTEND_HOST_PORT=3000

SECRET_KEY=ApplicationSecretKey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

MAIL_USERNAME=kizak.inno
MAIL_PASSWORD=qhdz uxqj wxuf ubkp
MAIL_FROM=kizak.inno@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_FROM_NAME=KIZAK Team

DOMAIN=localhost:8000
```

Also create _.env.local_ in front folder:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Then build and run the project using Docker Compose:

```bash
docker-compose up --build
```

Visit [localhost:8000/docs](http://localhost:8000/docs) to access KIZAK API docs or [localhost:3000](http://localhost:3000) to see front part

## Presentation draft

Our oresentation draft can be found [here](https://docs.google.com/presentation/d/1f-YpWAxS1KFvssm4z3-SoOicyxynLU4HUSK-ntVu4fI/edit?usp=sharing)

[Here](https://docs.google.com/document/d/1hR4DLrVlalvpKOJ_cdbv7ykV1taozR3tFScrN3r3x8Y/edit?usp=sharing) you can find our script

# 📝 **Weekly commitments**

## 📊 **Individual contribution of each participant**

* **Marsel Berheev:** m.berheev@innopolis.university
  * Report
  * Feedback support (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/111))
  * Added ml microservice (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/109))

* **Maksim Malov:** m.malov@innopolis.university
  * Tests update (see [pull requests](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/117))
  * Mali auth support (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/115))
  * Code refactor

* **Makar Egorov:** m.egorov@innopolis.university
  * Automatic course scrapper service (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/98))

* **Timur Farizunov:** t.farizunov@innopolis.university 
  * Fronted bugs fixes (see [pull requests](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/103))

* **Sarmat Lutfullin:** s.lutfullin@innopolis.university
  * Mail support (see [pull requets](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/116))
 
* **Ulyana Chaikovskaya:** u.chaikouskaya@innopolis.university
  * Course normalisation (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/96))

* **Kseniia Khudiakova:** k.khudiakova@innopolis.university
  * Feedback support (see [commit](https://github.com/IU-Capstone-Project-2025/KIZAK/commit/cc28342f94c0dbb059f6381e164423f8f934fd12))

## 🎯 **Plan for Next Week**

* Finilaze dataset
* Bug fixes
* Documentation finalization
  
## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
