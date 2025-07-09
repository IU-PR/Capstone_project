---
title: "Week #3"
---

# **Week #3**

## Deployment

Website with functionality: https://search.innohassle.ru  
API deployment: https://api.innohassle.ru/search/staging-v0/docs

## Implemented MVP features

We have implemented the basic functionality of user search. At the moment, text search in mongo works fully, ml-search works but requires testing. Closed issues see on the [board](https://github.com/orgs/one-zero-eight/projects/4), project `search`.

## Demonstration of the working MVP
![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week3/mvp1.png?raw=true)

![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week3/mvp2.png?raw=true)

![Image](https://github.com/belyakova-anna/Inno-Services-Search-Images/blob/main/Week3/mvp3.png?raw=true)

## Backend

Anna wrote an endpoint for running parsers and saving their results in mongodb (see [commit](https://github.com/one-zero-eight/search/commit/37af314d81d368746d06fe18c8e7c747c9e17142)) and implemented basic text search in mongodb (will be used if the ml-model is unable to process the request, see [commit](https://github.com/one-zero-eight/search/commit/da9f244dbba435eb22d7f8bab295eadd89b726d0))

Vladimir wrote an API for ml and wrote search logic (see [commit](https://github.com/one-zero-eight/search/commit/5440233f2a775a63dbb628818e2246eaada7c493))

Azaliia wrote a scheduler for periodically calling the parsing endpoint (see [commit](https://github.com/one-zero-eight/search/commit/5b7e2da273e9f418206754e008bbabd0cd47a219)).

Anna also refactored the code and bugfixed so that the backend and ml worked in a common pipeline (see [here](https://github.com/one-zero-eight/search/commit/aa367e27db3a9fd1dfb0f9d13f80c46d1fc93ce5) or [here](https://github.com/one-zero-eight/search/commit/8d666489f20c761049e5578f38b9b4c3a2be4a4f) or in other commits if needed).

## ML

Sofia connected the vector database (lancedb) and set up the ml pipeline (this [commit](https://github.com/one-zero-eight/search/commit/56ce6523b4e894f651878dcba85044fc970b3ee5)).

Azaliia wrote a function that updates the contents of lancedb (called when parsers are launched, [see](https://github.com/one-zero-eight/search/commit/075bbb8c75f814102ea22a28dbd909dce33f759e)).


## Frontend

Aliia completed the layout of components, connected the frontend with the backend (search, filtering; see [commit](https://github.com/one-zero-eight/website/commit/f738ee5070b87c9246f9ebb649b5e52889c54ce0))

## ML artefacts

At this stage of our work, our ml-part is implemented as a pipeline with a vector database, see the code [here](https://github.com/one-zero-eight/search/tree/main/src/ml_service)

In the future, we want to connect LLM for other functionality of our project (we assume that at the initial stage it will be one of the openai models and in the future a local model, for example ollama)

## Internal demo

The conducted testing revealed areas for improvement:
-  Add page anchors to links to lead the user to the desired section
-  Remove duplicate resources in ml search (the same link is issued several times because it appears in several chunks)
-  Improving the frontend (rethinking filtering options)

# Weekly commitments

## Individual contribution of each participant

| Team Member           | Contribution                                       |
|-----------------------|----------------------------------------------------|
| Anna Belyakova (Lead) | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week3/#backend) section     |
| Vladimir Paskal       | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week3/#backend) section                           |
| Azaliia Alisheva      | See [backend](https://capstone.innopolis.university/docs/2025/inno-services-search/week3/#backend) and [ML](https://capstone.innopolis.university/docs/2025/inno-services-search/week3/#ml) sections|
| Aliia Bashirova       | See [frontend](https://capstone.innopolis.university/docs/2025/inno-services-search/week3/#design--frontend) section |
| Sofia Pushkareva      | See [ML](https://capstone.innopolis.university/docs/2025/inno-services-search/week3/#ml) section                              |


## Plan for Next Week

### Main:
- Test the search
- Make the code readable, add logging
- Synchronize the team's understanding of the project code
### Other, priority TBD:
- Handle moodle resources
- Add resources for the current search pipeline (calling other APIs, parsing other resources)
- Write API for the ask section functionality

## Confirmation of the code's operability

**!!!** The working code in the backend repository is in the `main` branch, and in the frontend repository in the `capstone` branch (difficulties due to automatic deployment)
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).