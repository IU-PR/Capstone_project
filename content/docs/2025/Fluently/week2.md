---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

<!-- _This is your main task on this week, so please, make it detailed enough_ -->

This week’s primary focus was to develop a **low-fidelity wireframe** for the project’s frontend interface, analyze the structural design of databases, outline the **ML (Machine Learning)** core functionality, and map the **backend workflow**. Additionally, the task included analyzing and creating a user flow to ensure seamless navigation and usability.

### Prioritized backlog

<!-- *(Publicly accessible link OR screenshots OR table) of your prioritized backlog (Kanban board)* -->

The backlog link: [Backlog](https://github.com/orgs/FluentlyOrg/projects/2) \
As a Kanban board we create a [GitHub Project](https://github.com/orgs/FluentlyOrg/projects/2/views/2)

## Project specific progress

### Design

#### Low-Fidelity Wireframe Creation

Establish a foundational layout for user interfaces and workflows before committing to visual details.

Figma Prototype: Developed a [low-fidelity wireframe](https://www.figma.com/design/CcvdlGTayqnZPemfehfZjj/Fluently-Lofi?node-id=0-1&p=f&t=QIYBq4YclsutwNfQ-0) focusing on:

- Core Screens:
  - Login / Register,
  - Home screen
  - Settings / Profile
  - screens with other functional
    - Dictionary
    - Diary
    - Lesson screens
    - Statistic screen
    - Calendar screen

#### Visual Design & Theming

Define a comprehensive visual identity to enhance usability and brand alignment.

- [Design sketches](https://www.figma.com/design/fB7aZCbTyFek5OA1CTzJGw/Untitled?node-id=0-1&p=f&t=ILCjv8bIbJCePfVu-0) based on low-fidelity prototypes
- Color Theme: Selected a primary palette (Primary orange, white, and black, purple, blue as secondary colors)

### Data Analysis

#### Reverse Engineering & Functional Specification

Conducted reverse engineering of competitor platforms:

- **Platforms Studied:** Duolingo, Wordich, RE:Word, Babbel, Quizlet
- **Objective:** Systematically evaluate strengths to inform our feature prioritization.

#### Duolingo

- Typical exercises:

  - Filling in the correct word in a phrase
  - Text (dialogue), answering questions about it or filling in blanks
  - Listening to/reading a task and selecting/typing/voicing the answer
  - Constructing sentences from words

- Functional features:
  - Full sentence pronunciation with new words
  - Users can tap a word to see its translation and hear pronunciation
  - Rating and reward system

#### RE:Word

- Typical exercises:

  - Before starting, users see words with swipe options `<-- don't know> <know -->` to build a word base
  - Typing a specific word / selecting from options / seeing translation

- Functional features:
  - Words are added and categorized manually by users

#### Wordich

- Typical exercises:

  - User receives a spoken word, `English spelling - translation`, example sentence with the word and its translation
  - User listens to the word and types it
  - User receives a word and selects 1 of 4 translation options (English -> Russian and vice versa)

- Functional features:
  - All functionality is implemented through a Telegram bot that regularly sends notifications and reminders

#### Babbel

- Typical exercises:

  - Selecting picture-word flashcards
  - Filling words into dialogues

- Functional features:
  _none_

#### Quizlet

- Typical exercises:

  - Flashcard - translation, followed by memorization exercises

- Functional features:
  - Users can create their own flashcards and browse community cards

#### Database Engineering

Designed words Databse: [database schema](https://github.com/orgs/FluentlyOrg/projects/2/views/2?pane=issue&itemId=115467773&issue=FluentlyOrg%7CFluently-fork%7C49)

![Database](https://github.com/FluentlyOrg/Fluently-fork/blob/frontend/ios/report-imges/DB%20for%20Fluently.png)

[link to the DB](https://lucid.app/lucidchart/fc4d21dc-6250-46ea-8611-2b4b00ba26f2/edit?viewport_loc=-581%2C-496%2C1771%2C921%2C0_0&invitationId=inv_368c524a-14f2-4bd1-819f-068d8fefeebf)

### Frontend

- Planned user flow of application
- Understand common principles
- Started developing iOS and Android apps

### Backend

- Rethought the structure of authorization through Google (Rethought the fields for user and preferences models)
- Make full setup Google and email&password based authentication with JWT token generation
- Added an admin panel for CRUD database operations via a graphical interface
- The models in the code have been rewritten and new ones have been added with handlers of operations with them

### ML

#### Model Investigation & Selection

- Researched and evaluated multiple NLP architectures
- Selected BERT with MLM (Masked Language Modeling)
- Started developing of chosen model

### DevOps

### Updated README

**Changes Pushed to Main:**

- Added two installation guides:
  1. **Local Setup** (recommended for TA)
  2. **Full Deployment**

**Key Improvements:**

#### Local Setup Guide

- Designed specifically for tests of the system locally via `localhost`
- Includes:
  - One-command environment setup (Docker Compose)
  - Test data injection script
  - Health check endpoints for validation

#### Mobile Deployment

- **Android**
- **iOS**

#### Links

[Updated README](https://github.com/FluentlyOrg/Fluently-fork/issues/53) \
[Main site](https://fluently-app.ru) \
[Swagger (API documentation)](https://fluently-app.ru/swagger/index.html) \
[Admin Panel](https://admin.fluently-app.ru/admin/content/words)

# Weekly commitments

## Individual contribution of each participant

### Danila Kochegarov (Team Lead & Backend Developer)

- Rethought the structure of authorization through Google (Rethought the fields for user and preferences models)
- Organize work in the team (creating issues, communicate with each of the people on their topic, solve technical and theme, app logic issues)
- Populate database with 5950 words from Oxford dictionary (word, part of speech, CEFR level)
- Make full setup Google and email&password based authentication with JWT token generation

Issues links:

1. [User model revision](https://github.com/FluentlyOrg/Fluently-fork/issues/46)
2. [Populate DB](https://github.com/FluentlyOrg/Fluently-fork/issues/58)
3. [Google AUTH PR](https://github.com/FluentlyOrg/Fluently-fork/pull/55). \
   Related issues:

- [JWT](https://github.com/FluentlyOrg/Fluently-fork/issues/45)
- [Change psw](https://github.com/FluentlyOrg/Fluently-fork/issues/44)

### Savva Ponomarev (iOS Developer & Product Manager)

- Created backlog for a week
- Designed with Evgeniy low-fidelity design of the screens
- Made skethes for design app
- Set-up the iOS project structure, with fonts and colors
- Wrote a report
<!-- - Upadated README for iOS app -->
- Started Developing screens:
  - Home screen

link to [Backlog](https://github.com/orgs/FluentlyOrg/projects/2/views/1) \
links to issues: \
https://github.com/FluentlyOrg/Fluently-fork/issues/18 \
https://github.com/FluentlyOrg/Fluently-fork/issues/21 \
https://github.com/FluentlyOrg/Fluently-fork/issues/11

link to PR: \
[Home screen](https://github.com/FluentlyOrg/Fluently-fork/pull/59)

### George Selivanov (System Analyst)

- Conducted reverse engineering of competitor products to define core application functionality
- Collaboratively designed the database schema with Danya
- Researched and selected optimal data sources for parsing
- Mapped user flows based on competitive analysis findings

links to issues:

- [reverse engeniiring](https://github.com/orgs/FluentlyOrg/projects/2/views/6?sliceBy%5BcolumnId%5D=Assignees&filterQuery=&sliceBy%5Bvalue%5D=Ge-os&pane=issue&itemId=114967474&issue=FluentlyOrg%7CFluently-fork%7C15)
- [user model](https://github.com/orgs/FluentlyOrg/projects/2/views/6?sliceBy%5BcolumnId%5D=Assignees&filterQuery=&sliceBy%5Bvalue%5D=FunnyFoXD&pane=issue&itemId=115340899&issue=FluentlyOrg%7CFluently-fork%7C46)
- [words databse model](https://github.com/orgs/FluentlyOrg/projects/2/views/6?sliceBy%5BcolumnId%5D=Assignees&filterQuery=&sliceBy%5Bvalue%5D=FunnyFoXD&pane=issue&itemId=115467773&issue=FluentlyOrg%7CFluently-fork%7C49)

### Timofey Ivlev (DevOps Engineer)

Updated README
https://github.com/FluentlyOrg/Fluently-fork/issues/53

- Updated nginx.conf to new website structure
  Main site: https://fluently-app.ru
  Swagger (API documentation): https://fluently-app.ru/swagger/index.html

  Directus admin panel: https://admin.fluently-app.ru \

  https://github.com/FluentlyOrg/Fluently-fork/pull/50 \
  https://github.com/FluentlyOrg/Fluently-fork/issues/29

- Added Cloudflare CDN

### Anton Korotkov (ML Engineer)

- Researched and evaluated multiple NLP architectures
- Researched pre-tuned models capable of future fine-tuning
- Use BERT with MLM (Masked Language Modeling) concepts for:
  - Contextual understanding of word relationships
  - Native mask prediction capabilities
- Suggested to use WordNet and ConceptNet

### Daniil Tskhe (Backend Developer)

- Rethought the structure of authorization through Google
- I have linked an admin panel for interacting with the database through a graphical interface
- Rethought the fields for user and preferences models
- Changed user and preferences models in the code and added operations with them
- Added additional models and operations with them

Links to issues: \
https://github.com/FluentlyOrg/Fluently-fork/issues/26
https://github.com/FluentlyOrg/Fluently-fork/issues/37
https://github.com/FluentlyOrg/Fluently-fork/issues/46
https://github.com/FluentlyOrg/Fluently-fork/issues/47
https://github.com/FluentlyOrg/Fluently-fork/issues/49

### Evgeniy Bortsov (Android Developer)

- Made a Low-fidelity design for lesson part
- Set-up Android project sructure
- Created User flow diagram
  - [User flow](https://www.figma.com/board/J9LhwMVxXJT3lGmKAx2ej8/Untitled?node-id=0-1&p=f&t=kepRz1tknRgUh1Lh-0)

links to issues: \
https://github.com/FluentlyOrg/Fluently-fork/issues/16\
https://github.com/FluentlyOrg/Fluently-fork/issues/18#issuecomment-2980762714

## Plan for Next Week

### Design

- Finish UI design

### Frontend

- Create all key screens for both OS
  - iOS
  - Android
- Make navigation
- Network layer for working with API

### Backend

- configure authentication on swagger page
- make telegram bot to learn words and see some stats
- write tests for API
- check test coverage via SonarQube

### ML

- Develop smart system that will generate exercises for lessons

### Data Analysis

- Recollect datasets
- Parsing info from new sources

### DevOps

- configure SonarQube
- configure endpoint for SonarQube
- Set up Prometheus+Grafana for monitoring API load, security issues
- Set up Loki for logs aggregations
- Set up a second deploy server with domain for testing

## P.S.

[Acceptance criteria](https://miro.com/app/board/uXjVIsQXxms=/?share_link_id=729729910385)

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
