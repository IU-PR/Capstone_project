---
title: "Week #5"
---

# **Week #5**

Due to us having a product, specialized for a well defined group of clients (Leroy Merlin website and their users), we cannot rely on the feedback from fellow students or any public survey options.

## **Meetings**
There were scheduled meetings with different people from Leroy Merlin - with product manager, team leader and head of data direction of Leroy Merlin + with 1 expert from Yandex Cloud.


## **Feedback collection plan**
The plan was as follows:
 1. Are you generally satisfied with the quality of the product? Is it sufficient to be usable? Does the MVP fit your requirements?
 2. What do you like about the product?
 3. What do you dislike about the product?
 4. What improvements would you like to see in the next 2 weeks, and in the next six months?

Algorithmic is not suitable as our product is not for open source.

## **Feedback**

Feedback in English is translated from Russian using DeepL translator, originals provided.

{{<details "Product owner feedback" >}}

{{<details "Ru" >}}

1. Да, я даже больше скажу, вы превзошли ожидания.
2. UI/UX — он красивый и удобный. Быстрая генерация — вы выбрали хороший баланс между качеством и ресурсозатратностью.
3. Страница с сохраненными картинками не самая удобная.
4. Улучшения сохранений, чтобы там были промпты — ближайшие 2 недели. На полгода — в целом улучшение качества генерации + побольше интерактива — например, то, что вы предлагали, с канвасом*

*имелась в виду идея давать пользователю выбирать место объекта на картинке.

{{</details>}}

{{<details "En" >}}

1. Yes, I'll even say more, you've exceeded expectations.
2. UI/UX - it's beautiful and user-friendly. Fast generation - you've chosen a good balance between quality and resource efficiency.
3. The page with saved images is not the most user friendly.
4. Improvements to saves to have prompts there - next 2 weeks. For half a year - generally improving the quality of generation + more interactivity - for example, what you suggested, with canvas*
   
*referring to the idea of letting the user choose the location of the object in the picture.

{{</details>}}

{{</details>}}

{{<details "Teamlead feedback" >}}

{{<details "Ru" >}}
1. В целом да. Для использования чуть-чуть не хватает доделать, но для MVP результат очень хороший.
2. Генерация довольно быстрая, хорошие промпты предлагаются.
3. Нет распараллеливания на юзеров, только очередь. Достаточно артефактов.
4. Докеризация и деплой MVP — ближайшие 2 недели. А параллелизм и исправление артефактов — это больше долгосрочные задачи — то есть, скажем, на полгода. Для исправления артефактов идея с автоматическим определением наиболее подходящего местоположения мне нравится.
{{</details>}}

{{<details "En" >}}
1. Overall yes. A little bit lacking for usage, but for MVP the result is very good.
2. Generation is quite fast, good prompts are offered.
3. No parallelization to users, just a queue. Enough artifacts.
4. MVP dockerization and deploy - next 2 weeks. And parallelism and fixing artifacts - these are more long-term tasks - that is, say, for half a year. For artifact fixing, I like the idea of automatic detection of the most appropriate location.
{{</details>}}


{{</details>}}

{{<details "Executive feedback" >}}

{{<details "Ru" >}}
1. Качество продукта для MVP удовлетворительное, для конечного использования нет, тк есть артефакты, недоделан UI.  
2. Идея хорошая, результат лучше существующих открытых решений. UI понравился.
3. Артефакты, иногда совсем странные картинки.  
4. Исправление страницы с сохранением картинок, деплой — 2 недели. Для полгода надо смотреть пожелания бизнеса, но с моей стороны — работа над артефактами должен быть приоритетом. Нужно что-то придумать, чтобы максимально уменьшить их количество.
{{</details>}}

{{<details "En" >}}
1. Product quality is satisfactory for MVP, but not for end use, because there are artifacts and incomplete UI.  
2. The idea is good, the result is better than existing open source solutions. UI is good.
3. Artifacts, sometimes very strange images.  
4. Fixing the page with saving images, deploy - 2 weeks. For half a year we should look at the wishes of the business, but from my side - work on artifacts should be a priority. We need to think of something to minimize their number as much as possible.
{{</details>}}

{{</details>}}


{{<details "Yandex Cloud expert feedback" >}}

{{<details "Ru" >}}
1. Качество продукта как минимум сильно превзошло других участников хакатона, несмотря на то, что у них явно было больше опыта (ребята уже мидлы в больших компаниях, бакалавриат закончили) Думаю, продукт можно использовать, но есть куда расти. Для MVP, конечно, это сильно.
2. Классный UI, хорошее качество картинок в сравнении с конкурентами. Очень удивило то, как вы работаете с YandexGPT, что он выдает хорошие промпты на английском. Как один из разработчиков Яндекс GPT я удивлен.
3. Особо нет претензий. Может быть можно сделать качество лучше и генерацию быстрее, так как 50 секунд на 3060 Ti — не очень быстро.
4. Я не из Леруа, так что вопрос не совсем ко мне. Но мой взгляд — за 2 недели это деплой, за полгода — работа над качеством, скоростью, распараллеливанием, работа с кластером GPU
{{</details>}}

{{<details "En" >}}
1. The quality of the product at least strongly surpassed the other participants of the hackathon, despite the fact that they clearly had more experience (the guys are already middles in big companies, bachelor's degree finished) I think the product can be used, but there is room to grow. For an MVP, of course, it's strong.
2. Cool UI, good picture quality compared to competitors. Very surprised how you work with YandexGPT, that it gives good prompts in English. As one of the developers of YandexGPT I am surprised.
3. No particular complaints. Maybe you can make the quality better and generation faster, as 50 seconds on a 3060 Ti is not very fast.
4. I'm not from Leroy, so the question is not really for me. But my view is: in 2 weeks - deploy, in half a year - work on quality, speed, parallelization, work with GPU cluster
{{</details>}}

{{</details>}}
  
### **Improvements based on the received feedback**

See [**Conclusions & Next Steps**](/docs/2024/scenegenai/week5/#conclusions--next-steps)

## **Weekly progress report:**
Seeing as the project is now being finalized and prepared for deployment, our main goals for this week were to fix problems outlined in the last report and consider other resources for potentially making our UI look better and user-friendly.

### **Improvements in the design**

{{<details "Previous design" >}}
![UI1](/2024/SceneGenAI/OldDesign/UI_1.jpg)
![UI2](/2024/SceneGenAI/OldDesign/UI_2.jpg)
{{</details>}}

{{<details "Current main page" >}}
**Light mode**
![MainLight](/2024/SceneGenAI/NewDesign/main_light.jpg)


**Dark mode**
![MainDark](/2024/SceneGenAI/NewDesign/main_dark.jpg)
{{</details>}}

{{<details "Generation history view" >}}
![history1](/2024/SceneGenAI/NewDesign/UI_1.jpg)
![history2](/2024/SceneGenAI/NewDesign/UI_2.jpg)
![history3](/2024/SceneGenAI/NewDesign/UI_3.jpg)
![history4](/2024/SceneGenAI/NewDesign/UI_4.jpg)
{{</details>}}

{{<details "Image generation process" >}}
![generate1](/2024/SceneGenAI/NewDesign/generate_1.jpg)
![generate2](/2024/SceneGenAI/NewDesign/generate_2.jpg)
![generate3](/2024/SceneGenAI/NewDesign/generate_3.jpg)
![generate4](/2024/SceneGenAI/NewDesign/generate_4.jpg)
![generate5](/2024/SceneGenAI/NewDesign/generate_5.jpg)
{{</details>}}

{{<details "Registration process" >}}
![create1](/2024/SceneGenAI/NewDesign/create_account_1.jpg)
![login](/2024/SceneGenAI/NewDesign/login.jpg)
Trying to create an existing account
![create2](/2024/SceneGenAI/NewDesign/create_account_2.jpg)
{{</details>}}

### **Challenges, issues and solutions**

- **Little bugs and unpredictable behaviours**:  
  As the project grows bigger, the number of mistakes grows too. As an example, an hour of our teams time was wasted on a bug that caused the translation model to translate to the same language as the original message.  
  **Solution**: Debugging and cooperation between team members.

- **Security issues**:  
  Part of our code uses private keys to access Yandex's API, which cannot be shared publicly.  
  **Solution**: Store the API keys separatly in a file, that has to be added to the .gitignore or add the keys to the Python virtual environment and add access them from venv.

- **Docker and CUDA interaction**:  
  Using docker in the project comes with its own issues, namely the issue where docker doesn't recognize CUDA, required for launching models using GPU resources. This problem has been around since last week and caused us to postpone the deployment of our project.  
  **Solution**: Endless googling of problems, trying different methods, consulting with our TA on capstone. The final solution only consists in downloading some specific versions of drivers, docker images and packages + proper configuration of CUDA toolkit on Ubuntu

### **Conclusions & Next Steps**

Based on the received feedback, our main goal for future weeks is dockerisation, deployment and fixing the save page. In the long run, we can add other improvements, such as:
- autodetection of size and coordinates, possibility to select it manually
- transition to SD XL, Sanity Check, selection of the best by Sanity Check with the help of batches generation, parallelization into clusters.