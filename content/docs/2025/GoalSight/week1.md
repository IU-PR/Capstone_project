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

## Weekly commitments

### Individual contribution of each participant

- **Arina Zimina**: Brief market research/problem validation for top 1–2 ideas, template for backend side, brainstorm to find ideas
- **Artem Panov**: Report, brainstorm to find ideas, meeting organization, task destribution, task formalisation
- **Karina Siniatullina**: User Story, template for frontend side, brainstorm to find ideas
- **Egor Sergeev**: Formalisation of problem statement, a brief explanation of technology stack, brainstorm to find ideas
- **Egor Agapov**: Report, name of project, brainstorm to find ideas