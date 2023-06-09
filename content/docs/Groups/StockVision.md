# **Stock Vision** 

We are doing a project called Stock Vision. The aim of this project is to develop an ML tool for traders that provides additional analysis and predictions for stock market / currency pair movements.

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

**Feedback:** 

{{< hint danger >}}
Hi, your feedback rocks! You and your team did a great job!  
However, your feedback can be even better if you would do:   
1)...  
2)...  
3)...  
{{< /hint >}}