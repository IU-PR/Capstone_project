# Week #2

## Detailed Requirements Elaboration

### 1. Profile Screen
- The user must see up-to-date preference data (goal, gender, size, height, age, weight).
- Data is fetched from the server and cached locally using ObjectBox.
- When switching users, the local cache is cleared to prevent showing another user’s data.
- The UI must support multilingualism (Russian and English).
- Navigation to individual screens for editing each preference is implemented.

### 2. Product Storage Screen
- The screen should display the user’s product list.
- Support filtering and sorting options.
- Data is fetched from the backend and then saved to the local database.

### 3. Try-On and Outfits Screens
- Try-On screen should allow virtual clothing fitting with overlaying 3D models.
- Develop a 3D human body model for more accurate fitting.
- Outfits screen should display recommended clothing sets.

### 4. Backend
- Implement APIs for fetching and updating user preferences.
- Ensure data security via authentication and authorization.
- Support multilingual content.

### 5. Technologies and Tools
- Flutter for frontend development.
- ObjectBox for local caching.
- HTTP REST API for server communication.
- Flutter Bloc for state management.

---

## Prioritized Backlog

| Priority | Task                                                  | Area      | Assignee         | Status       |
|----------|-------------------------------------------------------|-----------|------------------|--------------|
| High     | Finish the Profile screen                             | Frontend  | Aleksandr        | In Progress  |
| High     | Continue working on Product Storage Screen            | Frontend  | Ilya             | Planned      |
| High     | Implement required backend functions to support frontend | Backend | Ilya             | In Progress  |
| Medium   | Start implementation of the Try-On Screen             | Frontend  | Ilya, Aleksandr  | Planned      |
| High     | Start implementation of 3D-model of human body        | ML / 3D   | Nikita           | Planned      |

---

## Project Specific Progress

### Frontend
- Changed design of register and login screens.
- Added setup screen for setting preferences during registration.
- Fixed long loading preferences bug.
- Added localization into Russian and English languages.

### Backend
- Changed registration logic and logic for fetching preferences a little bit.

---

## Weekly Commitments

### Individual Contribution of Each Participant

**Aleksandr Gavkovskii**  
- Developed new UI for registration and login screens.  
- Added setup screen for setting preferences during registration.  
- Added localization into Russian and English languages.

**Ilya Maksimov**  
- Fixed long loading preferences bug.  
- Changed registration logic and logic for fetching preferences a little bit.

**Nikita Shiyanov**  
- Rewrote the backend from TypeScript to Python.  
- Added migrations using Alembic.  
- Started exploring the MakeHuman code.
- Thought about the database architecture
---

## Plan for Next Week

### Frontend
- Continue working on the screen for product storage.
- Start working on try-on and outfits screens.
- Finish profile screen.

### Backend
- Add necessary functions for frontend.

### ML / 3D
- Start implementation of 3D-model of human body.

---

## Confirmation of the Code’s Operability

We confirm that the code in the main branch:
- Is in working condition.
- Can be run via `docker-compose` (or another alternative described in the `README.md`).
