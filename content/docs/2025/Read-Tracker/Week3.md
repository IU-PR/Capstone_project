# **Week #3**

## Implemented MVP features

The platform now includes a core feature: the Read Tracker, which is integrated with a calendar to allow users to view their reading streaks. 
Additionally, functionality has been added for users to write personal notes and leave reviews on books. 
Several user interface screens have also been developed, including Main Page, My Profile, My Books, My Reviews, and My Collections.

## Demonstration of the working MVP
https://disk.yandex.ru/d/ZsQcL-Vqy4elhQ

## Internal demo

### Frontend part

- Main Page:
Main page should display new reviews from subscriptions, not books

- My Profile page:
Calendar is too big and button "I have read today" is too small. We need to fix this

- The User Book page has bug that cover of the book is placed in the middle of page. It should be moved to the left side

- My Collection page also has bugs with covers of the books and text

### Backend part

- The authorization still under construction

- Not all errors are handled

- Not all exist endpoints are tested

- Not all endpoints are implemented

### Database

- The initial dump of the books data is missing

# Weekly commitments

## Individual contribution of each participant

Batraz created database functions, which in turn Ivan Isakov and Daria used in the handlers of the review (Daria), 
notes and tracker (Ivan). Ivan Savelev worked on the frontend for these three core features, and Andrey helped him with this. 
Andrey also made sure that the frontend and backend started functioning together and launched the application on the server. 
Dasha wrote a report and assigned tasks for the week. All the changes are in the relevant branches.

## Plan for Next Week

- Make authorization
- Add more books to the database
- Implement collections
- Test handlers and database, fix if it needed

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
