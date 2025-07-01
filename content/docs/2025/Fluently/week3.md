---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

<!-- _Describe all implemented features (with to relevant PRs/Issues for implemented features) in your MVP and functional user journey(s)_ -->

_Integrate the frontend with the backend APIs, finalize all datasets, and deploy the pre-trained models._

## Demonstration of the working MVP

<!-- _Screenshots/GIFs/PDF presentation/Videos demonstrating the working MVP_ -->

### iOS

| ![Registration](https://github.com/FluentlyOrg/Fluently-fork/blob/feature/network-layer/report-imges/GIFs/LogInIOS.gif) | ![Lesson](https://github.com/FluentlyOrg/Fluently-fork/blob/feature/network-layer/report-imges/GIFs/LessonsIOS.gif) |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |

### Android

![Android MVP](<https://github.com/FluentlyOrg/Fluently-fork/blob/feature/network-layer/report-imges/GIFs/MVP_recording%20(online-video-cutter.com).gif>)

## ML

**Structured Knowledge Base**:

- Built hierarchical word database (29,997 entries) via Oxford Dictionary parsing
- Organized by:
  - Topics/subtopics
  - CEFR levels
  - Parts of speech
  - Popularity metrics

**Intelligent Processing**:

- Implemented translation pipeline:
  - Fallback from Yandex (CAPTCHA) to alternative API
  - Auto-generated:
    - Accurate translations
    - 5 EN→RU contextual examples per word
    - 3 synthetic variants per sentence (NLP-augmented)

**Lightweight Architecture**:

- Metadata-driven recommendations (no heavy ML)
- Enables:
  - Thematic learning paths
  - Adaptive difficulty scaling
  - Transparent customization

**Link to the training code**: [link](https://github.com/FluentlyOrg/Fluently-fork/tree/feature/ML-training-)

**Links to the initial model artifacts**: [link](https://github.com/FluentlyOrg/Fluently-fork/tree/feature/ML-Artifacts)

## Internal demo

_Notes from internal demo_

# Weekly commitments

## Individual contribution of each participant

### Danila Kochegarov (Team Lead & Backend Developer)

- Made Oauth2 with refresh token rotation
- Reviewed pull requests from iOS, DevOPS and backend developers
- Made linking telegram account to shared one (with google oauth)
- Made Telegram bot with lesson learning logic
- Made setup of async (with many workers) FastAPI backend for ML

### Savva Ponomarev (iOS Developer & Product Manager)

- Integrated Google authentication
- Developed login screen UI
- Built interactive lesson screens:
  - Fill-in-the-blank exercises
  - Translation typing challenges
  - Multiple-choice translation quizzes
- Configured app navigation/routing
- Created functional mock implementation
- Implemente Backend integration

Issues: \
https://github.com/FluentlyOrg/Fluently-fork/issues/108 \
https://github.com/FluentlyOrg/Fluently-fork/issues/109 \
https://github.com/FluentlyOrg/Fluently-fork/issues/110 \
https://github.com/FluentlyOrg/Fluently-fork/issues/111 \
https://github.com/FluentlyOrg/Fluently-fork/issues/113 \

### George Selivanov (System Analyst)

- Enriched data using Oxford Dictionary (Selenium):
- 29,997 words with topics, levels, and parts of speech.
- Failed Yandex Translator (CAPTCHA blocked) → switched to alternative API:
- Auto-parsed translations + 5 EN/RU example sentences per word.
- ML integration: Generated 3 synthetic variants per sentence for exercises.
- Final dataset powers adaptive lessons and recommendations.

### Timofey Ivlev (DevOps Engineer)

- Set up Prometheus+Grafana for monitoring API load, security issues \
  https://github.com/FluentlyOrg/Fluently-fork/issues/104

- Set up SonarQube \
  https://github.com/FluentlyOrg/Fluently-fork/issues/97

- Set up Loki for logs aggregations \
  https://github.com/FluentlyOrg/Fluently-fork/issues/103

- Set up a second deploy server with domain for testing \
  https://github.com/FluentlyOrg/Fluently-fork/issues/119

### Anton Korotkov (ML Engineer)

- **Hierarchical structure**:
  - Topics/subtopics
  - CEFR levels
- **Metadata-driven** (no heavy ML):
  - Uses word popularity/complexity
- **Selection flow**:
  1. Focused thematic clusters
  2. Broader topics → same level → higher levels
- **Benefits**:
  - Transparent & customizable
  - Lightweight
  - Scalable

### Daniil Tskhe (Backend Developer)

- Helped with setting up authorization via Google
- Rethinking lesson generation
- Rewrote the models to meet new requirements
- Wrote the main JSON generation for the lesson

### Evgeniy Bortsov (Android Developer)

- Authorization flow
- Home screen
- Lesson screens:
  - New Word
  - Choose Translation exercise
  - Fill the gap exercise
- Backend mock + parsing of backend models into app's internal models

Issues: \
https://github.com/FluentlyOrg/Fluently-fork/issues/108 \
https://github.com/FluentlyOrg/Fluently-fork/issues/109 \
https://github.com/FluentlyOrg/Fluently-fork/issues/110 \
https://github.com/FluentlyOrg/Fluently-fork/issues/111 \
https://github.com/FluentlyOrg/Fluently-fork/issues/113 \

## Plan for Next Week

### Testing

- **Unit tests**: Cover critical backend logic & frontend components
- **Integration tests**: API endpoints validation
- **E2E tests**: Core user journey (minimum viable coverage)
- **ML**: Basic model validation/testing

### CI/CD Pipeline

- **CI Setup**: GitHub Actions for auto-build/test on `push/PR` to `main/develop`
- **Bonus** (+5pts): CD to staging on `main` merge

### Deployment

- **Staging**: Setup on Heroku/AWS free tier
- **Bonus**: Production env on VPS
- Deploy current version to staging
- _Optional_: Configure public domain

### Team Health

- **Vibe check**:
  - Progress review
  - Blockers discussion
  - Team dynamics alignment

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
