# Report 1. Foundation & Planning
# UrTraining

**Authors:** Ildar Rakiev, Makar Dyachenko, Salavat Faizullin, Egor Chernobrovkin, Alexandra Starikova, Ilona Dziurava, Anisya Kochetkova

**Date:** June 2025

# Team Members

| **Team Member**       | **Telegram**     | **Email Address**                     | **Role**            |
|-----------------------|------------------|---------------------------------------|---------------------|
| Ildar Rakiev (Lead)   | @mescudiway      | i.rakiev@innopolis.university         | Backend / Design    |
| Makar Dyachenko       | @index099        | m.dyachenko@innopolis.university      | Frontend / Design   |
| Salavat Faizullin     | @FSA_2005        | s.faizullin@innopolis.university      | Backend             |
| Egor Chernobrovkin    | @lolyhop         | e.chernobrovkin@innopolis.university  | ML                  |
| Alexandra Starikova   | @lexandrinnn_t   | a.nasibullina@innopolis.university    | ML                  |
| Ilona Dziurava        | @a_b_r_i_c_o_s   | il.dziurava@innopolis.university      | PM / Frontend       |
| Anisya Kochetkova     | @anis1305        | a.kochetkova@innopolis.university     | Backend             |

---

# 💡 Project Idea

## Problem Statement

Fitness and health are booming industries, but people are tired of one-size-fits-all solutions. They are looking for personalized guidance that adapts to their needs. At the same time, trainers want to share their knowledge but struggle to package it effectively or reach an audience online.

Moreover, the Internet is overflowing with conflicting advice from self-proclaimed experts, leaving people overwhelmed and confused. This overload of opinions creates paralysis, making it harder for individuals to take action or stick with a plan.

Meanwhile, trainers have valuable insights but lack the digital tools and strategies to grow their reputation and attract clients. Many great ideas get lost, helping no one. Our mission is to cut through the noise, make first steps easier for users, and help trainers connect with the people who need them most.

## Competitive Analysis

Competitors either provide pre-made workouts (with no real coach interaction), serve as promotional platforms (like Instagram* or YouTube), or simply function as marketplaces.

| **Platform**                | **Available Features**                      | **Missing / Pain Points**                                |
|-----------------------------|---------------------------------------------|----------------------------------------------------------|
| Fitify, Nike Training Club  | Ready-made plans, tracking                  | No live coaches, no adaptation to individual needs       |
| AllTrainer, Profi.ru        | Specialist search, personalized programs    | Few digital-first coaches, no quick monetization path    |
| Patreon / Boosty            | Subscriptions, private content              | No fitness-specific features, no user goal matching      | 
| Instagram*                  | Promotion and branding                      | Unstructured content, no real system                     |
| YouTube                     | Tons of free content                        | Hard to personalize, difficult to discover what fits you |

## Goal

The goal of our project is to simplify trainer-side workout plan uploads while automating user-side matching of optimal training programs.

## Solution

Our solution simplifies workout plan creation for trainers while using AI to match users with perfectly tailored programs. We combine live coaches, smart matching, fast knowledge integration, AI-powered tools, and - most importantly - effortless monetization. Trainers don’t need marketing skills to earn, and clients don’t need expertise to find value - our service handles the selection for them, ensuring they only get what works.

## Metrics of Success

To measure the success of our project, we would use the following metrics:

- **Feature Completion Rate** – Aim to implement 100% of the core features (MVP) defined in our project scope.
- **System Stability** – During testing, the system should run with zero critical bugs and less than 3 minor issues.
- **User Feedback Score** – From peer reviewers or instructors, we aim for an average satisfaction rating of 8 out of 10.
- **Task Success Rate** – At least 90% of test users should be able to complete key tasks without assistance (e.g., following a plan, navigating the UI).

Given the academic nature of the project, real-world adoption is out of scope for now, but these metrics allow us to evaluate the effectiveness and readiness of the system.

---

# 👥 Users

## Target Audience

| **Category**              | **Trainer (Coach)**                                                                                  | **Trainee (Client)**                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Goal**                  | - Share expertise with a wider audience<br>- Earn income from workout plans<br>- Build professional reputation | - Get fit with a personalized plan<br>- Stay consistent and motivated<br>- Avoid injury and confusion |
| **Main Problems**         | - Lacks technical skills to build structured online programs<br>- Struggles with promotion and audience reach<br>- Difficult to attract and retain clients | - Overwhelmed by conflicting advice<br>- Unsure what program fits their goals<br>- Lacks ongoing guidance and motivation |
| **Needs**                 | - Easy-to-use tool for program creation and sharing<br>- Built-in client discovery and matching<br>- Automated monetization options | - Clear and personalized fitness guidance<br>- Trusted and structured programs<br>- A simple way to get started |
| **How Our Platform Helps**| - Simplifies workout upload process<br>- Handles payments and monetization<br>- Uses AI for smart client matching<br>- Enables income without marketing efforts | - Matches users with the right trainer and program<br>- Removes guesswork and confusion<br>- Provides structured plans with real support |

## User Persona

### Trainer Persona – Alex, 32

Alex is a certified personal trainer with over 8 years of experience. He currently works freelance and has built a small following on social media, where he shares workout tips and motivational content. Despite his expertise, Alex struggles to scale his impact online. He lacks the time and technical skills to build structured digital programs or run marketing campaigns.

**Goals:**
- Share his knowledge with more people online
- Generate steady income from workout plans
- Build a stronger professional reputation

**Frustrations:**
- Too many disjointed tools for content creation and sales
- Difficulty reaching new clients online
- Time-consuming promotion efforts

**How our platform helps:** It enables Alex to easily create and share structured workout plans, automatically match with clients, and earn money without needing technical or marketing expertise.

---

### Trainee Persona – Daria, 27

Daria is a full-time marketing specialist who often feels overwhelmed by fitness advice online. She’s tried various workout apps and diets, but lacks consistency and often doubts whether she's following the right plan. Daria wants something simple, trustworthy, and adapted to her busy lifestyle.

**Goals:**
- Get fit using a plan that fits her personal schedule and needs
- Stay consistent with expert guidance
- Avoid injury and ineffective workouts

**Frustrations:**
- Conflicting fitness advice online
- Lack of motivation without structured support
- Difficulty choosing the right program

**How our platform helps:** It matches Daria with the right trainer and plan using AI, provides trusted and personalized guidance, and removes the guesswork so she can focus on progress.

## User Stories

1. **As a new user**, I want to register as either a trainer or a client so that I can access the features relevant to my role.
2. **As a client**, I want to fill out a profile questionnaire so that I can receive basic training recommendations tailored to my needs.
3. **As a trainer**, I want to easily create and upload workout programs so that I can share my expertise without needing technical skills.
4. **As a client**, I want to browse a catalog of training programs so that I can explore different options.

---

# Initial Scope (MVP)

### ✅ The following features will be included in the MVP:
- User registration for both trainers and clients.
- User profile questionnaire and basic workout recommendations based on input.
- Workout upload system for trainers (support for text, images, and PDFs).
- Content processing algorithm to structure uploaded workouts into standardized cards (with descriptions, structure, and tags).
- Basic recommendation system suggesting workouts based on user profiles.
- Training catalog as a scrollable feed of exercise cards.
- Purchase/save functionality for training programs.

### ❌ The following functionality is planned for future iterations but is excluded from the initial release:
- Effortless monetization of programs
- Video pages for trainers
- Real-time messaging/calls
- Mobile app (iOS/Android)
- Social/chat features
- Subscriptions
- Digital products (courses/guides)
- Ratings and reviews

---

# 🔗 Repository Link

https://github.com/IU-Capstone-Project-2025/UrTraining

---

# ⚙️ Tech Stack

## Frontend

- **React** – Primary framework for building dynamic user interfaces.
- **TailwindCSS** – Utility-first CSS framework for rapid styling.
- **shadcn/ui** – Customizable UI component libraries for consistent design.
- **Framer Motion** – Library for smooth animations and transitions.

## Backend

- **FastAPI** – High-performance Python framework to build APIs with automatic documentation (Swagger/OpenAPI).
- **PostgreSQL** – Relational database for structured data storage (user profiles, questionnaires).
- **SQLAlchemy** – ORM for Python to simplify database interactions.
- **Supabase (optional)** – Open-source Firebase alternative for authentication and storage.
- **Docker** – Containerization for consistent deployment across environments.
- **CI/CD (GitHub Actions)** – Automated testing and deployment pipelines.

## AI/ML

- **Sentence-BERT** – Pretrained embedding models for semantic search (initial phase, before fine-tuning).
- **HuggingFace Transformers** – Framework for leveraging LLM (e.g., fine-tuning or zero-shot tasks).
- **Faiss** – Efficient vector similarity search for recommendations.
- **EasyOCR / PaddleOCR** – Text extraction from images (e.g., scanned documents or screenshots).

## File Storage

- **Cloudinary / Supabase / AWS S3** – Scalable solutions for storing user-uploaded media (images, PDFs).

---

# Weekly Progress Report

During the first week, our team held several meetings to discuss the core idea of the project and define the roles and responsibilities of each team member. We established the initial scope of the project and agreed on the main technologies that will be used for development.

## Challenges & Solutions
The main challenge we faced was differing perspectives on the project details. To address this, we reached an agreement on the core functionality and defined clear, specific requirements. This ensured that all team members share a unified understanding of the project moving forward.

## Conclusions & Next Steps
During the first week, we made progress by defining the main goal of the project and outlining our future plans. In the upcoming week, our focus will shift to designing the project interface and beginning implementation based on the established backlog.
