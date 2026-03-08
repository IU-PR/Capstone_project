# Week #5


## 1. Interviews
### **Interview #1: Anya, 21, student, limited budget**

**Q:** Hi Ann! Tell us, how do you like our website? First impression?

**Ann:** Hi! First of all, I'll say it's very beautiful. The design makes you want to stay and click. Delicate colors, nice animation. Honestly, I didn't expect a service that's supposed to "analyze" to also be aesthetically pleasing. That's a real plus.

**Q:** You uploaded your photo. Were you able to determine your color type?

**Ann:** Yes! Very quickly! At first I thought it would take about 5 minutes, but everything appeared in literally 10 seconds. They wrote to me that I was a "soft spring" and immediately gave me a selection of suitable colors. It's so convenient. I really didn't know that mint and peach suit me. And I wore dark gray and black all the time.

**Q:** How did you feel about it?

**Ann:** At first I doubted it, I thought it was another AI, like fashion filters on Instagram. But when I actually looked at myself in a mint sweater (I found it in my closet), I was stunned. My eyes were brighter, my face was fresher. Even my mom noticed. So... I believed it.

**Q:** Have you tried analyzing your figure?

**Ann:** Yes, I entered my parameters, and it turned out that I have a "pear". The website explained why - my hips are wider than my chest, my waist is defined. And there were clothing tips: emphasize the top, don't wear low-waisted clothes. Very spot on. I often felt that I looked "wrong" in certain things, now I understand why.

**Q:** What would you like to add?

**Ann:** It would be cool to see images with clothes by budget right away. For example: "here are 3 tops from the mass market that will suit your color type and figure." Considering that I'm a student, the price is important to me - up to 2000 rubles, for example. But otherwise - wow.

---

### **Interview #2: Olga, 29, young mother**

**Q:** Olga, thank you for finding the time to test the site with your child. What are your first impressions?

**Olga:** The site is very clean and clear. It's a real salvation when you hold your baby in one hand and want to quickly find out something with the other. No ads, no extra buttons. Everything is to the point. I appreciated that the text is large and the buttons are not small

**Q:** You uploaded a photo for color type analysis. How did the process go?

**Olga:** Yes, I uploaded a regular selfie without makeup. A few seconds later they wrote to me that I am a "cold summer" and showed me what colors suit me. Pastel, powder, blue-gray. I have always been drawn to warm beiges - now I understand why they "muffle" me. I really liked the "avoid" block - specific and useful.

**Q:** And what about the figure analysis?

**Olga:** I entered my current parameters - a lot has changed after giving birth. I got the "rectangle" type, and the site offered advice on how to create a visual "hourglass" silhouette. For example, a belt at the waist, avoid baggy clothes. I tried on an old dress with a belt at home - and indeed, it immediately looks different. It's really cool that they didn't just say "this is your type", but explained what to do with it.

**Q:** Were there any difficulties?

**Olga:** There were a few missing hints when entering parameters — for example, how to measure the chest circumference correctly: at the protruding points or under the chest? Such clarifications would make the process more precise. And I would like the site to remember my data so that I don’t have to enter it every time.

**Q:** What else would I like?

**Olga:** I would add a selection of specific things by body type — for example, “the best dresses for a rectangle under 5,000 rubles.” Or a link to marketplaces. If I could immediately add to the basket — I would buy it. Seriously.

---

### **Interview #3: Kate, 25, is into fashion and loves online shopping**

**Q:** Kate, as a fashionable girl — how interesting is the idea of ​​the site to you?

**Katya:** It’s just a godsend. I'm constantly on Pinterest, looking for what would suit me. But it's all kind of blind. And then you upload a photo — and bam, the AI ​​tells you that you're a "warm autumn" and gives you a palette. It's super. I'd pay for such functionality.

**Q:** What colors were offered to you? Do you agree with the result?

**Katya:** Yes, completely. I've always been drawn to warm, olive, mustard, but I thought — maybe it's just taste. And now I know that it really suits me. I even tried an online store and applied these colors — everything looks harmonious. And before, there was a feeling that the things were good, but I was like "not mine."

**Q:** Did you use the figure analysis functionality?

**Katya:** Of course! I have an "hourglass" type, and the site immediately gave advice: emphasize the waist, do not wear robes. Everything is super logical and beautifully designed. I liked that the tips are accompanied by visuals - as if you were reading a magazine.

**Q:** What could be improved?

**Katya:** I want more interactivity. For example, a 3D model of my figure, where you can "try on" images. Or automatic collages - like Polyvore in the old days. Well, and links to specific brands for my color type and figure. If this works, you'll be a hit.

Q: How do you like the visual style?

Katya: Chic. Very fashionable. Doesn't look like a typical AI site. Everything breathes, beautifully, lightly. And yes, very important - no advertising, thanks for that. Only content, only style. Captivating.
## 2. Performance & Stability
Performance & Stability
To ensure the high performance and stability of our application, we will implement a comprehensive measurement and optimization strategy tailored to each major system component: backend services, machine learning models, and the parser module.

1. Backend & Database Performance
The backend, built with FastAPI and PostgreSQL, currently demonstrates stable performance even under moderate to high load. We will continue to test its behavior under increasing concurrent requests using tools likepytest-benchmark.
Key metrics we will track include:
- Average response time for API endpoints (currently under 150ms per authenticated request)
- Database query latency, which is consistently low due to optimized SQLAlchemy usage and proper indexing
- Error rate, monitored via logs and alerts
To maintain this level of performance, we will implement connection pooling, caching for frequent queries, and container health checks.

2. ML Model Inference Time
Currently, our ML model for color type detection takes an average of 23 seconds to process a user image and return a prediction. While this is acceptable for the current user load, we plan to:
- Further optimize the preprocessing pipeline
- Increase training data and model size over time to improve accuracy, while carefully balancing it with inference time
We expect to gradually reduce latency through technical improvements and infrastructure adjustments.

3. Parser Performance
The outfit suggestion parser currently requires approximately 76 seconds to process and return relevant clothing items based on user preferences. This delay is primarily due to:
- Real-time parsing of external sources
- Ranking and filtering logic for the top results
To improve this, we plan to:
- Introduce asynchronous scraping and caching mechanisms
- Utilize background tasks and job queues for heavy operations
- Preprocess or warm up popular queries to reduce cold-start delays

4. Continuous Monitoring and Stability
Across the entire stack, we will monitor:
- CPU and memory usage
- API response times
- Error logs and request success rates

Summary
While some components like the ML model and parser currently require optimization, they are functional and will be incrementally improved through better model training, architectural refinements, and parallelization. The backend and database already handle load efficiently, and we will continue to test and refine their scalability throughout the next iterations.

## 3. ML Model Refinement
Initially, due to the lack of a dataset with labeled data, my team and I tried to cluster images using the CLIP model **[link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/data.ipynb)** to transform them into embeddings. This did not yield significant results, but allowed us to create an initial markup, which we subsequently corrected. We decided to mark the data manually, adjusting the CLIP results **[link](https://github.com/IU-Capstone-Project-2025/styleU/tree/main/ml/color_type_clip/clustered_by_color_type_manually_cleaned_without_augmentation)** there were about 700 photos, to make the dataset larger, augmentation was applied and it turned out to increase the amount of data by 5 times **[link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/data_augmentation.ipynb)**. Using this data, the CNN model was trained **[link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/cnn.ipynb)**, but it did not give good results. We assumed that this might be related to the idea of ​​CNN: the architecture is aimed at extracting objects from a photo, and our task is to recognize colors.

Based on these findings, a decision was made to take a simpler model and pay more attention to color features in converting photos into data: this did not yield results **[link](https://github.com/IU-Capstone-Project-2025/styleU/blob/a243707784838c6b4baed22784279e0ae19eb442/ml/color_type_clip/random_forest.ipynb)**
To improve accuracy on test data, we assumed that the background in the photo could cause noise, but after testing this hypothesis, it turned out that it did not affect the model's performance **[link](https://github.com/IU-Capstone-Project-2025/styleU/blob/main/ml/color_type_clip/random_forest.ipynb)**

After these searches, we asked for help and received some tips to improve convergence. Among them were options: decreasing dropout, decreasing learning rate, improving the model architecture, working with evaluation methods.
**[link](https://github.com/IU-Capstone-Project-2025/styleU/commit/0221e1627451d675bdfb651806a5b4ca05ad752b)**

None of this gave any results. The main problem was retraining the model, we made a disappointing conclusion that the problem was with the data. We tried removing the background from the photo, removed normalization during preprocessing - since it darkened the images very much, tried offline augmentation and the standard way. But nevertheless, we were unable to come to anything positive.

A series of experiments was also conducted aimed at assessing the influence of the background on the behavior of the image classification model. For this purpose, a Random Forest model trained on 40 images with a background was used, and the importance values ​​of features in images with and without a background were compared using SHAP analysis. The results showed that the background can significantly affect the model's decisions - in some cases, a significant change in SHAP values ​​was observed when removing the background. The model was also interpreted based on color features (RGB, HSV), where it was found that the model is especially sensitive to hue and saturation, while the red channel has virtually no effect on the result.

Additionally, two neural network models were trained: a simple CNN and a retrained ResNet18 using label smoothing and augmentations. The CNN model allowed for a visual analysis of the model's attention using SHAP, but showed limited accuracy. ResNet18 with preliminary training and fine-tuning achieved validation accuracy of up to 64% and test accuracy of about 51%. This confirms that enhanced data preprocessing, background noise removal, and proper model tuning improve its robustness and interpretability.
**[link](https://github.com/IU-Capstone-Project-2025/styleU/commit/beb726e85708b1ebe171164be3d93759105e58bf)**

Having tried pre-trained models - this gave slightly better results (about 60% accuracy) - it was decided to collect and label more data, approaching this with special care.


## 4. Individual contribution of each participant

1) Ksenia Korchagina (lead) - organize interviews, work with deploying, write report & plan tasks

**[fix docker](https://github.com/IU-Capstone-Project-2025/styleU/commit/90bdba2d246ed8171fe38fb2bf560ef8d7f0e81d)**

2) Yasmina Mamadalieva - training a model to determine color type, more detailed info in ML Model Refinement part

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/beb726e85708b1ebe171164be3d93759105e58bf)** - Conducted a shap analysis, balanced the data by adding new ones, and checked the work of pretrained model

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/06816c358ccfc97a39e33dfaa8f0ccfaabb1ae74)** - Solved conflicts in random_forest file


3) Aisylu Fattakhova - connecting LLM, writing the frontend, integrating the backend service with the LLM service, conducting interviews

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/5fe4c8339ac849aac388bce539bc71ecadaa1a84)** - Added user input check in html file;
Added WB items ranking: The first products shown are the products with the best combination of rating and number of reviews.

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/ab7a6e72527edfb7e4221dcb7bcc6242ddd5be05)** - faceid_adapter_run.py - Connected to IP-Adapter-FaceID in HF space;
main.py - added endpont to generate avatar;

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/685c42f8494d73465da39e7e6485316702aa4dba)**

**[commit](https://github.com/IU-Capstone-Project-2025/styleU/commit/f2a06aca1f06c4124972d25805c207218cdeb970)** - switched to UploadFile and in-memory processing for avatar generation;
removed saving files to disk

4) Ekaterina Akimenko - completed the design for the pages that will be included in the MVP, compiled a survey

**[connect with back](https://github.com/IU-Capstone-Project-2025/styleU/commit/5bd9aaf6410d9b5e133f48c0e4ae5f2befa7d9cb)**

**[translate](https://github.com/IU-Capstone-Project-2025/styleU/commit/5bd9aaf6410d9b5e133f48c0e4ae5f2befa7d9cb)**

**[Added shop page, fixed issues with authorizarion](https://github.com/IU-Capstone-Project-2025/styleU/commit/b7db5c8ca2fe1b8e627cd231e838da469e90bd77)**

5) Sofia Goryunova - trained the model for the color type, improved its quality, collect dataset, , more detailed info in ML Model Refinement part

**[cnn model](https://github.com/IU-Capstone-Project-2025/styleU/commit/0221e1627451d675bdfb651806a5b4ca05ad752b)**


6) Alena Starikova - connect back with parser, help girls to connect everything

**[connect backend to parser](https://github.com/IU-Capstone-Project-2025/styleU/commit/03d2ab86913a4cf680332b19b24517d496a78f01)**

7) Rokkel Maria - developed the design, write registration & personal page in frontend

**[add register](https://github.com/IU-Capstone-Project-2025/styleU/commit/a56593449ae2386fbeae78f4285c0b20d14f160d)**

**[to add personal page](https://github.com/IU-Capstone-Project-2025/styleU/commit/8ab4c58c89f4309f769760cbf444ffc8609d575c)**


## 5. Plan for Next Week
[55] Backend for outfit feature (w6)

[56] Save user-created outfits in DB (w6)

[57] Add 3D/2D avatar (w6)

[58] add handlers in back for 3D avatar (w6)

[59] Write 3 feature in front (w6)

[60] Write favorites page & avatar in front  (w6)

[61] Finalize model training (w6)

[62] Finalize parser (w6)

[63] Deploy (w6)

[64] Interact with users (w6)

[Link to kanban board](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/database/f226fd43-ad24-45a2-ac21-8f5c7684f4c6)
