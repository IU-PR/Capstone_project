# **Stock Vision** 

We are doing a project called Stock Vision. The aim of this project is to develop an ML tool for traders that provides additional analysis and predictions for stock market / currency pair movements.

---

# **Week #1**

### **Team Members**

| Team Member            | Telegram Alias   | Email Address       |
|------------------------|---------------|---------------------|
| Danil Timofeev          | RND_RandoM | d.timofeev@innopolis.university     |
| David Eje          | David_ej | d.edje@innopolis.university     |
| Daria Lebedeva          | SwansOfApollo | d.lebedeva@innopolis.university     |
| Dima Batalov         | Legolass322 | d.batalov@innopolis.university     |
| Nikita Zorin          | nikznn | n.zorin@innopolis.university     |


### **Value Proposition**
- **Identify the Problem:** For many individuals and businesses involved in foreign exchange (forex) trading, making informed decisions can be challenging due to the complex nature of the market. Traders often struggle with identifying profitable entry and exit points, managing risk effectively, and staying up to date with market trends and analysis. This lack of expertise and timely information can lead to suboptimal trading decisions, resulting in financial losses.


- **Solution Description:** Our software project offers an AI-powered solution that revolutionizes forex trading. By leveraging advanced algorithms and machine learning techniques, our software analyzes vast amounts of historical and real-time market data, identifying patterns, trends, and potential trading opportunities. It provides accurate and reliable forex signals and suggestions, helping traders make well-informed decisions with confidence.

- **Benefits to Users:** Using our software project brings several key benefits to forex traders. Firstly, it saves them significant time and effort by automating the analysis and monitoring processes. Traders no longer need to spend hours studying charts, analyzing indicators, and conducting research. Our software does the heavy lifting, delivering concise and actionable signals directly to their devices. Secondly, our solution enhances traders' decision-making capabilities by providing accurate and data-driven insights, reducing the likelihood of errors or emotional biases. This leads to improved trading performance, increased profitability, and minimized risk exposure.

- **Differentiation:** What sets our software project apart from other forex signal providers is our use of cutting-edge AI technology. Our algorithms continually learn and adapt to market conditions, ensuring that our signals are always up to date and aligned with current trends. Moreover, our software's user-friendly interface and intuitive design make it accessible to traders of all experience levels. Additionally, we prioritize transparency and reliability, providing detailed performance reports and maintaining a track record of successful trades. These unique selling points make our solution the preferred choice for traders seeking accurate and actionable forex signals.

- **User Impact:** The adoption of our software project has a profound impact on individual traders, businesses, and the forex trading industry as a whole. By empowering traders with AI-driven insights, we enable them to make more informed decisions, reduce losses, and increase profitability. This, in turn, fosters confidence and growth within the trading community. Moreover, our solution democratizes access to advanced trading tools, leveling the playing field and providing equal opportunities for traders regardless of their experience or resources. As more traders benefit from our software, we envision a more efficient and transparent forex market that drives positive change.

- **User Testimonials or Use Cases:**
None so far 

## **Lean Startup Questionnaire**

Please answer the following questions related to the lean startup methodology:

1. What problem or need does your software project address?
   - Trading is hard, so we simplify the analysis that traders' perform by giving them AI predictions
2. Who are your target users or customers?
   - Traders who trade intrahour / intraday
3. How will you validate and test your assumptions about the project?
   - Run the model and see the accuracy / return of our predicted portfolio
4. What metrics will you use to measure the success of your project?
   - Return Of Investment for a given portfolio
   - Consistency of predictions
   - Amount of users who pay for the subscription (if we get to that point)
5. How do you plan to iterate and pivot if necessary based on user feedback?
   - It's possible to change the timeframe (to make the tool more suitable for investors instead of traders), add more instruments, add more analysis options. Or make the tool more suitable for hedge funds

## **Leveraging AI, Open-Source, and Experts**

- **AI (Artificial Intelligence):** we will be heavily using Machine Learning, and maybe even Reinforcement Learning to find the best algorithm to predict the prices. And, of course, we will be utilizing the power of Generative AI to help with development.
- **Open-Source:** we will be using Flutter, PyTorch, and most probably, some existing ML stock prediction projects to help us.
- **Experts in relevant domains:** TAs of our electives (Applied Machine Learning, Data Wrangling and Visualization, and others)

## **Inviting Other Students**

We initially formed a team, but after the discussion of the project some people decided to leave the team to work on their own project. So, we needed to find somebody who will do DevOps and Frontend. After "recruiting", I found a backend/DevOps person and a Flutter person. Now, our team is complete: ML people, DS person, Flutter frontend people and a Backend person.

## **Defining the Vision for Your Project**

- **Overview:**
The purpose of our project is to develop a ML tool for traders that provides additional analysis and predictions for market movements. By leveraging historical market data and utilizing ML techniques, our project aims to assist traders in making informed decisions and identifying potential opportunities in the stock market. The stock market is a very dynamic field, so additional analysis would be beneficial for traders and make their lives easier. They can leverage our tool to improve their decision-making, enhance their efficiency as a trader, and manage risks more effectively.

- **Schematic Drawings:**
![Diagram](/group/stockvision/diagram.jpeg "Diagram")

- **Tech Stack:**
    - Frontend: Flutter
    - ML/DS: PyTorch, pandas, etc.
    - Backend: most likely, NodeJS
    - MLOps: ??
    - DevOps: most likely, Yandex Cloud

- **Anticipating Future Problems:**
    - Poor performance of the ML model due to the complexity of the task.
    - We have no idea how to deploy ML models, so we will have to find this out.

- **Elaborate Explanations:**
1. Critical components:
   - Flutter app: minimalistic mobile / web dashboard that shows available instruments and notifies you about predictions.
   - Backend+database: a backend that supports auth, notification sending, and communication with the broker.
   - Broker: controls the connection between the backend and the ML server.
   - ML Server: repeatedly retrains the model (we most probably will be using online learning) and returns the predictions to the broker.
2. Core functionalities: 
   - auth, notifications, predictions, user feedback, simple UI
3. Innovative aspects:
   - We will most likely try using Reinforcement Learning to learn the patterns, and try to do some research for cutting-edge algorithms to give us a competitive edge.


{{< hint danger >}}

**Feedback:**   
Hi, this is a very interesting and potentially technically complicated project. I think it will be challenging to finish the project in confines of the Capstone as it currently stated. Consider scaling it down to a creating an app that does alpha/trading signal generation on one FX pair. Choose the platform from which you will be getting the FX data and try to focus on tech side of the project - to show that you can do it with one currency pair. Overall, I think this is a very in-demand product as lots of retail traders want more reliable signal apps. 
 
{{< /hint >}}

# **Week #2**
## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Architecture Design**

Designing a robust and scalable architecture is crucial for the long-term success and maintainability of your software project. This week, focus on defining the architecture that will serve as the backbone of your application. Consider the following aspects:

### **Component Breakdown:**

- **Mobile App:** This will act as the user interface developed in flutter. The user should be able to login and see the signals for the various currency pairs. Through this app the user can give feedback on the the predictions.

- **Authentication Service:** This is responsible for verifying and authorizing user access to the various resources on the backend.

- **Notification Service:** This is responsible for notifying the listening users when there is a new signal for a currency pair in their watchlist.

- **Consumer Service:** This is in charge of reading messages from the message broker and persist into a storage

- **Prediction Service:** This is a machine learning algorithm that generates the signal and pushes it to a rabbitmq service to be consumed by the consumer service.



### **Data Management**:
- **Database:** Firebase/ Firestore
### **User Interface (UI) Design**: 
- [Figma Link](https://www.figma.com/file/IXQhGgoVPjEqvQopgBl0FD/Capstone-Project?type=design&node-id=0-1&t=ioboFNrxKdD4CYdt-0)

### **Integration and APIs**:

We will use [**alphavantage**](https://alphavantage.co/) for collecting the data and getting current market data that will be used to periodically train the model.
  


1. **Scalability and Performance**: Anticipate future growth and consider scalability aspects when designing the architecture. Ensure that your application can handle increasing user loads and data volumes without compromising performance.

2. **Security and Privacy**: Incorporate appropriate security measures into your architecture to protect user data and safeguard against potential vulnerabilities. Consider authentication, authorization, encryption, and other relevant security practices.

3. **Error Handling and Resilience**: Plan for handling errors and exceptions to maintain a reliable and resilient application. Define strategies for error logging, monitoring, and graceful error recovery.

4. **Deployment and DevOps**: Consider the deployment process and DevOps practices that align with your chosen tech stack. Automate deployment tasks, implement version control, and establish a robust development workflow.

{{< hint danger >}}

**Feedback by Rustam:**   
So no ideas about scale, security and resilience?
{{< /hint >}}

5. **Scalability:** We are going to use kubernetes, so each service will be described with configuration file, which provides simple joining/excluding models and services to cluster, so the most scalability problems easily resolved.
   
6. **Security:** We are going to use JWT for auth and typical solutions for storing passwords. We will use Yandex Cloud to deploy, and make an API Gateway for clients so no inner services will be available from outside. (not mvp) Testing/Stable versions and enviroments.
7. **Error Handling:** (not mvp) Grafana
8. **DevOps:** We have already setup a Gitlab CI agent in kubernetes in Yandex Cloud, next steps are to configure each service and setup apk building.


**Mentorship Support:** Do you currently have a mentor actively involved in your project? If yes, kindly share the name of your mentor and explain how their guidance has positively influenced your project. If you don’t have a mentor yet, have you considered seeking one? How do you believe having a mentor could contribute to the success of your project? Remember, having an experienced mentor that can guide you and your team is your responsibility.

> We don't have a mentor yet, but we are considering an option to ask our AML TA (Imad Bekkouch) to guide us with the model. Having a mentor will simplify our work and allow us avoid potential

**Exploring Alternative Resources:** In addition to project-based books, what other resources have you explored to expand your understanding of your tech stack? This could include online courses, video tutorials, documentation, or any other sources that have been valuable in filling knowledge gaps. Please, name at least 3 resources

> We are not using books, but online courses to gain knowledge:
> 1. DL Course (understand neural networks to be able to build the prediction model): https://www.udemy.com/course/> the-complete-neural-networks-bootcamp-theory-applications
> 2. ML Ops: https://www.youtube.com/playlist?list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK
> 3. Flutter course: https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps

*Identifying Knowledge Gaps: Are there any specific areas within your tech stack where you or your team feel there are knowledge gaps or expertise is lacking? If so, how do you plan to address these gaps and ensure a well-rounded understanding of your chosen technologies? Please name the tech stack division in your team and outline how are you planning to deal with knowledge gaps*

**We have a knowledge gap in creating the actual model, because we are not sure about the exact architecture of the model, and how well it's going to perform. We are not using advanced financial mathematics, like stochastic calculus, which is a common practice in big corporations.
Furthermore, we've never setup clusters, which provide several enviroments, as well as we’ve never handled error logging and metrics collection.**

*Learning Objectives: What specific learning objectives have you set for yourself and your team in relation to your tech stack this week? How do you plan to achieve these objectives, and what strategies or resources will you employ to deepen your understanding?*

**This week, we have been studying ML and MLOps (Courses 1, 2). Also, we've been taking a DataCamp course to preprocess the data that we are getting from the Forex endpoints. Next week, we will start developing the Flutter app.**

*Sharing Knowledge with Peers: How have you been sharing your knowledge and expertise with your teammates? Have you organized any knowledge-sharing sessions or discussions to facilitate the exchange of insights and experiences related to your tech stack?*

**We hold meetings every week to ensure that everybody is staying on their track. We don't follow Agile yet, since we haven't started working on the project heavily, but we are planning to have more frequent meetings from the next week.**

*How have you leveraged AI to compensate for any lacking expertise in your tech stack? Have you utilized AI-powered tools or platforms to expedite the process of acquiring knowledge and expertise in your tech stack?*

**We extensively use generative AI like ChatGPT to help us gain the expertise we are lacking.**

## **Tech Stack:**

**Frontend**: Flutter <br>
**ML:** pytorch & keras <br>
**Backend**: NodeJS, Firebase <br>
**DevOps:** Docker, RabbitMQ, kubernetes <br>

## **Role Distribution:**

**Danil Timofeev** - UI/UX Design / Flutter Developer <br>
**David Eje** - ML Engineer <br>
**Dima Batalov** - Backend Developer / DevOps <br>
**Daria Lebedeva** - Graphic Design / Data Analyst <br>
**Nikita Zorin** - Flutter Developer <br>

We took each team members' skills and preferences and distributed responsibilities accordingly. All of our team members have the necessary skills to complete the given tasks.

{{< hint danger >}}

**Feedback by Rustam:**   
Progress reports are here to make sure that you have covered all major aspects of the dev process. Please do not copy all the text from the weekly tasks, but rather explain your progress on the basis of the questions and structure provided (it is also possible and encouraged to add your own sections if needed). After each week iteration it is possible to rework the report and make changes to the previous week. Please, next week update your project report file according to feedback. For me, is is still not clear the exact work you are planning to do to accomplish the project and develop a prototype. 
What this model supposed to do? 
Who will be the user and why would they prefer you vs. other trading apps? 
What would happen to the trading signal once it's available in the market? 
Can it dissapear due to trading on this signal?

You write in your report that: "By leveraging advanced algorithms and machine learning techniques, our software analyzes vast amounts of historical and real-time market data, identifying patterns, trends, and potential trading opportunities."
However, I am struggling to see how exactly you are planning to do that. 

Plus, the formatting of the progress reports is also part of the evaluation. Make sure that your reports look neat and clearly written. Avoid very general descriptions that "we will use AI and advanced algorithms" - we want very prices action plan on defined algorithms, frameworks and technologies. 
  
3/5 
{{< /hint >}}