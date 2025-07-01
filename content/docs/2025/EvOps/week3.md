---
title: "Week #3"
---

# **Week #3**

## Implemented MVP Features

### Back End

For now, our back end provides these features:

- REST & gRPC APIs powered by Axum and Tonic, fully documented with Swagger and
  Protobuf doc-comments
  [(PR)](https://github.com/evops-sum25/evops-backend/pull/27).
- Data storage in the PostgreSQL DBMS using Diesel as the driver (code).
- An extension for clients (front ends) to locally run functions that don’t
  require state ([repository](http://github.com/evops-sum25/evops-client-ext)):
  - Functions are exported as
    [UniFFI](https://mozilla.github.io/uniffi-rs/latest/) bindings
    ([code](https://github.com/evops-sum25/evops-client-ext/blob/main/crates/evops-uniffi/src/lib.rs))
    and [Extism](https://extism.org/)/WASM plugins
    ([code](https://github.com/evops-sum25/evops-client-ext/blob/main/crates/evops-extism/src/lib.rs)).
  - We expose a Markdown parser
    ([code](https://github.com/evops-sum25/evops-client-ext/blob/main/crates/evops-markdown/src/lib.rs))
    and validation functions (above).
- Basic operations – Create, find, and list entries.
  [(issue)](https://github.com/evops-sum25/evops-backend/issues/14).
- Still missing: authentication, image storage, update/delete operations, and ML
  features.

### Android

- Core screens implementing existing CRUD back end operations:
  - Event List screen
    ([commit 1](https://github.com/evops-sum25/evops-android/commit/f08f52a2fb97059e5f59b040019811ddc9e42750),
    [commit 2](https://github.com/evops-sum25/evops-android/commit/27d09c6719a33a40718f65a1d1c646a3064dc594)):
    here users can scroll the feed to explore events.
  - Event Details screen
    ([commit 1](https://github.com/evops-sum25/evops-android/commit/efd8b820ddabe88ef1ef87cbe1a2d147db472252),
    [commit 2](https://github.com/evops-sum25/evops-android/commit/423ad787882cc43d4a176855708984ce178ba995)):
    here users can see all the information related to the event, which is not
    fully presented on the Event List screen (e.g. scroll all the event images
    (if there is more than one), read full description, see all the tags
    associated with an event…).
  - Create Event screen
    ([commit](https://github.com/evops-sum25/evops-android/commit/f8097fe4b294382c8ada9841f6243073040e1329)):
    here user fills the form to create an event and submit it (for now the form
    is simple: it contains only fields for title and description, and switch to
    manage the need of attendance; there is also no validation for now).
- Navigation setup
  ([commit 1](https://github.com/evops-sum25/evops-android/commit/4374b0bf7cda61d30ac3d3bdcd960e0adbf5e3f2),
  [commit 2](https://github.com/evops-sum25/evops-android/commit/5de1fb5f93196e83fac406be4773af695ca24bdc)).
- Kotlin, Gradle, Jetpack Compose, Retrofit, Dagger Hilt.
- Still missing: styles, local caching, image posting.

## Demonstration of the Working MVP

- Back end: [http://31.59.170.53:8080](http://31.59.170.53:8080) (both REST and
  gRPC).
- Website: [http://31.59.170.53:3000](http://31.59.170.53:3000).
- ML server: [http://31.59.170.53:50051](http://31.59.170.53:50051) (should not
  display anything (gRPC without reflection)).

The Android app can be downloaded from here:
[https://github.com/evops-sum25/evops/releases](https://github.com/evops-sum25/evops/releases).

Screenshots:

- https://drive.google.com/file/d/18AWcQbfZHCqu0Q35_FBVIY3Y-d_zP9WG/view
- https://drive.google.com/file/d/1ZKKAVcJOimGXX1GKDohP9tSdHr0klJ4d/view
- https://drive.google.com/file/d/1cODQdz2NQEBy68vigHTTucgbQSuzpIpe/view

## ML

Pre-trained models are used without additional training:

- **sentence-transformers/paraphrase-multilingual-mpnet-base-v2** for text
  vector representations (recommendation system).
- **sileod/deberta-v3-base-tasksource-nli** for zero-shot classification
  (auto-tagging).

The dump of the “[Opportunities For You](https://t.me/opportunitiesforyou)”
telegram channel was used for auto-tagging testing and for building artificial
profiles for the recommendation system.

The auto-tagging system does not require any parameters as a zero-shot
classifier. The recommendation system has the following parameters:

- The preliminary set of users’ interaction weights has the following form:
  - `"commented": 1.3`.
  - `"upvoted": {True: 2, False: -0.5, None: 1}`, where True means that the user
    upvoted a post, False means that the user downvoted, and None means that the
    user does not mark it.
  - `"attended": 2.0`.
  - Initially, users can post reactions on posts. We have divided them into 3
    groups as follows:
    `"reactions": {ReactionType.GOOD: 1.2, ReactionType.NEUTRAL: 1, ReactionType.BAD: -0.8}`.

  According to these weights, the “good\_profile” and “bad\_profile” are
  constructed. “good\_profile” is an average vector of embeddings of events that
  were evaluated positively, and “bad\_profile” is an average vector of
  embeddings of events that were evaluated negatively.

- To compute the users’ profiles, the following formula is applied:
  `profile = good_profile - \lambda * bad_profile. \lamda = 1`.

All the values were chosen empirically. Further, they will be tuned.

Artifacts:

- [Embeddings model](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2)
- [Model for auto-tagging](https://huggingface.co/sileod/deberta-v3-base-tasksource-nli)
- [Systems code](https://github.com/evops-sum25/evops-ml/tree/main/notebooks)

## Internal demo

_Notes from internal demo_

## Weekly Commitments

### Individual Contribution of Each Participant

#### Aleksandr Isupov

- Created the logic of the Event Details screen
  ([commit](https://github.com/evops-sum25/evops-android/commit/423ad787882cc43d4a176855708984ce178ba995)).
- Completely implemented the Create Event screen with all the possible postable
  fields for now
  ([commit](https://github.com/evops-sum25/evops-android/commit/f8097fe4b294382c8ada9841f6243073040e1329)).
- Researched how to work with type-safe navigation in Jetpack Compose
  ([article](https://developer.android.com/guide/navigation/design/type-safety),
  [video](https://www.youtube.com/watch?v=qBxaZ071N0c&ab_channel=PhilippLackner)).
- Configured type-safe navigation
  ([commit 1](https://github.com/evops-sum25/evops-android/commit/4374b0bf7cda61d30ac3d3bdcd960e0adbf5e3f2),
  [commit 2](https://github.com/evops-sum25/evops-android/commit/5de1fb5f93196e83fac406be4773af695ca24bdc)).
- Resolved an issue with images not loading
  ([commit](https://github.com/evops-sum25/evops-android/commit/0d18cc73ab09acc80eebcf0491706c6359ba68fc)).

#### Arsen Galiev

- Created mobile layout for event list page
  ([commit](https://github.com/evops-sum25/evops-website/commit/edbc3be19ba309c97d7a32e05e2673d8e9697191)).
- Connected the website with the back end via gRPC
  ([commit](https://github.com/evops-sum25/evops-website/commit/114030e5bc270cbb7f26bec03c7b082581d5d399)).
- Added a pseudo sign up option
  ([commit](https://github.com/evops-sum25/evops-website/commit/c4f4c406d120a38cafe591445084d9f125fc19b1)).
- Created the desktop layout
  ([commit](https://github.com/evops-sum25/evops-website/commit/2c0591fe9a6f7ef0321422ca1e90f77698252068)).
- Created the create-event page
  ([commit](https://github.com/evops-sum25/evops-website/commit/3c200603f791c7281efde2e635d2f59d6623cc79)).

#### Asqar Arslanov

- Researched data storage solutions, learned
  [how to work with MinIO](https://github.com/minio/minio-rs).
- Documented back-end APIs
  ([commit 1](https://github.com/evops-sum25/evops-backend/commit/95109d3a10fa1f44249dc24b036ddfa752c7689d),
  [commit 2](https://github.com/evops-sum25/evops-client-ext/commit/e9fbc09065fa619746a12c73797a463a3860fb4e)).
- Removed profile pictures from schemas
  ([issue](https://github.com/evops-sum25/evops-backend/issues/32)).
- Unified error handling on the back end
  ([commit](https://github.com/evops-sum25/evops-backend/commit/8b2350b074a69a4eba2b8d3d169a30495e3da27a)).
- Modularized the client extension code
  ([commit](https://github.com/evops-sum25/evops-client-ext/commit/c9b93f8421fdcdc6f4c098dd75a7def6ef7f8231)).
- Exposed data validation functions from the client extension
  ([commit](https://github.com/evops-sum25/evops-client-ext/commit/28ca4fbb990fd574ced82920245b6a9f00e4626c)).
  - Clients (front ends) can use these functions via WASM/FFI to locally
    validate data (e.g. usernames, tag names).
- Implemented the event page on the website
  ([file](https://github.com/evops-sum25/evops-website/blob/main/src/app/events/[id]/page.tsx)).
- Implemented the sign-up form on the website
  ([file](https://github.com/evops-sum25/evops-website/blob/main/src/app/signup/page.tsx)).
- Wrote a script to populate the DB with fake data
  ([repository](https://github.com/evops-sum25/evops-dummy-data)).
- Fixed the problem of the website not building.

#### Egor Pustovoytenko

- Implemented pagination on the back end
  ([commit](https://github.com/evops-sum25/evops-backend/commit/d1696538e76b06636cc68eb74f067ed59330ee0b)).
- Researched ways of interacting with ML (Python gRPC and Python Postgres, Rust
  wrapper, Rust [ML](https://github.com/mladvladimir/rust-sentence-transformers)
  💀).

#### Ilya-Linh Nguen

- Made some fixes and changes on Dockerfiles for better development
  ([commit 1](https://github.com/evops-sum25/evops-backend/commit/1eae26ac30e078b1f438529b22e8bee8e29f226a),
  [commit 2](https://github.com/evops-sum25/evops-website/commit/7f99ab74b49d6bc9ab7179e6968185e0b1efd10a),
  [commit 3](https://github.com/evops-sum25/evops-website/commit/f5c4e4fe48ece4a15e54ddca411d31208cbcc364)).
- Create two android release
  ([release1](https://github.com/evops-sum25/evops/releases/tag/v0.1.0),
  [release2](https://github.com/evops-sum25/evops/releases/tag/v0.2.0))
- Made the deployment of our project to the server (singe server variant).

#### Maksim Ilin

- Migrated and documented the auto-tagging system in a python script
  ([commit](https://github.com/evops-sum25/evops-ml/commit/76ff766bf877c6c6acc88762036e1fcbe6c0282b)).
- A template has been created for the migrated service class of the
  recommendation system
  ([commit](https://github.com/evops-sum25/evops-ml/commit/7d5e329f4180917427a16fe227236cb336dc940c)).
- Found a suitable dataset with users’ interactions for fine-tuning the
  recommendation system
  ([dataset](https://huggingface.co/datasets/yandex/yambda)).
- Reviewed an article about metrics for the recommendation system
  ([article](https://www.evidentlyai.com/ranking-metrics/evaluating-recommender-systems)).

#### Ramil Shakirzyanov

- Tested whether the rec-sys concept works on the artificial user profiles
  ([commit](https://github.com/evops-sum25/evops-ml/commit/0b55e60216e92ab2efcd14b73d85316387e3ec98)).
- Made an approximate evaluation of the model performance via dynamically
  generated relevance simulation
  ([notebook](https://github.com/evops-sum25/evops-ml/blob/main/notebooks/Recommendation_System/1_Recommendation_System.ipynb)).

## Plan for Next Week

### DevOps

- Connect the script that populate the DB with the project to ease front-end
  development.
- Write CI/CD for every submodule.
- Think about the case with multiple servers, if Kuberentes is “must have” or it
  could be replaced with a more elegant and optimized solution.

### Machine Learning

- Discuss the data retrieval from the database with the backend team.
- Transfer the recommendation system model to production.
- Fine-tune hyperparameters for the recommendation system using the
  [Yambda](https://huggingface.co/datasets/yandex/yambda) dataset, relying on
  metrics.

### Back End

- Add pagination
  ([issue](https://github.com/evops-sum25/evops-backend/issues/21)).
- Integrate MinIO ([issue](https://github.com/evops-sum25/evops/issues/30)).
- Make input validation more robust
  ([issue](https://github.com/evops-sum25/evops-backend/issues/24)).
- Generate slugs for events
  ([issue](https://github.com/evops-sum25/evops-backend/issues/13)).
- Implement backend-ml and ml-database connection
  ([issue](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=117081854&issue=evops-sum25%7Cevops-backend%7C35),
  [issue](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=117082306&issue=evops-sum25%7Cevops-ml%7C31))
- Follow our front ends’ orders. 🫡

### Android

- Add styles ([issue](https://github.com/evops-sum25/evops-android/issues/8)).
- Implement image posting if the back end will implement image storage
  ([issue](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=117054899&issue=evops-sum25%7Cevops-android%7C25)).
- Add fields validation on the Create Event screen
  ([issue](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=117054713&issue=evops-sum25%7Cevops-android%7C24)).
- Fix a bug with icon selection in the navigation bar
  ([issue](https://github.com/evops-sum25/evops-android/issues/22)).

### Website

- Communicate with the back end with Connect-Query
  ([issue](https://github.com/evops-sum25/evops-website/issues/7)).
- Add internationalization
  ([issue](https://github.com/evops-sum25/evops-website/issues/3)).
- Design & Create new pages.

## Confirmation of the Code’s Operability

We confirm that the code in the `main` branch:

- [x] Is in working condition.
- [x] Runs via Docker Compose.
