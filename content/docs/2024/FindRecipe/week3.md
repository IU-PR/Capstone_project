---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

Как я понял, здесь можно расписать немного про то, как наша команда работает с гитом.
Тип вносим правки и корректикуем друг друга в чате 

По хорошему бы еще все форматы в json в гите зафиксировать, но ладно и так норм будет.

AlexeyShulmin:
Right now we are working on deployment of our whole project: server, telegram bot, and database - on remote virtual machine. Main problem here is in finding credible, reliable, and easy in use, but relatively cheap provider of VMs. We are giving it all to test different sources and find the best fit.

Development process in our team is pretty simple: each week we figure out tasks for thst week, assign them to people and commit work done to the GitHub repo. Every member of our team is participating in week-to-week progress and know how to work with git kit.
- **Backend Development**:

Structure of request for our server:

![request_struct](/2024/FindRecipe/API_req.jpg)

Structure of response from our server:

![response_struct](/2024/FindRecipe/API_res.jpg)

я не видел как это выглядело на прошлой неделе, но можно также расписать про этот функционал.

Нужно сказать, что на этой неделе нагрузка на бекэнд не добавилась. Остался тот же функционал и та же API. Но бекенд легко расширяем.

Также нужно упомянуть что за эту неделю мы 4 дня возились с деплоем и ничего не получилось, это нужно описать в последних блоках наверное.

Есть опциональный момент, если нужно еще что-то добавить, то можно сказать что локально алгос готов, но нужно сделать деплой, чтобы проверить его работу, 
но у нас пока что его нет.

AlexeyShulmin:
Crucial part of backend development in iur project is deployed and easily accessible database. Since we had no success in database deployment yet, we couldn't properly work on backend. We are actively searching for right service to deploy our database on. Two members of our team spent all week on that, but everything tried sadly wasn't fitting needs of our project.

- **Frontend Development**:

...

- **Data Management**:

We planned out the structure of iur database in furst week, extracted all necessary data using BeautifulSoup and Python's requests, and imported collected data into local MongoDB server. We also figured out, who to deploy MongoDB server and add our data to it on virtual machine with Ubuntu. Main problem is in host of this VM, since we want it to be online, not on one of our machines. Our database is basically reasy for production, since no writing operations would be necessary in our project, only data extraction from database will happen.

- **Prototype Testing**:

...

## **Weekly Progress Report**:

Our team did...

думаю здесь про то что девочки сделали почти всего бота, но остались улучшения (в некст степс) склеили его там и тд.

мальчики пытались сделать деплой, но не хватило мозгов. 

### **Challenges & Solutions**

During the development of our prototype, we had significant deployment obstacles, mostly due to a lack of DevOps experience and problems finding a suitable web service that provides free VPS. To solve the DevOps knowledge gap, we spent a significant amount of time researching internet materials to provide a solid basis. 
When it came to choosing a good online service, we discovered various free services that provide free vps. 
We divided the Telegram bot's functions into three parts, which made it tough to integrate these components. To overcome this, we held discussions to ensure a smooth integration. Finally, our persistence and collaborative problem-solving approach helped us overcome these challenges and successfully deploy our prototype.

### **Conclusions & Next Steps**

In the coming weeks, our primary focus will be on completing the deployment of our server and database, allowing our Telegram bot to submit queries to a real server and return actual menus. This deployment is critical for transitioning our prototype from a testing environment to the live operating stage. 
Following that, we intend to enhance the functionality of our Telegram bot by including features like tagging recipes as favorites, which will boost user experience and engagement. Furthermore, we intend to include the option to add images to menus, making the bot more visually appealing and instructive. These actions will greatly progress our project and lay the groundwork for future advances.
