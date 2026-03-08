# Week #1

## Project description

**Project name:** StyleU

**Code repository:** [GitHub Repository](https://github.com/IU-Capstone-Project-2025/styleU)

### **Project Idea**
Develop an AI-powered stylist that provides personalized outfit suggestions based on user input. Features include:
- Detecting user’s color type from a photo
- Identifying body type from measurements
- Suggesting real products from marketplaces like Wildberries and Ozon

### **Problem Statement**
 According to Thread (2023), around 65% of consumers feel uncertain when choosing clothes, as they don’t know what suits their body type and color palette.
	Although various solutions exist — online stores, virtual stylists, at-home try-ons, users often lack time for long outfit selection, waiting for deliveries, and managing returns. Moreover, many people have no clear understanding of what truly suits them, as well as fresh ideas on how to update their look or try a new style.


## 1) Team Members

| Team Member           | Telegram Alias     | Email Address                                 | Track            | Responsibilities                                             |
|-----------------------|--------------------|------------------------------------------------|------------------|--------------------------------------------------------------|
| Ksenia Korchagina (lead) | @Ksuuu245         | k.korchagina@innopolis.university             | Backend/Teamlead | Organizational work, deployment, backend support             |
| Yasmina Mamadalieva   | @yapii7            | y.mamadalieva@innopolis.university            | ML/Backend       | ML lead, model training                                      |
| Aisylu Fattakhova     | @Aisylu_Fattakhova | a.fattakhova@innopolis.university             | ML/Backend       | AI integration, prompt writing, optimization                 |
| Ekaterina Akimenko    | @akimoshka         | e.akimenko@innopolis.university               | Frontend/Design  | Design development, frontend implementation                 |
| Sofia Goryunova       | @ssffffqq          | s.goryunova@innopolis.university              | ML/Backend       | Dataset creation, parser development                         |
| Alena Starikova       | @alsstarikova      | a.starikova@innopolis.university              | Backend          | Backend service development                                  |
| Rokkel Maria          | @mars_min          | m.rokkel@innopolis.university                 | Frontend/Design  | Design development, frontend implementation                 |

---
## 2) Brainstorming

### Ideas during brainstorming:

1) **An AI platform that takes student notes or topics and auto-generates:**

    personalized quizzes,

    concise cheat sheets,

    voice-based explanations. 

2) **A system that gathers learning, sleep, diet, and schedule data to simulate a "digital twin" that predicts:**

    burnout risk,

    course success probability,

    optimal study slots.

3) **AR/VR Science Experiment Simulator**

    Build an AR/VR app that allows students to perform physics, chemistry, or biology experiments virtually when labs are unavailable.
    Great for remote learners or budget-constrained institutions. 

4) **AI-powered stylist that provides personalized outfit suggestions based on user input** (choosen one)

    Features include:

    Detecting user’s color type from a photo, identifying body type from measurements, suggesting real products from marketplaces like Wildberries and Ozon

### Brief market research / problem validation:

1) **An AI platform that takes student notes or topics and auto-generates:**

    A lot of students struggle with preparing for exams due to time constraints, information overload, and lack of personalized study strategies. Traditional learning platforms (e.g., Coursera, Umschool) offer static content that doesn’t adapt to individual needs or time pressures.



 2) **AI-powered stylist**

    **GETOUTFIT**
    An AI-based stylist. It finds clothing items of a specific color and model or suggests matching pieces for an existing item in your wardrobe.

    **STYLEDNA**
    Determines your color type using your phone’s camera. Allows you to add wardrobe items to the app in order to create outfits and capsule wardrobes.
    Enables confident clothing purchases based on your digital wardrobe.

    **STYLISTS**
    Online/offline outfit creation services provided by experienced fashion professionals, with looks tailored specifically for you.

    Our competitors have strong advantages:
    GETOUTFIT offers quick item selection based on color and model,
    STYLEDNA provides convenient tools for color type analysis and capsule creation,
    STYLISTS deliver a high level of personalization thanks to the expertise of human professionals.

    However, their disadvantages include:

    - limited automation and functionality (GETOUTFIT, STYLEDNA),

    - high costs and long service times (STYLEDNA, STYLISTS),

    - lack of innovations such as 3D visualization or the addition of accessories to complete outfits.


### **Target Users**
- **Career-driven individuals** – Limited time, unsure about sizing and style.
- **Mothers on maternity leave** – Post-pregnancy body changes, no time for shopping.
- **Students and young adults** – Budget constraints, need for trendy clothes.
- **Men aged 25–45** – Low interest in fashion, desire to look good.
- **People with non-standard body types** – Difficulty finding flattering, fitting clothes online.

---

## 3)  User Stories

- **Anna’s Story**  
  Anna, a young woman, wants to buy a new jacket for the season, but every color she tries seems off — too pale, too bright, or just not flattering. She feels frustrated and uncertain about what suits her.
She visits our app, uploads a photo, and quickly discovers her color type. The app provides personalized color palette recommendations tailored to her skin tone and features.
With this new knowledge, Anna confidently browses curated options and finds the perfect jacket in a flattering shade — saving time, money, and stress.


- **Alex’s Story**  
  Alex is getting ready for a first date. He wants to look stylish and make a great impression — but not overdressed or too flashy. He’s unsure where to begin.
He opens our app and describes the occasion, the look he wants (casual yet put-together), and his budget.
The app instantly offers a complete outfit suggestion using real products from marketplaces like Wildberries and Ozon. Alex can order the entire look with just a few clicks and feel confident walking into his date.

- **Alice’s Story**  
  Alice recently became a mother. Between caring for her baby and recovering physically, she doesn’t have time to go shopping — and the clothes she orders online rarely fit the way she hoped.
She uses our app to enter her updated body measurements. The app takes her new shape into account and curates clothing options that are more likely to fit and flatter her.
Maria can now shop smartly, without stress, and feel good in clothes that actually work for her new lifestyle.

- **Dmitry’s Story**  
  Dmitry is a 35-year-old professional working in a fast-paced corporate environment. He wants to look sharp every day but doesn’t enjoy spending time choosing outfits or shopping.
He tries our app and selects the “Capsule Wardrobe” option. Based on his lifestyle, color preferences, and measurements, the app suggests a compact set of versatile clothing items that can be easily mixed and matched — perfect for both work and casual outings.
Dmitry orders the recommended pieces from trusted marketplaces. Now he spends less time thinking about clothes and still looks effortlessly put-together every day.

---

## 4) Initial scope

The initial version includes integrating the AI, training the model to determine color types, and using the AI stylist without registration (this will be added after the MVP). It also includes creating a design that will require minimal adjustments later.

Subsequently, we will add user authentication, outfit selection, and the ability to save favorite looks.

---

## 5) Tech Stack and Justification

### Machine Learning (ML)

1) **Python**

    The primary programming language for all ML models and server-side logic.

2) **Scikit-learn**

    Used for building models on tabular data, such as Decision Trees, Random Forest, KNN, and clustering methods like KMeans. Suitable for classification tasks like determining body shape based on numerical parameters and for clustering CLIP embeddings.

3) **Pandas and NumPy**

    Used for loading, preprocessing, aggregating, and analyzing data. Pandas is convenient for working with tabular data, while NumPy is used for array operations and vector representations.

4) **Flask / FastAPI**

    Frameworks for building REST APIs, which integrate ML models into the backend of the web application. They allow handling user requests and returning prediction results.

5) **OpenCV**

    Used for image processing: photo preprocessing, extracting regions of interest, color manipulation, scaling, and cropping. It can be applied during dataset preparation or user image analysis.

6) **TensorFlow or PyTorch**

    Deep learning frameworks used when it’s necessary to train or fine-tune convolutional neural networks (CNNs) for image analysis, including color type classification or detection of visual body shape features.

7) **CLIP (Contrastive Language–Image Pretraining)**

    A model by OpenAI that maps images and text into a shared embedding space. It’s used to extract appearance features from photos and cluster them by color type, as well as to match clothing items based on text queries or embedding-based search.

8) **MediaPipe (optional)**

    A tool for extracting visual features from the face and body (e.g., face shape, body proportions), in case CLIP is not sufficient for analysis. It may also be used in custom dataset creation.

9) **Mistral AI (/ LLaMA / OpenChat)**

    A natural language processing model (LLM) used to interpret user text queries, convert them into structured instructions or search vectors, and generate outfit descriptions.


## Backend
1) **Python** - main programming language. 
                
    Great integration for Machine Learning & AI

    FastAPI: High Performance & Async Support
    
    Database Flexibility
    
    Rich Web & API Tooling

    Experience in software development in this programming langauge

2) **FastAPI** - was chosen because:

    Native async support (good for I/O-bound operations like DB queries and API calls)
    
    Automatic OpenAPI/Swagger documentation
    
    Excellent performance (comparable to Node.js/Go)
    
    Easy integration with Python's ML ecosystem

3) **Pydantic** - For data validation (naturally complements FastAPI)

## Database Stack

1) **PostgreSQL (Primary DB)** - Best for:
    
    User data (structured, relational)

    Body measurements 

    Transactional data (purchase history, etc.)

    Advanced querying (JOINs for outfit recommendations)

2) **MongoDB (Secondary DB)** - Ideal for:

    Storing image analysis results (flexible schema)
    
    Color type data (document-oriented nature fits well)
    
    Scaling read-heavy operations (caching recommendations)

    ____
    Justification for **Mixed DB Approach**:

    **PostgreSQL** handles structured user/profile data where relationships matter
    
    **MongoDB** accommodates unstructured data from ML analyses and scales for recommendation logs
    
    **FastAPI** seamlessly integrates with both via async drivers (asyncpg for PostgreSQL, motor for MongoDB)

    Also, maybe we will use **Redis** (for caching frequent recommendations), **SQLAlchemy** ORM/asyncpg (PostgreSQL interaction), **Motor** (async MongoDB driver)


## Frontend + Design
1) **React** - is a library for creating interactive interfaces. It allows  to easily break down an interface into frequently used components, which simplifies code development and maintenance.

2) **Tailwind CSS** -  is a set of ready-made styles for quick layout. It allows you to quickly create responsive design directly in HTML markup, without having to write a lot of CSS.

3) **[Design ideas](https://www.siteinspire.com/)** - a site with the best and unusual designs where we take ideas and get inspired (open with vpn)


## 5) Weekly commitments

1) Ksenia Korchagina (lead) - Task distribution and time estimation, organizing project deployment meetings, deploy, initial database sketch, writing the report

    **[Kanban board](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/database/f226fd43-ad24-45a2-ac21-8f5c7684f4c6?viewId=8db4dd59-b2c6-4239-a5df-f858e9cc0f39)**

    **[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/aba1f84a2f6b1af8c524039900023d45a3416e90)**

2) Yasmina Mamadalieva  - Organizing an additional meeting for the ML group, selecting core methods for ML training, gathering design ideas

    **choosen methods are presented in this reports**
   **[discussions](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/article/4bb0ce68-f724-4765-b7e9-b05cfc998590)**

4) Aisylu Fattakhova - Consulting acquaintances regarding model training, analyzing selected models

    **choosen methods are presented in this reports**
   **[discussions](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/article/4bb0ce68-f724-4765-b7e9-b05cfc998590)**

6) Ekaterina Akimenko - Started working on the design, created a minimally working version of the frontend

    **[Figma](https://www.figma.com/design/VHOnHId7DlFbgjnn46NGUW/StyleU?node-id=15-2&p=f&t=lgCLL10e3f1up4oQ-0)**

    **[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/1c1e5d87bf0915e2f939e17da29ae18ed56d8abc)**


7) Sofia Goryunova - Selected core methods for ML training

    **choosen methods are presented in this reports**
   **[discussions](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/article/4bb0ce68-f724-4765-b7e9-b05cfc998590)**

9) Alena Starikova - Drafted the architecture, created a minimal working version of the backend, analyzed databases we plan to use

    **[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/082d97b55a604607269671084efdcbfd4016239d)**

    **[architecture](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/article/3bd9fd5c-b32c-4e2f-8ce1-9d74af96f661)**
                      
10) Rokkel Maria - Started working on the design and logo 

    **[Figma](https://www.figma.com/design/VHOnHId7DlFbgjnn46NGUW/StyleU?node-id=15-2&p=f&t=lgCLL10e3f1up4oQ-0)**



