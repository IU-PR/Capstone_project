# Week #1

## Project description

### Project name: Fluently

**Code repository**: [https://github.com/IU-Capstone-Project-2025/Fluently](https://github.com/IU-Capstone-Project-2025/Fluently)

_This project will provide users rich ecosystem with ability to learn spoken english to become fluent. It will include mobile(both, ios and android) application, telegram bot and web extension. Application will consists of words learning via short pick options tests; have realistic conversations with AI assistant on relevant user-specific topics. It will have very flexible user experience customization. User can set goal, available hours, duration of lessons, level of difficulty. Telegram bot will provide short tests with picking from several options for fast and effective learning new words. Web extension will help you to save any interesting words you want to learn to user personal collection. This collection will have highest priority when words to learn will be suggested_

#### Problem Statement

There is no effective `fluent` English teaching application.

### Team Members

### Team Responsibilities

| Team Member                  | Role                      | Responsibilities                                                                                                                                                                 |
| ---------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Danila Kochegarov** (Lead) | Go Backend (Lead)         | - Lead backend development <br> - Design core architecture in Go <br> - Ensure code quality & reviews <br> - Coordinate cross-team collaboration <br> - Mentor junior developers |
| **Savva Ponomarev**          | iOS Dev & Project Manager | - Develop iOS app <br> - Manage timelines & tasks <br> - Facilitate meetings & communication <br> - Handle documentation & reporting                                             |
| **George Selivanov**         | System Analytics          | - Data collecting, preparation and analysis <br> - Product analytics and AB testing <br> - Competitors analytics <br> - Data Reverse Engineering                                 |
| **Anton Korotkov**           | ML Engineer               | - Develop/train ML models <br> - Integrate models with backend <br> - Optimize model performance <br> - Manage data pipelines                                                    |
| **Timofey Ivlev**            | DevOps Engineer           | - Set up CI/CD pipelines <br> - Manage cloud infrastructure <br> - Implement monitoring/logging <br> - Automate deployments & scaling                                            |
| **Daniil Tskhe**             | Go Backend Developer      | - Implement APIs & features <br> - Write tests & debug issues <br> - Optimize databases/caching <br> - Assist in architecture decisions                                          |
| **Evgeniy Bortsov**          | Android Developer         | - Develop Android app <br> - Ensure UI/UX performance <br> - Integrate backend APIs <br> - Collaborate with iOS team                                                             |

## Brainstorming

### Ideas during brainstorming

**1. Real-Time Cross-Platform Fitness Tracker**

_A mobile app (iOS/Android) with a Go backend that syncs workouts, nutrition, and health stats in real time. Includes AI-driven insights ("You burned 20% fewer calories today") and DevOps-automated scaling. Perfect for fitness enthusiasts who want data-driven progress tracking._

**2. Smart Home Hub with Anomaly Detection**

_A mobile-controlled smart home system (lights, thermostat) with AI-powered alerts for weird behavior ("Your fridge is using too much power!"). Uses Go for high-speed device communication and DevOps (Terraform/Grafana) for secure deployment. Ideal for IoT + security nerds._

**3. Decentralized Encrypted File Storage**

_A peer-to-peer Dropbox alternative where files sync across devices without central servers. Built with Go’s libp2p for networking, AES-256 encryption, and DevOps automation for node health checks. For privacy-focused users tired of Big Tech cloud storage._

### Brief market research / problem validation

**Wordich** - The service delivers short, daily lessons via a Telegram bot, utilizing spaced repetition based on the Ebbinghaus forgetting curve to maximize retention, and is suitable for users from beginner to advanced levels (A1–C2)

**Duolingo** - Duolingo is a global leader in language learning apps, featuring over 100 courses in 41 languages, and is known for its gamified, bite-sized lessons that make language acquisition accessible and engaging for millions of users

## Basic requirements

### Target users

**English Proficiency Level**

A2-B1 (Pre-Intermediate to Intermediate): Needs structured learning but can handle basic conversations.

B2-C1 (Upper-Intermediate to Advanced): Aims for fluency refinement (e.g., idioms, accents)

**Age**

14 - 50 years old

**Hobby**

- general spoken english learning
- travelling
- international shopping
- business
- IELTS
- IT

### Primary needs of Users

- Improve spoken english skills by use learned words in realistic, relevant, user-specific conversations with AI

- Be able to upgrade CEFR Level by learning user-specific unique lessons with simple and fast tests (pick options)

- Has the ability to eco-system on any device (ios/android/telegram) and in any place (across the web)

- Get personalized learning based on level, goals, and schedule

- Get updatable visual statistics of the learning process and see progress

- Ability to extend English vocabulary

### User stories

1. As a user, I want to take lessons with new words with simple and quick (pick options) tests, so that learn the most frequently used vocabulary

2. As a user, I want to be able to ask any english-related questions, so that I can quickly get relevant and useful information

3. As a user, I want to have classification of words by the difficulty level (A1 – C2) and by different topics, so that I can get relevant knowledge considering my level and goal

4. As a user, I want to receive notifications about lessons, so that I don't forget to practice

5. As a user, I want to have conversations with the AI, so that practice speaking skills

### Initial scope

_Remarks (for further understanding):_

**Full functionality** - AI assistant for personalized conversations in real-time, learning new words based on their level and goal with getting notifications based on the famous Ebbinghaus forgetting curve.

**Partial functionality** - lack of AI assistant, (further - same as in full functionality) learning new words based on their level and goal with getting notifications based on the famous Ebbinghaus forgetting curve.

**Web extension functionality** - save words to personal words collection for learning in Fluently ecosystem

- IOS application with _full functionality_
- Android application with _full functionality_
- Telegram bot with _partial functionality_
- Web extension with ecosystem synchronization and with _web extension functionality_

## Tech-stack

## Backend

- Golang (fast and secure)
- Chi (fast, not overloaded)
- Swagger (best for team communication about RestAPI)
- Air (hot-reload for faster development)
- Viper (easy and flexible configuration from any environment)
- GORM (auto migrations)
- Zap (fast and convenient logging)
- Postgres (reliable, support vectors)
- GoMock, testing (for integration and unit tests)
- Celery (Notifications system)

## Analytics

- requests, beautifulSoup4, lxml, selenium (parsing data from web pages)
- PyPDF2 (pdf parsing)
- pandas, numpy (data collecting, clearing and filtering)
- matplotlib, seaborn (plotting and analysis)
- NLTK (natural language analysis for context)
- google.genai (LLM prompts engineering)

## IOS

- Swift (Language for building native iOS applications)
- SwiftUI (UI for iOS application)
- Swift Concurrency (async/await, GCD) (for clean, performant asynchronous code)
- Combine (Reactive programming for state management and data flow)
- CoreData (Store user data on device)
- KeyChain (Store user credentials on device)
- URLSessions (for network layer)
- VIPER / MVVM (architecture pattern for flexible developping)
- XCTest (Unit/UI tests)

## Android

- Gradle (Build system)
- Kotlin (Language for building native android applications)
- Kotlin Coroutines (Kotlin's build-in support for asynchronous programming)
- Jetpack Compose (Modern UI toolkit recommended by Google)
- Room (SQLite-based local database)
- SharedPreferences (Simple local key-value storage for user's preferences)
- Retrofit/Okhttp (Libraries to perform network queries using http(s))

## ML

- Pytorch, tensorflow (neural networks creation and exploitation)
- sklearn (basic ML tools)
- pandas (data analysis and preprocessing)
- Probability and Statistics (data research)

## Telegram Bot

- Telebot.v3 (not deprecated library, all needed functionality)
- Redis (Store states in cache memory)

## Devops

- Docker, Docker-Compose (Containerization)
- Ansible (Deployment)
- Github Actions (CI/CD)
- Nginx (Load balancing)

<!-- ## _Something else you want to add_

_Feel free to add anything else that you consider important to your report_ -->

# Weekly commitments

## Individual contribution of each participant

## Individual Contributions

### Danila Kochegarov (Team Lead & Backend Developer)

- Proposed the original project idea
- Implemented boilerplate (architecture) of Telegram bot
- Overthink the User Flow, and design the UI
- Created boilerplate structure for the backend API
- Integrated Swagger documentation for the API
- Make some contribution on backend side (handlers and routers)
- Coordinated team workflow and technical decisions

### Savva Ponomarev (iOS Developer & Project Manager)

- Wrote project report
- Developed foundation of iOS application
- Created team schedule for organizing meetings
- Participated in UI/UX design process
- Managed project documentation and deadlines
- Facilitated team communication

### George Selivanov (System Analyst)

- Developed system for collecting and analyzing vocabulary from 111 themes using open sources (Gutenberg books)
- Created dataset of 1.35 million words with:
  - Complexity scores (0-100)
  - Theme classification
- Processed 1.4GB of text data with:
  - Automatic reading difficulty classification
  - Thematic categorization
- Designed data analysis pipelines

### Timofey Ivlev (DevOps Engineer)

- Created basic deployment workflow using GitHub Actions
- Developed Docker-compose configuration for backend
- Created Dockerfiles for:
  - Swagger documentation
  - Backend services
- Configured nginx server
- Deployed project Swagger at [https://swagger.fluently-app.ru](https://swagger.fluently-app.ru)
- Maintained infrastructure (Commit history: [GitHub](https://github.com/FluentlyOrg/Fluently-fork/tree/Dockerized-backend))

### Anton Korotkov (ML Engineer)

- Researched optimal AI model architecture
- Designed database schema for ML model storage
- Investigated model deployment strategies

### Daniil Tskhe (Backend Developer)

- Implemented API endpoints for all database models
- Developed CRUD operations for data access
- Assisted in backend architecture design
- Participated in API specification development

### Evgeniy Bortsov (Android Developer)

- Initialized Kotlin project for Android app
- Actively participated in UI/UX development

### Team Collaboration

All team members actively participated in:

- Brainstorming sessions for feature ideas
- Technical decision making
- Regular standup meetings
- Cross-functional problem solving

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
