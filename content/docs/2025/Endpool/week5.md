---
title: "Week #5"
---

# **Week #5**

## Feedback


### Sessions

We conducted 4 inteviews with potential users. Although all users had no issues with navigating through menu, 3/4 had problems with understanding some key concepts of our functionality (e.g. shopping list creation menu, list with recipes offered, unclear termins (What is "Хранилище??")). Also one user asked, why ingredients that are manually taken from shopping list, do not automaticlly offered to be added to one of the storages. All users lacked the interaction with generated shopping list (e.g. popping the bought products). Although all users found the ingredients search feature for filling up the storage pretty convenient, the same feauture for deleting ingredients is very unconvenient. Also all users experinced troubles with small ingredients names mismatch (e.g. "масло сливочное" and "сливочное масло" are diffrent in our system, but in fact, they are not).

### Analyze

Feedback was extremely helpful for us in identifying possible mass user interaction troubles. We immediately created issues for boosting UX/UI experience for first priority (adding major using instructions, adding hints throught the bot`s menus, adding lacked functionality and refactoring the problematic existed ones) both on backend and frontend. Also the issue with database normalisation was created, which should be taken as soon as possible.

## Iteration & Refinement

### Implemented features based on feedback

We boosted UI in all menus, especially in shopping list creation menu and in offering recipes menu, and implemented CRUD on generated shopping list.  

### Performance & Stability

The only important metrics for our project - telegram bot`s response delay. It can be boosted by bying more expensive virtual machines and setting up load balancers, or rewriting the application to adequate stack.

### Documentation

We have meaningful in-code comments throught the code and clear instructions for setting up the dev environments in .MD files in all repositories. 



# Weekly commitments

## Individual contribution of each participant


| Team member                             | Contribution |
|-----------------------------------------|------------------|
|Maxim Fomin (Lead)|https://github.com/Endpool/CookCookhNya-frontend/pull/74 - implemented deletion from shopping list. https://github.com/Endpool/CookCookhNya-frontend/pull/71 - fixed bug of sending buttons with quotes in the name. https://github.com/Endpool/CookCookhNya-frontend/pull/69 - little helped Amirkhan with integrating ingredient search to the ingredient list.|
|Ilia Kliantsevich|https://github.com/Endpool/CookCookhNya-frontend/pull/72 - implemented creation, deletion, veiw and publication of custom recipes along with private account for managing all og this. https://github.com/Endpool/CookCookhNya-frontend/pull/72/commits/9f8644196e559dd021e7477ac0849a570abb559c - refactored design for viewing offered recipes.|
|Amirkhan Kurbanov|https://github.com/Endpool/CookCookhNya-frontend/pull/61 - implemented main menu. https://github.com/Endpool/CookCookhNya-frontend/pull/69 - implemented private account feature, with ability to create and publish custom ingredients. https://github.com/Endpool/CookCookhNya-frontend/pull/62 - did code refactoring.|
|Daniel Gevorgyan|https://github.com/Endpool/CookCookhNya-backend/pull/51 - tests for all storage endpoints. https://github.com/Endpool/CookCookhNya-backend/pull/52 -refactored db errors handling to be pure and simple. https://github.com/Endpool/CookCookhNya-backend/pull/64 - restructured code to prevent security issues (accesing someone`s else storage). https://github.com/Endpool/CookCookhNya-backend/pull/68 - tests for all invites endpoints|
|Vadim Ksenofontov|https://github.com/Endpool/CookCookhNya-backend/pull/67 - migrated base id from long ot UUID. https://github.com/Endpool/CookCookhNya-backend/pull/66 - implemented add storage spend products delete endpoint. https://github.com/Endpool/CookCookhNya-backend/pull/69 - implemented custom private ingredients CRUD.|
|Aleksandr Gorbanev|https://github.com/Endpool/CookCookhNya-backend/pull/64 - imlemented invites feature on backend. https://github.com/Endpool/CookCookhNya-backend/pull/61 - implemented ingredient search with thresholds.|
|Rashid Badamshin|Set up observability - http://10.90.137.177:3000/dashboards (accessible from university wi-fi for now only)|


## Plan for Next Week

- Implement remaining features that will cover the interviewed users wishes
- Feature for users to publish private ingredients and recipes
- Add more tests to backend
## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).

