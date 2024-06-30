# **Week #3**

# **Developing the first prototype, creating the priority list**

## Project week focus & Approach 

The overarching goal of our project is to develop an effective predictive-algorithmic trading system. This week, we specifically focused on testing the profitability of our trading ideas and beginning the practical implementation of the technical infrastructure. This work is crucial as it lays the foundation for a robust and efficient trading platform, ensuring that our algorithms and infrastructure are both scalable and maintainable.

1. **Technical Infrastructure** 
   * Workflow conventions such as code versioning strategy in github & style of commits will be established to streamline the development process.
   * Build three github repositories (added rules to branches, give rights to participants) to efficiently and quickly develop each component of the project separately. 
   * Start thinking about CI|CD and MLops for implementation in the coming weeks.
2. **Backend Development**
   * Focus on the implementation of the main skeleton of the project and realisation of the first test operations on the stock cryptocurrency exchange. 
   * Implement the first basic trade algorithms and apply them in practice.
3. **Frontend Development**
   * Our main focus this week will be to intesively develop the UX|UI design of the web interface and create the first interactive prototype.
   * Implementation of the web interface is not a priority task for this week.
4. **Data Management**
    * Make a final decision on whether to choose MongoDB or SQLlite to create a logging system. 
5. **Prototype Testing**
   * Test the API interfaces of the cryptocurrency exchange in the spectre of realisation of buy and sell operations.
   * Test the first version of the predictive model and interpret the  obtained results.
   * Test of trading algorithms on practise & evaluation of their efficiency.

Throughout the week, we focused on maintaining consistent communication and teamwork. We held daily stand-up meetings to keep everyone informed about their tasks and progress. These meetings were crucial for aligning the backend, frontend & design and ML development efforts.

## **Progress Report**

### ML component:

Done:

- [X] Defined the repository structure
- [X] Configured the primary version control interface for the data
- [X] Implemented data collector programs for training and real-time use
- [X] Implemented initial preprocessing of the data
- [X] Tested several hypotheses related to the technical implementation of the product
- [X] Defined metrics for model evaluation (profit, number of transactions, winrate).

Key tasks for next week:

- Add cloud storage of training data (for version control)
- Customise data transformation pipelines (to make it easier for the model to identify patterns + improve interpretability).
- Implement reinforcement learning model prototype/Proof of Concept (most likely to be Proximal Policy Optimisation)

### Backend component:

Done:

- [X] Defined the techical structure of the project (creation of interfaces and basic modules): maintainable, easily addable and productive system
- [X] Implemented algorithms:
    * SMA (Simple Moving Average) and EMA (Exponential Moving Average) - look at the moving average of buy/sell picks. They are essential tools for analyzing price trends, serving as the baseline for our decision-making process.
    * RSI (Relative Strength Index) algorithm assesses whether a coin is oversold or overbought, using a scale from 0 to 100 to inform trading actions. 
    * The MACD (Moving Average Convergence Divergence) evaluates the interaction between two moving averages and signals actions when they cross.
    * Bollinger Bands analyze price volatility by considering moving averages and standard deviations, guiding our trading decisions based on price deviations from these bands.
- [X] Connected the API of the exchange
- [X] Tested the API interface (buying, selling)
- [X] Added logging
- [X] Refused from Mongo DB in favour of SQLlite DB (as it is natively supported by python and is more lightweight than MongoDB).

Key tasks for next week:

- Merge the branches & resolve conflicts 
- Add class methods to decompose the system into maintanable & atomic parts
- Up the SQLlite Database & save logs to it
- Connect trade algorithms with API interface 

### Frontend & Design components:

Done:

* [X] Designed Visual style (palette, fonts, icons)
* [X] Implemented interactive prototype in Figma with basic screens [https://www.figma.com/proto/01rc3K1AUBfTan3Pw3I8eI/ATS-Mockup?node-id=0-1&amp;t=bK4O4j9u07d5CLlh-1](https://www.figma.com/proto/01rc3K1AUBfTan3Pw3I8eI/ATS-Mockup?node-id=0-1&t=bK4O4j9u07d5CLlh-1)

Key tasks for next week:

* Design algorithm information screens (efficiency, comparison, etc.) and finalise dashboard
* Implemet Filters for the transaction history screen

These results align with our objectives by laying the groundwork for our trading system and providing initial insights into its performance. The successful implementation of algorithms and the API connection is crucial for the next stages of our project.

### Challenges & Solutions

- The predictive model was underfitting on the train data - we have extended the horizon of reviewing information on changes on the stock exchange to 15 seconds. 
- Failed to execute the test of trade algorithms on the stock exchange - need to customise the API interface and dive more into the theory of algorithmic trading.
- Unstructured process of developing and tasks execution - reorganization of project planning system using Linear app. 

These solutions are aimed at overcoming obstacles and ensuring smoother progress in the upcoming weeks.

### Conclusions
In Week 3, we successfully initiated the development of our first prototype and created a priority list to guide our efforts. We established key workflow conventions and set up GitHub repositories to streamline the development process. Both backend and frontend components saw significant progress: the backend implemented core trade algorithms and connected with the exchange API, while the frontend developed an interactive prototype in Figma. We also defined metrics for model evaluation and implemented initial data processing steps for the ML component. Despite facing challenges such as underfitting of the predictive model and issues with the trading algorithm tests, we identified solutions and outlined key tasks for the upcoming week to further refine our prototype and development processes.