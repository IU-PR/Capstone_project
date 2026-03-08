---
title: "Week #3"
---

# **Week #3**


### Project name: **InnoSync**

**Code repository**: https://github.com/IU-Capstone-Project-2025/InnoSync

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| (Lead) Ahmed Baha Eddine Alimi     | @Allimi3 | a.alimi@innopolis.university | [Management/Product Design] | Team Management, Frontend & Design Supervision|
| Yusuf Abudghafforzoda| @abdugafforzoda | y.abudghafforzoda@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Egor Lazutkin            | @Johnn_u | e.lazutkin@innopolis.university | [Backend] | Backend Integration, Database Design and Conception |
| Anvar Gilmiev            | @glmvai | a.gilmiev@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Asgat Keruly            | @east511 | a.keruly@innopolis.university | [Frontend] | Frontend Implementation, Design Conception |
| Aibek Bakirov | @bakirov817 | a.bakirov@innopolis.university | [DevOps] | Infrastructure Automation, CI/CD Setup, Deployment |
| Gurbanberdi Gulladyyev | @gurbangg | g.gulladyyev@innopolis.university | [ML] | ML Model Research & Development for QuickSyncing |


## Implemented MVP features

1. **User Authentication**  
   - Recruiters and Recruitees can sign up and log in securely.  
   - Profile creation flow is initiated upon first login.

2. **Recruitee Profile Creation**  
   - Recruitees can provide detailed information including:  
     - Preferred roles/positions  
     - Tech stack (skills)  
     - Expertise level (Entry, Junior, Mid, Senior)  
     - Experience level  
     - Work experience history  
     - Resume upload (optional)

3. **Talent Search & Filtering**  
   - Recruiters can manually search and filter Recruitees.  
   - Filtering options include skills, roles, and expertise level.

4. **Project Search & Application & Filter**  
   - Recruitees can browse and filter available projects.  
   - Projects are filterable by required skills, type (paid/academic), and time commitment.  
   - Recruitees can apply directly to projects via the dashboard.

---

## 🔄 Functional User Journeys

### 1️⃣ User Journey: Sign Up & Login

**Persona:** Recruitee or Recruiter

1. User visits the platform landing page.
2. Clicks on "Sign Up" and fills in the required registration form.
3. After successful sign-up, user is redirected to the profile creation wizard.

---

### 2️⃣ User Journey: Profile Creation

**Persona:** Recruitee or Recruiter

1. After first sign up, user is prompted to create a profile.
2. User fills in:
   - Preferred roles/positions
   - Tech stack (skills)
   - Expertise level (Entry–Senior)
   - Experience level
   - Work experience (optional)
   - Uploads resume (optional)
3. On completion, user is redirected to the Recruitee Dashboard.

---

### 3️⃣ User Journey: Recruiter Searches & Filters Recruitees

**Persona:** Recruiter

1. Recruiter logs into the platform.
2. Navigates to the "Talent Search" section from the dashboard.
3. Applies filters such as:
   - Skills
   - Roles
   - Expertise level
4. A list of matching Recruitee profiles is displayed.
5. Recruiter views profiles and may contact candidates.

---

### 4️⃣ User Journey: Recruitee Browses & Applies to Projects

**Persona:** Recruitee

1. Recruitee logs into their dashboard.
2. Navigates to the "Projects" section.
3. Uses filters like:
   - Required skills
   - Project type (paid/academic)
   - Time commitment
4. Selects a project and views detailed description.
5. Clicks “Apply” to send an application.


## Demonstration of the working MVP
Below are screenshots showcasing the current working state of our MVP:

### 🔐 Sign Up & Login
- New users can create an account and access the platform.
![Sign Up Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/Снимок%20экрана%202025-06-25%20200407.png)
![Login Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/Снимок%20экрана%202025-06-25%20201054.png)

---

### 📝 Profile Creation
- Recruitees can build a detailed profile, including roles, skills, experience, and resume upload.
![Profile Creation Step 1 Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/photo_4_2025-06-25_22-03-53.jpg)
![Profile Creation Step 2 Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/photo_2_2025-06-25_22-03-53.jpg)
![Profile Creation Step 3 Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/photo_3_2025-06-25_22-03-53.jpg)
![Profile Creation Success Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/photo_1_2025-06-25_22-03-53.jpg)

---

### 🧑‍💼 Recruiter View – Talent Search & Filter
- Recruiters can search and filter Recruitees based on multiple criteria.
![Talent Search Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/Снимок%20экрана%202025-06-25%20200901.png)
![Talent Filter Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/Снимок%20экрана%202025-06-25%20201002.png)

---

### 🧑‍🎓 Recruitee View – Project Search & Application
- Recruitees can search and apply for projects that match their skills.
![Project Search Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/Снимок%20экрана%202025-06-25%20200712.png)
![Project Filter Page](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/Снимок%20экрана%202025-06-25%20200848.png)


## 🛠️ Backend Implementation

The backend was developed using **Java with Spring Boot** and Below are screenshots showcasing some of the current working state of our MVP endpoints:
> 📄 To view the full list of working APIs, please check our backend API documentation:  
> [View ReadMe](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/assets/API_documentation.md)

---

### 🔐 Authentication APIs
![Sign Up API](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/image_2025-06-25_21-38-07.png)  
![Login API](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/image_2025-06-25_21-37-44.png)

---

### 📁 Project Management APIs
![Project API](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/image_2025-06-25_22-31-34.png)  
![Project API Success](https://raw.githubusercontent.com/IU-Capstone-Project-2025/InnoSync/refs/heads/main/assets/image_2025-06-25_22-32-21.png)



## 🤖 Machine Learning (QuickSyncing)

We enhanced the recommendation engine that powers QuickSyncing by introducing a **team synergy metric** and deploying a lightweight API.

**Link to the training code**: [View Code](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/ML/recommender.py)

### ✅ Improvements Made
- Added **team synergy scoring** using **Jaccard similarity** to assess how well candidates complement each other.
- Implemented **content-based filtering** using:
  - **TF-IDF vectorization** on skill descriptions.
  - **Cosine similarity** to match job requirements with candidate profiles.
- Built and deployed a **FastAPI microservice** to expose the model as an endpoint for backend integration.

### How The Model Works
- The Model uses content-based filtering by using TF-IDF vectorization to convert skills (text) into numerical weights. Then we use cosine similarity between job requirements and candidate skills. We also evaluate team synergy using Jaccard similarity. Also, added FastAPI for integration with backend.

**Links to the initial model artifacts**
- Mock data for jobs [View Code](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/ML/team_jobs.csv)
- Mock data for candidates [View Code](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/ML/team_candidates.csv)
- FastAPI App [View Code](https://github.com/IU-Capstone-Project-2025/InnoSync/blob/main/ML/app.py)

## 🧪 Internal demo

### 🔍 Demo Summary
We conducted an internal demo of the MVP to test the entire end-to-end user flow from both Recruitee and Recruiter perspectives.

### ✅ What Worked Well
- **Authentication system** was fully functional: sign up, log in, and session persistence worked as expected.
- **Profile creation** guided users step-by-step and stored data correctly.
- **Talent search and filtering** on the Recruiter side successfully returned Recruitees.
- **Project search and application flow** on the Recruitee side was responsive and filtered results accurately.
- **ML FastAPI integration** was functional locally, returning basic candidate recommendations.

### 🐞 Identified Issues / Bugs
- Profile creation form UX needs slight refinements.
- Filtering and searching pages for both recruitee and recruiters are not responsive and need more refined design.
- Some validation messages are not clearly displayed.

### 🔧 Immediate Action Points
- Improve UI/UX of forms (auto-focus fields, better error display).
- Fix inconsistencies in filtering results.
- Removing the role based feature and make everyone can act as recruiter and recruitee.
- Run another internal walkthrough post-patches before demoing externally.

### Product Design
- Conducted UX research to identify pain points and inefficiencies in the existing design and application flow [[View Docs Link]](https://docs.google.com/document/d/1MQrfwRCKrIERXYb7NTF-UlpgPONcMYxe_SBkxnDiKsw/edit?usp=sharing)
- Enhanced the high-fidelity designing for the web application [[View Figma File]](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=2LRuSQRB1dTt6pKe-1)

### CustDev
- Researched and formulated customer Journey Map [[View Docs Link]](https://docs.google.com/document/d/1kQEwIuQKmiQhXhjXWIOvx3K1JsMtacv6KoPEj-hRHkU/edit?tab=t.0)
# Weekly commitments

## **Individual Contribution of Each Participant**

- **Ahmed Baha Eddine Alimi:**
    - UX research of the user pain points in the current design and application flow [View Docs](https://docs.google.com/document/d/1MQrfwRCKrIERXYb7NTF-UlpgPONcMYxe_SBkxnDiKsw/edit?usp=sharing)
    - Created Issues in Github to facilitate collaboration and progress tracking [View](https://github.com/IU-Capstone-Project-2025/InnoSync/issues)
    - Implemented the design for Signup and Login Page [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/a31ba0c916b82763454177d229447cb33381f3e8)
    - Enhanced the application figma design [View High-Fi Figma File](https://www.figma.com/design/qDq1rHa8D5f1AlJtMBb0rz/High-Fi-design-InnoSync?node-id=0-1&t=2LRuSQRB1dTt6pKe-1)
    - Reviewed and merged pull requests in the frontend side [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/a5d064d94a8bc53857d494ef140224e2c715e69e)
    - Wrote the report


- **Yusuf Abudghafforzoda:**
    - Impelemented Project creation API [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/d07be90cc26580f02f384fe2a8d05c7adcaba0db)
    - Implementend Invititation API (Sending, accepting, deniying) [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/acd70e575e43b3f4c3e524e9d24443c02427c784)
    - Implementend application API [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f0380c95c68ed031bc98dc4fb5d81095754b3577)
    - Updated ReadMe for backend Documentation [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f479cf60420b4f5d30bf30ab75586f2b2863ff2f)

- **Egor Lazutkin:**
    - Expanded Functionality and information content of the user profile (added new fields and database connections between profile and additional information). [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/71e15876ddd8e906eb8505a045a48d99d8867ac1)
    - Implemented Customer Journey Map [View Docs](https://docs.google.com/document/d/1kQEwIuQKmiQhXhjXWIOvx3K1JsMtacv6KoPEj-hRHkU/edit?tab=t.0)
- **Asgat Keruly:**
    - Implemented Talent Search and Filtering Page [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/9a30c524d94c4149c63cf7fa385ad6544dddeb8e)
    - Implemented Project Search and Filtering Page [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/a4003b5bf9e3c367cb1eb2149ca41e2fafcf719f#diff-089f950c23464f18659413aae08e64964e313f2d7569cf434e69ef44d6cda6fc)
    - Linked frontend and backend, Endpoints linkage. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/b7ffd566677375d143e2a1e9b2a3c918876f35ce)
    - MVP testing, and provided screenshots of MVP to the report

- **Anvar Gilmiev:**
  - Continued Implementation of Profile creation pages [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/1ed6b851271774293ccaa6f3a010d58c082a52b6)
  - Worked on the endpoints linkage in the profile creation page [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/1ed6b851271774293ccaa6f3a010d58c082a52b6)
- **Aibek Bakirov:**
    - Created virtual machine [View ReadMe](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/5fc185e7f21cd54df7f5b65e58e5b940359a305a)
    - Deployed backend server [View Link](51.250.42.156:8080)

- **Gurbanberdi Gulladyyev:**
    - Improved ML model by introducing team synergy scoring using Jaccard similarity. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f194653dbb723b2a769fdc314fa6943f24280747)
    - Built FastAPI service for exposing capabilities. [View Commit](https://github.com/IU-Capstone-Project-2025/InnoSync/commit/f194653dbb723b2a769fdc314fa6943f24280747)

## Plan for Next Week
1. **Frontend:**
   - Enhance the current design implementation and align it with the latest Figma mockups.
   - Add consistent button styling and implement input validations across forms.
   - Introduce minimal responsiveness for better usability on smaller screens.
   - Implement the dashboard page layout and functionality.

2. **Backend:**
   - Add endpoints to accept/reject project applications.
   - Add pagination and sorting for search APIs.
   - Implement team management endpoints.


3. **Machine Learning:**
   - Add endpoint to accept full recruiter project data and return recommendations.
   - Add testing coverage and improve input validation.
   - Refactor FastAPI app for production-readiness (logging, error handling).


4. **DevOps:**
   - Finish `docker-compose` setup for full stack (frontend + backend + ML).
   - Configure GitHub Actions for continuous integration and linting.
   - Set up HTTPS and domain config (if applicable).
   - Add deployment guide to README for team usage.


5. **Product Design:**
   - Finalize remaining high-fidelity screens.
   - Conduct mini UX review based on demo feedback.
   - Update Figma with final logic flows for future reference.

5. **CustDev:**
   - Schedule and conduct short user testing sessions.
   - Gather feedback on current MVP experience (signup, navigation, value).
   - Prioritize key findings into quick wins vs. post-MVP backlog.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [**✔**] In working condition.
- [**✔**] Run via docker-compose (or another alternative described in the `README.md`).