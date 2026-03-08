---
title: "Week #4"
---

# **Week #4**

## Testing and QA

For the quality assurance, we made an automated build for our project that is activated on each push. 

### Evidence of test execution

![The pipeline](https://github.com/user-attachments/assets/0d783799-d895-420f-ada2-b781d4883194)

## CI/CD

### Tools we used

- [setup](https://github.com/bscotch/igor-setup)
- [build](https://github.com/bscotch/igor-build)

### Challanges 

- Making an automated build for the Gamemaker project was quite hard and demanded a lot of time

### Links to CI/CD configuration files

- [yml file](https://github.com/evolutionleo/Capstone-2025/blob/main/.github/workflows/ci.yml)

## Deployment

### Staging

Each push is going through the build pipeline, so if is not successful, we would not authorise the merge requests. 

### Production

Release builds meant for publishing are compiled on our developer's machine locally for now. This is to ensure optimal build settings.

## Vibe Check

- We still have some problems with organisation and the general mood of the team
- Some people are not satisfied with their roles and the need to make something creative under the deadlines, so we need to create a more comfortable environment
- Some members are still not present with a legal reason, so the communication is not as good as it could have been


# Weekly commitments

## Individual contribution of each participant

- Dmitry Korletynu: 
    - team organization
- Lev Ivanov: 
    - [implemented the jump pad](https://github.com/evolutionleo/Capstone-2025/commit/f87ae6975b138383e6859962171e3fbec4c26794)
    - [implemented death handling](https://github.com/evolutionleo/Capstone-2025/commit/92561e12d49579750ca4c13ae5b398e4827aff13)
    - [automated build](https://github.com/evolutionleo/Capstone-2025/commit/122a3e6749c0c37610680dd2484872aecd67874b)
- Ulyana Yanovitskaya: 
    - [worked on characters ("персонажи" field)](https://docs.google.com/document/d/1Ul-d97mPKF-ZTrO-CHl08b0JdEY6rSsgcE8PJKCeIiA/edit?tab=t.fepdcfwihw9p#heading=h.jrms3cqlaruf)
- Veronika Levasheva:
    - this report
    - [wrote all dialogues for the first level and for the start of the second one (lvl1 and lvl2 fields)](https://docs.google.com/document/d/1Ul-d97mPKF-ZTrO-CHl08b0JdEY6rSsgcE8PJKCeIiA/edit?tab=t.5t03903ai246)
- Bulat Shigapov:
    - [made new backgrounds](https://docs.google.com/document/d/18_2sXF0mWBhaDnU7dNCTDwzn7qXZSNZqnLJ529hH1vs/edit?usp=sharing)

## Plan for Next Week

### Things to code

- put the second level together

### Narrative and level design

- formulate the level design for the second level
- finish writing the second level dialogues

### Visual Design

- make the backgrounds for the next scenes 
- design objects for interaction
- animate objects for interaction

### Organisation

- group call to discuss the process
- keep consistent chat communication

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
