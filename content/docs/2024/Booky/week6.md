# Week #6
## Presentation

{{< embed-pdf url="/2024/Booky/presentation.pdf" >}}

### Weekly Progress Report:

#### Our Team did:

Video : [view ](https://drive.google.com/file/d/1nFQ2nCHEDdWCBywRpBGo_X6xGWmfFfAK/view?usp=sharing)

1. Selected a technological stack including Golang, gRPC, S3 by cloud.ru, YandexGPT, and in-memory storage to support scalability, performance, integration, and flexibility for the app.

2. Identified and resolved several critical bugs in the app, enhancing overall stability and user experience.

3. Redesigned some screens to improve user interface and experience, ensuring a more intuitive and visually appealing app.

4. Implemented the "Improve Text with AI" feature on mobile, allowing users to enhance their notes with AI-generated suggestions.

5. Added Markdown support for notes, explored rendering mathematical formulas, and began integrating improved Markdown rendering capabilities into the app.

6. Made significant progress on implementing the authorization system to enhance app security and user management.

7. Prepared for presentation the project to stakeholders, showcasing the latest developments and future plans.


#### Challenges & Solutions

- ##### Challenge 1: Integration with S3 (cloud.ru)
    - **Context:** The application needed to integrate with S3 for cloud storage, requiring secure and efficient data handling.
    - **Impact:** Several issues arose, including the complexity of setting up proper IAM roles and policies for secure access to S3 buckets, the latency introduced when accessing S3 resources which affected the application's responsiveness, and the challenge of ensuring data consistency between in-memory storage and S3, particularly with concurrent data modifications.
    - **Solution:**  The solution involved implementing robust IAM policies and roles to manage secure access, optimizing S3 access patterns to minimize latency, and establishing mechanisms to ensure data consistency between in-memory storage and S3.

- ##### Challenge 2: Integrating External AI Services (YandexGPT)
    - **Context:** The application required integration with external AI services for advanced functionalities.
    - **Impact:** The impact of integrating YandexGPT includes challenges such as ensuring responsive and reliable API integration, managing imposed rate limits effectively, and ensuring strict compliance with data privacy policies and regulations to safeguard sensitive information.
    - **Solution:** The solution involved optimizing API integration for minimal latency, implementing effective rate limit handling strategies like retries and caching, and ensuring all data interactions with YandexGPT complied with stringent privacy regulations through anonymization and secure storage practices. These efforts aimed to enhance integration reliability, responsiveness, and compliance.

- ##### Challenge 3: Defining a Universal Schema for the Database
    - **Context:** As our application integrates more advanced AI capabilities, such as text enhancement and analysis, the computational load has increased beyond initial expectations. This has led to slower response times and decreased overall system efficiency.
    - **Impact:** Frequent schema changes during the MVP stage due to evolving requirements made it difficult to establish a stable database foundation. These changes also resulted in complex and error-prone data migrations, critical for maintaining data integrity and system stability.
    - **Solution:** To overcome these challenges, non-relational data storage using S3 was adopted. This solution enabled flexible schema changes without compromising system stability, supporting continuous development and evolution of the database schema. Furthermore, strategies were devised to ensure smooth data migration across evolving schemas. These efforts were aimed at optimizing the transition process, reducing interruptions, and preserving operational continuity throughout the database's evolution.



#### Conclusions & Next Steps

- ##### Conclusions:
    - The selected technological stack of Golang, gRPC, S3 by cloud.ru, and YandexGPT has provided a solid foundation for developing a scalable and high-performing mobile app.
    - Integration challenges, performance architecture, AI service integration, and dynamic schema management have been crucial learning experiences.
    - Continued efforts to optimize and refine these aspects will enhance the application's reliability and performance as we move from MVP to stable release.

- ##### Next Steps:
    - Refine AI functionalities based on performance analytics.
    - Introduce authorization and access control.
    - Prepare project to be open source.
    - Prepare promotion strategy to find project inheritors.