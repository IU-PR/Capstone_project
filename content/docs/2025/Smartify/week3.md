---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

## 🧭 **User Journey Overview**

#### 👤 1. **Registration, Authentication and Password Recovery**

- User opens the app
- Navigates to the registration screen
- Enters email and password
- Confirms registration via email code
- Later, user can tap Forgot password:
  - Requests a password reset via email
  - Sets a new password and logs in again

✅ Related artefacts:
- [Frotend](https://github.com/IU-Capstone-Project-2025/Smartify/issues/13)
- [Backend (Registration and Authentication)](https://github.com/IU-Capstone-Project-2025/Smartify/issues/16)
- [Backend (Password Recovery)](https://github.com/IU-Capstone-Project-2025/Smartify/issues/18)

---

#### 🏠 2. **Home Screen**

- After logging in, user sees the home page with an overview of functionality
- Home includes access to:
  - University search
  - Questionnaire
  - Progress tracking
  - Profile settings

✅ Related artefacts:
- [Design](https://github.com/IU-Capstone-Project-2025/Smartify/issues/49)
- [Frontend](https://github.com/IU-Capstone-Project-2025/Smartify/issues/53)

---

#### 🔍 3. **University Search Page**

- User opens Search University page
- Can:
  - Search by name
  - Apply filters
  - View matching universities

✅ Related artefacts:
- [Design](https://github.com/IU-Capstone-Project-2025/Smartify/issues/12)
- [Frontend](https://github.com/IU-Capstone-Project-2025/Smartify/issues/14)

---

#### 📝 4. **Questionnaire**

- User opens the questionnaire
- Answers a series of structured questions
- Submits the questionnaire
- Server receives and saves the data

✅ Related artefacts:
- [Design](https://github.com/IU-Capstone-Project-2025/Smartify/issues/49)
- [Frontend](https://github.com/IU-Capstone-Project-2025/Smartify/issues/55)
- [Backend](https://github.com/IU-Capstone-Project-2025/Smartify/issues/58)

---

#### 📆 5. **Progress Tracking Page**

- User visits progress screen**
- Can:
  - Add personal learning or career goals
  - Set time for each task
  - View progress or daily schedule

✅ Related artefacts:
- [Design](https://github.com/IU-Capstone-Project-2025/Smartify/issues/12)
- [Frontend](https://github.com/IU-Capstone-Project-2025/Smartify/issues/62)

---

## Demonstration of the working MVP

Link - [Google Disk](https://drive.google.com/file/d/151nhpK6KhIyqQk9jXJx20fANeS7_gvnI/view)

# Weekly commitments

## Individual contribution of each participant

## 🎨 UX/UI

Responsible - **Kuchukbaeva Regina**
 - The career guidance test page
 - User profile page
 - The ЕГЭ preparation tracker page

✅ Related artefacts:
- [Figma](https://www.figma.com/design/7D72pnxGyyRk9lh58vzCFY/INFO-UNIVERSITIES?node-id=0-1&p=f)
- [Issue](https://github.com/IU-Capstone-Project-2025/Smartify/issues/49)

## 💻 Frontend

Responsible - **Chugaeva Mariia** and **Zakirov Karim**

- A main menu page has been created with navigation through the rest of the project
- Added password recovery steps: pin confirmation and entering a new password
- The interface of the already implemented pages has been translated into Russian
- Added a profile page: the ability to log out of your account, avatar display, siding animation and other visual elements
- Implemented a profile page
- Added transitions between pages
- An intermediate Professions Page has been created with the "Complete the questionnaire" button (in the future there will be a list of professions)
- University Filtering page:
  - Region and faculty selection
  - Sliders are used for setting rating and the number of budget-funded places
  - Switches are available for the "Dormitory" and "Military Training Center" filters
  - Buttons are provided to clear filters and apply them.
- Progress Track page:
  - Subjects can be added and removed.
  - Each subject allows adding tasks with a title and duration.
  - Tasks can be edited and marked as completed
  - The overall completion percentage is visualized with a CircularPercentIndicator

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/64)

## 🛠️ Backend

Responsible - **Mayorov Daniil** and **Antipov Alexey**
 - Fixed errors with sending responses from the server
 - Added API for password recovery
 - Fixed the issue of freezing when sending emails
 - Added a client-side API for working with tokens (not yet connected to the main application)
 - Implement mongo for questionnaire
 - MongoDB service is connected and linked to MongoDB Compass for database interaction
 - The MongoDB connection function to the Go server
 - Functions for adding and updating universities, questionnaires, and professions with appropriate checks
 - On the client side, a function for collecting a questionnaire and sending it via the API

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/66)

## 🤖 ML

Responsible - **Andruwenko Valery**
 - Developed an algorithm for determining MBTI based on questionnaire responses
 - Assigned each question to MBTI scales (E/I, S/N, T/F, J/P)
 - The determine_mbti() function has been written, which returns the personality type and is embedded in the database processing script
 - Сollected and structured descriptions of all 16 MBTI types
 - A new dataset_with_mbti_descriptions.json database has been created
 - Сonducted a user questionnaire among schoolchildren

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/69)
- [Questionnaire](https://docs.google.com/forms/d/1Ji5ww8OqN9WK-KvSsFbEP0bQxo4Id6vv4m_Zv_A0dhs/edit#responses)

## 📥 Project Management 

Responsible - **Basanov Maxim**
 - Establishing communication between each participants in the Telegram
 - Emerging problem solving, meetings organization
 - GitHub repositories, Backlog and all documentation maintaining
 - This report writing

✅ Related artefacts:
- [Backlog](https://github.com/orgs/IU-Capstone-Project-2025/projects/2)



## Plan for Next Week

### 🛠️ UX/UI

 - The UI for the tutors section
 - The tutorial design
 - Refine the user profile design

### 🛠️ Frontend

- Complete the implementation of the Professions Page
- Implement the tracker page
- Adapt the design to meet new requirements
- Refine the tracker's design
- Finalize the design of the university page
- Supplement the database with universities with missing data 
- Create a tab with the top of universities
- Add a detailed description of the universities

### 🛠️ Backend

 - Connect the client API for tokens to the application
 - Implement automatic login
 - Set up mail upload in the application
 - Implement the saving of the user questionnaire

### 🛠️ ML

- Completion of databases with the universities
- ML on the recommendation of professions



## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
