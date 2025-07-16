# Week #1 Report

## Project Description

**Project Name:** Looki  
**Code Repository:** [https://github.com/IU-Capstone-Project-2025/Looki](https://github.com/IU-Capstone-Project-2025/Looki)

**Idea:**  
Looki is a mobile app for virtual clothing fitting that uses advanced computer vision and 3D modeling technologies to revolutionize the online shopping experience.  
The app allows users to upload their photos, based on which the system analyzes individual body parameters, creates a personalized 3D model and offers accurate size recommendations for various clothing brands.

**Problem Statement:**  
Looki aims to solve a key problem of online shopping: high return rates due to size mismatches and the inability to assess how clothes will fit a particular figure.  
Traditional online retailers offer standardized sizing grids that often do not consider individual body features, resulting in increased returns and customer dissatisfaction.

---

## Team Members

| Name              | Telegram Alias     | Email Address                       | Track                            | Responsibilities                                                                 |
|-------------------|--------------------|-------------------------------------|-----------------------------------|----------------------------------------------------------------------------------|
| Nikita Shiyanov   | @Nikita_shiyanov   | n.shiyanov@innopolis.university     | ML/Backend developer, DevOps     | Computer vision, size recommendation, ML integration, Docker                     |
| Aleksandr Gavkovskii | @SachaYT        | a.gavkovskii@innopolis.university   | Frontend Flutter developer       | App design and theme, UI/UX, API integration                                    |
| Ilya Maksimov     | @ilyhamaks         | i.maksimov@innopolis.university     | Frontend/Backend developer       | API for app, UI/UX, backend                                                      |

---

## Brainstorming

### Problem Discussion

At the brainstorming session, we discussed various everyday challenges. One key problem was online clothing shopping.  
Clothes often do not match their stated sizes or look different in reality, leading to returns or dissatisfaction.  
This results in wasted time for the user and financial losses for sellers due to return logistics.

### Key Goals

- Create an app that reduces product returns and improves user satisfaction.
- Enable users to preview how clothes will look on their body.
- Ensure intuitive UI/UX to compete in a saturated market.

---

## Market Research / Problem Validation

**Current Market Players (Russia & Global):**

| Company         | Technology                           | Limitations                                     |
|----------------|--------------------------------------|-------------------------------------------------|
| Lamoda          | AI recommendations, “Find by Photo”  | No body measurements/virtual try-on             |
| Wildberries     | Image search, personalized suggestions | Focuses on search, not fitting simulation     |
| SberMegaMarket  | AI-driven product recommendations     | No AR/3D features                               |
| Yandex.Market   | Behavioral analytics, discounts       | Lacks sizing accuracy tools                     |
| Kleos AI        | Style-based recommendations           | No body scanning or virtual try-on              |
| AR Try-Ons      | Basic AR for glasses/makeup           | Limited to accessories                          |

**Gap Identified:**
- No Russian app combining **body measurement scanning** + **3D virtual try-on**.
- Existing 3D solutions do not support **personalized avatars**.

### Validated Problems:

- **High Return Rates**: Customers return items due to poor fit.
- **Inconsistent Sizing**: Varying size definitions across brands.
- **Environmental & Economic Losses**: Each return incurs logistical and packaging costs.

---

## Basic Requirements

### Target Users & Needs

- **Online Shoppers**: See how clothes fit on their own body, avoid returns, save time.
- **Fashion Retailers**: Reduce return rates, increase trust and sales.
- **E-Commerce Platforms**: Differentiate from competitors, lower fraud and complaints.

### User Stories

- _As a shopper_, I want to scan my body with my phone camera to get precise measurements.
- _As a user_, I want to see how clothes fit my unique body shape so I can buy with confidence.
- _As a retailer_, I want to upload my clothing catalog to the system so customers can try items.
- _As a plus-size customer_, I want to see realistic fitting on my body type so I feel represented.
- _As an admin_, I want to monitor size recommendation accuracy to improve the algorithm.

---

## Initial Scope

### MVP (In Scope)

- Flutter mobile camera measurement
- MakeHuman avatar generation
- Basic 3D try-on
- Size recommendation engine
- Dockerized deployment

### Post-MVP (Out of Scope)

- Real-time AR mirror mode
- Social sharing features
- Multi-brand size database
- Advanced fabric simulation

---

## Tech Stack

| Component        | Technology            | Justification                              |
|------------------|------------------------|---------------------------------------------|
| Frontend         | Flutter                | Cross-platform mobile development           |
| 3D Modeling      | MakeHuman + Blender    | Open-source parametric modeling             |
| Backend          | Python (FastAPI), TypeScript | ML integration & service logic         |
| Computer Vision  | OpenCV + MediaPipe     | Accurate body measurement                   |
| Deployment       | Docker                 | Containerization and reproducibility        |

---

## Weekly Commitments

- **Nikita Shiyanov**: Created size recommendation model, extracted parameters from photo using computer vision, developed API for model access, wrote this report.
- **Aleksandr Gavkovskii**: Developed Flutter app, configured architecture, added dependencies, set up themes, implemented registration/login/profile screens.
- **Ilya Maksimov**: Developed TypeScript backend for user authorization, product management, and user data. Created product storage screen and connected frontend to backend.

---

## Confirmation of Operability

- The code in the `main` branch is in working condition.
- The project runs using `docker-compose` (or an alternative described in `README.md`).

June 11, 2025
