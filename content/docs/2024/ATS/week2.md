# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

In order to successfully implement the project and fulfill all of our goals, our team decided to utilize the extensive technology stack that is required to write a fast backend, a supported AI system, and a lightweight frontend. We want to build an efficient system that can handle large amounts of data in real time, perform forecasting and prediction of cryptocurrency market behavior and trade with subsequent collection and demonstration of statics

The mainstone of our project is the **Python programming language**. The choice of this language is based on the following factors:

1. **Extensive Libraries and Frameworks** : Python boasts a rich ecosystem of libraries and frameworks for data analysis, machine learning, and AI-driven prediction models. It enable efficient development and deployment of complex algorithms crucial for forecasting cryptocurrency market behavior.
2. **Ease of Integration** : Python's versatility and ease of integration with other technologies make it an ideal choice for building a comprehensive system. It seamlessly integrates with databases, web services, and various third-party APIs, allowing for smooth data collection, processing, and presentation.
3. **Rapid Prototyping and Development** : Python's simple and readable syntax facilitates rapid prototyping and development. This allows our team to quickly iterate on ideas, test hypotheses, and deploy features, significantly reducing the time to market for our solutions.

We plan to use the following **python libraries and frameworks** in our project:

* **Pandas, NumPy, Matplotlib, TensorFlow, PyTorch, Keras**  - ***Pandas* and** ***NumPy* are fundamental for data manipulation and numerical operations.** ***Matplotlib* is essential for creating visualizations.** ***TensorFlow* ,** ***PyTorch* , and** **Keras** provide powerful tools for building and training machine learning and deep learning models.
* **Quantconnect, TA-Lib, Zipline, Backtrader, PyAlgoTrade** - These libraries and frameworks are specialized for financial and trading analytics. ***Quantconnect* offers a cloud-based algorithmic trading platform.** ***TA-Lib* provides technical analysis of financial market data. *Zipline* , *Backtrader* , and** ***PyAlgoTrade*** support backtesting trading algorithms.
* **Fast API, ByBit API** - ***FastAPI* is used for creating high-performance APIs, essential for our backend.** **ByBit API** allows us to interact with the binance cryptocurrency exchange for real-time trading operations.
* **PyMongo** - This library provides tools for working with MongoDB, enabling efficient storage and retrieval of our application's data.

An important component of our project is interactive statistics, which will be available to users in the web interface and will be updated in real time. This web interface will include general statistics on bot operations, count losses and profits, as well as comparative analysis between AI and trade algorithms. To implement this component, we decided to use the following technology setup:

1. **Vue.js**

* **Component-Based Architecture**: Vue.js allows you to build modular and reusable components, which is ideal for creating interactive dashboards and graphs.
* **Ease of Integration**: Vue.js can be easily integrated with other libraries or existing projects. This makes it a flexible choice for adding complex visualizations.
* **Reactive Data Binding**: Vue.js provides a reactive data-binding system that ensures your UI is always in sync with your data, which is crucial for dynamic statistics and interactive elements.

2. **D3.js**

* **Powerful Visualization Library**: D3.js is a powerful library for creating complex and highly customizable data visualizations. It’s perfect for building interactive graphs and dashboards.
* **Data-Driven Documents**: D3.js manipulates the Document Object Model (DOM) based on data, allowing you to create dynamic and responsive visualizations.

3. **Chart.js**

* **Simplicity and Ease of Use**: Chart.js is a simpler alternative to D3.js for creating basic charts and graphs. It’s easy to use and integrates well with Vue.js.
* **Variety of Chart Types**: Chart.js supports various chart types, such as line, bar, radar, pie, and bubble charts, which can be used to display different types of statistics.

To save information regarding the results of operations performed by the bot during trading, we decided to use **MongoDB** database because:

* **Document-Oriented Storage**: MongoDB stores data in flexible, JSON-like documents, which is advantageous for logging diverse trading operations without a fixed schema.
* **High Write Throughput**: MongoDB is designed to handle high volumes of concurrent writes, making it suitable for logging real-time trading activities.
* **Scalability and Flexibility**: MongoDB is highly scalable and can distribute data across multiple servers, ensuring quick access and storage even under heavy loads.
* **Indexing and Aggregation** : It offers powerful indexing and aggregation capabilities, enabling efficient querying and real-time data analysis.

As it was said earlier we will use **ByBit API** to communicate with crypto exchange market due to several features:

1. **User-Friendly Interface and Documentation**:

* ByBit provides a user-friendly API interface and comprehensive documentation, making it easier for developers to implement and integrate with their trading systems.
* The API is well-structured and designed for ease of use, which can reduce development time and complexity.

2. **High-Performance and Low Latency**:

* ByBit’s API is designed for high performance and low latency, ensuring fast execution of trades and minimal delays.
* This is crucial for high-frequency trading and algorithmic trading strategies where speed is a significant factor.

3. **Demo Account Option**:

* ByBit offers a demo account (also known as a testnet), allowing you to test trading strategies and API integrations in a risk-free environment.
* This feature is invaluable for developers to validate their trading algorithms and make necessary adjustments before deploying them in a live trading environment on Binance.

For system prototyping and UX/UI templates creation, we will use the **Figma**.

For project deployment we will use GitHub CI|CD piplines throw GitHub actions and possibly rent a dedicated server, where we will deploy ML system component via **Docker**.

To conclude, our tech stack is the following:

1. Backend and AI
   * Python
   * ByBit API
   * Fast API
   * MongoDB
2. Frontend
   * Vue.js
   * D3.js
   * Chart.js
   * Figma
3. CI/CD — GitHub Actions, Docker

### **Architecture Design**

![architecture_design](/2024/ATS/architecture.png)

Based on the above scheme, our project includes three key components.

**Component Breakdown**:

**The first component** is responsible for the direct implementation of the web interface. This is the business card of the project, where we will publish important information about updates and rules of our open sourse business model, as well as summarize comparative statistics on the evaluation of trading efficiency of AI and classical trading algorithms through interactive dashboards, tables and graphs.

**The next component** is a multifunctional system that performs various trading operations (buying, selling, setting orders, etc.) on the registered business account via the API, as well as monitors dynamically changing data of the cryptocurrency exchange and implements several trading strategies that are set through classical trading algorithms methodology.

Finally **the third component** is autonomous MLops system centered on the Long Short-Term Memory network (LSTM ) model, which predicts the future price of the selected cryptocurrency for the next 15 seconds time interval based on incoming real-time information. Afterward, the predicted information is transferred to the automated trading system through the API interface, where the trading decision-making process is executed based on the received data.

In conclusion, our system conducts parallel trading based on AI predictions and classical trading algorithms. After the active trading phase, data is collected and analyzed to summarize statistics, determining which strategies were more profitable and identifying patterns. This information is then displayed to the user through a dynamically updating web interface.

**Data Management**:

Our system will receive most of the information in real-time, both for the AI system and the trading algorithm components. Consequently, we don't need to develop a complex data management system, as the incoming information is only necessary during the trade decision-making stage.

We will save logs containing all actions, operations, and predicted information from our automated system to collect statistical data and perform subsequent analysis. For this purpose, we plan to use a simple MongoDB database.

**User Interface (UI) Design**:

At this stage of our project, developing and designing the UX/UI interfacing is not a key because the web interface is just a comlex dashboard and has not a high priority like other components of system. At this point in time, we have small sketches and a pool of references that we plan to use for future design of web interface.

Link to the sketch: [Click on me](https://www.figma.com/design/01rc3K1AUBfTan3Pw3I8eI/ATS-Mockup?node-id=0-1&t=C0nZIdFbW8QMaxv7-0 "Figma")

Link to the references: [Click on me](https://www.figma.com/design/GTVD1tq3Me2PjDWXIsdtHX/Purity-UI-Dashboard---Chakra-UI-Dashboard-(Community)?node-id=1516-368&t=MEM1y9foTgSxVXSo-1 "Figma"), [Click on me](https://www.figma.com/design/g0UYQvB52eVQtoigtuH1h7/Trading-Dashboard-(Community)?node-id=0-1&t=A2lO4aZ9l2nPMNU1-1), [Click on me](https://www.figma.com/design/pSSExxJlRNUFLC9P8cElp9/CryptoCrack---Cryptocurrency-trading-dashboard-UI-design-(Community)?node-id=0-1&t=LDPILRIq6QPx5Esi-1)

**Integration and APIs**:

In our system we use ByBit API. In our system, we use the ByBit API. This API provides a robust and reliable interface for accessing real-time market data, executing trades, and managing account information. Its advantages include high-speed data transmission, comprehensive documentation, and strong security features, making it well-suited for our project. By utilizing the ByBit API, we can ensure that our automated trading system operates efficiently and effectively, with minimal latency and maximum reliability. In addition, we will build our own API interface based on the Rest API framework to exchange data between component №2 and component №3.

**Scalability and Performance**:

Our approach involves constructing a modular system where each component is segmented into independent modules, facilitating efficient replacement and maintenance. Emphasizing the speed of information processing, we will harness advanced libraries and leverage a fast API interface. This strategy aims to enable rapid trading decision-making and timely responses to the dynamically fluctuating cryptocurrency market conditions.

**Security and Privacy**:

ByBit provides a secure and encrypted method for authenticating access to exchange accounts, ensuring robust security measures are in place. Users can securely interact with their accounts through authentication protocols that comply with industry standards, safeguarding sensitive information during data exchanges. Furthermore, ByBit offers a demo/sandbox mode, allowing users to test trading strategies without real-money transactions, which minimizes risks during development and testing phases. As the project is closed and serves an educational and enlightenment purpose, we do not handle user data directly. Therefore, the security standards of the system are simplified accordingly.

**Error Handling and Resilience**:

We are planning to build an efficient CI/CD pipline, which will include a test module based on the pytest framework to check the accuracy of the Mlops system and the system for making automated trading decisions based on trade algorithms.

Also, we will introduce a system of limits on the demo account to catch situations when the algorimt and predictions of the AI go beyond the results predicted by us.

**Deployment and DevOps**:

For deployment and continuous integration/continuous deployment (CI/CD), we utilize GitHub Actions to automate our build, test, and deployment pipelines. This ensures that our codebase is always in a deployable state, and any changes are automatically tested and deployed to our staging and production environments. We use Docker to containerize our applications, providing a consistent environment across development, testing, and production stages. Our deployment strategy includes using dedicated servers or cloud-based solutions to host our services, with load balancing and monitoring tools to manage resource allocation and system health. This DevOps approach allows for efficient and reliable updates, enabling us to quickly roll out new features and improvements while maintaining system stability.

### **Week 2 questionnaire:**

1) **Tech Stack Resources:** We utilize the textbook "**The Stock Market" authored by N.I. Berzone, A. Buyanova, M.A. Kozhevnikov, and A.V. Chalenko** as a foundational resource for studying and implementing trading algorithms. As for the methodology for predicting stock exchange behavior using AI technology, we conduct a detailed analysis of various articles that are collected in a literature review **"Artificial intelligence techniques in financial trading: A systematic literature review"** **authored by** **Fatima** **Dakalbab**, **Manar Abu** **Talib,** **Qassim** **Nasir** *and etc.*
2) **Mentorship Support:** Our project team does not have a mentor, but we are actively searching. We plan to seek help from the IU AI laboratory for advice on building an effective MLops system, and also hold a meeting with Zamira to discuss the details of the project and get consultation.
3) **Exploring Alternative Resources:** **YouTube channels:** [Azzrael Code](https://www.youtube.com/@azzraelcode), [ ritvikmath](https://www.youtube.com/@ritvikmath/videos). **Habr article** [Time series bootstrap](https://habr.com/ru/companies/X5Tech/articles/814579/). **Binance API** [documentation](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Kline-Candlestick-Data) and documentations fo **Quantconnect, TA-Lib, Zipline, Backtrader, PyAlgoTrade** python libraries.
4) **Identifying Knowledge Gaps:** In current stage of project we are faced with two difficult tasks: 1) Building a fast and efficient system for processing information in real time and implementing a system for making optimal trading decisions 2) Using cutting-edge technologies in the field of AI to predict the behavior of the cryptocurrency market. We do not have sufficient experience in such areas of knowledge as trading algorithms, setting up an MLops system and writing a fast backend system with minimal delays. By quickly developing and testing hypotheses, we can effectively select working ideas and implement them in practice, and through detailed study of the scientific environment and consultation with specialists from UI, we will be able to close knowledge gaps. You can get acquainted with the division of responsibilities and tech stack in our team below in the paragraph **Team responsibilities allocation.**
5) **Engaging with the Tech Community:** We actively engaged in biggest AI Russia community [ods.ai](https://ods.ai), because we need to get the latest knowledge and instruments for building effective AI systems . Also we subscribe on the Habr writers and telegram channels, which cover the topics of trading in the cryptocurrency market using of trading algorithms. We don't have means to engage experts into critical tech stack problems through professional networks.
6) **Learning Objectives:** This week, our team is focused on achieving specific learning objectives related to our chosen tech stack. Our primary goals include mastering the implementation of real-time data processing within our system architecture, enhancing proficiency in developing and deploying a fast backend system with minimal latency, and gaining deeper insights into utilizing AI technologies for predicting cryptocurrency market behavior. To achieve these objectives, we are actively engaging in hands-on practice sessions where we implement real-time data processing techniques using Python libraries such as Pandas and NumPy. Additionally, we are dedicating time to reviewing relevant documentation and articles that provide insights into building efficient backend systems and integrating AI frameworks like TensorFlow and PyTorch for market prediction. Collaborating with peers in online communities such as ODS AI and following educational content from YouTube channels like Azzrael Code and ritvikmath further supplements our learning process. These efforts are aimed at deepening our understanding and proficiency in critical areas of our tech stack, ensuring that we can effectively address current project challenges and meet our objectives.
7) **Sharing Knowledge with Peers**: We hold one and a half hour meetings twice a week to discuss ideas, exchange experiences and create a common vision for the project.
8) **Leveraging AI:** We are now actively using various AI tools to speed up the efficiency of our work. For example, we use Chat GPT and Phind to actively search various information, generate ideas and find already implemented solutions, Git Hub copylot for writing and debugging source code.

### **Team responsibilities allocation**

| Team Member        | Track                           | Responsibilities                                                                                                                                                       |
| ------------------ | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ivan Golov (Lead)  | Team Lead & Project manager     | setting up and supervising the development and maintenance of a git project, organizing team work, building a strategy for project implementation                      |
| Daniil Abrosimov   | ML engineer                     | building and maintaining an MLops system of pject                                                                                                                      |
| Dmitriy Nekrasov   | Data science engineer           | thinking through and testing various hypotheses regarding the use of AI to predict market behavior                                                                     |
| Andrey Pavlov      | Backend developer               | studying trading methodology and implementing trade algorithms in practice                                                                                             |
| Shamil Kashapov    | Backend developer               | writing the backend of an automated trading system, setting up and working with the database, as well as writing an API interface for communicating with component №3 |
| Bulat Latypov      | Backend developer               | studying trading methodology and implementing trade algorithms in practice                                                                                             |
| Yaroslav Prudnikov | Frontend developer and Designer | web interface UX/UI design and its subsequent implementation using Vue.js, D3.js and Chart.js                                                                       |

### **Weekly Progress Report**

**Our team did:**

* Held two one and a half hour meeting.
* Designed the technical architecture of the project and approved the technical stack.
* Distributed roles and assigned areas of responsibility.
* We prepared a git hub repository and approved the convention for maintaining git and writing commits.
* Planned the next week and set deadlines.

### **Challenges & Solutions**

1) Difficulty in organizing a meeting so that all team members are present - conducting hybrid meetings (online and offline) + maintaining documentation during meetings.
2) Insufficient understanding of the trading domain - studying articles, watching YouTube and searching for implemented solutions.
3) Lack of UX/UI design experience - search for templates and view learning courses.

### **Conclusions & Next Steps**

At this stage of the project, we have achieved a common vision for each team member, approved the system architecture and technical stack, and also prepared everything necessary for the start of development phase. 

**Our next steps will be:**

1. Creation of a working prototype of the system, when AI and trading algorithms will be able to show some result and the system will perform the first operations on the stock exchange.
2. We will design and implement web interface design as a project in Figma.
3. We will continue to delve into the theory of algorithmic trading and the use of AI to predict market behavior.
