---
title: "Week #2"
---

# **Week #2**

### Prioritized backlog

Link to backlog: https://github.com/orgs/IU-Capstone-Project-2025/projects/2

## Project specific progress

## 🎨 UX/UI

- Project information page 
- University listing interface:
  - Card-based layout
  - Tags for quick navigation
  - Indexed real-time search
- University detail page
- Filters for university search:
  - Region
  - Rating
  - Number of government-funded places
  - Dormitory availability
  - Military education center
  - Faculties
- “Show All” page for full university listings

## 💻 Frontend

- **University List Page**:
  - Full-featured `UniversityPage`
  - Responsive `GridView`  with dynamic card sizing
  - Real-time search filter by university name
  - Filter icon added (functionality stubbed for future updates)

- **University Card Component**:
  - Displays image, name, and rating
  - Image loading errors handled using `errorBuilder`
  - Long names truncated using `TextOverflow.ellipsis`
  - `onTap` action navigates to detail page

- **University Detail Page**:
  - Large cover image
  - University name, rating, location, motto, and description
  - Back button
  - Favorite button (`favorite_border` icon)

- **Demo Grid Screen**:
  - `UniversityGrid` created for previewing card layout.

- **Auth Pages**:
  - `sign_up_page.dart`: User registration form
  - `reset_password_page.dart`: Password recovery page
  - Button colors on auth and landing pages.
  - Navigation bug fixed (registering a new user no longer redirects to login).
  - Logo image and adjusted based on design feedback

## 🛠️ Backend

- **User Authentication**:
  - PostgreSQL connection parameters updated and tested via pgAdmin
  - Container orchestration stabilized

- **Token-Based Authentication**:
  - Access & Refresh tokens generated on login
  - `auth.go` module created:
    - Token generation logic
    - Secret key, expiration time, and encryption algorithm
  - `refresh_tokens` table in the database
  - Token-related DB functions in `database_api.go`.
  - `LoginHandler` updated to:
    - Verify user credentials.
    - Generate and store refresh token.
    - Return token pair in JSON response.

- **Password Security**:
  - Password hashing
  - Improved user validation with email format checks and duplication prevention.

- **New Features (In Progress)**:
  - `main.go`
  - `login.go` endpoint for user registration and DB storage
  - Temporary Docker setup for Go app and DB
  - Flutter-side connection to Go backend via `api_server`

- **Email Verification Flow** (`registration.go`):
  - Email registration
  - Send verification code
  - Confirm code
  - Create password

## 🤖 ML

- **Professions Dataset**:
  - `professions.json` with 100 professions
  - Each entry includes:
    - Description (3–4 sentences)
    - Relevant entrance exams (ЕГЭ)
    - MBTI types
    - Interests, values, roles, workplaces
    - Education level, salary range, and growth outlook
    - Justification provided for each entry

- **Career Test Dataset**:
  - `dataset_career_test.json` to simulate user test data
  - Structure of career-related user profiles

- **Data Validation**:
  - `validation_report_dataset_career_test.txt` confirms correct structure.
  - Python scripts:
    - `generate_dataset.py`: Dataset generation
    - `validate_dataset.py`: Schema and consistency checks

- **Survey and Synthetic Data**:
  - `Анкета профориентации.pdf`: Career survey created
  - `Синтетические_анкеты_профориентации.csv`: Synthetic user answers
  - `Шкалиные_вопросы_MBTI_с_типами.csv`: Data for MBTI-type mapping

# Weekly commitments

## Individual contribution of each participant

**Andruwenko Valery** – Compiled a detailed professions.json file containing 100 professions with descriptions, relevant exam subjects, MBTI types, values, interests, work environments, education levels, salary ranges, and growth potential. Created dataset_career_test.json for testing the career recommendation system, along with a validation report confirming data integrity. Developed and tested two Python scripts: generate_dataset.py for dataset creation and validate_dataset.py for structural validation. Also prepared a career questionnaire in PDF format and generated synthetic user responses in CSV files.
https://github.com/IU-Capstone-Project-2025/Smartify/pull/34

**Chugaeva Mariia** – Created sign_up_page.dart and reset_password_page.dart for registration and password recovery. Fixed button colors on auth and landing pages, resolved a redirect bug during account creation, and replaced the project title with a proper logo image. Updated the logo per feedback. Code is functional. A few interface improvements and crash fixes are still needed to match the latest Figma design.
https://github.com/IU-Capstone-Project-2025/Smartify/pull/39

**Zakirov Karim** – Developed a fully functional UniversityPage displaying a responsive grid of university cards based on universities.json. Implemented real-time search by university name and adaptive card sizing. Created the UniversityCard component showing image, name, and rating with error handling and layout trimming. Implemented navigation to the UniversityDetailPage, which includes detailed university info, hero animation, and a favorite icon. Also built a demo UniversityGrid for previewing cards.
https://github.com/IU-Capstone-Project-2025/Smartify/pull/29

**Mayorov Daniil** and **Antipov Alexey** - Fixed an issue where users were not being saved to the database. Updated PostgreSQL connection settings and integrated pgAdmin for manual data inspection. Docker containers are now synchronized and launch reliably. Implemented access and refresh token generation during login. Created the auth.go module to handle token creation and management, with configured secret keys, expiration time, and encryption algorithm. Added a refresh_tokens table in the database and corresponding functions in database_api.go. The LoginHandler was updated to validate users, generate tokens, save the refresh token, and return a proper JSON response. Password hashing and email validation were implemented, including checks for duplicate emails. Minor bugs were also fixed.
https://github.com/IU-Capstone-Project-2025/Smartify/pull/44

**Kuchukbaeva Regina** – Designed the main informational page about the project, the university listing interface with card layout, tag-based filtering, and indexed search. Created a detailed university profile page and implemented filtering options including region, rating, budget seats, dormitory availability, military training center, and faculties. A “Show All” page was also designed to improve navigation and discovery.
https://www.figma.com/design/kw2m1A0ArR9Tb4Obcb2FPx/Smartify?node-id=30-8511

**Basanov Maxim** – Establishing communication between each participants at meetings and in the Telegram, emerging problem solving, GitHub repositories, Backlog and all documentation maintaining, this report writing
https://github.com/orgs/IU-Capstone-Project-2025/projects/2

## Plan for Next Week

### 🛠️ UX/UI

- Development of a user role selection page: student/teacher/mentor. Personalize the content depending on the chosen role.
- Educational interface, a guide to the main functions of the application
- Optimization and improvement of current functionality

### 🛠️ Frontend

- Integrate new UI components based on updated Figma designs.
- Fix crash caused by arrow button interactions.
- Improve visual consistency with the latest mockups.

### 🛠️ Backend

- Implement the possibility of restoring your account by mail
- Connect mongodb to go 
- Implement an API on go to manage mongodb
- Implement token storage on the client side 
- Implement automatic login to the account using a token

### 🛠️ ML

- Write Python script to analyze dataset
- Normalize and index `professions.json`, `dataset_career_test.json`, and `universities.json`
- Datasets for training recommendation model
- Prototype model using `scikit-learn` or `TensorFlow`
  
## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition
- [+] Run via docker-compose (described in the `README.md`)
