---
title: "Week #5"
---

# **Week #5**



# Feedback

## Sessions

We conducted user sessions with representatives of our target audience.

### Session 1
**Feedback:**
- User-friendly interface and pleasant design
- Interested in the ability to contact tutors

### Session 2
**Feedback:**
- Liked the career guidance test feature
- Not enough information about tutor qualifications
- Wants to know about deadlines

### Session 3
**Feedback:**
- Liked the career guidance test feature
- Mobile interface is slightly overloaded
- Wants more gamification and visual feedback
- The university base is very small



# Analyze

Based on the feedback received, we identified the following key insights:

### High Priority
- Simplify and make the mobile interface more beautiful
- Make chat for communication
- Increase the university database

### Medium Priority
- Make notifications

### Low Priority
- Add gamification and visual rewards for activity



# Iteration & Refinement

Based on user feedback, we implemented the following improvements:

- Increased the university database
- Made sketch of chat for communication
- Take a note for notifications and gamification
- During work or free time, do user-friendly design



# Performance & Stability

We evaluate the performance and stability of our application:

- **Starting the app:** ~15 sec (due to start from terminal, not deploy)
- **Authentication and Authorization:** immediately after clicking
- **Sending the form:** immediately after clicking
- **Switching pages:** immediately after clicking



# Documentation

The project includes the following types of documentation:

1. **README.md** — general project description and goal
2. **Figma** — for creating more design things and features  
3. **Backlog** — for maintaining issues and tasks and planning the sprints
4. **Telegram** — for communication and files exchanging



# Weekly commitments

## Individual contribution of each participant

## 🎨 UX/UI

Responsible - **Kuchukbaeva Regina**
 - Сhat with tech support
 - List of notifications
 - Career recommendations page
 - Request a teacher to chat with him page
 - Start policy development

✅ Related artefacts:
- [Figma](https://www.figma.com/design/7D72pnxGyyRk9lh58vzCFY/INFO-UNIVERSITIES?node-id=0-1&p=f)
- [Recommended professions page](https://github.com/IU-Capstone-Project-2025/Smartify/issues/97)
- [Tutors page](https://github.com/IU-Capstone-Project-2025/Smartify/issues/98)



## 💻 Frontend

Responsible - **Chugaeva Mariia**

- Page with recommendations on professions recommendation_screen.dart
- Page with details recommendation_detail_screen.dart 
- Added a link to the recommendations page after sending the questionnaire
- Fixed minor bugs

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/102/)


Responsible - **Zakirov Karim**

- The tutor list page:
  - The layout design has been fully developed
  - The filters are stylized, filtering by rating and price ranges has been added
  - Fixed an issue with long item names

- The tutor's detailed page:
  - A modern design has been made: a full-width photo, a data card, stylized blocks.
  - The "Submit a request" button

- Application page:
  - Initially editable empty fields are implemented
  - Calendar Page

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/107)



## 🛠️ Backend

Responsible - **Mayorov Daniil**
- Added the ability to save tasks
- Task class for working with tasks
- Subject class for working with subjects
- Manager class, for managing subjects, tasks and saving data
- Fixed all the bugs that occurred while fixing map to object-oriented approach
- Added data saving using SharedPreferences
- Data is stored under the “subjects” key

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/108)


Responsible - **Antipov Alexey**
- Docker for ML
- Service for ML in docker software
- Connected ML to the server
- Functions and endpoints
- Configured recommendations to be saved in DB
- Function to update general information for the user

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/108)



## 🤖 ML

Responsible - **Andruwenko Valery**
 - Removed the intermediate database
 - Structured the output not to the console, but to a separate database

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/109)
- [Issue](https://github.com/IU-Capstone-Project-2025/Smartify/issues/100)



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

- Privacy policy page
- Minor edits in existing pages are possible
- Сontinuation policy development
- Work with open issues

### 🛠️ Frontend
- Implement further design
- Improvement the design to better match Figma
- Work with open issues

### 🛠️ Backend

- Renew all files which describe the architecture
- Configure saving questionnare of professions
- Make swagger documentation

### 🛠️ ML

- Continuous working on MLs
- Expand all DB



## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
