---
title: "Week #3"
---

# **Week #3**
#### Prototype Features

This week, we made significant progress in developing the **SayNoMore** prototype. Our primary user interface is through a Telegram Bot, designed to assist users with their travel planning. Here’s what we have accomplished:

1. **Telegram Bot Interface**:
   - **Proof of Concept**: We have developed a basic Telegram bot that can handle user messages and perform core functions essential for travel planning.
   - **Basic Functionality**: The bot can process user requests, ask for additional information if necessary, and return several travel routes that fit within the user’s specified budget.

2. **RequestAnalyzer Module**:
   - **User Input Processing**: The prototype can parse and understand user inputs, extracting key travel details such as destination, departure city, dates, and budget.
   - **Multi-step Interaction Handling**: The system interacts with users iteratively, prompting for more information when initial inputs are incomplete or ambiguous.
   - **Validation and Verification**: This module ensures the extracted details are valid and accurate, such as checking for valid cities and realistic dates.

3. **API Collector Module**:
   - **Flight Data Retrieval**: The bot can fetch the cheapest and most relevant flight options using the Aviasales API.
   - **Hotel Data Retrieval**: It also searches for hotel availability and pricing based on user-provided criteria.
   - **Data Formatting**: Retrieved data is standardized and formatted for easy presentation to the user, ensuring consistency and clarity.

4. **Integration of All Modules**:
   - We have successfully integrated the RequestAnalyzer, API Collector, and Telegram Bot Interface into a cohesive system.
   - The bot now processes user requests, retrieves relevant travel data, and provides recommendations based on the user's budget and preferences.

---

#### User Interface

The current UI is a Telegram Bot that facilitates user interaction for travel planning. Key screens and interactions include:

1. **Welcome Screen**:
   - The bot greets users with an introduction and overview of its capabilities.
2. **User Input Collection**:
   - The bot prompts users to provide travel details such as destination, departure city, and travel dates.
3. **Dynamic Querying**:
   - If initial information is incomplete, the bot interacts dynamically to gather additional necessary details.
4. **Travel Recommendations**:
   - After processing the request, the bot provides several travel routes that fit the user’s budget and preferences, including flights and hotel options.
![Demo](https://hackmd.io/_uploads/SJxS77QL0.png)

These interactions ensure that users can plan their travel efficiently and receive tailored recommendations.

---

### Challenges and Solutions

1. **Local LLM is GPU Expensive and Hard to Deploy**:
   - **Challenge**: Running the local LLaMA model requires significant GPU resources and presents challenges in deployment, making it difficult to scale and manage.
   - **Solution**: We are considering alternatives such as utilizing cloud-based LLM services or REST APIs for LLM tasks. This will reduce the burden on local resources and simplify deployment, ensuring scalability and easier management.

2. **API Data is Limited by Aviasales Cache**:
   - **Challenge**: The current API data from Aviasales is limited to their cache, which may not cover all possible user requests in real-time.
   - **Solution**: We plan to develop a functional prototype demonstrating our bot's capabilities. With this prototype, we will approach Aviasales directly to negotiate access to their full API, which will allow us to handle a broader range of user requests with up-to-date and comprehensive data.

---

#### Next Steps

As we move forward, our focus will be on enhancing the bot’s capabilities and refining its functionalities. Here’s what we plan to work on next:

1. **Feature Enhancements**:
   - **Advanced User Interactions**: Improve the bot’s ability to handle more complex user queries and provide richer responses.
   - **Expanded Data Retrieval**: Integrate additional APIs to offer a wider range of travel options, including alternative accommodations and local attractions.
   - **Budget Management**: Enhance budget handling capabilities to provide more tailored and cost-effective travel recommendations.

2. **User Experience Improvements**:
   - **Interactive Feedback**: Implement more interactive and user-friendly feedback mechanisms to keep users engaged and informed.
   - **Error Handling**: Improve the bot’s ability to gracefully handle errors and provide helpful suggestions when issues arise.

3. **Interface Development**:
   - **Web and Mobile Interfaces**: Begin the development of web and mobile platforms to provide users with more comprehensive and visually rich interfaces for travel planning.

4. **Testing and Refinement**:
   - **Comprehensive Testing**: Continue with rigorous testing of all features to ensure stability and reliability.
   - **User Feedback Integration**: Collect and integrate user feedback to refine and enhance the bot’s functionalities.

5. **Documentation and Knowledge Sharing**:
   - **Detailed Documentation**: Update and expand the documentation to reflect new features and provide clear guidance for users and developers.
   - **Team Knowledge Sharing**: Foster ongoing knowledge sharing within the team to ensure everyone is aligned and up-to-date on the latest developments.

---
