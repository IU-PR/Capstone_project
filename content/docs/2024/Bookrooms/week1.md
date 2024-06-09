---
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member              | Telegram ID   | Email Address   |
|--------------------------|---------------|-----------------|
| Ismagil Iskakov (Lead)    | @absorian | i.iskakov@innopolis.university |
| Mikhail Gladyshev            | @secretanry | m.gladyshev@innopolis.university |
| Alexander Sevastyanov            | @alexander_sev | a.sevastyanov@innopolis.university |
| Vladislav Kishkovskiy            | @deeprecession | v.kishkovskiy@innopolis.university |
| Said Nurullin            | @Nurullin_Said | s.nurullin@innopolis.university |
| Matvey Platonov | @Matvey_Platonov | m.platonov@innopolis.university |
| Aleksandr Ryabov | @Raleksan | a.ryabov@innopolis.university |

### **Value Proposition**

### The Problem

There are several difficulties with the existing Innopolis University room reservation system for both staff and students:
- Time-consuming and frustrating procedure: To find availability, users must manually check each room's calendar, which may be especially difficult when looking for a room at a certain time.
- Difficulty Finding Rooms: Not only is it difficult to make reservations, but students and staff sometimes have trouble finding particular rooms, auditoriums, and offices inside the university's walls.

To gain a deeper understanding of these challenges, a team of developers [^1] at Innopolis University conducted a survey in the previous year. The survey yielded the following insights:
- A majority of participants (over 50%) spend more than 5 minutes on average to choose and book a room.
- Participants expressed general dissatisfaction with the usability of the current system, with none rating its convenience as highly as 5 out of 5.
- A large majority of participants (over 66%) would like to see a feature that allows them to view all rooms available within a specific time range, while a quarter found this to be a good idea.
- Over half of the participants would appreciate a visual representation of room layouts while booking.

These findings highlight the need for a more efficient and user-friendly room booking system at Innopolis University.


### Solution

To address the challenges faced by students and employees in booking rooms at Innopolis University, we propose a new room booking system with the following features:
- Real-Time Availability Display: Our system will provide a real-time display of all available rooms within a specified time range. This will eliminate the need for users to manually check each room's calendar, saving them significant time and frustration.
- Specific Room Availability: For users who prefer to book a specific room, our system will display the availability of that room for the desired time range. This will allow users to check the availability of their preferred rooms and time slots in a timely manner.
- Interactive 3D University Model: Our system will feature a visually appealing 3D model of the university campus. This model will allow users to easily locate and select rooms, and will include animations to highlight the selected room. This will greatly enhance the user experience and make the booking process more intuitive.

By implementing these features, our room booking system will significantly improve the efficiency and convenience of the room booking process at Innopolis University. Users will be able to quickly and easily find and book the rooms they need, without the frustration and time waste associated with the current system.


### Benefits to Users

Our proposed room booking system offers several key benefits to users:
- Increased Efficiency: By providing a real-time display of available rooms and allowing users to quickly determine the availability of specific rooms, our system will significantly reduce the time and effort required to book a room.
- Improved Convenience: Our system's user-friendly interface and interactive 3D campus model make the booking process more convenient and intuitive. Users can easily find and select the rooms they need, without the frustration associated with the current system.
- Enhanced User Experience: The visually appealing 3D campus model provides a more immersive and engaging user experience. Users can easily visualize the location of rooms and see how they fit into the overall campus layout.

Overall, our room booking system will make it easier, faster, and more enjoyable for students and employees at Innopolis University to book the rooms they need.


### Differentiation

Our room booking system stands out from existing solutions by offering:
- Real-time availability display: Quickly find available rooms within a specific time range.
- Interactive 3D campus model: Visualize room locations and campus layout.

These unique features provide a superior user experience and set our system apart.


### User Impact

Our room booking system empowers users to book rooms quickly and easily, saving them time and frustration. Its user-friendly interface and intuitive navigation enhance the overall user experience.

### Use Cases

- Students can quickly book study rooms for group projects or individual study sessions.
- Employees can easily reserve meeting rooms for conferences, presentations, or team meetings.
- University administrators can efficiently manage room bookings and ensure that all rooms are being used effectively.


## **Lean Questionnaire**

1. What problem or need does your software project address?

Our room booking system addresses the need for a more efficient and user-friendly room booking process at Innopolis University.

2. Who are your target users or customers?

Our target users are students, employees, and administrators at Innopolis University.

3. How will you validate and test your assumptions about the project?

We will validate and test our assumptions through user testing and feedback. We will conduct surveys and interviews to gather feedback on the system's usability, functionality, and overall user experience.

4. What metrics will you use to measure the success of your project?

We will use the following metrics to measure the success of our project:

- Number of bookings made through the system
- User satisfaction ratings
- Time saved by users compared to the previous system

5. How do you plan to iterate and pivot if necessary based on user feedback?

We plan to iterate and pivot based on user feedback by continuously collecting and analyzing feedback, identifying areas for improvement, and implementing changes to the system. We will also monitor usage data to identify any trends or patterns that suggest the need for changes.


## **Leveraging AI, Open-Source, and Experts**

Our team leverages the power of AI and open-source technologies to develop a room booking system providing a superior user experience. We utilize ChatGPT and Copilot to reduce development time and costs. For the frontend, we employ Svelte and React for a responsive and engaging user interface, and WebGL/Three.js for the interactive 3D campus model. On the backend, we rely on XORM for object-relational mapping and Gorilla/Mux for API routing and handling. By leveraging these open-source tools, we can focus on delivering a high-quality and user-centric room booking system.

## **Defining the Vision for Your Project**

### Overview

Our room booking system is a comprehensive solution that addresses the challenges of the current system at Innopolis University. It provides a real-time display of available rooms, allows users to easily find and book specific rooms, and features an interactive 3D campus model for visualizing room locations. By leveraging open-source technologies, our system offers a user-friendly and efficient room booking experience for students, employees, and administrators alike.

### Schematic Drawings

   ![Schematic drawing](/2024/Bookrooms/schema.jpg "Schema").

### Tech Stack

- Backend: XORM, Gorilla/Mux
- Database: PostgreSQL
- Frontend: Svelte/React, WebGL/Three.js



### References

[^1]: [Bookinng](docs/2023/bookinng/)