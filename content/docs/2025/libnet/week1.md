# Project description
## Project name: LibNet
**Code repository:** https://github.com/IU-Capstone-Project-2025/libnet

**Project Idea:**
LibNet is a service that unifies the search of the books for a user, making it more simple. Libraries can plug into our system to keep track of available books and let users reserve them easily.  The aggregator is built to work with many libraries at once, so everything stays organized and simple to reach.

**Problem Statement:**
Many libraries struggle with outdated, clunky websites that lack functionality and a pleasant user experience. This makes it harder for students and staff to access resources efficiently.



| Team Member      | Telegram Alias    | Email Address                   | Track                                      | Responsibilities                                                                                 |
|------------------|-------------------|---------------------------------|--------------------------------------------|--------------------------------------------------------------------------------------------------|
| Ivan Murzin      | @alliumpro        | i.murzin@innopolis.university   | TeamLead, DevOps Engineer, Frontend Developer, UX/UI | Designed UX/UI, assists with frontend development, and performs DevOps tasks                     |
| Aliya Sagdieva   | @aliushka_sgdv    | a.sagdieva@innopolis.university | Technical Writer, Backend Developer        | Prepares weekly progress reports and contributes to backend implementation                       |
| Alena Averina    | @flowelx          | a.averina@innopolis.university  | DevOps Engineer, Technical Writer          | Performing DevOps tasks and preparing weekly reports.                                            |
| Anna Serova      | @kbvsp            | a.serova@innopolis.university   | Lead Frontend Developer                    | Handling all frontend development tasks.                                                         |
| Artem Ostapenko  | @ostxxp           | a.ostapenko@innopolis.university| Lead Backend Developer, Project Manager    | Organization of work and communication. Maintaining FastAPI (Python). Develops backend services. |

# Brainstorming 
## Ideas during brainstorming
### Financial Tracker App
An app to track personal finances by integrating with bank APIs. Features include importing transactions from banks, spending forecasts, expense analysis, and suggestions for improving financial habits.
### Concierge Service for Hotels
A service to enhance the guest experience in hotels. Features include hotel registration, voice assistant for handling guest requests, AI-powered restaurant orders, climate control in rooms, and information about local events and attractions. Guests can also book taxis or send items to the laundry via the in-room interface.
### Library Website
A user-friendly website where users can search for books, check availability across multiple libraries, and reserve books online. Additional features include book recommendations, booking history tracking, interfaces for both readers and library administrators, and filtering and search options.


## Brief market research / problem validation
### Financial Tracker App
**Problem**: Many individuals struggle with managing personal finances due to a lack of real-time tracking.  Manual expense tracking is time-consuming, and existing apps often have limited bank integrations.\
**Reason for Rejection**: Banks' APIs are difficult to use due to legal restrictions, financial costs, and privacy concerns.


### Concierge Service for Hotels
**Problem**: Hotel guests often face delays in service requests (room service, housekeeping, booking tours), and staff spend excessive time handling routine inquiries manually.\
**Reason for Rejection**: The implementation is complex, and our team lacks the necessary resources to develop such a solution.


### Library Website
**Problem**: Many library users struggle to find and reserve books efficiently, especially when dealing with multiple libraries. Existing systems are often outdated or lack user-friendly features.\
**Validation**:
Competitor analysis shows that most library websites lack advanced features like personalized recommendations or multi-library search.\
Libraries are open to digital solutions that improve user experience and operational efficiency.\
**Selected Idea**: This idea was chosen due to its feasibility, clear value proposition, and alignment with our team's capabilities.

# Basic requirements

## Target Users and their primary needs:
1)Students – Easy access to books, research materials, and library services.\
2)Library Administrators – A simple, customizable platform to manage their digital presence.

## Initial Scope (MVP – First Version):
1)Book Catalog – Display book cards with key details (title, author, availability).\
2)User Accounts – Sign-up/login for readers and library staff.\
3)Book Reservation – Allow users to reserve books online.\
4)Personal Dashboard – Basic user profile and reservation history.

## Future Scope (Post-MVP):
1)Search & Filters – Find books by title, author, genre, etc.\
2)Favorites List – Save preferred books for quick access.\
3)Admin Panel – Manage books (add/edit/remove), track reservations, and update statuses (e.g., "checked out," "reserved").

## High-Level User Stories:
### For Students:
1)As a student, I want to see book cards with title, author, and availability status so I can 
quickly find the books I need.\
2)As a student, I would like to register or log in to my account to access book reservations.\
3)As a student, I want to reserve books online and then pick them up from the library.\
4)As a student, I want to see my current bookings and history to keep track of the books I have borrowed.
### For Library Staff:
1)As a librarian, I want to add, edit and remove books from the catalog to keep the database up to date.\
2)As a librarian, I want to see the list of reserved books so that I can prepare them for checkout.

### Additional functionality (Post-MVP)
1)As a student, I want to search for books by title, author, and genre to find the materials I need faster.\
2)As a student, I want to save my favorite books in a separate list so that I can easily return to them later.\
3)As a librarian, I want to mark books as "out," "in stock," or "on hold" to track their availability.

## Tech Stack
To ensure scalability, high performance, and development convenience, we have selected the following technology stack.

**Backend:**

**Python.** Python’s simple syntax and vast libraries enable fast 

**FastAPI** is a modern framework that delivers:

- High performance.
- Seamless integration with PostgreSQL.
- Support for asynchronous queries.

**Frontend:**

**React** is a widely used framework for building interfaces. It simplifies the creation of reusable components (e.g., book cards, reservation forms) and scales well for future features like favorites and advanced filters.

**Vite** is a fast build tool that accelerates development.

**Database:**

**PostgreSQL** offers a reliable relational structure, making it ideal for complex queries. It is also highly flexible and scalable—new tables can be added effortlessly, and it includes built-in JSON support.

**DevOps:**

**Docker** Containerization ensures consistent environments from development to production. 

**GitHub Actions** Automates CI/CD pipelines with:\
Automated testing on pull requests.\
Seamless deployment to staging/production.

For task management and project coordination, our team uses **ClickUp**.

## Weekly commitments
### Individual contribution of each participant
| Team Member     | Completed Work                                                                                        |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Ivan Murzin     | Started UX/UI design development                                                                      |
| Aliya Sagdieva  | Сreated a report and started UX/UI design development                                                 |
| Alena Averina   | Implemented containerization using Dockerfiles and Docker compose, participated in report preparation |
| Anna Serova     | Started UX/UI design development                                                                      |
| Artem Ostapenko | Created boilerplate and base for API launch<br/>                                                           |

Link to design in Figma: https://www.figma.com/design/PEK6pAX4gh7f5oO9C0jNfq/libnet?node-id=0-1&t=sEVJZ4Fg0AY8jxIw-1

# Confirmation of the code’s operability

We confirm that the code in the main branch:

- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the README.md). 