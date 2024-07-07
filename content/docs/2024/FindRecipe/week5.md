---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

  This week, our primary objective is to gather comprehensive feedback from stakeholders to refine our product. To achieve this, we have prepared Feedback Collection Tools:
  
  - Develop a structured feedback form using online tools like Google Forms.
  - Create an online chart for quantitative assessments of various features.
  - Include specific questions focusing on:
    - Usability
    - Functionality
    - Overall satisfaction
    - Preferences on calories, cooking time, number of products, and spiciness
    - Prepare interview scripts with open-ended questions for deeper insights.

- **Conducted user surveys or feedback sessions**

  Throughout the week, we successfully conducted 15 online survey responses collected via our structured feedback form. We sent this form to our student chats. The survey was focused on understanding user experiences, identifying pain points, and collecting suggestions for new features.
  
  **Documenting Feedback Received**
  
  The feedback collected was documented meticulously, highlighting key insights:
    
   - **Usability**:
    
      - Users appreciated the intuitive interface but suggested improving the navigation flow.
      - Some users found the recipe filtering options limited.
    
   - **Functionality**:
    
      - Requests for a broader variety of recipes, especially for specific dietary requirements.
      - Suggestions to include a feature for tracking consumed meals and nutritional intake.
      - Add dishes to favorites: Users want the ability to save and easily access their favorite dishes.
      - Product scanning: Users suggested incorporating computer vision to scan ingredients they have at home.
  
  **Overall Satisfaction**
  
  Most users expressed satisfaction with the personalized menu suggestions. However they suggested ideas to improve the bot.

- **Analyzing feedback, identifying and prioritizing issues**

  The feedback analysis revealed several common themes and areas for improvement:
  
  We need to prioritize the implementation of the "Add to Favorites" feature, redesign the navigation flow based on user feedback, expand recipe database and improve calorie accuracy.
  Continue collecting feedback to ensure ongoing refinement and user satisfaction.

## **Roadmap**:

Analyzing the Feedbacks above it is possible to build the following plan of action

### In the near future:
* We need to fix the design of the application, the feedback on this item is enough to make sure of the problem.
* Increase the number of filters.

### In the next month:
* We need to expand the database a lot and start partitioning the data into groups.
* Add favorite dishes and products.
* Need to refine the algorithm for new conditions.

### In the next year:
* Need to consider the idea of implementing CV tools

## **Weekly Progress Report**:

This week we finished the development of menu generating algorithm as well as collected a great base of 20k+ recipes to generate menu from. Also, [Telegram bot](https://t.me/WeeklyChefBot) functions smoothly, providing positive user experience. We will comtinue on polishing Telegram bot to find and exclude all bugs. At the same time, we will improve menu generation algorithm by adding new filters and parameters.

### **Challenges & Solutions**

While working on the menu generation, we faced the need of more data from the recipes, particulary data about number of servings for each recipe. This led to reconstruction of parsing code, since it wasn't optimal beforehand. By changing the style of saving recipe data and adding necessary new one, we resolved this issue. 

To provide the most informative menus, such menus must contain a set of pictures representing the recipes suggested in the menu. Sadly, Telegram does not allow to pin more than one image to the message, and we found an exquisite solution - collages. Combining three photos of breakfast, lunch, and dinner recipes in the one meaningful image for each day allowed as to show all pictures and satisfy such user need.

### **Conclusions & Next Steps**

We are satisfied with our product and our weekly progress, since this week we reached our goals from the previous one. Upcoming challenges are solved, Telegram bot works seamless and looks good. The next week will be dedicated to adding new parameters for users to set and tuning menu generation algorithm.
