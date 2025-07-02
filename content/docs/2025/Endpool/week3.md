---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features

In the MVP we focused on implementing basic management of ingredients/products in storages and search of recipes suggestions.
The application has a frontend in form of a Telegram bot and backend API.
Here is the full list of implemented features:
- At the start of using the app you are suggested to **create** your own **storage**.
- A user can own several storages as well as **delete them**.
- It is possible to **invite** any other **user** to a storage in order to share products.
- The main feature is to **put/remove ingredients** and products from a storage.
  At the moment of MVP it is done through the global list of known ingredients.
- The last but not the least feature is **recipe suggestions**.
  Based on the ingredients in storages (possible to use several simultaneously), you can get suggestion on what to cook
  sorted by the number of available ingredients.

## Demonstration of the working MVP

Here: [https://github.com/Endpool/Endpool/blob/static-files/static/2025/Endpool/MVP_demo.mp4?raw=true](https://github.com/Endpool/Endpool/blob/static-files/static/2025/Endpool/MVP_demo.mp4?raw=true)
(Probably you will need to refresh the page or explicitly copy the link to download the file)

## Local testing

The code can be run via `docker compose`.

Go to [https://github.com/Endpool/CookCookhNya-backend](https://github.com/Endpool/CookCookhNya-backend) 
and execute the following commands to run the backend.
API information will be available in Swagger on `localhost:8080/docs`
```bash
cp .env.example .env
docker compose up --build
```

Go to [https://github.com/Endpool/CookCookhNya](https://github.com/Endpool/CookCookhNya) 
and execute the same commands to run the whole application.
But don't forget to pass your Telegram bot's secret token in `.env`.

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
          <li>Code refactoring (https://github.com/Endpool/CookCookhNya-frontend/pull/12)</li>
          <li>Handle registration of users (https://github.com/Endpool/CookCookhNya-frontend/pull/27)</li>
          <li>Code style refactoring (https://github.com/Endpool/CookCookhNya-frontend/pull/28)</li>
          <li>Fix CI linting (https://github.com/Endpool/CookCookhNya-frontend/pull/30 & https://github.com/Endpool/CookCookhNya-frontend/pull/31)</li>
          <li>View and management of a storage's ingredients (https://github.com/Endpool/CookCookhNya-frontend/pull/32)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Ilia Kliantsevich (frontend)</td>
      <td>
        <ul>
          <li>Code refactoring (https://github.com/Endpool/CookCookhNya-frontend/pull/12)</li>
          <li>View of recipes suggestions (API client + suggestions list + recipe details view) (https://github.com/Endpool/CookCookhNya-frontend/pull/34)</li>
          <li>Fixes (https://github.com/Endpool/CookCookhNya-frontend/pull/36)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Amirkhan Kurbanov (frontend)</td>
      <td>
        <ul>
          <li>Handle registration of users (API client + handler) (https://github.com/Endpool/CookCookhNya-frontend/pull/27)</li>
          <li>Fixes and refactor (https://github.com/Endpool/CookCookhNya-frontend/pull/29 & https://github.com/Endpool/CookCookhNya-frontend/commit/4d036b0430a470208b1709b3e834c877680d5806 & https://github.com/Endpool/CookCookhNya-frontend/commit/55745f9f6ac6bd14914bb197b3d5ce6e8021d494)</li>
          <li>Selection of storages for recipes search (https://github.com/Endpool/CookCookhNya-frontend/pull/33)</li>
          <li>Translated interface to Russian (https://github.com/Endpool/CookCookhNya-frontend/pull/35)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Daniel Gevorgyan (UI/UX + backend)</td>
      <td>
        <ul>
          <li>User flow for MVP - continuation (<a href="https://github.com/Endpool/Endpool/blob/be189359c350e57a2e4f743718aeedf80582138a/static/2025/Endpool/MVP_userflow.pdf?raw=true">https://github.com/Endpool/Endpool/blob/be189359c350e57a2e4f743718aeedf80582138a/static/2025/Endpool/MVP_userflow.pdf?raw=true</a>) </li>
          <li>Code refactoring (https://github.com/Endpool/CookCookhNya-backend/pull/12)</li>
          <li>Use of .env (https://github.com/Endpool/CookCookhNya-backend/pull/13)</li>
          <li>Code refactoring 2 (https://github.com/Endpool/CookCookhNya-backend/pull/28)</li>
          <li>Fixes and refactoring (https://github.com/Endpool/CookCookhNya-backend/pull/30)</li>
          <li>Managing a storage's members (https://github.com/Endpool/CookCookhNya-backend/pull/31)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Vadim Ksenofontov (backend)</td>
      <td>
        <ul>
          <li>CRUD for storage management (https://github.com/Endpool/CookCookhNya-backend/pull/11)</li>
          <li>Code refactoring (https://github.com/Endpool/CookCookhNya-backend/pull/12)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Aleksandr Gorbanev (backend)</td>
      <td>
        <ul>
          <li>Saving users to DB (https://github.com/Endpool/CookCookhNya-backend/pull/14)</li>
          <li>Recipes suggestions (https://github.com/Endpool/CookCookhNya-backend/pull/32)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Rashid Badamshin (DevOps)</td>
      <td>
        <ul>
          <li>Docker composes for development purposes (https://github.com/Endpool/CookCookhNya-backend/pull/27)</li>
          <li>Updated CI/CD to be efficient and use newer versions of linter and formatter (https://github.com/Endpool/CookCookhNya-frontend/pull/26)</li>
          <li>Added database to Docker compose (https://github.com/Endpool/CookCookhNya/pull/28 & https://github.com/Endpool/CookCookhNya/pull/29)</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Plan for Next Week

- Finish refactoring
- Cover backend with tests
- Improve frontend UI (buttons layout, emoji, etc.)
- Recipe details view
- Global search of ingredients via inline query
- Ability to create custom recipes (and pull request them)

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
