---
title: "Week #2"
---

# Week #2

## **Tech Stack Selection**
Maintainability and reliability are the most critical aspects for the project’s architecture. The customers of the project are demanding the product that could be easily adapted to their requirements. So, to lay the foundation for the project architecture, firstly, we chose the modern and stable framework, which perfectly suits industrial requirements. Secondly, we found the open-source optimal solutions for the specific subparts of the project. Thus, our tech stack is as follows (later it can be changed for the custom solutions):



- **Programming languages – C++/Python**

We are limited by ROS2 requirements. It supports only C++ and Python. We chose C++ for developing ROS2 nodes. For the rest of the backend infrastructure (database, API for backend-frontend communication) we are using Python. We decided to use C++ to make it possible in the future to obfuscate the source code, before sending it to the customer, so the customer can use the code, but not steal it.


- **ROS2 Humble**

ROS2 is a preferable choice for industrial projects, a modern standard stack. It is a popular and stable distribution of ROS2. Another its benefit is the fact that a lot of sources and materials exist about ROS2 Humble.

- **`slam_toolbox`, `navigation2`**

SLAM toolbox is a base package for SLAM in ROS2. It perfectly matches the Nav2 package that we use for navigation, since they were created by the same developer. This package is also open source. SLAM toolbox also supports lifelong mapping, a concept of being able to update and improve the map while interacting with the environment. As for Nav2, it is a commonly used package for navigation. 

- **`rosbridge_suite`**

The rosbridge_suite package is a collection of packages that implement the rosbridge protocol to create a websocket for the transport layer. Rosbridge provides many services, such as subscribing and publishing topics, service calls. Moreover, this package can work with any programming language since JSON format is used for transporting data.

- **MongoDB**

MongoDB is a NoSQL database, which simplifies the development of applications with it. It also has a dynamic schematic structure that can be easily changed if needed. 



## **Architecture Design**

### **Component Breakdown:**


As described in the report for week 1, our project has the following structure:
- **Simultaneous Localization and Mapping** - algorithm to build a map of the environment with the obstacles around and understand where the mobile platform is located within this environment based on the data from the mobile platform. SLAM should support two modes: 
 1. Localization + Mapping, when Map is built
 2. Only Localization, when Map is taken from memory or Database

    SLAM will accept input from the hardware, specifically data from lidar. Also, SLAM node will subscribe to `tf` topic (transformations) of the model. Based on this data it will calculate the position of the platform. The calculated current position and velocity will be sent to the Path Planner. The map created by SLAM will be saved in the Database. 

- **Path Planning** - algorithm to build a path from the current location of the mobile platform to the desired one based on the given map and current position and velocity. Ideally, functionality to add custom obstacles, not detectable by platform itself, should also be added. 
Path Planner will accept a map from the Database, current position and velocity from SLAM, and desired position from Frontend. The desired velocity computed by Path Planner will be sent to the Controller. 

- **Controller** - robotic software to communicate with the hardware interface of motors (motors drivers) to pass the desired velocities to the motors. The Controller should work the same for the real-life hardware and simulation. Moreover, for the sake of simplicity and maintainability, Controller-Hardware and Controller-Simulation communication should be as similar as possible to ensure fast and easy switching between one and another.
Controller gets data from sensors from Hardware, and can accept desired velocity from either Path Planner, or Frontend via the ros bridge. 

- **Web Interaction** - part of the software, responsible for transferring data between Frontend and Backend part of the project. Will be created with Rosbridge Suite
Database  - the database where maps and possible paths can be stored to not build them every time.
Database saves maps created by SLAM and provides needed maps for the Path Planner.



### **Data Management:**
We will use the MongoDB database to store maps created by SLAM, paths created by Path Planner, system settings, obstacles. The data from the Database can be accessed from Frontend and Path Planner.
The database will be accessed via Python and the data will be wrapped in ROS2 elements. 
We will use `rosbridge_suite`, a middleware that connects ros nodes with a websocket server, to send data to the Frontend part of the project. 

### **User Interface (UI) Design:**
Since our team develops the Backend part of the project, we are not responsible for the UI Design. The Frontend team is responsible for it. However, we use rviz for map visualization. This map will be sent to the frontend and displayed for users. 

### **Integration and APIs:**
Our project will communicate with Frontend and Hardware/Simulation projects. This is the structure we have established for this communication:

#### Frontend-Backend API: 

It will be mainly done with the Rosbridge Suite package.

- The following information will be received from Frontend:
1. Command to start mapping
2. Desired position of the robot (x and y coordinates)
3. Virtual walls which need to be added manually (polygon nodes, representing the walls)
4. Desired velocity of the robot (linear and angular velocities with respect to x and y axes)


- The following information will be sent to Frontend:
1. Map created by SLAM
2. Robot’s position
3. Information about battery charge of the robot

#### Backend-Hardware/Simulation API: 

Each of physical components has packages used for communication.

- The following information will be send to Hardware:

1. Command to wheels (wanted velocity and direction)

    *Node DiffDriveController communicates with MotorsDriver node via `wheel_control` topic.*

- The following information will be received from Hardware:

1. Data from the model (`tf`)
2. Data from lidar sensors
3. Current position of wheels
4. IMU data
5. Data from cameras
6. Data from sonars
7. Information about battery charge of the robot


### **Scalability and Performance:**
- ROS architecture itself allows to extend functionality seamlessly, since each component, represented by node, is a stand-alone program that can be replaced.

- Boost C++ library can be used to increase performance in the future.

### **Security and Privacy:**
- C++ used to enable source code obfuscation
- Established strict APIs, so that frontend part cannot interfere with backend and hardware/simulation, and different part of the project do not depend on each others implementation
- The passwords needed for logging will be hashed, not stored directly

### **Error Handling and Resilience:**

1. We will make each node resistant to not getting any message from another nodes, so if one node does not work, others will still function.

2. In the future, everything can be logged and reproduced using rosbag.


### **Deployment and DevOps:**

Our experts assisted in developing CI/CD pipeline to smoothen the development process. Docker containers are used to integrate all parts of the project and ensure they work together.

We do not have any deployment yet, since the actual robot is still being assembled. However, in the future we will use the docker container and create a script to automatically deploy everything on the robot by just launching it.


## **Week 2 questionnaire:**
### **Tech Stack Resources:**

We do not have any specific project related books, the only book we rely on is general Bible of all robotics: [Spong's Robot Modeling and Control](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.researchgate.net/profile/Mohamed_Mourad_Lafifi/post/How_to_avoid_singular_configurations/attachment/59d6361b79197b807799389a/AS%253A386996594855942%25401469278586939/download/Spong%2B-%2BRobot%2Bmodeling%2Band%2BControl.pdf&ved=2ahUKEwjW5_6iueCGAxX_IhAIHen8AZkQFnoECBkQAQ&usg=AOvVaw0SmJvmoTWd1k0O3PyRfDSI).


### **Mentorship Support:**
As mentioned in the report for week 1, Ivan Domrachev, Robotics lab employee, is guiding us in this project. He provides us useful advice and feedback on what can be done in the project. 

### **Exploring Alternative Resources:**
1. [Main source (Tutorials for ROS2)](https://docs.ros.org/en/humble/Tutorials.html )
2. [Tutorials for Nav2 package](https://docs.nav2.org/)
3. [Tutorials for security in ROS2](https://docs.ros.org/en/rolling/Tutorials/Advanced/Security/Security-Main.html)
4. [WIKI for slam toolbox](http://wiki.ros.org/slam_toolbox)
5. [WIKI for Rosbridge suite](http://wiki.ros.org/rosbridge_suite)


### **Identifying Knowledge Gaps:**

We are quite confident in our knowledge. However, we can always contact our mentor or outside sources in case we have any difficulties. To further ensure no problem with knowledge gaps occur, we divided tasks in a way that Robotics students get task more connected with manipulating the Hardware and solving Kinematics problems, while non-Robotics students have to work with the Database and Frontend API, more Software-related tasks.

### **Engaging with the Tech Community:**

As mentioned in report for week 1, this project is inspired by Robotics lab employees. Consequently, the Robotics lab provides us with needed equipment and a place to hold meetings. Moreover, we also discussed possibilities to use projects created by other Robotics lab employees in our project (for example, we asked the team developing the Follow-me mobile platform to test our SLAM on their robot). 


### **Learning Objectives:**
During this week we aimed to become more comfortable with ROS2. Also, we set a goal to deeply understand how to connect different parts of the project together and finalize the implementation approaches for these parts. The main goal was to create a working prototype which can be launched inside a Docker container.


### **Sharing Knowledge with Peers:**
We held several meetings during the week, both within our team and with teams responsible for other parts of the project, to share our progress, discuss communication between different components and exchange knowledge in case any team members had difficulties or questions. Moreover, all team members communicated via Telegram to get information without having to wait for meetings.

### **Leveraging AI:**
Despite the huge hype around AI nowadays, our team and mentor believe that not all projects can justify the leverage of AI, in some projects it is not  needed at all, especially in the tasks related to hardware communication. To satisfy the course requirements we are searching for the tools in path planning.

### **Tech Stack and Team Allocation**

| Team Member              | Track   | Responsibilities   |
|--------------------------|---------------|-----------------|
| Ekaterina Mozhegova (Lead)     | Backend (Controller) | Implement the controller |
| Iurii Podkorytov | Backend (SLAM) | Develop the SLAM node using `slam_toolbox` |
| Mukhammadrizo Maribjonov | Backend (Path Planner)| Implement the Path Planner using `nav2` |
| Yehia Sobeh            | Backend (Frontend API) | Establish the Frontend API using `rosbridge_suite` |
| Ali Hamdan            | DevOps | Write the launch file |
| Saveliy Khlebnov | Backend (Database) | Implement the database using MongoDB and Python |
| Anastasiia Shvets | Technical Writer | Write the report |


## **Weekly Progress Report**

**Goal of the week:** build the foundation for the project’s architecture. We developed the main nodes: Controller, SLAM. We searched for the tools for bridging frontend and ROS2 and started developing the API. Also, we defined the types of data for communication between frontend and backend. 


## **Challenges & Solutions**

1. AgileX leverages the API provided by Scout, which supports only ROS1. Since we use ROS2, we decided that testing on real-life hardware is not vital right now. So, we postponed the testing the SLAM node when our mobile platform will be assembled.

2. Non-Robotics students did not have previous experience with ROS2. They asked help from our mentor, and provided feedback to help them overcome this lack of expertise.

## **Conclusions & Next Steps**

This week, we developed the main components of the backend. We will continue working on it. So, we stick to the plan.
The main objectives of the next week are as follows:

1. Refine the Path Planner
2. Finalize the communication infrastructure between Frontend and Backend
3. Write the launch files with remapping
4. Continue implementing the database
