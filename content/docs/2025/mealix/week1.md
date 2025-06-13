# Practicum Project Summer 2025 Report 1
## Week 1
## Team mealix

---

# 1. Project description

**Project name:** Mealix
**Code repository:** [https://github.com/IU-Capstone-Project-2025/mealix](https://github.com/IU-Capstone-Project-2025/mealix)

Our project is a **Telegram bot** with **AI** that collects information from the user about food preferences (allergies, dietary restrictions, favorite cuisines, cooking time) and, upon request, **generates a personal meal plan** for a given period (day, three days, week). The user receives a food ration for the specified period with detailed cooking instructions and a generated list of products from "Magnit" with actual prices and images.

**Team members:**

| Team Member        | Telegram Alias   | Email Address                | Track       | Responsibilities                      |
|--------------------|------------------|------------------------------|-------------|---------------------------------------|
| Samat Iakupov      | @samerspc        | sa.iakupov@ innopolis.university | Frontend    | Task distribution, Frontend development |
| Alexander Kachmazov | @vozamhcak       | a.kachmazov@ innopolis.university | ML          | Machine learning models development   |
| Dmitrii Antipov    | @stacss          | d.antipov@ innopolis.university | Backend     | Database and API development          |
| Danil Eramasov     | @Danil0Danil     | d.eramasov@ innopolis.university | ML          | Data preprocessing and analysis       |
| Albert Shammasov   | @myavg           | a.shammasov@ innopolis.university | Data Analyst | Data preparation and management       |

# 2. Brainstorming

**Ideas during brainstorming:**
**A telegram bot** with a personalized meal plan is the main idea: the bot collects data about user preferences and generates an individual diet with recipes and a shopping list.
**Integration with the store** (Magnit) – Parsing current prices and availability of goods to create an accurate shopping list.
**Filtering by product rating** is to consider only products with a high rating (>=4.5) in order to offer users the best options.

**Brief market research / problem validation:**
**The problem**: People spend a lot of time planning meals, especially considering diets, allergies, and budgets.
**Decision:** The bot automates the process by offering personalized plans and shopping lists.
**Analogues:** There are applications (for example, "EatThisMuch"), but they are not integrated with Russian stores and do not take into account local prices.

# 3. Basic requirements

**Target users and their primary needs:**
**Who:** People who monitor nutrition (healthy lifestyle, diets, allergies), busy professionals, students.
**Needs:** Saving time on meal planning, taking into account food restrictions, affordable and convenient shopping lists.

**User stories:**
1. "As a user with a nut allergy, I want to receive recipes without nuts so as not to waste time checking the ingredients."
2. "As a busy employee, I want a ready-made meal plan for the week with a shopping list so that I can quickly order everything in one place."
3. "As a student on a tight budget, I want to see recipes with cheap ingredients from the nearest store."

**Initial scope:**
Store data parsing (catalog, prices, ratings), data cleaning and structuring (CSV, pandas), bot architecture development (states, query processing), ML model design for recommendations (preference analysis).

# 4. Tech-stack

This week we used Python and the Selenium and BS4 libraries for data parsing, and we used Pandas to work with the product database.

The Telegram bot will be written in Python, the mini-app for the Telegram bot will be written in React, for ML we will use PyTorch, for the backend we will use FAST API.

# 5. Weekly commitments

**Individual contribution of each participant:**
We conducted a parsing of the entire catalog of the Magnit store. Each of us individually dealt with our own categories: First, we collected product links from each catalog, and after that, using Python, we went through each product link and saved all the necessary characteristics of each product in a csv table. Then, through the pandas library, we removed all the empty lines, sorted the products, and removed all products with a rating below 4.5 to improve quality. Our backend developer thought over the architecture of the application, and ML developers began to think over the ML part for implementing AI into our product. Data analyst and Frontend developer mostly worked with tables and links in csv table.

In this repo we pushed code of first parser, which go through the product categories and collect link of each product.
[https://github.com/IU-Capstone-Project2025/mealix/tree/ProductLinks_parser](https://github.com/IU-Capstone-Project2025/mealix/tree/ProductLinks_parser)

In thid repo we pushed code of second parser which collect data of each product by its link.
[https://github.com/IU-Capstone-Project-2025/mealix/tree/ProductData_parser](https://github.com/IU-Capstone-Project-2025/mealix/tree/ProductData_parser)
