---
weight: 3
bookFlatSection: true
title: "Week #3"
---

# **Week #3**


## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**: Continuous Integration and Continuous Deployment (CI/CD) with GitHub Actions for a Python FastAPI backend involves several key steps, including linting, testing, building a Docker image, and deploying the application to a server.
    
    - Lint: Linting in Python enhances code quality by detecting potential issues early, improving readability, and ensuring coding standards are met, thus facilitating efficient development and collaboration
    - Test: Testing in software development is crucial as it ensures the software meets requirements, identifies defects early, mitigates risks, enhances user satisfaction, and optimizes the development process, leading to cost savings and improved quality
    - Push on server: Pushing a Docker image to a server without storing the code on the server involves saving the Docker image to Docker Hub, and then loading the image on the server. This method ensures that the server only contains the runtime environment and dependencies encapsulated within the Docker image, not the source code itself.
    - Deploy: Deploying with Docker Image simplifies the process of automating environment production and code deployment across various stages, enabling seamless transitions between development, testing, and production environments.
    
    We configured CD for front-end development purposes using Cloudflare Pages to make the process of testing easier. Cloudflare Pages clones a repository on each new commit, deploys using its own infrastructure and connects unique subdomain. Also, we discovered the reference material online to explain the whole process to other team members.
    
- **Backend Development**: Several crucial API endpoints, providing minimal valuable service were implemented. Specifically, short link `CRUD`:
    
    1) Creation of short links
    
    2) Retrieval of the links
    
    3) Deletion of the links
    
    Some secondary features, e.g. statistics, redirection via a password and limitation of visits number are not yet implemented, as we were mainly focusing on the core functionality.
    
    It is also worth mentioning that we have implemented link creator authentication functionality, so only authorized and authenticated users may access secondary features in the future.
    
- **Frontend Development**: Our front-end developers has started developing the working prototype of the website. We have used the wireframes created earlier in [Figma sketch file](https://www.figma.com/design/cmUJUrV3SsOqX8GXTZvsKH/LinkLink-In?node-id=0-1&t=SLzvGrmKDmK6iE6v-0) to start building the web pages. To accelerate the speed of front-end development, we decided to build our own component library on top of open-source user interface library.
For now, we prioritize the first feature set (link shortening) over the secondary set (link customization).
- **Data Management**: We have already set up a `postgres` database for our user data management and link storage. As mentioned earlier, the `CRUD` functionality (endpoints) is already implemented. Although our service does not yet support advanced features, we have designed our database with them in mind, so when we will enable them in the future `db scheme` will need no redesign. Our API uses ORM, which allows to manage items in database easily and safely.

We have enlisted the help of our colleagues and friends to use the prototype to identify any flaws or overlooked aspects in our plans. This additional feedback is essential, as the frontend developers may have missed certain issues during their initial assessments.

Following comprehensive testing and interviews, we discovered that several pages we initially deemed necessary as separate entities can be effectively integrated into the main page (e.g., advanced settings for links). Additionally, we identified several new user paths that we had not previously considered, such as users attempting to access non-existent or expired short links.

We intend to address these issues in the next iteration. By refining the page structure and incorporating feedback on user paths, we aim to enhance the overall user experience and functionality of the prototype.

## **Weekly Progress Report**:

- **Prototype Features:** Our team has implemented:
    - Link shortening —  user enters the long link and gets the shortened one. It is the core interaction which is essential to the project goal.
    - User authorization — user may create and login into his account so only authorized users may access secondary features in the future.
    - Website core interactions — user will be able to access the website hosted publicly and create short links via convenient and user-friendly interface.
- **User Interface:** Our team has prepared the user interface design using [Figma Prototype](https://www.figma.com/proto/cmUJUrV3SsOqX8GXTZvsKH/LinkLink-In?node-id=1-2&t=SLzvGrmKDmK6iE6v-0&scaling=contain&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A2) feature. The key screens for the website are:
    - Main page — where the user will be able to make the link shorter
    - Redirect page — make user experience greater by speeding up redirection and intuitive design
    - Dashboard — where the user will be able to manage the links and view statistics.
    
    Moreover, user will also interact via Telegram bot, which will be connected to the same API as the web app, improving UX by integration with the most popular messenger and enforcing the consistency of data across multiple sources of interaction.
    

### **Challenges & Solutions**

During the front-end development, our team has encountered the obstacle of styling the UI interface. This process requires a proper dedication and significant time resources although it requires only knowledge of CSS. 
Therefore, our team decided to use open-source UI components for development of first prototype. In future, we will build own component library as in Figma design file on top of used UI library.

While setting up the deployment via Cloudflare Pages, we encountered that the domain `pages.dev` [is blocked](https://rknweb.ru/blocked/933200/) in Russia due to legal reasons. Therefore, our team researched alternatives and decided to migrate to Vercel for development deployments, so the website will be accessible in Russia without proxy services.

### **Conclusions & Next Steps**

During upcoming weeks, we will continue the development of our product to deliver a fully-functional prototype in the future. We will improve the user interface based on the feedback from the users and address discovered bugs and errors. Also, we may perform the database normalization if this measure will be necessary. 
Moreover, we aim to develop more secondary features for customizing the creation of short link, such as limiting the visits number, password protection, customizing expiration time, adding banners and advanced statistics. Later, we aim to develop the dashboard with possibility of managing the created links within a corresponding link creator account. Additionally, we may setup a Grafana monitoring to get more insights from the application metrics in the future.