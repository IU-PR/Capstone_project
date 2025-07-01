---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

During the third sprint, the NeuroCoach team successfully developed and delivered a functional MVP that enables a complete end-to-end user journey. The following core features were implemented:

- **Gamified Workout Journey**: Users can progress through workout sessions step by step in an engaging, game-like format. The workout flow includes visual tracking and a level-up system that will serve as a base for future achievements and motivational mechanics.
- **Chat with AI Coach**: Users can interact with the AI assistant to clarify exercise techniques or ask general fitness-related questions. The chat provides real-time feedback based on the user's activity and state.
- **User Profile Management**: Users fill out an onboarding form with personal data (e.g., age, fitness goals, level) which is used to personalize their training experience. This information is stored and retrieved from the database.
- **Personalized Training Plan**: Based on the filled form and AI recommendations, a personalized plan is generated for each user. Users can regenerate the plan based on their feedback or changing fitness goals.
- **Authorization System**: A secure registration and login system is in place, using JWT-based authorization for authenticated access to personalized features.
- **Progress Tracking and Rating System**: A gamified system tracks user progress and evaluates consistency. This serves as the basis for achievements, competition elements, and adaptive goal-setting in future iterations.

### Functional user journey implemented:

1. A new user registers in the system.
2. The user completes a personal questionnaire (onboarding).
3. The system generates a training plan using LLM responses.
4. The user begins the workout path, completing exercises step-by-step.
5. Progress is tracked and visually updated.
6. The user may chat with the AI coach to clarify technique or submit feedback.
7. Based on this feedback, a new training plan can be generated.

**Relevant PRs/Issues:**
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/16
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/issues/17
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/18
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/19
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/20
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/21
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/22

## Demonstration of the working MVP

Screenshots and videos of the working MVP can be found in the shared document:

- **[Screenshots & Demo Materials](https://docs.google.com/document/d/1GKH65g0w2tS63SKzz-NLyUFZlJydY6h5OzF5j8t8izM/edit?usp=sharing)**

The demo includes:
- Full onboarding and workout path
- Chat interaction with AI
- Progress tracking and plan regeneration features

## LLM

**Model Selected**: Mistral Small 3.2 24B (open-source, free to use)

**Integration details**:
- Integration with the LLM model has been successfully completed.
- AI requests were engineered using 

**Prompt Engineering** techniques for workout generation and contextual chat replies.
- Model selection was conducted after evaluating existing free LLMs for performance, context length, latency, and capability to understand fitness-related prompts.
- The chosen model was integrated into the backend with a mockable layer to enable testing and future substitution.

**Use cases**:
- Generating training plans personalized to user profile data
- Regenerating plans based on subjective feedback ("I'm tired", "This was too easy")
- Chat-based clarifications ("What is deadlift?", "How to stretch after workout?")

## Internal demo

An internal demo was conducted with the entire team participating. The following notes were captured:

- The MVP is functional and covers the full user journey from onboarding to AI-assisted training.
- No critical bugs were identified, but UX improvements were suggested:
  - Add smoother transitions between workout steps
  - Clarify the placement of the AI chat button
  - Improve visual cues when plan is being regenerated
- Backend services responded stably under test loads.
- LLM responses were contextually accurate, although some generic answers were flagged for improvement.

# Weekly commitments

## Individual contribution of each participant

**Mariia Nikolashina**
- Conducted solution interviews to validate user loyalty and draw conclusions to improve product-market fit.
- Implemented user progress tracking and a rating system based on user consistency.
- Updated API documentation.
- Synchronized backend integration with both mobile and frontend developers through planned sync meetings.
- Performed integration of frontend and backend, resulting in a fully functional MVP.
- Led the sprint retrospective and summarized improvement areas.
- Added a one-command backend launch script for streamlined development.

https://docs.google.com/document/d/1i7nXwaFUiTwG9h0q_EPWk0NXzP8sQXj_b6-5DwWmKkQ/edit?usp=sharing

https://docs.google.com/spreadsheets/d/1x4WTPxLsZnhnjLXQXuvY_Tfj6heq2VUT8Rl-fEodgT0/edit?usp=sharing

https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/19

https://github.com/IU-Capstone-Project-2025/NeuroCoach/blob/main/docs/rest-api.md

**Maxim Oleynik**
- Implemented AI-based training plan generation logic.
- Integrated plan regeneration based on user feedback and preferences.
- Collaborated with frontend and mobile developers during sync meetings to ensure alignment.
- Contributed to the successful MVP integration and participated in sprint retrospective.
- Participated in backend code reviews for quality assurance.

https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/21

**Danil Fishchenko**
- Fully implemented integration with the chosen LLM model.
- Conducted comparative analysis of free LLM models and justified the selection of Mistral Small.
- Developed mobile UI design components based on the agreed prototype.
- Created a Customer Journey Map (CJM) to describe and improve the user flow.

https://www.figma.com/design/ggsx8HjvuNhfUltSbONPfu/Untitled?node-id=0-1&t=CN432rmJ0ESmdEj7-1

https://github.com/IU-Capstone-Project-2025/NeuroCoach/blob/main/apps/rest-api/AI_MODELS.md

**Mark Petrov**
- Led sprint review and internal MVP demo presentation.
- Monitored and verified sprint progress against defined goals.
- Conducted market analysis and researched growth potential of the project.
- Carried out a competitor analysis aligned with the prototype to benchmark feature set and identify differentiators.

https://docs.google.com/spreadsheets/d/1k-b3tZIzNAhxXYmuCIed6HkwW6t28aK6Q5HRbdlhHCc/edit?usp=sharing

https://docs.google.com/document/d/19S7zju2yutqEot-EkVBD44lH6cuHXEJgWQgFRDT-djY/edit?usp=sharing

**Klimentii Chistyakov**
- Developed Flutter app with fully implemented and integrated functionality of login/registration, chat with AI, Duolingo-like path progression, profile view/edit, as well as minimalistic app settings
- Integrated with backend endpoints and tested user flow on mobile.
- Implemented state management and navigation logic using Bloc and MVVM.
- Collaborated with Mariia on API testing for mobile flows.

https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/22

https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/20

**Saidaziz Kadirov**  
Said:
- Connected the frontend dashboard with real backend data.
- Implemented workout and progress visualization components.
- Fixed layout issues on multiple screen sizes.
- Built regeneration request UI and connected it to the LLM endpoint.

## Plan for Next Week

- Improve user flow based on demo feedback (e.g., button clarity, transitions).
- Expand gamification: add initial achievements and milestone markers.
- Improve contextual LLM prompts based on edge cases found in demo.
- Conduct early user tests outside the team and collect structured feedback.
- Prepare presentation materials for demo.
- Polish mobile responsiveness and cross-platform compatibility.
- Increase code quality, add unit tests, conduct load tesing

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
