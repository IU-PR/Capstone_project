# Week #3


## 1. Implemented MVP features

### Determining Color Type from a Photo</u>

Description:

The user uploads a photo without filters. The system sends the image to an ML service that analyzes it and returns the user’s color type along with personalized color recommendations.

<u>Tech Stack:</u>

- Frontend: Photo upload interface and result display.

- Backend: Validates and sends the data.

- ML Service: Trained model for color type recognition from images.

- LLM: complement recommendations.

<u>User Flow:</u>

- The user reads the feature description and decides to try it.

- Uploads a photo → clicks “Send.”

- Waits and sees a loading icon.

- The photo is sent to the backend and then to the ML service.

- ML returns the result (color type + recommendations).

- The result is shown to the user.

<u>Outcome:</u>

The user sees their color type, learns which colors suit them, and can use this information when choosing clothes, accessories, or makeup.

### Determining Body Type by Parameters</u>


Description:
The user manually enters body measurements (e.g., bust, waist, hips). An LLM-based service processes the data and determines the body type, returning personalized styling tips.

<u>Tech Stack:</u>

- Frontend: Parameter input form, result display.

- Backend: Validates and sends data to LLM.

- LLM: Analyzes the input and generates the response.

<u>User Flow:</u>

- The user reads the feature description and decides to try it.

- Enters body measurements → clicks “Send.”

- Waits and sees a loading icon.

- Backend validates and sends the data to the LLM.

- LLM returns the body type and style recommendations.

- The result is shown to the user.

<u>Outcome:</u>

The user learns their body type, gets a description and personalized advice on how to dress in a way that suits their shape.

**[user journey(s)](https://drive.google.com/file/d/1CsTmiyxcY6WXu5WApotIpVwZgsV2ObBh/view?usp=share_link)**

## 2. Monetization

We made a plan for monetizing the project: **[monetization plan](https://docs.google.com/document/d/173g375998dgrqL8R7SuuC_CXnJF3rKw6liYgs8c7ZWQ/edit?hl=nl&tab=t.0)**

## 3. Marketing

We analyzed competitors and created a marketing plan: **[analysis](https://docs.google.com/spreadsheets/d/11iMQxC_3RPmFkfHju4t6jE9UjHxVKwigpAY-6AhwK0I/edit?hl=ru&gid=0#gid=0)**

## 3. Plan of developing

Plan: **[developing](https://drive.google.com/file/d/1yrGUk3QLkkxuMQcBVimMRm0i0K6zXeBB/view?usp=share_link)**


## 4. Interaction with startup specialists 

Some team members attended Lyubov Kosvintseva's lecture
and then we prepared a presentation about the project, discussed it with her and received feedback: **[presentation](https://drive.google.com/file/d/1_f2y4QOsi8LPJtHRpK8-9094hp-FSVyu/view?usp=share_link)**

## 5. ML

Initially, due to the lack of a dataset with labeled data, my team and I tried to cluster images using the CLIP model [link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/data.ipynb) to transform them into embeddings. This did not yield significant results, but allowed us to create an initial markup, which we subsequently corrected. We decided to mark the data manually, adjusting the CLIP results [link](https://github.com/IU-Capstone-Project-2025/styleU/tree/main/ml/color_type_clip/clustered_by_color_type_manually_cleaned_without_augmentation) there were about 700 photos, to make the dataset larger, augmentation was applied and it turned out to increase the amount of data by 5 times [link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/data_augmentation.ipynb). Using this data, a CNN model was trained [link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/cnn.ipynb), but it did not give good results because it is aimed at selecting objects from a photo, and the task is to recognize colors. Based on these findings, it was decided to take a simpler model and pay more attention to color features in converting photos into data: this gave a result of 93% accuracy [link](https://github.com/IU-Capstone-Project-2025/styleU/blob/a243707784838c6b4baed22784279e0ae19eb442/ml/color_type_clip/random_forest.ipynb)
To improve the accuracy on test data, we assumed that the background in the photo could cause noise, but after testing this hypothesis, it turned out that this only worsened the model's performance [link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/random_forest.ipynb)


## 5. Internal demo

We will condact internal demo this thursday

## 6. Demonstration of the working MVP

**[demo]()**


## 7. Individual contribution of each participant

1) Ksenia Korchagina (lead) - prepare tasks for next features, writing a report

2) Yasmina Mamadalieva - organize meeting with Lyubov Kosvintseva, work with ml, work on marketing plan

 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/194a7649af93ea14bf835c24efeabf18d4f3e274)** - Cleaned background now for train/test data + added file for define colortype by 1 image


 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/2725427bc0760cfb4dcad8c9970da6a0ebda35dd)** - 	continue of Cleaned background now for train/test data + added file for define colortype by 1 image

**[marketing](https://docs.google.com/spreadsheets/d/11iMQxC_3RPmFkfHju4t6jE9UjHxVKwigpAY-6AhwK0I/edit?hl=ru&gid=0#gid=0)**

3) Aisylu Fattakhova - connecting LLM, solve issues with ollama, connect backend & llm service

 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/c1655017ef6746c000beadfbda815fbeee967c6c)**

 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/9e88453d04f8717a918909059f146b385141bd95)** - Connected to LLM model via Together.ai

 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/55bc7f865d2baeb566d453afbca993513f6a1d1c)** - 	modified:   llm-service/app/main.py

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/40e25936d0eaa1133c213b27a1dc1f3aa59d6c4f)**

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/de4195691c37c83f0b1c13caf5bc5d545caf068e)**

4) Ekaterina Akimenko - almost finished writing front for mvp, analyse marketing 

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/5c2667f6279c2278d83a39b1fa7601d062075e0c)** - FRONT main page

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/292bf9808d9c553ec827290e46676fe538ba57f7)** - fixed main and about pages

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/9d48bbf6f1873aa86a27b46fc9f6da1473af0526)** - fexed home, added body shape page, added login page, made transitions

**[marketing](https://docs.google.com/spreadsheets/d/11iMQxC_3RPmFkfHju4t6jE9UjHxVKwigpAY-6AhwK0I/edit?hl=ru&gid=0#gid=0)**

5) Sofia Goryunova - trained the model for the color type, create monetization plan


 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/a243707784838c6b4baed22784279e0ae19eb442)** - add color type classification functionality and improve model performance

 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/bb19c1a6e2c79533033b1a617eeca35f92a5f79b)** - Update colortype_model.py for returning strings

 **[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/8fd3dab7acf591abaaefc729fc0a8cc2089e1f29)** - fix: remove bug


6) Alena Starikova - finished writing the backend functions for mvp, connect backend & llm service
**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/8f49d9e61650d336c6211596ccc72fd6b37aeeb4)** - connect backend and service for color type prediction

**[developing](https://drive.google.com/file/d/1yrGUk3QLkkxuMQcBVimMRm0i0K6zXeBB/view?usp=share_link)** - developing plan

7) Rokkel Maria - almost finished writing front for mvp, created presentation for Lyubov Kosvintseva

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/83c84c625eca09c7ee3aa6df61687deee8a68d34)** - update home page

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/6a17d65e61b57b0ffe742d85532348899d571e86)** - add color type page

**[presentation](https://drive.google.com/file/d/1_f2y4QOsi8LPJtHRpK8-9094hp-FSVyu/view?usp=share_link)**

## 9. Plan for Next Week
[33]Start development of outfit recommendation by request feature (w4)

[34]Set up basic database schema:User table (w4)

[35]Set up basic database schema:Favorite looks (w4)

[36]Set up basic database schema:User parameters (w4)

[37]Start implementing authentication(w4)

[38] Research web scraping of Wildberries (WB) (w4)

[39] Build a basic scraper (save images, titles, product details) (w4)

[40] Build login/registration screens (w4)

[41] Create initial Favorites screen (placeholder) (w4)

[42] Load and display user parameters (from analysis) (w4)

[43] Begin UI/UX for features 3 and 4 (outfit picker + capsule)

[44] Update MVP screens based on internal feedback (w4)

[Link to kanban board](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/database/f226fd43-ad24-45a2-ac21-8f5c7684f4c6)
