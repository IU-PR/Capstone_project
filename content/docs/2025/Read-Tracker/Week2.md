# **Week #2**

## Detailed Requirements Elaboration

### Prioritized backlog

https://github.com/orgs/IU-Capstone-Project-2025/projects/13

## Project specific progress

### Detailed user-stories
#### 1. Tracking reading activity

##### High-level User Story:

As a user I want to be able to mark what I've read today so that I can see statistics on how many days I've read this
week/month/year.

##### Expanded User Stories:

- As a user, I want to mark that I read today and collect streak to motivate me read tomorrow.
- As a user, I want to view a calendar of days I've read.
- As a user, I want to see a summary of my reading days.

##### Acceptance criteria:

- User can tap a "I have read today" button.
- The system records the date.
- The user can view his reading streak.
- The user can see his streaks on the calendar.
- The summary updates in real time after marking today's reading.
- If user don't read this day, the streak will be cancelled.

#### 2. Documenting read books

##### High-level User Story:

As a user I want a convenient tool, where I can document books I have read, so I can track my reading activity.

##### Expanded User Stories:

- As a user, I want to add a new book entry manually with title, author, language, description and cover.
- As a user, I want to mark a book as "finished" to add it to my history.
- As a user, I want to view a list of all books I have read.
- As a user, I want to be able to add notes for the book, so I can track my decisions through the book.

##### Acceptance criteria:

- User can create a new book entry by filling in required fields.
- "finished" status updates the reading history immediately.
- Read books appear in a user-books list and can be sorted by title, author and can be filtered by status or language.
- User can make and edit notes for any his book.

#### 3. Book reviews platform

##### High-level User Story:

As a user I want to have access to platform with ability to read others reviews on books and create own, so I have
easier time finding book worth my time.

##### Expanded User Stories:

- As a user, I want to write a review after reading a book.
- As a user, I want to search book reviews by other users.
- As a user, I want to see how many people have reviewed a given book.

##### Acceptance criteria:

- User can create a text-based review to a specific book.
- Reports are publicly visible and associated with usernames (or private if user do not want to share them).
- User may see other reviews from other user he saw.
- Book detail pages show aggregated list of user-submitted reviews.
- Reviews can be sorted by most recent or most liked/disliked (optional for MVP).

#### 4. Creating book collections

##### High-level User Story:

As a user I want to make collections (e.g. "The top 10 books that everyone should read"), so that may be helpful for
other users and maybe for me.

##### Expanded User Stories:
- As a user, I want to create a custom-named book collection.
- As a user, I want to add books from user-book list to this collection.
- As a user, I want to view and edit my collections later.

##### Acceptance Criteria:
- User can create a named collection (e.g. "The top 10 books that everyone should read").
- User can add or remove books to/from the collection.
- Collections are visible on user’s profile and can be shared via URL (if it is visible).
- Each collection displays book titles and cover images.


#### 5. "Next to read" list
As a user I want to create “Next to read list”, so it will be convenient to select the next book.

##### Expanded User Stories:
- As a user, I want to create a list labeled "Next to read".
- As a user, I want to add and reorder books in this list.
- As a user, I want to mark a book as read directly from the list.

##### Acceptance Criteria:
- User can add a book to "Next to read" list with one click.
- Books can be manually reordered.
- Clicking "Mark as read" removes book from the list and adds to the "Read" section.
- The list is saved and persists between sessions.

### Frontend
During this week basic ideas of design were created and visualized in Figma:
https://www.figma.com/design/pYttfnV3jeoDErQZeNmGPj/Draft-on-Webpge?node-id=0-1&t=wZ5CilWZ10Wsiwfd-1

Materials are located on page named “Draft”. Later,based on desired functionality, personal ideas and preferences of whole team (during meeting) it was decided to make several changes in initial design.These changes were taken into consideration and documented as 2nd iteration(same page).

On the otherpage named “Interaction flow” documented navigational abilities of user.
HTML page was created, which has some most basic functionality of frontend part.

### Backend
During this week we created initial user-flow of the service, where you can check all possibilities user can
use in our application. After that, we created initial structure of our API.
https://miro.com/welcomeonboard/c09neEoyUkpXU1JkN3BZUks3V2lGWHlJZ0NTNU1KMmhIU2pkcU1kUUQ2aGRrOXpZamJueDVPVVBjMWFlUkxpWll6clpxNTFkcUdvV1hXOVlHbjdzTVN5UTdKclc0b2w5bENDTndsVXJOOEZ3VDlrMnk1Q0M5dDNSVFZZbGVLVjBQdGo1ZEV3bUdPQWRZUHQzSGl6V2NBPT0hdjE=?share_link_id=173411649380

You can check all router roots and endpoints of the API in the markdown file, API-contract. We design such router roots
as /books for all endpoints with books, /auth for all endpoints of authorization, /profile for changing password or
avatar of the user in the profile page, /collections for all endpoints with collections, /reviews for reviews, /notes
for notes, /subscribers for subscribers, /feed for all endpoints with subscribers info (e.g. new reviews or collections)
and /me for interacting with user books, reviews and collections.

Also, we implemented all structure of routers and all endpoints described before as non-functional for now. This
will help us to implement features in a structured and convenient way.

Moreover, our team designed the initial database schema. It contains all tables we need for our service. 
You can check all these things in the project directory.

# Weekly commitments

## Individual contribution of each participant
Batraz created a database schema and a query to create tables according to the schema.

Andrey created a Dockerfile for each component of the application, a common docker-compose on them, as well as a Makefile and helped review the code of Ivan Isakov and Ivan Savelev.

Dasha created a scheme according to which she wrote documentation for the API, wrote a report, created server and oversees the task board.

Ivan Isakov translated the API documentation into python code (so far only the structure).

Ivan Savelev created the design in figma and wrote the frontend.

Specific branches were created for each task, they can be found on the tasks tab.

## Plan for Next Week
Next week, we plan to finalize the frontend and backend for the key pages, as well as combine them together. We are also planning to try to run our service on the server.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
