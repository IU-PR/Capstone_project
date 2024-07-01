# Week 3 Report #

## Developing the First Prototype, Creating the Priority List ##

### Technical Infrastructure: ###
Our technical infrastructure is currently set up to support local development, as backend, frontend, and ML components are being developed separately. Each team is working on their respective parts locally. Once multiple components are ready, they will be integrated to work together seamlessly. This setup ensures that we can efficiently develop and test each component individually before integration.

### Backend Development: ###
- Developing the server-side logic and APIs for user and product management.
- Integrating authentication with Single Sign-On (SSO).
- Migrating QR code processing from Python to Kotlin.
- Exploring JPA for efficient database interaction.
- Writing unit tests to ensure code quality and reliability.

### Frontend Development: ###
- Completed initial versions of several key pages.
- Implemented basic UI components to create an intuitive and user-friendly interface.

### Data Management: ###
- Designing data models for users and products.
- Implementing data retrieval and storage functionalities to support the MVP feature set.

### ML (Machine Learning) Integration: ###
- Implementing algorithms for file processing.
- Vectorizing data and storing it in a database.
- Integrating Yandex GPT for recipe generation, enhancing the prototype’s capability to offer personalized content.

### Prototype Testing: ###
We are currently focused on developing and refining the existing prototype. While formal testing is scheduled for later stages, initial rounds of internal testing have been conducted to identify and address any immediate usability issues or bugs.

## Weekly Progress Report: ##
Our team achieved significant progress across all critical areas this week. The technical infrastructure is fully operational, supporting efficient development and testing activities. Backend development saw substantial advancements with API development, SSO integration, and the transition of QR code processing to Kotlin. Frontend development progressed with the completion of key pages and UI components, ensuring a user-friendly interface. In data management, we prepared our database structure to effectively manage user and product data. The ML integration saw the implementation of crucial algorithms and advanced functionalities using Yandex GPT. Initial prototype testing has begun, focusing on refining and enhancing the prototype.

## Challenges & Solutions ##
- Integrating SSO with existing authentication systems presented complexities that required a phased approach for smooth transition.
- Implementing JPA for backend database interactions involved extensive learning and adaptation to ensure efficient data management.
- Balancing frontend and backend tasks required prioritization and clear communication to maintain consistent progress on both fronts.
- In the ML component, the model occasionally produced strange outputs despite well-constructed prompts, requiring additional fine-tuning and testing to ensure more reliable and accurate results.

## Conclusions & Next Steps ##
- Finalizing frontend development and integrating it seamlessly with the main backend functionalities (completing QR code migration to Kotlin and integrating dish data into the database).
- Developing a secondary backend system and connecting it with the ML component to enhance overall system capabilities.
- Continuing to refine the prototype based on initial testing feedback, aiming to ensure a robust and user-friendly final product.
- Addressing the ML model's inconsistencies by further fine-tuning and testing to ensure more reliable and accurate results.
