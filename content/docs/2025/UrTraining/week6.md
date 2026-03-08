# Report 6. Final Touches & Presentation Preparation

# UrTraining

**Authors:** Ildar Rakiev, Makar Dyachenko, Salavat Faizullin, Egor Chernobrovkin, Alexandra Starikova, Ilona Dziurava, Anisya Kochetkova

The application can be viewed here: [UrTraining](http://31.129.96.182/)

**Date:** July 2025

# Team Members

| **Team Member**     | **Telegram**   | **Email Address**                    | **Role**          |
| ------------------- | -------------- | ------------------------------------ | ----------------- |
| Ildar Rakiev (Lead) | @mescudiway    | i.rakiev@innopolis.university        | Backend / Frontend|
| Makar Dyachenko     | @index099      | m.dyachenko@innopolis.university     | Frontend / Design |
| Salavat Faizullin   | @FSA_2005      | s.faizullin@innopolis.university     | Backend           |
| Egor Chernobrovkin  | @lolyhop       | e.chernobrovkin@innopolis.university | ML                |
| Alexandra Starikova | @lexandrinnn_t | a.nasibullina@innopolis.university   | ML                |
| Ilona Dziurava      | @a_b_r_i_c_o_s | il.dziurava@innopolis.university     | PM                |
| Anisya Kochetkova   | @anis1305      | a.kochetkova@innopolis.university    | Testing           |

---
# Links 

### Frontend deployment: [Frontend](http://31.129.96.182/) 
### Backend deployment: [Backend](http://31.129.96.182:8000/)
### ML deployment: [ML](http://31.129.96.182:1337/)
### API Docs: [Saved programs API](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/backend/documentation/SAVED_PROGRAMS_API.md), [Training progress API](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/backend/documentation/TRAINING_PROGRESS_API.md), [Trainer API](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/backend/TrainerDocumentation.md), [Main API](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/backend/ENDPOINTS.md)
### Design: [Figma](https://www.figma.com/design/JCcg0OidafifcL1SRYnZC4/UrTraining-design-draft?node-id=0-1&p=f&t=qxtzvroxewe8tgPq-0)
### Demo draft: [Client flow](https://drive.google.com/file/d/1SyvwZ0c6wAwnoQHJF5BX_85TcQkbp_S8/view?usp=sharing), [Trainer flow](https://drive.google.com/file/d/1HdDF1eE4lbEzQPsncmrEYhpK5p3zFFkE/view?usp=sharing)
### README: [README](https://github.com/IU-Capstone-Project-2025/UrTraining/blob/main/README.md)
### Repository: [Repository](https://github.com/IU-Capstone-Project-2025/UrTraining)

---
# Project Overview

Have you ever felt shy going to the gym? You don’t know what to train, but don’t want a trainer watching over your shoulder? Or maybe you’re a trainer who wants to share your experience but doesn’t want to spend time editing videos?

Then here we are!

UrTraining is a platform for both trainers and trainees, offering benefits to each. Trainers can share their training plans as text or simply by uploading a photo. Clients get access to qualified trainer programs, but only see relevant workouts thanks to AI personalization. You can save trainings, track your progress, and explore the catalog.

Join now!

---
# Features

- Main page with Sign In and Sign Up buttons for trainers and clients

![main](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/main_page.png)

- Registration process

![re-login](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/logfix.gif) 

- Questionnaire for users to generate recommendations

![client_survey](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/client_survey.gif)

- AI-powered recommendation engine

![main](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/client_recomendation.png)

- Client profile

![profile](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/client_profilee.gif)

- Training catalog with filtering

![catalog](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/catalog.gif)

- Course card

![card](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/card1.png)
![card](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/card2.png)

- Save functionality

![save](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/save.gif)

- Simple tracking system

![tracking1](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/tracking1.png)
![tracking2](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/tracking2.png)

- Questionnaire for trainers

![trainer_survey](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/trainer_survey.gif)

- Trainer profile

![trainer_profile](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/trainer_profile.gif)

- Course metadata information

![metadata](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/course_step1.gif)

- Manual course creation

![upload_manualy](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/course_step2.gif)

- Training upload from photo

![upload_photo](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/photo_upload.gif)

- FAQ page

![FAQ](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/FAQ.gif)

---
# Tech Stack

## Frontend
- **React** – Component-based UI development
- **vite** – Fast build- and dev-server for service
- **Nginx** - Serve built frontend vite-application to users

## Backend
- **FastAPI** – High-performance Python backend
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM for database interactions
- **Docker** – Containerization
- **GitHub Actions** – CI/CD pipeline

## ML
- **FAISS** - Vector storage library
- **PyTorch, Transformers** -  Fine-tuned, pre-trained models hosting
- **OpenAI-like APIs** - LLMs integration
- **sentence_transformers** - embedding models training

---
# Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/IU-Capstone-Project-2025/UrTraining.git
cd urtraining
```

### 2. Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate     # or .\venv\Scripts\activate on Windows
docker-compose build
docker-compose up -d
```

Server will be accessible at **port 8000**.

### 3. Frontend Setup (React + Tailwind)
```bash
cd frontend
npm install
npm run dev
```

### 4. Vector Database (for recommendation engine)
```bash
cd ml/vector-db
docker-compose build
docker-compose up -d
# Run any script or training notebook as needed
```

Endpoints will be accessible at **port 1337**.

### 5. Image2tracker Module
```bash
cd ml/image2tracker
docker-compose build
docker-compose up -d
# Run any script or training notebook as needed
```

Endpoints will be accessible at **port 1338**.

### 6. Smart Assistant (for the course card)
```bash
cd ml/course-assistant
# Run any script or training notebook as needed
```

### 7. Trainer Assistant (for the training uploading)
```bash
cd ml/course-checker
pip install -r requirements.txt
# Run any script or training notebook as needed
```

### 8. Environment Variables

Set environment variables for backend/frontend via .env files:


**backend/.env**

**frontend/.env.local**

**Hint:** copy ```.env.example``` to ```.env``` and fill in the required data before running the project.

---
# New Feedback

This week we collected feedback from two unknown people: one trainee and one trainer. One feedback session was conducted in person — we observed the user as she went through the flow. The second person shared feedback online via screen sharing, allowing us to observe the entire user journey and their frustrations.

This time, we had fewer minor issues, and the users had a generally positive experience.

## User 1 Feedback (Trainee Case)

**Alina**, 20 years old, management student, trains every day at the gym and is interested in personalized training programs.

- **Navigation is unclear**  
  Currently, the only way to return to the homepage is by clicking the logo, which is not intuitive or user-friendly.  
  ➤ Suggestion: Add a clear “Back” or “Home” button in the navigation menu.

- **Error messages during registration are confusing**  
  While registering, error messages appear but don’t specify which fields they relate to.  
  ➤ Suggestion: Display validation errors directly under the affected fields with clear explanations.

- **Cannot upload or change profile picture**  
  After registration, the user couldn’t upload or update their profile photo. While this isn’t critical, it negatively impacted the experience.

- **Upload page is accessible to clients**  
  Clients can access the *Upload* page and attempt to submit training programs, even though it’s meant for trainers.  
  ➤ Suggestion: Hide this page from trainees or display a clear message that it’s for trainers only.

- **Step 1 resets after returning from Step 2 in the questionnaire**  
  When moving from Step 2 back to Step 1 of the onboarding questionnaire, all previous input is lost.  
  ➤ Suggestion: Preserve form state between steps to avoid re-entering data.

- **Unpleasant and inconvenient training type rating scale**  
  The 1–5 scale used to select training preferences is visually unappealing and unintuitive.  
  ➤ Suggestion: Consider redesigning the UI with sliders, emojis, or a more compact layout.

- **“Oops” error (401 Unauthorized) after submitting questionnaire**  
  After completing the onboarding flow, an error message “Oops” with code 401 appeared. Despite this, the user was greeted with “Hello, [Name]”.  
  ➤ Suggestion: Investigate authorization logic and ensure that session state is preserved.

- **Filter panel hides content by default**  
  The filter sidebar is open by default and takes up a large portion of the page.  
  ➤ Suggestion: Collapse it by default and let users open it when needed.

- **Scalability of catalog is unclear**  
  The user asked what will happen when more training programs are added. Currently, everything is shown on a single page.  
  ➤ Suggestion: Consider pagination or infinite scroll for a better browsing experience.

## User 2 Feedback (Trainer Case)

**Victoryia**, 27 years old, stretching trainer from Minsk, shares workouts on Instagram: @cova_fit.

- **Registration required too early**
  When I first visit the site, I want to freely explore — click around, see how it works, and view what other trainers offer.  
  However, I’m immediately prompted to register. This discourages me, and I just close the page.  
  ➤ Suggestion: Allow browsing of at least limited training content before requiring registration.

- **No indication of required fields in the questionnaire**  
  It’s unclear which fields are mandatory when filling out the questionnaire.  
  ➤ Suggestion: Mark required fields with an asterisk (*) or provide clear instructions.

- **Belarus is missing from the country list**  
  I couldn’t find Belarus in the country dropdown.

- **Only one specialization can be selected**  
  What if I specialize in several training types (e.g., stretching, pilates)? I can only select one.  
  ➤ Suggestion: Allow selecting multiple training specializations.

- **Too many certificates — no batch upload**  
  I constantly study and have many certificates. Uploading them one by one is time-consuming.  
  ➤ Suggestion: Add multi-file upload support for certificates or allow grouping by categories.

- **No space for sharing personal achievements**  
  I want to share my competition victories, which help build credibility with clients.  
  ➤ Suggestion: Add a “Achievements” or “Awards” section in the trainer profile.

- **Workout creation needs validation (ideally AI-powered)**  
  It's essential to validate training programs to prevent harm or poor-quality recommendations.  
  ➤ Suggestion: Add strong validation logic, possibly with AI, to detect illogical or risky content.

- **Unclear course duration options**  
  While creating a course, I see options like “1”, “2”, and “5” under *Course Duration*.  
  ➤ Suggestion: Clarify what these values mean — are they weeks, months, days? Why those numbers?

- **No way to share a single workout without creating a course**  
  Sometimes I just want to post a great individual workout, not a full course.  
  ➤ Suggestion: Add a “Single Workout” mode to post standalone training sessions.

- **Dropdowns lack “Other” option**  
  Predefined dropdown lists are helpful, but sometimes my needed value is missing.  
  ➤ Suggestion: Add an “Other” option that allows free text input.

- **Misleading AI button label**  
  When I click **"Generate with AI"**, I expect the AI to create a course for me, like a chatbot would.  
  But it only converts my photo into course format.  
  ➤ Suggestion: Rename the button to something like *"Convert from Photo"* or *"Import workout from image"* to better reflect what it does.

- **Course labeled as “by unknown trainer”**  
  After creating a course from a photo, it appeared as created by “unknown trainer.”  
  ➤ Suggestion: Automatically link the course to the trainer’s name/profile.

- **Session expired too quickly**  
  After 30 minutes of inactivity, I was logged out and had to log in again.  
  ➤ Suggestion: Either extend session duration or provide a warning before logout.

---
# Testing

## Trainer tests

We implemented unit and integration tests to validate our Pydantic models for trainer profiles and onboarding forms. The tests cover default values, validation errors, serialization, and edge cases. **39** tests were implemented.

**Commit:** [Trainer tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/f04956f8949af63d67581853998ee91aa76d82d5)

![Trainer tests](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/trainer_tests.png)

## Training validation and editing tests

We tested the FastAPI endpoints for training validation and editing, ensuring correct request handling and LLM integration. Unit tests also validate request/response models and simulate LLM responses using mocking. This guarantees reliability of both API logic and AI-assisted feedback processing. **10** tests were implemented.

**Commit:** [Training validation tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/c639c48a16a9668233f43be35d1cd448666420de)

![Training validation tests](https://raw.githubusercontent.com/IU-Capstone-Project-2025/UrTraining/main/reports/static/training_tests.png)

---

# Weekly Progress Report

| Team Member (Role)         | Contribution Description                                                                                                                                             | Contribution Link                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Ildar Rakiev (Backend/Frontend, Lead) | Implemented fully functional profile pages for clients and trainers, updated course structure logic, added FAQ page, restricted upload access for non-trainers, fixed client survey bugs and improved trainer registration flow   | [Profile page](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/189cbe72f8e2d08755a40930748128b49ea3142d), [Course structure](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/1efd8224bb97ff698fed4822930dab2f0d0d65b1), [FAQ](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/c818e82fab407a3bacb8ab3aceff8ea0a4220331), [Navbar updates](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/bbcba33102048cf9ba66df40a76b2ce0f1b153c8), [Fixes](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/5db97564783b73608865e31357f51b89e6017363)      |
| Makar Dyachenko (Frontend/Design) | Implemented mobile adaptation for Welcome, Profile, Catalog, Begin, and Recommendation pages. Improved UI styling across course and general views   | [Course style improvements](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/0cc9e03c2be88e4f30455badd3702b68c3646fbb), [General style improvements](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/90f6b8828c4bef420bcb19b52d840e0e1384c42f), [Mobile adaptation](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/43980ec3e65b1224bbdfee62bb46a54319c09c68)        |
| Salavat Faizullin (Backend)   | Developed backend features allowing users to update their full profile, added advanced course filtering, and implemented the training tracker in catalog or training page  | [User data endpoint](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/ac211e3738efec967257a2e28681a4efe294e379), [Filtering](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/106), [Tracker](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/112)        |
| Egor Chernobrovkin (ML)  | Implemented course generation from uploaded images and contributed to mobile UI adaptation design in Figma  | [Generate course from image](https://github.com/IU-Capstone-Project-2025/UrTraining/pull/94), [Mobile adaptation design](https://www.figma.com/design/JCcg0OidafifcL1SRYnZC4/UrTraining-design-draft?node-id=0-1&p=f&t=Te5X4ZcOUdxb1a3B-0) |
| Alexandra Starikova (ML) | Participated in designing the mobile UI and interface improvements using Figma | [Design](https://www.figma.com/design/JCcg0OidafifcL1SRYnZC4/UrTraining-design-draft?node-id=0-1&p=f&t=Te5X4ZcOUdxb1a3B-0)       |
| Ilona Dziurava (PM)      | Designed the FAQ page and wrote its content, collected user feedback, organized team backlog, coordinated teamwork, and wrote the report and README.  | [FAQ page](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/cd791228446a909026098eb5dc3624a1b9aed265), [README](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/4e91af7a770e97e51c4b384fd56f71b5676294b6), This report :)   |
| Anisya Kochetkova (Testing)   | Verified API interaction using mock backend tests, ensured query invalidation logic, implemented frontend mutation tests, and documented trainer-related APIs | [Trainer tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/f04956f8949af63d67581853998ee91aa76d82d5), [Course tests](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/c639c48a16a9668233f43be35d1cd448666420de), [Frontend tests for API](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/79e2f539529d782e10a05a7ef570329ca54dd1f1), [Frontend tests mutation](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/277691de0d453db46e2b7b2fd0a5a4d7cd8c2596), [Trainer API documentation](https://github.com/IU-Capstone-Project-2025/UrTraining/commit/298715923738ecb8b18abce862a12f9ed73b1829) |

## Challenges & Solutions
The biggest challenge this week was to switch the entire team to frontend development and design, as the core backend and ml functionality had already been implemented. For many team members, this was their first experience working with frontend technologies. Despite this, we managed to successfully adapt by supporting each other, dividing tasks effectively, and actively learning new tools and frameworks on the go.

## Conclusions & Next Steps

During Week 6, our primary focus was on finalizing and polishing the project in preparation for the upcoming final presentation. We completed remaining high-priority features, fixed outstanding bugs, and performed comprehensive end-to-end testing to ensure stability and usability across the application. Also we conducted two more feedback sessions to see the user perpective. 

Our team finalized the project documentation:
- The `README.md` was updated with a full project overview, list of features, tech stack, setup instructions, and a deployment link.
- API documentation was completed and reviewed for accuracy.
- Design documents (including Figma screens) were aligned with the final state of the application.

We also made progress on preparing the final presentation:
- Presentation slides were drafted.
- Draft of the demo was created. 

Overall, this week was dedicated to polishing the application from both technical and user perspectives, ensuring we are ready to showcase a complete, stable, and user-friendly product.

### Next Steps for Week 7

- **Final Rehearsal**  
  Conduct one last complete run-through of the presentation and live demo with the full team.

- **Technical Check**  
  Implement the final feature - progress tracking. Verify that the demo environment is working correctly and that all project components are functioning as expected.

- **Deliver Final Presentation**  
  Present the project clearly and confidently to TAs and peers.

**We confirm that the code in the main branch:**

In working condition.
Run via docker-compose.
