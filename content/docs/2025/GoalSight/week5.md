# Week #5

### Summary of feedback collection methods and key findings.

Sessions #
Conduct at least three sessions with potential users, describe detailed user reviews here (potential users should NOT be your team members).

Analyze #
Describe the important points that you received from the user feedback, what issues and with which priority you created.

### Link to updated backlog reflecting feedback.


### Description and demonstration (screenshots/GIFs, links to PRs) of implemented improvements and bug fixes.


### Updated link to the deployed application.

### Frontend Part 
 
#### Overview 
 
This section describes the key improvements made to the frontend interface, focusing on mobile adaptation, user experience enhancements, and API integration optimizations. Major changes include complete mobile responsiveness, redesigned navigation, and improved data loading patterns. 
 
#### 1. Mobile Adaptation Improvements 
 
##### Header Navigation Redesign 
 
Implementation: 
- Restructured header navigation for narrow mobile screens 
- Implemented responsive breakpoints for different device sizes 
- Optimized touch targets for mobile usability 
 
Technical Details: 
- Used CSS media queries for viewport-specific styling 
- Implemented hamburger menu pattern for mobile 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/17fd5e70ee9b4b273446b20fa830ec1098a6910b) 
 
##### Full Mobile Adaptation 
 
Implementation: 
- Comprehensive responsive design implementation across all components 
- Viewport-optimized layouts for all mobile size 
- Mobile-first approach for critical user flows 
 
Technical Details: 
- Used CSS media queries for viewport-specific styling 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/6d05c914ea38db8d3b830bf91ef93f476a600caf) 
 
#### 2. Prediction Interface Enhancements 
 
##### Instruction Panel System 
 
Implementation: 
- Added interactive tutorial for prediction workflow 
- Implemented panel transition between instructions and prediction view 
- Fixed positioning for persistent visibility during scrolling 
 
Technical Details: 
- React state management for panel visibility 
- CSS position: sticky for persistent display 
- Smooth animations for panel transitions 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/b5f7ac35b82e0be008b9a9a3fa50b75de0251560) 
 
##### Forecast Description Window 
 
Implementation: 
- Interactive popup explaining prediction methodology 
- Context-sensitive positioning relative to forecast elements 
- Accessible design with keyboard navigation support 
 
Technical Details: 
- Portal-based implementation for proper z-index management 
- Dynamic positioning calculations 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/d19f37594ece5417860c1020c657c07d67df752f) 
 
#### 3. Data Presentation Improvements 
 
##### Statistics Panel Enhancements 
 
Implementation: 
- Multiple simultaneous stat panel support for comparison 
- Revised opening/closing logic with improved state management 
- Conditional rendering optimizations 
 
Technical Details: 
- Array-based state management for multiple panels 
- Memoized component rendering 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/e19c71ab40c2b9a7be0c87e27fb4c873f41d8f9a) 
 
##### Team Logos Integration 
 
Implementation: 
- Added visual team identifiers across all interfaces 
- Responsive logo sizing system 
- Fallback handling for missing assets 
 
Technical Details: 
- Asset pipeline integration 
- CDN-based image delivery 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/pull/49) 
 
#### 4. API Integration & Data Flow 
 
##### Prediction API Optimization 
 
Implementation: 
- Restructured response handling for better performance 
- Percentage calculation fixes 
- Error state management 
 
Technical Details: 
- Response normalization layer 
- Client-side calculation validation 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/a1521b2a19f103573fb982e4bf1d8af3348c191e) 
 
##### Team Statistics API Separation 
 
Implementation: 
- Decoupled team metadata from statistical data 
- Parallel loading for improved performance 
- Independent error handling 
 
Technical Details: 
- Separate Redux actions/reducers 
- React Query implementation 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f042e4a08b4c2d4613e073a9f060dd900c69142f) 
 
#### 5. Testing & Deployment

##### E2E Testing Pipeline Fixes 
 
Implementation: 
- Docker container integration for testing 
- Environment configuration management 
- Pipeline reliability improvements 
 
Technical Details: 
- Docker Compose test configuration 
- CI/CD workflow adjustments 
- [Main Commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/3b9fad6d400f0cb11a6c7e33b6587e6929d9043a) | [Final Commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/aadb9e4f8481da42c2880d42e43a85f5cb9ca9aa) 
 
##### Browser Tab Metadata 
 
Implementation: 
- Favicon integration 
- Title tag standardization 
- PWA compatibility 
 
Technical Details: 
- Webpack asset processing 
- HTML meta tag configuration 
- [Commit Reference](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/497f49f1583e3e902db2d355f67917fff0259d9d)

### Backend & Data Updates

#### Key Improvements

#### 1. Automated Daily DB Updates
- Implemented cron jobs for scheduled database refreshes
- Ensures predictions always use fresh data

#### 2. Enhanced Tournament & Match Data
- Added:
  - Country information to tournaments
  - Club logos for better visualization
  - Precise match timing data
- Fixed Predictions API accuracy issues

#### 3. Feature Research for ML Model
- Identified key performance factors for teams
- Evaluating data collection methods:
  - API integrations
  - Web parsing solutions
  - Manual data curation

### ML part

#### Overview

This part describes considerations for further ML improvements, as well as a description of the implemented parts. Also this week, the 3rd class classifier was replaced with a 2nd class classifier, which allowed us to increase the prediction accuracy from 0.48 to 0.69. This was done based on the considerations that the 2nd class brothel is more in line with the requirements of the product, and it will also increase the accuracy of the prediction right now.

#### 1. API-Compatible Feature Selection

##### Objective

Filter training features to only include those accessible through external APIs to ensure real-world applicability.

##### Implementation

- **Data Audit**: Review current feature set and match with API availability
- **Feature Mapping**: Create mapping between internal features and API endpoints
- **Validation Pipeline**: Implement checks to ensure feature consistency between training and prediction

##### Expected Outcome

Reduced feature set but improved model reliability in production environment.

#### 2. Feature Categorization

##### General Football Features

- Team statistics (goals scored/conceded, possession, shots)
- Historical match results
- League standings and form
- Weather conditions and venue factors

##### Player-Specific Features

- Individual player statistics (goals, assists, minutes played)
- Player ratings and performance metrics
- Injury status and availability
- Transfer market values

##### Rationale

Separating features allows for specialized processing and better model interpretability.

#### 3. Player Embedding Layers (done)

##### Implementation

###### Overview:

Implemented player embeddings using the European Soccer Database with 11,060 unique players and 35 numerical attributes per player.

###### Core Implementation Steps

**Data Processing Pipeline**:

  - **Source**: European Soccer Database (183,978 player records)
  - **Players**: 11,060 unique players with attribute data 
  - **Features**: 35 numerical attributes including overall_rating, potential, crossing, finishing, dribbling, etc. 
  - **Missing Values**: Handled via mean imputation (< 1.5% missing for most attributes)

**Temporal Weighting System**:
```python
# Exponential decay implementation
weights = np.array([0.95 ** (n_records - i - 1) for i in range(n_records)])
```
  - **Decay Factor**: α = 0.95 (configurable)
  - **Logic**: Recent player performance weighted higher than historical data 
  - **Application**: Applied to all 35 numerical attributes per player 

###### Player Profile Creation
  - Aggregation: Weighted averages calculated for each attribute per player 
  - Categorical Data: Latest record used for preferred_foot, work_rates 
  - Profile Structure: Each player represented by 35-dimensional feature vector

##### Embedding Preparation
  - **Normalization**: StandardScaler applied to all numerical features 
  - **Player Mapping**:
    - player_id_to_idx: Maps API IDs to sequential indices 
    - idx_to_player_id: Reverse mapping for inference 
  - **Serialization**: Complete embedding data saved as embeddings_data.pkl

###### Technical Specifications
  - **Embedding Dimension**: 35 features
  - **Data Structure**: Normalized profiles ready for embedding layer input
  - **Scalability**: Mapping system supports easy addition of new players

**Integration is Ready to Integration.**

#### 4. Temporal Weight Implementation

##### Exponential Decay Formula

```python
weight(t) = exp(-α * (current_time - match_time))
```

Where α is the decay parameter.

##### Implementation Strategy

- **Decay Parameter**: Start with α = 0.1 and tune based on validation performance
- **Time Windows**: Apply stronger weights to matches within last 6 months
- **Seasonal Adjustments**: Account for transfer windows and season breaks

##### Benefits

- Recent matches have higher influence on predictions
- Adapts to team form and tactical changes
- Reduces impact of outdated information


#### 5. Ensemble Architecture

  **Proposed Models**:
  - XGBoost Component
  - LSTM Component 
  - Ensemble Combination

  - **Method**: Weighted averaging or stacking
  - **Weights**: Determine through cross-validation
  - **Meta-learner**: Consider logistic regression for final predictions

##### References

- Razali et al. (2024) showed XGBoost effectiveness for football prediction
- Zhang et al. (2022) demonstrated LSTM success in sports forecasting

#### 6. Evaluation Metrics

##### Primary Metrics

- **Accuracy**: Overall prediction correctness
- **F1-Score**: Balanced precision and recall, especially important for draw predictions
- **Log-Loss**: Measures probability calibration quality
- **Brier Score**: Evaluates probabilistic prediction accuracy

#### 7. Regularization Strategy

- L1 Regularization (Lasso)
- L2 Regularization (Ridge)

##### Monitoring

- **Validation Loss**: Track to detect overfitting
- **Learning Curves**: Monitor training vs validation performance
- **Early Stopping**: Implement based on validation metrics


## Individual Contribution of Each Participant

- **Arina Zimina**:  
  - Provide daily database updates | Add cron scheduling | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/d3d2aaf5267f5f428885005cb74e42fe9f4e9181) 
  - Backend improvements | Fix predictions API, add country to Tournament API, add clubs' logos, add time of matches | [Add logos](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/7845d169ac6a1e9fd2c3afad3244f8531f329dd8), [Add time](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/3081f28f757462dc18cfeb697cc44d8bf2287261), [Fix API](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/40033bce6c5349dfa5870b36ab0b242690f159ce) 
  - Search data for dataset  
  - Search for features to improve the ML model | Help with finding relevant features for our teams participating in the tournament to determine predictions (parsing/api/manual copying) | [Link to doc](https://docs.google.com/document/d/1S2x5Z-1dhCz3l11dlGOEv48BbouwoaJoBkI0bOby6Lk/edit?usp=sharing)

- **Artem Panov**:
  - PM:
    - Template for individual contribution of each participant part in report.
    - Meeting organization and Task distribution | [Link to Kanban board in Weeek](https://app.weeek.net/ws/809762/shared/board/3Xt4iII1JUgOmusxANh9WPCW1SN0A6UZ)

  - ML:
    - Exploring approaches and ideas to improve the ML part | part of report
    - Player Embedding Layers implementation | [Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/67f73bedfb514ebc80bc0079b61b1fa1f200fc9c)
    - Replacing a 3-class classifier with a binary classifier |[Link to commit in GitHub repository](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/64f2d01cee71b65f1c301db7d13f7081f239a862)


- **Karina Siniatullina**: 
  - Adapted the navigation in the header for the mobile version. | Adapted the navigation in the header for the mobile version so that it narrows down to a narrower version. | [Link to commit]([https://github.com/IU-Capstone-Project-2025/GoalSight/commit/1b899e86b7a56b3584bb7d6d1d0aa81c7a6abd8c](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/17fd5e70ee9b4b273446b20fa830ec1098a6910b)) 
  - Added instruction panel for forecast. | Added instructions for predicting the match, which are initially on the page, and then go to the prediction panel and back. | [Link to commit]([https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c0a034b6be627ae4c117ea19f92ba09e37742145](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/17fd5e70ee9b4b273446b20fa830ec1098a6910b)) 
  - Fixed instruction panel. | This panel is fixed on top of the screen. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/b5f7ac35b82e0be008b9a9a3fa50b75de0251560) 
  - Prediction panel output. | Changed the order of prediction output. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/b5f7ac35b82e0be008b9a9a3fa50b75de0251560) 
  - Statistic panel clickability. | Fixed the condition for the statistics panel to appear. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/b5f7ac35b82e0be008b9a9a3fa50b75de0251560) 
  - Prediction api. | Changed api responses and fixed percents. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/a1521b2a19f103573fb982e4bf1d8af3348c191e) 
  - Teams’ statistics api. | Separated api responses for team and its statistics. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/f042e4a08b4c2d4613e073a9f060dd900c69142f) 
  - Opening statistics. | Now user can open more than one stats panel and compare them. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/e19c71ab40c2b9a7be0c87e27fb4c873f41d8f9a) 
  - Window for forecast description. | There is a pop-up window near the forecast that describes how the forecast is calculated. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/d19f37594ece5417860c1020c657c07d67df752f) 
  - Logos for teams. | Added logos for all teams. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/pull/49) 
  - Adaptation. | Added adaptation of the entire design for the mobile version of the site. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/6d05c914ea38db8d3b830bf91ef93f476a600caf)


- **Egor Sergeev**:
  - Created a list of different questions for a survey to find improvements
  - Conduct surveys | [Link to google disk](https://docs.google.com/forms/d/1gDofDPW1Q5GyEf0EOadSr5eBuavBRZW_Hd9BwQ_vNTE/previewResponse)
  - Send to different groups in telegram to collect feedback
  - Aggregate survey results and create a list of improvements for the project based on this | [Link to google doc](https://docs.google.com/document/d/1HPyVWUsEUGXHCCLz_TdWyGqo9ErNNSwOG74pWQkfQK0/edit?usp=sharing)
  - Create a document of overall feedback from survey | [Link to google doc] (https://docs.google.com/document/d/1gPtPhgrDNgGuZ1pvSb2B4HGsGZYB8Rv5YHTEdbQJRe0/edit?usp=sharing)
  - Write a weekly report.

- **Egor Agapov**: 
  - Search for features to improve the ML model | Help with finding relevant features for our teams participating in the tournament to determine predictions (parsing/api/manual copying) | [Link to google doc](https://docs.google.com/document/d/1S2x5Z-1dhCz3l11dlGOEv48BbouwoaJoBkI0bOby6Lk/edit?usp=sharing) 
  - Website improvement based on feedback requests | Below I described in detail exactly what I did 
  - Fix the tab in the browser | Changed the tab's logo instead of the base one and changed the name of the tab itself | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/497f49f1583e3e902db2d355f67917fff0259d9d) 
  - Fix the data loading process on both pages | I made sure that the entire skeleton of the page was loaded immediately and the data was dynamically loaded later | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/31b50f853ece9d45c997bfe3473818db41837d18) 
  - Fix the e2e test in the pipeline | To Complete the test, it was necessary to run the docker containers of the entire project in the pipeline. | [Link to main commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/3b9fad6d400f0cb11a6c7e33b6587e6929d9043a) | [Link to final commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/aadb9e4f8481da42c2880d42e43a85f5cb9ca9aa) 
  - Fixing the navigation menu on the website | Fixed hovering the cursor over a page where the user is already on, so that hovering does not merge with the background. | [Link to commit](https://github.com/IU-Capstone-Project-2025/GoalSight/commit/c42cf4dbd80aced50e5edc2805827525713c7242)

## Weekly Commitments

### Plan for Next Week

#### Sprint Goal

Finalize the project, prepare all deliverables, and craft a compelling presentation.

#### Frontend

- Ensure design documents (Figma) are up to date and reflect the final product - Karina, Egor A
- Add a disclaimer stating that the model may be wrong and the accuracy of the model is 0.69 - Karina, Egor A
- Add a representation of list with features of model - Karin, Egor A
- Cleaning the code (removing unused parts) - Karina, Egor A
- Comments on the code - Karina, Egor A

#### Backend

- Cleaning the code (removing unused parts) - Arina
- Comments on the code - Arina
- Filling the DB with new data - Arina
- API docs - Arina

#### ML

- Creating new, more relevant data from the dataset API for training - Arina
- Cleaning the code (removing unused parts) - Artem
- Comments on the code - Artem
- Description of further improvements - Artem
- Training a model on new data - Artem
- Adding time scales for all model features - Artem

#### Presentation

- Create a draft presentation - Egor S

#### Sprint acceptance criteria

- A fully completed project
- Comprehensive final documentation (README, API docs, Figma)
- Draft of presentation slides
- Plan for the live demo