---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: @cookcookhnyabot
- **API Docs**: http://10.90.137.177:8080/docs

## Final deliverables

### Project Overview  

**CookCookhNya** is a smart cooking assistant that helps people find recipes based on what they already have at home. It solves a simple but common problem: when you open your fridge and don't know what to cook.  

#### What It Does  
- Shows you recipes you can make right now with your available ingredients  
- Creates shopping lists for missing items when you pick a recipe  
- Lets you save your own recipes and share them with others  
- Works for households - multiple people can use the same storage  

#### Main Features  
1. **Your Kitchen Storage**  
   - Add or remove ingredients you have  
   - See everything you've got in one place  

2. **Smart Recipe Finder**  
   - Gets recipe ideas based on what's in your kitchen  
   - Works with multiple people's storages combined  

3. **Shopping Lists**  
   - Automatically shows what to buy for recipes you choose  
   - Saves time and reduces food waste  
4. **Custom ingredients**
   - Unmentioned in our database ingredient? Add it by yourself!
4. **Your Recipes**  
   - Create your custom recipes and share them  



We made CookCookhNya to make cooking simpler and help people use what they already have. It's perfect for students, families, or anyone who cooks at home.

### Features

- Creating and deleting storages
- Viewing storages` members and ingredients
- Adding ingredients to storages
- Adding another users to storages
- Offering a user list of recipes based on ingredient in one or multiple storages
- Generating a shopping list for user based on missing ingrediens for chosen recipe
- Personal profile with ability to create custom ingredients and recipes, and even publishing them to public


### Tech stack

#### Backend 
- Scala 
- PostgreSQL
- zio - effect system
- tapir - endpoint definition
- quill & magnum - database management
- circe - json serialization
- zio-test - testing


#### Frontend
- C++
- Telegram
- TgBotStater (https://github.com/Makcal/TgBotStater) - main framework, used for Telegram bot development
- Boost - for working with JSON and UUID
- cpp-httplib - for communication with backend

#### Devops 
- Docker, Docker Compose - containerisation and orchestration
- GitHub Actions - CI/CD
- Loki, Promtail - log scapping and storing 
- Cadvisor, postgres-exporter, Prometheus - metric scrapper
- Grafana - visualisation
- Nginx - reverse proxy (for webhook setup)

### Setup instructions


1. Create a new directory;
2. Clone repo with
```bash
git clone git@github.com:Endpool/CookCookhNya.git
```
3. Run
```bash
git submodule init && git submodule update
```
4. Create a bot at [@BotFather](https://t.me/BotFather) (don't forget to enable inline mode in settings)
5. Create `.env` specifying your `BOT_TOKEN` in the same directory
```bash
cp .env.example .env
```
6. Run
```bash
docker compose up --build
```


# Weekly commitments

## Individual contribution of each participant

<table>
  <thead>
    <tr>
      <th>Team member</th>
      <th>Contribution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Maxim Fomin (lead + frontend)</td>
      <td>
        <ul>
  <li>Migration to UUID - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/83">PR</a></li>
  <li>Big refactor - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/84">PR</a></li>
  <li>Webhooks - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/94">PR</a></li>
  <li>Improved logging and webhook support in TgBotStater - <a href="https://github.com/Makcal/TgBotStater/compare/v0.3.8...v0.4.0">Changes</a></li>
  <li>Shopping list improvement - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/99">PR</a></li>
</ul>
      </td>
    </tr>
    <tr>
      <td>Ilia Kliantsevich (frontend)</td>
      <td>
                <ul>
  <li>Custom recipe connection to backend CRUD - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/92">PR</a></li>
  <li>Big refactor - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/84">PR</a></li>
  <li>Shopping list refactor- <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/93">PR</a></li>
  <li>Pagination for ingredient search in storage - <a href="github.com/Endpool/CookCookhNya-frontend/pull/93">PR</a></li>
</ul>
      </td>
    </tr>
    <tr>
      <td>Amirkhan Kurbanov (frontend)</td>
      <td>
        <ul>
           <li>API refactor  - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/95">PR</a></li>
  <li>Big refactor - <a href="https://github.com/Endpool/CookCookhNya-frontend/pull/84">PR</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Daniel Gevorgyan (UI/UX + backend)</td>
      <td>
        <ul>
  <li>Recipes tests - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/73">PR</a></li>
  <li>Migrate some of database layer from Magnum to Quill - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/74">PR</a></li>
  <li>Personal recipes crud - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/75">PR</a></li>
  <li>Authorize get suggested recipes endpoint - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/82">PR</a></li>
  <li>Custom recipes - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/83">PR</a></li>
  <li>Filter for /ingredients search - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/84">PR</a></li>
  <li>Custom recipes ingredients Add and Delete operations - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/86">PR</a></li>
  <li>Add DELETE /recipes/:recipeId endpoint - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/87">PR</a></li>
</ul>
      </td>
    </tr>
    <tr>
      <td>Vadim Ksenofontov (backend)</td>
      <td>
        <ul>
            <li>Moderator Interface - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/98">PR</a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Aleksandr Gorbanev (backend)</td>
      <td>
        <ul>
  <li>Ingredient creation fix - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/97">PR</a></li>
  <li>Ingredient publication req - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/96">PR</a></li>
  <li>Change models - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/94">PR</a></li>
  <li>Buy products - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/85">PR</a></li>
  <li>Search for recipe - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/80">PR</a></li>
  <li>Storage Ingredietns pagination - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/78">PR</a></li>
  <li>Shopping list pagination - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/77">PR</a></li>
</ul>
      </td>
    </tr>
    <tr>
      <td>Rashid Badamshin (DevOps)</td>
      <td>
        <ul>
          <li>Configured metrics endpoint for observability purposes - <a href="https://github.com/Endpool/CookCookhNya-backend/pull/81">PR</a></li>
  <li> Congiifured Prometheus to scrapping /metrics </li>
        <li>Visualised handlers response time in grafana </li>
        <li> Setup nginx reverse proxy service with self-assigned authority for webhooks integration</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Plan for Next Week

- DB normalisation
- Refactor
- Perfomance optimisation
- Moderation of custom ingredients and recipes
- Suggest spend products after cooking a recipe

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
