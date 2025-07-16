---
title: "Week #6"
---

# **Week #6**

## Links


- **Deployment**: [website](https://search.innohassle.ru/search)
- **API Docs**: [swagger](https://api.innohassle.ru/search/staging-v0/docs)
- **Design**:
  - Desktop version [pages](https://www.figma.com/design/yZIK0jneKe3qTf4HLIkTFb/Search--updated-design-?node-id=4-134&t=hyCEQmhXjvecMk8R-1), [prototype](https://www.figma.com/proto/yZIK0jneKe3qTf4HLIkTFb/Search--updated-design-?node-id=4-234&t=IajzMsdfFwffe7Zg-1&starting-point-node-id=4%3A234)
  - Mobile version [pages](https://www.figma.com/design/yZIK0jneKe3qTf4HLIkTFb/Search--updated-design-?node-id=4-134&t=hyCEQmhXjvecMk8R-1), [prototype](https://www.figma.com/proto/yZIK0jneKe3qTf4HLIkTFb/Search--updated-design-?node-id=4-1545&p=f&t=ewaQYCzvfeAA7ENJ-1&scaling=min-zoom&content-scaling=fixed&page-id=4%3A134&starting-point-node-id=4%3A1545&show-proto-sidebar=1)
- **Demo**: [video](https://drive.google.com/file/d/1CgQGlCTahn_Yko4nyJ8AQxiTI18lIqpw/view?usp=sharing)

## Final deliverables

### Project overview

Our project is one of the services of the [InNoHassle](https://innohassle.ru) ecosystem - a unified digital platform created to facilitate the routine of Innopolis students.

**Problems of IU students:**  
- All information is scattered across different sources
- There is no single reliable knowledge base

**Solution:**  
The Search service produces information searches for all relevant resources available to Innopolis students.

### Features

- Search engine for IU-related sites
  - User hints in the form of default queries
  - Filtering answers by sources
  - Visual preview of websites
  - Text preview of the answer from the website
  - The answer link leads directly to the desired section of the page

- AI system answering questions about IU
  - LLM answers (openai gpt-4.1-mini)
  - Links to references

- AI interface performing actions for the user
  - Booking a music room or stating the impossibility of booking in response to a user request in free form

### Sources of information:
Sites available without authorization as an Innopolis student are parsed every hour. Our search engine provides answers based on their current content.  
These sources include:
- [Maps](https://innohassle.ru/maps)
- [Campus life](http://campuslife.innopolis.ru/)
- [Eduwiki](https://eduwiki.innopolis.university)
- [Hotel](https://hotel.innopolis.university/)
- [Residents](https://sez-innopolis.ru/residents/)

Sites available only to students are considered confidential. We have independently created and manually maintain a database of their functionality, describing in general terms what can be found on them. Only this information is available to users of our service until they go to the original site.  
These sources include:

- [InNoHassle](https://innohassle.ru)
- [My University](https://my.university.innopolis.ru/)
- [ITHelp Wiki](https://help.university.innopolis.ru/ru/home)

### Tech stack

**Backend:**

- [Python 3.11](https://www.python.org/downloads/): The main programming language used for backend development.
- [poetry](https://python-poetry.org/docs/): Dependency and package manager for Python projects; used to manage virtual environments and libraries.
- [FastAPI](https://fastapi.tiangolo.com/): High-performance web framework for building RESTful APIs.
- [Pydantic](https://docs.pydantic.dev/latest/): Data validation and parsing with type hints
- [MongoDB](https://www.mongodb.com/): NoSQL document-oriented database used to store application data.

**Frontend:**

- [TypeScript](https://www.typescriptlang.org/), [Node.js](https://nodejs.org/en): Type-safe programming language (TypeScript) and runtime environment (Node.js) used for frontend tooling and development.
- [React](https://react.dev/): JavaScript library for building user interfaces.
- [Vite](https://vite.dev/): Fast build tool and development server for modern frontend frameworks like React.
- [TailwindCSS](https://tailwindcss.com/): Utility-first CSS framework used for styling components with minimal custom CSS.

**ML**

- [Lancedb](https://lancedb.com/): Vector database optimized for similarity search and storing embeddings.
- Bi-encoder, cross-encoder: Models used for semantic search and ranking; bi-encoders for fast retrieval, cross-encoders for accurate re-ranking.
- [Infinity](https://github.com/michaelfeil/infinity): High-performance inference engine for deploying and running ML models efficiently.
- [langdetect](https://pypi.org/project/langdetect/): Language detection library to identify the language of input text.
- [LLM openai/gpt-4.1-mini](https://openrouter.ai/openai/gpt-4.1-mini): Lightweight version of OpenAI's GPT-4 model used for tasks like summarization, generation, or semantic understanding.
- [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M): Multilingual translation model from Facebook (Meta) used for machine translation across multiple languages.

### Setup instructions

See the repositories README.md for detailed instructions:
- [Frontend](https://github.com/one-zero-eight/website)
- [Backend](https://github.com/one-zero-eight/search)

## Presentation draft

Use vpn to access our [presentation](https://www.canva.com/design/DAGs37XRL5k/LToMI-JXRZlb-J8XXVMCxw/edit?utm_content=DAGs37XRL5k&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

# Weekly commitments

### Team management
**Anna** prioritized existing tasks (see [Kanban board](https://github.com/orgs/one-zero-eight/projects/4), `search` project), assigned top-priority tasks to performers, reviewed all actions of team members, controlled the redesign process, communicated with customers from [one-zero-eight](https://t.me/one_zero_eight).

### ML

**Anna** corrected the transmission of the prompt system and changed its structure (see commits [#1](https://github.com/one-zero-eight/search/commit/f52398ac9dae9cbf6db7518d91414921495798f6), [#2](https://github.com/one-zero-eight/search/commit/99a3562eb0f023b2efde19f59467b452dd72d46b)).

**Sofia** has implemented:
- Encoder change: bi- and cross-encoders have been updated, which has increased the accuracy and speed of the search (see commits [#1](https://github.com/one-zero-eight/search/commit/f83560f06728b622800d9fd8648a4a0194a1b154) and [#2](https://github.com/one-zero-eight/search/commit/b001913cdfce72e966626d3ad6d17d6e7968b1a3))

- Optimization of the LLM response backend: if the LLM returns that there is no information, the backend does not send resources to the client; when the information is found, it returns only filtered, maximally relevant results (see [commit](https://github.com/one-zero-eight/search/commit/0323ab005d906dc619d68b7cb6db36ee4a68d951))

- Implementation of the ACT module: added a service for booking a music room with endpoints /act/availability and /act/book and saving statistics to the database  (see commits [#1](https://github.com/one-zero-eight/search/commit/5bc3ff6d5d4b453ef02f22049ae572a33f74f05c) and [#2](https://github.com/one-zero-eight/search/commit/ec6dd04213128330b1ab4a199d073aac1a58fea1)).

### Backend

**Anna** added typing of static resources to the backend (commit [#1](https://github.com/one-zero-eight/search/commit/5a412995ac39b144e0dddb83af8fdb5caf173407), [#2](https://github.com/one-zero-eight/search/commit/89a51aa64ef8d7da361a37175e8b68249f7f84c2))
**Anna** also added processing of the innohassle user token so that the act service could execute requests on his behalf (see [commit](https://github.com/one-zero-eight/search/commit/9e2c8d43864efbcf09170b70a909416c3c786195)).

**Vladimir** extended resources we use with [ITHelp Wiki](https://help.university.innopolis.ru). He analysed each page and prepared it for databases(see [commit](https://github.com/one-zero-eight/search/commit/3a4111a8db09647ffd726cec5b59652d6f82f86e)). Also Vladimir migrated our project from poetry to uv (see commits [#1](https://github.com/one-zero-eight/search/commit/5a42180b12ad21d489f6d5e0f0a56bbfab76bfc4) and [#2](https://github.com/one-zero-eight/search/commit/04a9c8045f123249b392b1fafe88e6bf0fe22ecc))

**Azaliia** fixed parsers for eduwiki and campus_life. Redirection issue is solved, section parsing is corrected (see commits [#1](https://github.com/one-zero-eight/search/commit/62134865e8e127da699f4dcfbea519c05c0f23cc), [#2](https://github.com/one-zero-eight/search/commit/2f3d5d1651e21232f4128cae16bd42042b56f0be))

### Frontend

**Anna** added correct filtering of static resources: InNoHassle, My University, ITHelp Wiki (commits [#1](https://github.com/one-zero-eight/website/commit/374fed1fea736a98fb0fb970edf5d5c88d098feb), [#2](https://github.com/one-zero-eight/website/commit/6aa72ad65b5a30c9a7b4967d4667856c3db99ee2))

**Aliia:**
- Made redesign in accordance with user testing feedback: see [Figma](https://www.figma.com/design/yZIK0jneKe3qTf4HLIkTFb/Search--updated-design-?node-id=4-134&t=4Fqe2sgQnN3h3foB-1)
- Updated the design, made it adaptive for small screens: see commit [#1](https://www.figma.com/design/yZIK0jneKe3qTf4HLIkTFb/Search--updated-design-?node-id=4-134&t=vhsnYPpknRKgmGcK-1)
- Added links highlighting in the ask response: [#2](https://github.com/one-zero-eight/website/commit/8ecb891dafcec98b990ada335e204340aad6c0aa)
- Updated the code according to the new design: [#3](https://github.com/one-zero-eight/website/commit/7c6db9278d371e48ecb7d59ceea71aa2c5a2ca3d), [#4](https://github.com/one-zero-eight/website/commit/9e168aeed1928f25283e5b3d99a875bd3fcd0b0f), [#5](https://github.com/one-zero-eight/website/commit/9962eb72a5799930da75a7510f4f1137457557bf)
- Added 502 processing for ask: [#6](https://github.com/one-zero-eight/website/commit/3dfdce42a16a85c5c64387199861a15afb88a262)
- Connected `act` page to backend: [#7](https://github.com/one-zero-eight/website/commit/4f0393707eca46b269b91c61b95c9cab2386ff6f)

### Overall progress

#### Redesign

Our most significant advances include the redesign we made based on the results of user testing sessions. We moved the functionality to separate sections of the site instead of buttons as it was before because the functionality of the buttons raised questions among users. We also changed the filter field.

Old design:
![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week5/search.png?raw=true)

Updated design:
![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week6/redesign.png?raw=true)

#### Act functionality

Another important feature was the connection of the act functionality. Now it allows users to book a music room for the time they want using a free-form request.  
Request:  
![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week6/act.png?raw=true)
Result:  
<img src="https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week6/booking.png?raw=true" width="300">

## Individual contribution of each participant

| Team Member           | Contribution                                       |
|-----------------------|----------------------------------------------------|
| Anna Belyakova (Lead) | See [team management](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#team-management), [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#backend), [frontend](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#frontend) and [ML](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#ml) sections |
| Vladimir Paskal       | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#backend) section    |
| Azaliia Alisheva      | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#backend) section|
| Aliia Bashirova       | See [frontend](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#frontend) section |
| Sofia Pushkareva      | See [ML](https://capstone.innopolis.university/docs/2025/inno-services-search/week6/#ml) section                              |


## Plan for Next Week

- Separate static resources on the frontend
- Implement the ability to continue the conversation in the ask section
- Add visual previews to static resources
- Fix the preview text in the search section
- Prepare for the presentation

## Confirmation of the code's operability

**!!!** The working code in the backend repository is in the `main` branch, and in the frontend repository in the `capstone` branch (difficulties due to automatic deployment)
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).
