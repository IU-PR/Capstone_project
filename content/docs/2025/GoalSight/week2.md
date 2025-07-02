# Week #2

## Detailed Requirements Elaboration

### Detailed user stories with acceptance criteria for the MVP

#### User story for coaches

- As a football team coach, I want to see basic statistics of any team and a simple match prediction between two selected teams so I can get a quick overview of potential opponents.

#### Acceptance Criteria

- On the team list page, you can select any two teams and get a forecast
- When the team is expanded, basic statistics are displayed

#### User story for football fans

- As a football fan, I want to check the upcoming matches and see a simple win probability for any two selected teams so I can discuss possible outcomes with friends.

#### Acceptance Criteria

- The main page displays a list of upcoming matches
- On the teams page, you can select two teams and see the percentage of each team's probability of winning

#### User story for journalist and analyst

- As a sports journalist and analyst, I want to access basic team statistics and a simple match prediction to reference in quick articles or social media posts.

#### Acceptance Criteria

- User can select two teams and get a forecast
- User can open any command and see the minimum statistics

### Prioritized Backlog

- [Link to backlog](https://app.weeek.net/ws/809762/project/1/board/3)

## Project Specific Progress

## Design

### Layout of the main pages of the website and basic user flow diagrams for key interactions

- [Link to layout in Figma](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)

## Frontend

### Frontend project structure
```
frontend/              # React frontend
├── src/               # Source files
│   ├── pages/         # Application pages
│   ├── components/    # Reusable components
│   ├── api/           # API clients and requests
│   ├── styles/        # Global styles and themes
│   ├── utils/         # Helper functions
│   ├── types/         # TypeScript types and interfaces
│   ├── constants/     # Constants and configurations
│   ├── assets/       # Static resources (images, icons)
│   └── index.tsx      # Application entry point
├── public/            # Static files
├── package.json       # Node.js dependencies
├── tsconfig.json      # TypeScript configuration
├── tailwind.config.js # Tailwind CSS configuration
└── postcss.config.js  # PostCSS configuration
```
### Skeleton components based on initial design

- [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/650087ed555049634e47a272864f4b931080824a)

## Backend

### Initial API contract

- [Link to API doc](https://editor.swagger.io/?url=https://raw.githubusercontent.com/IU-Capstone-Project-2025/GoalSight/main/openapi.yaml)

### Initial database schema

Each team can participate in multiple matches as both the home team (home_team) and the away team (away_team), which creates two one-to-many relationships between Team and Match. Additionally, each team can take part in multiple tournaments, and each tournament can include multiple teams, forming a many-to-many relationship between Team and Tournament.

- [Link to ERD](https://drive.google.com/file/d/1y5h6sagHA8bIGDpwj2m-uwIarY8R_WIz/view?usp=sharing)

### Implement one or two basic, non-functional (dummy data) endpoints.

- [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/5b78c11bf233931565e0be0a47a5ab3a86c45009)

## ML

### Research Objective

It shows the main stages of work on the preparation of training data and the design of models and neural networks for classifying the outcomes of football matches.

### Dataset Overview

#### Data Sources Integration

| Database | Content | Records |
| :-- | :-- | :-- |
| European Soccer Database | Match results, team/player attributes, leagues | Primary source |
| World Soccer Database | Betting odds, complementary statistics | Secondary |
| FIFA Players Dataset | Detailed player attributes, skills, market values | Player data |
| International Football Results | Historical matches (1872-2025) | Historical context |

#### Dataset Characteristics

| Metric | Value |
| :-- | :-- |
| **Total Matches** | 25,979 |
| **Features (Original)** | 331 |
| **Features (Cleaned)** | 296 |
| **Data Completeness** | 75.5% |
| **Complete Records** | 19,603 |

### Data Processing Pipeline

#### Feature Categories

| Category | Features | Description |
| :-- | :-- | :-- |
| **Match Information** | 2 | Tournament stage, season encoding |
| **Team Tactical Attributes** | 16 | Build-up play, chance creation, defensive metrics |
| **Betting Market Data** | 3 | Bet365 odds (home/draw/away) |
| **Player Statistics** | 38 | Overall ratings, technical skills, physical attributes |

#### Data Cleaning Results

| Process | Original | After Cleaning |
| :-- | :-- | :-- |
| Features | 331 | 296 |
| Missing columns removed | - | 35 |
| NaN records | 24,217 | 6,376 |
| Complete records | 1,762 | 19,603 |

### Machine Learning Models

#### Model Architectures

| Model | Architecture | Key Parameters |
| :-- | :-- | :-- |
| **MLP Neural Network** | Input → Hidden(32) → Hidden(16) → Output(3) | Dropout: 0.5/0.3, Early stopping |
| **Logistic Regression** | Grid Search optimization | C: [0.01-100], Solvers: lbfgs/saga |

#### Training Configuration

| Aspect | MLP | Logistic Regression |
| :-- | :-- | :-- |
| **Class Weighting** | Weighted random sampling | Inverse frequency weights |
| **Validation** | Early stopping (patience=10) | 8-fold cross-validation |
| **Optimization** | AdamW, weight decay=1e-4 | Grid search hyperparameters |

### Results and Performance

#### Model Performance Comparison

| Model | Accuracy | Best Hyperparameters |
| :-- | :-- | :-- |
| **MLP Neural Network** | 41% | Hidden: 32/16, LR: 5e-4 |
| **Logistic Regression** | 49% | C=0.01, solver='lbfgs' |

#### Detailed Classification Results

| Outcome | MLP Precision | MLP Recall | MLP F1 | LR Precision | LR Recall | LR F1 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **Home Win** | 0.78 | 0.23 | 0.36 | 0.64 | 0.51 | 0.57 |
| **Away Win** | 0.49 | 0.54 | 0.51 | 0.49 | 0.56 | 0.52 |
| **Draw** | 0.28 | 0.59 | 0.38 | 0.30 | 0.36 | 0.33 |

### Research Limitations and Future Directions

#### Current Limitations

| Area | Limitation | Impact |
| :-- | :-- | :-- |
| **Data Quality** | Missing player lineups (some matches) | Reduced feature completeness |
| **Feature Coverage** | No formation/tactical data | Limited tactical analysis |
| **Real-time Data** | Static historical dataset | No live match integration |

#### Enhancement Opportunities

| Category | Improvement |
| :-- | :-- |
| **Data Sources** | API integration for live data, weather conditions |
| **Features** | Team formations, player injury status, referee statistics |
| **Models** | Ensemble methods, deep learning architectures |
| **Deployment** | Real-time prediction pipeline, web interface |

### Conclusion

Logistic regression showed 49% accuracy and provided more balanced forecasts than the neural network.
The dataset provides a solid foundation for match analytics, although it needs to be improved in terms of completeness and updating the data in real time.
Adding streaming data and using ensemble methods can improve the accuracy of models in the future.

### Links to materials and artefacts
---

- [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer?resource=download)
- [World Soccer DB: archive of odds [01-JUN-2021]](https://www.kaggle.com/datasets/sashchernuh/european-football/data?select=database.sqlite)
- [fifa_players.csv](https://www.kaggle.com/datasets/maso0dahmed/football-players-data)
- [International football results from 1872 to 2025](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017/data?select=former_names.csv)
- [comprehensive_dataset.csv](https://drive.google.com/file/d/17QxXqTdFZ1uKNatLrrHk2nWGI0k749bI/view?usp=sharing)
- [Jupyter Notebook with code](https://drive.google.com/file/d/1uLc3iZOqxnea1GiHvL-grV9UcBi0ungA/view?usp=sharing)

## Individual Contribution of Each Participant

- **Arina Zimina**:
  - ERD implementation. | Django models created, migration files generated | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/5b78c11bf233931565e0be0a47a5ab3a86c45009)
  - DB design as ERD diagram. | Tournament, Match, and Team entities  | [Link to ERD](https://drive.google.com/file/d/1y5h6sagHA8bIGDpwj2m-uwIarY8R_WIz/view?usp=sharing)
  - (Backend) Links to PRs/Issues for initial endpoints, link to API documentation. | [Link to API doc](https://editor.swagger.io/?url=https://raw.githubusercontent.com/IU-Capstone-Project-2025/GoalSight/main/openapi.yaml)


- **Artem Panov**:
  - PM:
    - Individual contribution of each participant part in report.
    - Meeting organization and Task destribution | [Link to Kanban board in Weeek](https://app.weeek.net/ws/809762/project/1/board/3)

  - ML:
    - Data preprocessing. | Select features from list and data normalization and data separation. | [Link to Jupyter Notebook with code.](https://drive.google.com/file/d/1uLc3iZOqxnea1GiHvL-grV9UcBi0ungA/view?usp=sharing)
    - Data parsing. | Open source data search. | [Link to Jupyter Notebook with code.](https://drive.google.com/file/d/1uLc3iZOqxnea1GiHvL-grV9UcBi0ungA/view?usp=sharing)
    - Feature selection. | Selection of the most influential features based on football data. | [Link to Jupyter Notebook with code.](https://drive.google.com/file/d/1uLc3iZOqxnea1GiHvL-grV9UcBi0ungA/view?usp=sharing)
    - Simple model design. | Simple classifier (e.g. sigmoid function) | [Link to Jupyter Notebook with code.](https://drive.google.com/file/d/1uLc3iZOqxnea1GiHvL-grV9UcBi0ungA/view?usp=sharing)
    - (ML) Summary of research, link to dataset or data collection plan. | A well-structured report which shows the main stages of work on the preparation of training data and the design of models
and neural networks for classifying the outcomes of football matches. | [Link to (ML) Summary of research, link to dataset or data collection plan.](https://drive.google.com/file/d/1FChTesY5RQDcpFcIAfp1vSHqNrEtFqO7/view?usp=sharing)

- **Karina Siniatullina**:
  - Updated/detailed user stories with acceptance criteria.
  - Low-fi prototype(UX). | A low-fidelity prototype is a simplified and rough version of a product or design concept, used early in the design process to test ideas, gather feedback, and validate concepts. (UX) | [Link to Figma.](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)
  - Development of figma prototype based UI design preprocessing and Low-fi prototype. | A figma prototype based on low-fi prototype that displays user stories. | [Link to Figma.](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)
  - (Designers) Wireframes/mockups. | Clickable prototypes of the two main pages of the site  | [Link to Figma.](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)
  - (Frontend) Links to PRs/Issues for skeleton pages/components. | Basic implemented skeletons of two pages | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/650087ed555049634e47a272864f4b931080824a)

- **Egor Sergeev**:
  - UI design preprocessing. | Choosing a color scheme for a page, fonts, and searching for references for a web page. | [Link to Figma.](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)
  - Development of figma prototype based UI design preprocessing and Low-fi prototype. | A figma prototype based on low-fi prototype that displays user stories. | [Link to Figma.](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)
  - (Designers) Wireframes/mockups. | Clickable prototypes of the two main pages of the site | [Link to Figma.](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)

- **Egor Agapov**:
    - Report
    - User flow diagrams | Three main flow diagrams | [Link to Figma.](https://www.figma.com/design/YRRZnNaqDfFbm4vQoAKMUS/CAPSTONE---GOALSIGHT?node-id=0-1&t=oa4kbOBhEUDcSbR7-1)
    - Feature selection. | Selection of the most influential features based on football data. | [Link to google disc](https://drive.google.com/file/d/1PmpNQXgoIrVn_TKk8R_CgMepQ4beDkTF/view?usp=sharing)
    - Selection of parameters for sorting data in tables. | [Link to google disc](https://drive.google.com/file/d/1lqPlGrjphc63XcmHietMCEcyCiTD9UjG/view?usp=sharing)
    - Selection of parameters for representation in tables. | Write list of parameters for representation in tables. | [Link to google disc](https://drive.google.com/file/d/1lqPlGrjphc63XcmHietMCEcyCiTD9UjG/view?usp=sharing)
    - Selection of filters in tables. | Write list of filters in tables. | [Link to google disc](https://drive.google.com/file/d/1lqPlGrjphc63XcmHietMCEcyCiTD9UjG/view?usp=sharing)


## Weekly Commitments

### Plan for Next Week

#### Frontend (React Components and Communication setup with the Backend)
- React project with TypeScript and Integration with Tailwind CSS 
	- Home page:
	1. List of upcoming matches:
		- Make a tab with the nearest match
		- Make a component for upcoming matches
		- Make a list with upcoming matches
			- Fill the list with custom data
	- Tournament page:
		1. List of commands
			- Component for each team
		- The list of commands is custom
			- Add statistics tabs to commands
		- Add basic statistics
		    - Connect the API from the backend
		2. Forecast
		- Add a checkbox to the command component
		- Add a tab for the forecast
		- Connect the API for the forecast
#### Backend
- Final configuring a Django project with PostgreSQL
- Django REST Framework endpoints
	- Endpoints for frontend and ML
		- Connect the API for frontend
		- Connect the API for ML
- Upload initial data in DB
#### ML
- Integration ML models with Django apps
	- ML project structure | Create files structure for Django ML app in structure of project
	- Store trained models | .pkl files in project
	- Create structure of API endpoints | Create one API endpoint for return prediction of the outcome of football match
	- Function of uploading models with project start
- Research of articles on data preparation for training, ensemble approaches, decision tree approaches.  (low priority on this week)
	- Summary of data preparation and ensemble methods