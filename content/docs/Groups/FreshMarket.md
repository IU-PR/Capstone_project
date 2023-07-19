---
weight: 1
bookFlatSection: true
title: "FreshMarket"
---
# **FreshMarket**


<img alt="icon" src="/FreshMarket/assets/icon.png" width="200">

[Website](https://innofreshmarket.github.io/flutter/)  \
[Github](https://github.com/InnoFreshMarket/)
[PDF](FreshMarket/assets/FreshMarket.pdf)

# **Introduction**
 
Fresh Market is a marketplace of farm products with the possibility of subscription. Customers see the assortment of regional farm products and collect products in the basket for ordering. Farmers post products with photos, descriptions, quantities and the possibility of subscribing to their products. When placing an order, the buyer chooses payment by card, cash or invoice for the organization and chooses the delivery method courier, pickup or transport company. The farmer receives his funds the next day after the delivery of the goods to the card attached to the profile.

# **Week #1**

### **Team Members**
| Team Member            | Telegram ID        | Email Address                      |
|------------------------|--------------------|------------------------------------|
| Timur Kharin **(Lead)**| @timur_harin       | t.kharin@innopolis.university      |
| Ilya Pecherskiy        | @Happy_endon       | i.pechersky@innopolis.university   |
| Renat Khairullin       | @renatkh           | re.khairullin@innopolis.university |
| Grisha Rybolovlev      | @Grisha_Rybolovlev | g.rybolovlev@innopolis.university  |
| Herman Dyudin          | @Dudukk            | h.dyudin@innopolis.university      |
| Zufar Azizov           | @hugowea           | z.azizov@innopolis.university      |


### **Value Proposition**

1. **The problem:** In grocery stores, purchasing directors choose large suppliers who win the competition at the expense of not purely grown animals and products. Farmers with excessive production are forced to find their customers in chat rooms in messengers. Buyers want to buy fresh and cleanly grown products, but there are no guarantees in the delivery of the product after transferring funds directly to the farmer's account.

2. **Solution:** Fresh Market is a marketplace of farm products with the possibility of subscription. Customers see the assortment of regional farm products and collect products in the basket for ordering. Farmers post products with photos, descriptions, quantities and the possibility of subscribing to their products. When placing an order, the buyer chooses payment by card, cash or invoice for the organization and chooses the delivery method courier, pickup or transport company. The farmer receives his funds the next day after the delivery of the goods to the card attached to the profile. The most adequate and working store on the Russian market is esh-derevenskoe.ru , but they do not work with a subscription in any way and cannot give regular customers to their suppliers.

3. **Advantages for the parties:** We are intermediaries between the buyer and the farmer, which gives security in both directions: the farmer will receive money only for a quality product, the buyer will give money only for a quality product. It is easier and more variable for the buyer to choose and order goods, and the farmer does not have to worry about promotion, because buyers see his products, rating and reviews

4. **Differentiation:** A distinctive function from all other marketplaces of fresh farm products is a subscription for delivery, thanks to which the buyer knows that, for example, every week for a month he will have a dozen fresh chicken eggs, and the farmer knows that he has a planned demand for his products

5. **Impact on users:** Explain what broader impact your software project has on users and possibly on society or the industry as a whole. Highlight any positive changes, transformative effects or achievements that result from the implementation of your solution. Think about how it improves workflows, empowers users, or promotes positive change.

6. **Impact:** More users will have a reliable tool for buying fresh farm products, and more farmers will be able to commercialize their mini production without problems

7. **Interest:** The Ministry of Agriculture of the Republic of Tatarstan has shown interest in developing such a product for farmers of the republic, because now everyone really has to spam in chat rooms about their products

## **Lean Startup Questionnaire**

1. *What problem or need does your software project address?*
**Answer:** Our software project solves the problem of finding potential customers or finding farmers to buy fresh products without spending a lot of time. Now it is more common to post such advertisements in messengers like WhatsApp or Telegram. So it makes it hard to find it efficiently, the central platform would be convenient.

2. *Who are your target users or customers?*
**Answer:** Our target users/customers are:
– farmers who want to sell products,
– people or companies (cafes, restaurants) who want to buy these products

3. *How will you validate and test your assumptions about the project?*
**Answer:**  To validate and test our assumptions about the project, we will interview with people who often buy fresh products or farmers. We are going to ask them about how much time they usually spend on selling/buying and would it be more convenient for them if there will be one platform for this purpose specifically.

4. *What metrics will you use to measure the success of your project?*
**Answer:** Metrics to measure the success of our project are the number of users that will register and use our platform and the feedback, which we will collect to ensure that this platform is convenient and needed.

5. *How do you plan to iterate and pivot if necessary based on user feedback?*
**Answer:** Based on user feedback, we plan to iterate and pivot if necessary by changing the UI to make it more user-friendly, also we can add some new features, post more information about users and products if they need it.


## **Leveraging AI, Open-Source, and Experts**

For our project, **we don't really need** to use Artificial Intelligence, Open-Sources, or any sources with experts in relevant domains. For our domain, any of these resources will approach us to development or success. However, at some stage, to provide more useful and usable functions of our product to potential users, **we will need to interview** some farmer-workers to collect necessary data.

## **Inviting Other Students**

At this stage, **we have assembled a full team** of people covering all the positions needed for the project, so for now we are not planning to invite other students for our project. Nevertheless, in case of any specific situations, we are ready to collaborate with other people or teams to complete the product.

## **Defining the Vision for Your Project**

1. **Overview:** Provide a concise summary of your project, highlighting its purpose and value proposition. Explain how your project addresses a specific problem or need in the chosen domain. Clearly state the intended benefits and impact on users or stakeholders. 
Answer: Our project is a platform that helps farmers sell their products directly to consumers. By eliminating middlemen and offering a subscription model for customers, we connect farmers with a wider customer base. The platform addresses the problem of limited market access for farmers and offers benefits such as increased profitability, reduced dependency on intermediaries, and access to locally sourced produce for customers. Ultimately, our project aims to empower farmers, connect them with consumers, and create a sustainable ecosystem in the agricultural industry.

2. **Schematic Drawings:** Use visual representations such as diagrams, flowcharts, or wireframes to illustrate the structure and flow of your project. Include all essential components, modules, and interactions within the system. Ensure the drawings are clear, labeled, and easily understandable by both technical and non-technical stakeholders.
![image1](/FreshMarket/assets/requests.jpeg)
![image2](/FreshMarket/assets/parts.png)

3. **Tech Stack:** Specify the technologies, frameworks, and programming languages you plan to utilize in your project. Justify your tech stack choices based on their suitability for the project requirements and team expertise. Consider scalability, performance, security, and ease of development when selecting your tech stack.
Answer: For the backend part (API) we have chosen the Django framework because it provides convenient ORM. As a database we decided to use PostgreSQL. Also to authorize requests to the backend part we will use JWT tokens. Visual part of our platform will be  written using Flutter because of its cross-platform usage. For the beginning we will create the website but then it will not be difficult to convert it to the mobile app. All these parts are good in both performance and ease of development.

4. **Anticipating Future Problems:** Foresee potential challenges and obstacles that may arise during the project development and deployment phases. Identify risks related to technical complexities, resource limitations, time constraints, or external dependencies. Propose mitigation strategies or alternative approaches to address these anticipated problems. 
Developing a platform that caters to both farmers and customers can be technically complex. There may be issues related to compatibility, scalability, and security. Talking about resource limitations, the project may require a significant amount of resources, including human resources, financial resources, and technological resources. Finally, we have some time constraints: the project may face delays due to unforeseen circumstances such as technical glitches or changes in requirements, and still for creating a MVP we have only seven weeks.
To deal with such problems, we should stick to following strategies: 
– Create a detailed project plan that outlines the required resources and allocate them accordingly, 
– Conduct regular testing and debugging to ensure the smooth functioning of the platform,
– Set realistic timelines and milestones for each phase of the project. Regularly monitor progress and adjust timelines if necessary.

5. **Elaborate Explanations:** Provide detailed descriptions of critical components, algorithms, or methodologies employed in your project. Explain the core functionalities and how they contribute to achieving the project goals. Highlight any innovative or unique aspects of your solution that differentiate it from existing alternatives.
Answer: Our project employs the MVC template, JWT tokens for security, and a REST API. The MVC pattern separates the application into Model, View, and Controller components. JWT tokens provide secure authentication, while the REST API enables communication with well-defined endpoints. Core functionalities include user authentication, product listing and management, subscription model, and order management. Our solution stands out by facilitating direct farmer-consumer interaction, offering a subscription model, and ensuring secure authentication.

{{< hint danger >}}

**Feedback**  
I think, your project is really cool! A long needed service that will benefit us all - by making as healthier through delivering high-quality farmer produce. Your team's dedication and strong collaboration are evident, and it's great to see that you have a clear vision for the project.

Considering that our course aims to achieve a minimal viable product (MVP) by the end of the semester, I would suggest, as to most teams, to focus on scaling down the project to create a web app that encompasses the core functionalities. This approach will allow you to build a solid foundation that can be expanded and enhanced in the future.

To ensure efficient execution within our limited timeframe of already six weeks, I recommend outlining the main features of your project and prioritizing their development. It's essential to identify specific areas that can be streamlined or simplified without compromising the core functionality.

Also, take a note that it is possible to utilize open-source as means of scaling down your project: for example, there is a multitude of open-source platforms for e-commerce: i.e. https://saleor.io/, https://strapi.io/ that you can use as a modular back-end. Although, I am not sure how rigid or flexible this solutions are. {{< /hint >}}

# **Week #2**

1. **Tech Stack Resources:**
Actually, we prefer online-courses, documentations, and other resources to books since this way it is easier and faster to find necessary information. However, we do not avoid using additional sources in case of extraordinary situations and problems. For such cases, we will turn to books which cover tech stack of our project: 
- "Django for Beginners" by William S. Vincent
- "Flutter in Action" by Eric Windmill
- "Python Crash Course" by Eric Matthes
We are familiar with these books, so we are sure that they would provide a comprehensive understanding and help in building the project or be a reference guide for any future updates or changes in the tech stack.

2. **Mentorship Support:**
No, we currently do not have a mentor actively involved in our project. Still, three members of our team now have a Programming in Python elective, so its lecturer, Alaa Aldin Hajjar, agreed to weekly follow-up progress connected with the python-related part of the project. We haven’t considered seeking another mentor for the whole project but we believe that having an experienced one will put project management in strict structureness and keep team members disciplined.

3. **Exploring Alternative Resources:**
In addition to project-based books, we expand our understanding of our tech stack by following resources: 
- as already was said, attending Programming in Python elective really helps us extend our knowledge in language; 
- Python, Django documentation to understand specific nuances;
- video tutorials on Youtube; 
- saved notes from the Flutter elective from a year ago. 

4. **Identifying Knowledge Gaps:**
Project is equally divided into two huge parts: backend and frontend; three of our members are responsible for front-, which is mostly based on Flutter, while three others deal with backend by using Python, Django framework. For now, team is fully aware of what they should do and how they should do it due to early gained experience in corresponding areas. 
But, of course, it is inevitable that in the future we will face several problems due to lack of knowledge — this is when we will start using relevant resources (books, courses, documentations, tutorials) described above.

5. **Engaging with the Tech Community:** 
We have never interacted with the wider tech community. We have not been to special forums and groups, nor have we been to local meetups. At the moment, we don't have a way to engage experts on critical technology stack issues.

6. **Learning Objectives:** 
Well, firstly, we plan to expand our knowledge in the field of front-end flutter. It is also planned to expand their knowledge in the field of backend. To achieve our goals, we plan to use third-party courses, as well as information on the web.

7. **Sharing Knowledge with Peers:**
​As a team, we communicate on the project quite often. We have a common group in telegram where we write all the changes on the project, as well as if we want to get together to discuss further goals. Outside of the project, we also communicate very often and exchange experiences and ideas with each other.

8. **AI in project** 
For the project, we did not use AI. We take our entire technology stack from courses on the web, as well as on forums where we discussed the problems that we had and new technologies that we may soon need.

## **Weekly Progress Report**
The first and the most important thing we did is that we decided what functionality we want to implement during this course. They are basic buying, adding, removing and editing products. Also it is filtering by type and some other small features. Right after making a decision about functionality we decided which models our Django backend will have. We tried to not forget about something because it is very problematic to change databases after starting a project. Sometimes it causes problems, so we hope that this number of classes will be enough. After that we were already divided into two teams and started working on the backend and frontend part. 
According to frontend part:
We have made significant progress in terms of the visual interface. Firstly, the overall design of the platform was launched by creating a common set of client tools, uikit. It also turned out to implement an authorization page, and work is also underway to link this page with our backend part.
In the future, we plan to use the prepared database in the form of uikit to develop a single GUI template.
According to backend part:
As we decided which models we will create, we started to implement them. So we created a django application. Connected it to the PostgreSQL database. Django has a convenient ORM so working with databases will not be hard. After that we implemented classes with all their fields and inner functions. In the next week we want to start implementation of the API part. In other words we want to create functionality for our application to sell, buy, add products and connect it with a database. We already have some problems with using files and images. We were discussing how to send and retrieve them. For now we agreed that we will use the Base64 format because of its simplicity. So we will send base64 code and name of the file to restore the file with the true name and extension. 

In general we did a great job. We thinked over our models and their connections and already started working on its implementation.

{{< hint danger >}}

**Feedback by Rustam**  
All parts of the tasks are covered and I liked your own assessment of the state of affairs regarding your progress. Make sure to think through the process of providing efficient communication between the backend and frontend team members as it can het a little messy sometimes. Consider adding more AI-assisted scripting to expedite the process of developing routine features - this course aims to develop skills of fast prototyping, so make sure to use this advantage. 
I am a little surprised that you have no connections with the local tech community. There are numerous meetups every year and it's a great opportunity to get up to last trends and solutions. After all, there is almost 2000 developers in the city, and I hope, one can think of ways to leverage that for developing your network and projects.
5/5 for the week
{{< /hint >}}

# **Week #3**

**Prototype Features:**
Frontend:
- Login and registering with saving in local secure store JWT tokens
- Integrate and providing own chat interacting implementation between any 2 users
- UI-kit

Backend:
- Methods for registering and logging users in, and getting their JWT tokens. Now, after signing up or logging in, the user will get a JWT token which he can use to make requests to the IP
- Methods for getting your own ID (system will return ID of your user); for leaving comments to some other user and see comments got by other people; for getting information about user (address, number, etc.) and also for editing your own personal info
- Methods to place, edit the goods, to get the goods of a particular farmer; also for getting them; and getting not just all the goods, but the goods of a particular category.

**User Interface:**

Frontend visual - https://innofreshmarket.github.io/flutter/
Backend Django interface - https://fspmainservice.onrender.com/


**Challenges and Solutions:**
- Bacause main platform is web and front part is flutter - it is difficult to manage work with JRT tokens => We just needed some hours to do it 
- Manage naming for API => write it and do not touch without two-side agreement

**Next Steps:**
- Make product shelves with categories
- Make search working
- Make states of order with status and estimated time


{{< hint danger >}}

**Feedback by Rustam**  
It seems that you have an ordered approach to the project and already have main parts deployed - which is great. 
I hope you and your team will be able to keep the pace and make the necessary adjustments on the way. 
Progress report is a little too short, would be interesting to see more details on current considerations and trade-offs regarding the choices you make.  
5/5 for the week
{{< /hint >}}

# **Week #4**

**External Feedback**

Parallel to this course, some of our team members have another one called the Basics of Product Management, in which they had to take some interviews with potential customers to collect some information about their problem (pain the customer face), what they already tried to do, cost and frequency, and also some insights. 
So,  overall, they talked to 6 different farmers and asked them about some issues connected to their work 

According to the results of the interview on the first week of our courses, we specified the first part of customer segment - farmers, who want to sell their products but can't find enough clients or have no time to sit and sell their products on a fair. So 2 biggest problems are time and finding new clients. Because it is done offline or with groups in messengers. So our goal should be to make ONLINE platform and make it convenient, so people would use it.

Then, three weeks later, they had different task to collect feedback already about the prototype. That is why we took the interview with the farmer from Verhniy Uslon Alexey Arhireev (the
same person we took an interview with during problem validation). After showing him
the prototype and describing some functionalities that it will have we took feedback
about it. He said that solution is what he needed exactly, it looks pretty user-friendly
and has the functions that he needs. The most important advantages that he had
pointed:
1. It is an online platform, so the number of clients is not limited by distance.
2. Also if the platform will be used by customers then selling the products will be
easier.
3. User-friendly interface will allow people of all ages to use it, even if people are not
experienced smartphone or PC users. (that is really important point for old people)
4. We have subscription functionality. He pointed out that never saw it, so he will be
able to have regular customers.
5. He will not spend time sitting on fairs, he will be able to spend more time on
farming and just post products on the platform.
6. He really appreciates that the platform is free, so more people will use it.
Actually he didn’t mention the weak spots of such a platform except for the number
of users who will use it. He said that it will not be a useful platform until a big number
of clients will use it. So it will take some time before this platform will be used by
farmers.
So as a result, the farmer told us that it is a good and useful platform, so if it will be
used by both clients and other farmers it will help him to do his job.


**Testing** 

**In flutter** we have tests:
- Unit tests for functions and classes
- Widget tests for widgets
- Integration tests for the whole app

Because we are making startup - we only need unit and widget tests
Especcialy unit tests are important for us because we are making a lot of cost calculations, transport estimations and balance operations

Unit tests are written in the different file with the same name but with _test suffix
It helped us to separate tests from the code and to make code more readable
And also find bug which could make order without enough balance for customer

**In django** backend we have tests:
- Model tests
- Form tests
- Api tests

Because of not enoght time we tried only to test model and api test in django
It held us to catch some bugs about enums in models and waiting time in api tests


**Iteration**

We are using iterations like week springs and every week we have changes and we are coming closer to goals which we made.

We understood these things:
- The iterative approach is indeed a crucial aspect of successful project development
- By continuously evaluating and refining the project based on feedback and testing results, teams can adapt to changing circumstances and improve the product over time
-  But we don't have time to really feel the full power of this approach, because it requires several dozens such sprints

But because some of us working - we can illustrate our history in industry:
- Table with tasks and backlog is necessary
- Weeks to evaluate working period of each person
- For each feature we have to clip the person who will be response in any next iteration to debug or improve


{{< hint danger >}}

**Feedback by Rustam**  
Not sure about the comment about time - we are already 4 weeks in - not much time left for the prototype.
I've visited your repo and website - same as it was 3 weeks ago (just a navbar and few icons). Backend repo - 12 commits and once a week activity. 
I am a little concerned with the speed of your dev process - are you using different repo? 
If yes, please provide up to date information and screens of the current state 
Liked the interviews - good work.
Not much progress in developing the prototype
3/5 for the week
{{< /hint >}}

# **Week #5**

This week, our team focused on entering the second iteration of feedback collection for our online platform for farmers and customers. 

To accomplish our goals for the week, we executed the given tasks:

**1.** Scheduled meetings or interviews with relevant stakeholders: We reached out to potential clients, users, and fellow students to gather feedback on the current version of our product. By engaging with a diverse range of stakeholders, we aimed to obtain a broader perspective on our platform's strengths and areas that require refinement.
There were some farmers we met with on the first week of doing the project during the Basics of Product Management course; and some of our friends from our study groups who could really value our product and give detailed feedback. 

**2.** We developed a comprehensive plan that outlined specific questions and areas of focus to gather feedback on. Instead of conducting one-on-one meetings, we utilized algorithmic ways such as online forms to collect standardized feedback. This approach allowed us to quantitatively assess user satisfaction with our product and its features.

Questions were following: 
1. How often do you purchase fresh produce from local farmers?
- Daily
- Weekly
- Monthly
- Rarely
- Never

2. What are the main challenges you face when trying to buy local fresh products?
- Limited availability
- Lack of information about local farmers and their products
- Difficulty in finding a variety of products in one place
- Inconvenient purchasing process (e.g., long travel distances, limited payment options)
- Other (please specify)

3. On a scale of 1 to 5, how important is it for you to support local farmers and their businesses?
- 1 (Not important at all)
- 2
- 3
- 4
- 5 (Extremely important)

4. How likely are you to use an online platform that connects farmers and customers for purchasing local fresh products?
- Very unlikely
- Unlikely
- Neutral
- Likely
- Very likely

5. What features or functionalities would you expect from an online platform connecting farmers and customers for purchasing local fresh products? (Select all that apply)
- Detailed farmer profiles with information about their farming practices and certifications.
- Search filters to find specific types of produce or products.
- User reviews and ratings for farmers and their products.
- Secure payment options.
- Delivery or pickup options.
- Integration with social media platforms for sharing experiences.
- Other (please specify)

6. How user-friendly do you find the current design/layout of the online platform?
(open-ended feedback)

7. Are there any specific improvements or additions you would like to see in the online platform?
(open-ended feedback)

8. On a scale of 1 to 5, how satisfied are you with the overall experience of using the online platform?

9. Would you recommend this online platform to others who are interested in buying local fresh products?
- Yes
- No
- Maybe

10. Please provide any additional comments or suggestions you may have to help us improve the online platform.



**3.** We ensured clear identification of specific areas of improvement or enhancement by documenting all the feedback received from stakeholders. This documentation will serve as a reference point for future iterations and enhancements.
There are some statistics for first questions: 

1. 
- Daily: 5%
- Weekly: 30%
- Monthly: 40%
- Rarely: 20%
- Never: 5%

2. 
- Limited availability: 25%
- Lack of information about local farmers and their products: 35%
- Difficulty in finding a variety of products in one place: 20%
- Inconvenient purchasing process (e.g., long travel distances, limited payment options): 15%
- Other (please specify): 5%

3. 
- Average rating: 4.6

4. 
- Very unlikely: 2%
- Unlikely: 8%
- Neutral: 10%
- Likely: 50%
- Very likely: 30%

5. 
- Detailed farmer profiles with information about their farming practices and certifications: 70%
- Search filters to find specific types of produce or products: 80%
- User reviews and ratings for farmers and their products: 60%
- Secure payment options: 90%
- Delivery or pickup options: 85%
- Integration with social media platforms for sharing experiences: 40%
Other (please specify): N/A

6. How user-friendly do you find the current design/layout of the online platform?
- Average rating: 3.8


**4.** We carefully analyzed all the feedback collected from stakeholders to identify common themes, patterns, or recurring issues. This analysis allowed us to gain a deeper understanding of user needs and expectations.
With those who estimated our features lower than 4 we talked individually to get more feedback on what to improve. 

**5.** After analyzing the collected feedback, we prioritized it based on its impact on user experience and feasibility of implementation. This step will guide us in making informed decisions about which improvements or enhancements to focus on first.
Overall, this week was dedicated to gathering a broader range of feedback and refining our product based on the insights obtained. 


Speaking about  improvements which our back-enders and front-enders worked on this week: 
— members responsible for Django administration worked on balances and implementing the methods for ordering and buying. 
— front-end dealt with shopping basket, subscriptions; for farmers ordering list now can be shown (in alphabet order)


{{< hint danger >}}
Alright, report looks good. Liked the survey data - good work!. Noted the absence of the final presentation on the top of the file. Please add the PDF file to the top of the md file.
5 for the week!

Overall, I am optimistic and excited about your project. Good luck with the project and the final presentation! You have accomplished a lot! Cheers, Rustam 
{{< /hint >}}