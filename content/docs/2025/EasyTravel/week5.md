---
title: "Week #5"
---

# Week #5

## Feedback

### Sessions

We conducted three sessions with potential users. Each session lasted about 20 minutes and included a demonstration of the app followed by a discussion of the user experience.

**User feedback:**

* **User 1:**

    * Liked the simplicity of the search.
    * Would like to see more filters (e.g., by price and opening hours).
    * Found the personalized recommendations very useful.

* **User 2:**

    * Requested the ability to save favorite places.
    * Pointed out the need to improve the visual design of the recommendations list.

* **User 3:**

    * Liked the app’s responsiveness (speed of loading recommendations).
    * Wanted to see other users’ reviews and ratings.

---

### Analysis

Based on the user feedback, we identified the following key issues and their priorities:

| Issue                                          | Priority |
| ---------------------------------------------- | -------- |
| Ability to save favorite places                | Medium   |
| Addition of filters by price and opening hours | Low      |
| Implementation of user reviews and ratings     | Low      |

---

### Performance & Stability

We measured performance and stability using the following metrics:

* **Search response time (latency):**

    * Average search execution time is **0.4 ms** (FAISS IVF-PQ).
* **Precision\@5 and Precision\@10:**

    * Precision\@5 ≈ **84%**
    * Precision\@10 ≈ **80%**
* **Query encoding time (encode latency):**

    * Average ≈ **92 ms** (CPU).

Latency is already very good; in the future, we can further improve encoding time using a GPU or lighter models.

---

### Documentation

The project includes the following documentation:

* **README.md:** Main instructions for running and configuring the app (Docker, Docker Compose, environment variables, frontend startup).
* **Swagger API docs:** Interactive documentation of the FastAPI endpoints.
* **Experimental documentation** (`experiments/README.md`): Description of the experiments conducted, metrics, and reproduction instructions.

Each of these documents is intended to ease development and maintenance of the project and to facilitate onboarding of new team members.

---

### ML Model Refinement

We conducted additional experiments comparing different embedding models:

* Compared the embedders **LaBSE**, **MiniLM-L6**, and **MiniLM-L12**.
* LaBSE achieved the best results (Precision\@5 ≈ 84%).
* Planned future improvements include fine-tuning on our domain and implementing a feedback loop with real users.

---

# Weekly Commitments

## Individual Contributions

* **Emil Goryachih:**

    * Conducted user interviews and processed feedback.
    * Prepared the application setup documentation.
    
  https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/64b1a846560f63a84ddf3d85dc047af227b2ae53

* **Vlad Galkin:**

    * Conducted user interviews and processed feedback.
    * Enhanced the frontend (backend integration).
    * Implemented the save-recommendations feature.
    * Added a profile page.
  
  https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/2b809b9ef85d451dde3c8482134d2e9ae7ba67d2
  https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/15ad0fae25442a9f5f4fb7afc9caf14e33aef380

---

## Plan for Next Week

* Implement additional search filters (by price and opening hours).
* Explore integration of user reviews and ratings into the app.

---

## Confirmation of Code Operability

We confirm that the code in the main branch:

* [x] Is in working condition.
* [x] Runs via Docker Compose (or another alternative described in `README.md`).
