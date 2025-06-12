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
| Andruwenko Valery     | @valery2005and | v.andruwenko@innopolis.university | ML developer, Data Analytic | ML models, Data collection |
| Chugaeva Mariia            | @mariiachugaeva | m.chugaeva@innopolis.university | Frontend developer, Data Analytic | App development, Data collection |
| Zakirov Karim            | @karimzakirov | k.zakirov@innopolis.university | Frontend developer | App development |
| Mayorov Daniil | @Daniil20xx | d.mayorov@innopolis.university | Backend developer | Backend development, Database interactions  |
| Antipov Alexey | @Aleksey_Antipov1725 | a.antipov@innopolis.university | Backend developer | Backend development, Database interactions |
| Kuchukbaeva Regina            | The Grand Architecton | r.kuchukbaeva@innopolis.university | UX/UI-Designer | Figma design  |
| Basanov Maxim            | @scruffyscarf | m.basanov@innopolis.university | Project Manager | Team coordination, Documentation responsible |

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

### MVP v0 (3 weeks)
The goal of MVP v0 is to create a working version of the platform in which the user can complete a questionnaire, see which professions might suit him, choose a university and get basic recommendations on the Unified State Exam.
**Basic functionality:**
1. Authentication and Profile
   - Register and log in using email and password.
   - Minimum personal account: name, class, region, average score.
2. Career guidance questionnaire (without AI)
   - A questionnaire with questions about interests, favorite subjects, and personality type.
   - After passing through, the user is shown 3-5 professions based on manual rules.
   - Each profession includes a description and a list of required exam subjects.
3. The University selection module
   - The user selects a region and a budget/contract.
   - The application displays a table of universities with scores, cost and referral.
   - So far, there is no comparison or analysis.
4. Preparation for the Unified State Exam
   - The necessary subjects are offered for the chosen profession.
   - Recommended number of hours per week.
   - A mini-test on one subject (5 questions) with an assessment of the level of knowledge.

What is not included:
- AI-profession recommendations
- Tutors and mentors
- Score forecast, progress tracker
- Chat, export to calendar

### MVP v1 (up to 7 weeks)
The goal of MVP v1 is to implement AI recommendations and bring the platform to a full—fledged product for schoolchildren.
What is being added:
1. Artificial intelligence
   - A trained ML model based on questionnaires.
   - Recommendations of professions with precise justification (for example, “pediatric surgeon" + why).
2. University Module — Advanced
   - Comparison of universities by scores, rating, and cost.
   - The ability to add to favorites.
3. Preparation for the Unified State Exam — tracker and forecast
   - Tracker of studied topics and hours.
   - Forecast of results for mini-tests.
   - Export the plan to Google Calendar.
4. The Tutors and Mentors module
   - Filters by subject, communication style.
   - Student and mentor cards (for example, “Nastya, MGU student, chemistry 95”).
5. Interface
   - Updated design.
   - Personal account with all modules and saved results.

## Tech-stack

1. ML - Python, sklearn, pandas, matplotlib
   - Python + sklearn for fast development and training of ML models.
   - pandas for working with data.
   - matplotlib for visualization.

2. Frontend - Flutter and its packets
   - Flutter for a development the app due to its cross-platform nature, which allows us to create apps for iOS and Android with a single codebase. Flutter provides high performance and smooth interface, as well as offers design flexibility through a variety of widgets.
   - dio – for sending requests to the REST API.
   - shared_preferences – for storing simple data (for example, tokens, settings).
   - flutter_secure_storage - a secure encrypted storage for confidential data.
   - hive - a fast local database for storing complex structures.
   - go_router – for a convenient navigation system between screens.
   - flutter_bloc – for managing the state of the application using the BLoC template.
   - riverpod - an alternative to BLoC, a flexible way to manage state.
   - flutter_screenutil – scaling the UI to fit different screen sizes.
   - web_socket_channel – for connection to WebSocket for real-time interaction.

3. Backend - Python, Go, MongoDB, PostgreSQL, psycopg2, SQLAlchemy, asyncpg, pymongo, grpsio, bcrypt, numpy
   - Python for the server side of the code, as it is optimal for working with databases and ML models. He also already has experience working with various protocols, databases and ML, gained in the 2nd year of the 2nd semester.
   - Go for the user-side backend because it is integrated with flutter.
   - MongoDB for storing information about universities, professions, and tests.
   - Postgresql for storing user information because it is optimal for working with vectors.
   - psycopg2 for connection to PostgreSQL.
   - SQLAlchemy for a convenient abstraction of working with a database.
   - asyncpg for asynchronous execution of database operations and query processing.
   - pymongo for work with MongoDB.
   - grpsio for interaction between services.
   - bcrypt for hashing and password verification.
   - numpy for numerical operations, working with vectors.

4. Design - Figma
   - Figma for easy and convenient operation with each component of design

# Weekly commitments

## Individual contribution of each participant

**Andruwenko Valery** – the architectural scheme of the career guidance system, the final version of the questionnaire (35+ questions) with blocks, generated synthetic questionnaires (40 lines) with signs and target professions, a separate dataset for training the MBTI model, studied and selected open datasets MBTI and Holland Code - https://github.com/IU-Capstone-Project-2025/Smartify/tree/main/ml

**Chugaeva Mariia** – logo app implementation and data base of university collection - https://github.com/IU-Capstone-Project-2025/Smartify/pull/4/commits

**Zakirov Karim** – the first page, which is displayed when the user log in to the system, implements a basic interface with a welcome message, registration page with a user data entry form - https://github.com/IU-Capstone-Project-2025/Smartify/pull/5/commits

**Mayorov Daniil** and **Antipov Alexey** - discussed how the architecture of the project will look in general, thought about which protocols to use to communicate between different parts of the project - created a picture of architecture, discussed the structure of the project - was created a new branch with folder structure - https://github.com/IU-Capstone-Project-2025/Smartify/pull/7/commits

**Kuchukbaeva Regina** – basic view of app implementation: drawed sign up, log in, password validation and forgot password algorithms - https://www.figma.com/design/kw2m1A0ArR9Tb4Obcb2FPx/Smartify?node-id=30-8511

**Basanov Maxim** – establishing communication between each participants at meetings and in the Telegram, emerging problem solving, GitHub repositories, Backlog and all documentation maintaining, this report writing - https://github.com/orgs/IU-Capstone-Project-2025/projects/2

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
