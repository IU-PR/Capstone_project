# **Week №3 Report: Outfit Predict**

### **Implemented MVP features**

1. Possibility to upload images of your clothes from the wardrobe.  
- [Backend commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/5a0347da914714069cbd99a0dba23539f12eefa6)   
- [Frontend commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/bdd27021c52d4a241164836bdff18f99c1888af5)  
2. Possibility to view uploaded images from your wardrobe  
- [Backend commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/5a0347da914714069cbd99a0dba23539f12eefa6)  
- [Frontend commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/bdd27021c52d4a241164836bdff18f99c1888af5)   
3. Possibility to get best outfits based on your wardrobe (Core Idea of this project)  
- [Searching algorithm v1](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/41f94c1e7435b8f76e12144258f2e5432091eacf)   
- [Searching algorithm v2](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/45b676fff0f80c960f91e44c242bd6fbefd5f35d) (Suggestions from your wardrobe and more optimized)  
- [Frontend commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/f360e7b94b51e75438f18abbb4806d96ad708c3b)

**Summary**: The MVP currently contains the core functionality of our project: finding best outfits with items from your wardrobes. For future improvements, we will improve the user interface, try different models (for detection and embeddings), add more features (such as finding outfits based on filters). 

### **Demonstration of the working MVP**

- [Link](https://drive.google.com/file/d/1oAxaei80WDixYazBjbu_-Fr6KKBtj1R-/view?usp=sharing)

### **ML**

- [Link to the training code](https://github.com/IU-Capstone-Project-2025/Outfit_predict/blob/main/notebooks/basic_model_training.ipynb)  
- [Links to the initial model artifacts](https://github.com/IU-Capstone-Project-2025/Outfit_predict/blob/main/backend/app/ml/best.pt)   
- **Training the model:** We firstly downloaded a dataset from kaggle called \- ‘Colorful-Fashion-Dataset’ which consists of \~6000 images with bounding boxes on each clothing item. Then we formatted this dataset according to the Ultralytics dataset format. After that, we fine tuned the already pre-trained YOLO v11 model on this dataset. Our model uses default hyperparameters for making predictions, as their balance perfectly between precision and recall. Our model needs only the image as parameter to make predictions of bounding boxes for clothing items. 

### **Internal Demo**

- From the demo we have identified that we need to improve the visual part of our project. We plan to make it black-and-white and adapt to the current fashion store's style.  
- We also noticed the need for developing authentication for the user, as different users have different wardrobes.  
- In the demonstration our model suggested wearing 'Sunflower’ as a part of the outfit. We found out the reason for the bag: The embeddings model which we used \- ‘CLIP’ \- have very low performance on differentiating images. Therefore, the embeddings produced by this model could not efficiently describe the images. The similarity score on which we perform suggestions ranking are directly computed from embeddings, and therefore, the embedder model directly influences our performance.  We already point out better solutions \- such as ‘Dino V2’ and 'Fashion Clip’, which has much better performance. We plan to incorporate these models next week.

### **Weekly commitments**

**Individual contribution of each participant**

- Bulat Sharipov: Defined which tasks to complete this week. Distributed the tasks for team members. Provided notes from internal demonstration and identified future steps. Wrote the report, updated README and added a logo. [Link to commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/4a6d876201728b7764642315ae40c7110bc49cc6)  
- Artyom Grishin: Synthesized feedback from this week customer development(MVP), provided hypotheses for the next features in our project ([Link](https://www.notion.so/Analyzing-custdev-of-MVP-21da795c445f8081ae50e1577d7fa0a0?source=copy_link)). Provided hypotheses for features based on product analogues ([Link](https://www.notion.so/Features-for-Product-Features-Based-on-Competitor-Analysis-216a795c445f80b990aff24b8f6be650?source=copy_link)).  
- Victor Mazanov: Refined questions for customer development process. Conducted this week customer development. [Link](https://www.notion.so/CustDev-for-Week-3-21d5a218c5d5807da8a2d1e3306cf45c?source=copy_link)  
- Dinar Yakupov: Created design-prototypes for pages of user's wardrobe, outfit predictions, updated the main page. Developed the frontend application for aforementioned pages. [Link to commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/709b40b8ff03b3004a501b4e71897d6ec3f7a235)   
- Remal Gareev: Update backend, added migrations, deployed the project. [Link to commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/8cb88b1005fb1f1170586f30dfd1a2804a8ca575)  
- Danil Fathutdinov: Uploaded training scripts, updated the search algorithm. [Link to commit](https://github.com/IU-Capstone-Project-2025/Outfit_predict/commit/b3dfd93ad138b472c2984d8c70190535fb62d3f3)

**Plan for the next week**

- Incorporating new models for creating embeddings. Evaluating the models against similar images and different images, so that similar clothes are close, and non-clothes images are far away from clothes images.  
- Creating authorization: developing frontend page and backend endpoints.   
- Updating the backend so that it is possible to delete images from databases. (Currently we can only add and edit).  
- Updating frontend for printing the errors that could be produced by backend.  
- Developing possibility to choose only a subset of clothes from the wardrobe to make outfit predictions.  
- Possibility to filter outfit searches by gender (i.e. showing clothes for girls only).  
- Possibility to filter outfit based on styles (i.e. casual, official).  
- Possibility to filter outfit based on dominated color on the outfit (i.e. yellow outfits).  
- Possibility to download outfit images.  
- Customer development.

## Confirmation of the code’s operability [\#](https://capstone.innopolis.university/docs/2025/exampleproject/week3/#confirmation-of-the-codes-operability)

We confirm that the code in the main branch:

- [x] ~~In working condition.~~  
- [x] ~~Run via docker-compose (or another alternative described in the `README.md`).~~