---
title: "Week #6"
---

## Week 6 - Debriefing and Presentation

### Weekly Progress

During this week, our primary focus has been the preparation of our presentation and the finalizing of our application for the upcoming demo day. We are almost done, with all the intended functionalities implemented. At present, we are in the process of resolving minor issues to ensure a seamless demonstration on the demo day.

### Backend

- **Search by Recipe Name**: Fixed the search functionality to be case insensitive, include spaces, and work more intuitively.
- **Recipe Validation Logic**: Adjusted the validation logic for the recipe entity to better handle the size constraints of the recipe representation in the database.
- **Dockerfiles**: Wrote and enhanced the Dockerfiles for Backend and ML parts to include all necessary environment variables.
- **Logging**: Modified `docker-compose` and changed the log output to a console format for better readability and debugging.

### Mobile

- **Profile Page**: Fixed profile page parameters.
- **Calorie Counting**: Added the calorie counting logic to consider individual user parameters (age, weight, height).
- **Like Functionality**: Fixed and specified the like functionality by adding the ability to like recipes from the recipe description page.
- **Food Pictures**: Associated each generated recipe with a corresponding food picture. Implemented a feature to show retrieved food pictures on the generated recipe page using BeautifulSoup.

### ML - Recipe Generation

Mistral associated part of the work was completed during this week. Overall, we have two methods communicating with Mistral API which are recipes and daily advice generation. Both create their responses based on the user's preferences and concrete context.

Moreover, we completed the part with image generation for recipes, this was done by parsing web pages by the corresponding URL. And the final thing that was completed is FastAPI communication. Now we have four methods for communication with this Python part via HTTP requests. We have methods for recipes, daily advice, and image generation, and a default method for 'reading root'. Now, everything from this part works correctly and is already integrated into our app.

### ML - Ingredients Detection

This week, the grocery item detection model was refined by upgrading to a larger YOLO model, specifically YOLOv8x-oiv7, which is pre-trained on the Open Images dataset with 600 classes, compared to the previous COCO dataset with only 80 classes.

The number of training epochs was increased to 20, resulting in improved model performance. This enhancement was evident through visual analysis of evaluated testing images, showcasing better recognition and accuracy across a broader range of ingredients.

### Challenges and Solutions

#### ML - Recipe Generation

The main challenge appeared with image generation. Firstly, we did not know how we would generate images because MistralAPI does not have such functionality. We started to search for the available options, but all of them were blocked in Russia or had overly strong limitations on usage (we found SerpAPI and Yandex SearchAPI). 

So, for now, we decided to choose web pages parsing for image retrieval. This solution looks good for now but as a future work we need to consider more autonomous options. Secondly, during the creation of the FastAPI method for image generation, we faced another difficulty. At the beginning, we had no idea how to perform this task and if it is even possible. After some time and mainly research, we found out that this task is easily performed by the use of some additional methods.

### Future Work

Our future plans extend well beyond the capstone scope, aiming to enhance and expand the CookAInno app significantly. The next steps for development include a range of features and improvements designed to create a comprehensive and user-friendly food ecosystem.

1. **Ingredient-Based Filtering**: Enable filtering to show recipes that can be made with available ingredients from the saved recipe database without relying on AI generation.
2. **Ingredients Recognition**: Continuously refine the accuracy of image recognition by incorporating additional images from various sources to the dataset.
3. **Dietary Filters**: Develop filters for specific diets such as vegan, vegetarian, halal, and lactose-free, to cater to a broader range of user needs.
4. **Daily Menu Suggestions**: Introduce personalized daily menu suggestions based on user calorie needs and dietary preferences, using a sophisticated recommendation system.
5. **Calorie Calculation**: Develop a feature to calculate the total calories of a meal based on the ingredients and portions used, helping users manage their diet and health goals more effectively.
6. **Shopping List Integration**: Create a shopping list feature that automatically generates lists of needed ingredients based on selected recipes, allowing users to edit and manage their shopping lists within the app.
7. **UI/UX Design Improvements**: Conduct thorough user testing to gather feedback on the UI/UX design and implement improvements, focusing on enhancing the user experience through better color schemes and navigation.
8. **Nutritional Insights**: Introduce a feature providing detailed nutritional information for each recipe, including macronutrient breakdown (proteins, fats, carbohydrates) and essential vitamins and minerals, supporting users in making informed dietary choices.
9. **Fixes**: Correct food items’ sizing issues on the main page.

By focusing on these areas, we aim to continuously enhance CookAInno, making it an indispensable tool for our users. Our commitment to user-centric development ensures that the app will evolve to meet and exceed user expectations.