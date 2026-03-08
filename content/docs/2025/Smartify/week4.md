---
title: "Week #4"
---

# **Week #4**

## CI/CD

The pipeline does the following:

- Responds to push or pull_request in main
- Establishes an SSH connection to a remote server using a secret key
- Copies the project (docker-compose.yml, backend, frontend, database, ml) to the server
- Performs on the server:
  - docker-compose build — collects
  - docker images-compose up -d
- Deletes the key after completion for security

### Links to CI/CD configuration files
[Here](https://github.com/IU-Capstone-Project-2025/Smartify/blob/main/.github/workflows/main.yml) is the CI/CD configuration file

## Deployment

What's unfolding:
- backend/ - a backend service 
- frontend/ — an interface
- ml/ — ML model
- database/ — databases
- docker-compose.yml — binds all services in containers

Where it is deployed:
- Remote server with IP 213.226.112.206
- Under the user ghrunner
- To the /pro/smartify directory

How:
- The SCP files are copied first.
- Then on the server:
  - The project is being built with the docker-compose build
  - It starts with docker-compose up -d

## Vibe Check

Everything is going well with the team. We're all on track and managing to meet our deadlines smoothly. Everyone is contributing effectively, and there are no major roadblocks at the moment. The team dynamics are positive, and communication is clear, so we are confident that we will continue to work constantly. Since our project is quite voluminous and involves constant use by people, we try to fill it with various features as much as possible.

# Weekly commitments

## Individual contribution of each participant



## 🎨 UX/UI

Responsible - **Kuchukbaeva Regina**
 - Implement the tutors page
 - Implement tutorship page
 - Working on a privacy policy

✅ Related artefacts:
- [Figma](https://www.figma.com/design/7D72pnxGyyRk9lh58vzCFY/INFO-UNIVERSITIES?node-id=0-1&p=f)
- [Tutors page](https://github.com/IU-Capstone-Project-2025/Smartify/issues/70)
- [Tutorship page](https://github.com/IU-Capstone-Project-2025/Smartify/issues/71)



## 💻 Frontend

Responsible - **Chugaeva Mariia**

- Page with a list of professions with a search by name
- Page with the details of the professions with a detailed description
- Fixed a bug with text input in the field in the questionnaire
- Fixed the displacement of the button on the phone screen
- Replaced the university icon with a new one
- Changed the hierarchy of the profession and EXAM preparation buttons according to the updated design

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/87)


Responsible - **Zakirov Karim**

- Adding universities to favorites
- Implementing a tape with selected universities at the top of the page
- Adding information about faculties and region to the university card
- Implement animations when scrolling through a carousel with favorites
- Adding deadlines to Task Tracker
- Adding a calendar page
- Ability to view current assignments by date

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/90)



## 🛠️ Backend

Responsible - **Mayorov Daniil**
 - Fixed the problem that caused to be unable to run flutter security storage
 - Configured the token storage in a secure location
 - Set up automatic login to the account when the token is present
 - Set up logging out of the account on the client side
 - Implement a couple of functions for saving and reading data in Shared Preferences + configured the mail connection
 - Connected the Shared Preference to the application, now your mail is displayed

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/92)


Responsible - **Antipov Alexey**
 - Configure token-conversion
 - CI/CD configuration

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/92)



## 🤖 ML

Responsible - **Andruwenko Valery**
 - Analysis and refinement AI.py
   - The logic of calculating the rating of professions
   - The correctness of the calculation and limitations of the final rating
   - The output is the top 5 professions for the student
 - Checking professions.json
   - Rechecked the file structure
   - The presence of required fields: name, description, ege_subjects, mbti_types

✅ Related artefacts:
- [PR](https://github.com/IU-Capstone-Project-2025/Smartify/pull/88)



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

 - Updating the profile page
 - Calendar
 - Mini-chat
 - Privacy Policy for the next weeks:
   - Determine which data is being collected
   - Study the legal requirements

### 🛠️ Frontend

- Filters for finding professions
- Improve the design to better match Figma
- Implement further design as it becomes available
- Calendar
- Mini-chat
- Database with university

### 🛠️ Backend

 - Renew all files which describe the architecture
 - Configure saving questionnare of professions

### 🛠️ ML

- Working on ML
- Expand DB of professions
- Connect MLs to the app



## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
