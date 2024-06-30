---
title: "Week #4"
---

# **Week #4**

## **External Feedback**

During this week we have contacted our friends and asked them to try our app. 
Since some of them were using physical cookbooks for the whole their experience, they were interested 
in the alternative we have provided. 
Most of them were not using such apps before, so we could check how easy it is to interact with our app. 
Everyone has successfully created their accounts and tested the app. 
In the response our team did not notice any troubles with acknowledging the main functionality and its usage.

## **Testing**

For the current state our team has created several test cases for whitebox manual testing of all endpoints. 
For example, auth: testing that it is working correctly with correct data, returns 401 error if username already exists.
For the future we are planning to prepare unit tests to exclude potentially critical errors, and also we need 
to create CI/CD pipeline for further deployment.

## **Iteration**

For the current state of the project we have decided to redesign some parts of our app:

### Recipe list

* New version

![](/2024/CookingCorner/new_recipe_list.png)

### Recipe description

* New version

![](/2024/CookingCorner/new_recipe_desc.png)

Old versions are available in the report of week 2.

## **Weekly Progress Report**:

### **Design**

1) Designed a shimmer effect for the loading frames

2) Changed the button for creation recipe and the settings button

3) Created a blank recipe design panel

4) Added pages for recipes creation:

![](/2024/CookingCorner/new_things.png)

### **Mobile**

1) Implemented search screen

2) Implemented profile screen

3) Implemented detailed recipe screen

4) Implemented shimmer effect for loading

5) Implemented ripple effect on click

6) Added password visibility

7) Implemented auth API

**Result: https://www.youtube.com/watch?v=UdwPkTBcEIk**

### **Backend**

1) Fixed bugs with some endpoints

2) Added endpoints for my recipes page, for favourites and for private recipes

3) Improved recipes endpoints, add additional endpoints such as get_by_tag, get_by_category

4) Deployed backend part (used Yandex Cloud for that)

5) Started working with integration of LLama3 using Ollama

### **Frontend**:

1) Added a filter panel to the home page

2) Connected the backend

3) Added recipe upload processing

4) Added error handling when loading recipes

5) Connected registration and authorization to the backend

## **Challenges & Solutions**

1) connection with frontend (CORS problems) - fixed

2) integration of AI (LLama3 in particular) - for now in progress

3) deployment problems (somehow someone get access to our database, so we need to fix issues with security) - security
fixes are in progress

## **Conclusions & Next Steps**

For the next week our team is planning to:

1) Integrate API for recipes management

2) Implement error handling and UI for stubs

3) Connect to mock web server and implementing UI tests

4) Design pages for the AI recipes import

5) Implements Tag selection and creation

6) Make adjustments in interactive functionalities

7) Fully integrate LLama3

8) Continue to improve existing endpoints and creating needed

9) Fix problems with security of the remote server

10) Write unit tests for backend (at least for some endpoints)