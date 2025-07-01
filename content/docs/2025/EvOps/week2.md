---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

As the semester goes on, we approach the point when we have to present an MVP.
At the least, it should have a feed of events with tags and pages to view event
details. As simple as it may sound, there is also much subsidiary work that
needs to be done as well.

Having defined a clear goal helps us organize our work more efficiently. For
example, during this week, a lot of effort was put into the back end. Now, when
its basic functionality has more-or-less been implemented, we can focus more on
the front ends.

To reach this milestone, we keep a backlog / kanban board with all issues sorted
by their priority. We have three main sections: **Todo** (work hasn’t been
started yet), **In Progress** (issue is being worked on), and **Done** (solution
has been implemented). To avoid polluting the Done section over time, we created
an **Archive** section where all old issues go after some time. We deliberately
avoided adding more sections with more complex semantics (e.g. _Review_ or
_Plans_) since it would only slow us down.

Here is the link to our…

### Prioritized Backlog

[https://github.com/orgs/evops-sum25/projects/1](https://github.com/orgs/evops-sum25/projects/1)

## Project Specific Progress

### Back End

- Implemented REST and gRPC endpoints to find/list/create events/tags/users.
- Added rich HTTP and gRPC error handling.
- Refactored the codebase to match new architectural patterns.

### Machine Learning

- The recommendation system has been partially implemented. For each user, a
  recommendation profile has been assigned.
- Ten artificial users with complete metadata were created to test the
  recommendation system. The test group experiments were abandoned due to their
  complexity.

### UX/UI Design

- Designed the event details page.

### Android Application

- Set up a dev connection to the back end.
- Implemented UI components of the event details screen as much as possible for
  now.
- Mapped back-end models to native types.

## Weekly Commitments

### Individual Contribution of Each Participant

#### Aleksandr Isupov

- Completed all the work related to the Android section of Project Specific
  Progress:
  - Set up dependencies for network calls (Retrofit) and dependency injection
    (Dagger Hilt).
  - Made presentation layer components for the event details screen
    ([commit](https://github.com/evops-sum25/evops-android/commit/eb05efadf8449e7252ac376b1d30ad69ff8c64ec)).
  - Integrated Retrofit and Dagger Hilt to the app to set up a network
    connection with a local back end
    ([commit](https://github.com/evops-sum25/evops-android/commit/efd8b820ddabe88ef1ef87cbe1a2d147db472252)).
- Created data models from the back end and mappers to existing domain models
  ([commit](https://github.com/evops-sum25/evops-android/commit/ea5e8b51c748c5b45555678e01096edafdd865df)).
- Studied QA tools (JUnit) in the T-Course section “Introduction to Automated
  Testing” ([course page](https://education.tbank.ru/study/fintech/qamobile/)).

#### Arsen Galiev

- Completed the design of event pages
  ([Figma](https://www.figma.com/design/TLU6AcZ9vvGVVoCpWuYaoN)).
- Visited the meeting with a university employee (TA) on service integration and
  development.
- Finalized the choice of a UI library and merged the pull request with its
  addition ([PR](https://github.com/evops-sum25/evops-website/pull/16)).

#### Asqar Arslanov

- Studied
  [hexagonal architecture](https://www.howtocodeit.com/articles/master-hexagonal-architecture-rust)
  and
  [type-driven design](https://www.howtocodeit.com/articles/ultimate-guide-rust-newtypes).
- Refactored the back end using techniques described in the articles above
  ([commit](https://github.com/evops-sum25/evops-backend/commit/65fec9d67dbaa9e4c74facf780b3a0df3b6a4e6a)).
- Added basic CRUD endpoints to the back end (the exact same
  [commit](https://github.com/evops-sum25/evops-backend/commit/65fec9d67dbaa9e4c74facf780b3a0df3b6a4e6a)).
- Visited the meeting with our TA (👋) on integrating our product into the
  university ecosystem.
- Reviewed Egor’s pull request on the ML gRPC server
  ([PR](https://github.com/evops-sum25/evops-ml/pull/16)).

#### Egor Pustovoytenko

- Implemented the ML gRPC server
  ([commit](https://github.com/evops-sum25/evops-ml/commit/f335d38ea1cb4767e38ed4fc0547102c6e02d416)).
- Created the `server-ext` repository for easy server communication
  ([commit](https://github.com/evops-sum25/evops-ml/commit/f335d38ea1cb4767e38ed4fc0547102c6e02d416)).

#### Ilya-Linh Nguen

- Added automatic changelog generated using the
  [git-cliff](https://git-cliff.org/) tool
  ([commit](https://github.com/evops-sum25/evops/commit/630ef02903c3041deb2ae437f911f725ae26bfcd)).
- Add a Dockerfile and .env.example to ML repository for deployment
  ([commit](https://github.com/evops-sum25/evops-ml/commit/6f69adedaf39934b75344238f7863a1d93378c86)).
- Add the ML server to the Compose file
  ([commit](https://github.com/evops-sum25/evops/commit/a754ea2dcc5ace338048a776b48af61f9cb0e02e)).
- Some small fixes regarding Automated Changelog, Docker Compose file, and
  `.env.example` for the back end
  ([commit 1](https://github.com/evops-sum25/evops/commit/e236106bd36c9818af3aeb2672d4968875e84133),
  [commit 2](https://github.com/evops-sum25/evops/commit/86cb814deff687135a6591b6df165331433a5835)).

#### Maksim Ilin

- Create five artificial users for further testing of the recommendation system
  ([commit](https://github.com/evops-sum25/evops-ml/commit/ccbbce6fd4e851903a5ff048ac117f17dd06a8ac)).
- Implement user profile generation for the recommendation system testing and
  hyperparameter selection. Here, a user profile is considered to be the
  weighted average of post embeddings and metadata
  ([commit](https://github.com/evops-sum25/evops-ml/commit/ccbbce6fd4e851903a5ff048ac117f17dd06a8ac)).

#### Ramil Shakirzyanov

- Create the initial data frame with user messages
  ([commit](https://github.com/evops-sum25/evops-ml/commit/8f886ee304294f8aa09d20fa048635b1d5eb3f50)).
- Adjust the user interaction data frame and create five mock user interaction
  profiles for later rec-sys testing
  ([commit](https://github.com/evops-sum25/evops-ml/commit/8f886ee304294f8aa09d20fa048635b1d5eb3f50)).

## Plan for Next Week

#### DevOps

I plan to clarify the amount of servers and start deploying the Kubernetes on
servers. If I end this fast, I will start writing CI/CD using GitHub actions and
maybe deploy some services (back end or front end or all together).

#### Machine Learning

The ML team plans to fine-tune the hyperparameters for the recommendation
system, such as the weights of the metadata and the hyperparameter for the
formula _(profile \= good\_profile − λ bad\_profile)_, where the profiles are
considered embeddings, by manually comparing recommendation sets for ten
artificial users.

The most important part of the plan is to transfer the tag classification and
recommendation system models from Jupyter notebooks to production.

Additionally, we plan to create database table structures for posts and users
and connect the models to the database.

#### Back End

- Add more endpoints / update the existing ones.
- Establish communication with the ML gRPC server.
- Document all methods and schemas with proper descriptions.
- Extract some functionality to `server-ext`.
- Export validation methods to `client-ext`.

#### Android Appliaction

- Complete the `EventList` and `EventDetails` screens.
- Start working on the `CreateEvent` screen.

#### Website & Design

- Complete the rest of the main pages in the Figma prototype.
- Host a server for the front end and implement some pages in code.

### Confirmation of the Code’s Operability

We confirm that the code in the `main` branch:

- [x] Is in working condition.
- [x] Runs via Docker Compose.
