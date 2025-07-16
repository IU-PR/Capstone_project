---
title: "Week #6"
---

# **Week #6**

## Links

<!-- _Specify here all the necessary links to your website, application installer, final demo, etc._ -->

- **Deployment**: [fluently-app.ru](https://fluently-app.ru/)
- **API Docs**: [fluently-app.ru/swagger/ (Private)](https://fluently-app.ru/swagger/index.html)
- **Design**:
  - Lofi: [Figma-Lofi](https://www.figma.com/design/CcvdlGTayqnZPemfehfZjj/Fluently-Lofi?node-id=0-1&p=f&t=ge0Wpe0RCLRRmT72-0)
  - UI/UX: [Figma-UI/UX](https://www.figma.com/design/fB7aZCbTyFek5OA1CTzJGw/Untitled?node-id=0-1&p=f&t=LEFSUjFFhlMM0QNq-0)
- **Demo**: [folder with demos](https://github.com/FluentlyOrg/Fluently-fork/tree/main/report-imges/GIFs)
- LLMs API docs: https://fluently-app.ru/llm/docs
- Thersaurus API docs: https://fluently-app.ru/thesaurus/docs
- Ml API docs: https://fluently-app.ru/ml/docs

## Final deliverables

### Project overview

<!-- _Describe your project, what problems it solves and what key features it has (only those that are implemented)._ -->

Fluently is an innovative English learning application that creates personalized study programs based on user preferences and current knowledge level. The app features adaptive learning algorithms, interactive lessons, and progress tracking.

### Features

user Interface:

- iOS app
- Android app
- telegram bot

AI:

- BERT - Sorting and choosing most relevant words for exercises
- Thesaurus - Selecting most relevant words for user English level
- LLM - Gemeni and Groq for chat with ai (part of the lesson)
<!-- _List of all implemented features in your project._ -->

### Tech stack

**iOS:**

- SwiftUl - Ul
- VIPER - Architecture
- SwiftData - persistent storage
- KeyChain - storage of user secrets
- URLSession - Network Layer (request to API)
- async/await - concurency
- GoogleSignin - login by google

**Android:**

- Gradle (Build system)
- Kotlin (Language for building native android applications)
- Kotlin Coroutines (Kotlin's build-in support for asynchronous programming)
- Jetpack Compose (Modern UI toolkit recommended by Google)
- Room (SQLite-based local database)
- SharedPreferences (Simple local key-value storage for user's preferences)
- Retrofit/Okhttp (Libraries to perform network queries using http(s))
- Hilt (Dependency Injection)
- Kotlinx Serialization (Json serialization/deserialization)
- Coil (Library for image loading for Jetpack Compose)
- AppAuth (Library for OAuth flow)

**Backend:**

- Chi (Lightweight, idiomatic and composable router for building Go HTTP services)
- Cobra (Library for creating powerful modern CLI applications)
- Viper (Complete configuration solution for Go applications)
- Testify (Go code (golang) set of packages that provide many tools for testifying that your code will behave as you intend)
- Swaggo (Swag converts Go annotations to Swagger Documentation)
- Zap (It's 4-10x faster than other structured logging packages)
- GORM (The fantastic ORM library for Golang, aims to be developer friendly)
- Prometheus-client
- Nginx
- PostgreSQL
- Directus

**Telegram:**

- Telebot.v3 (Telebot is a bot framework for Telegram Bot API)
- Go-reddis (go-redis is the official Redis client library for the Go programming language)
- Asynq (Asynq is a Go library for queueing tasks and processing them asynchronously with workers)

**Metrics & Monitoring:**

- Prometheus
- Grafana
- Loki
- Node exporter
- Nginx exporter
- Cadvisor (Monitoring containers)

**ML:**

- Bert
- Thesaurus
- Gemini
- Groq
- FAST API
- Uvicorn
- Pydentic (Pydantic is the most widely used data validation library for Python)
- Transformers, Torch, Tokenizers, Numpy, Pandas, NLTK, Scikit, Selenium

### Setup instructions

<!-- _Describe the sequence of actions to launch your project, starting with cloning repositories._ -->

Installation & Testing
[README](https://github.com/FluentlyOrg/Fluently-fork/blob/main/README.md)

Fluently can be installed in two ways:

1. [Local/Development Installation](https://github.com/FluentlyOrg/Fluently-fork/blob/main/docs/Install_Local.md)

   Recommended for teaching assistants and quick testing.
   No domain or SSL required.
   All services run on localhost using Docker Compose.
   Test API, Swagger UI, and frontend separately.

2. [Full Production Installation](https://github.com/FluentlyOrg/Fluently-fork/blob/main/docs/Install_Full.md)

   For advanced users or production deployment.
   Requires your own domain and SSL certificates.
   Replicates the production environment.

## Presentation draft

<!-- _Add here a link to the presentation draft._ -->

[link](https://www.canva.com/design/DAGs-uCYPyY/-Af5fB66awIhLapWH_ZIOw/edit?utm_content=DAGs-uCYPyY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

# Weekly commitments

## Individual contribution of each participant

### Danila Kochegarov (Team Lead & Backend Developer)

- Finalized telegram bot implementation
- Fixed Backend side
- Did presentation
- Connect AI proxy with backend

### Savva Ponomarev (iOS Developer & Project Manager)

- Wrote report
- Add comments for new code
- Integrate new endpoints from backend to app
- Fixed errors and other problems that appeared
- Finalize UI with:
  - chat with AI screen
  - user preferences screen
  - daily word

### George Selivanov (System Analyst)

- Setup prompts for LLM Chat
- Make endpoint to work with it

### Timofey Ivlev (DevOps Engineer)

- Added platform testing workflow: tested local installation on windows, ubuntu, macos. Sadly, only ubuntu local installation works stable. Hence, currently, the only supported platform for installation is ubunty 22.04 or higher
  https://github.com/FluentlyOrg/Fluently-fork/commit/c82b1ae
- Fixed problems with quality-check pipeline
  https://github.com/FluentlyOrg/Fluently-fork/pull/237

### Anton Korotkov (ML Engineer)

- Fixed BERT issues

### Daniil Tskhe (Backend Developer)

- Wrote endpoint for getting day word (depends on user's cefr_level)
- Wrote getting user_pref (settings for user) and fix small bag with it
- Wrote update user_pref with optional fields (without errors)
- Clean swagger and add new documentation
- Wrote comments for backend code
- Clean code

### Evgeniy Bortsov (Android Developer)

- Calendar screen
- Statistics screen of learned/unlearned words
- Support for the word of the day

## Plan for Next Week

- Preparing for final presentation
- Technical Tests, fixing crucial bugs
- Final vibe-check

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
