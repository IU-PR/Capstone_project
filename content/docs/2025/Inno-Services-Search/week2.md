---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

### User stories with acceptance criteria

- **Keyword Search**  
  - User Story:  
As a user, I want to enter keywords and get a list of services that relate to them in order to find relevant materials.  
  - Acceptance Criteria:  
**Given:** the user is on the search page  
**When:** he enters keywords (e.g. "food", "sport") and clicks the search button  
**Then:** the system should display a list of links/resources related to these words  

- **Typo Support**
  - User Story:  
As a user, I want to be able to make a typo in the spelling of a word but still get a relevant result so that I have the opportunity to make a mistake.  
  - Acceptance Criteria:  
**Given:** the user entered a keyword with a small typo (e.g. "foood" instead of "food")  
**When:** he searches  
**Then:** the system should return relevant results as if he had spelled the word correctly  

- **Follow the link**  
  - User Story:  
As a user, I want to go to the resource issued by my request via a link to start using it.  
  - Acceptance Criteria:  
**Given:** the user sees the search results  
**When:** he clicks on the link (e.g. "Campus Life")  
**Then:** a new tab opens with the relevant site/resource  

- **Go to the desired section**  
  - User Story:  
As a user, I want the resource to open on click on the section I need in order to save time on manual search.  
  - Acceptance Criteria:  
**Given:** results show structured resources (e.g. Campus Life)  
**When:** a user clicks on a result that is related to a specific section of the site  
**Then:** they are taken directly to the relevant section within the page  

- **Sorting by Relevance**  
  - User Story:  
As a user, I want search results to be ranked by relevance, so that the most useful links appear first.  
  - Acceptance Criteria:  
**Given:** a user searches for a common topic (e.g. "108")  
**When:** relevance can depend on matching the title, keywords, context  
**Then:** results with a higher match score (by score) are displayed above  

### Prioritized backlog

[Kanban board](https://github.com/orgs/one-zero-eight/projects/4), see `search` project

## Project specific progress

### Design + Frontend
Anna and Aliia mage [user flow diagrams](https://www.figma.com/design/M4RIWYSKjVPz931J6nWERK/Search?node-id=0-1&t=CkxKvRmwUXQlwE5S-1). Later, Aliia made a [layout](https://www.figma.com/design/M4RIWYSKjVPz931J6nWERK/Search?node-id=12-2&t=HrHzzgtyEYvRmcDB-1) and a [clickable prototype](https://www.figma.com/proto/M4RIWYSKjVPz931J6nWERK/Search?node-id=12-2&t=HrHzzgtyEYvRmcDB-1) in Figma, approved it with [one-zero-eight team](https://t.me/one_zero_eight) (our customers) and made the appropriate edits. She also created some of the page components and routing (see [PR](https://github.com/one-zero-eight/website/pull/204)).

### ML
Parsers were written to collect data from different sources and convert data to the md format. Anna - a parser for Campus Life ([PR](https://github.com/one-zero-eight/search/pull/75)), Vladimir - a parser for eduwiki ([PR](https://github.com/one-zero-eight/search/pull/74)), Sofia - a parser for the dorm website ([PR](https://github.com/one-zero-eight/search/pull/76)), Azalia - integration with API maps ([PR](https://github.com/one-zero-eight/search/pull/77)).

### Backend:
The structure of interaction with the AI ​​was verbally defined (see the [architecture section](#architecture)), and endpoints began to be written. Anna began to write the mongodb scheme, endpoints for parsing data and writing to mongo ([commit](https://github.com/one-zero-eight/search/commit/6a5ead46fc5eb3bc7d59ce8d608f5b8f531de055)).

### Architecture:
It was clarified in detail for a better understanding of the API requirements.
- Mongo:  
Moodle is stored in mongo - information about courses (id and names, list of file names in the course). The files themselves are in minio (see below).
Separate collections for each resource (site - sports, foodwiki, etc.): link to the site/page, text in md format, page name, to send to the front and display not https://long_link... but just Handbook.

- Minio:  
stores large files (moodle pdfs). Runs on a separate server. Back can make links to files in minio.
Back sends to the front just links to these files - the user, if he wants to download a file, just clicks on the button and downloads this file by the link

- Vector base + embendings + LLM  
work as one system. See Week #1 for specific technologies.

- For `search` functionality:  
The user asks a question. Front sends it along with filters (return links or files, search in moodle foodwiki sports, etc.) as query parameters.
The backend sends this question along with the places to search (already json'ami) to the vector database + embeddings api. In the database, for each resource (eduwiki, etc.), the best candidates are selected independently of each other, then a set of id for monga and score (confidence in the answer) is returned to the backend. Then the backend, depending on the type (file or link), getting this information from monga, returns a list of answers to the frontend.

- For `ask` functionality:  
The user asks a question. The frontend sends it to the backend. The backend also accesses the vector database + embeddings api. The backend returns not id for monga, but the pieces of text from Moodle PDFs, parsed sites. Then the backend sends these pieces to the LLM api along with the user's question. LLM, taking into account the additional context, already produces something meaningful based on these texts. This is called RAG (thanks again to Ruslan). Then simply the LLM response is sent to the back, then to the front

- Updater:  
The database needs to be updated, for example, with new site parsing, with new files in moodle (already done).
It is necessary to delete records from the vector database, from mongo, upload them again to mongo, upload them to the vector database (along with new id's for mongo).

# Weekly commitments

## Individual contribution of each participant

| Team Member           | Contribution                                       |
|-----------------------|----------------------------------------------------|
| Anna Belyakova (Lead) | See [design + frontend](#design--frontend), [backend](#backend), and [ML](#ml) sections     |
| Vladimir Paskal       | See [ML](#ml) section                              |
| Azaliia Alisheva      | See [ML](#ml) section                              |
| Aliia Bashirova       | See [design + frontend](#design--frontend) section |
| Sofia Pushkareva      | See [ML](#ml) section                              |


## Plan for Next Week

- Finish the frontend components and implement the logic of interaction with the page
- Save all searches in database
- Add new sources (eduwiki, CampusLife, dorm, maps) into basic search pipeline
- Reimplement vector search with LanceDB or Chroma

## Confirmation of the code's operability

**!!!** The working code in the backend repository is in the `main` branch, and in the frontend repository in the `capstone` branch (difficulties due to automatic deployment)
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).