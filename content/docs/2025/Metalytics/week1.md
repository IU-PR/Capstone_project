---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *Metalytics*

**Code repository**: [https://github.com/IU-Capstone-Project-2025/Metalytics](https://github.com/IU-Capstone-Project-2025/Metalytics)

#### Description
The goal of this project is to develop an analytical system for forecasting the prices of specific metals traded on the Russian financial market.
The system aims to explore and implement modern approaches to metal price prediction, analyzing historical price patterns, market volume data, and seasonal trends. Based on this research, the project will propose a set of analytical tools tailored for monitoring and forecasting the behavior of selected metal types — such as gold, nickel, or aluminum.
In addition to raw forecasting, the system will also generate explainability reports to help interpret observed and predicted price movements. These reports will incorporate contextual factors such as macroeconomic indicators, sanctions, major news events, and global market volatility, providing insights that may influence investor decision-making.

#### Problem Statement
One of the major flaws is that private investors and analysis lack access to precious metals with tools involving predictive modeling and explainability based on some external circumstances. This project attempts to fill the gap through a focused system with the ability to forecast metal prices as well as giving the reasons for such forecasts in an interpretable, automated manner.

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | Responsibilities   |
|-----------------------------------------|------------------|-----------------|---------------------------------------------|--------------------|
| Vladimir Toporkov (Lead)     | @Spectre113 | v.toporkov@innopolis.university | Frontend | Frontend development, team coordination |
| Ilya Grigorev           | @DavidVista | il.grigorev@innopolis.university | ML | R&D, Filtration design, Model Selection, and ML team coordination |
| Farit Sharafutdinov            | @Ivenho123 | f.sharafutdinov@innopolis.university | ML | Data collection, preprocessing, and delivery |
| Rail Sharipov            | @ZilaBu | ra.sharipov@innopolis.university | ML | R&D, Exploratory data analysis, and feature engineering |
| Askar Kadyrgulov            | @gaha1ad | a.kadyrgulov@innopolis.university | Backend | Development and Operations for backend and ML, scraping functionality |
| Nikita Solomennikov | @Hikisol | n.solomennikov@innopolis.university | Design | Creating design for frontend |


## Brainstorming

### Ideas during brainstorming

1. **Metalytics** - analytical system for forecasting metal prices, Focus on 2–3 metals traded on the Russian financial market. Will include explainability reports.
2. **Idea 2** - forecasting system for company shares. Similar to Metalytics, but applied to public companies listed on the Moscow Exchange.
3. **Idea 3** - Asset allocation recommendation system. Helps users decide how to distribute their finances across stocks, bonds or metals.

### Brief market research / problem validation

#### Metalytics
- Metal price forecasting is a key task in trading and industrial planning.
- Many private investors lack access to expert analytics tools.
- Market volatility makes manual analysis difficult.

**Conclusion**: the idea is timely, realistic, and fills a clear niche.

#### Idea 2
- Requires analysis of company financials or reports.
- Much higher volatility due to internal company events (e.g., earnings, scandals).
- Risk of low-quality predictions due to insufficient public data or noisy trends.

**Conclusion**: Better to gain experience in metal price analysis with simpler time series first.


#### Idea 3
- Technically challenging: requires accurate predictions across multiple markets.
- Relies heavily on external financial APIs and historical datasets.
- Scope too large for MVP and difficult to evaluate success metrics.

**Conclusion**: The idea is ambitious but out of scope for initial project phase.


## Basic requirements

### Target users and their primary needs

Our target users include:

- Retail investors — interested in understanding price trends to make better investment decisions in metals.
- Financial analysts — who need support tools for price forecasting, especially with explainability behind trends.
- Students  — exploring real-world time series prediction with ML tools.

Their primary needs are:
- Simple, accessible interface for checking metal forecasts.
- Trustworthy predictions based on market and external data.


### User stories

- As an investor, I want to see price forecasts for specific metals so that I can make better trading decisions.
- As a financial analyst, I want to understand why a model made a prediction so that I can assess its reliability.
- As a student interested in ML, I want to explore how external events influence time-series models so that I can learn practical ML skills.


### Initial scope

MVP includes:
- Price prediction for simple and stable metal (*gold*) to start with
- Static frontend with data visualization.
- Backend with baseline ML models

MVP will not include:
- Advanced deep learning models.
- Report generation
- Volatile metals price prediction


## Tech-stack

| Category       | Tools / Libraries                              | Why we chose them                             |
|----------------|------------------------------------------------|-----------------------------------------------|
| ML / Baseline  | scikit-learn                                 | Lightweight, well-documented, great for fast prototyping |
| Deep Learning  | Keras, TensorFlow, PyTorch, Theano     | For advanced modeling |
| Metaheuristics | DEAP, scikit-opt, pyswarmpackage         | For experimenting with alternative optimizers |
| Backend        | FastAPI                                      | Fast, modern, built-in OpenAPI docs           |
| Frontend       | HTML, CSS, JavaScript                    | Simple static frontend |
| Data Processing| pandas, NumPy                              | Standard tools for loading and transforming data |
| Infrastructure | Docker, docker-compose                     | Reproducibility, unified local setup          |

## Project structure

```
Metalytics/
├── frontend/           # Client-side application with figma design
├── backend/            # Server-side logic and API handling
├── ml/                 # Machine learning models, training, and inference scripts
├── docker-compose.yml  # Orchestration file for running all services together
├── .gitignore          # Git exclusion rules
└── README.md           # Project overview and instructions
```

## 

# Weekly commitments

## Individual contribution of each participant
- **Vladimir Toporkov** - created GitHub repository, prepared initial structure, wrote [readme](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/main/README.md) in project repository, wrote full week1 report. Most commits.
- **Farit Sharafutdinov** -  explored available datasets relevant for the task and developed script for automatic extraction and augmentation of dataset. `calculate_indicators.py and fetch_gold_ohlcv.py` [in Metalytics repository](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/main/ml) the work result. [Commit link](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/2ab6f5319de1aeaab0bc6558f1f72cbade6c145b/ml).
- **Ilya Grigorev** - performed preliminary market behavior analysis of gold prices, investigated filter design principles, and [prepared](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/main/ml/notebooks) an in-depth exploratory notebook focused on volatility and preprocessing. [Commit link](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/319a19b354acad96a178c08c0f52019e995a5d17/ml/notebooks).
- **Rail Sharipov** - Explored Kaggle and began reviewing external data sources. Wrote down gold exploration [details here](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/545460d500f4401ba34a318829c8fa5f8c691bdc/ml/overall_gold_exploration)
- **Askar Kadyrgulov** - started studying FastAPI and backend architecture principles. Wrote down [API endpoints](https://github.com/IU-Capstone-Project-2025/Metalytics?tab=readme-ov-file#-waypoints) in readme section and created basic [template in backend](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/main/backend/main.py). [Commit of creation endpoints](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/2bef05d4ca1803dd38aa474c619e15e6ffc20a2a) and [backend creation](https://github.com/IU-Capstone-Project-2025/Metalytics/blob/fd3f77e4838d968091dfd3d811a00c4789992b14/backend/main.py).
-  **Nikita Solomennikov** - Created a [logo.png](https://raw.githubusercontent.com/IU-Capstone-Project-2025/Metalytics/main/frontend/img/logo.png
) for the site and adapted it to [vector form](https://raw.githubusercontent.com/IU-Capstone-Project-2025/Metalytics/5fdc249a0b8b69aab1e35e83e8c0186c44d86aaf/frontend/img/logo.svg), began learning Figma and UI/UX fundamentals to design user-facing components. [Commit of adding logo](https://github.com/IU-Capstone-Project-2025/Metalytics/tree/5fdc249a0b8b69aab1e35e83e8c0186c44d86aaf/frontend/img).

 ### Plans for the next week:
- Create the first version of the UI prototype in Figma.
- Continue collecting and cleaning relevant datasets;
- Explore and evaluate potential data sources;
- Start working on the first baseline model for price trend analysis.
-  Define the backend architecture and project structure;
- Start implementation of basic API endpoints;


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✓] In working condition.
- [✓] Run via docker-compose (or another alternative described in the `README.md`).
