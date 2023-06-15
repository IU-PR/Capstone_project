# **Bookinng**
> Desirable room booking service at Innopolis University.

# **Week 1**

## **Team Formation and Project Proposal**

### **Team Members**

| **Member**                 | **Telegram**                                  | **E-mail**                           |
|----------------------------|-----------------------------------------------|--------------------------------------|
| Vladislav Deryabkin (Lead) | [evermake](https://t.me/evermake)             | v.deryabkin@innopolis.university     |
| Yaroslav Kivaev            | [catdog905](https://t.me/catdog905)           | k.yaroslav@innopolis.university      |
| Ekaterina Koshmanova       | [k_koshmann](https://t.me/k_koshmann)         | e.koshmanova@innopolis.university    |
| Vadim Zbarashchenko        | [metafates](https://t.me/metafates)           | v.zbarashchenko@innopolis.university |
| Ruslan Bakirov             | [monyter](https://t.me/monyter)               | r.bakirov@innopolis.university       |
| Anton Skorkin              | [PozhiloyProger](https://t.me/PozhiloyProger) | a.skorkin@innopolis.university       |

### **Value Proposition**

#### **The Problem**

Innopolis University offers students and employees the opportunity to book rooms
for personal use through the
[my.university.innopolis.ru](http://my.university.innopolis.ru/) website. While
this service is appreciated, there are several issues with the current process
of rooms booking that need to be addressed.

Currently, users must select a specific room and check its calendar for
availability. If a time slot is free, they can book the room by creating an
event in the calendar. This system is convenient if the user knows exactly which
room they want to book or if most rooms are available. However, when students
need a free room for a specific time slot they must check the schedule of every
room which can be time-consuming and frustrating.

Another related problem that we observe is that students and employees often
struggle to physically locate specific rooms, auditoriums, and offices in the
university building.

To justify the problems and make sure we are not the only one who have troubles,
we conducted a survey with 26 participants (excluding those who do not book
rooms and our team members). The results showed that:

1. Students in general actively use the rooms booking service.
2. More than a half of participants spend more than 5 minutes on average to
   choose and book a room.
3. Participants are generally dissatisfied with the usability of the current
   system. Furthermore, none of the participants rated the system's convenience
   as a five out of five.
4. Two-thirds of the participants would very much like to be able to see rooms
   available at a selected time interval, while a quarter found it to be a good
   idea. Almost the same for the ability to see available time slots for a
   specific room.
5. Over half of participants would appreciate a visual view of the room layout
   while booking.

![piechart_how-often-do-u-book-rooms.png](/bookinng/piechart_how-often-do-u-book-rooms.png)

You can find the complete survey results in the
[attached PDF file](/bookinng/Rooms-Booking-Survey-Report.pdf).


#### **Solution**

Both of the problems listed above can be solved by a service that provide a
convenient interface for choosing an available room in the university and a map
of each floor. User can check available rooms for a specific time, entering
period of time and see free rooms at this time on the graphical map (where free
and booked rooms will look differently helping a user to find an appropriate
room). Grouping all free room entering specific time helps to quickly find a
room within a specific time period. Also this service helps to get the position
of rooms in Innopolis University building having its name/number.


#### **Benefits To Users**

Time saving is the most valuable outcome for users from our service. We expect
these things to happen after we finish the project:

- Users will not have to scramble through the rooms to find a free one for the
  desired time slot;
- Users will find a free time slot for the selected room faster as this will
  be done in a more convenient way;
- Users will not run around a minute before the meeting to look for a room, as
  they will see the room locations on the map at the time of booking;
- An overall user experience will be improved by making the process of the
  events planning more pleasant.


#### **Uniqueness**

The proposed (tentative) system is better than the existing Microsoft Outlook
solution of room booking in different aspects:

1. It provides extra functionality for finding an available room;
2. It will show a visual representation of rooms location to help users find
   rooms;
3. It will have a mobile-friendly interface to simplify the booking process
   using a phone, which is usually most often at the fingertips of people.

One of our optional goals is to make the process of adding new building map
easily, that can make this project useful for others companies and took it to
commercial level.


#### **User Impact**

We believe that successful solution will not only improve users experience and
their productivity but also will highly affect on the university’s ecosystem
level. Such unique solutions make ecosystem more innovative and underline the
IT technologies in our university. 


#### **User Testimonials or Use Cases**

Use case of a building map — many shopping malls provides a digital map of the
building with description and navigation to specific shops that helps customers
locate different facilities. But these solutions usually implemented using
stationary displays. Another drawback of existing solutions is that they are
not globalized.


## **Lean Startup Questionnaire**

**1. What problem or need does your software project address?**

> The primary problem our project addresses is the inconvenience of the rooms
> booking process in Innopolis University.

**2. Who are your target users or customers?**

> Our target users are the university students and employees who take advantage
> of the rooms booking service.

**3. How will you validate and test your assumptions about the project?**

> We will give an opportunity to the users to try our MVP version’s and test
> our assumptions by measuring the performance and considering overall feedback.
> After that we will analyze the results and make decisions abou the testes
> assumptions.

**4. What metrics will you use to measure the success of your project?**

> We are going to make another survey similar to the mentioned above and make
> sure that performance has improved, users are happy with the interface and
> spend a minimum of time searching and booking rooms. We will collect the
> following metrics to evaluate our success:
> - Amount of reduction of the average booking time of a room;
> - Positive feedback from users — how much are they satisfied with the
>   interface and performance of our system.

**5. How do you plan to iterate and pivot if necessary based on user feedback?**

> We will see the main complaining points, ask for ideas from users and
> generate new solutions for these tasks. After that we will try to implement
> the best ones and once again give it for testing to users.

## **Leveraging AI, Open-Source, and Experts**

### **Artificial Intelligence**

Our team plans to use LLM code generation (GitHub Copilot) to make the process
of development faster, especially working with Outlook Calendar API, that is,
AI will help us find relevant API endpoints and their response schemas quicker,
than browsing documentation ourselves.

We are also considering incorporating AI-powered features  in our system that
will require use of AI, such as suggesting the best place and time for a meeting
based on a user's preferences and predicting room occupancy at different times
to help users make better decisions when booking a room.

### **Open-Source**

First of all, we are going to use open-source libraries and frameworks during
development. Particularly, for frontend part we are going to use either Vue.js
or React.js framework; for backend we will use one of the most popular
frameworks (Django or FastAPI for Python, Spring for Java), but it depends on
the programming language and stack we will agree on.

Secondly, we will also open-source all our code, which is not intended to be
private and may be useful for others.

### **Experts in Relevant Domains**

We have reached out to the individual involved with Innopolis current room
booking system. They have given their approval for our proposal and will be
available to assist us whenever any issues arise.

## **Inviting Other Students**
We found out that there is a group of first year students who are working on a
Software Project to create a Telegram bot for rooms booking. We have contacted
them and plan to discuss combining our projects to add a Telegram bot to the
system. If we will agree to work together, we can get the project done faster
and better.

## **Vision Of The Project**

### **Overview**

We want to create a service for convenient booking rooms. A lot of people have
difficulties with finding rooms, checking accessibility of a rooms and finally
booking them. Our project will try to solve these problems.

### **Schematic Drawings**

We do not have a clear understanding of which components will we have in our
system and how will they communicate, but we can share our our current view of
what the system’s core components may look like on the diagram:

![components-diagram.png](/bookinng/components-diagram.png)

There are two core parts:

- Backend — responsible for handling booking requests and managing database
  operations.
- Web-interface — user-facing aspect of the project, what the user will see and
  interact with.

Additionally, we are considering incorporating a Telegram Bot as an optional
feature, but we have not yet decided whether to implement it or to ask for help
from first-year students for its development.

### **Tech Stack**

We have not yet decided about our stack, but we have some ideas. For frontend
part we are going to use either Vue.js or React.js framework; for backend we
will use one of the most popular frameworks (Django or FastAPI for Python,
Spring for Java).

It is very likely that we will use some kind of data storage. We plan to use
Postgres as a  DBMS and/or Redis for caching.

### **Anticipating Future Problems**

We see 2 primary problems we can face in the future:

1. **Obtaining the map of the university and making the interactive digital copy
   of it.** If this task turns out to be too complicated and time-consuming, we
   plan to implement it in a simpler way, such as using static photos to help
   people locate the rooms.
2. **Finding a way to integrate our system into the life of the university, as
   this will most likely require working with the Microsoft Outlook API.** To
   solve this problem we are going to consult with people in university who are
   responsible for My University portal or can give us advice.

### **Elaborate Explanations**

For now we do not have a clear vision of components that make up our system and
their relations. But the core parts we are going to implement are the following:

- Backend that utilizes currently used Outlook API to provide a better interface
  for rooms booking;
- Mobile-friendly interface with focus on usability and simplicity;
- Digital map or other way to help users find rooms location.


{{< hint danger >}}
**Feedback**  

**Value Proposition**
Very nice details and approach. Although we previously had an opportunity to book rooms though calendar in outlooks and it was very convenient. It will check which free rooms available at the desired time. 

Also, the university does have a map to tell which room and where is it. You can contact me to sent it to you.

**Lean startup question**
- Only positive feedback? Why :) negative feedback is important also

**AI** 
I hardly see AI application in your product 

Vision Of The Project 
One very easy way to tell people where is meeting room. Is to tell them they are located next to what rooms? 
Or maybe give description how to reach by description the road to take. 

**Overall**
Very good report! But try to think more about AI utilizing. 
5/5

_Feedback by Moofiy_
{{< /hint >}}