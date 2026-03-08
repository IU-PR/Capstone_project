# Week #2


## 1. Detailed Requirements Elaboration

### Project Goal</u>

<u>Build an AI-powered fashion assistant that helps users:</u>

- Choose clothing items based on their photo, figure, and style preferences

- Assemble capsule wardrobes and plan outfits

- See visual try-ons via 3D model

- Scollect images from real products from vb

### Outfit Recommendation Engine

<u>Input:</u>

- Color type (from photo)

- Body shape (from photo)

- Optional user style query ("I want something romantic for spring")

- Optional constraints: max price, preferred color, fabric, store

<u>Processing Logic:</u>

- Match the user profile to compatible items scraped from WB

- Apply filters (price, size, color, category)

<u>Output:</u>

- Visual list of 5–10 recommended items

- Ability to “save to favorites” or “add to capsule”

<u>UX Notes:</u>

- Each item shows image, size availability, price, store, and rating

- Visual badges: “Matches your figure”, “In your color palette”, etc.

### Capsule Wardrobe Generator

<u>Input:</u>

- User-selected styles OR system-generated suggestions

- Number of looks or days (e.g., “capsule for 5 days”)

- Preferred color palette and categories (tops, bottoms, outerwear)

<u>Logic:</u>

- Combine compatible items into 3–7 interchangeable outfits

- Use basic fashion rules: color harmony, proportions, layering

<u>Output:</u>

- Saved capsule with preview (grid of outfits)

<u>UX Notes:</u>

- Drag-and-drop feature for manual capsule editing

- Capsule preview = grid layout (Mon–Fr)

### 3D Try-On Preview

This is a very popular feature but within 7 weeks we plan to make a 2D avatar so that you can try on clothes and see the compatibility

the idea is to make the application more interesting for the user and lay the foundation for a future 3D model


### Scraping Wildberries (WB)

<u>Scrape periodically:</u>

- Title, price, photos, size availability, brand, composition

- User reviews and user-uploaded photos

- Store enriched dataset with parsed tags (e.g., boho, summer, organic cotton)

### Authentication & DB

- User login via email + password (JWT-based auth)

- DB tables: Users, Favorites, Capsules, Looks, BodyProfile [scheme]()

### Constraints & Challenges

- WB HTML structure may change — scraper must be modular and resilient

- Some fashion rules (like layering logic or trend-matching) may require manual curation for now

## 2. Prioritized backlog

[Link to kanban board](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/database/f226fd43-ad24-45a2-ac21-8f5c7684f4c6)

## 3. User flow diagram

[Link to diagram](https://drive.google.com/file/d/1LCBG4nfG-dhn5NuYnWl7PiuGGpm8rnvT/view?usp=sharing)
## 4. Updated / Detailed User Stories with Acceptance Criteria
#### 1. Set a Maximum Price

User Story:
As a budget-conscious user, I want to set a price limit so I don’t see unaffordable options.

Acceptance Criteria:

- User can define a price cap

- All items shown are below that value

- Price clearly visible on each card

#### 2. Show Only Available Sizes

User Story:
As a user, I want to see only items available in my size so I don’t get disappointed.

Acceptance Criteria:

- User sets size once

- Results show only items in stock for that size

- “Out of stock” labels or filters available


#### 3. Suggest Outfits for My Body Type

User Story:
As a user, I want outfit suggestions that suit my body type so I feel confident.

Acceptance Criteria:

- Personalized tips per figure

- Recommended styles for each type

- Visual examples provided

#### 4. Color Coordination Assistant

User Story:
As a user, I want help matching colors so my outfits look harmonious.

Acceptance Criteria:

- User can choose base color

- App suggests matching combinations

- Example looks with selected palette

#### 5. Jeans/Trousers for Petite Height

User Story:
As a petite user, I want trousers that fit me in length so I don’t look awkward.

Acceptance Criteria:

- Filter/tag for petite sizing

- Inseam info shown

- Height recommendation on item card

#### 6. International Size Conversion

User Story:
As a user, I want to see size conversions across countries and brands.

Acceptance Criteria:

- RU ⇄ EU ⇄ US ⇄ Asia chart

- Store-specific sizing guidelines

- Auto-convert based on user profile


#### 7. 3D Try-On

User Story:
As a user, I want to preview clothes on a 3D model of myself to check fit and look.

Acceptance Criteria:

- Avatar created from body parameters

- Clothes visually “worn” by avatar

- Can rotate and zoom in viewer

#### 8. Capsule Wardrobe Builder

User Story:
As a user, I want to build a capsule wardrobe to mix and match items easily.

Acceptance Criteria:

- Generate 5–10 item capsule sets

- Combinations previewed visually

- Save/edit capsule looks

#### 9. Weekly Wardrobe Planner

User Story:
As a user, I want to plan my weekly outfits to avoid daily stress.

Acceptance Criteria:

- Calendar interface for outfit slots

- Drag/drop saved looks

- Add notes like “rainy day” or “event”

#### 10. Smart Search with Tags

User Story:
As a user, I want smart search that understands my style keywords.

Acceptance Criteria:

- Search supports style terms (e.g., boho, minimalist)

- Keyword mapping to tags

- Filters adapt to description

#### 11. Boost Self-Esteem

User Story:
As an insecure user, I want positive feedback and suited suggestions so I feel good.

Acceptance Criteria:

- Friendly body-type feedback

- Focus on what suits, not flaws

- No negative language

#### 12. Filter by Country of Origin

User Story:
As a user, I want to choose the country of manufacture to avoid low-trust brands.

Acceptance Criteria:

- Show country flag/origin on product card

- Filter by origin

- Option to exclude certain countries

## 5. Interviews & anlysis
[Interviews & anlysis](https://drive.google.com/drive/folders/1yCxQriXf92pzZWRIAA2L-d7nqFIFgvtU?usp=share_link)


## 6. Project specific progress

<u>Backend:</u> almost wrote the logic for 2 features that will be included in mvp

<u>Design:</u> finished developing the design, held several meetings on this topic, discussed with the user

<u>Frontend:</u> started writing 1 of 4 pages that will be needed for mvp

<u>ML:</u> connected llm but it requires revision, created a simple model for determining the color, but have not connected it yet

<u>Deployment:</u> added to the docker file launch of llm and ml service, but due to ollama it does not work yet - we are launching them separately

<u>CMO:</u> agreed on advertising with a blogger in tg (audience of 15 thousand on instagram), after creating mvp or closer to the end of development we will conduct

<u>Public relation&CustDev:</u> conducted a survey, 60+ people took part, conducted several personal interviews - results at the [link](https://drive.google.com/drive/folders/1yCxQriXf92pzZWRIAA2L-d7nqFIFgvtU?usp=share_link)

## 7. Individual contribution of each participant

1) Ksenia Korchagina (lead) - conducting design meetings, design review, questionnaire review, compiling survey analysis, writing a report

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/140bfc095f068967360f19785ea0e2d20e12b32a)**

2) Yasmina Mamadalieva - training a model to determine color type, conducting interviews with young mothers

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/b856b61d61e6bfe6e2a8759b0c2efe5030dcf4ac)**

3) Aisylu Fattakhova - connecting LLM, writing the frontend, integrating the backend service with the LLM service, conducting interviews

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/2a97e2bf829037aa8213dc6954466ff2f196b7b4)**

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/58569f833c1a85d26281c118fd4a5f2e0b0dcaef)**

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/16e247e115223ed16d1a24c60443edd2dbc574d1)**

4) Ekaterina Akimenko - completed the design for the pages that will be included in the MVP, compiled a survey

**[Figma](https://www.figma.com/design/VHOnHId7DlFbgjnn46NGUW/StyleU?node-id=15-2&p=f&t=lgCLL10e3f1up4oQ-0)**

5) Sofia Goryunova - trained the model for the color type, improved its quality, compiled a survey and actively distributed it

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/10a6a51b9e2a5e0fe47874213b82ab4e01853bf4)**

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/c5bcb85196be73a86abeb6bf2d81881ce8112ce4)**

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/2f682915b257c147a46f6bcd96daeca4a7c888b4)**

6) Alena Starikova - almost finished writing the backend functions for mvp, conducted interviews

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/9829ec17c97d0500e278ea561c76b99439380407)**

**[commit in repo](https://github.com/IU-Capstone-Project-2025/styleU/commit/5f62f9bff2c7ece30eff911c9af03c4814dc21ad)**

7) Rokkel Maria - developed the design, started writing the frontend, conducted interviews

**[Figma](https://github.com/IU-Capstone-Project-2025/styleU/commit/2a97e2bf829037aa8213dc6954466ff2f196b7b4)**

**[Figma](https://github.com/IU-Capstone-Project-2025/styleU/commit/3a16b277d997abc05dc3e9c10312a15a01c565f1)**


## 8. Plan for Next Week
[23] FRONT transition to feature pages (w3)

[24] FRONT connect logic for 2 features with the back (w3)

[25] FRONT handle errors (w3)

[26] BACK test and finish connecting features

[27] BACK Upload everything to the main branch (w3)

[28] ML catch errors (w3)

[29] ML finish training the mode (w3)

[30] ML prepare a dataset for display (w3)

[31] ML Upload everything to the main branch (w3)

[32] FRONT Upload everything to the main branch (w3)

[Link to kanban board](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/database/f226fd43-ad24-45a2-ac21-8f5c7684f4c6)
