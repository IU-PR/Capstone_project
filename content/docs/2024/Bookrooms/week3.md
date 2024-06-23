---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

### **Technical Infrastructure**:

???- Hosting Environment: Currently running on a local server using Docker Compose for development and testing. We plan to transition to a cloud-based hosting solution (AWS, Azure, or GCP) in future iterations.
- Deployment Method: Currently, we are using Docker Compose for containerizing and deploying the application locally. We will implement a CI/CD pipeline for automated deployments as the project matures.
- Logging: We are using basic logging mechanisms within our Go backend and Javascript frontend. We will consider implementing a centralized log aggregator like Splunk for more comprehensive error tracking and analysis as the project progresses.

### **Backend Development**:

- API Endpoints: By the end of 3 weeks, we developed the following API endpoints: 
  * Room Availability Query: This endpoint allows users to retrieve available rooms within a specified time range.
  * Booking Creation: This endpoint handles booking requests, including validation of user input and booking constraints.
???- Data Validation: We implemented data validation rules to ensure the integrity of bookings. These rules include:
  * Validating date and time formats
  * Verifying room availability within the specified time range
  * Ensuring the booking capacity does not exceed the room's maximum capacity
???- Security: We implemented basic security measures, including:
  * Input sanitization to prevent injection attacks
  * Authorization rules to control user access to sensitive data
  * Data encryption for sensitive information stored in the database.

### **Frontend Development**:

- User Interface Components: We developed the following user interface components:
  * Search Bar: Allows users to search for rooms by name, building, room type, and availability.
  * Booking Form: Enables users to create and manage booking requests.
???- User Interaction: We implemented user interactions using:
  * Event listeners to handle user input and actions
  * AJAX requests for communication between the frontend and backend API
???- 3D Model: We developed the 3D campus model using Three.js:
  * Created a 3D model in ... and imported it using Three.js.
  * Created interactive parts of the 3D model that change texture when a button is pressed.
  * Integrated the 3D model with the frontend interface.

### **Data Management**:

We have established a database schema with the following tables:
- Room: Stores information about each room, including its type, name, capacity, and building location.
- User: Stores user information, including roles (student, staff, etc.), names, and email addresses.
- Booking: Records booking details, including the room ID, user ID, start time, and end time.
- Building: Defines buildings on campus with unique IDs and names.
- Room Type: Categorizes room types, such as auditoriums, meeting rooms, and study rooms.
- User Favorite Room: Allows users to mark specific rooms as favorites.

### **Prototype Testing**:

- Testing Methods: We conducted manual testing this week. 
- Testing Scope: We tested the backend API functionality, frontend user interface, 3D model interactions, and database integration.
- Test Results: We did not encounter any critical bugs or issues during this testing phase.
- User Feedback: We have not yet conducted user testing but will prioritize it in the coming weeks to gather valuable feedback.

## **Weekly Progress Report**:

This week, our team has made significant progress in developing the project:

1. Added Default Rooms to the Database:
We implemented a mechanism to populate the database with default Innopolis rooms during backend startup. This involved:
- Creating a initRooms.json file containing a list of default rooms with their attributes (name, type, floor, capacity, building ID).
- Implementing logic in the backend to parse the initRooms.json file and insert the rooms into the PostgreSQL database.<br>
This ensures the database has a starting point with essential rooms, simplifying initial testing and setup.

2. Developed the 3D model using Three.js:<br>
- Created a basic 3D viewer with features like loading multiple models, moving, and scaling
- Designed interactive 3D model elements that respond to button presses by altering their texture.

3. Created the basic frontend layout:<br>
We designed and implemented a basic layout for the frontend user interface. This included a rough sketch of the layout elements based on the provided requirements. This initial layout provides a visual foundation for further development.

4. Defined the Database Schema:<br>
We defined our database schema that includes tables for:
- Room: Details about each room, including type (lecture room, meeting room, etc.), name, capacity, floor, and building.
- User: Information about users, including their role (student, staff, etc.), name, and email.
- Booking: Records of room bookings, including room ID, user ID, start time, and end time.
- Building: Defines buildings on campus, with unique IDs, names and numbers of floors.
- Room Type: Categorizes room types (lecture room, meeting room, etc.).
- User Favorite Room: Allows users to mark specific rooms as favorites. 

???5. Conducted a meeting<br>:
We held a meeting with the team leader of last year’s capstone team "Bookinng". We received useful information:
- Integration: We received some advice on how to integrate our system into IU Outlook.
- Contacts: The team leader shared the contacts of the developers of the current room booking service.
- Calendar: We got some ideas on how bookings can be displayed on the timeline to make the user experience more convenient.

### **Challenges & Solutions**

???...

### **Conclusions & Next Steps**

Our priority list for the next weeks:
- Continue Backend Development: Expand API endpoints to include booking cancellation, user management, and other essential features.
- Frontend Development: Develop the complete user interface, including user profile pages, booking history, calendar integration, and more.
- 3D Model Development: Refine the 3D campus model, adding more detail, navigation features, and user interactions.
- Database Optimization: Optimize database queries and implement data migration strategies.
- Integration Testing: Develop comprehensive integration tests for the backend and frontend.
- User Testing: Conduct user testing with real students, faculty, and staff to gather feedback and identify areas for improvement.

Overall, we are progressing well on our goal of delivering a robust and user-friendly room booking system for Innopolis University. The team is focused on creating a system that addresses the university's specific needs and enhances the overall room booking experience.