---
title: "Week #1"
---

# Week #1

## Project description

### Project name: Smartify

**Code repository**: https://github.com/IU-Capstone-Project-2025/Smartify

### Problem Statement:

Russian schoolchildren in grades 9-11 face a number of difficulties in planning their educational and professional path:

- Disparate services: career guidance, university selection, preparation for the Unified State Exam and the search for tutors — all on different platforms.
- Generalized tips: recommendations without taking into account the interests, strengths, and goals of a particular student.
- Difficulties in preparation: it is unclear which subjects to take, how much to study, where to seek help.
- Unavailability of quality support: it is difficult to find understandable and free resources.

### Project description:

Smartify - an all-in-one educational platform that helps Russian high school students (grades 9–11) navigate their career path, choose the right university, prepare for the Unified State Exam (ЕГЭ), and find suitable tutors.
The key feature is AI-based personalized recommendations that make the journey clear and accessible for every student.

Key Advantages

- **All-in-one solution** — no need to juggle multiple websites and tools  
- **Personalized guidance** — specific career suggestions, not just general directions  
- **Accessible and clear** — recommendations based on student interests, scores, and goals  

Career Guidance Module

- Interactive questionnaire covering interests, school performance, and hobbies  
- AI-powered analysis suggests **specific careers** (e.g., _pediatric surgeon_ instead of just _medic_)  
- Shows required subjects for admission right away  
- Includes reasoning behind the career choice to help students understand the fit

University Selection Module

- Filter universities by region, tuition (budget/paid), and field of study  
- Compare universities by:
  - Entrance scores
  - Education costs
  - National rankings

Exam Preparation Module

- Based on the chosen career and university, recommends:
  - Required subjects
  - Weekly study plan (hours per subject)
- Built-in mini-tests to assess current knowledge  
- Progress tracker to monitor preparation

Tutors & Mentors Module

- Find tutors using flexible filters:
  - Subject
  - Teaching style (e.g., friendly, strict, structured)
- Browse detailed tutor profiles, including:
  - Background and experience
  - University they attended

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| Andruwenko Valery     | @valery2005and | v.andruwenko@innopolis.university | ML developer | ML models,  |
| Chugaeva Mariia            | @mariiachugaeva | m.chugaeva@innopolis.university | ML developer | ML models, |
| Basanov Maxim            | @scruffyscarf | m.basanov@innopolis.university | Project Manager | Team coordination, Documentation responsible |
| Kuchukbaeva Regina            | The Grand Architecton | r.kuchukbaeva@innopolis.university | Frontend developer, Designer | Figma design,  |
| Zakirov Karim            | @karimzakirov | k.zakirov@innopolis.university | Frontend developer | [Responsibilities] |
| Mayorov Daniil | @Daniil20xx | d.mayorov@innopolis.university | Backend developer | [Responsibilities] |
| Antipov Alexey | @Aleksey_Antipov1725 | a.antipov@innopolis.university | Backend developer | [Responsibilities] |


## Brainstorming

### Ideas during brainstorming

1. Smartify - an all-in-one educational platform that helps Russian high school students (grades 9–11) navigate their career path, choose the right university, prepare for the Unified State Exam (ЕГЭ), and find suitable tutors.
2. Skill Development Planner - the user enters the desired goal (for example, to become a frontend developer), and receives a plan of courses, books, and projects with progress tracking.
3. Training in household skills - a learning about "life" in an interactive form: from taxes and cooking to renting a home. Courses from real people with interactive tasks and tests.
   
### Brief market research / problem validation

1. Yandex.Textbook — a platform for a preparation to Unified State Exam in computer science. It offers tasks and a built‑in AI-assistant to explain solutions to computer science problems.

Pros:
- A real AI assistant for specific tasks.
- Free access and support the probes.

Cons:
- Limited to computer science — there is no career or university direction.
- There is no comprehensive personalization for a profile or university.

2. Roadmap.sh - a platform for a development plan with detailed roadmaps for a variety of IT areas.

Pros:
- Detailed roadmaps for a variety of IT areas (frontend, backend, DevOps, etc.)
- Visual development schemes

Cons:
- There is no progress tracking
- There is no personalization for the current level of knowledge

## Basic requirements

### Target users and their primary needs

1. High School Students
- To understand which profession is suitable for them, taking into account their interests, grades and inclinations
- Get specific admission recommendations (what to take, where to enroll)
- Prepare for the Unified State Exam efficiently and according to plan
- Find trusted tutors or mentors

2. Parents of High Schoolers

- To help a child choose a future profession
- Monitor progress in preparation for the Unified State Exam
- Find affordable and high-quality educational resources or tutors

3. Tutors and Mentors

- Find interested students
- Get a platform to promote your services
- Adjust the filtering to suit your teaching style and subject

### User stories

1. As a high school student, I want to take a career orientation quiz, so that I can understand which profession fits me best.

2. As a student with a limited budget, I want to filter universities by location, tuition, and entrance scores, so that I can apply where I have the best chances.

3. As a student preparing for exams, I want to get a study plan and take mini-quizzes, so that I can track my progress and focus on weak areas.

4. As a student struggling with a some subject, I want to find a tutor whose teaching style fits me, so that learning becomes easier and more effective.

5. As a tutor, I want to create a profile with my experience, subjects, and availability, so that students can easily find and contact me.

### Initial scope

*...*

## Tech-stack

1. ML - Python, sklearn, pandas, matplotlib
   - Python + sklearn for fast development and training of ML models.
   - pandas for working with data.
   - matplotlib for visualization.

2. Frontend - Flutter
   - Flutter for a development the app due to its cross-platform nature, which allows us to create apps for iOS and Android with a single codebase. Flutter provides high performance and smooth interface, as well as offers design flexibility through a variety of widgets.

3. Backend - Python, Go, MongoDB, PostgreSQL
   - Python for the server side of the code, as it is optimal for working with databases and ML models. He also already has experience working with various protocols, databases and ML, gained in the 2nd year of the 2nd semester.
   - Go for the user-side backend because it is integrated with flutter.
   - MongoDB for storing information about universities, professions, and tests
   - Postgresql for storing user information because it is optimal for working with vectors

4. Design - Figma
   - Figma for easy and convenient operation with each component of design

# Weekly commitments

## Individual contribution of each participant

**Andruwenko Valery** – 

**Chugaeva Mariia** – 

**Basanov Maxim** – 

**Kuchukbaeva Regina** – 

**Zakirov Karim** – 

**Mayorov Daniil** - 

**Antipov Alexey** - 

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
