---
title: "Week #6"
---

# Week #6 Report

# Presentation

{{< embed-pdf url="/2024/AlumniPortal-Innopolis/AlumniPortal.pdf" >}}

# Weekly Progress Report

Our team achieved several key milestones this week:

- **Backend Deployment**: Successfully deployed the backend infrastructure into Yandex Cloud, leveraging CI/CD pipelines through GitHub Actions to streamline and automate our deployment process.
- **AI Integration**: Completed the integration of an AI-powered Spam Filtering Service. This service is designed to significantly reduce the workload on university staff by automatically filtering and categorizing proposed events and projects submitted by students.
- **Microservice Configuration**: Configured Traefik as our reverse proxy to efficiently manage routing within our microservice architecture. This setup enhances the scalability and maintainability of our application.
- **Caching Implementation and DB server changing**: Integrated Redis for caching, which optimizes performance by reducing the load on our primary database server. This ensures faster data retrieval and improves the overall user experience. Also due to scalability of the project a 6 microservices already running we had to move our DB to another host in order to increase number of connections.
- **Unit Testing**: Developed and implemented comprehensive unit tests across various components to ensure the stability and reliability of our project during new updates and deployments.
- **Frontend Development**: The frontend team has nearly completed the implementation of the main pages for the Minimum Viable Product (MVP). They finalized the transition to Nuxt.js as the framework for the frontend. This part of the project has been successfully deployed to Netlify and is accessible via the link: [https://alumni-inno.netlify.app/](https://alumni-inno.netlify.app/).
- **User Feedback**: Collected valuable feedback from our early adopters regarding the updated design and enhanced functionality. This feedback will inform further refinements and improvements.

# Challenges & Solutions

- **Challenge: CI/CD Pipeline Complexity**
  - **Solution**: We encountered difficulties in configuring the CI/CD pipeline due to the complexity of our multi-service architecture. To address this, we modularized our pipeline scripts and utilized reusable workflows in GitHub Actions. This approach simplified the pipeline management and reduced the chance of errors during deployment.

- **Challenge: AI Spam Filter Tuning**
  - **Solution**: Initially, the AI spam filter produced a high rate of false positives, incorrectly flagging legitimate submissions. We refined the machine learning models and incorporated more diverse training data. Additionally, we implemented a feedback loop where flagged items could be reviewed and corrected, enhancing the model's accuracy over time.

- **Challenge: Traefik Configuration for Microservices**
  - **Solution**: Setting up Traefik to handle routing for multiple microservices posed a challenge due to complex routing rules and SSL termination. We resolved this by leveraging dynamic configuration using Docker labels and automated SSL certificate management through Let's Encrypt, which streamlined the process and ensured secure communication.

- **Challenge: Performance Bottlenecks in Database**
  - **Solution**: Our initial deployment faced performance bottlenecks due to heavy database load. Integrating Redis as a caching layer helped alleviate this load by caching frequently accessed data. We also optimized our indexing strategies, resulting in significantly improved performance.

- **Challenge: Ensuring Frontend-Backend Integration**
  - **Solution**: Ensuring seamless integration between the frontend and backend was challenging due to differing development timelines and environments. We established a robust API contract and utilized Swagger for API documentation, which facilitated better collaboration and alignment between frontend and backend teams.

- **Challenge: Incorporating User Feedback Effectively**
  - **Solution**: Integrating feedback from early adopters was initially overwhelming due to the volume and diversity of suggestions. We categorized the feedback into themes and prioritized changes based on impact and feasibility. Regular sprint reviews and feedback sessions helped us iteratively incorporate the most critical updates.

# Conclusions & Next Steps

Our next steps include:

- **ELK Stack Integration**: Attaching the ELK stack (Elasticsearch, Logstash, and Kibana) for comprehensive metrics gathering and advanced analytics. This will provide deeper insights into system performance and user behavior.
- **Backend Refinement and Testing**: Continuously refining our backend services to ensure optimal performance and stability. Conducting rigorous testing to identify and resolve any potential issues.
- **Frontend Completion and Integration**: Finalizing the frontend development and ensuring seamless integration with the backend services. This will involve thorough testing to guarantee a smooth user experience.
- **Final Pitch Preparation**: Preparing for the final pitch and demo day. This will include rehearsing presentations, refining demo scenarios, and ensuring all project components are ready for demonstration.

