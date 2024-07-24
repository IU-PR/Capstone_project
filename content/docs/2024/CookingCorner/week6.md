---
title: "Week #6"
---

# **Week #6**

## **Presentation**:

{{< embed-pdf url="/2024/CookingCorner/CookingCorner_presentation.pdf" >}}

## **Weekly Progress Report**:

### **Design**

1) Changed the design of ingredient panels and their interactions

2) Reworked the interface of add panels

3) Changed the filter icons

4) Added design for cases of empty content panels

5) Added Rating functionality 

6) Added display of additional information about the recipe

7) Implemented functions to add images for recipe steps in manual recipe creation

### **Mobile**

1) Recipe API integration for search, favourites, publish, delete, get by id

2) Global Events refactoring

3) Recipe Editor feature

4) Category API implementation

5) Immutable List Serializer fix

6) Tag API implementation

7) Recipe own status fix

8) Kebab menu items fix

9) Snackbar events collection fix

10) Empty item screens placeholder

11) Rating implementation

### **Backend**

1) Integrated llama3 for importing recipes from the url

2) Fixed bugs with some endpoints

3) Wrote tests for recipes (not for all recipe endpoints for now)

4) Started working with images using yandex s3 bucket

### **Frontend**

1) Added logic for editing recipe

2) Adding steps and ingredients to the recipe creation form

3) Added placeholders for search and home page

4) Search for recipes using search bar in search page

5) Autocomplete form for recipe creation/editing

6) Added the ability to add a review for a recipe

### **Challenges & Solutions**

1) Integration of llama, writing correct prompt for it and parse result data

2) Working with images (using s3 bucket)

### **Conclusions & Next Steps**

1) Generate request + navigation to recipe editor

2) Error stubs

3) Favourites request + integration

4) Image picker

5) Pull-to-refresh

6) Profile editor screen

7) Clean up the details

8) Fix experimental features

9) Finish writing tests

10) Finish working with images

11) Fix bugs and improve endpoints