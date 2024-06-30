---
title: "Week #3"
---

## Week 3: Developing the First Prototype, Creating the Priority List

---

### Backend Development:

- Implemented local storage for generated recipes to reduce AI generation costs and time. Recipes can be reused by other users, with popular recipes highlighted based on likes.
- Developed JWT security for user authentication and authorization, including endpoints for login and token generation, token validation in middleware, and securing API endpoints with role-based access control.
- Added functionality to delete and create user accounts.
- Improved API interaction by fixing URLs.
- Refactored database structure to store recipe photos.
- New database schema implemented.

---

### Machine Learning (ML):

- **YOLOv8 Model Training:**
  - Trained on a [Retail Store Dataset](https://universe.roboflow.com/muhammadmoin-y1qrz/retail-store-axhqk), showing good performance for well-represented ingredients but struggled with underrepresented classes due to dataset imbalance.
  - Defined a basic set of ingredients for consistent recognition and commenced image collection from grocery stores to improve dataset quality.

- **MistralAPI Functionality:**
  - Completed functionality to generate recipes and provide daily advice.
  - Implemented `generate_recipes` and `daily_advice` methods.
  - Developed communication between Python code and other app components using FastAPI.
  - Implemented methods to get recipes and daily advice via HTTP requests.

---

### Mobile Development:

- Implemented authentication processes including registration, login, and logout functionalities with email verification for new accounts.
- Developed the main page to display mock data with recipes' names and photos.
- Integrated camera capabilities for capturing or selecting images, which are processed using backend ML algorithms for product recognition.
- Added the option for users to manually input ingredients.
- Utilized Retrofit for network communications and Jetpack Compose for interface design.

---

### Data Management:

- New database schema implemented:

  ![db_schema](/2024/cookainno/db_schema.jpg)

---

### Prototype Testing:

- Currently, only local testing by developers has been implemented.

---

### Prototype Features:

During the third week there have been some useful assumptions and serious reorganizations of the application navigation. Additionally, in the meeting discussion, we sumed up the first priority functions of the application and synchronized it with the whole team. You can see the results of the team brainstorm and a detailed description of the approved version of features below:

  ![board1](/2024/cookainno/board1.jpg)
  ![board2](/2024/cookainno/board2.jpg)

- **Main Tab (Low Navigation Bar, Middle Button):**
  - Displays general recipe recommendations.
  - Includes a search bar for recipe names.
  - Features an AI activation button for photo functions, allowing users to load or take photos, with AI recognizing and filling ingredients automatically. Users can manually adjust ingredients.
  - Accept button triggers recipe search/generation appearing on the main page.

- **Favourite Recipes (Low Navigation Bar, Left Button):**
  - Shows liked recipes with a search by name feature.
  - Allows opening and viewing full recipe descriptions.
  - Enables sorting recipes by the date of addition to favourites.

- **User Profile (Low Navigation Bar, Right Button):**
  - Displays short personal info and a profile picture.
  - Provides daily AI-generated advice tips for health maintenance.
  - Allows changes to personal height and weight.
  - Calculates daily calories based on preferred mode (gain weight, normal, lose weight).

- **User Interface:**
  - Includes registration, sign-up/sign-in, receipt recommendations, AI camera (take/upload photo, add ingredients manually), search receipts, view liked food items, get daily advice, set user parameters (height, weight, daily calories).
  - Link to [user flow](https://www.figma.com/board/1cEHXZAlCBIHG2Nmt6B9MQ/Untitled?node-id=1-899&t=SJurddamCnsLBnRv-1)
  - Link to [figma design](https://www.figma.com/design/vpqc9bsK1bBngEr7yXHRUP/Untitled?node-id=179-301&t=xYZ4KH6osEuln5xc-0)

  ![design2](/2024/cookainno/design2.jpg)

---

### Challenges & Solutions:

- **Challenge:** Android developers did not know how to link screens together and how transitions would be performed. 
  - **Solution:** In this regard, we decided to organize a meeting and decide at it what functionality of the application and what logic will be implemented in it. After the meeting, we reviewed some details of our idea and moved the "favorite foods" to the main screen, and the camera to the recipe search button. Thus, the application began to look more logical and user-friendly.

- **Challenge:** Ineffective and unscalable solution for searching stored recipes by ingredients.
  - **Solution:** Decided to implement search functionality by recipe name for the first version of the product. Engredients will be used only for the recipe generation for now. In future versions of the product we will analyse possible solutions for the current temporary problem and provide users with more comprehensive filtering from existing/stored recipes.

---

### Conclusions & Next Steps:

During the third week, significant progress was made across backend, ML, and mobile development. The backend saw enhancements in storage, security, and database structure. In ML, model training advanced with steps taken to address dataset imbalance. Mobile development focused on user authentication and integrating camera capabilities. These efforts collectively pushed the project closer to a functional prototype.

**Next Steps:**

- Collect and annotate images for dataset and retrain the model on the extended dataset to enhance performance across all ingredient classes.
- Research and consider using remote storage for recipes to enable searching non-generated recipes by ingredients.
- Implement logic and endpoints for calorie recommendation calculations.
- Involve first real users to test the app prototype.
- Implement screens with recipes and favourite recipes, gather items for them from database.
- Create ingredients insertion and camera recognition for recipe generation and show the generated recipe with photo.
- Implement profile screen with daily recomendation option, connect them to ML part.
- Adjust colors and improve UI/UX.
