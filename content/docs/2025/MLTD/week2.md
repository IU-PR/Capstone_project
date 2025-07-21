# Week 2

## Detailed Requirements Elaboration

For this week, we are focusing on preparing the backend API for the web interface and upcoming features (see plans for next week) as well as planning which machine learning models to use for the project (see progress for ML). As the frontend depends on the API to be able to interact with its features. While both the frontend and API depend on machine learning since it is one of the main core functions.

### API Interaction:
The API should be able to recieve files from users through a web interface or a command line interface and allow only non-empty txt, log, and csv files to the API. Which would allow users to create scripts to automate threat detection on a timely basis.

### Machine learning models and Data pre-processing
See ML in project progress for the requirements of data-preprocessing and models.

### Prioritized backlog
[Kanban board](https://tree.taiga.io/project/bulatfakhrutdinov-mltd/kanban)

## Project progress

### Frontend
Currently we do not have a frontend, but have plans to make one next week with Nextjs.

### Backend
The backend API can now recieve log files (csv, log, txt) from users by sending a POST request with a file to "http://localhost:8000/upload". And the API has been prepared for upcoming features such as threat detection, batch processing, and result retrival. As well as the frontend, as parts of the backend API are important for building the web interface.

### ML
For ML we've pre-selected Decision Trees (DT), Random Forests (RF), SVM, and pre-trained models as the core ML approaches for threat detection in log files. There are some benefits of using these models:
1) Handling Categorical Features
Log data often contains categorical values.
DT/RF natively support categorical data (via one-hot encoding or label encoding) without requiring extensive feature engineering.

2) Interpretability
DT/RF provide clear decision paths, crucial for:
Debugging why a log entry was flagged as a threat.
SMV provides clear hyperplane and handles non-linear cases.

## Weekly commitments
Paramon:
- Added [API endpoint mappings](https://github.com/IU-Capstone-Project-2025/MLTD/commit/2ad380a773fa665ef44982e56b0b5819a057c05b) for uploading files.
- Implemented [File uploading](https://github.com/IU-Capstone-Project-2025/MLTD/commit/09581e73560c14e63144d4bb92dce79baf9de31e) to allow files to be uploaded through an interface. 

Bulat:
- Created [backlog](https://tree.taiga.io/project/bulatfakhrutdinov-mltd/kanban).
- Defined set of ML features for MLTD.

## Plans for next week
* [Preprocess log data: cleaning, feature extraction](https://tree.taiga.io/project/bulatfakhrutdinov-mltd/us/2?kanban-status=10310817)
* [Research and select ML model: supervised vs. unsupervised](https://tree.taiga.io/project/bulatfakhrutdinov-mltd/us/1?kanban-status=10310817)
* [Train initial model on sample threat datasets](https://tree.taiga.io/project/bulatfakhrutdinov-mltd/us/3?kanban-status=10310817)
* [Set up Next.js project with basic UI](https://tree.taiga.io/project/bulatfakhrutdinov-mltd/us/8?kanban-status=10310817)
