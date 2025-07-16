
---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

#### Session 1 – Pavel, 22, Student & Amateur Powerlifter  
Pavel uses a notebook to track his workouts and was excited about digitizing the process. He appreciated the clean UI and the ability to log sets with weight and reps. However, he mentioned it would be useful to have templates for common workout routines (e.g., push/pull/legs).

> *“I like that it’s simple and fast. I would use it at the gym, but I wish I could quickly reuse my previous workouts.”*

#### Session 2 – Olga, 27, Fitness Trainer  
Olga works with clients and tracks their workouts manually. She liked the idea of having client profiles and the ability to see progress over time. She pointed out the lack of a progress graph or statistics dashboard as a major limitation.

> *“If I could track how my clients improve — that would be a game-changer. Graphs, stats, maybe even exporting to PDF.”*

#### Session 3 – Timur, 19, Gym Newbie  
Timur recently started training and was confused by some of the terminology in the interface. He asked for an onboarding tutorial and simple explanations for each field. He also wanted motivational features like badges or personal best tracking.

> *“It’s cool but a bit hard to understand at first. What’s a set vs workout? Maybe add a beginner mode or hints.”*

---

### Analyze
Based on user feedback, we identified the following issues and prioritized them:

1. **Lack of reusable workout templates** – High Priority  
   Many users want to repeat their past workouts or follow a fixed routine.

2. **No progress visualization** – High Priority  
   Users (especially trainers) expect to see graphs or reports of progress.

3. **Missing beginner support/onboarding** – Medium Priority  
   Important for increasing adoption among less experienced users.

4. **No motivational elements** – Low Priority  
   Badges and achievements could increase user retention but are not essential at this stage.

---

## Iteration & Refinement

### Implemented features based on feedback

We plan to implement this features on the next week:
- Ability to copy previous workout sessions.
- Improve field descriptions and added tooltips for beginners.
- Prepare mockup for progress tracking.

---

### Performance & Stability

- **App load time**: measured using browser dev tools – currently ~1.2s.
- **Database query time**: measured via logging – most queries under 100ms.
- **Error rate**: monitored through console logs – < 1% over 100+ test sessions.

Next step: integrate Sentry or another monitoring tool for real-time error tracking.

---

### Documentation

- `README.md`: setup and run instructions using Docker Compose.
- `Backend Swagger`: describes API endpoints and expected request/response format.
- Inline code comments to explain important logic.
- Planned: user guide with screenshots and example flows.

This ensures that both developers and testers can easily navigate the codebase and deploy the system.

---

# Weekly commitments

## Individual contribution of each participant

Ivan Chabanov:
- Added tests for project (sql, entities)
- Added Database Logic
- Added activity method on mobile
`https://github.com/IU-Capstone-Project-2025/gym-genius/commit/daa9bdb12066c43c207f504450bcbdabe61c018d
https://github.com/IU-Capstone-Project-2025/gym-genius/commit/ec94804813300d7560910f0e6e17e3617937fe7d
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/35/

Aleksandr Mikhailov:
- Add method to get users with pagination
- Fix swagger annotations (update exercise endpoint)
- Add static exercise info jsons and images
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/26

Nosov Kirill:
- Added method for getting all users
- Updated swagger for this new method
- Ensured that the new API methods are properly documented and maintainable for future development.
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/27

Egor Dushin:
-   filtering
-   ban/unbain
-   checking information about the user/subscription status/user activity withing the last month
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/28

Vlad Kuznetsov:
- Setup domens and nginx - api.говно.site  admin.говно.site
- Setup logging
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/29
https://github.com/IU-Capstone-Project-2025/gym-genius/pull/30

## Plan for Next Week

- Implement basic progress chart using existing workout data.
- Add ability to save custom workout templates.
- Deploy preview version to staging server for internal testing.
- Collect more feedback with embedded form.

---

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
