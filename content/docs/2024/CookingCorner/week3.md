---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

Currently, our team is sticking to the initial scheme of infrastructure:

![](/2024/CookingCorner/General_infrastructure_with_user.png)

- **Backend Development**:

Current priority list for backend:

1) Create additional endpoints for recipes

2) Create endpoints according to the designer and frontender requests

3) AI integration

- **Frontend Development**:

Current priority list for frontend:

1) Connect existing pages to the backend endpoints and test them

2) Design pages for settings and editing profile/recipes 

3) Create desktop analogues for the current mobile design

- **Data Management**:

Current design of database for our project:

Created 5 tables:

| recipe          |         
|-----------------|         
|id               |         
|name             |         
|description      |         
|icon_path        |         
|rating           |         
|user_id          |         
|category_id      |         
|preparing_time   |         
|cooking_time     |         
|waiting_time     |         
|total_time       |         
|portions         |         
|ingredients      |         
|how_to_cook      |         
|images_paths     |         
|comments         |         
|nutritional_value|         
|proteins_value   |         
|fats_value       |         
|carbohydrates_value|         
|dishes|         
|video_link|          
|source|         


|users|
|----|
|id|
|username|
|hashed_password|
|email|
|name|
|surname|
|cooking_experience|
|image_path|

|category|
|--------|
|id|
|name|

|tags|
|----|
|id|
|name|
|user_id|

|recipe_tag|
|---------|
|id|
|recipe_id|
|tag_id|

- **Prototype Testing**:

Current prototype is available through this link: https://www.figma.com/design/VutdYJEW7nxaz0BhGJExvL/Cooking-Recipe-App-design?node-id=0-1&t=UEvomQhrpfn9WVeD-1

## **Weekly Progress Report**:

#### **Design**

1) Design for recipe steps and ingredients window

2) Templates for recipes and their buttons

#### **Mobile**

1) Authorization data & domain layers done

2) Main splash screen done

3) Main navigation logic done

4) Home tab done

5) Profile page done

#### **Backend**

1) Improved login/register endpoints (now they are working with bearer token, and for register it is enough to write username and password)

2) Added endpoint for categories (get_all)

3) Added endpoints for tags - get_all, create, update, delete

4) Added endpoints for recipes - get_by_id, get_all, create, update, delete

#### **Frontend**:

1) Implemented sign-in, sign-up, search, home, profile pages

2) Validation and data retrieval from fields on sign-in/sign-up pages

3) Implemented recipe cards where brief information about the recipe and who added it is displayed.

4) Implemented the display of information about the user in the profile

5) Added a search bar that filters recipes by their name.


### **Challenges & Solutions**

We were thinking about integrating AI. So we have decided to use it to get all the information from raw description of 
some recipe provided by user (from some website), such as price of products, time to cook, nutritional value etc. It
can be useful because not all recipes contains such small details, but these details (even if they are generated and 
calculated approximately) can really help people with cooking.

### **Conclusions & Next Steps**

For the next week our team is planning to:

1) Design of URL converting page from a link to a ready-made recipe

2) Design settings and other miscellaneous features

3) Design a page for a recipe

4) Continue working on recipe routes and other requested routes

5) Integrate AI

6) Connect backend with frontend design and test it manually

