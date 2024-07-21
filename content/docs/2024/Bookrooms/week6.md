---
title: "Week #6"
---

# **Week #6**

## **Presentation**:

{{< embed-pdf url="/2024/Bookrooms/Bookrooms.pdf" >}}

## **Weekly Progress Report**:

This week, we made significant strides towards completing the core functionalities of the Innopolis University Room Booking System. Our focus was on finalizing the frontend integration and ensuring the system is ready for user testing and our upcoming presentation. 

User Survey Results:

We conducted a survey to gather insights into user preferences and needs for the room booking system. The key findings from the survey were:
- Availability is important: The majority of students valued the most availability of a room at a specific date and time, leaving behind type, location and capacity.
- Floor Flexibility: Almost all students indicated that booking a room on a specific floor was not very important, and they would be willing to book on a different floor if their preferred floor was unavailable.

Refinements based on Feedback:

Based on the survey results, we made the following adjustments to the frontend design:
- Optional Floor Selection: We will implement an optional floor filter, allowing users to refine their search by floor if desired. This makes the search process more flexible and caters to users who prefer not to be restricted by floor selection.

Floors filter enabled:

![Enabled](/2024/Bookrooms/floors_enabled.jpg "Enabled")

Floors filter disabled:

![Disabled](/2024/Bookrooms/floors_disabled.jpg "Disabled")

- Visual Time Range: We will incorporate a visual time range selection feature, enabling users to choose their desired time slot using dropdowns for "start time" and "end time". All their actions will be displayed on a timeline in a user-friendly manner. This will allow users to easily specify their preferred time range for booking.
![Time selection](/2024/Bookrooms/time_selection.jpg "Time selection")

Frontend Development:

- We completed the development of the frontend user interface, including:
  * Site Appearance: We finalized the visual design, ensuring a user-friendly and intuitive layout.
  * Room Access and Booking: Users can now access information about specific rooms, view availability, and make bookings.
  * Room Filters: We implemented filters to allow users to search for rooms based on type (Meeting Room, Lecture Room, etc.).
  * 3D Model Integration: We successfully integrated the fully developed 3D model of the university building into the frontend, providing users with an interactive and immersive experience.

![Frontend](/2024/Bookrooms/frontend1.jpg "Frontend")
![Booking](/2024/Bookrooms/frontend2.jpg "Booking")

- The following features are still under development:
  * Time Filter: We are currently working on implementing a time filter to refine room searches based on specific time slots. 
  * Authorization: We are integrating authorization mechanisms to ensure users have appropriate access rights to specific functionalities and rooms.
  * Dynamic Room Occupancy Display: We plan to display real-time room occupancy information to enhance booking accuracy.

Backend Development:

- The backend development is now complete. We have implemented all necessary functionalities, including:
  * Booking Functionality: Users can create, view, and cancel bookings.
  * Availability Retrieval: The backend efficiently provides data on available rooms based on user search criteria.
  * Authentication and Authorization: We have implemented a robust authentication system using Google SSO and an authorization system that controls user access based on roles and permissions. 

3D Model Development:

- The 3D model of the university building is complete. All floors have been modeled and are integrated into the frontend, allowing users to explore the campus in 3D. 

### **Challenges & Solutions**

This week, we grappled with a key decision: how to organize user roles in the database. 

- Tech Debt vs. Scalability: We debated between two options: a simple role-room table or a more complex system for managing roles and permissions. We opted for the simpler approach, creating a single table, to avoid overengineering and accelerate development. This decision acknowledged that we might need to revisit this design in the future if the system becomes more complex, but it allowed us to prioritize functionality and deliver the MVP efficiently. 

This decision highlights the ongoing balance between immediate needs and long-term scalability that we face in software development.

### **Conclusions & Next Steps**

- Progress & Key Milestones: We have reached a significant milestone with the completion of the core frontend and backend functionalities, the integration of the 3D model, and the implementation of a robust authorization system.
- Next Steps: Our priority now is to:
  * Finalize Time Filter and Dynamic Room Occupancy: Implement these remaining frontend features to enhance user experience.
  * Conduct User Testing: We will conduct user testing to gather feedback and ensure the system meets the needs of the university community.
  * Prepare for Presentation: We will finalize the presentation, showcasing the system's features and achievements.

We are excited to present the progress of the Innopolis University Room Booking System and are confident that this project will provide a valuable tool for the university community.