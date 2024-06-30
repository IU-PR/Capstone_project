---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member        | Telegram ID   | Email Address                             |
|--------------------|---------------|-------------------------------------------|
| Egor Lebedev       | @egorled      | e.lebedev@innopolis.university            |
| Alie Ablaeva       | @laliyenl     | a.ablaeva@innopolis.university            |
| Sofia Gamershmidt  | @Miss_Shmidt  | s.gamershmidt@innopolis.university        |
| Ilsiia Nasibullina | @ilsiya_n     | i.nasibullina@innopolis.university        |
| Alex Shulmin       | @xhug_xhug    | a.shulmin@innopolis.university            |

### **Value Proposition**

- Identify the Problem:

    Modern lifestyles frequently leave people with little time to plan and prepare healthy meals. Many people struggle to maintain a balanced diet due to a lack of time, nutritional awareness, or trouble finding appropriate meals. This causes poor eating habits, weight difficulties, and vitamin and protein deficits. People face distinct challenges such as problems planning meals and finding ideal recipes, tracking the time required to make meals, and calculating calories. When looking for a service to assist with menu preparation, a person can only discover either a weekly meal template that does not take into account personal needs and tastes, or paid menus from a nutritionist online.

- Solution Description:

    Our software project addresses these issues by creating a Telegram bot that generates a personalized weekly menu and shopping list based on user information. Customers can set their preferred cooking times, calorie counts, and dietary allergies. The bot produces meal plans based on your tastes, ensuring that your overall menu is balanced. Daily customized recipes, automatic shopping list generation, and convenient access via a popular chat platform are among the key features. Unlike existing subscription services or static meal plans, the solution is free and simple to use, making it accessible to a wide audience.

- Benefits to Users:

    By using our Telegram bot, users will greatly improve their meal planning process. The bot increases productivity by saving time that would otherwise be spent planning meals, searching for recipes, and creating shopping list. It ensures efficiency by creating balanced, calorie-controlled diets that take into account individual dietary restrictions and preferences. The service is free, therefore users will save money by not having to pay for a dietician consultation. Dynamic personalized meal plans will help users manage their weight more effectively, improve their overall health and simplify the shopping process through automatically generated lists.

- Differentiation:

    Our software project distinguishes itself from rival options through its dynamic, individualized approach to meal planning. Unlike template menus or the expensive services of a nutritionist, our bot provides free, customizable meal plans that reflect the user's preferences. The ease of accessing the service through Telegram adds to its preference over other existing solutions. The ability to dynamically change meal plans based on user data distinguishes it from competitors, making it the greatest option for customers seeking a flexible, accessible, and cost-effective solution for their dietary demands.

- User Impact:

    Our Telegram bot has a greater impact on society as a whole, not just individual consumers. Promoting healthier eating habits has the potential to help improve public health outcomes. Users will experience transforming effects in their daily routines, with improved meal planning and better dietary management resulting in beneficial lifestyle improvements. The bot enables users by allowing them to control their nutritional choices, making healthy eating more accessible and manageable. In the long term, this could result in lower healthcare expenses and a more health-conscious community.

- User Testimonials or Use Cases:

    We intend to gather feedback from clients and create case studies in order to highlight the importance and advantages of our software product. One consumer might describe how the bot's consistent, well-balanced meals that suited their dietary requirements and timetable helped them lose weight. Another case study would focus on a user who struggled to prepare meals due to particular food allergies but is now able to eat a varied and safe diet thanks to the bot's help. Presenting these real-world instances will strengthen our project's effectiveness and applicability while also giving it more legitimacy.

## **Lean Questionnaire**

1. What problem or need does your software project address? 
   
   The software project addresses several key problems and needs, such as time-consuming meal planning, calorie management, dietary restrictions and preferences. 
   - **Time-Consuming Meal Planning**: the bot automates the meal planning process and creates shopping list, saving users time and effort by providing a ready-made menu for the week.
   - **Calorie Management**: the bot provides meal plans with precise calorie counts, helping users stay within their desired calorie range.
   - **Dietary Restrictions and Preferences**: the bot customizes meal plans to accommodate various dietary restrictions and preferences, ensuring all meals are suitable for the user.

2. Who are your target users or customers?
    
    Our target users are individuals who are actively trying to manage their weight, whether they are trying to lose, maintain, or gain weight. This includes individuals with specific dietary restrictions or preferences such as allergen considerations. Additionally, our platform can be useful for people who have limited time for meal planning and prefer a convenient solution to ensure they eat balanced and nutritious meals.

3. How will you validate and test your assumptions about the project?

   - Conduct surveys and questionnaires among potential target users to understand their needs, preferences, and pain points related to meal planning and dietary management.
   - Analyze existing meal planning apps and services to identify gaps in the market and areas for improvement.
   - Release the MVP to a small group of beta testers from the target user base to gather initial feedback.

4. What metrics will you use to measure the success of your project?

   - **Number of Sign-Ups**: Track the total number of users who sign up for the bot.
   - **User Growth Rate**: Measure the rate at which new users are joining over time.
   - **User Retention Rate**: Calculate the percentage of users who continue using the bot over a defined period (e.g., one month, three months).
   - **User Ratings and Reviews**: Collect ratings and reviews from users regarding the quality and suitability of the menus provided.
5. How do you plan to iterate and pivot if necessary based on user feedback?
   - Regularly collect feedback through surveys, user interviews, and observing user interactions to pinpoint areas for enhancement or possible changes.
   - Make adjustments or add new features based on user input, refining the product as needed. 
   - Stay adaptable and willing to implement substantial modifications to the platform if user feedback suggests a different strategy or extra features are necessary.

## **Leveraging AI, Open-Source, and Experts**

   - Open-source:

        In this project our team decided to build everything up from scratch, so we will use open-source Python libraries and MongoDB or PostgreSQL for data storing. 
   - AI:

        As for AI, we will consult with chatbots like ChatGPT or Claude models to get more experience in unknown fields faster and resolve confusing errors. 
   - Experts:

        We will also contact advanced nutritionists to review the quality of generated menus.

## **Defining the Vision for Your Project**

- Overview: 

  We want to ease people's lives by solving a serious problem - deciding, what to eat on each day. Main product we are going to provide is a Telegram bot which creates the menu for a week with several meals for each day. We are intending to provide the most diverse set of options in the market to satisfy a greater range of customers. Such menus could help people stay fit, manage time for cooking, since our menu will be constructed to optimize product use, minimize time spendings, and count calories. But even with such great surrounding qualities, main goal of our menu is providing concrete, high quality, and diverse meal schedule. Additionally, our bot provides free solution of this problem with a large number of hyperparameters for customers.

- Schematic Drawings:

   Preliminary simplified schema of our project:
   
  ![project_schema](/2024/FindRecipe/project_schema.jpg)
    
    Database structure:

  ![database](/2024/FindRecipe/DataBase.png)
    
- Tech Stack: 

  We are planing to use:
     * FastAPI: framework for backend development
     * Mongodb: for connecting and maintaining database
     * Telebot: for Telegram bot creation
     * Python: main development language in our project
     * MongoDatabase / SQL database

