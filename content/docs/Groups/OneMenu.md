---
weight: 1
bookFlatSection: true
title: "One Menu"
---

# **Week #1**

# **Introduction**

{{< hint danger >}}

**Feedback**  
Write concise and well-written project description here. To enhance it further, we recommend incorporating additional details that provide an overview of your project. Consider including elements such as a project logo, a link to your project's webpage, or any other relevant visual materials that can help showcase your work effectively.  
As we plan to promote your work, it's crucial to ensure that this file serves as a compelling introduction that captures the attention of the potential reader. 
{{< /hint >}}

## **Team Members**


| Team Member      | Telegram ID                         | Email Address                       |
|------------------|-------------------------------------|-------------------------------------|
| Timofey Sedov    | [moflotas](https://t.me/moflotas)   | <t.sedov@innopolis.university>      |
| Nikita Bogdankov | [nikibog](https://t.me/nikibog)     | <n.bogdankov@innopolis.university>  |
| Grigorii Fil     | [Fil126](https://t.me/Fil126)       | <g.fil@innopolis.university>        |
| Pavel Nestiurkin | [whoevertf](https://t.me/whoevertf) | <p.nestiurkin@innopolis.university> |


## **Value Proposition**

> Identify the Problem:

First pain point is a big amount of different websites, apps, and telegram chats for different restaurants. Our goal is to reduce their number to a unified powerful solution for better user experience. Second one is that almost none of the eating establishments have a loyalty system. Another problem we discovered is that no one  uses statistics to improve their efficiency. Lastly, clients experience discomfort, since they don’t have personalized recommendations while they are choosing what to order and where to order from. 

> Solution Description:

We propose a solution, where clients can view a list of different restaurants in one app. It makes the choice of the eateries easier. Also it reduces the number of applications used by a client.

Personalization for the client is also one of the ways to solve the problem. Our chat-bot will advise users what to order, because most times it’s hard to choose.

One app for a booking system, and an online menu is convenient. Integrated chat-bot will advise the establishment how to improve their business model based on the gathered statistics. Because of the personalization for users, chat-bot will be able to attract clients to the eateries.

> Benefits to users:

The first benefit for the user is that the user will have one list of all the eating establishments in our website (Telegram WebApp), so the clients won’t need to search somewhere else, or visit different sites to view a menu. It is time saving for the user. The second benefit is personalization. Users will have personalized recommendations and discounts from the eateries, and advising the dishes. Thirdly, since we will gather statistics, we will have the ability to share with customers, amount of each product to buy and which number of dishes to cook more etc. Additionally, our website will have a convenient online menu with a nice design, improving UI and UX.

> Differentiation:

Our competitive advantage for clients is that they will have  a personalized app and it will improve their experience a lot. Also nice design is a rare thing in apps like this. 

Our competitive advantage for eateries is that they will have personalized advice based on the statistics we gathered. It can improve the business model of the company which is crucial.

> User Impact:

Our app makes it easier for clients to discover new places to visit and to choose the dishes. The main impact on clients is that they will have a personalized app.

Our app improves the productivity of the eateries, because it allows the establishments to reduce the number of people working in your business. Moreover, it allows us to centralize all the systems at once. Advice from AI is a useful tool that improves the workflow. 

> User testimonials or Use Case:

The client came to the restaurant, but they didn't know what to order. The client asks the chat-bot what to order like: “Advise what to order for four people for less than 100 dollars.” Our chat-bot can advise the user dishes. And also it can help the eateries to sell what they have left more than should. It helps both of the sides. 

Another example is that the owner of the establishments doesn’t have a big profit, because his business model is not that profitable. Our AI can advise the way to improve the business model based on statistics. 


## **Lean Startup Questionnaire**

> 1. What problem or need does your software project address?

Our project is aimed to develop a convenient environment for businesses in the food (restaurant) industry. The software we suggest is a system for companies allowing them to take orders automatically, get ratings and statistics, personalize the customers and special offers for them.

> 2. Who are your target users or customers?

Our target users are going to be the restaurant businesses and end users, i.e. customers of the restaurants using our software. The companies use our solution for unified order taking and their customers for convenient order making.

> 3. How will you validate and test your assumptions about the project?

We will obtain the data of some certain cafe/restaurant, calculate metrics, analyze the info about sellings and revenue. Then provide the company with our product and evaluate the performance after some time. Compare the data and track the tendencies.

> 4. What metrics will you use to measure the success of your project?

For the efficiency evaluation we will use the economic metrics which are supposed to be the main ones for any business, e.g., customer retention rate, average order value and the customer satisfaction index.

> 5. How do you plan to iterate and pivot if necessary based on user feedback?

We will definitely design a process that allows users to give feedback regularly and ensure that the team is actively listening to their suggestions. Based on it, we will modify the trajectory of our further development. 


## **Leveraging AI, Open-Source, and Experts**

> AI:

We plan to use AI in several ways:

Firstly, we are going to introduce chat-bot helping users to choose dishes from the menu. It often happens that people don't know what to order and they only have vague desires such as “sweet coffee drink” or “lunch without soup under 500 rubles”. Here comes the chat-bot, which will take into consideration any client desire and provide suggestions. 

Second way to use AI is to collect and analyze data from the clients and provide them with personal offers such as fixed discounts on all the dishes or discounts on particular combos. We are going to use knowledge acquired during IML and STDSR courses to generate useful statistics and suggestions for the customers.

Lastly, we plan to speed up our development using tools such as ChatGPT, Copilot, DALLE, etc. They will help us with bug-fixing, test coverage, meaningful picture placeholder generation and other labor work.

> Open-source:

We plan to use tailwind css framework as it is providing comprehensive designs for free and it will be very helpful due to the lack of time for the project. For the development part, we will use open source libraries for frontend (React), backend (Pyrogram, Flask), ML (pandas, scikit-learn, numpy, etc.) For the deployment part, we are planning to use docker.

> Experts in relevant domain:

- Andrei Markov - backend specialist, he will help us resolving issues with database scheme
- Rustam Lukmanov - ML specialist, he will help suggest us on ML problems

## **Inviting Other Students**

> Solution:

We plan to invite some students for help in particular parts of our project such as database schema creation and ML-algorithm implementations, since we might not have enough expertise in those fields.


## **Defining the Vision for Your Project**

> Overview:

We provide a simple and unified solution for ordering food in restaurants. Telegram bot (with the usage of WebApp) will make it easier for users to interact with the restaurant, and will be able to provide personal offers for each user. AI assistant can help with the choice of dishes.

> Schematic Drawings:

![Our project scheme](/Onemenu/scheme.svg)

> Tech Stack:

We will use python for backend and ML because we are most experienced with it. For the server we will use the Flask framework, for telegram bot - Pyrogram. For frontend we will use JavaScript React because we are also familiar with it.

> Anticipating Future Problems:

One major problem of all software projects is unclear architecture. If we choose the wrong structure of our project now, then, in the future, it would be hard to maintain and develop the product. Moreover, if during the development it turns out that the architecture is unsuitable for our project, then the project will be unfinished. To avoid this, we will thoroughly choose the architecture and development stack in the beginning, and if we find any problems with our choice, we will make corrections as fast as possible to avoid problems in future.

> Elaborate Explanations:

Our app consists of 3 components: backend server, telegram bot, website. Website and bot will do essentially the same thing: clients will interact with them to order dishes, and restaurant staff will see available orders. Server will be used to process inputs from bot and website, and also for ML (analytics).

{{< hint danger >}}

**Feedback**  
You have a great team and a great project! It is also clear that you have a properly defined vision for the project. The idea of the Capstone is to create a smallest working prototype - therefore, take one menu from one restaurant and try to showcase you technology. Scale down your project to the main features and execute on the main parts. 
{{< /hint >}}

