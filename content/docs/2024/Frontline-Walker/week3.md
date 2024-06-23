---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:

The necessary technical infrastructure for the project (Unity game engine, IDE for C#, desktop github) was installed for all team members.

For further development of the project, a package for unity (2d animation rigging) was installed.

- **Backend Development**:

An analogue of the backend for our project are all scripts and other assets not related to the user interface. 
At the moment, most of the atomic mechanics have been implemented (explosion mechanics have been added, taking 
into account force, obstacles and distance, the walking mechanics have been changed to the first version of 
procedural animation, the mechanics of the behavior of air opponents and turrets are also ready). The project is ready to begin partial implementation of complex mechanics (for example, combining basic mechanics into enemy prefabs), but a number of atomic mechanics are still awaiting implementation (implementation of Neural Networks as an enemy controller, interface, etc.) or refinement (player movement).

- **Frontend Development**:

An analogue of the frontend for our project is everything directly related to the user interface and touch controls. Until most of the mechanics are completed, the interface cannot be fully formed. However, the team begins to make blanks (such as a sprite of binoculars on top of the camera in the test scene).
For the interface, controls are the first priority, followed by information about the walker's condition and amount of ammunition, then visual effects such as hit marks or the effect of a lens in binoculars. All of the above is planned to be added to the project, if possible, in parallel with the development of basic mechanics not related to the interface.

- **Data Management**:

The analogue of a database for our project is the assets stored in it. At this moment, the asset components are in development, upon completion of which they will be placed in the appropriate folders. The exchange of information between codes is also carried out using internal tools of Unity and C#.

- **Prototype Testing**:

Most of the implemented mechanics did not require changes during testing.
The air enemy mechanics have been restructured into two separate scripts to ensure proper modularity of the project and simplify future development.
The walking mechanics, based on the physical control of each joint of both legs, were implemented and worked properly, but were considered unsuitable. The user was required to simultaneously control both limbs with both hands, something most people cannot do effectively. In addition, although such mechanics made it possible to use neural networks as a controller for an enemy walker, but based on the experience of similar implementations found on the Internet for neural networks, it should have produced a result different from the required one.
The previous version was replaced by a walking mechanic using procedural generation. An empty object with a round collider was used as a controller, which became the root for the entire walker model. The body, legs and feet of the walker were sequentially attached to this object. A procedural animation script has been added to the body of the walker, based on a script from a third party source (https://www.youtube.com/watch?v=hrIimDYV0IA). The walker's leg joints were used for the skeleton of the procedural animation, the direction of the feet was controlled by a separately created script that rotated them down.
![ProceduralWalkingV1Demonstration](/2024/Frontline-Walker/ProceduralWalkingV1Demonstration.zip)

## **Weekly Progress Report**:

The team mostly continued developing atomic mechanics as planned, as well as drawing prototypes of in-game models and environments.

### **User Interface**:

Sprites for the game environment and interface are being actively developed. At this point in the project, the layering of sprites on top of the camera has been implemented, prototypes of the walker, background, etc. have also been drawn. For the needs of the interface and user experience, the walking mechanics were changed (instead of two joysticks to control each leg - one to adjust the height and movement of the walker, as on the interface prototype). The final version of the interface will be discussed by the team after the implementation of complex mechanics.
![handdrawn-prototype](/2024/Frontline-Walker/handdrawn-prototype.jpg)

### **Challenges & Solutions**

Sprites challenges: It was difficult to choose colors without it looking cheap. I selected several pictures with sunset lighting and after several attempts, the most successful one, in my opinion, was chosen. The success was in minimizing the number of colors so that the eyes would not run wild.
Some of the difficulties are described above (for example, the need to replace the walking mechanics and the replacement itself).
It was also noticed that the walker's feet do not always point down when walking, as we would like them to, but follow the direction of the lower leg joint to which they are hierarchically attached. The solution was a script attached to the walker's torso as a root element and constantly turning the feet in its direction.
While adapting the code from the above video, a slight modification of the code was required - the walker began to take a new step not upon completion of the previous one, but after a certain time had passed. This was done to comply with the style of the project.
The remaining mechanics were based on past projects of team members and did not pose any difficulties during development and testing. (However, some mechanics have been reformatted while maintaining the logic of work, to increase modularity and simplify code modification)


### **Conclusions & Next Steps**

In general, this week can be called successful and productive, however, in order to have time to polish the project by the deadline, it is planned to put in even more effort in the next week. 
plans for interface: We have already selected interface samples. Our plans are to successfully combine a loaded interface as if from the cockpit and mobile control. Joysticks, buttons, so that everything is located conveniently. We also plan to speed up the pace and draw several options for obstacles with such characteristics as fragile/hard, high/low.
The team plans to transfer part of the resources to the development of interfaces and its binding to controllers. In addition, it is planned to implement the remaining atomic mechanics, compile a list of new ones, as well as the first attempts to assemble them into complex mechanics and construct assets. The movement model will undergo modification to the second version (with the ability to adjust the height and disable damaged limbs) and the third version (with the ability to destroy obstacles depending on their strength and the weight of the walker) sequentially after testing.
