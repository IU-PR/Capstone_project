---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

Right now we are working on deployment of our whole project: server, telegram bot, and database - on remote virtual machine. Main problem here is in finding credible, reliable, and easy in use, but relatively cheap provider of VMs. We are giving it all to test different sources and find the best fit.

Development process in our team is pretty simple: each week we figure out tasks for this week, assign them to people and commit work done to the GitHub repo. Every member of our team is participating in week-to-week progress and know how to work with git kit.
- **Backend Development**:

Structure of request for our server:

![request_struct](/2024/FindRecipe/API_req.jpg)

Structure of response from our server:

![response_struct](/2024/FindRecipe/API_res.jpg)

Crucial part of backend development in iur project is deployed and easily accessible database. Since we had no success in database deployment yet, we couldn't properly work on backend. We are actively searching for right service to deploy our database on. Two members of our team spent all week on that, but everything tried sadly wasn't fitting needs of our project.

- **Frontend Development**:

We have successfully created all the buttons for the three key sections: choosing preferences, demonstrating the menu, and editing the blacklist, according to the design we created earlier. Currently, we are in the process of integrating these components to ensure they work all together and are planning to work on connecting the frontend with the backend.

- **Data Management**:

We planned out the structure of our database in first week, extracted all necessary data using BeautifulSoup and Python's requests, and imported collected data into local MongoDB server. We also figured out how to deploy MongoDB server and add our data to it on virtual machine with Ubuntu. Main problem is in host of this VM, since we want it to be online, not on one of our machines. Our database is basically ready for production, since no writing operations would be necessary in our project, only data extraction from database will happen.

- **Prototype Testing**:

...

## **Weekly Progress Report**:

### **Prototype Features**

 In our  development progress 
- we've created intuitive buttons for key functionalities such as selecting preferences, displaying the menu, and managing the blacklist, all designed to match specified UI guidelines
- users can seamlessly interact with these features, choosing preferences like calories, cooking time or complexity, see the test menu (as we have not yet connected the bot to the server) and managing their blacklist to exclude test unwanted items (as we have not yet created a database for blacklist)
- we have set up a robust recipe database to store all culinary options, though deployment is pending.

### **User Interface**

The starting message tells user about the functionality of the bot.
There is always a button 'начать составление' available in the bottom to start generating menu.
After pressing this button preferences buttons displayed so that user could set their preferences by sending corresponding message
When clicking on blacklist button, the user sees a list of products as buttons and can add or remove them from blacklist
When clicking on generate menu button, the user sees product list for the menu and buttons to see menu for specific day of the week

![bot-start](/2024/FindRecipe/bot-start.png)

![main-button](/2024/FindRecipe/main-button.png)

![parameters](/2024/FindRecipe/parameters.png)

![calories](/2024/FindRecipe/calories.png)

![product-list](/2024/FindRecipe/product-list.png)

![black-list](/2024/FindRecipe/black-list.png)

![shopping-list](/2024/FindRecipe/shopping-list.png)

### **Challenges & Solutions**

During the development of our prototype, we had significant deployment obstacles, mostly due to a lack of DevOps experience and problems finding a suitable web service that provides free VPS. To solve the DevOps knowledge gap, we spent a significant amount of time researching internet materials to provide a solid basis. 
When it came to choosing a good online service, we discovered various free services that provide free vps. 
We divided the Telegram bot's functions into three parts, which made it tough to integrate these components. To overcome this, we held discussions to ensure a smooth integration. Finally, our persistence and collaborative problem-solving approach helped us overcome these challenges and successfully deploy our prototype.

### **Conclusions & Next Steps**

In the coming weeks, our primary focus will be on completing the deployment of our server and database, allowing our Telegram bot to submit queries to a real server and return actual menus. This deployment is critical for transitioning our prototype from a testing environment to the live operating stage. 
Following that, we intend to enhance the functionality of our Telegram bot by including features like tagging recipes as favorites, which will boost user experience and engagement. Furthermore, we intend to include the option to add images to menus, making the bot more visually appealing and instructive. These actions will greatly progress our project and lay the groundwork for future advances.
