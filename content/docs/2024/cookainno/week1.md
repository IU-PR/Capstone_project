---
title: "CookAInno"
---

# **Week #1**

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address                     |
|--------------------------|---------------|-----------------------------------|
| Efim Puzhalov (Lead)     | @yeaphm       | e.puzhalov@innopolis.university   |
| Egor Meganov             | @KezhKesh     | e.meganov@innopolis.university    |
| Vladislav Grigorev       | @VLADISLAVVV777 | v.grigorev@innopolis.university |
| Renata Latypova          | @renalaty     | r.latypova@innopolis.university   |
| Polina Pushkareva        | @pupolina     | p.pushkareva@innopolis.university |
| Milyausha Shamsutdinova  | @mili_sham    | m.shamsutdinova@innopolis.university |
| Aliia Bogapova           | @ch3rnushka   | a.bogapova@innopolis.university   |

### **Value Proposition**

#### Identify the Problem:
  Many people struggle with meal planning, finding recipes that match their dietary preferences, managing their daily calorie intake, and efficiently using ingredients they already have at home. Moreover, one big problem is food waste, which is often associated with a fridge full of seemingly mismatched ingredients. Therefore, an environment that helps people save time and use food rationally is needed.

#### Solution Description:
  CookAInno is a mobile app that simplifies meal planning by providing personalized recipe suggestions based on user preferences, dietary restrictions, and available ingredients. The app leverages AI to recognize food items from photos of the user's fridge and generates new recipes.

#### Benefits to Users:
  - Personalized recipe recommendations.
  - Efficient use of ingredients already available at home.
  - Easy tracking and management of daily calorie intake.
  - Simplified meal planning that accommodates dietary restrictions.
  - Enhanced cooking experience with AI-generated recipes and images.

#### Differentiation:
  - Advanced AI integration for food recognition and personalized recipe generation.
  - Use of AI models for creating unique recipes and generating appetizing images.
  - A holistic approach that combines meal planning, dietary management, and recipe discovery in one app.
  - Seamless user experience from fridge photo upload to meal preparation.

#### User Impact:
  - Reduces the stress of meal planning and grocery shopping.
  - Encourages healthier eating habits by providing calorie-managed meal options.
  - Saves time and reduces food waste by suggesting recipes based on available ingredients.
  - Enhances cooking skills with diverse and creative recipes.

#### User Testimonials or Use Cases:
  - A student, after a long studying day, comes home, downloads a photo of the food in the fridge to CookAInno, and gets recipes that require minimal time and effort.
  - Before grocery shopping, one can download a photo of the fridge to see what can already be cooked and also get a list of other ingredients for meals for the next few days.
  - A person trying to lose weight can download a meal photo to see the caloric intake of the meal without wasting much time.

## **Lean Questionnaire**

1. What problem or need does your software project address? 
   
   The app addresses the problem of meal planning, recipe discovery, and dietary management by providing personalized and AI-driven solutions to make cooking easier and more efficient.

2. Who are your target users or customers?

   - Individuals with specific dietary preferences or restrictions (e.g., vegans, vegetarians, lactose-intolerant).
   - Health-conscious users who want to manage their calorie intake.
   - Home cooks who want to reduce food waste and use available ingredients efficiently.
   - Mothers.
   - Students.
   - Everyone who wants to study cooking.

3. How will you validate and test your assumptions about the project?

   - User Interest and Engagement
     - Surveys and Interviews: Conduct a survey among potential users (students of Innopolis University) to understand their interest in such an app. Ask about their cooking habits, pain points, and willingness to use technology in their kitchen.
   - AI Image Recognition Accuracy
     - Training and Testing: Train the AI model on a portion of the data and test it on the rest. Measure performance.
     - User Testing: Have users take pictures of their fridge and compare the AI's recognition results with manual inventories.
   - User Interface and User Experience
     - Prototyping and Usability Testing: Create a prototype of the app and conduct usability testing sessions with real users. Gather feedback on the layout, navigation, and overall user experience.
     - System Testing: Test the entire system as a whole to ensure it meets the project requirements and functions as expected.

4. What metrics will you use to measure the success of your project?

   - User engagement metrics
     - Daily Active Users/Monthly Active Users
     - Session Length 
     - Session Frequency
   - AI performance metrics
     - Image Recognition Accuracy
     - Processing Time
   - User interface and experience metrics
     - User Feedback and Ratings

5. How do you plan to iterate and pivot if necessary based on user feedback?

   We plan to iterate based on user feedback by making:
   - Prioritization 
     - Address critical pain points that significantly affect user satisfaction and app usability.
   - Development Sprints
     - Aim for frequent, smaller releases rather than large, infrequent updates. This allows us to address issues and introduce new features more quickly.

   We plan to pivot if necessary based on user feedback choosing from these strategies:
   - Feature Pivot: Shift focus to a different set of features or capabilities that better meet user needs.
   - Technology Pivot: Switch to a different technology or platform if current technical limitations are hindering progress.

## **Leveraging AI, Open-Source, and Experts**

### AI (Artificial Intelligence):

- AI food recognition: We will utilize ML models to identify food items in photos provided by users, enabling accurate recipe suggestions based on recognized ingredients.
- Recipe generation: We will use ready LLM and prompt engineering for generating the recipes in case the recipe was not found in the database.
- Personalized recipe recommendations: We will create a recommendation system based on user-saved recipes.
- Menu Composing: We will either use the ChatGPT model for generating menus based on users' preferences or implement straightforward logic for choosing food recipes for the menu from a database based on users’ saved recipes.

By leveraging AI in these areas, CookAInno aims to provide personalized, efficient, and engaging user experiences.

### Open-Source:

Open-source resources play a significant role in the project’s development and success. The AI features of our project will be implemented using open-source ML models, datasets, and libraries. Additionally, we will use open-source tools and libraries for the development of the application.

### Experts in Relevant Domains:

For our project on AI recognition of fridge contents through a phone camera and recipe suggestion based on available ingredients, we will seek the expertise of several key professionals. While we aim to develop the app independently, we will reach out to experts for guidance and assistance. We expect to collaborate with computer vision experts, including university professors, to enhance the accuracy of object detection and recognition algorithms. Additionally, we may consult backend and Android developers whose expertise will be helpful in project creation. Furthermore, we will seek insights from chefs and culinary experts, such as those from the university canteen, to ensure the correctness of product placement in the fridge and to cater to various dietary preferences.

## **Defining the Vision for Your Project**

#### Overview: 

CookAInno aims to revolutionize how users interact with their kitchen by integrating AI-driven food recognition and personalized recipe recommendations. Here's a detailed breakdown of its key functionalities:

1. User Authentication and Account Management:
   - MVP 1:
     - Sign-Up and Login Functionality: Users can create an account and log in securely.
     - User Profile Management: Store and manage user-specific information such as height, weight, and age.
     - Favorite/Saved Recipes: Users can save and categorize their favorite recipes for easy access and better recommendations.
   - MVP 2:
     - Daily Calorie Calculation: Automatically calculate the recommended daily calorie intake based on the user’s weight and height. 

2. AI Food Recognition
   - MVP 1:
     - Photo Upload/Capture: Users can upload or capture photos of their fridge contents.
     - Image Recognition: Utilize AI to identify food items in the uploaded images.
     - Immediate Suggestions: Instantly display recipes that can be made with recognized ingredients.
   - MVP 2:
     - Manual Adjustment: Allow users to manually adjust identified items before displaying possible recipes in case of wrong recognition.

3. Personalized Menu Planning
   - MVP 1:
     - Recipe Search: Allow users to search for recipes by name.
     - Ingredient-Based Filtering: Enable users to filter recipes that can be made with the ingredients they have on hand.
   - MVP 2:
     - Dietary Filters: Provide filters for specific diets like vegan, vegetarian, halal, and lactose-free options.
     - Daily Menu Suggestions: Generate daily menu suggestions based on the user’s calorie needs and preferences using a recommendation system (RecSys) or GPT API.
   - MVP 3:
     - Recipe Generation: Use GPT API to create recipes based on identified food items or suggest items to purchase if ingredients are missing.
     - Food Image Generation: Generate images of the food from generated recipes using DALL-E or Midjourney API.

#### Schematic Drawings:
  ![user_scenarios](https://github.com/yeaphm/cookainno/blob/master/static/2024/cookainno/user_scenarios.jpg)

#### Tech Stack:
  - Backend (Java, Spring, Docker)
  - Database (PostgreSQL) 
  - Third-party APIs
  - Android (Kotlin, Jetpack Compose, Retrofit, Room, CameraX)
  - ML (Python, OpenCV, Scikit-learn, PyTorch, TensorFlow, Keras)
