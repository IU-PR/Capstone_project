# Week #1

## Project description

### Project name: Read Tracker

**Code repository**: https://github.com/IU-Capstone-Project-2025/Read-Tracker

Our project is aimed at creating a multifunctional system for reading people. 
It includes: a tracker for reading, 
storing information about books read (when finished, a review of the book read), 
creating your own collections according to certain criteria (for example, "the 10 best books in the fantasy genre"). 
Thanks to our system, users will be able to track their reading progress and store information about what they have read, but they will also be able to share this information with others (if desired).

### **Team Members**

| Team Member                             | Telegram Alias   | Email Address                      | Track                                       | Responsibilities                                                                                                      |
|-----------------------------------------|------------------|------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Darya Tolmeneva (Lead)                  | @DinPg           | d.tolmeneva@innopolis.university   | Fullstack                                   | Reports, tracker functionality and database design                                                                    | 
| Andrey Torgashinov                      | @TovarishDru     | a.torgashinov@innopolis.university | DevOps                                      | Docker, testing, CI/CD                                                                                                |
| Ivan Isakov                             | @Muhozhukich     | i.isakov@innopolis.university      | Backend                                     | Creating the functionality of collections and what you have read (the fact that you have read + a review of the book) |                           |
| Ivan Savelev                            | @Savelev_IV      | i.savelev@innopolis.university     | Frontend                                    | Creating the entire front-end of our service                                                                          |
| Batraz Dzesov                           | @Borodum         | b.dzesov@innopolis.university      | Backend                                     | Creating an opportunity to view information about other users, subscribe to users                                     |


## Brainstorming

### Ideas during brainstorming
The project description has already added the ideas that we came up with during brainstorming, but below we will add information about the order in which the ideas appeared.

Firstly, we conducted the project idea brainstorming. Among all ideas we came up with the best ones were:
 - The application that will help to keep up with the study timetable and not be late. Was rejected due to lack of ideas that are not implemented yet by the majority of calendars
 - Some application that will simplify the communication between HR's and candidates. Ruled out to due to inability to create in the available short time any features that are not present in most applications for job search
 - The reader's diary with additional social functionality and rating systems. Was kept, we proceeded with it

The original idea is a tracker. But this is too trivial and it was necessary to develop the project somehow. That's why we had the idea to keep lists of what we've read and, accordingly, reviews of these books we've read. Then we decided that it would be nice to create our own collections of books (because they are more thematic and focused than just "I want to read"). After that, we thought it would be nice for users to share information with each other. But since this is not comfortable for everyone, we decided that the user will decide for himself what to share and what not to share. If he wants to stay completely private, then he will.

### Brief market research / problem validation

We conducted market research on the topic of our project, and want to emphasize two available solutions that we found:

[The first site](https://readed.me/books)
 - There is tracking, calendar, statistics, general database of books, reviews and rating
 - There is no way to make your own collections and share them.
 - It is not possible to subscribe to other users or read their collections.

   
[The second site](https://rj-ten.vercel.app/)
 - A simpler solution
 - You can track how many pages you read per day in a book
 - There are functions of a reader's diary, reading progress and statistics
 - There is no global literature list, all books are downloaded locally
 - No reviews, no global rating
 - The only way to share literature is through the creation of groups, where, again, all books are uploaded manually by the creator
 - There are no collections, as such, there are no user accounts to subscribe to and whose recommendations can be viewed.

Although the first site showed the functionality pretty close to our goals, we consider the social functionality of the application as
important as the tracking one. We expect that the ability to make and share collections of books will stand out favorably. The second
website we reviwed showed pretty poor communication abilities between users, adding which is one of our primary goals. To conclude, the
strong side of our application - the combination of reader's diary with broad rating and communication system - will be unique on the 
market amongst competitors.

## Basic requirements

### Target users and their primary needs

The target user is a person who reads and wants to track his progress (by the number of days he has read), 
as well as store information about what he has already read or wants to read and his reviews of the books 
he has read (which can be public or private, depending on the user's desire). In addition, the target user
wants to create collections of books (for example, "The top 10 books that everyone should read") that they 
can share with other users or keep secret. The user will be able to subscribe to other users to read their reviews, watch collections and progress.

### User stories
As a user I want to be able to mark what I've read today so that I can see statistics on how many days I've read this week/month/year.

As a user I want a convenient tool, where I can document books I have read, so I can track my reading activity.

As a user I want to have access to platform with ability to read others reports on books and create own, so I have easier time finding book worth my time.

As a user I want to make collections (e.g. "The top 10 books that everyone should read"), so that may be helpful for other users and maybe for me.

As a user I want to create "Next to read list", so it will be convenient to select the next book.

### Initial scope

**IN MVP**
- The opportunity to mark what I read today (as a fact). Accordingly, viewing the statistics of the days when user read
- The ability to add a book to the read/want to read list
- The ability to write a review of a book you've read
- The ability to create collections of books
- The ability to subscribe to other users and view information that the user has allowed to watch
  
**OUT MVP**
- Personalized suggestions for what to read based on what you've read before
- The ability to add the number of pages of a book and mark which page you are on now to see how many percent have been read
- The ability to view detailed statistics for a period of time (genres of books, number of reviews, number of pages read)
- The ability to discuss a specific book with users through comments under the review
  
## Tech-stack

- HTML + CSS
- Javascript
- Python
- Fast API
- Flask
- SQL Alchemy
- Postgre SQL
- Docker

## Something else you want to add 
At this point, it is important to explain the difference between collections and "want to read" lists. The collection can contain both books that you have already read and books that you will read. The collection has a specific theme, and the books in it can be arranged in the order in which it is worth reading, so that it is clear (because an unprepared reader may not understand certain literature). So the collections are more of an inspiration. The user can save/create many collections, but the reading plan will still have some direction (it is unlikely that he will be able to read books from 10 collections at the same time). He may set a plan to read all the books from the "Haruki Murakami" collection by the end of the year, but he won't necessarily do it in a row. It will just create/save the collection and when he wants to read something from there, he will take it to his list of plans.

# Weekly commitments

## Individual contribution of each participant
**Darya:** wrote the [report](https://github.com/IU-Capstone-Project-2025/Read-Tracker/edit/main/Reports/Week1/Week1-Report.md). Commits: [7d378cf](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/7d378cf062b4a3127e98c45c0038897be1bf861a), [825633a](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/825633a85dafc50de693340b658412abb22a98b3), [1b5e814](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/1b5e8147375687ab7e88d48b2b3b80d4597436fb), [42ec874](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/42ec874791c2ea4b95ed1a08d1d500815b4df065)


**Ivan Savelev and Batraz:** сreated the directory structure and files, docker-compose and `README.md`. Commits: [81f2bc4](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/81f2bc47a05c99ca5ae052c91a389af96ade04ce), [2afb506](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/2afb5068c85e5b6b5dafb4b0744a6e4f734c977a), [df6981a](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/df6981a756a1210babcc767106881405407cf96c)


**Ivan Isakov:** studied the market and product analogues, recorded and structurized meetings' [milestones](https://github.com/IU-Capstone-Project-2025/Read-Tracker/blob/main/Reports/Week1/Extras/Brief%20project%20description.txt)


**Andrey Torgashinov:** studied the market and product analogues, redacted the report. Commits: [9f14484](https://github.com/IU-Capstone-Project-2025/Read-Tracker/commit/9f14484939d8e95c55554763acce133ff2495d57) and the last version of the report

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
