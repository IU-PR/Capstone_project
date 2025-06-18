---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

### Detailed User Stories

| Initial User Story | Expanded User Stories |
|--------------------|-----------------|
| As a freelancer with shifting project loads, I want to rearrange or skip roadmap steps, so that I can fit my learning into a dynamic schedule without losing overall progress. | - As a user, I can manually reorder steps in my roadmap.<br>- As a user, I can skip or mark steps as complete/incomplete.<br>- As a user, I can view overall progress regardless of the order I complete steps. |
| As a busy professional, I want to input my goals, current skill level, and available time in one place, so that I can receive a clear, personalized study roadmap without spending hours researching. | - As a new user, I can quickly create a profile with basic details.<br>- As a user, I can select or enter my desired skill/goal with free text.<br>- As a user, I can describe my current skill level using a simple interface.<br>- As a user I want to highlight the skills I want to focus on, so I get a personalised results <br>- As a user, I can specify my preferred study time in hours.<br>- As a user, I receive courses I can go by link to.<br>- As a user, I receive a step-by-step study roadmap based on my inputs. |
| As a budget-constrained learner, I want to set a maximum spend, so that every recommended step fits my financial limits and I don’t encounter hidden costs. | - As a user, I can set a total or monthly budget for my learning roadmap.<br>- As a user, I can see the cost of each recommended step/resource.<br>- As a user, I can filter/exclude paid resources from my roadmap if I want only free content. |
| As a returning user, I want to update my profile and regenerate my roadmap on demand, so that my learning plan always adapts to my evolving goals and circumstances. | - As a user, I can log in and view my saved profile and roadmaps.<br>- As a user, I can update my learning goal, skill level, time, or budget at any time.<br>- As a user, I can regenerate or refresh my roadmap. |
| As a freelancer with shifting project loads, I want to rearrange or skip roadmap steps, so that I can fit my learning into a dynamic schedule without losing overall progress. | - As a user, I can manually reorder steps in my roadmap.<br>- As a user, I can skip or mark steps as complete/incomplete.<br>- As a user, I can view overall progress regardless of the order I complete steps. |
| As a user, I want to export or copy my personalized roadmap (course titles + links), so that I can save or share it outside the platform. | - As a user, I can copy my roadmap (with titles & links) to clipboard.<br>- As a user, I can download my roadmap as a PDF, CSV, or text file.<br>- As a user, I can share my roadmap via a shareable link. |

### Key user stories for MVP and their acceptance criteria

| User Story                                                                                        | Acceptance Criteria                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a user, I can select or enter my desired skill/goal with free text.                            | Given I am in the chat interface, when the system asks about my learning goal, then I can write the answer in the free-form.                |
| As a user, I can describe my current skill level with free-form text                              | Given I am in the chat interface, when the system asks about my knowledge, then I can write the answer in the free-form.           |
| As a user, I want to highlight the skills I want to focus on, so I get a personalised results     | Given I have entered my skills, when I submit them in the chat, then I receive a list of recommended courses that include the skills I provided.                         |
| As a user, I receive courses I can go by link to.                                                 | Given I have answered the system questions, when I view my personalized recommendations, then each step/resource contains a course title, a brief description, and a direct link that opens the course in a new tab or window.  |
| As a user, I can see all necesary information for each recommended step/resource.                 | Given I view my recommended courses, when I review each course, then the title, duration, difficulty, price, enrolled students, authors and rating are clearly displayed.                                                  |
| As a user, I can specify my preferred study time in hours.                                        | Given I am creating my request for a roadmap, when I am prompted for time commitment, then I can enter the number of hours per week I want to spend studying, and this is used to inform the pacing of my roadmap.                                      |
| As a user, I can download my roadmap as a PDF, CSV, or text file.                                 | Given I have a course list generated and visible, when I click a download button, then I am prompted to download my courses in my chosen format (PDF, CSV, or text).           
| As a user, I can skip steps or mark them as complete/incomplete.                                  | Given I have a course list generated and visible, when I interact with the steps via checkboxes, then I can mark a step as complete, incomplete, or skipped, and the status is visually updated and saved for future sessions.        
| As a user, I can filter/exclude paid resources from my roadmap if I want only free content.       | Given I have a course list generated and visible, when I select an option to exclude paid resources, then my cource list is regenerated to show only free resources         

### Prioritized backlog

Private acces to click-up: https://app.clickup.com/9015876757/v/s/90155186012


_write to product manager's Telegram @oELYAo (Lana Ermolaeva) if you have access issues_


#### View sugesstions:

List: "Closed" -> enable "Tasks" & "Substasks"

Board: "Filter" -> "Task type" is "Task"; change "Subtasks" to "Separate"

## Project specific progress

### Design

- Made design for core pages (main and chat)
- Developed basic user flow diagram

### Frontend

- Implemented components and pages (main and chat page)
- Implemented basic routing


### Backend

- Implemented search endpoint
- Implemented get course endpoint
- Implemented popular course endpoint

### ML

- Implemented encoder & Qdrant services (no caching)

### DevOps

- Changed Docker to Uvicorn


# Weekly commitments

## Individual contribution of each participant

| Team Member                         | Telegram Alias    | Email Address                        | Track                                   | Responsibilities                                                                                                                                                                                                                                                        |
|-------------------------------------|-------------------|--------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lana Ermolaeva (lead)               | @oELYAo           | l.ermolaeva@innopolis.university     | Project and Product Management           | Backlog: https://app.clickup.com/9015876757/v/s/90155186012; report writing                                                                                                                                                |
| Adilya Saifetdiarova                | @sayfetik         | a.saifetdiarova@innopolis.university | Front-end and UX/UI design               | Design: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/tree/master/assets/week2/, Frontend:  https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/3|                                                                                         |
| Ivan Ershov                         | @spiritonchiс     | i.ershov@innopolis.university        | ML                                       | Encoder & Qdrant, upload courses: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/4                                                                                                                             |
| Bulat Gazizov                       | @BulatGazizov0    | b.gazizov@innopolis.university       | Back-end working with Front-end, DevOps  | Encoder & Qdrant, vector search services: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/4; update readme: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/5/commits|
| Arthur Popov                        | @ee_boooy         | ar.popov@innopolis.university        | Back-end working with ML, MLOps,         | Endpoints: https://github.com/IU-Capstone-Project-2025/SkillsNavigator.ai/pull/5/commits                                                     |


## Plan for Next Week

Fully implement backend needed for MVP, implement all user stories: fullfill backlog & complete tasks 

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose (or another alternative described in the `README.md`).
