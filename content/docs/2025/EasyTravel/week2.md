---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

### Functional requirements:

- Semantic Point of Interest (POI) search: The system should accept user queries in natural language, such as "romantic place for an evening stroll" or "museums without crowds", and return the most relevant POIs. This is achieved by converting both the query and the POI descriptions into vector representations, followed by a similarity search.

- Flexible filtering and refinement of results: Users should be able to refine search results based on various criteria, such as the type of facility (restaurant, park, museum), rating, availability of certain amenities (accessibility for the disabled, Wi-Fi), as well as the current status of work (open now).

- Displaying detailed information about the POI: For each location found, the system should provide detailed information, including the name, address, coordinates, opening hours, contact information (phone, website) and an extended text description. This description will be enriched using LLM to provide a more complete and engaging context.

- User Data management: The system must support user authentication and authorization. Functionality is planned to save your favorite places and search history.

- Route generation (future expansion): It should be possible to expand to build optimal routes between selected POIs, taking into account time and preferences.

- Consideration of contextual factors (future expansion): The ability to integrate external data, such as weather conditions or the type of company (for example, places for family vacations, for meetings with friends), for even more personalized recommendations.

### Non-functional requirements:

- Search response rate: The system should respond to user requests as quickly as possible, aiming for a response time of no more than 1-3 seconds for most requests. This requires an efficient DLS architecture, optimized similarity search algorithms, and the use of a productive vector database.


- Scalability: The architecture of the system must be designed with horizontal scaling in mind to handle an increasing number of POIs (more than 50,000 objects) and an increasing number of simultaneous user requests without significantly reducing performance.

- Usability: The user interface should be intuitive, providing easy interaction when forming queries and navigating through the results.

- Security: The implemented authentication system (JWT) should provide reliable protection of user data and API access. All interactions must be protected.

- Maintainability: The project code should be clean, modular, and well documented to facilitate further development, testing, and support.
### Prioritized backlog

https://github.com/orgs/IU-Capstone-Project-2025/projects/16/views/1

## Project specific progress

### Frontend

- **Project setup & scaffolding**  
  Initialized the frontend codebase using Next.js, configured TypeScript support, and integrated Tailwind CSS for utility-first styling.

- **Core UI components**
  - **Search & filters**: Built a reusable `SearchBar` component with autocomplete, and a `FilterPanel` for type, rating, amenities, and “open now” toggles.
  - **POI list & detail**: Developed `PoiList` and `PoiCard` components to display results; created a `PoiDetailModal` for extended information.
  - **Map integration**: Integrated React Leaflet to render POI locations on an interactive map, synchronized with list selections.

- **State management & API integration**
  - Configured Redux Toolkit slices for search parameters and POI results.
  - Wired up API service layer (using Axios) to backend stubs for fetching and filtering POIs.

- **Routing & auth flows**
  - Set up Next.js dynamic routes for POI detail pages.
  - Implemented authentication UI: login, registration, and protected routes using JWT tokens.

- **Responsive design & accessibility**
  - Ensured mobile-first layouts, tested across breakpoints.
  - Added ARIA attributes and keyboard navigation to key components.

### Backend

Significant work has been done to set up the basic backend infrastructure, which includes:

- Database initialization: PostgreSQL is configured for data storage and Alembic for migrations.

- Authorization setup: An initial authentication system using the JSON Web Token (JWT) has been implemented, which provides secure access to the API.

- Preparing for API development: An API development environment has been set up, basic structures have been created for future endpoints, which allows you to start developing functionality in the near future.

### DLS

The key achievement in the DLS part of the project was the collection and preparation of the initial dataset of points of interest (POI). The following steps have been completed:

- Data collection: Using the Overpass API and OpenStreetMap, a POI dataset was collected for six main cities: Kazan, St. Petersburg, Moscow, Nizhny Novgorod, Ufa and Yekaterinburg.

- Filtering and enrichment: A POI filtering mechanism has been implemented and applied at the request stage to the Overpass API in order to exclude irrelevant objects (for example, banks, pharmacies) and focus on places of interest to tourists and leisure (museums, parks, shopping malls, restaurants, etc.). The dataset is enriched with additional information from Wikipedia and Wikidata, which significantly improves the quality of the text descriptions for each POI.

- Dataset size: Currently, about 50,000 unique and relevant objects have been collected.

- The prospects: The possibility of using the Large Language Model (LLM) API to further enrich POI text descriptions is being considered, which will allow for deeper and more contextual vector representations. This will ensure a more accurate and relevant search.


# Weekly commitments

## Individual contribution of each participant

### Emil Goryachih

- Active participation in the backend setup: Contributing to the initial configuration of the backend infrastructure, including the database configuration (PostgreSQL) and the implementation of JWT-based authorization, laying the foundation for further API development. (https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/c9c9514ecc7aa6b7183170722faacd211dbdc37b)

- Collection and primary processing of the POI dataset for the DLS system: Complete completion of collection and primary processing of the dataset of points of interest, including filtering of irrelevant objects and data enrichment from Wikipedia/Wikidata. (https://github.com/IU-Capstone-Project-2025/EasyTravel/commit/86465bd60f7482d45ceae77822b2e0648c8c037d)

- Setting up Teamwork Tools: Participate in setting up GitHub Projects for effective task and schedule management. (https://github.com/orgs/IU-Capstone-Project-2025/projects/16/views/1)

- Research and testing of methods for enriching POI text descriptions (Wikipedia/Wikidata, LLM).

- Analyzing the collected data and preparing it for vectorization.

### Vlad Galkin
- Leading the frontend architecture: set up the Next.js project with TypeScript and Tailwind CSS.
- Implemented core UI components including the search bar with autocomplete, filter panel, POI list and detail modal.
- Integrated interactive map visualization using React Leaflet.
- Wired state management (Redux Toolkit) and API service layer for real-time search and filtering.
- Ensured responsive, accessible design across devices.

### Saidaziz Kadirov
- Wrote unit tests for critical components (Jest & React Testing Library).
- Started DevOps developement
- Organized team meets
- Checked report and team contributions 
## Plan for Next Week

- **DLS**:

    - Proceed with the selection and initial integration of a model for vectorizing text descriptions of POIs.

    - Perform a preliminary analysis of the vectors.

    - Start experimenting with LLM to enrich POI descriptions using available data center resources.

- **Backend**:

    - Develop and implement the first API endpoints for receiving and filtering POIs.

    - Start integrating the backend with the DLS part to get vectorized data.

- **Frontend**:

  - Refine and polish core UI components: enhance search bar UX, improve filter panel animations, and optimize PoiDetailModal transitions.
  
  - Complete integration between map and list: ensure clicking a map marker highlights the corresponding POI card, and vice versa.
  
  - Implement clustering of POI markers on the map for better performance and usability in dense areas.
  
  - Hook up real API endpoints once available: replace stub data with live POI fetches, and handle loading and error states gracefully.
  
  - Add end-to-end tests for main workflows (search, filter, POI detail) using Cypress.
  
  - Improve mobile navigation: build a responsive drawer menu and a bottom tab bar for quick access to search, favorites, and profile.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
