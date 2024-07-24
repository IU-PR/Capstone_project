---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

**Feedback collection plan**

* Create a questionnaire for collecting the feedback

* Ask people who can help personnaly

**Conducted user surveys or feedback sessions**

Our team members have sent a questionnaire to our course chat and asked several friends in real life to check the design and performance of the current state of the application


**Analyzing feedback, identifying and prioritizing issues**

Results of the questionnaire:

![](/2024/CookingCorner/q1.png)

![](/2024/CookingCorner/q2.png)

![](/2024/CookingCorner/q3.png)

![](/2024/CookingCorner/q4.png)

![](/2024/CookingCorner/q5.png)

![](/2024/CookingCorner/q6.png)

![](/2024/CookingCorner/q7.png)

![](/2024/CookingCorner/q8.png)

Overall users were satisfacted by the model of the app, hovewer, we had some feedback that granted our team several useful ideas for application performance improvement:

* Creation of notifications about every next step to accomplish during the cooking process

* Segregation of the favorite recipes into another app activity "favorites"

## **Roadmap**:

The roadmap for several month after creating MVP implies development of next features:

1) Notification system - user will be able to receive notifications about when to start/finish each step in the preparation of the recipe

2) Advanced recipe search - search not only by name/category, but additionally by some words in description, maybe search with correction of mistakes user make while he/she writes something using their keyboard

3) Recommendation system - this system will show user recipes based on their recent searches and their own created recipes

4) System of comments under a recipe - will allow not only rate a recipe, but communicate with other users to know some specific information about recipe and how to cook it

5) AI generation recipes preview image by its name - sometimes users are lazy to search or make a photo of some recipe, so AI can generate image based on the name of the recipe

## **Weekly Progress Report**:

### **Design**

1) Added panes related to AI recipes import functions

2) Added functions to user account, edit and log out

3) Made adjustments in ingredients list of recipe panel

4) Created snackbar templates for future use in case of tokens missing

### **Mobile**

1) Auth API review + implementation + integration

2) Global Event Repository implementation (logout, snackbar and error handling) + Token Interactor implementation

3) Insecure connection fix

4) Recipe kebab menu implementation

5) Import screen implementation

6) Shadow and ripple effects improves

7) Detailed recipe UI updates

8) Recipe API + Recipe Repository + DI module

9) Integration of Recipe Repository to Home & Search components

### **Backend**

1) Fixed bugs with endpoints

2) Corrected responses for get-recipe endpoints (all of them)

3) Fixed issues with security on the server

4) Started working with uploading/downloading images

5) Continued working with Llama3

6) Started writing unit tests

### **Frontend**

1) Added logic for profile edit

2) Added page for upload a recipe from url

3) Added skeleton loading for all the pages

4) Displaying recent recipes

5)  Displaying best rated recipes

6) Adding new recipe using recipe form

7) Add logic for publishing recipe (if it is private)

### **Challenges & Solutions**

During this week we got some troubles with connection backend endpoints and frontend requests. Problem was solved after a discussion between developers.

### **Conclusions & Next Steps**

1) Finish Implementing tag creation and selection

2) Implement functions to add images for recipe steps in manual recipe creation

3) Add filtering functionality for buttons

4) Create recipe / edit recipe screen implementation

5) Continue to review & integrate APIs

6) Add logic for deleting  recipe (if the user is a recipe author)

7) Add logic for editing recipe (if the user is a recipe author)

8) Fix bug with button in home page(Add to your recipes)

9) Fix bug when click on button in recipe card it redirect to recipe page

10) Search using search bar in search page

11) Integrate images to endpoints with recipe and user

12) Get some progress with LLama3

13) Continue fixing bugs and improve backend overall

14) Continue writing tests