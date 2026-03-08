# Practicum Project Summer 2025 Report 6
**Team mealix**  

---

## 1. Links 

### Specify here all the necessary links to your website, application installer, final demo, etc.  
- **Deployment:** https://mealix.vercel.app
- **Not final demo:** [link](https://drive.google.com/drive/folders/1bLe45qyquxreOjGaAtORP1FpTKihp6HY?usp=sharing)

## 2. Final deliverables
Project overview 
- Mealix is a web and Telegram-based service for personalized meal planning.

Features 

- Lets users generate daily meal plans tailored to their preferences, allergies, budget, and nutrition goals (calories, proteins, fats, carbs).
- Users register and log in via Telegram bot (no separate signup needed).
- Users can save their food profile (allergies, restrictions, favorite cuisines).
- The frontend provides a form to generate a meal plan for one day, with fields for preferences, budget, and nutrition goals.
- The backend stores user profiles, checks registration, and generates meal plans by integrating with an ML service.
- All components (frontend, backend, ML, bot, database) are containerized and run together via Docker Compose.

Tech stack 

**Frontend:**
- React
- TypeScript
- Vite
- React Router

**Backend:**
- Java 21
- Spring Boot
- Spring Web, Spring Validation, Spring Data JPA, Spring WebFlux
- PostgreSQL
- Liquibase (database migrations)
- Maven

**ML Service:**
- Pytorch
- FastAPI

**Telegram Bot:**
- python-telegram-bot (asyncio)
- httpx
- python-dotenv

## 3. Presentation draft
[Link for presentation draft](https://cloud.mail.ru/public/mKtW/EgR58uetx) 

---

## 4. Weekly commitments  

### Individual contributions  

**Alexander Kachmazov (ML):**  
- Implemented structured response generation based on a predefined JSON schema.
- Added retry logic for error handling to improve robustness.
- Retrained the RAG (Retrieval-Augmented Generation) model for improved performance and accuracy.
- [Link](https://github.com/IU-Capstone-Project-2025/mealix/commit/841a55f0df0b2db032e06fc1e86e5483815ed545)

**Samat Iakupov (Frontend):**  
- Adapted frontend with new backend contract.  
- [Link](https://github.com/IU-Capstone-Project-2025/mealix/commit/913db31c56342da2e2d8b4da45cc72897c6b3bdb)  

**Dmitrii Antipov (Backend):**  
- Adapted backend with new ML contract.  
- [Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/backend_contract_update)  

**Danil Eramasov (ML):**  
- Improved recepies deleting all trash from text. Read all recipes in 5 categories.
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/tree/Recipes_parser)  

**Albert Shammasov (Data Analyst):**  
- Improved recepies deleting all trash from text. Read all recipes in 5 categories.
- [Code link](https://github.com/IU-Capstone-Project-2025/mealix/tree/Recipes_parser)  


---

## 3. Confirmation of the code's operability  

We confirm that the code in the main branch:  
- Is in working condition  
- Can be run via docker-compose (or alternative method described in README.md)  