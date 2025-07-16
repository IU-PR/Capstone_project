---
title: "Week #6"
---

# **Week #6**

## Links

*Specify here all the necessary links to your website, application installer, final demo, etc.*

* **Deployment**: [http://localhost:3000](http://localhost:3000)
* **API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

## Final deliverables

### Project overview

**EasyTravel** — a web platform for semantic search and personalized recommendations of interesting places.
The backend is built on FastAPI and provides authentication, user profile management, search, and recommendations based on interests.
The frontend, built with Next.js, allows users to register, view recommendations, and save favorite places.

### Features

* User registration and authentication with JWT.
* Updating profile data: city, interests, additional interests, and “about me” section.
* Saving and retrieving favorite POIs via `/api/user/favorites`.
* Retrieving main user interests via `/api/user/interests`.
* Semantic search and recommendations based on interests and city.
* Docker environment for deploying backend, frontend, and database.

On the frontend:

* Redesigned and simplified interface — unnecessary elements and buttons removed, more logical and user-friendly layout.
* Registration button on the login page and login button on the registration page.
* Filter by the user’s top three interests on the recommendations page.
* Saving places to favorites from search and recommendations sections; separate favorites page.
* Displaying results on a map and the ability to edit the profile.

### Tech stack

* **Backend**: FastAPI, PostgreSQL, SQLAlchemy, Pydantic, Docker
* **Frontend**: Next.js, React, Tailwind CSS
* **Data Layer**: FAISS, sentence-transformers
* **Containerization**: Docker & docker-compose

### Setup instructions

1. Clone the repository.
2. Download the FAISS index and embeddings as described in the README.
3. Run `docker-compose up --build`.
4. The API will be available at [http://localhost:8000](http://localhost:8000), and the frontend at [http://localhost:3000](http://localhost:3000).

## Presentation draft

https://drive.google.com/file/d/1DY7Ny9v5GjEwwwC2ug1XtN7rus8WGT2i/view?usp=sharing

# Weekly commitments

## Individual contribution of each participant

* **Emil Goryachih – backend:**

    * Implemented user profile update functionality.
    * Added endpoint for saving and retrieving user’s favorite places.

    https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/616a8b565feda6d9f9cb6bfc7f3408ac79ead589
    https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/604d6f5422022813191c424e32540d1204fff90b

* **Said – frontend:**

    * Redesigned authentication pages, simplified interface, and removed unnecessary buttons.
    * Implemented map view for places, saving to favorites, and a favorites page.
    * Added change profile functionality      
      https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/3b3fcfdc94f54d40775fd7fd37760545b5395862

* **Vlad – frontend:**

    * Added filter by interests on the recommendations page.
    * Redesigned interface: removed redundant elements, implemented profile editing, and tags on pages.
      https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/1ac655163f5f734dfe2da89e54631a0ae995bf34

## Plan for Next Week

* Perform final testing and fix any potential bugs.
* Prepare demo video and presentation.
* Update deployment documentation.

## Confirmation of the code's operability

We confirm that the code in the main branch:

* [x] In working condition.
* [x] Run via docker-compose (or another alternative described in the `README.md`).
