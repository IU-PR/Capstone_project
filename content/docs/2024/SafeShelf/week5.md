# Week #5 #
## Feedbacks ##
### Feedback collection plan ###
- Conduct user surveys and feedback sessions to gather insights on usability, functionality, and desired features.
- Utilize face-to-face interviews and focus groups to ensure comprehensive feedback from a diverse user base.

### Conducted user surveys or feedback sessions ###
- Conducted feedback sessions with a diverse group of users including busy professionals, students, and homemakers.
- Collected insights on various aspects of the application including user interface, ease of use, feature requests, and overall satisfaction.

### Analyzing feedback, identifying and prioritizing issues ###
- Key issues identified from feedback:
  - **User Interface (UI) Improvements**: Users found some elements of the UI confusing, some of them suggested changing the main color of the website.
  - **Feature Requests**: Users suggested several new features that could enhance the application's usability, such as more options on a person, about his lifestyle and habits.
  - **Customization Options**: Users asked about integration with other apps and websites using the API.

- Prioritization of Issues:
  - High priority: UI improvements, performance enhancements.
  - Medium priority: New feature development based on user suggestions, including customization lifestyle options.
  - Low priority: Long-term integration with other apps.

### User Suggestions ###
- **Dark Mode**: Many users requested a dark mode option to reduce eye strain during night usage.
- **Social Sharing**: Users wanted the ability to share their favorite recipes and meal plans on social media.
- **Bulk Item Management**: There was feedback on the need for better management of bulk items, including quantity tracking and expiration dates.
- **Custom Input**: Some users suggested implementing input for adding items to the inventory by themselves.
- **Detailed Analytics**: Users wanted detailed analytics on their shopping habits, such as spending trends and frequently purchased items.
- **Color Scheme Options**: Users requested the ability to change the application's color scheme to match their personal preferences.
- **Lifestyle Settings**: Users wanted additional settings to input information about their lifestyle, such as dietary preferences, activity level, and health goals, to receive more personalized recommendations.

## Roadmap: ##
- Refine user interface based on feedback to enhance usability.
- Implement new features such as dark mode and social sharing.
- Enhance performance and scalability to handle peak usage times.

 ### Mid-Term Goals (3-6 months) ###
- Explore mobile app development for iOS/Android platforms.
- Plan for long-term integration with custom input and lifestyle-based settings.
- Initiate discussions with grocery chains like Pyaterochka and Magnit for potential collaboration opportunities.

## Weekly Progress Report: ##
### Our team did: ###
- Completed the authorization module for the user authentication process.
- Developed the backend functionality for managing dishes.
- Integrated the backend with the frontend for seamless user and product management.
- Connected the QR API to the backend and frontend parts.
- Fully completed the layout of the screens on the website.
- Conducted comprehensive data cleaning and preprocessing to ensure data consistency and quality.
- Developed a model for storing and retrieving data from a vector database.
- Completed the development of the RAG (Retrieval-Augmented Generation) model.
- Tested and selected the most suitable language model (LLM) for generating responses based on information retrieved using the RAG model.

## Challenges & Solutions ##
### QR Code Integration ###
- **Challenge**: Difficulty integrating QR code functionality into the frontend.
- **Solution**: Conducted thorough debugging and consulted with backend developers to ensure seamless integration. Implemented additional error handling and validation to improve stability and user experience.

### Endpoint Refactoring ###
- **Challenge**: Some endpoints required refactoring to enhance performance and maintainability.
- **Solution**: Conducted code reviews and refactored endpoints to streamline data processing and improve API response times. Implemented best practices for API development to ensure consistency and reliability.

### Database Model Refinement ###
- **Challenge**: Initial database models required refinement to better support application requirements.
- **Solution**: Reformatted some columns and rewrote the database repository functions for better functionality

### Regex Pattern Accuracy ###
- **Challenge**: The initial regex pattern was not accurately identifying and converting units and quantities from the ingredient strings.
- **Solution**: Refined the regex pattern to cover a broader range of units and quantity formats, ensuring it correctly parses the entire ingredient string.

### Handling Mixed Units ###
- **Challenge**: Ingredients with mixed units (e.g., "2 (16 oz.) pkg. frozen corn") were not being converted correctly.
- **Solution**: Updated the regex pattern and conversion logic to handle nested quantities and units, and standardized the units to a consistent metric format.

### String Parsing ###
- **Challenge**: Each character of the ingredient string was being processed individually due to incorrect handling in the convert_to_metric function.
- **Solution**: Adjusted the regex and parsing logic to handle the entire ingredient string as a single entity, correctly isolating the quantity and unit from the product name.

### Data Consistency ###
- **Challenge**: Inconsistent formatting and unexpected characters in the ingredient strings could lead to conversion errors.
- **Solution**: Added preprocessing steps to clean and standardize the ingredient strings before applying the conversion logic.

### Debugging and Validation ###
- **Challenge**: Identifying and troubleshooting conversion issues without clear feedback.
- **Solution**: Added detailed debugging statements to output any ingredients that are not converted correctly, helping to identify patterns and edge cases for further refinement.

### Saiga Model LLM Integration ###
- **Challenge**: Generating coherent and structured final recipes using the Saiga model LLM.
- **Solution**: Utilized the Saiga model LLM for generating the final recipes with complete cooking instructions, ensuring the output is clear, comprehensive, and user-friendly.

## Saiga Model LLM Integration ##
### Introduction to Saiga Model LLM ###
The Saiga model LLM is a state-of-the-art language model designed for generating high-quality text based on given inputs. It excels in tasks such as text generation, content structuring, and context-aware narrative creation, making it ideal for generating well-structured and coherent recipes.

### Benefits ###
- **Coherent Recipe Generation**: The Saiga model LLM's advanced text generation capabilities ensure that the final recipes are coherent, comprehensive, and easy to follow.
- **Context-Aware Instructions**: The model's ability to understand context helps in generating precise and detailed cooking instructions, enhancing the usability of the recipes.
- **Customizable Outputs**: The flexibility of the Saiga model LLM allows for customization of recipe outputs based on specific user preferences or dietary requirements.

### Implementation ###
- **Data Structuring**: Structured the recipe data (ingredients, directions, NER) into a format suitable for input into the Saiga model LLM.
- **Recipe Generation**: Leveraged the Saiga model LLM to generate complete recipes, incorporating the ingredients, directions, and additional information into a cohesive and easy-to-understand format.
- **Validation and Refinement**: Employed the model to validate the generated recipes and ensure they meet the desired quality and clarity standards.

## Conclusions & Next Steps ##

#### Conclusions ####
- Successfully developed a robust system for converting recipe ingredient quantities to metric units, ensuring accuracy and consistency across diverse ingredient formats.
- Leveraged the Saiga model LLM to generate clear, comprehensive, and user-friendly final recipes with precise cooking instructions.
- Identified potential edge cases and provided debugging tools to handle unexpected input formats, enhancing the robustness of the conversion and recipe generation processes.
- Improved pur backend part for better functionality
- Refined some issues happened on the frontend part
- Fixed different bugs on the backend part

#### Next Steps ####
1. **Expand Unit Coverage:**
   - Further refine and expand the regex patterns to cover additional units and quantity formats that might be encountered in a broader dataset.
   - Enhance the algorithm to handle complex ingredient descriptions and variations in formatting.

2. **Enhance Preprocessing:**
   - Implement more sophisticated text preprocessing techniques to handle variations in ingredient string formats, including additional punctuation, abbreviations, and nested quantities.
   - Ensure the preprocessing pipeline is efficient and scalable to support large-scale recipe databases.

3. **User Interface/API Development:**
   - Develop a user-friendly interface or API that allows users to input recipes and receive converted ingredient lists and cooking instructions in a structured JSON format.
   - Incorporate feedback mechanisms to refine user interactions and improve overall usability.

4. **Advanced Recipe Customization:**
   - Explore integrating user preferences and dietary requirements into the Saiga model LLM's recipe generation process.
   - Enable personalized recipe outputs tailored to specific dietary needs and preferences, enhancing user satisfaction and engagement.

5. **Second Backend for ML Integration:**
   - Develop a secondary backend to facilitate seamless integration with machine learning models for advanced recipe analysis and recommendation systems.
   - Ensure compatibility and scalability of the backend infrastructure to support future enhancements and features.

6. **Containerization and Deployment:**
   - Containerize the application components using Docker for streamlined deployment and scalability.
   - Implement CI/CD pipelines to automate testing, integration, and deployment processes, ensuring rapid iteration and delivery of updates.


