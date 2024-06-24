---
title: "Week #2"
---

# **Week #2**

## **Week 2 - Choosing the Tech Stack, Designing the Architecture**

### **Tech Stack Selection**

The team chose the Unity game engine to create the project, since the team had the most experience working with it. In addition, Unity provides a rich toolkit and a set of ready-made solutions for working with 2D projects, which should speed up development.

### **Architecture Design**

1. **Component Breakdown**:
   Scene loader is a class responsible for loading and transitioning between scenes. (The scene can be the initial menu, individual levels, and so on)
   
Scene controller is a class responsible for controlling the state of the scene. He is responsible for the initial position of the player and all obstacles, tracking the player's state, spawning and general control of opponents and completing the scene.

Canvas is a class responsible for the specific display of the user interface, as well as for applying and saving settings. (receives information from the stage controller and player)

Enemy AI - an interface that allows receiving enemy commands from the stage controller and providing information about the enemy's state. In addition, it is the brain of each individual enemy. (The result should be a swarm intelligence, where each individual representative has a share of autonomy, and the task of the collective mind is the constant presence and stimulation/entertainment of the player)

Player is a class responsible for receiving commands from the user interface and applying them to the player object. Also transmits information to the Canvas and the scene controller.

The architecture can change and expand as the project develops and mechanics are added to it.

2. **Data Management**:

Structural information about in-game objects is stored in the form of prefabs in the corresponding project folder.
Operational information about the state of objects is transmitted by them themselves in the form of commands and messages.
Other information, such as settings, will be stored as text files or prefabs.

3. **User Interface (UI) Design**:

During the game, the user interface will be a skeuomorphic (simulating internal controls) set of arrows/joysticks (to control each of the legs of the walker separately), switches (to activate modules, if any), a slider/screw wheel (to aim the main guns, additional targeting is planned to be done by tapping on the screen), buttons for opening fire and entering the aiming mode. Access to settings and scene transitions should appear as a pop-up window that appears when you press the pause button. (it is planned that it will be located in the corners of the screen)
![Example_of_interface](/2024/Frontline-Walker/Example_of_interface.jpg)
![handdrawn-prototype](/2024/Frontline-Walker/handdrawn-prototype.jpg)
![Reference_of_interface](/2024/Frontline-Walker/Reference_of_interface.jpg)

4. **Integration and APIs**:

Integrations are planned only from Unity Asset Store. All systems from there will be integrated directly into the project as its “components”. The transfer of information will be similar to the exchange of operational information between objects (commands and messages using the engine). At the moment, there are no specific integrations planned; the team plans to resort to them in case of difficulties with the implementation of mechanics or lack of time.   

5. **Scalability and Performance**:

The expansion of the project is planned through expanding the number of mechanics, types of existing opponents/locations/weapons, etc. To ensure smooth implementation of innovations and avoid unnecessary complexity of the project, the team will pay special attention to the modularity and atomicity of scripts in the project. Increasing the number of users should not be a problem, since each copy of the application should be completely autonomous. However, if general game statistics and other activities related to the participation of the server are added in the future, the number of users will become a problem.    

6. **Security and Privacy**:

Until a server is involved in the project, the application will not request any specific data and will not communicate with the Internet, so at the current stage of the project, in our opinion, there is no need to ensure the security of user data. If in the future the application needs Internet access and user registration, the team plans to consult with experts on ways to ensure security.

7. **Error Handling and Resilience**:

At the time of application development, it is planned to use Unity's built-in error detection tools. When the project goes into open use, players who notice errors will be asked to write about it by email to the developers. In addition, there are plans to develop a system for automatically sending error reports, but this will require Internet access and permission to send specific data about the user’s device.

8. **Deployment and DevOps**:

The first release version of the project will be published on ITCH.IO. If the release will be successful, future updates are planned to be released there. The process of creating updates will not differ critically from the process of creating a release version. Interim versions of the project are planned to be stored on Git Hub or in the version control system built into the engine.   

### **Week 2 questionnaire:**

1) Tech Stack Resources: 

So far the only text reference material is the Unity documentation, .NET documentation and the book "Unity in Action" (3rd edition).

2) Mentorship Support: 

At the moment the team does not have a coach, but it would be good to find one. A mentor can greatly facilitate development by suggesting where and how to find implementation of complex mechanics, as well as warning us about potential problems and how to avoid or solve them.

3) Exploring Alternative Resources: 

In addition to books, the team is actively looking for ready-made solutions or useful information in articles on specialized sites and forums, as well as in videos of other beginners or experienced Unity developers.

4) Identifying Knowledge Gaps: 

The team has problems implementing one of the key mechanics in Unity (piston mechanics). At the moment, we plan to try to find similar solutions on the resources mentioned above and experiment with the engine tools (various types of “joints” are currently being actively tested).

5) Engaging with the Tech Community: 

Until now, the team has not actively tried to interact live with the community, but plans to ask for advice in developer groups. (for example, community GDE (Kazan-Innopolis game development community) )

6) Learning Objectives: 

For the second week, the main task was to set up synchronous work with the project. This was achieved by moving all key components of the project to Git Hub and creating separate test scenes in it with a common set of assets, which allowed the team to work simultaneously and independently without changing the code of other participants. Our designer Margarita sets herself the task of drawing the required minimum. She would also like to maintain a unified style in the project, so that even with a minimum of objects the game would look pleasing to the eye. For the third week, the main goal is to implement as many necessary mechanics as possible to build the foundation of the project. To achieve this, the team will actively exploit the created scenes and delve into the above sources to find useful information.

7) Sharing Knowledge with Peers: 

The team meets (usually on a Tuesday) to discuss progress and any problems encountered.

8) Leveraging AI: 

So far, AI has been used to generate images needed as references. In addition, it is planned to use AI to provide advice on the implementation of mechanics. (the main difficulty with this method of obtaining information is drawing up the correct prompt and the limited capabilities of the AI ​​(Basically, it can only offer a script, but not the correct use of the Unity engine tools))

### **Tech Stack and Team Allocation**

| Team Member              | Track                                       | Responsibilities   |
|--------------------------|---------------------------------------------|--------------------|
| Andrei  (Lead)           | Fullstack                                   | Full vision of the project, help all others with any problems, maintaining Git Hub, implementing mechanics, constructions of scenes. (right now - piston mechanic) |
| Timofey                  | Backend (Scripter)                          | implementing mechanics, constructions of scenes. (right now - projectile mechanic) |
| Nikita                   | Backend (Scripter)                          | implementing mechanics, constructions of scenes. (right now - simple enemy behavior) |
| Dmitriy                  | Backend (Scripter)                          | implementing mechanics, constructions of scenes. (right now - piston mechanic) |
| Margarita                | Design                                      | drawing of all sprites, visual part of the project. (right now - basic walker sprites)
 |

### **Weekly Progress Report**

The team was able to establish synchronous work on the project and identify current goals (make piston mechanics, projectiles, turret behavior, aircraft behavior; make sketches of walkers). The team also divided responsibilities and scheduled weekly meetings.

![Sketch1](/2024/Frontline-Walker/Sketch1.jpg)
![Sketch2](/2024/Frontline-Walker/Sketch2.jpg)
![Sketch3](/2024/Frontline-Walker/Sketch3.jpg)

### **Challenges & Solutions**

Synchronous work - Solved - transfer of key project components to the git hub, creation of separate test scenes for developers with shared access to assets.

Project compatibility - Solved - creating a project on a 2D core, unifying engine versions.

Piston mechanics - Unsolved - active search for similar solutions, experimenting with engine tools.

Increasing efficiency - Unsolved - increasing the amount of reporting by team members, increasing the number of personal meetings.


### **Conclusions & Next Steps**

As a result, the second week was successfully achieved, all necessary preparations for the further stage of project development were completed (All intermediate stages are omitted in this report, since they were successfully completed and no problems arose with them). However, there were also difficulties. The team encountered difficulty in implementing one of the key mechanics. Additional resources were allocated to the development of this mechanics and a backup implementation option was proposed (full inverse kinematics of the walker using procedural animation). To increase efficiency, it was decided to turn to familiar developers, AI, forums and other sources of information. In addition, the team can increase its efficiency if each of its members is more active in reporting and discussing all development-related events. The next steps are to continue working on the current mechanics and create a new list of needed mechanics. After all the fundamental (atomic) mechanics are implemented, the team will begin building the architecture described above and creating a test game level (namely a level, not a scene for experimenting with mechanics).

### **Project stages**

1. Creating a repository
2. Creating a Unity Project
3. Synchronization of work
4. Implementation of atomic mechanics (we are here)
5. Implementation of complex mechanics
6. Creating game levels
7. Finishing the project, eliminating problems (repeating steps 4-7)
8. Project release
   
 Steps 1-3 - preparing the environment for developing a game project. Steps 4-7 are the most labor intensive as they are the actual development.
