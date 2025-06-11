---
title: "Week #1"
---

# Week #1

## Project description

### Project name: Inno Services Search

**Code repository**:  
https://github.com/IU-Capstone-Project-2025/Inno-Services-Search-Backend  
https://github.com/IU-Capstone-Project-2025/Inno-Services-Search-Frontend

### Problem:
the information that Innopolis University students use in their daily lives is scattered across different services (EduWiki, Campus Life, moodle, sports website, etc.). Moreover, a student does not always know which service to contact with their needs.
### Solution:
implement smart search for existing Innopolis University services.
- Minimum plan: search by service content
- Base plan: use AI to answer free-form questions from users
- Advanced plan: add the ability to perform actions for the user by their text request (sign up for sports, book a room)
### Implementation:
our project is a work for [one-zero-eight](https://t.me/one_zero_eight) to create a new service for [innohassle.ru](https://innohassle.ru). We will use the list of services provided on the main page of [innohassle.ru](https://innohassle.ru), and think about supplementing it.

### **Team Members**

| Team Member           | Telegram Alias                                 | Email Address                       | Track        | Responsibilities   |
|-----------------------|------------------------------------------------|-------------------------------------|--------------|--------------------|
| Anna Belyakova (Lead) | [@belyak_anya](https://t.me/belyak_anya)       | a.belyakova@innopolis.university    | Fullstack    | Team management, integration with existing one-zero-eight services |
| Vladimir Paskal       | [@vladimirpaskal](https://t.me/vladimirpaskal) | v.paskal@innopolis.university       | Backend      | Source parsing |
| Azaliia Alisheva      | [@AzaliaAlisheva](https://t.me/AzaliaAlisheva) | a.alisheva@innopolis.university     | Backend+ML   | ML things (embedder selection and similar) |
| Aliia Bashirova       | [@Gpshfrd](https://t.me/Gpshfrd)               | al.bashirova@innopolis.university   | Frontend     | Design and frontend |
| Sofia Pushkareva      | [@mcpushka](https://t.me/mcpushka)             | s.pushkareva@innopolis.university   | Backend+ML   | Connection of a vector database |

## Brainstorming

### Ideas during brainstorming

- Search by Innopolis services  
search for any information from different services and sites for Innopolis University students.
- When2meet  
utility, when2meet analogue, working on the phone, with display of employment from the calendar, with a good UX.
- AI generator of corporate courses based on their knowledge base  
The idea is inspired by one of the largest educational platforms in Russia [Ispring](https://www.ispring.ru/) providing corporate courses constructors (without using AI)
- Determining salary expectations based on resumes  
Using AI to analyze the market and based on the collected data to assess the candidate
- Innovative Analysis for Agile teams  
Analysis of team productivity, blockers, effective sprint strategy.
- Analysis of the project on GitHub  
Determine the structure and logic of the project, evaluate the quality and security of the code, the likelihood that the project will develop
- AI generation of documentation for the code  
Automatic generation and updating of documentation when changing the code with output in markdown/HTML/wiki format

### Brief market research

- Search by innopolis services  
Existing analogues:  
[@InnaHelpBot](https://t.me/InnaHelpBot) – information by city, but not by university  
[Campus Life](http://campuslife.innopolis.ru) – no search, information is presented only partially (the formula for scholarships is not for all courses), not always relevant and optimally organized site info  
[Innohassle](https://innohassle.ru/dashboard) - not smart search, the list of services can be expanded  
- When2meet  
[Original when2meet](https://www.when2meet.com/) - not an adaptive site, without integration with calendars  
[Crab.fit](https://crab.fit) – does not integrate with calendars  
[Schej.it](https://schej.it/) - covers most requests but can be improved, for example, by integrating into innohassle to automatically take into account the students' schedule

## Basic requirements

### Target users and their primary needs

Innopolis university students.  
The main need of Innopolis students seems to be a single trusted up-to-date source of information. In our IT city and IT university, almost all services are provided only online/additionally online, but the student does not always know where exactly he should contact because there is no single knowledge base with a convenient search.  
Additionally, out project may be useful for IU staff.

### User stories

Minimum version:
- As a user, I want to enter keywords and get a list of services that relate to them in order to find relevant materials
- As a user, I want to be able to make a typo in the spelling of a word but still get a relevant result so that I have the opportunity to make a mistake
- As a user, I want to go to the resource issued by my request via a link to start using it
- As a user, I want the resource to open on click on the section I need in order to save time on manual search
- As a user, I want search results to be ranked by relevance, so that the most useful links appear first  

Basic case
- As a user, I want to enter a question in free form and get a relevant answer to it because I can't know for sure what keywords I should search for  

Advanced case
- As a user, I want to type a task (e.g., “sign up for football training”) and have the system perform the action on my behalf, so I save time.
- As a user, I want the system to autofill forms and book appointments for me when possible, so I avoid repetitive manual input.
- As a user, I want the system to recommend actions based on my academic or extracurricular activities (e.g., “You have a free slot at 4 PM – book a study room?”), so I make better use of my time.

### Initial scope

- Search bar accepting text queries
- Responses containing keywords from my query with a link to the original service  

Proposed sources of information:
- [EduWiki](https://eduwiki.innopolis.university/index.php/AcademicCalendar)
- [Moodle](https://moodle.innopolis.university/)
- Professors' database
- [Campus Life](http://campuslife.innopolis.ru/) information
- [Dorm website](https://hotel.innopolis.university/) information
- Maps, schedule, sports website (see [one-zero-eight projects](https://github.com/one-zero-eight))  

Many more sources available, but these are the main ones.

## Tech-stack

**Backend:**

- **Python:** For its simplicity and extensive libraries for data processing and machine learning.
- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard
  Python type hints.
- **MongoDB:** As our database solutions to efficiently store and manage data from various data sources (schema-less)
- **Chroma/lancedb/weaviate (the choice is expected to be made closer to practice when there is more information about the format of the parsed data):** Vector database to store embedded information for content-meaningful search.

**Frontend:**

- **TypeScript, Node.js:** A strongly typed programming language that builds on JavaScript, providing better tooling at any scale.
- **React, Vite** For building dynamic and high-performance user interfaces and server-side rendering capabilities.
- **TailwindCSS:** A utility-first CSS framework for rapid UI development with consistent and responsive design.

**ML**
- **Langchain, embeddings (choice is expected to be made based on performance with test data):** To implement the Retrieval-Augmented Generation (RAG) pipeline for generating search results.

## About using one-zero-eight repositories:
### Frontend:
we will create a page for search almost from scratch and add it to innohassle as a separate tab
### Backend:
we will use a project created as a search for moodle materials and will add search for other services to it. ML will be added from scratch (we had experience connecting this project with ML but we will do it again with new technologies)


# Weekly commitments

## Individual contribution of each participant

| Team Member           | Contribution                                                                                    | Artefacts | 
|-----------------------|-------------------------------------------------------------------------------------------------|-----------|
| Anna Belyakova (Lead) | Updated one-zero-eight repositories (configured launch via docker, removed irrelevant ml usage), outlined the immediate tasks for all areas of project work |[Commit](https://github.com/IU-Capstone-Project-2025/Inno-Services-Search-Backend/commit/b0aa0b004c8e38896866f57516450f698ba51fdd), [team management artefacts](https://docs.google.com/document/d/1WamLxAam8864_ut_-ajJb7jrpumyyM21-jONnoYv8Xc/edit?usp=sharing)|
| Vladimir Paskal       | Wrote user stories, studied one-zero-eight repositories to find out which services already have APIs, prioritized services for parsing (to start from the most accessible)| [List of services to start from and their API if available](https://docs.google.com/document/d/1XM7tfhPSQ2npRn6oPqqCARInRovXSG4OaiP1dlMo2fk/edit?usp=sharing) |
| Azaliia Alisheva      | Studied the source repository of the backend, searched for all available info services for the project        | [Services list](https://docs.google.com/document/d/1-H1Ehg0a6mOEHk5WTfNokDm04soi-WPtGF9FZ1uf-nY/edit?usp=sharing) |
| Aliia Bashirova       | Studied the repository of the frontend, hepled with report writing, started work in figma with very basic version of search page | [Figma basic sketch](https://www.figma.com/design/M4RIWYSKjVPz931J6nWERK/Untitled?node-id=0-1&t=23XeUUL4uMfx0tgv-1)|
| Sofia Pushkareva      | Studied vector databases                                                                        | [Comparison table](https://docs.google.com/spreadsheets/d/15UXyz4b-uMg8fkPI5ZbNQRJzdMZ3gHnekLKNU81r_7Y/edit?usp=sharing)|

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).