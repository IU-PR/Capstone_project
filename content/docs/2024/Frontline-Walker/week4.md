---
title: "Week #4"
---

# **Week #4**

## **External Feedback**

To obtain feedback, acquaintances from the field of computer game development were interviewed. With their help, it was possible to collect useful information:

The character controller can be improved. Now he is applying force to the walker object strictly to the right and left. In the new controller, the force can take into account the angle of inclination of the surface on which the walker is currently standing (the position of its feet) to manually set the speed of movement on slopes of different steepness and limit the angle of ascent.

To improve the ambience when the walker moves, it is worth adding up and down swaying of the walker body and gun. The force of rocking should depend on the height of the walker.

The speed of the walker can be varied. For example, a walker can back up noticeably slower than it goes forward.

The walker can interact more visually with the surface, taking into account its material and slope.

The behavior of an enemy aircraft can be changed by leaving it with only one bomb run per player, during which shooting down this enemy will be the player's highest priority.

The binoculars can not only move the camera away from the walker when pressed, but also force the camera forward.

The interface also received a number of tips for improvement. It was proposed to move the gun tilt control slider so that it corresponds to the maximum and minimum horizontal angles of the gun direction. It was also proposed to change the icons for binoculars, fire from the main and secondary guns.

### **Testing**

Testing of the project is carried out in different planes. Individual scripts are evaluated by analyzing their complexity and monitoring indicators of computer resource usage and frames per second (a good example of a program for evaluation is MSI Afterburner). Each individual mechanism is evaluated for compliance with the idea and user response to its implementation and use. The same goes for the interface.

Based on the results of testing this week, the interface and walking mechanics were improved (now the feet are inclined towards the inclination of the surface, the walking speed of the walker has been changed backwards).

#### **Iteration**

At the end of each week, a list of finished mechanics and components of projects is compiled, a list of new ones that need to be implemented is compiled, which also includes mechanics and components that require improvement.


Based on the results of this week, the list of mechanics is as follows. 
Implement:

1. Mechanics of shooting from the main gun (steering, recoil mechanics + projectile shooting mechanics).
2. Destabilization mechanics (if the speed is too high, the body of the walker will quickly sink to the ground and be damaged).
3. Mechanics of spawning opponents and players (scene controller)
4. Mechanics of modularity of the walker (add a separate layer of colliders for reading hits, blocking legs, hp of modules)


Edit:
1. Projectile mechanics (add custom ballistics)
2. Walking mechanics (add shaking)
3. Mechanics of binoculars (moving the camera forward)

##### **Challenges & Solutions**

This week the team was mainly focused on improving existing mechanics and prototyping the interface, so they didn’t encounter any particular difficulties along the way.

During the creation of the mechanics of inclination of the foot to the surface, the incorrect Vector3.Angles function was used, instead of the Vector3.SignedAngles function (according to title, allows to receive negative angles, wich solves problem with slopes with negative angle, such as -15 equal to 345).

While finalizing the mechanics of the explosion (adding rays of force application to correctly knock over objects behind a partial barrier), the project froze due to the fact that the offset in the corners was +0. After noticing a typo, the team solved the problem.

###### **Conclusions & Next Steps**

At the end of the week, a large amount of positive feedback and tips for improvement were collected. Some of them were implemented in the project this week. Next week it is planned to complete most of the mechanics and create the first version of a full-fledged interface.
