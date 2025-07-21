# Practicum Project Summer 2025 Report 3  
**Team mealix**  

---

## 1. Implemented MVP features  

Our LLM agent can generate full user diet:
```json
{
  "meals": [
    {
      "type": "breakfast",
      "dish": "омлет с овощами и зеленью",
      "ingredients": [
        {
          "name": "Яйца",
          "amount": 3,
          "unit": "pcs",
          "product_name": "Яйцо куриное Село Зеленое С1 Деревенское 15шт",
          "article": 1000554424
        },
        {
          "name": "Молоко",
          "amount": 100,
          "unit": "ml",
          "product_name": "Молоко сухое цельное Магнит",
          "article": 1000387141
        },
        {
          "name": "Овощи (например, помидоры, шпинат)",
          "amount": 100,
          "unit": "g",
          "product_name": "Ассорти Кубань продукт огурцы и помидоры маринованные",
          "article": 1000156398
        },
        {
          "name": "Зелень (например, укроп, петрушка)",
          "amount": 20,
          "unit": "g",
          "product_name": "Укроп",
          "article": 3412080023
        },
        {
          "name": "Соль",
          "amount": "по вкусу",
          "unit": "г",
          "product_name": "Фасоль зеленая 4 Сезона быстрозамороженная",
          "article": 9009072909
        },
        {
          "name": "Перец",
          "amount": "по вкусу",
          "unit": "г",
          "product_name": "Приправа Индана Перец красный молотый",
          "article": 1000449670
        }
      ],
      "steps": [
        "Шаг 1: Взбейте яйца с молоком в миске.",
        "Шаг 2: Нарежьте овощи и зелень, добавьте в яично-молочную смесь.",
        "Шаг 3: Посолите и поперчите по вкусу.",
        "Шаг 4: Разогрейте сковороду на среднем огне, смажьте маслом и вылейте смесь.",
        "Шаг 5: Жарьте омлет до золотистой корочки с обеих сторон."
      ]
    },
    {
      "type": "lunch",
      "dish": "куриный суп с лапшой и зеленью",
      "ingredients": [
        {
          "name": "Бульон (куриный)",
          "amount": 1500,
          "unit": "ml",
          "product_name": "Бульон куриный Роллтон Домашний",
          "article": 1000498400
        },
        {
          "name": "Яйцо куриное",
          "amount": 2,
          "unit": "pcs",
          "product_name": "Яйцо куриное Село Зеленое С1 Деревенское 15шт",
          "article": 1000554424
        },
        {
          "name": "Мука пшеничная",
          "amount": 60,
          "unit": "g",
          "product_name": "Мука Пшеничная",
          "article": 1042229921
        },
        {
          "name": "Картофель",
          "amount": 6,
          "unit": "pcs",
          "product_name": "Картофельное пюре Роллтон с сухариками",
          "article": 2199910300
        },
        {
          "name": "Лук репчатый",
          "amount": 1,
          "unit": "pcs",
          "product_name": "Лук репчатый",
          "article": 9072651204
        },
        {
          "name": "Морковь",
          "amount": 1,
          "unit": "pcs",
          "product_name": "Морковь мытая",
          "article": 3412070008
        },
        {
          "name": "Лист лавровый",
          "amount": 1,
          "unit": "pcs",
          "product_name": "Лист лавровый Восточный гость сухой",
          "article": 1000338410
        },
        {
          "name": "Сметана",
          "amount": 100,
          "unit": "g",
          "product_name": "Сметана Очень важная корова 20%",
          "article": 1000278588
        },
        {
          "name": "Петрушка",
          "amount": 1,
          "unit": "bunch",
          "product_name": "Тушка цыпленка-бройлера",
          "article": 5555552001
        },
        {
          "name": "Соль",
          "amount": "по вкусу",
          "unit": "г",
          "product_name": "Фасоль зеленая 4 Сезона быстрозамороженная",
          "article": 9009072909
        }
      ],
      "steps": [
        "Шаг 1: В кипящий куриный бульон добавьте картофель, нарезанный произвольно, варите минут 5.",
        "Шаг 2: Лук мелко нарежьте, морковь натрите на мелкой терке, обжарьте под крышкой на сковородке.",
        "Шаг 3: Яйцо взбейте и разотрите в крошку с мукой.",
        "Шаг 4: Второе яйцо взбейте, добавьте пару ложек кипящей воды из супа, размешайте. Вылейте в кастрюлю, помешивая.",
        "Шаг 5: Добавьте зажарку, лавровый лист и тесто, пару минут хорошо помешайте по дну, чтобы не пристало.",
        "Шаг 6: Солите, перчите по вкусу, варите еще минут 10.",
        "Шаг 7: Добавьте мелко нарезанную зелень и сметану, томите на маленьком огне пару минут."
      ]
    },
    {
      "type": "dinner",
      "dish": "тирамису",
      "ingredients": [
        {
          "name": "Печенье (например, савоярди)",
          "amount": 200,
          "unit": "g",
          "product_name": "Печенье Goute",
          "article": 1000242531
        },
        {
          "name": "Кофе эспрессо",
          "amount": 4,
          "unit": "pcs",
          "product_name": "Сок Сады Придонья яблоко-персик",
          "article": 1000374936
        },
        {
          "name": "Сахар",
          "amount": 50,
          "unit": "g",
          "product_name": "Сахар-песок белый",
          "article": 1670400001
        },
        {
          "name": "Маскарпоне",
          "amount": 500,
          "unit": "g",
          "product_name": "Макароны Makfa Спагетти №16 Группа А",
          "article": 1000425470
        },
        {
          "name": "Сливки (33%)",
          "amount": 300,
          "unit": "ml",
          "product_name": "Сливки Очень важная корова 10% стерилизованные",
          "article": 1896600066
        },
        {
          "name": "Какао-порошок",
          "amount": 20,
          "unit": "g",
          "product_name": "Какао-порошок Золотой ярлык",
          "article": 1000125976
        },
        {
          "name": "Ликер (по желанию)",
          "amount": 20,
          "unit": "ml",
          "product_name": "Лазанья Gusto Di Roma",
          "article": 1000566108
        }
      ],
      "steps": [
        "Шаг 1: Приготовьте крепкий кофе эспрессо.",
        "Шаг 2: Взбейте сливки с маскарпоне до однородной массы.",
        "Шаг 3: Обмакните печенье в кофе, выложите в форму.",
        "Шаг 4: На печенье выложите слой из взбитой массы маскарпоне и сливок.",
        "Шаг 5: Повторите слои до окончания ингредиентов.",
        "Шаг 6: Поставьте в холодильник на несколько часов для пропитки.",
        "Шаг 7: Перед подачей посыпьте какао-порошком."
      ]
    }
  ]
}
```
Also we completed telegram bot and telegram mini app functionality for generation a diet.


### ML  
As part of the project, a hybrid text response generation system was implemented, combining the Yandex API (as a language model) and a custom RAG architecture (Retrieval-Augmented Generation), trained on a specialized recipe database.
First, the first agent generates 3 dishes based on the user's preferences, then the RAG system correlates the actual recipes of these dishes (which we paired) with the recipes of the dishes generated by the first agent. Then all the recipes are sent to the second agent and he compiles the final json file from the recipes. 


## 2. Weekly commitments  

### Individual contribution of each participant:  

**Alexander Kachmazov (ML):**  
Connected the entire system:
1. The gpt agent generates three sample dishes according to your wishes.
2. System RAG adds recipes to each dish if they are in the database. 
3. All this is transferred to the final model, which generates dishes, recipes, and necessary products. 
4. Connects to the Albert's function where it is compared with real dishes.
5. Put it all on fastcap.  
[Link](https://github.com/IU-Capstone-Project-2025/mealix/commit/7aefe11f3d6811cf8efab75448c887bd20d9133d)  

**Samat Iakupov (Frontend):**  
1. Implemented connection with backend to save user profile.
2. Made generation user diet page and connection with backend.
[Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/frontend)  

**Dmitrii Antipov (Backend):**  
1. Wrote the entire backend. Saving data, endpoints for saving the user and generating menus.
[Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/main/backend/src/main/java/ru/backend/endpoint)
2. Completed the bot.
[Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/devops)  
[Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/tg_bot)  
3. Wrote Docker Compose for generation on the server, Dockerfile for the bot and backend.
[Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/backend)  

**Danil Eramasov (ML):**  
1. Wrote documentation of ML part in README.md.  
[Link](https://github.com/IU-Capstone-Project-2025/mealix/blob/llm_agent_code/ml/README.md)  
2. Wrote Dockerfile also in ML part.  
[Link](https://github.com/IU-Capstone-Project-2025/mealix/blob/llm_agent_code/ml/fastapi-app/Dockerfile) 

**Albert Shammasov (Data Analyst):**  
1. Have completed the implementation of the function that I started last week.
2. Fixed the identified problems in the search algorithm.
3. Tested the function, and now it correctly finds products by name.
4. Improved the accuracy of the search. 
5. Increased the variety of some product categories in the dataset. 
[Link](https://github.com/IU-Capstone-Project-2025/mealix/tree/llm_agent_code)  

---

### Plan for Next Week:  

**Frontend:**  


**Backend:**  
We planning to cover the entire functionality of the bot with tests.  

**ML:**  
On next week we want to start developing algorithms to account for BCG and protein targets.  

### Confirmation of the code's operability  
We confirm that the code in the main branch:  
- In working condition.  
- Run via docker-compose (or another alternative described in the README.md)  