# Week #3

## Description of implemented MVP features and the functional user journey(s).

- Component reactive drop down list - for fans, coaches and analytics
- Banner for next match - for fans
- Setup state management in React application
- Pixel perfect design implementation - for fans, coaches and journalists/analysts
- Tournament page with statistics - for coaches, journalist and fans
- Built database architecture for teams, players, etc.
- Connected backend method to frontend
- ML for anticipating the match result - for coaches, fans, journalists

### Detailed user stories
#### User story for coaches

- As a football team coach, I want to see basic statistics of any team and a simple match prediction between two selected teams so I can get a quick overview of potential opponents.

#### User story for football fans

- As a football fan, I want to check the upcoming matches and see a simple win probability for any two selected teams so I can discuss possible outcomes with friends.
#### User story for journalist and analyst

- As a sports journalist and analyst, I want to access basic team statistics and a simple match prediction to reference in quick articles or social media posts.

## Screenshots/GIFs demonstrating the working MVP.
[Link to Demo](https://drive.google.com/file/d/1aenfQGihR3WVXlIe6HiEdcrA1hFA78qe/view?usp=sharing)

## Updated API documentation.
[Link to updated API documentation](https://editor.swagger.io/?url=https://raw.githubusercontent.com/IU-Capstone-Project-2025/GoalSight/refs/heads/main/openapi.yaml)
## ML

### Research Objective

It shows the main stages of work on the preparation of training data and the design of models and neural networks for classifying the outcomes of football matches. Also 

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
| :-- |:---------| :-- |
| **MLP Neural Network** | 41%      | Hidden: 32/16, LR: 5e-4 |
| **Logistic Regression** | 48%      | C=0.01, solver='lbfgs' |

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

Logistic regression showed 48% accuracy and provided more balanced forecasts than the neural network.
The dataset provides a solid foundation for match analytics, although it needs to be improved in terms of completeness and updating the data in real time.
Adding streaming data and using ensemble methods can improve the accuracy of models in the future.

logistic regression has been integrated into the product for MVP.

### Links to materials and artefacts
---

- [European Soccer Database](https://www.kaggle.com/datasets/hugomathien/soccer?resource=download)
- [World Soccer DB: archive of odds [01-JUN-2021]](https://www.kaggle.com/datasets/sashchernuh/european-football/data?select=database.sqlite)
- [fifa_players.csv](https://www.kaggle.com/datasets/maso0dahmed/football-players-data)
- [International football results from 1872 to 2025](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017/data?select=former_names.csv)
- [comprehensive_dataset.csv](https://drive.google.com/file/d/17QxXqTdFZ1uKNatLrrHk2nWGI0k749bI/view?usp=sharing)
- [Link to model training code/notebook, any initial model artifacts.](https://drive.google.com/file/d/1I7s4tg-F4oNqyxUcNHlj6zTBGqmae7nR/view?usp=sharing)
## Weekly Commitments
## Individual Contribution of Each Participant

- **Arina Zimina**:
  - Final configuring a Django project with PostgreSQL.| [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/9b3c0f0fae06f98c2ef72cf913e43571cd382213)
  - Django REST Framework endpoints. | Add endpoints for GET and POST requests| [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/9b3c0f0fae06f98c2ef72cf913e43571cd382213)
  - Upload initial data in DB. | Create and upload initial data into database | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/9b3c0f0fae06f98c2ef72cf913e43571cd382213)


- **Artem Panov**:
  - PM:
    - Template for individual contribution of each participant part in report.
    - Meeting organization and Task distribution | [Link to Kanban board in Weeek](https://app.weeek.net/ws/809762/shared/board/agyOlrNZ7aTbte8P0Gc4ZRyZjNOc1m7g)

  - ML:
    - Function of uploading models with project start.| [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/9ea2c81779812ac144b55d1d9385877b8289621c)
    - Create structure of API endpoints. | API endpoint for getting model prediction. | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/9ea2c81779812ac144b55d1d9385877b8289621c)
    - Storing models after training. | [Link to model training code/notebook, any initial model artifacts.](https://drive.google.com/file/d/1I7s4tg-F4oNqyxUcNHlj6zTBGqmae7nR/view?usp=sharing)
    - ML project structure. | Creating an ML service file structure in a Django project | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/9ea2c81779812ac144b55d1d9385877b8289621c)

- **Karina Siniatullina**: 
  - Tournament page: Add list of team components. | Implementation of Team model and components for teams that participate in the tournament | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/083dffb5bc890f2a3a12669d45f2cb27fe8ca006) 
  - Tournament page: Add statistics tabs to commands. | Implementation of a statistics panel for each team with tabs that make statistics by groups | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/5e12148c732d658ab28ebcc9a8272e5c4ce52d11) 
  - Tournament page: Connect the API from the backend. | Connecting to the backend via the API to display a list of the team and its statistics | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/694bc336d86bcdcd282a4228762e9b7a6a8349b9) 
  - Forecast: Add a tab for the forecast. | Implementation of a panel for predicting the result of a match | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/777e008114cdb99239927e19eca20037379dc0c4) 
  - Forecast: Connect the API for the forecast. | Connecting to the server side via the API to output match result prediction | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/694bc336d86bcdcd282a4228762e9b7a6a8349b9)

- **Egor Sergeev**:
  - Report
  - Started working with DeepSeek API for future implementation

- **Egor Agapov**: 
    - Home Page: Next match tab | Implementation of the upper part of the homepage with major information about the upcoming match. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/fd6e98be4bd288090b14499d1338dd2ecec56760) 
    - Home Page: List of upcoming matches. | An implementation of the bottom of the homepage with the four closest matches. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/fd6e98be4bd288090b14499d1338dd2ecec56760) 
    - Home page: Connect the API from the backend. | Full connection of the home page with the backend. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/e12b455238aae25f53e4ec9d60bca2b99e267d96) | [Link to another commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/47758b5818ac4cf071a86451f2308ba486f0215f)

  
### Plan for Next Week

#### Sprint Goal

  

Testing, CI/CD & Deployment Setup

  

### Frontend

  

#### Testing \& Quality Assurance

  

- **Unit Tests for React components**

    - Write unit tests for the MatchCard component

    - Write unit tests for the TeamCard component

    - Write unit tests for PredictionPanel component

    - Write unit tests for UpcomingMatches component

    - **Acceptance Criteria:** Test coverage of all critical components using the Jest/React Testing Library

  

    - **Assignee:** Karina/Egor A

  

- **Integration of tests with API**

    - Tests to verify the correctness of working with the endpoints API

    - Mock data for isolating tests

    - Error handling testing

    - **Acceptance Criteria:** All API calls are covered by integration

    by tests

  

    - **Assignee:** Karina/Egor A

  

- **E2E tests of the main user journey**

    - Configure Cypress for E2E testing

    - Test: home page → team selection → getting a forecast

    - Test: navigation between pages

    - **Acceptance Criteria:** Basic user scenarios are covered by E2E tests

  

    - **Assignee:** Karina/Egor A

  

- **Setting up test coverage**

    - Configure the generation of test coverage reports

    - Integration with CI pipeline

    - **Acceptance Criteria:** Coverage reports are generated automatically, the goal is 60%+

  

    - **Assignee:** Karina/Egor A

  
  

### Backend

  

#### API Testing \& Data Integrity

  

- **Unit tests for models**

    - Tests for the Team model

    - Tests for the Match model

    - Tests for the Tournament model

    - **Acceptance Criteria:** All models are covered by unit tests, including validation rules

  

    - **Assignee:** Arina

  

- **Integration tests for the API**

    - Tests for all GET endpoints

    - Tests for POST endpoints with validation

    - Testing with a real test database

    - **Acceptance Criteria:** All endpoints APIs work correctly with different data scenarios

  

    - **Assignee:** Arina

  

- **Middleware and utils tests**

    - Test coverage of auxiliary functions

    - Custom middleware testing

    - **Acceptance Criteria:** Auxiliary functions are covered by tests with edge cases

  

    - **Assignee:** Arina

  
  

### ML

  

#### Model Validation \& Testing

  

- **ML Model Validation**

    - Implementation of cross-validation to improve the reliability of the model

    - Create a confusion matrix for performance analysis

    - Add precision/recall/F1 metrics

    - **Acceptance Criteria:** The model is validated with detailed performance metrics

    - **Assignee:** Artem

  

- **Tests for ML endpoints**

    - Unit tests for prediction endpoint

    - Tests for model loading and initialization

    - Error handling testing for incorrect data

    - **Acceptance Criteria:** ML API endpoints work stably and handle errors

    - **Assignee:** Artem

  

- **Validation of input data**

    - Checking the correctness of the data before submitting it to the model

    - Processing of missing values

    - Validation of team IDs and tournament data

    - **Acceptance Criteria:** Robust input validation prevents model failures

    - **Assignee:** Artem

  
  

### CI/CD \& Deployment

  

#### Automation \& Infrastructure

  

- **GitHub Actions CI Pipeline**

    - Set up automatic push/PR tests

    - Configuration for frontend and backend tests

    - Setup test database for CI

    - **Acceptance Criteria:** All tests run automatically and block merge in case of errors

    - **Assignee:** Egor S

  

- **Setting up the Staging Environment**

    - Deploying the application on Heroku staging

    - Configuration of environment variables

    - Setup production-like database

    - **Acceptance Criteria:** The working application is available at a public URL

    - **Assignee:** Arina


- **Environment Variables Management**

    - Configure environment variables for staging/production

    - Secure storage of API keys and secrets

    - **Acceptance Criteria:** Confidential data is protected and properly configured

    - **Assignee:** Arina

  

- **Continuous Deployment (Bonus)**

    - Automatic deployment when merging to main

    - Setup staging → production pipeline

    - **Acceptance Criteria:** CD pipeline will automatically deposit upon successful merge

     - **Assignee:** Artem

  

## Acceptance criteria for sprint:
  
- **Test Coverage**

- **CI Pipeline:** Automatic tests are performed on every PR

- **Staging Environment:** a working application is available at a public URL

- **Documentation:** updated documentation on testing and deployment