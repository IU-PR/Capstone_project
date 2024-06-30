---
title: "Week #4"
---

# **Week #4**


## **External Feedback**

We received valuable feedback from the leader of the previous year's "Bookinng" team. He expressed positive sentiment towards our design and provided insightful suggestions for improvement:

- Full Calendar Resource Manager: He recommended implementing a full calendar resource manager to provide a comprehensive view of room availability over time. This would enhance user understanding of which rooms are available and when. We will incorporate this feedback into our planning for future iterations. 

![Calendar](/2024/Bookrooms/calendar.jpg "Calendar")

## **Testing and Narrowing the Scope**

This week, we focused on developing core backend functionality and API endpoints, setting the stage for future testing efforts. 

We are planning to implement automated testing to ensure the quality and stability of our system. We'll be incorporating integration tests to verify the interactions between our API endpoints and the database, ensuring data integrity and correct functionality.

## **Iteration and Refinement**

We made significant progress in aligning the frontend's appearance with our original Figma design, resulting in a more polished and cohesive user interface.

Design:
![Design](/2024/Bookrooms/Design.jpg "Design")

Frontend:
![Frontend](/2024/Bookrooms/frontend.jpg "Frontend")

We also made progress on the 3D model development. We modeled the first floor of Innopolis University, taking into account the exact layout of the premises and the configuration of the building.

Before:
![3D](/2024/Bookrooms/3d.jpg "3D")

After:
![3D Campus](/2024/Bookrooms/3d_first_floor.jpg "3D Campus")

## **Weekly Progress Report**:

Backend Development:

This week, we made significant strides in expanding the backend API to handle core functionality related to building, room type, and booking management. 

- Building and Room Type Retrieval: We implemented two essential endpoints:
  * GET /buildings: This endpoint allows users to retrieve a comprehensive list of all buildings on campus. The response includes each building's ID, name, and a list of its floors. 
  * GET /roomTypes: This endpoint provides a list of all room types available within the university, including their ID and name. This information is crucial for enabling user filtering and selection of rooms based on their intended purpose. 

- User-Specific Booking Management: We developed API endpoints to facilitate user-specific booking actions: 
  * POST /bookings: This endpoint enables users to create new bookings. It validates user input and ensures adherence to room availability.
  * DELETE /bookings/{bookingId}: This endpoint allows users to cancel their existing bookings. It ensures proper authorization and deletion of relevant data. 

- Current Bookings Retrieval: We implemented an endpoint to retrieve a user's current bookings:
  * GET /bookings/current: This endpoint provides users with a list of all their active bookings. This allows users to easily track their scheduled room reservations. 

Frontend Development:

We continued refining our frontend, focusing on creating a visually appealing and user-friendly interface. This week's accomplishments include:

- Implementation of Key Features: We successfully implemented essential features based on our Figma design:
  * Room Display: Users can easily browse available rooms with details like name, type, building, and floor information.
  * Room Filtering: Users can filter rooms by specific criteria, such as room type, capacity, building, and availability.
  * Booking Management: Users can select rooms, specify the booking duration, and submit booking requests. 

- API Integration: We successfully connected the frontend to our newly developed backend API endpoints. This enables seamless communication between the client and server, facilitating real-time data retrieval and user actions.

Deployment:

We successfully deployed our application to a server, making the booking system accessible to users. This deployment included the newly implemented API endpoints and the updated database schema. This marks a significant milestone, as it allows us to test the system in a production-like environment and gather valuable feedback from potential users. 


### **Challenges & Solutions**

- Modeling Complexity: Creating a detailed 3D model of a large campus is a complex and time-consuming task. To overcome this, we will break down the modeling process into manageable phases, focusing on specific buildings or areas at a time.
- Time Management: Balancing project work with personal commitments and other coursework can be challenging. To address this, we will establish clear schedules, prioritize tasks, and effectively communicate with team members to ensure everyone is on track.

### **Conclusions & Next Steps**

- User Authentication: We will implement user authentication and authorization mechanisms to secure the system and ensure only authorized users can access and manage bookings.
- Calendar Integration: We will integrate a calendar view to provide a comprehensive overview of room availability, allowing users to easily visualize booking schedules and plan their activities. 
- Error Handling: We will implement robust error handling mechanisms to gracefully handle exceptions and provide informative error messages to users. 
- Testing and Documentation: We will continue developing comprehensive test suites for both the backend and frontend, and we will create detailed documentation for all API endpoints.
- 3D Campus Modeling: We will model other floors of the campus. These 3D models will be integrated into the frontend to provide a visually immersive experience for users.
- Backend Expansion: We will continue adding additional endpoints to the backend API to support more complex functionalities, such as room management, user profiles, and administrative controls. 
- Frontend Completion: We will create the remaining frontend components to provide comprehensive user interfaces for all implemented backend endpoints, ensuring a fully functional and intuitive user experience.