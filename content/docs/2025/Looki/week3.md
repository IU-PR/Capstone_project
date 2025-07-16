# Week #3 Report

## Implemented MVP Features

### User Authentication (Login & Registration)
- Implemented **user registration** and **login** functionality using FastAPI with JWT-based authentication.
- Secured endpoints to ensure only authenticated users can access protected features like body prediction or profile editing.

### ML-Based Body Parameter Extraction
- Integrated a pipeline that allows users to upload a **single full-body photo**.
- From the photo, we extract two key measurements (shoulder width and hip width) using **MediaPipe Pose Estimation**.
- These values are passed into a custom **Random Forest regression model** to predict over 20+ detailed body measurements.
- The output is then used by a **Random Forest classifier** to predict the appropriate **clothing size (XS–XXXL)** based on body shape.

### Manual Editing of Measurements
- Users can manually **edit their predicted body measurements** if needed.
- Manual changes are persisted to the database and override model predictions where applicable.
- This ensures user control and correction in cases where the ML model might be less accurate due to poor input quality.

### Structured Database Design
- Designed and implemented a relational database schema using SQLAlchemy ORM.
- Core entities include `User`, `UserBodyProfile`, and related preference and measurement models.

### Cross-Platform Frontend (Flutter)
- Developed a **cross-platform mobile frontend** using **Flutter**, targeting both Android and iOS devices.
- Implemented:
  - **Registration and login screens** with input validation and secure JWT handling.
  - A **photo upload screen** to trigger ML-based prediction.
  - A **measurement display page** showing predicted sizes and measurements.
  - An **editing interface** allowing users to adjust their body parameters manually.
- Integrated REST API calls with the FastAPI backend.

## Demonstration of the Working MVP

### Screenshots / Video / Demo Links

- [Attachments](https://drive.google.com/drive/folders/1Ta4rJgo148GvsicmUfRG0Y2ZUgLi1L1K?usp=sharing)

---

## ML

### Link to Training Code

- **Body Predictor**: [`ml/src/core/body_modeling/body_predictor.py`](https://github.com/IU-Capstone-Project-2025/Looki/blob/main/ml/src/core/body_modeling/body_predictor.py)  
- **Size Recommender**: [`ml/src/core/body_modeling/size_recommender.py`](https://github.com/IU-Capstone-Project-2025/Looki/blob/main/ml/src/core/body_modeling/size_recommender.py)  
- **Pose Estimator**: [`ml/src/core/image_processing/pose_estimator.py`](https://github.com/IU-Capstone-Project-2025/Looki/blob/main/ml/src/core/image_processing/pose_estimator.py)  

---

### Overview of ML Models

#### Pose-Based Measurement Extraction (`PoseEstimator`)

- Uses **MediaPipe Pose** to detect key body landmarks from a user-provided photo.
- Extracts only two features:
  - **bia_di** – biacromial (shoulder) breadth
  - **bit_di** – bitrochanteric (hip) breadth
- Relies on user-provided real height to calculate scale (centimeters per pixel).

---

#### Body Parameter Prediction (`BodyPredictor`)

- **Model**: Multiple RandomForestRegressor models trained per target body measurement (e.g., chest girth, waist girth, elbow diameter, etc.).
- **Input Features**:
  - `bia_di`, `bit_di` (from pose estimator)
  - User metadata: weight (`wgt`), height (`hgt`), age, and gender (`sex`)
- **Output**:
  - 20+ predicted anthropometric measurements (e.g., `che_gi`, `wai_gi`, `hip_gi`, etc.)
- **Training**:
  - We used the publicly available body measurements dataset from Kaggle: [Body Measurements Dataset](https://www.kaggle.com/datasets/mexwell/body-measurements).
  - Preprocessing: `StandardScaler` for input features
  - Each model trained independently and saved to a single `.joblib` file.
- **Storage**:
  - Saved model path: `ml/src/data/models/body_predictor.joblib`

---

#### Clothing Size Prediction (`SizeRecommender`)
- Predicts clothing size (e.g., S, M, L, XL) based on predicted body girths:
  - Chest (`che_gi`), Waist (`wai_gi`), Hips (`hip_gi`)
- Uses a size chart CSV as input (`size_chart.csv`) which contain data about size from internet with columns (size, chest_min, chest_max, waist_min, waist_max, hip_min, hip_max)
- **Model**:
  - `RandomForestClassifier` trained on synthetic data generated from the size chart using normal distributions
  - Each size (XS to XXXL) is simulated with 1,000 samples
- **Preprocessing**: Uses `StandardScaler` for feature scaling
- **Storage**:
  - Saved model path: `ml/src/data/models/size_recommender.joblib`


---

## Internal demo

- Demonstrated the full flow:
  - User registration and login.
  - Uploading a photo and receiving predicted body measurements and recommended clothing size.
  - Manual editing of predicted body parameters.
- Key features presented:
  - Pose-based extraction of shoulder and hip width from photo.
  - Full-body measurement prediction using a trained ML model.
  - Size recommendation based on chest, waist, and hip measurements.
- Showcased API functionality through Swagger UI.
- Discussion points:
  - Improve design of the application
  - Add stricter validation on input data.
  - Improve API error responses and feedback handling.


---

## Weekly Commitments

### Individual Contributions

- **Nikita Shiyanov** — Updated database schema with new fields for user body profile measurements, size recommendations, and user attributes, refactored async database connection and session management using SQLAlchemy and asyncpg, updated SQLAlchemy models accordingly, worked with the MakeHuman API and successfully established a stable connection between the Python backend and the frontend.

- **Aleksandr Gavkovski** — Configured docker for flutter, set up a repository and set up CI/CD, wrote unit tests.

- **Ilya Maksimov** — Added uploading of a photo of oneself by the user when registering an account, added a page with the user's body parameters that the model determines from the photo uploaded by the user, and also added the ability for the user to change these parameters.

---

## Plan for Next Week

- Redesign the user interface for better usability and aesthetics
- Implement 3D human model visualization on the frontend
- Work on generating 3D body models from predicted measurements
- Start adding automated tests to cover key API endpoints
- Enhance robustness by improving error handling and edge case management


---

## Confirmation of the Code’s Operability

We confirm that the code in the main branch is:

- In working condition  
- Fully runnable via docker-compose as described in README.md