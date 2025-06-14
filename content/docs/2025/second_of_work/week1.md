# Capstone Project Report – GymGenius

## 1. Team Members & Assigned Roles

| Name | Role | Responsibilities |
| --- | --- | --- |
| Ivan Chabanov | Team Leader · Mobile Dev | Define product vision; manage agile flow; implement Flutter app |
| Egor Dushin | Front-End Dev (Vue) | Build Vue admin UI; design UX; maintain component library |
| Kirill Nosov | Back-End Dev (Python · FastAPI) | Design admin API; integrate with Go core; ensure tests |
| Vlad Kuznetsov | DevOps & Go Dev | Containerisation; IaC; monitoring; author high-load Go services |
| Alexander Mikhailov | Back-End & ML Eng. | Create AI services; integrate OpenAI; develop analytics micro-service |

---

## 2. Project Overview

### 2.1 Idea
GymGenius is a smart workout tracker that combines intuitive logging with AI-powered feedback, giving gym-goers data-driven insights normally available only through a personal trainer.

### 2.2 Problem Statement
Athletes often track workouts in spreadsheets or basic apps that lack meaningful analytics. Personal trainers offer insight but are expensive and time-bound.

### 2.3 Target Users
- Self-coached enthusiasts seeking actionable metrics  
- Beginners needing affordable guidance  
- Coaches wanting a quick overview of clients’ progress  

---

## 3. High-Level User Stories (MVP)

| ID   | User Story                                   | Acceptance Criterion                                               |
| ---  | ---                                          | ---                                                                |
| US-1 | Sign up and set goals                        | Goals stored in DB after email/social sign-up                      |
| US-2 | Log workouts in under 30 s                   | Exercise autocomplete; works offline                               |
| US-3 | Receive AI insights post-workout             | Insight card appears within 5 s of sync                            |
| US-4 | View trend charts (volume / intensity / 1RM) | Charts refresh immediately on data change                          |
| US-5 | Sync with Apple Health / Google Fit          | OAuth in one tap; daily background sync                            |
| US-6 | Admin CRUD catalogue & model params          | Protected Vue panel with FastAPI endpoints                         |
| US-7 | One-command deployment                       | `docker compose up` boots complete stack                           |

**MVP Scope (12 weeks)**  
- **Mobile:** US-1, US-2, US-4  
- **AI:** US-3 (text insight stub), US-5 (form feedback PoC)  
- **Sync:** partial US-6 (Google Fit)  
- **Backend:** exercise catalogue, auth, analytics endpoints  
- **Admin:** Vue CRUD screens (US-6) on FastAPI backend  
- **DevOps:** CI/CD & one-click deployment (US-7)  

---

## 4. Code Repository

<https://github.com/IU-Capstone-Project-2025/gym-genius>

Contains runnable boilerplate (Flutter app, Go API, Vue admin, FastAPI admin backend, Docker Compose).

---

## 5. Tech Stack

| Layer   | Tech                                                                    |
| ---     | ---                                                                     |
| Mobile  | Flutter 3.22 / Dart 3 · Bloc · SQLite                                   |
| Core API| Go 1.22 · Gin · gRPC-Gateway · PostgreSQL 14+                           |
| Admin FE| Vue 3 (Vite) · TypeScript 5 · Pinia · shadcn/ui                         |
| Admin BE| Python 3.12 · FastAPI · SQLAlchemy                                      |
| AI Svcs | OpenAI API · Go concurrency workers                                     |
| DevOps  | Docker-Compose · GitHub Actions CI · Terraform (Linode)                 |

---