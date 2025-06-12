# Week #1

## Project description

**Project name:** GoalSight

**Code repository:** [GitHub Repository](https://github.com/IU-Capstone-Project-2025/GoalSight)

### Problem Statement

- **Coaches** are forced to manually compile relevant data from various platforms to prepare for matches and training, spending valuable time on routine analytical tasks.  
- **Fans** struggle to access clear and insightful overviews of team and tournament-level advanced stats, which limits engagement with analytical content.  
- **Sports journalists and analysts** invest excessive time verifying and structuring data because existing platforms are hard to navigate and poorly organized.  

This fragmentation results in inefficiencies, lost opportunities for strategic insights, and lower engagement with rich football data.

### Importance of the Problem

A centralized and user-friendly analytics hub is essential for:

- Improving match preparation and training for teams through accessible data  
- Enhancing the speed and quality of analytical reporting for journalists  
- Boosting fan engagement through visualized, advanced metrics and match insights  
- Reducing time spent on data discovery, processing, and validation  

### Our Solution

We are building a web-based platform powered by AI that aggregates, structures, and presents advanced football statistics from multiple reliable sources. The system will:

- Provide interactive visualizations and summaries for teams, tournaments, and players  
- Allow intuitive search and filtering of relevant metrics  
- Offer **AI-based match result predictions**, giving users deeper insights into likely outcomes  
- Serve as a centralized hub for all stakeholders in football analytics — coaches, fans, and media professionals  

This platform will not only centralize football data but also empower users with prediction tools and high-quality visual content, making analytics accessible, efficient, and engaging.

## Team Members

| Team Member | Telegram Alias | Email Address | Track | Responsibilities |
|---------------------------------|----------------|----------------|------------------------------|------------------|
| Arina Zimina *(Lead)*       | @arino4ka_myr       | a.zimina@innopolis.university | Fullstack                      | Frontend design, interaction with the backend and ML |
| Artem Panov | @Tema_eto_tema       | a.panov@innopolis.university | ML/PM                      | Data preparation, ML models design and learning |
| Karina Siniatullina                | @karishka1222       | k.siniatullina@innopolis.university | Frontend                      | Website visualization, interaction with the backend and ML |
| Egor Sergeev                | @clotjh       | e.sergeev@innopolis.university | Design                      | Frontend design, Website visualization |
| Egor Agapov                | @AEZuraa       | e.agapov@innopolis.university | Frontend/ML                      | Frontend design, data preparation, weekly reports |

---

## Brainstorming

### Ideas during brainstorming

1. **Idea 1** – Football Match Forecasting
2. **Idea 2** – Movie Swiping App
3. **Idea 3** – Hairstyle selection or clothing selection (for filmmakers, for marketplaces, for retail, etc.)
4. **Idea 4** - AI tutor for the "Unified State Exam"

### Brief market research / problem validation

- **Idea 1: Football Match Forecasting**

  **Relevance:**  
  Advanced match prediction tools are in demand among key stakeholders in the football ecosystem.

  **Target Audience:**  
  - Coaches  
  - Football fans  
  - Sports journalists  

  **Competitors:**  
  - **FiveThirtyEight (Algorithm-based):**  
    Provides fairly accurate predictions (e.g., correctly predicted winners in 3 out of 5 top leagues).  
    ❌ No user interface  
    ❌ Doesn’t account for draws  
    ❌ No explanation of how predictions are made  

  - **Betting Apps:**  
    Use real-time statistics for predictions.  
    ❌ Money-based bets  
    ❌ Overloaded and cluttered interfaces  

  **Validation:**  
  Existing tools do not sufficiently explain or visualize predictions. There is a gap for an intuitive, transparent forecasting platform that avoids gambling connotations and improves user experience.


- **Idea 2: Movie Swiping App**

  **Relevance:**  
  With increasing use of streaming platforms, users face decision fatigue when selecting what to watch. A swipe-based interface could simplify discovery and make it more engaging.

  **Target Audience:**  
  - Active users of movie recommendation or streaming apps  

  **Competitors:**  
  - **Queue:**  
    Swipe-based app for choosing movies/TV shows with friends.  
    ❌ Limited selection familiar to Russian-speaking audiences  
    ❌ No info on streaming availability  

  - **Streaming service apps (e.g., Netflix, Kinopoisk):**  
    Large catalogs of movies/TV shows available for immediate viewing.  
    ❌ No swipe-based discovery or collaborative decision-making  
    ❌ No filtering by similar movies or shared preferences  

  **Validation:**  
  Social discovery for movie selection is underdeveloped. A more interactive, swipe-based platform with real-time collaboration features could significantly improve group decision-making.

---

## Basic requirements

### Target users and their primary needs

- **Coaches**  
  Need quick and structured access to advanced football statistics for effective match preparation and training planning.  
  ❌ Currently waste time collecting data from scattered sources  
  ✅ Want centralized dashboards, tactical summaries, and team analytics

- **Football fans**  
  Want intuitive and engaging overviews of team performance and tournament stats to stay informed and deepen their involvement in the sport.  
  ❌ Existing platforms are too technical or hard to navigate  
  ✅ Prefer visual summaries, rankings, and AI-based match predictions

- **Sports journalists and analysts**  
  Require reliable and well-structured data to create high-quality analytical content quickly.  
  ❌ Spend too much time cleaning and verifying information  
  ✅ Need exportable stats, summaries, and explanations of predictive models

> All these users share a common pain point: **current platforms are fragmented and unintuitive**, lacking in both functionality and user experience.  
> Our platform addresses this by providing a **centralized AI-powered hub** with visualized stats, match predictions, and intuitive navigation.

---

### User stories

- As a football team coach, I want to receive match predictions match analysis of the opponent's weaknesses so that I can better prepare tactics, lineups, and training strategy.
- As a football fan, I want to see probable match outcomes for my favorite team so that I can engage in debates with friends and track league standings.
- As a sports journalist, I want to use prediction data in my analytical articles so that I can create more informed pre-match reviews.

---

### Initial scope

A web page with an AI tool that aggregates and structures advanced
football statistics from various sources, provides convenient visualizations and
summaries of teams and tournaments, and allows you to quickly and intuitively find
the information you need. The platform will become a central hub for all football
analytics and will greatly simplify the work of coaches, journalists and fans.

---

### MVP scope

A website with football statistics, with tools for useful representation and visualisation - tables with filters and diagrams and AI tool for prediction of results of collision of teams. 

---

## Tech-stack

- **Frontend**: Node.js 18, React 18, TypeScript, Tailwind CSS, Axios for API calls
- **Backend**: Python, Django
- **Database**: PostgresDB
- **Other tools**: REST API

---

## A brief explanation of technology stack


### Frontend: React.js

#### Why Chosen:
- Interactivity: React provides a dynamic and responsive interface for visualizing football analytics (charts, dashboards), improving navigation and data perception.
- Scalability: Its component-based architecture simplifies adding new features (e.g., player profiles, live statistics).
- Ecosystem: Support for libraries like Chart.js for visualizations and React Query for API handling makes it suitable for real-time analytics.

#### Problem Addressed:
An intuitive UI solves the issue of poor navigation and inaccessibility of advanced statistics for fans and journalists.

### Backend: Django (Django REST Framework)

#### Why Chosen:
- Asynchronicity: Django with async support (via ASGI) enables handling real-time requests, such as live match statistics.
- Scalability: Built-in tools (ORM, admin panel, authentication) simplify managing complex data and user roles (coaches, journalists), while its modular structure supports platform growth.
- Reliability: A mature framework with strong security and community support, crucial for long-term projects.

#### Problem Addressed:
Centralizes data from multiple sources, accelerates access to analytics, and simplifies preparation for coaches and journalists.

### Machine Learning: Python

#### Why Chosen:
- Versatility: Python unifies backend and ML, simplifying the integration of models (e.g., xG predictions or tactical analysis) into the platform.
- Libraries: Pandas, Scikit-learn, and TensorFlow enable building scalable analytics models (e.g., match outcome predictions).
- Flexibility: Supports both simple models (for MVP) and complex ones (e.g., video analysis), ensuring the evolution of analytical capabilities.

#### Problem Addressed:
Automates data collection and analysis, providing coaches and journalists with ready insights and fans with engaging statistics.

#### Additional (Infrastructure)

- PostgreSQL: For storing structured data (statistics, matches, players) with scalability support.
- Docker: Simplifies deployment and ensures environment consistency.
- Redis: Caching to speed up access to frequently used data (e.g., live statistics).

---

## Weekly contribution

### Individual contribution of each participant

- **Arina Zimina**:
  - GitHub Repository setup. | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/99cf2b0622ac997c86837da97928bca06a790826)
  - Brief market research/problem validation for top 1–2 ideas. [Link to google disc](https://docs.google.com/document/d/1URM2aJgmpOyZOtoX8QOIdzx356njD-aO/edit?usp=sharing&ouid=102622026097705461090&rtpof=true&sd=true)
  - Template for backend side | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/02eaafe1ebf7fdb50b9a45f42a9151855c2f543b)

- **Artem Panov**:
  - Individual contribution of each participant part in report
  - Meeting organization and Task destribution | [Link to Kanban board in Weeek](https://app.weeek.net/ws/809762/shared/board/oOOPwpKcegOdA0POz8h39PopnsQnCPWe) | [Link to Miro board with ideas](https://miro.com/welcomeonboard/MUJQY0xDdVE2dlA4VU9QM014UXkxR1FCSUZrNWhSRGUrZVBZVWNaMjdZY1hjRStBYjhOVjZnQjNvUm1kdmV5emQ2NllkRmsxWGJVQ2cwZnBWY2tQaVBZVWVVQWNxZ2RLOUhUR0RmMlY5dER4dVUwVXRlanVqNGNLYUVabkVxNTlBS2NFMDFkcUNFSnM0d3FEN050ekl3PT0hdjE=?share_link_id=698316100792)

- **Karina Siniatullina**:
  - Formalise 3 user stories.
  - Template for frontend side. | [Link to commit GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f5d68d0379a46ae3e9bbf311863824c91d83ba32)

- **Egor Sergeev**:
  - Formalisation of problem statement | [Link to google disc](https://drive.google.com/file/d/1mUMPJ2W-dWslX6Siw1hNXchHz7tpfQXf/view?usp=drive_link)
  - A brief explanation of technology stack | [Link to google disc](https://drive.google.com/file/d/1SNdZaXo3aOgLdQM_cuEebPwVELcNnRt8/view?usp=sharing)

- **Egor Agapov**:
  - Report
  - Name of project.

## Weekly commitments

### Sprint goal: 

**Create a data structure, a prototype user interface with basic analytics to demonstrate the value of the platform — centralized access to football statistics with AI tools.**

**Success criteria:**

- Implemented ERD with basic entities
    
- Ready-made design system and interactive prototype
    
- Processed and normalized data for testing
    
- A simple model for predicting match results
    
- Specific filtering and sorting options for tables

## Frontend:

1) Selection of parameters for representation in tables | Write list of parameters for representation in tables.
----------------|-----------------
2) Selection of  filters in tables | Write list of filters in tables.
----------------|-----------------
3) Selection of  parameters for sorting data in tables | Write list of parameters for sorting data in tables.
----------------|-----------------
4) Low-fi prototype (UX) | A low-fidelity prototype is a simplified and rough version of a product or design concept, used early in the design process to test ideas, gather feedback, and validate concepts. (UX)
----------------|-----------------
5) UI design preprocessing | colors, font, photos, peactures
----------------|-----------------
6) Development of figma prototype based UI design preprocessing and Low-fi prototype | A figma prototype that displays user stories
----------------|-----------------

## Backend:
1) DB design as ERD diagram | Create ERD diagram
----------------|-----------------
2) ERD implementation | ///
----------------|-----------------
## ML:
1) Feature selection | List of features
----------------|-----------------
2) Data parsing | All data in .csv
----------------|-----------------
3) Data preprocessing | Select features from list (1) and data normalization and data separation.
----------------|-----------------
4) Simple model design | Simple classifier (e.g. sigmoid function)
----------------|-----------------