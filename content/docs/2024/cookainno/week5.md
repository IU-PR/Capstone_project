---
title: "Week #5"
---

# Week 5 Report: Feedback and Surveys - 2nd Iteration

At the beginning of the fifth week, we studied the results of the survey and people's wishes for improving our application. Based on this, we created a work plan for the week and successfully completed it. We added several features and made design changes to enhance the CookAInno app. 

Week 5 marked a crucial phase of iteration and refinement based on user feedback. This week, our primary focus was on gathering comprehensive feedback from our users to ensure the continuous improvement of the CookAInno app. By engaging with our users and stakeholders, we aimed to validate our development direction and refine our application to better meet user needs.

## Feedback and Surveys

In Week 5, we continued to improve the CookAInno app by meeting with our users again. We showed them the new features and updated interface. Just like last week, we conducted another survey, this time with new questions and the latest app design. This helped us see how satisfied our users are and whether we are heading in the right direction.

We shared the updated app with our testers and gathered their feedback through a revised questionnaire. This process helped us better understand user preferences and made our users feel involved in developing the product. We encouraged them to share their ideas for improving and adding new features to the app.

By involving our users this way, we aim to create a collaborative development process where continuous feedback leads to meaningful improvements. This ongoing engagement is key to building an app that meets the needs and expectations of our users, making CookAInno a user-friendly solution.

![w5f1](/2024/cookainno/w5f1.png)

## Analysis of the Feedback

Our analysis of the feedback revealed several key insights. 


![w5f2](/2024/cookainno/w5f2.png)
- Most respondents indicated that they often discard unused food items, highlighting the relevance of our project. CookAInno aims to address this issue by helping users utilize their fridge contents more effectively, thereby reducing food waste.


![w5f3](/2024/cookainno/w5f3.png)
- Additionally, many respondents expressed interest in a feature for calculating meal calories from a photo, confirming its potential usefulness. 


![w5f4](/2024/cookainno/w5f4.png)
- Users also showed enthusiasm for features like weekly menu planning, which we plan to incorporate based on this feedback.


![w5f5](/2024/cookainno/w5f5.png)
- The survey results also indicated that the respondents had previously disliked the design, prompting us to make changes. This week, the updated design received positive feedback, with users appreciating the new look and color palette. 


![w5f6](/2024/cookainno/w5f6.png)
- Furthermore, respondents indicated that they found the current color scheme appealing, so we decided to maintain it.

![w5f7](/2024/cookainno/w5f7.png)
- The survey revealed that not only did respondents find the app useful, but they were also willing to recommend it to their friends. This positive reception underscores the potential impact of CookAInno.

From the feedback, we also gathered suggestions for new features, such as sharing recipes with friends, providing nutritional information, direct calorie calculations within the app, and offering filtering options to accommodate personal dietary preferences, like vegetarian meal plans. Also users wanted a feature of creating a shop list with recommended ingredients.

## Prioritizing Feedback and Future Plans

By conducting and analysing the useful feedback from the stakeholders we can prioritise some of the features, which can be added or improved in our product. Design has already been improved and positively resulted in user’s opinion. The project roadmap below will outline our future plan of work, considering the full current list of the potential changes.

## Project Roadmap

As of 07.07.2024, we have successfully implemented several key features of the CookAInno app, including recipe generation by ingredients, recipe recommendations based on user preferences, basic ingredients recognition by photo, calorie recommendations, and daily advice. Our roadmap for the remainder of 2024 includes the following milestones:

- **August-September 2024**:
  - Enable ingredient-based filtering to show recipes that can be made with available ingredients in the save recipe database without AI generation.
  - AI Food Recognition: Continue refining image recognition accuracy.

- **October 2024**:
  - Develop dietary filters for specific diets (vegan, vegetarian, halal, lactose-free).
  - Introduce daily menu suggestions based on user calorie needs and preferences.

- **November 2024**:
  - Refine daily menu suggestions using user feedback and advanced recommendation algorithms.
  - Develop a feature to calculate meal calories based on ingredients and portions used.

- **December 2024**:
  - Develop a shopping list feature that automatically generates lists based on selected recipes.
  - Conduct thorough user testing and gather feedback on UI/UX design for further improvements.

- **January 2025**:
  - Nutritional Insights: Introduce a feature that provides detailed nutritional information for each recipe, including macronutrient breakdown (proteins, fats, carbohydrates) and essential vitamins and minerals. This will further support users in making informed dietary choices.

We remain committed to regularly assessing our progress, comparing it against our initial goals, and making necessary adjustments to enhance our application's design, features, and functionalities. By fostering collaboration and maintaining a focus on user needs, we aim to deliver a product that not only meets but exceeds expectations, creating a comprehensive food ecosystem for our users.

## Iteration and Refinement

### Mobile Achievements:
- Implemented ingredient recognition allowing users to take photos of ingredients for identification.
- [Demo Link](https://youtube.com/shorts/AZvl9N-y3oA?feature=share)
- Profile: Implemented generation of daily advice with use of machine learning. Implemented editable profile parameters. Users can update their weight and height.v

![w5f8](/2024/cookainno/w5f8.png)

- Registration: Implemented pages for user characteristics during registration for calorie calculation.

![w5f9](/2024/cookainno/w5f9.png)

### Changes Based on Feedback:
- Based on user feedback, we added implementation of search functionality. Users can quickly find recipes on the main and favorite pages.

![w5f10](/2024/cookainno/w5f10.png)

- Refined UI based on user suggestions, resulting in a more appealing color scheme.

![w5f11](/2024/cookainno/w5f11.png)

### ML – Ingredient Recognition:
- The ingredient images dataset was updated and finalized, extending the initial list of ingredients that the model can recognize. Using a base dataset [link](https://universe.roboflow.com/jonas-hiltl-vuqw9/test-zlrwd/health) and incorporating data from 3 additional datasets (links to [1](https://universe.roboflow.com/ida-bagus-indrabudhi-kusuma-rm4ud/retail-product-kak-felix), [2](https://universe.roboflow.com/coretus/food-item-detection-fggyf), and [3](https://universe.roboflow.com/fridgeapp/whatsinyourfridge-1cbaa/health)), I aimed to create a comprehensive dataset with the most commonly used cooking ingredients.
[The final dataset](https://universe.roboflow.com/groceryitemsdetection/ingredients_images_for_detection) contains 9982 images across 42 classes, including the following ingredients:
  - Vegetables: tomato, potato, carrot, onion, bell pepper, corn, cucumber, green beans, red beans, white beans, spinach, eggplant, broccoli, peas, garlic, lettuce.
  - Fruits: apple, avocado, lemon, lime, banana, strawberries, orange, nectarine, kiwi, mango, blueberries, pomegranate.
  - Dairy products: milk, egg (separately), eggs (in a package), cheese, yogurt, butter.
  - Protein: chicken, meat, shrimp.
  - Other: bread, oil, pasta, flour, champignons.
  - Each class has an average of 200-400 images and over 200 annotations.
- YOLOv8 model was retrained on the updated dataset and evaluated its performance. The metrics indicate good overall performance, but with room for improvement in specific classes such as cucumber, carrot, peas, and eggs, which have lower mAP50-95 scores (<0.5). There are metrics on validation set:

| Class          | Images | Instances | Box(P) | R    | mAP50 | mAP50-95 |
|----------------|--------|-----------|--------|------|-------|----------|
| all            | 432    | 1292      | 0.825  | 0.764| 0.833 | 0.669    |
| apple          | 10     | 42        | 0.936  | 0.714| 0.872 | 0.655    |
| avocado        | 17     | 43        | 0.645  | 0.860| 0.849 | 0.692    |
| banana         | 19     | 23        | 0.992  | 0.957| 0.977 | 0.753    |
| bell pepper    | 14     | 30        | 0.868  | 0.800| 0.918 | 0.764    |
| blueberries    | 10     | 42        | 0.795  | 1.000| 0.955 | 0.696    |
| bread          | 10     | 15        | 0.933  | 0.733| 0.826 | 0.619    |
| broccoli       | 14     | 42        | 0.780  | 0.675| 0.785 | 0.546    |
| butter         | 10     | 18        | 0.764  | 0.667| 0.753 | 0.702    |
| carrot         | 14     | 55        | 0.734  | 0.655| 0.691 | 0.369    |
| champignons    | 12     | 12        | 0.978  | 1.000| 0.995 | 0.767    |
| cheese         | 23     | 25        | 0.871  | 0.810| 0.886 | 0.819    |
| chicken        | 17     | 35        | 0.711  | 0.714| 0.770 | 0.587    |
| corn           | 28     | 29        | 0.799  | 0.724| 0.829 | 0.780    |
| cucumber       | 13     | 54        | 0.827  | 0.353| 0.567 | 0.399    |
| egg            | 8      | 38        | 0.893  | 0.921| 0.943 | 0.775    |
| eggplant       | 10     | 23        | 0.880  | 0.640| 0.702 | 0.571    |
| eggs           | 23     | 52        | 0.866  | 0.423| 0.468 | 0.448    |
| flour          | 5      | 42        | 0.792  | 0.714| 0.748 | 0.468    |
| garlic         | 4      | 23        | 0.717  | 0.739| 0.793 | 0.667    |
| green beans    | 38     | 38        | 0.901  | 0.959| 0.961 | 0.894    |
| kiwi           | 2      | 9         | 0.641  | 1.000| 0.791 | 0.613    |
| lemon          | 4      | 11        | 0.836  | 0.909| 0.973 | 0.850    |
| lettuce        | 22     | 27        | 0.938  | 0.852| 0.933 | 0.824    |
| lime           | 5      | 20        | 0.772  | 0.845| 0.817 | 0.473    |
| meat           | 15     | 22        | 0.860  | 0.561| 0.868 | 0.634    |
| milk           | 14     | 18        | 0.890  | 0.833| 0.903 | 0.758    |
| nectarine      | 3      | 55        | 0.750  | 0.928| 0.926 | 0.840    |
| oil            | 10     | 16        | 0.852  | 0.625| 0.701 | 0.647    |
| onion          | 17     | 77        | 0.871  | 0.818| 0.942 | 0.681    |
| orange         | 3      | 12        | 0.982  | 0.833| 0.922 | 0.618    |
| pasta          | 16     | 21        | 0.577  | 0.571| 0.717 | 0.616    |
| peas           | 9      | 24        | 0.756  | 0.500| 0.685 | 0.406    |
| pomegranate    | 1      | 3         | 0.529  | 1.000| 0.863 | 0.771    |
| potato         | 9      | 31        | 0.954  | 0.669| 0.892 | 0.600    |
| red beans      | 7      | 7         | 0.788  | 0.857| 0.869 | 0.869    |
| shrimp         | 20     | 21        | 0.839  | 0.714| 0.772 | 0.578    |
| spinach        | 39     | 39        | 0.939  | 0.793| 0.925 | 0.777    |
| strawberries   | 24     | 24        | 0.934  | 0.875| 0.910 | 0.809    |
| tomato         | 26     | 147       | 0.919  | 0.843| 0.904 | 0.664    |
| white beans    | 8      | 9         | 0.767  | 0.556| 0.784 | 0.767    |
| yogurt         | 10     | 18        | 0.769  | 0.667| 0.771 | 0.664    |

- Compared the performance of the lightweight multimodal model PaliGemma and YOLOv8 trained on the custom dataset.    

  - For this purpose 2 images was chosen:
    Image containing milk, bananas, eggs, bread, and tomatoes.

    ![w5f13](/2024/cookainno/w5f13.png)
    Yolov8m trained on custom dataset answer:
    ['milk', 'tomato', 'banana', 'bread', 'egg']
    
    PaliGemma answer:
    milk, eggs, tomatoes, bananas

  - More complex and realistic example — a photo of a fridge.
    ![w5f14](/2024/cookainno/w5f14.png)

    Yolov8m trained on custom dataset answer:
    ['lime', 'banana', 'green beans', 'onion', 'flour', 'carrot', 'milk', 'meat', 'tomato']

    PaliGemma answer:
    Vegetable

**Comparing outcomes:** YOLOv8 demonstrated superior accuracy and specificity compared to PaliGemma. It could accurately identify and list multiple items in both simple and complex images, whereas PaliGemma tended to generalize and failed to identify specific items accurately. Thus, the choice of a model is obvious. YOLOv8 is more appropriate model for ingredients detection task.

### Challenges and Solutions:
- Our team faced a difficulty in presenting a picture based on the name of the generated dish recipe. We didn't understand exactly how to implement this.
  - We've gone through several image generation APIs. Some do not have access, and some are allowed to work only at night. And we decided to implement image parsing by its name. This approach turned out to be the most successful, convenient and workable.
- Our team decided to change the design due to people's feedback. And at the meeting at the beginning of the week, we faced disagreements from different team members in choosing the design.
  - We discussed it for a long time and decided on a pastel blue color and several shades of gray.

Here is the new Figma design: 
https://www.figma.com/design/vpqc9bsK1bBngEr7yXHRUP/Untitled?node-id=0-1&t=5dARqG7DerDkbgEc-0

**ML – Ingredient recognition:**
- Initially planned to use a specific dataset ([link](https://universe.roboflow.com/muhammadmoin-y1qrz/retail-store-axhqk)), but found a better alternative ([link](https://universe.roboflow.com/groceryitemsdetection/ingredients_images_for_detection)) through extensive search. However, this dataset could not be downloaded in one go, requiring incremental cloning of 1000 images at a time.
- Faced limitations on Roboflow free plan, which restricts datasets to a maximum of 10,000 images. This necessitated careful selection to ensure each class had a minimum representative number of images (200 images).

**Backend:**
- Android developers found a bug limiting the number of chars in recipe description (255 -> 10000). We are going to exceed these limitations. Characters are not so heavy data so we can store longer recipes.

### Next Steps:

**Android**: 
- Associate each generated receipt with the corresponding food picture. The food picture now is requested with the use of BeautifulSoup, but not yet integrated into the application.
- Analyse memory and traffic metrics, improve performance.

**Backend**:
- Implement the deployment of the fully implemented backend part on the remote server including Java and Python APIs.
- Enlarge limits for the recipe storage in the database.

**ML**: 
- Focus on improving the model’s performance by experimenting with different sizes of the YOLO model (e.g., medium and large) and tuning training hyperparameters for optimal results.
- Perform testing on manually collected real images of the fridge.

## Conclusion

Week 5 has been pivotal in refining CookAInno based on user feedback. By involving users in the development process, we have been able to make significant improvements and plan for future enhancements. Our ongoing commitment to user-centric development ensures that CookAInno will continue to evolve into a comprehensive and user-friendly food ecosystem.
