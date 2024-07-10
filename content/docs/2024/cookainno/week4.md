---
title: "Week #4"
---

# Week 4 - External Feedback

Welcome to Week 4 of the Capstone Project! This week has been pivotal as we delve into testing, feedback integration, and continuous iteration. These processes are crucial to ensure we deliver a high-quality, functional product that aligns with our original vision. This report provides a detailed account of our activities, findings, and future steps for the CookAInno app.

## External Feedback

In Week 4, our team conducted the first user testing of our application prototype. Despite some features still under development, we showcased the functioning Android app, UI/UX design, and gathered valuable feedback for continuous iteration and reinforcement of the CookAInno app.

We collected feedback from friends and their associates, ensuring honest and valuable reactions to our current progress. Participants tested the Android app and filled out a short feedback form. Additionally, we shared the design of the Android app with those unable to access the app itself and provided the same questionnaire to gather additional comments and suggestions.

- **Google Form:** [Form Link](https://docs.google.com/forms/d/e/1FAIpQLSdDlMMATe2F1uxXDEFa9Dho3_KlDtwizT4J6jQD81NsioRGPA/viewform)
- **Google Form Results:** [Results Link](https://docs.google.com/spreadsheets/d/1ygEoXQvIPhhOETLZBdRW9vb2d5vuYKVJYgemA9itZC0/edit?gid=649458892#gid=649458892)

### Aggregate Outcomes from the Research:

![w4f1](/2024/cookainno/w4f1.png)
- **Cooking Frequency:** The majority of respondents cook at least once a day, confirming the project's relevance and potential user base.

![w4f2](/2024/cookainno/w4f2.png)
- **Struggles with Cooking Ideas:** Most students struggle with generating cooking ideas, underscoring the need for our application.

![w4f3](/2024/cookainno/w4f3.png)
- **App Usefulness:** Feedback indicates that users find the app potentially useful for their daily cooking needs.

![w4f4](/2024/cookainno/w4f4.png)
- **UI Design:** Overall, the UI design was well-received, although some users provided constructive feedback for improvements.

### User Comments:

![w4f5](/2024/cookainno/w4f5.jpg)
- **Emil:** "Very nice app. The design is awesome!"

![w4f6](/2024/cookainno/w4f6.jpg)
- **Mikita:** "Awful appearance. Who has been matching the colors?" "It would be great to see a wider bottom navigation bar. There may be misclicks due to the close placement of buttons."

![w4f7](/2024/cookainno/w4f7.jpg)
- **Egor:** "Everything is clear, the icons here are awesome." "Everything is intuitive." "The pink is too caustic, maybe a different pink." "Brighter highlight of the active page on the bottom navigation bar." "Found a bug with the jumping loading icon."

![w4f8](/2024/cookainno/w4f8.jpg)
- **Alsu:** "Wow, there's even a recipe for dumplings!!!"

![w4f9](/2024/cookainno/w4f9.jpg)
- **Abdurakhmon:** "It would be nice to be able to enlarge the picture to see better what kind of dish it is. Very cool!"

## Testing

### Unit Testing

Throughout the iterative development process, we continually test small components to ensure their proper functionality. This approach guarantees that the production environment is populated with working components before integration into the final application.

**Current Stage Findings:**
- **Backend Functionality:** Identified an issue where old test users were not deleted upon backend restart, causing application crashes. This was resolved by manually deleting test users from the database. Such bugs are critical to address in the testing environment to prevent similar issues in production.
- **Android:** During the development process, we experimented with altering the 'pagesize' parameter for loading recipes from the backend to test the recipe updating feature. However, we encountered an issue where duplicate or incorrect recipes appeared in our list. We found out that the 'page' parameter in the query does not represent the page number, but rather the number of recipes to skip. Having identified this, we promptly fixed this bug.

### Integration Testing

Integration testing ensures that different components of our application work seamlessly together.

**Issues Identified:**
- **Recipe Generation:** Inconsistencies were found between the expected format of responses from the Python API and the Android side, resulting in empty pages without generated recipes. Future steps will involve stricter format adjustments for API responses.

### User Testing

User feedback collection revealed unexpected behaviors, resulting in valuable test cases not previously considered.

**Issues to be Fixed:**
- Lagging loading animation appearing in different screen parts while updating the main page.
- Sharp corners of the “search” label on the search bar when typing the request.

**UI Design Feedback:**
- Current pink color seems to be bright and unpleasant to see. Can be changed to another color or another softer tone.
- Need for the brighter highlight of the active page on the bottom navigation bar. The current one seems low visible, which causes misunderstanding on which page user is currently located.
- It would be great to see a wider bottom navigation bar. There may be misclicks due to the close placement of buttons.

## Iteration and Refinement

### Mobile Part

**Achievements:**
- **Recipe Generation:** Implemented the ability to generate recipes by manually adding ingredients. This feature was developed in anticipation of the machine learning part, which will recognize ingredients from images. Now we can add ingredients in the list and generate the recipe (currently without an image).
- **Recipe Database:** Created a database of recipes. Developed a screen to display these recipes, and upon clicking a recipe, its details are shown (name, ingredients, and instructions).
- **Favourites Functionality:** Implemented a favourites functionality, allowing users to add and remove likes from user’s favourite recipes. Created a screen to display these favourite recipes, with the number of likes shown next to each recipe.

![w4f10](/2024/cookainno/w4f10.jpg)

**Changes Based on Feedback:**
- **Camera Functionality:** Moved the camera functionality (for recognizing recipes) to the screen where we add ingredients, as users found this more logical.
- **UI/UX Improvements:** Users praised our UI/UX for being comfortable to use. However, feedback indicated that our color scheme is a bit too bright and annoying. We plan to refine this next week, adhering to best practices of design and color combinations.

### Machine Learning

**Achievements:**
- For grocery item detection model, gathered a dataset of images featuring underrepresented classes of grocery items from local stores in Innopolis. This involved taking photographs of different products to create a diverse and representative dataset for training the model.
- Created an API for the grocery items detector, which will serve as the interface for the mobile app to interact with the ML model and retrieve detection results.

### Backend Development

**Achievements:**
- **Finalized Functionality:** Implemented the last feature of the MVP for daily calorie calculation and refined backend design to store generated recipes, enhancing user recommendations.
- Refined the backend design to not just always generate recipes, but also store them in the database. This allows for access to all recipes generated from our app and forms a rating system for user recommendations based on the preferences of most users.

## Challenges and Solutions

**Android:**
- Implemented a feature to check if a recipe is in the user's list of favorites and accordingly show the like button, but the process of integrating this functionality presented some complexities that we had to navigate.

**Machine Learning:**
- Established a final list of grocery items that the model will be able to recognize from the photographs. The classes include:
  - **Dairy products:** milk, eggs, flour, yoghurt, cheese.
  - **Vegetables:** cucumber, tomato, carrots, bell pepper, onion, garlic, peas, beans.
  - **Fruits:** banana, apple, lemon, orange.
  - This clear categorization will improve model performance on real photos by focusing on specific, commonly recognized grocery items.

## Next Steps

**Android:**
- Create a profile screen with nutrition tips and calories calculation.
- Implement search functionality for recipes.
- Develop pages for user characteristics during registration for calorie calculation.

**Machine Learning:**
- For grocery item detection models, collect additional images from the internet to broaden and diversify the dataset. This will involve sourcing a variety of images to ensure the model can generalize well to different conditions and packaging.
- Annotate collected images for grocery items detection model and retrain the model using the expanded dataset to refine grocery items detection.

**Backend:**
- Implement deployment for stable and continuous remote connection between the Android app and backend services.

## GitHub Issues

- You can see our current tasks in [GitHub Issues](https://github.com/orgs/IU-Capstone-Project-2024/projects/6/views/1).

This week has been instrumental in refining CookAInno through user feedback, rigorous testing, and continuous iteration. We remain committed to regularly assessing our progress, comparing it against our initial goals, and making necessary adjustments to enhance our application's design, features, and functionalities. By fostering collaboration and maintaining a focus on user needs, we aim to deliver a product that not only meets but exceeds expectations.