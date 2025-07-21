---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: [http://31.59.170.53:3000](http://31.59.170.53:3000)
- **API Docs**:
  [http://31.59.170.53:8080/swagger](http://31.59.170.53:8080/swagger)
- **Demo**:
  [https://drive.google.com/drive/folders/1Ng3-i41OIIswpilSoouyh_s6slSOx8rE](https://drive.google.com/drive/folders/1Ng3-i41OIIswpilSoouyh_s6slSOx8rE)
- **Android Application Releases**:
  [https://github.com/evops-sum25/evops/releases](https://github.com/evops-sum25/evops/releases)
- **Source Code**:
  [https://github.com/evops-sum25/evops](https://github.com/evops-sum25/evops)

## Final Deliverables

### Project Overview

EvOps is a self-hosted platform to share and discover local events (e.g.
performances, parties, or study sessions). You can think of it as a full-stack
alternative to the “Opportunities For You” Telegram channel.

While the problem we’re solving isn’t very special or unique, we try to stand
out with our implementation. We designed two convenient user interfaces and
exposed a fast and robust API.

### Features

**Machine Learning:**

- Event Multi-Tagging: Automatically assigns multiple relevant tags to
  university events.
- User Profile Embeddings: Creates unique user profile embeddings based on their
  interactions (upvotes/downvotes, reactions, etc.) with event posts.
- Event Description Embeddings: Converts event descriptions into numerical
  embedding vectors.
- Custom University Tagging: Uses a specialized tag list developed based on the
  “Opportunities For You” Telegram channel.

**Back End:**

- API methods to create and view users, events, event images, and event tags
  (groups).
- Combined REST+gRPC web-server so that clients can choose their preferred
  communication way.
- Auto-generated OpenAPI documentation \+ Swagger webpage.
- Persistent data storage with PostgreSQL.
- Persistent image storage with MinIO.
- Data validation at the type-system level.
- Basic logging of incoming requests and their responses.
- Configurability with environment variables and a
  [`.env` file](https://github.com/evops-sum25/evops-backend/blob/main/.env.example).
- An [API extension](https://github.com/evops-sum25/evops-client-ext) for
  clients to ease the interaction with our back end:
  - Validation functions (such as `validate_event_title` or
    `validate_tag_alias`) that reuse the logic from the back-end core.
  - Fully-typed
    [Markdown parser](https://github.com/evops-sum25/evops-client-ext/blob/main/crates/evops-markdown/src/lib.rs)
    with our own parse settings.
  - Exporting to [WASM](https://webassembly.org/) with
    [Extism](https://extism.org/) and [Protobuf](https://protobuf.dev/) types.
  - Generating type-safe FFI bindings with
    [UniFFI](https://mozilla.github.io/uniffi-rs/latest/).

**Android Application:**

- **Event List screen:**
  - Displays a feed of event cards (card consists of title, author, truncated
    description, and one image).
- **Event Details screen**:
  - Displays all the event details (title, author, full description, up to 10
    attached images, location, time).
- **Add Event screen**:
  - Creates an event with the following fields:
    - Attached images.
    - Title.
    - Description.
    - Attached tags (if there is no tag for user needs, it can be created).
- **Settings**:
  - Switches between themes.

**Website:**

- Event feed page.
- Event details page.
- Event creation page.
- Smart dark mode.
- API query caching.
- Adaptive desktop+mobile layout.
- English and Russian localizations.

### Tech Stack

**DevOps:**

Our DevOps tech stack is pretty regular for any project. The only thing that
stands out is the use of `git-cliff` to automate the generation of changelogs.

- [**Docker**](https://www.docker.com/),
  [**Docker Compose**](https://docs.docker.com/compose/): containerization of
  services and connecting them with each other.
- [**`git-cliff`](https://git-cliff.org/)**: Markdown changelog generator.
- [**Ubuntu Server**](https://ubuntu.com/server): server based on Ubuntu for
  deploying the project.
- [**GitHub Actions**](https://docs.github.com/en/actions): CI/CD workflow.

**Machine Learning:**

The stack was not modified from the very beginning. The only thing that was
added is YAKE that helped us to determine the initial set of tags based on the
“Opportunities For You” Telegram channel.

- [**Python**](https://www.python.org/): primary language for ML development
- [**PyTorch**](https://pytorch.org/): deep learning framework for Zero-Shot
  classification
- [**Transformers**](https://github.com/huggingface/transformers)
  **/[Sentence-Transformers](https://github.com/UKPLab/sentence-transformers)**:
  NLP models for embeddings and text representation
- [**YAKE**](http://yake.inesctec.pt/): keyword extraction
- [**Scikit-learn**](https://scikit-learn.org/): model evaluation and metrics
  calculation
- [**Pandas**](https://pandas.pydata.org/): data processing and manipulation
- [**NumPy**](https://numpy.org/): numerical operations and array processing
- [**Jupyter**](https://jupyter.org/): interactive notebooks for code
  experiments and sharing results.

These technologies were selected for their proven capabilities in NLP tasks. The
main advantages include extensive pre-trained models and strong community
support. The only trade-offs were higher memory requirements for transformer
models and the need for GPU acceleration during inference. Overall, the stack
delivered maintainable solutions for our classification/embedding tasks.

**Back End:**

The tech stack for the back end hasn’t changed since the beginning. The only
major thing added was an object storage.

- [**Rust**](https://www.rust-lang.org/): primary programming language.
- [**Axum**](https://github.com/tokio-rs/axum): REST web-framework.
- [**Tonic**](https://github.com/hyperium/tonic): gRPC web-framework.
- [**Diesel**](https://diesel.rs/): type-safe ORM.
- [**PostgreSQL**](https://www.postgresql.org/): the most popular DBMS.
- [**MinIO**](https://min.io/): S3-compatible object storage.

These technologies proved themselves suitable for large-scale development. We’re
left satisfied choosing them. The only cons were long compile times and long
(but routine) development cycles. Though, when finishing refactors, we were
confident that we hadn’t broken anything. The type system and development
tooling have been very helpful.

**Android Application:**

The Android tech stack has not significantly changed from the initial plan. The
only changes are related to data storage: the application only uses the storage
for settings and does not utilize a database to cache the event list because it
may be frequently changed between user sessions.

- [**Kotlin**](https://kotlinlang.org/): primary platform programming language.
- [**Jetpack Compose**](https://developer.android.com/compose): UI toolkit.
- [**Gradle**](https://gradle.org/): build system.
- [**Retrofit**](https://square.github.io/retrofit/): type-safe HTTP client for
  REST API communication.
- [**Coil**](https://coil-kt.github.io/coil/): library providing cached network
  calls for image retrieval.
- [**Dagger Hilt**](https://dagger.dev/hilt/): dependency Injection (DI)
  framework.
- [**Kotlin Coroutines**](https://kotlinlang.org/docs/coroutines-overview.html):
  Kotlin asynchronous programming tool.
- [**Jetpack Navigation**](https://developer.android.com/guide/navigation):
  type-safe navigation library.
- [**Preferences DataStore**](https://developer.android.com/topic/libraries/architecture/datastore):
  settings key-value storage, providing flow access to data.

**Website:**

We decided to change the stack of our website to make development cycles faster
and reduce complexity of the project. The main change was moving from Next.js to
TanStack Router.

- [**TypeScript**](https://www.typescriptlang.org/): primary programming
  language.
- [**React**](https://react.dev/): UI framework.
- [**TanStack Router**](https://tanstack.com/router/latest): type-safe URL
  router.
- [**TanStack Query**](https://tanstack.com/query/latest): API handling library
  with data caching.
- [**Vite**](https://vite.dev/): code bundler and builder.
- [**pnpm**](https://pnpm.io/): fast package manager.
- [**Tailwind CSS**](https://tailwindcss.com/): styling framework.
- [**daisyUI**](https://daisyui.com/): Tailwind CSS UI framework.
- [**Connect RPC**](https://connectrpc.com/): type-safe gRPC client.
- [**react-i18next**](https://react.i18next.com/): React-specific port of the
  [i18next](https://www.i18next.com/) localization library.

### Setup Instructions

Prerequisites: we assume, you don’t have any Docker volumes or build cache that
may collide with our application. Also, we expose ports `3000`, `5432`, `8080`,
`9000`, and `9090`.

1. Clone the repository and enter its directory:

- ```shell
  git clone --recurse-submodules https://github.com/IU-Capstone-Project-2025/evops.git

  cd evops/
  ```

2. Set up the `.env`, `backend/.env`, `ml/.env`, and `website/.env` files:

   ```shell
   cp .env.example .env
   cp backend/.env.example backend/.env
   cp ml/.env.example ml/.env
   cp website/.env.example website/.env
   ```

3. Run the app with Docker Compose:

- ```shell
  docker compose up --build
  ```

The website should then be available on
[http://localhost:3000](http://localhost:3000).

The back end should also be accessible on
[http://localhost:8080](http://localhost:8080).

Note that service communication is assumed to take place on your local machine
via the HTTP protocol. Web-browsers may apply CORS restrictions. Make sure your
browser settings don’t interfere (you may want to use an extension such as CORS
Unblock).

## Presentation Draft

[Right here](https://docs.google.com/presentation/d/1unrj7ghi3QbifSerq3MB0h3T1QeoA0ZiyXCXjEJ5u6c/edit?usp=sharing).
😁

## Weekly Commitments

### Individual Contribution of Each Participant

#### Aleksandr Isupov

- Integrated tag attachment and creation functionality
  ([commit](https://github.com/evops-sum25/evops-android/commit/ab0e6eb54f58b41f3c23cd3a5886ee400711ee5d)).
- Updated the Add Event screen design
  ([commit](https://github.com/evops-sum25/evops-android/commit/feae6e6d112fc2a8bd91c62b6740dec1f1627798)).
- Integrated pagination
  ([commit](https://github.com/evops-sum25/evops-android/commit/68dd0e1f2acaec964264905c0bc0ec3833eba685)).
- Fixed a bug that caused multiple images to be deleted by a single URI
  ([commit](https://github.com/evops-sum25/evops-android/commit/3706aadd4baa79ff5a313416ba0d57184588935d)).
- Added descriptions to event list cards
  ([commit](https://github.com/evops-sum25/evops-android/commit/ad9872b27a3643ab96d6ef6930c45cbf4745a669)).
- Started working on the Settings screen
  ([branch](https://github.com/evops-sum25/evops-android/tree/can4red/settings)).

#### Arsen Galiev

- Migrated from SSR Next.js to Vite \+ default React with CSR
  ([commit](https://github.com/evops-sum25/evops-website/commit/6f7759346ad1f4cbd1369551bb6719d61ccd71b2))
- Complete integration with TanStack Query for data caching
  ([issue](https://github.com/evops-sum25/evops-website/issues/7))
- Add multiple image uploads for an event
  ([issue](https://github.com/evops-sum25/evops-website/issues/27))
- Update adaptive layout bugs
  ([commit](https://github.com/evops-sum25/evops-website/commit/e4370279cdfbbc0ee60ba0c09e884e95736491fe))
- Pagination ([issue](https://github.com/evops-sum25/evops-website/issues/28))

#### Asqar Arslanov

- Fixed the WASM build of the client extension
  ([commit 1](https://github.com/evops-sum25/evops-client-ext/commit/cc5b6adfc0a963f172c758e9b6aa868e32224508),
  [commit 2](https://github.com/evops-sum25/evops-client-ext/commit/5614be2f3ba26c5ca51bc91eb9cee81299b97ea6)).
- Fixed image uploading to the back end not being atomic
  ([commit](https://github.com/evops-sum25/evops-backend/commit/79fe33bca2268dc412efbdb9b76d30e7c5834fa9)).
- Designed new API endpoints with Egor
  ([PR](https://github.com/evops-sum25/evops-backend/pull/57)).
- Helped Arsen migrate the website from Next.js to TanStack Router
  ([commit](https://github.com/evops-sum25/evops-website/commit/6f7759346ad1f4cbd1369551bb6719d61ccd71b2)).
  - Connected the
    [API extension](https://github.com/evops-sum25/evops-client-ext).
  - Configured i18n to be type-safe.
- Wrote a Markdown renderer for the website
  ([commit](https://github.com/evops-sum25/evops-website/commit/464f3ff12d384ad6adf855caef4a64025c44be18)).

#### Egor Pustovoytenko

- Worked on API endpoints (we used Zed collab for it, so not my commit
  ([PR](https://github.com/evops-sum25/evops-backend/pull/57))).
- Work in progress on implementing the business logic
  ([commit](https://github.com/evops-sum25/evops-backend/commit/bd93d5f06e3123ba5dad8c4947d78b210916a3aa)).
- Created draft presentation.

#### Ilya-Linh Nguen

- Added a CI workflow for the Android app
  ([commit](https://github.com/evops-sum25/evops/commit/fe402c4a9f11d35a37c876e74058bbffc8ddfe5a)).
- Published a a new Android release
  ([release](https://github.com/evops-sum25/evops/releases/tag/v0.4.0)).
- Bought a domain for the server, started setting up nginx on it

#### Maksim Ilin

- Reworked the fake data uploading process and contents
  ([PR](https://github.com/scrii/evops-dummy-photos/pull/1),
  [commit](https://github.com/evops-sum25/evops-dummy-data/commit/2b6d1bb181efe9095dc37078c2cb110c33ae7eb5))
  - Refactor the event-creating function and the event code structure.
  - Added meaningful (more or less) titles for events (a language model
    approach).
- Created a service class for the event description embedding creation
  ([commit](https://github.com/evops-sum25/evops-ml/commit/3b2349b0533077422cf438d2d899902e99765a7c)).
- Issued the tags as they become available
  ([commit](https://github.com/evops-sum25/evops-ml/commit/3b97033cd175c5b844bf51614e17908a557a7268)).

#### Ramil Shakirzyanov

- Tested ArgosTranslate-based NMT approach
  ([commit](https://github.com/evops-sum25/evops-ml/commit/922e9da7f8418c973664fc772d8e5162049ab602)).
- Tested LLM-based NMT approach
  ([commit](https://github.com/evops-sum25/evops-ml/commit/06a5a5e87d5f9c1fb5dff3e602e1e09a77e97fe3)).
- Switched the auto-tagger model to half-precision
  ([commit](https://github.com/evops-sum25/evops-ml/commit/27136df42cd23037d4d55d0c271f5b2b7be07338)).

## Plan for Next Week

### DevOps

- Finish domain setup.

### Machine Learning

- Implement the machine translation service class.
- Review the models’ work.

### Back End

- Implement the new endpoints.

### Android

- Update the Create Event screen to include new fields: location, date & time
  (depends on the back end).
- Integrate new fields into the Event Details screen (depends on the back end).
- Implement functional search on the Event List screen (depends on the back
  end).
- Add form validation to the Event List screen.

### Website

- Add a PWA.
- Implement event searching.
- Integrate the ML capabilities.
- Improve the layout.

## Confirmation of the Code’s Operability

We confirm that the code in the `main` branch:

- [x] Is in working condition.
- [x] Runs via Docker Compose.
