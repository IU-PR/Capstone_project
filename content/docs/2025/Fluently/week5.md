---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

<!-- _Conduct at least three sessions with potential users, describe detailed user reviews here (potential users should NOT be your team members)._ -->

- _It will be greate to customize personal lessons plan from settings_
- _The design of the app is pretty simple and looks good. But i think that it will be good to add picture to the background corresponding to the learning goal_
- _The word database is huge and really helpful, but more variety in exercises would make lessons even better_
- _It will be good to add pronounce training to words from dictionary and custom lessons for words from non-learned group_
- _Loggin system is simple, but i think that it will be good to add other services for loggin_

### Analyze

<!-- _Describe the important points that you received from the user feedback, what issues and with which priority you created._ -->

- The customization of the lessons will be added to profile as soon as possible
- Since some models of the lessons are not made yet, we are going to implement them at the next week
- The idea of the repeating words from dictionary is good one, we will discuss about it

## Iteration & Refinement

### Implemented features based on feedback

- Discuss profile settings that we will have
- Discuss exercise versions
- Discuss word repeatitions

### Performance & Stability

<!-- _How would you measure the performance of your application? Calculate the metrics that are suitable for your project and find out if they can be improved in any way, if necessary._ -->

```
==================================================
📊 IMPORT STATISTICS
==================================================
⏱️ Duration: 1h24m43s
🚀 Speed: 6.8 rows/second
📄 Total rows processed: 34743
📝 Words imported: 34743
🏷 Topics created: 570
💬 Sentences added: 172060
❌ Errors encountered: 106
```

### Documentation

<!-- _Describe what types of documentation you have in your project, and why exactly are they?_ -->

[Project README](https://github.com/FluentlyOrg/Fluently-fork/blob/main/README.md)

[iOS README](https://github.com/FluentlyOrg/Fluently-fork/blob/feature/screens/calendar/ios-app/README.md)\
[Thesaurus README](https://github.com/FluentlyOrg/Fluently-fork/tree/main/analysis/thesaurus)\
[CONTRIBUTION.md](https://github.com/FluentlyOrg/Fluently-fork/blob/main/CONTRIBUTING.md)

[All docs](https://github.com/FluentlyOrg/Fluently-fork/tree/main/docs)

### ML Model Refinement

<!-- _If applicable: Describe the process of improving the quality of your ML model, how you managed to achieve this and how you plan to improve it further._ -->

**Thesaurus**

- 3.5 MB RAM
- 7.5 ms per request
- VRAM: 0.55 GB

# Weekly commitments

## Individual contribution of each participant

### Danila Kochegarov (Team Lead & Backend Developer)

- Fixed filling script
- Continue developing telegram bot functionality
- Fixed issues with lesson
- Connect ML with backend
- Integrate ML into database filling
- Wrote script that access website with word transcription for filling database

### Savva Ponomarev (iOS Developer & Project Manager)

- Wrote report
- Add navigation bar and new screens:
  - Calendar with statistic of the lessons
  - Statistic screen with information about progress
- Integrate new endpoints from backend to app
- Started to work with cahcing info

### George Selivanov (System Analyst)

- I found and tested many different llm
- Tested for specific requests for working with English in dialog format
- Wrote a fault-tolerant microservice for interaction with the service for selected models of the groq and gemini service

### Timofey Ivlev (DevOps Engineer)

- Dockerized Thesaurus & llms API. It is accessible in production by: http://10.243.92.227:8002/docs
  PR: https://github.com/FluentlyOrg/Fluently-fork/pull/202
- Added disk clean up script in CI/CD.
  PR: https://github.com/FluentlyOrg/Fluently-fork/pull/201
- Added feature for CI/CD to publish and pull most heavy images from docker hub.
  Issue: https://github.com/FluentlyOrg/Fluently-fork/issues/179
  Our docker hub repository: https://hub.docker.com/repositories/fluentlyorg
- Fixed problem with directus - in docker file it had wrong env variables for redis which caused directus crashes.  
  PR: https://github.com/FluentlyOrg/Fluently-fork/pull/204

### Anton Korotkov (ML Engineer)

- Improving the distractors creation: now supports different forms of words
- Fixed random errors occuring during working of NLP module.

### Daniil Tskhe (Backend Developer)

- Wrote the logic for saving the user's progress after the lesson
- Fixed the paths for the router
- Fixed auth logic and models creation error (user pref before user = error, same with sentence before word = error). Very important for database, where we need to see right relationship

### Evgeniy Bortsov (Android Developer)

- Statistic screen
- Statistic calculation locally
- Fix routing between Home screen and lesson screen
- After lesson the result sending back to the backend

## Plan for Next Week

- Complete any remaining high-priority features or bug fixes
- Ensure all code is well-commented and clean
- Documentation Finalization: Ensure README.md is comprehensive (project overview, features, tech stack, setup instructions,
  deployment link)
- Presentation Preparation: Develop slides covering the problem statement/solution, target audience, key features/tech stack, live
  demo, challenges, future work, team contributions
- Finalize API documentation

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
