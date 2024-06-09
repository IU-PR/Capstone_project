# Week #1

## Team Formation and Project Proposal

### Team Members

| **Team Member**          | **Telegram ID**                                | **Email Address**                     |
|--------------------------|------------------------------------------------|---------------------------------------|
| Dmitry Zvidrin (Lead) 1  | [@Hyperlope](https://t.me/Hyperlope)           | d.zvidrin@innopolis.university        |
| Danila Tretyakov 2       | [@Ezzy\_a](https://t.me/Ezzy_a)                | d.tretyakov@innopolis.university      |
| Anton Fadeenkov 3        | [@friji\_off](https://t.me/friji_off)          | a.fadeenkov@innopolis.university      |
| Kseniia Voronova 4       | [@ksushechkavoron9](https://t.me/ksushechkavoron9) | k.voronova@innopolis.university    |
| Yassine Allala 5         | [@Bidrift](https://t.me/Bidrift)               | m.allala@innopolis.university         |

## Value Proposition

- ### Problem Identification
In Innopolis, residents and visitors face difficulties finding reliable and convenient carpooling options. Currently, a Telegram chat is used for coordinating rides, but this method has several drawbacks:

- **Lack of structure:** The chat format is disorganized, making it difficult to quickly find necessary information.
- **Limited search capabilities:** Users cannot easily search for rides based on specific criteria such as time, date, or destination.
- **Safety issues:** There is no system for verifying the identities of drivers and passengers, leading to potential safety risks.



- ### Solution Description
Our project offers a specialized web application for finding ride companions in Innopolis, similar to BlaBlaCar but tailored to local conditions. Key features include:

- **User profiles and verification:** Comprehensive user profiles.
- **Advanced search and filtering:** Users can search for rides based on various parameters such as date, time, departure and arrival points, user ratings.
- **Booking and communication:** An integrated messaging and booking system to simplify coordination between drivers and passengers.
- **Ratings and reviews:** A ratings and reviews system to enhance accountability and reliability.
- **Notifications and alerts:** Automatic notifications about trip confirmations, reminders, and updates.
- **Local taxi call in Innopolis:** If no companions are found, the app will suggest calling a local taxi immediately or booking for a specific time.
- **Group creation for taxi calling:** Users can create a trip together by forming a group of companions to call a taxi or car-sharing.



- ### Benefits to Users
By using our web application, users will gain the following benefits:

- **Increased convenience:** A user-friendly platform for quickly finding and booking rides, creating their own group for finding companions for taxi or car-sharing, and calling local taxis.
- **Enhanced safety:** Verified user profiles and ratings improve safety and trust.
- **Time savings:** Efficient search and booking processes reduce the time spent organizing rides.
- **Improved coordination:** Integrated communication tools simplify interactions between drivers and passengers.
- **Cost savings:** Carpooling helps users save on transportation costs by sharing expenses.



- ### Differentiation
Our web application stands out from existing solutions due to:

- **Local focus:** Tailored specifically for the Innopolis community, considering local needs and preferences.
- **Comprehensive safety measures:** Enhanced verification and rating system compared to informal chat methods.
- **User-friendly interface:** Designed for ease of use with intuitive navigation and functionality.
- **Multi-functional travel options:** Choice of existing rides, creating their own group, or calling local taxis-all in one app.



- ### User Impact
Implementing our web application for finding ride companions will have a significant positive impact:

- **Improved mobility:** Facilitating access to transportation options for residents and visitors of Innopolis, enhancing overall mobility in the city.
- **Environmental benefits:** Promoting carpooling reduces the number of cars on the road and lowers carbon emissions.
- **Cost savings:** Reducing users' transportation costs through shared rides.
- **Safety and reliability:** Creating a safer and more reliable ecosystem for shared rides compared to informal methods.



- ### User Testimonials or Use Cases:
 **Actors**:
- User (Passenger)
- Fellow Traveler (Driver)

 **Preconditions**:
- User and Fellow Traveler are registered and logged into the app.
- User has a need for transportation.

**Main Flow**:
1. User opens the app and selects the "Order Taxi" option.
2. User enters the desired pick-up and drop-off locations, as well as the date and time for the ride.
3. The app displays available taxi options, including solo rides and shared rides with Fellow Travelers.
4. User selects a taxi option and confirms the booking.
5. If the user chooses a shared ride, the app matches them with a Fellow Traveler who has a similar route and schedule.
6. The Fellow Traveler receives a notification and can accept or decline the request to share the ride.
7. If accepted, the app provides the User and Fellow Traveler with each other's contact information and meeting point details.
8. User and Fellow Traveler meet at the designated location and complete the ride together.

**Alternative Flow (User as a Fellow Traveler)**:
- Instead of ordering a taxi, the User can choose to be a Fellow Traveler by offering a ride to others.
- The process is similar, but the User selects the "Offer a Ride" option and provides details about their trip.
- Other Users looking for rides can then see the User's offer and request to join as a Fellow Traveler.

**Postconditions**:
- User reaches their destination safely and efficiently.
- Fellow Traveler earns a share of the ride cost and contributes to a more sustainable transportation system.

**Exceptional Flow**:
- If no Fellow Travelers are available for a shared ride, the User can proceed with a solo taxi ride.



## Lean Questionnaire

1. **What problem or need does your software project address?**

   Our project addresses several key problems and needs related to organizing carpooling in Innopolis:

- **Inconvenience of using Telegram chat:** The current system of coordinating rides via Telegram chat is disorganized and inefficient.
- **Limited search and filtering capabilities:** Users cannot easily find suitable rides based on specific criteria.
- **Lack of safety measures:** There is no mechanism for verifying the identities of drivers and passengers.
- **Lack of integrated services:** There is no option for calling local taxis or creating trips to bring users together for taxi or car-sharing.

2. **Who are your target users or customers?**

   Our target users include:

- **Students and faculty of Innopolis University:** For daily commutes to and from the university.
- **Employees of local companies:** For commutes to and from work.
- **Residents and visitors of Innopolis:** For any trips within and outside the city.
- **Visitors and tourists:** For convenient transportation around the city and its surroundings.

3. **How will you validate and test your assumptions about the project?**

We will send links in Telegram chats for carpooling and taxis in Innopolis to our MVP version for testing the app's functionality, user interest, and gathering feedback. We will validate our assumptions by analyzing app performance and considering overall user feedback. Then, we will analyze the collected data and implement necessary updates to improve the app based on the testing results.



4. **What metrics will you use to measure the success of your project?**

To measure the success of the project, we will use the following metrics:

- **Number of registered users:** Growth in the number of new users on the platform.
- **User activity:** Frequency of app usage, number of booked rides.
- **User satisfaction level:** User ratings and reviews.

5. **How do you plan to iterate and pivot if necessary based on user feedback?**

   Based on user feedback, we will gather information to identify key issues and needs. Depending on the importance and urgency of the identified issues, we will implement appropriate changes on the platform. Afterward, new testing will be conducted to evaluate the effectiveness of the changes made. We will continuously update and improve the app based on both current and new data, ensuring it meets user needs.

## Leveraging AI, Open-Source, and Experts

We intend to use open libraries and frameworks such as React, Redux, and FastAPI to accelerate the development process and implement modern technologies. Additionally, we plan to use artificial intelligence, such as chatGPT, to effectively solve emerging problems.

## Defining the Vision for Your Project

### Overview
The "KUDA" project is a web application designed to facilitate the organization of carpooling in Innopolis. Our app offers a convenient and safe way to find ride companions. Users can quickly find shared rides by specifying their preferences for time and route. Additionally, an interface will be implemented for creating joint trips to call a taxi with other passengers or car-sharing.

### Schematic Drawings:
Our current view of what the system's core components may look like on the diagram:

<div style="text-align: center;">
<img src="/2024/kuda_team/week1/scheme.svg" width="600" height="300"> 
</div>

### Tech Stack
- **Frontend:** React, Redux, JavaScript
- **Backend:** FastAPI, SQLAlchemy, PostgreSQL, Redis, GitHub Actions
