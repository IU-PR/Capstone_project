---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *CookCookhNya*

Code repository:  https://github.com/IU-Capstone-Project-2025/CookCookhNya

#### Description
CookCookhNya is a smart service, which helps people to find recipes based on products they have in fridge and create grocery list which considers products they already have and recipe requirements.
#### Problem Statement 
People have ingredients but don't know what to cook. Our project will keep track of list of products that you have and will suggest recipes for them based on their preferences.



### **Team Members**

| Team Member                             | Telegram Alias   | Email Address   | Track                                       | 
|-----------------------------------------|------------------|-----------------|---------------------------------------------|
| Maxim Fomin (Lead)     | @maximf3 | m.fomin@innopolis.university | Frontend (C++) |
| Ilia Kliantsevich            | @ilia852 | i.kliantsevich@innopolis.university | Frontend (C++) | 
| Amirkhan Kurbanov            | @s3rap1s | am.kurbanov@innopolis.university | Frontend (C++) | 
| Daniel Gevorgyan           | @danielambda | d.gevorgyan@innopolis.university | UI/UX + Quality Assurance | 
| Vadim Ksenofontov           | @Leropsis | v.ksenofontov@innopolis.university | Backend (Scala) | 
| Aleksandr Gorbanev | @ben_joyce | a.gorbanev@innopolis.university | Backend (Scala) | 
| Rashid Badamshin | @j0cos | r.badamshin@innopolis.university | DevOps + Report writer |


## Brainstorming

### Ideas during brainstorming

Throughout discussion we thought about the following ideas:
1) P2P messanger. Simple messanger, which main advantage (and specific) is P2P architecture.
2) Video streaming service (like Youtube). That idea itself quite complicated, so we though that basic features of youtube would be enough.
3) Dogsitter service. Service similar to dating apps but for pet owners to find dogsitter and vice versa.


### Brief market research / problem validation
We researched market for the similar services, which already exist and found the following:
* [Supercook](https://www.supercook.com/#/desktop)
* [Samsungfood](https://samsungfood.com/recipe-box-app/)
* [Paprikaapp](https://paprikaapp.com/)


Considering the large amount of people in russia who cook home ([this](https://mayaksbor.ru/news/society/kak_chasto_rossiyane_gotovyat_domashnyuyu_edu_rezultaty_oprosa/?ysclid=mbs78304yv466886804) website provides survey) we come to conclusion that service, which will optimise and enhance cookng experience is in demand. 

Analogical services like samsungfood are great examples, however it's not localised for Russia. Paprika app and Supercook are good working services also, but in it products can be added only by hand, which is tiresome for user. 


## Basic requirements

### Target users and their primary needs
#### Target Users
* Students
* Grandmas with dementia
* Homecooks

#### Needs
* Have a list of available ingredients
* Get recipes based on ingredients that user has
* Have clear grocery list in hand

### User stories
* As a user, I want to add or remove ingredients from my kitchen storage so that the system always reflects what I have available.
* As a user, I want to scan grocery receipt  so that the system automatically adds new ingredients.
* As a user, I want to automatically create a grocery list based on missing ingredients for recipes so that I know what to buy.  
* As a user, I want to receive recipe suggestions based on my available ingredients so that I can easily decide what to cook.  
* As a user, I want to modify recipes and ingredient preferences so that the system better fits my cooking habits.

### Initial scope
IN:
* Simple* search for recipes
* Manual storage (in service) filling
* Creating grocery list

OUT:
* Advanced* search for recipes
* Storage (in service) filling by QR code of receipt
* Recipe recommendation system (based on storage content)
* Ability to change saved recipes

"Simple" and "Advanced" search types are classified by accuracy, quantity of recipes and variety it. 

## Tech-stack
| Field                             | Technology |
|-----------------------------------------|------------------|
|Frontend | C++  & telegram API|
|Backend|Scala & Zio framework|
|Database|PostgreSQL|

We believe that our technological stack is justified by perfomance and efficiency of C++ and Scala being scalable, functional, high-level and concise programming language.

# Weekly commitments

## Individual contribution of each participant
| Team member                             | Contribution |
|-----------------------------------------|------------------|
|Maxim Fomin (Lead)|Created [boilerplate](https://github.com/Endpool/CookCookhNya-frontend/commit/7d109990622867c2722336baa808a5d4ea6d631f) for telegram bot and repo itself|
|Ilia Kliantsevich|Created report merging toghether information and notes of group|
|Amirkhan Kurbanov| Recorded important [notes](https://docs.google.com/document/d/1aenhNZ6kAU-TjWsPBzH2w8j92kIUYm-1taXHXUCKAHg/edit?usp=sharing) from group meetings|
|Daniel Gevorgyan| Found services similar to CookCookhNya ([Supercook](https://www.supercook.com/#/desktop), [Samsungfood](https://samsungfood.com/recipe-box-app/)) and created [document](https://docs.google.com/document/d/1aTwwhphUXfrhAbGrF3jY31zj9AtmUjediO8awceY4HQ/edit?tab=t.0#heading=h.ukd1y9r1l6zl) about overall idea of CookCookhNya|
|Vadim Ksenofontov|Found services similar to CookCookhNya ([Paprikaapp](https://paprikaapp.com/)) and contributed to market research|
|Aleksandr Gorbanev|Created [backend boilerplate](https://github.com/Endpool/CookCookhNya-backend/commit/0be48a5861fd166893a68b4d38c70a53e5fa59ef)|
|Rashid Badamshin| Made compose.yml file|

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).