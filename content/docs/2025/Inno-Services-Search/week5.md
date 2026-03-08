---
title: "Week #5"
---

# **Week #5**

## Feedback

### Testing session with TA

Suggestions:

- Add visual preview
- Think about the possibilities of moving to a specific text on the page

### Testing session inside the team
- Fix the format of md files for the correct text preview of search answer cards
- Fix the applicability of filters to search

### Testing session test sessions with potential users

Testing sessions were conducted in person, when users used our product for their needs and commented out loud on their intentions, actions and difficulties.

**Session #1:**

Search
- The user found the page a bit empty when first visiting it
- The user was confused by the search result for an empty string - unclear state of the website

Problem queries in search
- A search containing "108" or "one-zero-eight" does not return the desired club
- User queries that are not covered by our resources:
  - Coffee
  - Cafe
  - *any information about course instructors and schedule*
  - List of electives

Ask
- Consistency of the query and response language of LLM does not work
- The user expressed the opinion that a good feature would be to implement clarifying questions from the user
- The user tried to ask LLM what resources it uses

Problem queries in ask
- The user tried to find information about the heads of clubs, not all names gave a relevant answer

**Session #2:**

Search
- Our resources do not cover the query "schedule"
- The filter does not work if you remove all types of answers from it (pdf, website)

By design search
- Remove the dash in the "Web-site" text in the filters
- The text in the "Residents" filters is not self-explanatory - it is not clear what kind of resource this is
- The user said that he wants a longer description of the cards, otherwise it does not make sense
- During loading, he suggested making a blinking skeleton or a moving loading icon at least to make the state clear

Ask
- Error 502 was thrown for the request "calculate my scholarship for GPA 4.5"
- For the request "Please calculate my scholarship for GPA 4.0" LLM could not calculate a specific value because the minimum and maximum thresholds are unknown

**Session #3:**

Search
- For the request "campus" the website campuslife is returned, although information on dorms was expected

Ask
- For requests unrelated to Innopolis like "do you understand Russian?" AI gives an answer but puts a random resource of ours as a reference

**Session #4:**

Search
- For a request for which we cannot provide an answer, irrelevant answers are given
- Request not covered by our resources - "How to see my GPA"

Design
- On a mobile device, it is unclear what the search button is responsible for
- The filtering window needs improvement - the user noted that the window overlapping the page is not a typical look for this element

Ask
- If you ask something in binary code, it throws an error
- For the request "What is my name?" LLM answers with the names of professors
- A request not fully covered by our resources - "How to get innopoint"

**Session #5:**

Ask
- Is the Ashkazan canteen open? Answers that yes, although this is not the case
- Is it possible to bring a PC to the dorm? LLM answers that yes, but does not recommend registering it, which would be an important part of the answer

### Analyze

During the discussion, it was determined that we should focus on the UX/UI of our web page, the completeness of the data and its presentation in the search pipeline. Namely, we prioritized our tasks from the most important to the least.
- Add a visual preview of search sites (see closed [issue](https://github.com/one-zero-eight/search/issues/109))
- Fix a text preview in answer cards (see [issue](https://github.com/one-zero-eight/search/issues/107) and commits [#1](https://github.com/one-zero-eight/search/commit/9ab96a72f7bbde7daa1e25b0a7043d52e65fc352), [#2](https://github.com/one-zero-eight/search/commit/8f9e09d5d9be5e18dee6d2fdef49086bdde26f9c), [#3](https://github.com/one-zero-eight/search/commit/c05fee0664b9920327f62cdcfcbb9679155de8fa))
- Fix LLM for answers in the same language as the request (see commits [#1](https://github.com/one-zero-eight/search/commit/57c61275a7ed05f69ea93ded9a5c0889313365e8) and [#2](https://github.com/one-zero-eight/search/commit/ddab02391ab11b962387f4c408bfd468b4b4176f))
- Expand the pool of resources used by the search (see closed [issue](https://github.com/one-zero-eight/search/issues/112))
- Give the user answers and resources only if they are relevant to him (see [issue](https://github.com/one-zero-eight/search/issues/113))
- Make minor adjustments to the frontend (labels, filter fixes) (see [commit](https://github.com/one-zero-eight/website/commit/2550f10928cb661fbfce0407b28d7dce368cbda0))

## Iteration & Refinement

### Implemented features based on feedback

As you can see from the task artifacts, our team has closed/made progress on almost all tasks. In addition, our team has been working on general advancement of the project functionality, see the ["Project development" section](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#project-development).

### Performance & Stability

For our project, it is important to provide answers to users' search queries relatively quickly. Therefore, we mainly measure our performance in two metrics:
- **Response time for a search query.** Most search queries do not exceed 1 sec, the average time to receive a response from the backend = 0.98 sec.
- **LLM response time.** At the moment, almost all queries are processed in less than 10 seconds, while the average time for a request to LLM = 4.25 sec.

We are satisfied with the current state of the metrics and our task is to monitor them so that the results do not worsen with an increase in the number of sources and the addition of new features.

### Documentation

In our project we have documentation in the form of:
- [README](https://github.com/one-zero-eight/search/blob/main/README.md) - a typical way of documentation for team members and potential contributors, includes:
  - Project description
  - Technology stack
  - Project launch instructions
  - Contribution guide
- [Swagger](https://api.innohassle.ru/search/staging-v0/docs) - uses openapi scheme to facilitate the work of frontenders (automate their routine), synchronize developers
- Code comments - will allow developers who are not currently involved in the development to quickly understand the project if they wish.

### ML Model Refinement

This week we checked user testing, as a result of which we found problems with:

Search:
- Queries containing "one-zero-eight" do not give the expected results (there is no club among the answers)
- Not all queries for university room numbers give the expected results
- When there are no relevant answers to a question, the result is still given

Ask:
- The language of the query and the answer does not match (fixed)
- When the answer does not use our knowledge base (the assistant answers that there is no data for the answer), our resources are still indicated in the list of sources

Some of the tasks were fixed or we started the process, some are left for future weeks. At the moment, we also have a [dataset](https://docs.google.com/spreadsheets/d/1Q9SwNH2yBCkL_TCIoj3L1JRfgEZlX-Zc5eADguABHoQ/edit?gid=0#gid=0) for testing the operation of our models and can use it if desired. In the future, we are considering the possibility of automating model testing.

## Project development

### Testing

**Vladimir** was writing integration and ml tests to ensure ml service works correctly and interacts with backend service properly (see commits: [#1](https://github.com/one-zero-eight/search/commit/b53ccec046bf4c115487c557abab4743c55e44c0), [#2](https://github.com/one-zero-eight/search/commit/91619241f5d91d1ede609e05c48f997ed5c5a37f), [#3](https://github.com/one-zero-eight/search/commit/a70360f20722be3df71920388de4d34b270be662), [#4](https://github.com/one-zero-eight/search/commit/48c35b1a08c826ee4a2b6f49003fa7d9dbe8a7b0), [#5](https://github.com/one-zero-eight/search/commit/d474f85b45e01052deaba57e66e9b32b64df45a1), [#6](https://github.com/one-zero-eight/search/commit/6d51a4acc01abb0d75e4d2546105b32c098fd5f5)). More precisely, **Vladimir** wrote the code to preparse test data from sources and save it locally to use it in test mongo database for integration tests. Then implemented (partially , main part) core code(fixtures, test case) for integration tests. Spent many time to overcame problems with wrong fastapi initialisation for tests. Since ml database can be used locally, in the first prototype it processed again and again for each test running. However in reality it takes incredibly much time to index all documents from test mongodb, so it was decided that we should write pipeline to prepare test data - parse it from sources, load in temporary mongodb, then index all documents used powerful hardware and save this data for lancedb locally, so there will be fast initialisation in integration tests.

**Anna** conducted testing sessions with TA, within the team, with five potential users (see [feedback section](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#feedback)). From the feedback received, **Anna** identified relevant notes and formed issues, prioritized them and assigned them to team members (see [Kanban board](https://github.com/orgs/one-zero-eight/projects/4), `search` project).


### Backend

To correctly display the preview text of search results, it was necessary to provide MD files that the frontend could process. To do this, **Anna** adjusted the parser [hotel](https://github.com/one-zero-eight/search/commit/9ab96a72f7bbde7daa1e25b0a7043d52e65fc352), [campuslife](https://github.com/one-zero-eight/search/commit/8f9e09d5d9be5e18dee6d2fdef49086bdde26f9c), eduwiki (see commits [#1](https://github.com/one-zero-eight/search/commit/fab53e73499a8d1ca07102ce16ac887e6f6ac75c), [#2](https://github.com/one-zero-eight/search/commit/c05fee0664b9920327f62cdcfcbb9679155de8fa)). For a more meaningful search, the parser of the residents' site was [refactored](https://github.com/one-zero-eight/search/commit/a659da4e9f8acbd71a861006bb45039a283b2a91). To improve the visual presentation, the map processing pipeline was [refactored](https://github.com/one-zero-eight/search/commit/6b24f1231f96f3cb40f4575fca28837d67a539c8).
During site testing, we caught the 502 error several times, so Anna debugged it (see [#1](https://github.com/one-zero-eight/search/commit/5b581f338ed477d0e41e98d7d87642d537379ac7), [#2](https://github.com/one-zero-eight/search/commit/ab10bd0fbfc29d11f70070f4a1e0327e67015f02)) and [refactored](https://github.com/one-zero-eight/search/commit/582f00c3fb12112a00c8cd2e3fe93bd3955e54bb) the code for a more pleasant presentation in swagger.

**Azaliia** implemented ask statistics saving to MongoDB (see [PR](https://github.com/one-zero-eight/search/pull/110)), enabling the tracking of user queries to support analytics and in future response optimization. **Azaliia** also implemented static sources processing (see [PR](https://github.com/one-zero-eight/search/pull/111)), ensuring efficient handling of predefined data ([InNoHassle](https://innohassle.ru) and [My University](https://my.university.innopolis.ru)).

### ML

**Sofia** implemented:
- One of the modules for act - booking module for “music-room” (in progress, not fully correctly implemented): added Pydantic schemas, implemented ActRepository and FastAPI routes (see [branch](https://github.com/one-zero-eight/search/tree/ml_service/act))
- Use-cases  for act: documented core scenarios (see [document](https://docs.google.com/document/d/1kmtuAYrolJmltc42D2UO6__dpliRdL0RoGDdJp2vx0A/edit?usp=sharing))
- Map-based search improvements (in progress): attempted to align numerical room identifiers with database entries by full-text search, adjusting parsing and query logic, but the issue remains unresolved (see [branch](https://github.com/one-zero-eight/search/tree/ml_service/details))
- Bilingual Q/A support: enhanced language layer so that, even if database resources exist only in Russian, users can query in English and receive English responses and the same way on Russian (see commits [#1](https://github.com/one-zero-eight/search/commit/57c61275a7ed05f69ea93ded9a5c0889313365e8) and [#2](https://github.com/one-zero-eight/search/commit/ddab02391ab11b962387f4c408bfd468b4b4176f))

### Frontend

**Aliia** made:  
- [First PR](https://github.com/one-zero-eight/website/pull/214): Connected a new endpoint /ask/ and implemented fetchAsk with the POST method. Added the download and display of the AI response on the AskPage page: the "Thinking..." status is displayed while waiting for a response and the result is displayed with source. Refactored the AskPage and AskResult to match the response structure from the API. Added the TruncatableMarkdown component for the correct display of markdown content
- [Second PR](https://github.com/one-zero-eight/website/pull/219): Added a new IframePreviewCard component to display website content inside an iframe. Updated the logic of displaying previews on SearchPage: depending on the type of source, either PreviewCard or IframePreviewCard is now rendered. Improved the TruncatableMarkdown component: added logic for more correct text cropping, depending on the type of source. Added the display of several unique sources on the Ask
- Other minor changes (see [#1](https://github.com/one-zero-eight/website/commit/81fb4ca8b9eb46354ac6509bd2ecb0aca22c4708), [#2](https://github.com/one-zero-eight/website/commit/be1ae9c3de0a479857ddeded4c712934f2a48718), [#3](https://github.com/one-zero-eight/website/commit/ee68b29cc26b228903f1d06e79616f7288f785c6), [#4](https://github.com/one-zero-eight/website/commit/626df7dd63ce35cf2b5af11fabb129d47d3cfeb3)).

**Anna** [corrected](https://github.com/one-zero-eight/website/commit/3964dd29098ae65a48513ff892b32bd329d01f9f) the request sent to the backend (if you do not pass the source parameters to the search query, then a search will be performed on all sources, see the commit) and [enabled](https://github.com/one-zero-eight/website/commit/2550f10928cb661fbfce0407b28d7dce368cbda0) new sources for display (see the commit).

## Overall progress

Check our progress [here](https://search.innohassle.ru/search).

The most notable points of our progress this week are adding a visual preview for the `search` functionality, adding new sources (InNoHassle, My University). We also added a new `ask` section where you can get answers from the AI ​​assistant.

![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week5/search.png?raw=true)
![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week5/ask.png?raw=true)

# Weekly commitments

## Individual contribution of each participant

| Team Member           | Contribution                                       |
|-----------------------|----------------------------------------------------|
| Anna Belyakova (Lead) | See [testing](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#testing), [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#backend), and [frontend](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#frontend) sections |
| Vladimir Paskal       | See [testing](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#testing) section    |
| Azaliia Alisheva      | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#backend) section|
| Aliia Bashirova       | See [frontend](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#frontend) section |
| Sofia Pushkareva      | See [ML](https://capstone.innopolis.university/docs/2025/inno-services-search/week5/#ml) section                              |


## Plan for Next Week

- Rewrite the project to uv (faster than poetry, better resolves dependencies, more convenient CI/CD)
- Continue writing the `act` functionality
- Redesign the page
- Correctly display static resources on the frontend (divide them into cards of different types)
- Provide search results only if they are relevant
- Fix the search and ask for problematic queries

## Confirmation of the code's operability

**!!!** The working code in the backend repository is in the `main` branch, and in the frontend repository in the `capstone` branch (difficulties due to automatic deployment)
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).