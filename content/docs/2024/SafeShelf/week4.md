# Week 4 Report

## Testing, Feedback Integration, and Continuous Iteration

### Overview
This week, our primary focus was on three critical areas: obtaining external feedback, rigorous testing, and iterative development. These processes are fundamental to ensuring our project aligns with user expectations and functions effectively.

### External Feedback

#### User Acceptance Testing (UAT)
We conducted a survey among our friends to gather initial feedback on the frontend part of our application. We presented the current version of our interface and collected insights on desired features and overall usability. The key findings from the survey are as follows:

- **Photo Analysis Feature**: A majority of the respondents expressed a strong interest in having a feature that allows them to analyze the contents of a grocery bag by simply taking a photo. This would significantly streamline the process of inventory management and meal planning.
- **Recipe Suggestions**: Users want personalized recipe suggestions based on the ingredients they have.
- **Expiration Date Alerts**: Many users highlighted the importance of receiving alerts for items nearing their expiration dates.
- **Meal Planning**: There is a high demand for meal planning functionalities that consider dietary restrictions and preferences.
- **Mobile App Development**: Users expressed a desire to have the application available on iOS/Android devices or as a Telegram bot for easier accessibility. While we are not currently considering a Telegram bot, developing a mobile app is a potential future development after creating a fully functional prototype.

These insights have provided a valuable direction for refining our application to better meet user needs.

We plan to gather feedback again from our friends, and possibly from a broader audience including people who are not related to IT, to get diverse perspectives on the application's usability and features.

### Testing

#### Prototype Testing
This week, we initiated thorough testing of our prototype to identify bugs, assess usability, and ensure reliability. The primary focus areas included:

- **Functionality Testing**: Verifying that features that are currently exists work as intended, including QR code scanning.
- **Usability Testing**: Assessing the user interface for ease of use and intuitive navigation.
- **Performance Testing**: Ensuring the application runs smoothly without significant lag or crashes.

**Results**:
- We identified several bugs in the QR code scanning feature that occasionally caused incorrect product entries. These issues are currently being addressed.
- User feedback indicated that some interface elements were not as intuitive as expected, prompting a redesign of certain UI components to improve user experience.

Additionally, we fixed a bug in the backend part related to working with the external API, which provides us with information from receipts. This fix ensures more reliable data retrieval and processing.

### Iteration

#### Continuous Improvement
Based on the feedback and testing results, we entered an iterative development phase. Key actions taken include:

- **Refining the User Interface**: Implementing changes to the UI to enhance usability based on user feedback. We are making the frontend more user-friendly to improve the overall user experience.
- **Bug Fixes**: Addressing the identified bugs in QR code scanning and other functionalities.
- **Feature Enhancement**: We are still working with prototype, so for now we are not thinking about new features integration (but for example adding authorization via Azure or Yandex still exists as an idea in mind)
- **Performance Optimization**: Optimizing the backend to improve performance when handling larger datasets.
- **Parallel Writing Tests**: Writing integration tests for the backend to ensure the robustness of various components and their interactions.

### Machine Learning/AI Integration

#### AI-Driven Features
This week, we also focused on integrating machine learning and AI components to enhance the application's functionality:

- **Receipt Generation Using RAG and LLM**: We developed a system to generate receipts using Retrieval-Augmented Generation (RAG) and Large Language Models (LLM). This system extracts relevant product information from various data sources and generates realistic receipts. This allows users to automatically populate their inventory without manual entry, improving efficiency and accuracy.
- **Personalized Recipe Suggestions**: An AI algorithm is being developed to provide personalized recipe suggestions. This algorithm analyzes user inventory, dietary restrictions, and preferences to recommend recipes. We are using collaborative filtering techniques and user preference learning to improve the relevance of suggestions.
- **Expiration Date Prediction**: A machine learning model is being trained to predict expiration dates based on product type and purchase date. This will enhance the expiration date alert feature, providing users with timely notifications to reduce food waste.

#### Challenges in AI Integration
- **Data Collection**: Gathering and annotating a sufficient amount of high-quality data for training the receipt generation model has been time-consuming.
- **Model Accuracy**: Achieving high accuracy in receipt generation and expiration date prediction requires extensive training and fine-tuning of models.
- **Resource Constraints**: Running AI models efficiently without compromising the application's performance is challenging. We are exploring cloud-based solutions to manage computational loads effectively.

### Integration Challenges
We have not yet connected the frontend and backend parts of the application due to some existing bugs. These issues are currently being addressed, and we plan to integrate both parts once they are resolved to ensure seamless functionality.

### Future Testing Plans
We are currently considering end-to-end (e2e) testing, although it is still in the planning stage. Implementing e2e testing will allow us to evaluate the entire workflow of the application from start to finish, ensuring comprehensive coverage of all functionalities.

### Weekly Progress Report

**Achievements**:
- Conducted a comprehensive survey to gather external feedback.
- Initiated and completed initial rounds of functionality and usability testing.
- Fixed a bug in the backend related to the external API.
- Began iterative improvements based on testing and feedback, focusing on UI refinement and bug fixes.
- Developed AI models for receipt generation, personalized recipe suggestions, and expiration date prediction.

**Challenges**:
- Some bugs in QR code scanning required significant debugging efforts.
- Balancing the implementation of new features with ongoing bug fixes and optimizations posed scheduling challenges.
- Delay in connecting frontend and backend parts due to existing bugs.
- Data collection and model training for AI features are resource-intensive and time-consuming.

**Next Steps**:
- Continue iterative improvements, focusing on user feedback to refine and enhance the application.
- Conduct additional rounds of testing post-iterations to ensure stability and usability.
- Plan and potentially implement end-to-end testing to ensure comprehensive coverage.
- Further develop and fine-tune AI models for enhanced functionality.
- Explore cloud-based solutions to manage computational loads for AI components.

### Conclusions
Week 4 has been pivotal in refining our project through testing, feedback integration, and iterative development. By continuously evaluating and adjusting our approach based on real user input and testing results, we are steadily moving towards a robust and user-centric final product. As we proceed, maintaining this iterative and feedback-driven approach will be crucial to our success.
