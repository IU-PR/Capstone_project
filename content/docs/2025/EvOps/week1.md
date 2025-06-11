---
title: "Week #1"
---

# Week #1

## Project Description

- **Name**: EvOps 🐳
- **Code repository**: https://github.com/IU-Capstone-Project-2025/evops

### Motivation

It is 2025, there are many sources of information. Telegram chats, email
notifications, real-life announcements—everything wants your attention\! Because
of this option hell, people get lost and frustrated. In short, “many info bad.”
That’s why we decided to create a new app to rule them all\!

### Description

**EvOps** is a self-hosted platform to share and discover local events (e.g.
performances, parties, or study sessions). You can think of it as a full-stack
alternative to the “Opportunities For You” Telegram channel (which it may
actually become).

Our main goal for now is to integrate into the university ecosystem. If
everything goes well, we may even go beyond and allow anyone to launch their own
instance of EvOps.

## Team Members

| Team Member           | Telegram Alias                             | Email Address                        | Track                        | Responsibilities                                                                                                             |
| --------------------- | ------------------------------------------ | ------------------------------------ | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| (Lead) Asqar Arslanov | [@AsqArslanov](https://t.me/AsqArslanov)   | a.arslanov@innopolis.university      | Full-Stack                   | Make sure the project gets finished.                                                                                         |
| Aleksandr Isupov      | [@can4red](https://t.me/can4red)           | a.isupov@innopolis.university        | Mobile, Design, QA           | Design the front end (especially, mobile), develop the Android application.                                                  |
| Arsen Galiev          | [@rosehipbloom](https://t.me/rosehipbloom) | a.galiev@innopolis.university        | Frond-End, DevSecOps, Design | Develop the web user interface, maintain security of the services.                                                           |
| Egor Pustovoytenko    | [@egraPA](https://t.me/egraPA)             | e.pustovoytenko@innopolis.university | Back-End, Documentation      | Help with implementing the back end, write docs, reports.                                                                    |
| Ilya-Linh Nguen       | [@pickpusha](https://t.me/pickpusha)       | i.nguen@innopolis.university         | DevOps, Documentation        | Deploy the project, set up runtime environments, prepare the infrastructure.                                                 |
| Maksim Ilin           | [@iamimd](https://t.me/iamimd)             | m.ilin@innopolis.university          | ML                           | Work on tag auto-assignment, implement an event recommendation system, conduct experiments to evaluate efficiency of models. |
| Ramil Shakirzyanov    | [@Fullerite](https://t.me/Fullerite)       | r.shakirzyanov@innopolis.university  | ML                           | Work on preliminary tag extraction, implement an event recommendation system, deploy the trained models.                     |

## Brainstorming

### Ideas During Brainstorming

1. A type-safe i18n framework with code generation.

   The concept is similar to Paraglide JS. The main difference is that we wanted
   to build an app not restricted to JavaScript only. This project would have
   high value since there are no alternatives that offer the same functionality.
   However, it requires a very narrow set of skills and doesn’t seem suitable
   for a team project.

2. Yet another educational platform with fancy visualization of computer science
   concepts.

   The idea arose when reading Tanenbaum’s Modern Operating Systems book. The
   lack of visualization and interaction made understanding fundamental concepts
   complicated. However, we did not want to implement this project because
   education and AI are overrated nowadays. 👹

3. Finally, today’s star—an event aggregator.

   We settled on this idea because (1) this project has easy to understand and
   implement requirements, (2) it incorporates different skills. We decided to
   take on this idea and make the best out of it. Besides, there is a need for
   such a service in our university, so we can already research requirements of
   our first potential client and try to meet them in our product.

### Market Research

#### Competitors

| Platform                                                       | Self-Hosted? | Authentication / Closed Groups                      | Admin Controls (Moderation/Review) | Open Source?         | Monetization                       | Key Strengths                     | Key Weaknesses                                    |
| :------------------------------------------------------------- | :----------- | :-------------------------------------------------- | :--------------------------------- | :------------------- | :--------------------------------- | :-------------------------------- | :------------------------------------------------ |
| [**Mobilizon**](https://mobilizon.org/)                        | ✅ Yes       | ✅ Federated (multiple closed groups), SSO possible | ❌ Limited moderation tools        | ✅ AGPL (fully open) | 🐧 Free (hosting costs only)       | Privacy focused, decentralized    | Weak admin controls, hard to scale for large unis |
| [**Gath.io**](http://gath.io/)                                 | ✅ Yes       | ✅ Private groups, email-based access               | ✅ Basic admin dashboard           | ❌ Proprietary       | 💰 Subscription (per-user pricing) | AI-based networking, clean UI     | Expensive, vendor lock-in                         |
| [**Eventyay**](https://www.eventyay.com/)                      | ✅ Yes       | ❌ Public-first (weak closed groups)                | ✅ Event approval workflows        | ✅ Apache 2.0        | 🐧 Free (self-hosted)              | Good for ticketing and scheduling | Not built for universities                        |
| [**CampusGroups**](https://www.campusgroups.com/product/home/) | ❌ No (SaaS) | ✅ University SSO, org-based access                 | ✅ Full admin controls             | ❌ Closed-source     | 💰💰 High annual licensing         | Tailored for student engagement   | Expensive, no self-hosting                        |
| [**Meetup.com**](http://meetup.com/)                           | ❌ No (SaaS) | ❌ Public (no real closed groups)                   | ✅ Basic moderation                | ❌ Proprietary       | 💰 Organizer fees \+ ads           | Large network effect              | No privacy, unsuitable for universities           |

#### Conclusion

The comparison table shows the gap in existing solutions. There is no
easy-to-use open source, self-hosted system, that provides all the needed
functionality.

## Basic Requirements

### Target Users and Their Primary Needs

Since our main priority is to integrate into our university’s ecosystem, the
requirements are defined with respect to the administration’s (319 👋) requests.
Here, we’ve split our users into several groups and tried to identify their
needs:

- Event viewers (e.g. students)
  - Smart recommendation system
  - Convenient UX / responsiveness
- Event organizers (e.g. club leads, active students, administration)
  - Rich tools for creating events
  - Collecting attenders for an event
- Moderators (e.g. administration, trusted people)
  - Reviewing events to be published
- Hosters (e.g. our university)
  - Ease of hosting
  - Configurability
  - Maintainability

### User Stories

- Event viewers (student):
  - **Discover Events:** as a student, I want to see upcoming events relevant to
    my interests (e.g., CS workshops, basketball games), so that I don’t miss
    opportunities.
  - **One-Click Registration:** as a busy student, I want to discover events in
    one click, so that I can quickly register for events without logging into
    multiple platforms.
- Event organizer:
  - **Simple Event Creation:** as an event organizer, I want to create an event
    with title, date, location, description, and tags, so I can share it in less
    than five minutes.
  - **Event Tracking:** as an event organizer, I want to see in real time the
    number of attendees, so I can plan my resources.
  - **Event Updates:** as an event organizer, I want to notify all potential
    attendees if an event is cancelled or updated, so everyone will know only
    relevant information.
- Moderators:
  - **Content Moderation:** as an admin, I want to review inappropriate events
    and ban abusive users, so the platform stays safe and spam-free.
  - **User Role Permissions:** as an admin, I want to assign roles to club
    leaders, so only trusted accounts can post events as clubs.

### Initial Scope

Based on our current vision for the project, we want to see the following core
features:

- Account management.
- CRUD operations on events.
- Feed with existing events with a recommendation system.
- Convenient event editor.
- Search system with filters.
- Admin dashboard.
- Cross-platform support.

## Tech Stack

Below are listed the main technologies we are going to use in our project.\
We could say that the main criteria we valued were scalability, performance,
maturity, and other nice things, (which isn’t false to be fair), but being
honest, our tech stack has mainly been justified by our experience and personal
preferences. We’re only students, after all\!

### Back End

- **Rust**: primary programming language (fast, robust, mature, fun 🦀).
- **Axum**: REST web-framework with great ecosystem support.
- **Tonic**: gRPC web-framework with great ecosystem support.
- **Diesel**: type-safe and fast database driver.
- **PostgreSQL**: battle-tested DBMS, needs no introduction.

### ML

- **Python**: primary programming language with a huge ML ecosystem.
- **PyTorch**: deep learning framework used to build and train neural networks.
- **Hugging Face Transformers**: library providing powerful, ready-to-use
  versions of BERT and other advanced AI models (transformers).
- **SentenceTransformers**: library for creating embeddings (vector
  representations) for whole sentences.
- **scikit-learn**: toolkit for measuring model performance (metrics) and using
  standard (“classical”) machine learning algorithms.
- **pandas/numpy**: essential libraries for working with data and doing math
  operations.
- **Jupyter**: interactive notebooks for code experiments and sharing results.

### Android

- **Kotlin**: primary programming language.
- **Jetpack Compose**: UI toolkit.
- **Room**: library for local data storage using SQLite.
- **Dagger Hilt**: dependency Injection (DI) framework.
- **Retrofit**: type-safe HTTP client for REST API communication.

### Website

- **TypeScript**: primary programming language, JavaScript’s best version (no
  discussion).
- **Next.js**: full-stack meta framework to build web apps.
- **pnpm**: package manager, the fastest npm replacement.
- **Tailwind CSS**: battle tested CSS framework to style the application.
- **Element UI**: UI library for desktop web apps.
- **ConnectRPC**: library for client-server gRPC communication.

### DevOps

- **Docker Compose**: industry standard for orchestrating containers.
- **GitHub Actions**: automated CI/CD.

#### Potentially:

- **Prometheus**: hardware metrics and monitoring.
- **Grafana**: visualization dashboard that works well with Prometheus.
- **Kubernetes**: container orchestration platform.

## Notable Meeting Results

### Key Points From Meeting 1 _(June 3)_

- Agreed on the main idea of the project.
- Distributed the team roles (see the “Team Members” table)
- Picked a name for the project (the other options were Exam, UniVerse, and
  O4U).
- Drew the User Flow diagram.
- Agreed to design screen prototypes.
  (https://www.figma.com/design/TLU6AcZ9vvGVVoCpWuYaoN/EvOps?node-id=10-3&t=7Lin6J0iCJnUqnXt-1)
- Came up with a club system.
- Designed a communication between the back end and front end.

![](https://downloader.disk.yandex.ru/preview/80341ad084bf90ade986c3b218f6d19e38a24d68fac1257aeb17d27adf1dd454/684a23bb/loPBuXttaOqYftmULVIz8Lm9BuCwxru1420mbeWVRqbjmRgwfp9uIgB60zH9_TrOXLpYs0AHI-7IR5weVTpqKQ%3D%3D?uid=0&filename=small_board_1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v3&size=2048x2048)
![](https://downloader.disk.yandex.ru/preview/58c72893c4dabe08c200c073abc32e3df24042c3c1976554b1c3057f77b25cdf/684a2306/Q0L1zp36EVOnPPfzY4H3XKwo1i68goYrL8pjUJ1SWynrrDWy0V61ZgOgQHPEvbZwhvTdWeoxPI27prFDwjJ2hA%3D%3D?uid=0&filename=board_2.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v3&size=2048x2048)

### Key Points From Meeting 2 _(June 5)_

- Discussed ML services, such as the tag-assignment system and the
  recommendation system.
- Came up with a system of upvotes/downvotes for posts to configure
  recommendations.
- Decided to treat clubs as tags (initially, they were planned to be treated as
  separate entities).
- Divided tags into “public” and “private.”
- Agreed to give “hosters” (organizations that run an instance of our
  application) the right to define a preliminary set of tags.
- Decided to take a less strict approach to the API and not establish it very
  early, since we need to explore the requirements better first.
- Started to construct request/response schemas on the back end.

### Key Points From the Meeting With 319 _(June 10)_

1. **Comprehensive Content Moderation**
   - Strict oversight of all published content.
   - Zero tolerance for low-quality or irrelevant material in public channels.
2. **Innopolis Super App Development**
   - Integration of essential functionalities within a unified platform.
3. **Mandatory Communications**
   - Critical announcements must remain unmuted for all users.
   - The #official tag should be auto-favorited in user profiles.
4. **User Reporting & Transparency**
   - Clear process for submitting moderation complaints.
   - Constructive feedback provided upon content disapproval.
5. **Content Creation Standards**
   - Established templates and guidelines for post formatting.
   - Prohibition of harmful or dangerous content.
6. **User Experience Enhancements**
   - Intuitive UI with content categorization.
   - Automated language localization (e.g., Russian/English) based on user
     settings (potential LLM integration).
7. **Moderation Workflow**
   - Dedicated staff for manual review (with potential AI/LLM assistance).
8. **User-Centric Approach**
   - Regular focus group sessions to gather feedback.
   - Prioritization of utility over social networking features.
9. **Cross-Platform Integration**
   - Seamless synchronization with Telegram channels.
10. **Public Access & Ethical Standards**
    - Compliance with public ethics and corporate PR policies.
11. **AI-Powered Efficiency**
    - Automated summaries of posts for quick consumption.

## Weekly Commitments

### Individual contribution of each participant

#### Asqar Arslanov

- Designed the structure of Git repositories.
  ([https://github.com/evops-sum25/evops](https://github.com/evops-sum25/evops))
- Configured the Git workflow for the team.
  ([https://github.com/evops-sum25](https://github.com/evops-sum25))
- Wrote boilerplate code for the back end.
  ([https://github.com/evops-sum25/evops-backend](https://github.com/evops-sum25/evops-backend))
- Made a hybrid REST + gRPC web server.
  ([https://github.com/evops-sum25/evops-backend/blob/7d9d507bd739b48d9feb83aa36aa22fc700b158e/crates/evops/src/main.rs](https://github.com/evops-sum25/evops-backend/blob/7d9d507bd739b48d9feb83aa36aa22fc700b158e/crates/evops/src/main.rs))
- Configured automated generation of API docs.
  ([https://github.com/evops-sum25/evops-backend/blob/7d9d507bd739b48d9feb83aa36aa22fc700b158e/crates/evops-rest/src/docs.rs](https://github.com/evops-sum25/evops-backend/blob/7d9d507bd739b48d9feb83aa36aa22fc700b158e/crates/evops-rest/src/docs.rs))
- Wrote boilerplate code for the client extension.
  ([https://github.com/evops-sum25/evops-client-ext/tree/d47977ad880ee480b820448aaefbe3ac9e52b813](https://github.com/evops-sum25/evops-client-ext/tree/d47977ad880ee480b820448aaefbe3ac9e52b813))
- Wrapped a Markdown parser in a language-independent API.
  ([https://github.com/evops-sum25/evops-client-ext/blob/d47977ad880ee480b820448aaefbe3ac9e52b813/crate/src/markdown.rs](https://github.com/evops-sum25/evops-client-ext/blob/d47977ad880ee480b820448aaefbe3ac9e52b813/crate/src/markdown.rs))
- Wrote Dockerfiles for the back end.
  ([https://github.com/evops-sum25/evops-backend/tree/7d9d507bd739b48d9feb83aa36aa22fc700b158e](https://github.com/evops-sum25/evops-backend/tree/7d9d507bd739b48d9feb83aa36aa22fc700b158e))
- Helped with creating the Docker Compose file.
  ([https://github.com/evops-sum25/evops/blob/e05e44d799a5cb196a1313faaf5ca336a0e010a4/compose.yaml](https://github.com/evops-sum25/evops/blob/e05e44d799a5cb196a1313faaf5ca336a0e010a4/compose.yaml))
- Visited the meeting with the 319 team.

#### Aleksandr Isupov

- Designed two screens of the Android application in
  [Figma](https://www.figma.com/design/TLU6AcZ9vvGVVoCpWuYaoN/EvOps?node-id=10-3&t=7Lin6J0iCJnUqnXt-1).
- Created presentation layer components of those two screens.
  - https://github.com/evops-sum25/evops-android/commit/f08f52a2fb97059e5f59b040019811ddc9e42750
  - https://github.com/evops-sum25/evops-android/tree/can4red/event-details-ui

#### Arsen Galiev

- Wrote boilerplate code for the web front end.
  ([https://github.com/evops-sum25/evops-website](https://github.com/evops-sum25/evops-website))
- Organized and hosted a meeting with the IU 319 team.
- Created and distributed tasks in the kanban dashboard via GitHub Projects.
  ([https://github.com/orgs/evops-sum25/projects/1](https://github.com/orgs/evops-sum25/projects/1))
- Created a technological concept of the project (photos below on a whiteboard).

#### Egor Pustovoytenko

- Refreshed knowledge of Rust by going through the
  [Rust Book](https://doc.rust-lang.org/book/) (Especialy Chap. 7, 9, 14).
- Read the
  [Tonic documentation](https://github.com/hyperium/tonic/blob/master/examples/helloworld-tutorial.md)
  and set up a Hello world app.
- Researched the market and competitors.
- Made a stub gRPC server for ML.
  (https://github.com/evops-sum25/evops-ml/commit/7bbc1bc06a7f7f66feee3e76cbd94a9f45f9bf35)

#### Ilya-Linh Nguen

- Configured the Docker Compose file.
  (https://github.com/evops-sum25/evops/commit/0a824be1adde5b59e1e34e39156a1462d18f080a)
- Wrote the README.md file with build instructions.
  (https://github.com/evops-sum25/evops/commit/e05e44d799a5cb196a1313faaf5ca336a0e010a4)
- Made the Dockerfile for the website.
  (https://github.com/evops-sum25/evops-website/commit/f18d200937c91c51a2f25762fb1b8e0aa387a72f)
- Searched and read the documentation of Kubernetes
  (https://kubernetes.io/docs/home/)
- Researched about
  [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and how
  to automate them.
  (https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes)

#### Maksim Ilin

- Extracted and preprocessed messages from the “Opportunities For You” Telegram
  channel for further work.
  (https://github.com/evops-sum25/evops-ml/commit/e39a8141c5bec5292c4f5e9cb93282ed1439bfe5)
- Learned how to download and launch models locally.
  (https://huggingface.co/docs/huggingface_hub/guides/download)
- Implemented automated post tagging using zero-shot classification.
  (https://github.com/evops-sum25/evops-ml/commit/b7d200d2afd2ecd061960b67b297358dd3c11045)

#### Ramil Shakirzyanov

- Reviewed the preprocessed messages by Maksim.
- Extracted keywords from the messages using statistical keyword extraction,
  noun phrase chunking, and topic extraction based on semantical clustering.
  (https://github.com/evops-sum25/evops-ml/commit/689f6b5888528cb4c03aff8a8c7aab04792e03a7)
- Curated the extracted keywords to build a final list of predefined tags.
  (https://github.com/evops-sum25/evops-ml/commit/01dc88d3905da0e577f543d6277b020e7ee41ed0)

#### Ramil Shakirzyanov and Maksim Ilin

The ML team discussed the project’s solution designs and the ways of measuring
their efficiency.

**Proposed Ideas**

1. **Automatic Tag Extraction**
   - **Goal**: Get a preliminary list of tags for application events
   - **How**: Load and preprocess messages from the Telegram channel
     “Opportunities For You.” Send them to a language model to retrieve post
     topics. Finally, manually choose the preliminary set of tags.

2. **Automatic Post Classification**
   - **Goal**: Automatically tag posts within the application.
   - **How**: When a user creates a post in the application, send the post
     description _and_ the preliminary tag set to a language model. The model
     will assign the most suitable multiple tags.

3. **Post Recommendation System:**
   - **Goal**: Recommend relevant posts to users.
   - **How**:
     - Build user “good” and “bad” profiles using metadata (for example, emoji
       reactions to posts in the application, comments left, etc.) as a weighted
       sum of the vector representations of the corresponding posts.
     - For each post the user hasn’t seen and that is still relevant, calculate
       its “score” using a formula.
     - Recommend posts with the highest scores.
   - **Notes:**
     - A post is “unseen” if the user hasn’t reacted to it with an emoji.
     - “Relevant” means the event isn’t over when we make recommendations.
     - This formula is subject to change.

**Measuring Effectiveness**

- **For Automatic Tag Extraction and Automatic Post Classification:**
  - We will verify how well the tags align with the meaning of a sample of posts
    taken from the “Opportunities For You” Telegram channel, logically.
- **For the Post Recommendation System:**
  - We’ll give access to the Application to a test group (inside and probably
    outside the team).
  - Each person will focus more on a pre-agreed set of events.
  - We will assess how well the recommended posts align with the types of events
    people view.

## Confirmation of the Code’s Operability

We confirm that the code in the `main` branch:

- [x] Is in a working condition.
- [x] Runs via Docker Compose.
