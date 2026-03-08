# Week 6

## Links

**Specify here all the necessary links to your website, application installer, final demo, etc.**

### Deployment: Link to the final, deployed version of the project.
[Goalsight.ru](https://goalsight.ru/)
### Code repository: Link to the final code repository state
[Repo Link](https://github.com/IU-Capstone-Project-2025/GoalSight)
### API Docs: Link to README, API docs
[See README.md](https://github.com/IU-Capstone-Project-2025/GoalSight) 

[Swagger](http://localhost:8000/swagger/)(When backend is running)   

### Design: Link to Figma
[Figma](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=382-3671&t=BJdM8xJqsh9Fh4Pf-1)



## Final deliverables

### Project overview
#### Project Description

GoalSight is an AI-powered web platform serving as a centralized hub for football analytics. It aggregates advanced statistics from reliable sources like WhoScored, providing intuitive tools for users such as coaches, fans, and journalists to analyze teams, matches, and tournaments efficiently. The focus is on simplifying data access, enabling quick insights, and enhancing engagement through predictive features.

##### Problems It Solves

GoalSight tackles common challenges in football data handling:

- Coaches spend excessive time manually collecting data from various platforms for match preparation and training.
- Fans struggle with accessing clear, advanced stats for teams and tournaments, which reduces their engagement.
- Journalists and analysts waste effort on verifying and organizing data from fragmented, hard-to-navigate sources.
- Overall fragmentation leads to inefficiencies, lost strategic opportunities, and lower interaction with valuable football data.


##### Key Features
- **Interactive Visualizations and Summaries**: View basic team statistics like goals, possession, and xG upon expanding a team.
- **Intuitive Search and Filtering**: Easily select teams and metrics for quick overviews and comparisons.
- **AI-Based Match Predictions**: Select any two teams to generate real-time probabilities for win, draw, or loss, based on historical data.
- **Upcoming Matches Overview**: Home page displays a list of future games with predicted win probabilities.
- **Centralized Data Hub**: User-friendly interface integrating stats from APIs, with navigation for all user types.


### Features
- Home page displaying upcoming matches (e.g., FIFA Club World Cup 2025 fixtures) with win probability percentages.
- Team selection interface for choosing two teams from a list (e.g., Real Madrid, Juventus, Paris Saint-Germain) to run AI predictions.
- Real-time match forecast generation, showing outcomes like "Real Madrid vs Juventus: 32% - 67%".
- Expandable team views revealing basic statistics such as goals, possession, and xG.
- Integration with data APIs (e.g., WhoScored) for aggregating reliable football metrics.
- Simple predictor explanation: Steps to select teams and get AI-powered match probabilities.
- Basic navigation including home, tournament views, and predictor tool.


### Tech stack
Technology:
- **Frontend:** Node.js 18, React 18, TypeScript, Tailwind CSS, Axios for API calls
- **Backend:** Python, Django
- **Database:** PostgresDB
- **Other tools:** REST API


### Setup instructions

#### Quick Start

##### Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/IU-Capstone-Project-2025/GoalSight.git
   cd GoalSight
   ```
2. Decrypt the environment variables file:
   ```bash
   cd docker/local
   gpg --decrypt .env.gpg > .env
   ```
   > You will need a password to decrypt. If you don't have it, contact the [team lead](https://github.com/Arino4kaMyr).
3. Start the services:
   ```bash
   docker-compose up --build
   ```
- Backend: http://localhost:8000/
- Frontend: http://localhost:3000/



### Plan for the live demo.
1. **Start at the Home Page**
2. **Show Team Stats Functionality**
3. **Navigate to the Predictor/Teams Page**
3. **Demonstrate AI Predictor**
4. **Interactive Q&A**

## Presentation draft
[Link to Figma Slides](https://www.figma.com/deck/sKvgDjSToX0KR5gXtrPQu4/GoalSight?node-id=1-119&t=jevtzmwvgIQSoZMb-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1)

## Individual contribution of each participant

- **Arina Zimina**:  
  - API docs | [See README.md](https://github.com/IU-Capstone-Project-2025/GoalSight) 
  - Collecting data for dataset 
  - Cleaning the code (removing unused parts) & comments on the code| [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/7dc15fafb232f5dd0170df445d7cd940536d5c66) 
  - Enabling ssl certificates and adding a https connection | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/cbd4c8a7e6c13f50fe2b1faf69b3ec13a2dce719)


- **Artem Panov**:
  - PM:
    - Template for individual contribution of each participant part in report.
    - Meeting organization and Task distribution | [Link to Kanban board in Weeek](https://app.weeek.net/ws/809762/shared/board/oOOPwpKcegOdA0POz8h39PopnsQnCPWe)

  - ML:
    - Data Preprocessing Update (PCA) | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/pull/69/commits/3df0d410e9e8e55a58d31f01d0c7eaca70bdf0db)
    - Adding time scales for all model features | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/pull/69/commits/3df0d410e9e8e55a58d31f01d0c7eaca70bdf0db)
    - Cleaning the code (removing unused parts) | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/bace9aabeaad7c316e5ad9dc72ed393884e198fe)
    - Comments on the code | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/bace9aabeaad7c316e5ad9dc72ed393884e198fe)
    - Description of the ML part for frontend | [Link to google disc](https://drive.google.com/file/d/18CcD48lV_RY-1Gg_v0YaGn06Elg2YubS/view?usp=sharing)


- **Karina Siniatullina**: 
  - Prediction on home page. | On the home page, where there are upcoming matches, there is now a button to predict the result for each upcoming match. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/db6243733d683e8d94e3e657508f15e2fe71f290) 
  - Statistics info. | Added info about each statistic and changed its design. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c4b1ed61c6f786b32c06ef6bb513ef8dee2e7843) 
  - More statistics. | Added more statistics for all teams and added tabs and their distribution. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/745ce3eb1bde3ea1a8c1f97247d72f7d48dd1e83) 
  - Forecast panel. | Added a logo to the commands and changed the text of the description of how the forecast is calculated. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/475bb1d13f651aa712201b77835c152cfcf1f831) 
  - Component tests. | Сhanged the unit tests because the design of some components has changed. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/911a3c95ff8cab144fe86c05af5568e906044337) 
  - Figma. | Added the Final version frame, which displays the entire final design of the site. | [Link to commit](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=382-3671&t=BJdM8xJqsh9Fh4Pf-1) 
  - Comments for part of frontend side. | Added comment for component tests, cypress test and ui components. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/e8dab87f8d8dfa74abce782163150867ec864868)


- **Egor Sergeev**:
  - Create a draft presentation | [Link to Figma Slides](https://www.figma.com/deck/sKvgDjSToX0KR5gXtrPQu4/GoalSight?node-id=1-119&t=jevtzmwvgIQSoZMb-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1)
  - Write a weekly report.


- **Egor Agapov**:  
  - Transferring the project to another staging server 
  - Fixing frontend tests (integration API tests and e2e test) | [Link to first commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/67f2e8432692d78eb7e1f0cc60a4dd76dcd466e2) | [Link to second commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/de30e87df6f0a33acd3205eeef9241ff021eb6a3) 
  - Enabling ssl certificates and adding an https connection | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c9b6aa948a3e84458f9b28997ce6c175509cbc1b) 
  - Building a single pipeline without dividing it into a frontend and backend part | Reducing the test run time in the pipeline when pushing | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/6cbd34df747d4f1b6a56a7f98f22aa75133e158a) 
  - Making the Goalsight label clickable and linking to the homepage and changing some of the displayed text on the pages | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/a17f4ed43081ab00d52b5207907a92ecca12c222) 
  - Correcting the translation of the website into Russian | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/6ff0f9586ba92334f36057ff0ca26d931a8947a3) 
  - Writing comments for the frontend part of the project | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/94329135654bc9f73af65474d65c4f53b88576e8)
## Weekly commitments
### Plan for Next Week
Successfully present our project to TAs and peers.