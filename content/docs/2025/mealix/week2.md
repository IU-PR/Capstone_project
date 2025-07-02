# Practicum Project Summer 2025 **Report 2**  
**Team mealix**

| Team Member        | Telegram Alias   | Email Address                | Track       | Responsibilities                      |
|--------------------|------------------|------------------------------|-------------|---------------------------------------|
| Samat Iakupov      | @samerspc        | sa.iakupov@ innopolis.university | Frontend    | Task distribution, Frontend development |
| Alexander Kachmazov | @vozamhcak       | a.kachmazov@ innopolis.university | ML          | Machine learning models development   |
| Dmitrii Antipov    | @stacss          | d.antipov@ innopolis.university | Backend     | Database and API development          |
| Danil Eramasov     | @Danil0Danil     | d.eramasov@ innopolis.university | ML          | Data preprocessing and analysis       |
| Albert Shammasov   | @myavg           | a.shammasov@ innopolis.university | Data Analyst | Data preparation and management       |
---

## 1. Detailed Requirements Elaboration

We have a big project with many challenging tasks and plans. Therefore, we need to work in three different ways, transitioning between them after setting everything up. This week, we aimed to **create the basic functionality of our bot, implement a script that can generate a menu for one day, and parse the necessary data including recipes**. Each of us had important tasks, and overall, we accomplished everything we had planned.

**Prioritized backlog:**  
[https://github.com/orgs/IU-Capstone-Project-2025/projects/20/views/1](https://github.com/orgs/IU-Capstone-Project-2025/projects/20/views/1)

---

## 2. Project Specific Progress

### Frontend ([Branch](https://github.com/IU-Capstone-Project-2025/mealix/tree/frontend))
- There is a home page and a registration page with a survey for new users.
- Routing for these pages is implemented, taking into account user authorization.

### Backend ([Branch](https://github.com/IU-Capstone-Project-2025/mealix/tree/main/tg-bot))
- Built the bot's core with launch/settings commands.
- Started the backend for data storage and AI modules.

### ML ([Branch](https://github.com/IU-Capstone-Project-2025/mealix/tree/llm_agent_code))
- The script already generates a menu for one day. It reads your information and preferences and tries to generate the best menu option for you. The menu is saved in a JSON file. Exception handling is implemented. For the generated menu, we implemented a script that selects products from our "Magnit" database.

---

## 3. Weekly Commitments

### Individual contribution of each participant:

**Alexander Kachmazov (ML):**  
Implemented a Python script that generates a menu for the day using Yandex GPT. The program reads the user's preferences (general, for today, and allergies) from text files, generates a request, and sends it to Yandex GPT Lite. The model's response is parsed as JSON and saved to the output file. Exception handling is provided for errors (missing files, incorrect response format). [Link](https://github.com/IU-Capstone-Project-2025/mealix/blob/llm_agent_code/ml/generate_menu.py)

**Samat Iakupov (Frontend):**  
1. Implemented the initial project structure and prepared the environment. [Link](https://github.com/IU-Capstone-Project-2025/mealix/commit/df579aa5b2783fcce9191bc89d6a3aab25c96418)  
2. Chose and implemented the architecture, also documented it. [Link](https://github.com/IU-Capstone-Project-2025/mealix/blob/frontend/frontend/README.md)  
3. Created the main page and the registration page with a survey for new users. Set up routing for these pages, considering user authorization. [Link](https://github.com/IU-Capstone-Project-2025/mealix/commit/59064bd8b522f37e02c097523a7774df042baefc)

**Dmitrii Antipov (Backend):**  
Implemented the basic structure of the bot, added the initial commands for startup and settings. Started implementing the backend part of the application to save data and a bunch of bots, mini-apps, and AI. [Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/tg_bot/tg-bot)

**Danil Eramasov (ML):**  
1. Wrote Python code so that by simply changing the link, data from the site povarenok.ru is parsed. Processed 300 recipes of various dishes from 10 categories. Entered each category into a separate JSON file with ingredients, cooking method, number of calories, and other data. [Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/Recipes_parser)  
2. Created a backlog for our project and distributed the tasks into three columns: ToDo, In Progress, Done (the link is attached above).

**Albert Shammasov (Data Analyst):**  
Implemented a function that selects the best products from the "Magnit" database based on the generated diet for the user. [Link](https://github.com/IU-Capstone-Project-2025/mealix/commit/f777332cd6fdb8e807c018a3a46e433075c85c3e)

---

## Plan for Next Week

### Frontend
We plan to implement pages where diet generation will be available, separate pages for generated dishes, their recipes, and ingredients. Also, implement connection with the backend via Docker.

### Backend
We plan to implement all base endpoints, create a separate server for ML, and establish connections between all services via Docker.

### ML
Next week, we will finish our LLM agent, as discussed in the meeting with the TA. It will generate a diet with recipes for dishes and the necessary ingredients.
