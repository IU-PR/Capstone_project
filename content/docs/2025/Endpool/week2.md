---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

### Functional Requirements

#### 1. Kitchen Storage Management
1.1. The system shall allow users to manually add ingredients to their kitchen storage by:
   - Entering ingredient name

1.2. The system shall allow users to remove ingredients by:
   - Deleting items individually

1.3. The system shall display a real-time inventory of available ingredients.


Note: we with decided to go from quantity management to not push users to use scales all the time. So if ingredient in the storage, it means it is enough for mahority of reciepies. If after cooking some ingridients are not enough for future usages, user should be offered to delete it from the storage.

---

#### 2. Grocery Receipt Scanning
2.1. The system shall allow users to upload images/scans of grocery receipts for processing.

2.2. The system shall extract ingredient names and quantities from receipts and auto-add them to the kitchen storage.

2.3. The system shall prompt users to confirm/correct extracted data before finalizing updates.

---

#### 3. Automated Grocery List Generation
3.1. The system shall allow users to select recipes they wish to cook.

3.2. The system shall compare recipe ingredients against the user's kitchen storage and identify missing items.

3.3. The system shall generate a grocery list containing missing ingredients

3.4. The system shall allow manual edits to the grocery list (e.g., adding non-recipe items).


---

#### 4. Recipe Suggestions Based on Available Ingredients
4.1. The system shall analyze the user's kitchen storage and suggest recipes that:
   - Can be made entirely with available ingredients.
   - Require minimal additional ingredients (configurable threshold).

4.2. The system shall allow filtering recipe suggestions by dietary preferences and cooking time

---

#### 5. Recipe and Preference Customization
5.1. The system shall allow users to copy and modify existing recipes by adding/removing ingredients

5.2. The system shall let users create and save new custom recipes.

5.3. The system shall allow users to set dietary preferences/allergies to filter suggestions.

---

### Future Features (If Time Permits)

#### 6. Computer Vision Ingredient Addition
6.1. The system shall allow users to point their phone camera at ingredients to to automatically detect ingredient names via computer vision and auto-fill storage entries.

6.2. The system shall support scanning multiple items on a kitchen counter.

6.3. The system shall provide fallback to manual entry if detection fails.

---

#### 7. Interactive Recipe Mode
7.1. The system shall provide a step-by-step cooking mode where with embeded timers.

7.2. The system shall allow pausing/resuming recipes and tracking progress.


---

### Non-Functional Requirements
- **Performance:** Inventory updates and suggestions load in <2 seconds.
- **Accuracy:** QR-code scanning and computer vision achieve >90% detection rate for common items.
- **Usability:** The user interface should be intuitive, providing positive experience.
- **Maintainability:** The project code should be clean, modular, and well documented to facilitate further development, testing, and support.

---

### Prioritized backlog

https://github.com/orgs/Endpool/projects/2/views/1?layout=board

---

## Project specific progress

### Frontend

#### 1. General user flow was designed
#### 2. An interface menu for viewing information about a specific storage and its users was created
#### 3. Functions handling addition and deletion of users were implemented
#### 4. The menu for selecting, deleting and creating existing storages was implemented
#### 5. Development infrastructure was improved

### Backend

#### 1. Endpoints for mvp version were defined
#### 2. PostgreSQL tables were defined

### DevOps

#### 1. Optimised building of backend service
#### 2. Configured hosting server and implemented continuous deployment via Github Actions
#### 3. Added cashing to C++ building dependencies in CD pipeline

# Weekly commitments

## Individual contribution of each participant
| Team member                             | Contribution |
|-----------------------------------------|------------------|
|Maxim Fomin (Lead)|Introduced frontend team to project structure and workflow. Improved developing infrastructure by adding Makefile and README.md with build instructions (https://github.com/Endpool/CookCookhNya-frontend/commit/411d139227e58c2e0a72f3a31baee9266a601e88). Provided linting configs (https://github.com/Endpool/CookCookhNya-frontend/commit/22e9f8875f7da9156dda345225e208509f6f6b5d). Started implementing backend and frontend interaction?(https://github.com/Endpool/CookCookhNya-frontend/pull/5) |
|Ilia Kliantsevich| Implement a menu for selecting, deleting and creating existing storages (https://github.com/Endpool/CookCookhNya-frontend/pull/2)|
|Amirkhan Kurbanov|Created an interface menu for viewing information about a specific storage and its users and implement addition and deletion of users on frontend https://github.com/Endpool/CookCookhNya-frontend/pull/3|
|Daniel Gevorgyan| Designed the userflows for MVP (https://drive.google.com/file/d/1Rnft1kc9A1IMNHlD7eLzL-7-DPn7zqkG/view?usp=drive_link), reviewed and merged Vadim's and Aleksandr's pull requests (https://github.com/Endpool/CookCookhNya-backend/pull/7), and contributed to defining ingredients storage endpoints (https://github.com/Endpool/CookCookhNya-backend/pull/9)|
|Vadim Ksenofontov|Defined ingredients endpoints (https://github.com/Endpool/CookCookhNya-backend/pull/6)|
|Aleksandr Gorbanev|Created database schemas (https://github.com/Endpool/CookCookhNya-backend/pull/5), added basic error handling (https://github.com/Endpool/CookCookhNya-backend/pull/6)|
|Rashid Badamshin| Configured hosting server and implemented continuous deployment via Github Actions (https://github.com/Endpool/CookCookhNya/actions). Link to hosted bot - [@tests040492005bot](https://t.me/tests040492005bot). Also optimised scala dockerfile (https://github.com/Endpool/CookCookhNya-backend/commit/49eed30d9c0f9cd0d08a920ae7bf79689e22117b)|

## Plan for Next Week

The main goal is to create all the endpoints required for mvp, configure the database and add connect backend for all endpoints on frontend. Also it is important to set up linting and basic testing in ci pipeline.



## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
