# Week \#2 

## Detailed Requirements Elaboration


User stories:

1\) As an **ordinary user**, I want to quickly generate complete outfit suggestions tailored to my existing wardrobe and personal preferences, so that I can save time choosing clothes daily and consistently look well-coordinated.

	**Acceptance Criteria:**

- **Generate Full Outfit:** The system should generate a complete outfit (e.g., top, bottom, outer, shoes, accessories) based on selected criteria.  
- **Wardrobe Integration:** Outfit suggestions must primarily utilize items already uploaded to my digital wardrobe.  
- **Save/Favorite Outfit:** I should be able to save or favorite a generated outfit for future reference.

2\) As a **stylist**, I want to efficiently assemble and propose curated outfit combinations for my clients, leveraging their uploaded clothing items, so that I can streamline my styling process and offer personalized recommendations.

	**Acceptance Criteria:**

- **Outfit Assembly Tool:** I can drag and drop or easily select individual items to build an outfit.  
- **Multiple Outfit Proposals:** I can create and manage multiple outfit proposals for a single client.

3\) As a **clothes seller**, I want to generate diverse and visually appealing outfit combinations featuring my products, enabling me to create compelling marketing content and showcase product versatility to attract more customers.

**Acceptance Criteria:**

- **Product Catalog Integration:** I can upload and categorize my clothing products, making them available for outfit generation.

4\)  As a **customer**, I want to identify missing clothing items that would complete an existing outfit or create a desired new look, so that I can make informed purchasing decisions and build a more versatile wardrobe.

**Acceptance Criteria:**

- **Outfit Completion Suggestions:** Given a partial outfit, the system suggests complementary clothing items (e.g., "Add a blazer to this dress").  
- **Style Recommendations:** Recommendations for missing items are aligned with the overall style of the existing outfit.

### Prioritized backlog 

Our notion [link](https://www.notion.so/Week-2-2115a218c5d580b6b886d7e26f92e2fb?source=copy_link%20) with backlog (not kanban table, but similar) and task management with future tasks.

## Project specific progress 

### **Frontend** 

UI tweaks, added file uploading and linked it to the backend’s endpoint. Added “View Wardrobe” button and linked backend’s endpoint to it. Added .dockerignore to /frontend and added Git dependency inside /backend/Dockerfile.

### **Backend** 

Added database for storing outfits. Added endpoints according to this database, so that there is ability to upload outfit, get all outfits, get specific outfit. Moreover, there is a simple outfit prediction endpoint, where you have to submit clothes, and the system will respond with the most suitable outfit. Backend contract (Swagger): [swagger.jpg](https://drive.google.com/file/d/1soq2QEAElbTj0m2Y15RXqAwEP2rkvAYc/view?usp=sharing)

### 

### **ML** 

Added class representing the image search engine. This class utilizes qdrant vector databases for adding clothes to the database, retrieving and searching created embeddings. Moreover, starter logic for making outfit predictions is added. 

### **Business** 

We conducted small customer development research \- [https://www.notion.so/test-2165a218c5d580e3bf88fb3184bff116](https://www.notion.so/test-2165a218c5d580e3bf88fb3184bff116)  
And also analyzed the market, competitors and understood the place of our project in it \-  
[Analyzing the market](https://www.notion.so/Analyzing-business-part-2165a218c5d58000a8dff63ebc8395eb)

**Design**

New design (Wireframes/mockups):[user-flow.jpg](https://drive.google.com/file/d/17W1I6F2ASWE74y5MHkO0v-gxc2vLFec_/view?usp=sharing)

User-flow diagram: [user-flow.jpg](https://drive.google.com/file/d/17W1I6F2ASWE74y5MHkO0v-gxc2vLFec_/view?usp=sharing)

# Weekly commitments 

## **Individual contribution of each participant** 

*Dinar Yakupov \- Enhanced landing page of our application. Provided basic connection between frontend and backend.*  

*Artyom Grishin \- Complete market analysis, market volume, describe in more details product, possible customers, creating report.*

*Victor Mazanov \- Conducted customer development research. Made survey with 5 people on the street and made google form (survey). Got more familiar with auditory, tested how relevant the problem is, if the auditory is ready to use our solution and pay for it.*

*Remal Gareev \- improved product design. Generated some new ideas: provide users urls to the missing product for their outfit from Wildberries; creating folders with different outfits which can be useful if you have many outfits or you work for it professionally (for example stylist).*

*Danil Fathutdinov \- Implemented image search engine class that involves interacting with Qdrant vector database. Implemented inserting to the database logic, and searching for most similar embeddings in database logic. Moreover, created a function to retrieve similar outfits based on provided clothes \- starter logic for the core of our project.*

*Bulat Sharipov \- Contributed to the Backend developing. Created database for storing outfits: in database realised endpoints for uploading outfits, retrieving all of them, retrieving outfit by id. Moreover, created an endpoint that wraps up the main logic for searching similar outfits from image search engine class. Therefore, there is an endpoint that makes the basic prediction for outfit.*

## **Plan for Next Week** 

1. **Creating authentication**: creating database for storing user accounts, creating endpoints for registering and logging. Moreover, on the frontend side there are tasks to create login and register pages.  
2. **Enhancing endpoints for outfit predictions**: Currently, for outfit prediction we need to manually upload images. We will connect our tables from databases, so that there is a single pipeline for creating outfit predictions based on previously uploaded wardrobe.  
3. **Providing deeper customer development**: We will conduct more interviews and try to enhance our previous, based on conducted feedback and experience.  
4. **Project design and management**: Exploring ways for obtaining payments, designing and analysing our go-to-market strategy.

## **What have already been done for our project:**

**Backend**: We already have 10 endpoints that capture the main logic of our application. We have three types of databases: Relational Database, Image Storage Database, Qdrant Vector Database. In the relational database we have tables for storing the user's wardrobe and all possible outfits. Image Storage with MinIO is used for storing images of outfits, wardrobes, and clothes. Vector database is used to save embeddings of clothes.

**Frontend**: The landing page of the application is done and working. There is a possibility to upload wardrobe images. 

**ML**: We explored possible datasets, the report of explored datasets are available in github repository. We trained the YOLO v11 model for detecting clothes on the outfits and subsequently storing them in our database. We implemented a vector database and basic search of similar outfits \- the main idea of our project. 

**Customer** **Development**: We have reached our customer and conducted first interviews through google forms. Analytics from customer development were conducted.

**Project** **Management**: We formulated business characteristics of our project, such as market size, target users, competitive analysis, and unique selling proposition.

**Product Design**: Future directions of the product were analyzed. We collected possible features and saved them for future implementation.

## Confirmation of the code’s operability 

We confirm that the code in the main branch:

- [x] ~~In working condition.~~   
- [x] ~~Run via docker-compose (or another alternative described in the `README.md`).~~

