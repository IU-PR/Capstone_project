---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

 #### MVP requirments:

Backend
- User login and registration
- Name of the profile
- Picture in the profile

Frontend:
- Possibility to rotate the map
- Possibility to open labels with fish pictures on the map
- Possibility to start the event of fishing
- User interface to add pictures of fishes

ML:
- Test model for ML

#### Final project
Backend
- User login and registration
- Name of the profile
- Picture in the profile
- Databases for all entities 

Frontend:
- Possibility to rotate the map
- Possibility to open labels with fish pictures on the map
- Possibility to start the event of fishing
- Fully functional form to add pictures of fishes
- Possibility to leave comments and have discussion of the fish locations
- Profile with all caught fish
- Level of user in profile

ML:
- Accurate model for ML to determine types of fish
- Fish database

### Prioritized backlog

[Link to Github](https://github.com/orgs/IU-Capstone-Project-2025/projects/19/)

Backlog for week 3 will be created soon
## Project specific progress

### Frontend

- Pages with Login, Register, Home, Menu, Settings, About, Profile, Catch, Notifications, Discussion skeleton pages with basic routing, map for future fishing locations was added

### Backend

- Create new entities: Fish, CaughtFish, Fishing and Water. Update initial fishers table adding photo column.

- Fish responsible for fish object itself, contains unique id, name, average weight and photo.
Fishing responsible for fishing event, contains unique id, start time, end time and fish were caught on the water.
CaughtFish responsible for fish caught during fishing.
Water responsible for the place where fishers could catch fish, contains unique id and coordinates (x, y)

Created register and login steps and added Fisher profile structure




### Design

- First prototype and userflow were created


### ML
#### Insights found:
- Fish_Dataset
  - here used only 9 types of fishes: Black Sea Sprat, Glit-Head Bream, Hourse Mackerel, Red Mullet, Red Sea Bream Sea Bass, Shrimp, Striped Red Mullet, Trout
  - But in our region only Trout can be useful
  - Think about rejecting this dataset or save for the time of upgrading the app
- Fish_Data
  - a lot of species which is great
  - after lookup there is no common species for Tatarstan
- FishImgDataset
  - this dataset have some familiar species for Tatarstan

### DevOps

- First CI/CD pipeline was created, nginx configured, pool for secrets was created

# Weekly commitments

## Individual contribution of each participant
Stepan Vagin:
- Created the first version of backlog in github, [link](https://github.com/orgs/IU-Capstone-Project-2025/projects/19)
- Organized meeting to define Final MVP and project requirments
- Created report
- Wrote new MVP and Project requirments, based on the team feedback

Kostya Zimin:
- Defined backend structure
- Docker-compose, dockerfile and described how to build backend. Created register and login steps and added Fisher profile structure, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/4)

Ivan Vasiliev:
- Explored existing datasets got some meaningful insights on relevance of the datasets [link](https://colab.research.google.com/drive/1FtPluhihg3swVpO5fyCh7DDB7kDe4C5E?usp=sharing)
- Found few more datasets to explore: [first link](https://www.kaggle.com/datasets/tarunkumar1912/fish-dataset1), [second link](https://www.kaggle.com/datasets/giannisgeorgiou/fish-species), [third link](https://www.kaggle.com/datasets/akashguna/fish-detection-dataset)
- Made cross-review of the figma design provided some design ideas

Kirill Greshnov:

- Implement frontend project structure, [link to PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/1)
- Added Login, Register, Home, Menu, Settings, About, Profile, Catch, Notifications, Discussion skeleton pages with basic routing, map for future fishing location, link to [PR_1](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/7), [PR_2](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/8)


Egor Belozerov:
- Setup github self hosted runner for CI/CD
- Configuring nginx as reverse proxy for https connection between flutter and java backend [domen](https://capstone.aquaf1na.fun/)
- Introduce sops for secret managing inside repo, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/9)
- CI/CD (cd need to be manually triggered), [PR_1](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/6), [PR_2](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/12)

Damir Sadykov:
- Created design sketches and userflows in figma, [link](https://www.figma.com/design/DBMIs26GU4KfwtITxK8BPT/FishMasters?node-id=0-1&t=D7lcAZkSX9YP476A-1)

Adel Gaznanov:
- Created new entities, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/21)
-  Created relationships between new entities, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/21)

## Plan for Next Week

 - Prepare project for mvp
 - Connect frontend and backend
 - Add new database entities and relations
 - Make an update version on design
 - Build test version of ML side of project
 - Add name and picture to the profile
 - All other things to meet defined MVP requirments
## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).