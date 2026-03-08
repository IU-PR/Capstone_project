# **Week #6**

## Links

- **Deployment**: http://read-tracker.ru/
- **API Docs**: https://github.com/IU-Capstone-Project-2025/Read-Tracker/blob/main/backend/docs/openapi.yaml
- **Design** && **Demo**: https://disk.yandex.ru/d/tpxdMhDVn66B3g

## Final deliverables

### Project overview

Read-Tracker is a multifunctional web application designed to help users manage and enhance their reading experience. It
allows users to track their daily reading activity, maintain a personal digital library, write and read book reviews,
create and share thematic book collections, and organize a "Next to Read" list.

### Features

* Ability to mark the fact of reading for the day to view statistics.
* Adding a book to the "Read" / "Want to read" list.
* Writing a review of the book you have read.
* Creating collections (selections) of books.

### Tech stack

- Python
- Fast API
- Vue + CSS
- JavaScript
- SQL Alchemy
- PostgreSQL
- Docker

### Setup instructions

Open your terminal and run these commands:

```bash
    git clone https://github.com/IU-Capstone-Project-2025/Read-Tracker.git
    cd Read-Tracker
    make docker-build-up
```

The website is running on localhost:8080

Backend handlers are accessible on localhost:8000

To stop containers and clear the data run:

```bash
sudo make docker-clean-data
```

## Presentation draft

[*link to the presentation draft.*](https://www.figma.com/slides/qq9lfEJv8rsQzXwdkiQBVS/Untitled?node-id=1-36&t=hOS42iUa5FxbvFMx-1)

# Weekly commitments

## Individual contribution of each participant

Andrey

- Fixed the profile page and improved its data handling.
- Made minor UI adjustments, such as removing redundant buttons and adding a "Back" button.

Darya

- Implemented routes for retrieving the list of users from subscriptions.
- Created a project report and updated the README documentation.
- Started creating presentation.

Ivan Savelev

- Added a frontend page for subscriptions.
- Integrated review display into the book profile page.
- Implemented the ability to subscribe/unsubscribe after reading a review on the book profile page.

Ivan Isakov

- Fixed issues related to streaks, reviews, and tags on the backend.
- Performed code refactoring for improved maintainability.

Batraz

- Continued to support and expand methods for database operations.

## Plan for Next Week

Polishing the project and micro fixes and preparation to presentation.

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
