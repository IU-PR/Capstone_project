# **Stock Vision** 

We are doing a project called Stock Vision. The aim of this project is to develop an ML tool for traders that provides additional analysis and predictions for stock market / currency pair movements.

---
![Logo](/group/stockvision/logo.png)
---
<!-- ![Presentation](/group/stockvision/final1.pdf) -->
{{< embed-pdf url="/group/stockvision/final1.pdf" >}}

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

{{< hint info >}}

We decided to pivot and make more emphasis on making the model more interpretable. Our main difference from the competitors is that we focus on interpretability, so that the trader can make better decisions based on the ML model. The end user of our app is a trader.
  
{{< /hint >}}

# **Week #3**

## **ML Model**
1. **Introduction**
The model utilizes data from the paid source, AlphaVantage, which provides hourly price data. The model is built using a transformer encoder architecture, incorporating positional encoding and embeddings for both time and price inputs. It employs multihead attention with 8 heads and consists of 5 encoder blocks to compute the attention scores, which aids in the interpretability of the model. The machine learning service is implemented as a Flask app and follows an event-driven approach, retraining the model every hour to incorporate the latest price data. The training and inference processes are communicated via a RabbitMQ queue to the backend service.

1. **Model Architecture**
The machine learning model is based on the transformer encoder architecture, which has proven to be highly effective for sequence modeling tasks. The transformer architecture utilizes self-attention mechanisms to capture dependencies between different positions in the input sequence. The inclusion of positional encoding and embeddings allows the model to understand the temporal and price-related aspects of the data.

    2.1 *Input Representation*
The input to the model consists of two components: price and timestep. The price represents the historical BTC/USD price at each timestep, while the timestep indicates the relative ordering of the data points. Both price and timestep are encoded using embeddings to provide meaningful representations to the model.



    2.2 *Transformer Encoder*
The model employs a multihead attention mechanism with 8 heads to capture different types of dependencies in the input data. Each attention head attends to different parts of the input sequence, enabling the model to extract diverse and informative features. The multihead attention is followed by feed-forward layers to further process the attended information.



    2.3 *Encoder Blocks*
To enhance the interpretability of the model, we utilize 5 encoder blocks. Each encoder block consists of a multihead attention layer, layer normalization, feed-forward layers, and residual connections. This design choice allows for a deeper understanding of the attention scores, enabling insights into the specific features or time periods that influence the model's predictions.

3. **Machine Learning Service**
The machine learning service is implemented as a Flask app, providing a robust and scalable infrastructure for handling prediction requests. The service follows an event-driven approach, triggered by an hourly event to retrieve the latest price data. Upon receiving new data, the model is retrained using the updated dataset. The training process incorporates a RabbitMQ queue, where messages containing the training data are sent to the backend service.

4. **Results and Interpretability**
Through the use of the transformer encoder architecture and attention mechanisms, the model is capable of capturing important temporal and price-related patterns in the data. The multihead attention with 8 heads allows for a comprehensive analysis of the input sequence, providing valuable interpretability. The interpretability of the model is further enhanced by utilizing 5 encoder blocks. By examining the attention scores, we can gain insights into the specific aspects of the data that the model focuses on during inference. This enables users to understand the driving factors behind the model's predictions, aiding decision-making processes.

5. **Challenges**
The major challenge so far is the training time. Since the model needs to retrain every hour and make a prediction before the market moves by a reasonable amount. The second major problem is that the paid api from which we get our hourly data sometimes goes down and this can affect the training of the model. The model’s architecture is simple for now and there is room for improvement in terms of number of heads and number of layers. We are not implementing any data engineering pipeline and doing all the processing in the python code, for now this is not an issue since we do not have billions of data, but when we include news and other data sources then we would need a big data technology.

{{< hint danger >}}

**Feedback:**   
So does it predict the future price movements based on the history? It would be nice to see more elaborate explanations here.
Is this algorithm actually works? Have you done any backtests?  
{{< /hint >}}

## **Frontend**
1. **Introduction**
The frontend is a mobile app written in Flutter. We decided to use clean architecture, since this will allow us to scale better in the future. We are using bloc for our state management, go_router for routing and dio+retrofit to handle network requests. 
2. **UI Design**
Below is a prototype design of our application, which was created using Figma: - [Figma Link](https://www.figma.com/file/IXQhGgoVPjEqvQopgBl0FD/Capstone-Project?type=design&node-id=0-1&t=ioboFNrxKdD4CYdt-0)
{{< hint danger >}}

**Feedback:**   
Nice figma design!  
{{< /hint >}}


3. **Prototype Features**
The features are pretty straightforward, for the MVP we have only the authentication and the actual screen that shows the prediction part. Also, we are going to implement push notifications using Firebase Cloud Messaging to make sure that the traders are notified as soon as the new signal comes out.

{{< hint danger >}}
**Feedback:**   
How much long does the signal holds? Which ticks are you using to make predictions? I suppose this is hourly data, right? Would it be possible that high-frequency traders will outrun you with the signal?
{{< /hint >}}


4. **What is implemented**
At this stage, we have a functional version of the application design. As development progresses, we are making changes to enhance the user experience. Currently, our primary focus lies in establishing the application's architecture, work with the application’s backend. We have successfully completed the authentication screens, and our objective is to finalize the design layout by the end of the next iteration.

{{< hint danger >}}

**Feedback:**   
It is still somewhat cryptic language - do you have an app implemented of only design in figma?   
{{< /hint >}}


1. **Challenges** 
So far we didn't meet any substantial challenges on the frontend. The only problem we had was with the navigation in the app, but this problem was quickly resolved.

## **Backend**
1. **Service Architecture**
We are deploying project on Yandex Cloud, which provides virtual machines and network for inner services. So this network has public ip address, on which API Gateway node will be placed in. API Gateway purpose is to maintain user interactions: auth (jwt), listing models, subscribtions, etc. In this private network will be placed persistent storage (database, etc) where we will collect user information, subscribtion records and metrics. And, of course, models will be placed in private network. So each node can easily make request to another within the network, but out of networks peers will see only API Gateway node with public ip. Architecture will be described in helm/k8s files and automaticaly rollout with kubernetes

{{< hint danger >}}

**Feedback:**   
Good  
{{< /hint >}}


2. **API Gateway Architecture**
We choose Fastify framework as it provides modern approaches to build backed services as well as openapi plugins (swagger) in the box. It will provide several endpoints to interact with.

3. **Database**
We choose postgres for storing users and subscriptions.

4. **Challenges**
Due to lack of experience it is extremely hard to build infrastructure. So another major problem is to organize all services with kubernetes.
Also Backend developer faced problems with Fastify. It is modern one and has an excellent documentation, yet not enough real world examples, which with lack of experience makes development slower.

{{< hint danger >}}

**Feedback:**   
So backend also doesn't work? I am struggling to understand what is already build and functioning and what is in the implementation stage. Please, consider using more precise language to describe actual state of things.     
{{< /hint >}}



## **Next Steps**
Next week, we are going to finish with the UI part on the frontend and start implementing the data and domain layers of the app. Also, we are expecting to have authentication working. Furthermore, the ML part is constantly improving, so most likely, the model will have a better accuracy and the training time will be reduced.

{{< hint danger >}}

**Feedback:**   
It seems you have some progress but it is hard for me to understand and quantify this progress, due to the way this report was written. Please use the following structure - describe what was done exactly this past week. What are the challenges and how are you planning to overcome them. 
Also, use the chance to iterate on your reports too - this are an integral part of the project. Consider this as an opportunity to train your skills in project management. 
Overall 3/5 for the week!
{{< /hint >}}


# **Week #4**

## **External Feedback**
Our users gave us useful feedback on our app. Here is the list of cons that they found:
- Navigation bar seems to be excessive, since there are only two buttons. You may have to fix it via deleting it or adding extra navigation buttons. (We fixed this in our app immediately)
- I find forex pair prediction quite useless for me. I would be glad to see crypto prediction. 
- It would be much cooler if you add light theme. But it’s an optional feature.
- It is a little bit hard for me to navigate in your app. Can you add screen hints on first run of the application?
- I would like to see my profit from following your buying tips. In other words, see the price changing of the shares I bought.<br>
  
Also our users pointed out the following pros in our app:
- I love the minimalistic elegant design. Dark mode is my favourite.
- Stock bar chart visually helps me a lot.
- As the representative of the target audience, so far I like the implementation of the app.
- What I really like about your app is that it collects the real time stock information and makes frequent predictions based on it.

## **Testing**
We haven't implemented any testing on the frontend yet, but we are following the clean architecture, so our app would be easily testable in the future. On the backend, there is only one thing we did to simplify testing, and it is OpenAPI. With OpenAPI it’s much easier to work with endpoints. So everyone can see the schema of endpoints and validate request / response. 

## **Iteration**
{{< hint danger >}}

**Feedback:**   
SO no iteration on the basis of feedback you have received?   
{{< /hint >}}

### **ML Model**
This week we didn't implement the model directly, but we worked on the infrastructure of the ML-Backend connection. A cronjob that starts the training at every oclock was implemented, as well as the dockerization of the application. Next week, sending the signal to the backend through Kafka will be implemented.

### **Flutter**
This week was the final one for creating the design of our application. First of all, edits were made to the application's appearance. It was decided to abandon the bottom navigation and instead remove the settings button from the header of the application. This leads to a more restrained appearance since unnecessary elements do not distract the user's attention.
Additionally, during a small study, it was decided to use the CandleSticks library to draw charts of currency quote changes. Such a chart is more understandable for those engaged in trading. Its appearance closely resembles similar charts from the popular Binance platform. This solution reduces the entry threshold for new users of our application.
The following screens were added this week: [Screens Link.](https://docs.google.com/document/d/1tIHRcuAdRDGARpaLYMHx7be-KM58D6L9iwXr5Xp4ihs/edit?usp=sharing)
Now, our further work will focus on adding the main features: user authentication, drawing real-time graphs, and communicating with the backend to receive predictions from the neural network.
## **Iteration**
{{< hint danger >}}

**Feedback:**   
Good! Nice to see the app taking shape!   
{{< /hint >}}


### **Backend**
As Backend && DevOps developer I setup a postgres container and a migrations tool (node-pg-migration). Also provided /create-user and /list-users for database endpoints. For now we can run it only locally, however we will deploy it soon. <br>
For the backend framework I have chosen Fastify, which is the edge of the novice and progressive ideas. Yet I am faced with a lack of examples of the codebase of this framework. Paradigms of Fastify strongly diverge from the more popular Express.
## **Iteration**
{{< hint danger >}}

**Feedback:**   
This is already 4th week. Progress for the week is weak and report is not very impressive either. 
You have to speed up and make sure that all parts should be working before the finals.
I think you'll be able to get to the MVP but make sure to make a final sprints a little more intense. 
You have a great team and a good idea, so do it as planned and not compromise for less.  

Overall, 3.5/5 for the week.
{{< /hint >}}


# **Week #5**

## **Progress**

### **Backend**
All endpoints provided. Backend is reading the message queue from ML services and the frontend can get the latest predictions.

### **Frontend**
As planned, this week has been dedicated to connecting the backend and frontend parts of our application. Currently, several issues have been resolved:

Real-time graph rendering has been added. The data is sourced from Binance, which enables access to accurate information at any time.

User authorization functionality has been implemented. This will eventually allow for the creation of a personalized user feed, where users can save currency pairs of interest on the main screen, view the history of currency changes, and share a list of user preferences.

Next week, we will finalize getting the predictions from the backend and test everything to make sure that everything works.


### **ML Model**
Objective:
The objective of this weekly report is to provide an overview of the progress and updates regarding the machine learning service implemented in the application. This report aims to highlight the usage of multi-head attention and time encoding to generate signals for the crypto and forex market, specifically focusing on the BTCUSD pair on a 1-hour timeframe. Additionally, it will cover the scheduling, data retrieval, training pipeline, and deployment aspects of the machine learning service.

1. Development Overview:
During this week, significant advancements have been made in the machine learning service of the application. The following key areas were addressed:

   a. Multi-Head Attention and Time Encoding:
      The machine learning model has been successfully implemented using multi-head attention and time encoding techniques. These techniques contribute to the model's ability to capture complex patterns and temporal dependencies in the market data, allowing for more accurate and robust signal predictions.

   b. Data Retrieval:
      A scheduler has been integrated into the system, ensuring that hourly data for the BTCUSD pair is pulled from the Alpha Vantage APIs. This ensures that the most recent and relevant data is used for training and prediction purposes. The scheduler runs every hour, precisely on the hour, to maintain consistency and timeliness of the data.

   c. Training Pipeline:
      The training pipeline has been set up to process the retrieved hourly data. This pipeline involves data preprocessing, feature engineering, model training, and evaluation. The pipeline is designed to handle large volumes of data efficiently while maintaining the integrity and quality of the training process.

   d. Prediction and RabbitMQ Integration:
      Once the model is trained, the predictions for each hour are sent through a RabbitMQ queue. This integration ensures seamless communication between the machine learning service and other components of the application. The RabbitMQ queue acts as a reliable and scalable messaging system, facilitating the distribution of predictions to the relevant parties.

   e. Dockerization and Deployment:
      The machine learning service has been successfully dockerized, ensuring easy deployment and scalability. The Docker Compose file has been written to orchestrate the RabbitMQ service and the machine learning service, providing a streamlined and efficient infrastructure for the application. The Docker images have been transferred to the backend department for further deployment.

1. Challenges and Mitigation:
During the development process, a few challenges were encountered. These challenges were promptly addressed with the following mitigation strategies:

   a. Data Consistency:
     Implementation of error handling to handle cases when the alpha vantage API was unavailable.

1. Next Steps:
Looking ahead, the following tasks are planned for the upcoming weeks:

   a. Expand Signal Coverage:
      Expand the coverage of signals to additional currency pairs and timeframes. This will involve extending the existing model and training it on additional datasets to provide a wider range of signals for users.

   b. Performance Evaluation:
      Conduct comprehensive performance evaluations of the machine learning model to ensure its accuracy and reliability. Fine-tune the model parameters and architecture, if necessary, to optimize its performance.

   c. Backend Deployment:
      Collaborate with the backend department to facilitate the deployment of the Dockerized machine learning service. Ensure seamless integration with other components of the application and conduct thorough testing to ensure proper functionality in a production environment.

1. Conclusion:
In summary, significant progress has been made in the development of the machine learning service for the application.

The implementation of multi-head attention and time encoding techniques, along with the integration of data retrieval, training pipeline, prediction, and RabbitMQ communication, has resulted in a robust and scalable machine learning service. The Dockerization of the service further enhances its deployment and scalability. Looking ahead, the focus will be on expanding signal coverage, conducting performance evaluations, and ensuring that the backend connection is written robustly.

## **Feedback**
We have collected a small amount of feedback from the people who are somewhat interested in trading, and these are the results of the survey: https://docs.google.com/forms/d/1zeGz3OToET72KEXrfhcWx6o9Lwf3bdlXqS1AIGdmZgY/viewanalytics

{{< hint danger >}}
Alright, report looks good. Liked the survey data visualizations. Noted the final presentation on the top of the file.
5 the week! And good luck with the project and the final presentation! You have accomplished a lot! Cheers 
{{< /hint >}}