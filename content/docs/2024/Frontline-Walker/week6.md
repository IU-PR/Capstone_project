---
title: "Week #6"
---

# **Week #6**

## **Presentation**:

PLease, read comments to presentation!

https://docs.google.com/presentation/d/14hUs5JRxWqL4QVvdDLyFbe-fYAG-L3Khff139UsCNiE/edit#slide=id.g2ec0fb28cb1_0_90

## **Weekly Progress Report**:

This week was the most productive of all. The reason for this was the proximity of the project presentation date, inspiring feedback, improvement in production processes (the team began to meet in person more often, which made it possible to talk about problems and tasks faster, and better explain the requirements).

The game featured a touch interface. Now it functionally almost completely coincides with the prototype (there is no anti-aircraft machine gun yet and, therefore, there is no control for it), however, it does not fully display information about the walker in comparison with the prototype (there is no display of modules health, the display of remaining ammunition and fuel is still only numerical). Fortunately, the project was able to implement curved sliders that display the gun declination angle (there is no such slider in standard Unity tools, so it was written from scratch).

A new enemy was assembled - an airplane. It carries bomb weapons (which can be hit in flight, thereby destroying it).

Modular walker health with a penalty system was implemented. Damage to the feet leads to slight deceleration and reduced braking ability. Damage to the lower legs results in moderate deceleration and reduced rate of body height adjustment. Damage to the upper legs causes significant deceleration. Damaging a weapon prevents the player from aiming and firing. Torso damage is critical and restarts the scene.

New sounds and sprites were created (such as walker engine sounds and an improved walker model).

A playable build of the mobile version of the game was assembled and tested on different devices. The results are satisfactory, but in the future it will be necessary to add interface customization in the form of changing the position and size of the buttons.

### **Challenges & Solutions**

The team encountered many difficulties when implementing the interface and modular health system.

The currently used hierarchical system of components, where the components of the lower layers are in no way connected with the components of the higher layers, previously greatly helped the team, ensuring the modularity of all objects on the stage, as well as ease of assembly and replacement of prefabs and debugging. However, the modular health system required components of higher layers to instantly respond to damage to internal modules. One solution was to scan each module for damage every tick, but this is too resource-intensive as the number of modules and enemies increases (for opponents a modular damage system is also used, for example, a barrel - a base for a turret). Another solution was to instruct the internal modules to send signals to the modules above that they were damaged. However, to do this they would need information about the modules on top, which is contrary to our architecture. The solution was to create the Message Sender module and the abstract Message Receiver class. The first could send signals to anyone of the second (normal and terminal, which necessarily led to the complete shutdown/destruction of the object). Any component that could receive messages from modules above (rather than polling them itself) became an inheritor of the abstract class. This allowed the team to create a non-hierarchical messaging system without losing modularity or interchangeability.

A bent slider was also a separate test. The team couldn’t find anything suitable either in standard tools or in the official asset store, so they created it from scratch. It consists basically of a slider that tracks clicks on it and monitors the position of the cursor until the mouse button is released. Using the vector of the difference between the cursor position and the center of the slider circle, the angle of inclination of the slider and its position on the circle were calculated.

Previous ideas of introducing adversaries with neural networks as brains turned out to be unviable. Current opponents attack from too close a distance along an almost flat trajectory, which deprives neural networks of their advantage in variability. The idea of ​​​​attacking opponents of different walker modules did not make much sense, since the player cannot fully fight this (except for shooting opponents from a distance beyond their reach). In this regard, the design of a new enemy was developed - a mortar turret. This turret will be controlled by two neural networks at once. The first will analyze the player's last positions (possibly also the distance to him) and his current speed to predict his position after some time (during which the turret projectile will fly). The second neural network, based on the results of the first one, as well as the speed of the projectile, the distance to the player and the current pointing angle, will aim the gun (which automatically fires a salvo after reloading). Neural networks will train independently of each other. It is assumed that it will be more interesting for the player to fight such an enemy, because he will have to carefully monitor the mortar, try to deceive its aiming, and also quickly change his position after firing the turret (which will have to be monitored with the help of binoculars, which do not allow you to control the walker).

Building the build was quite a troublesome process. Firstly, the system for processing events from the interface that we used (Standalone Module System) turned out to be outdated. However, the new version (InputSystemUIInputModule) did not have the functionality we needed. I just had to ignore the warning. In addition, the project has grown sufficiently that it does not have more than five gigabytes of disk space for assembly. I had to perform a clean build on a separate disk with one hundred gigabytes of free space (on the phone). The last problem was the team’s lack of a license; the built-in Windows defender considered the game build to be virus software and automatically deleted it. I had to disable it in order to transfer and install the build (the team does not recommend this method due to its insecurity).

### **Conclusions & Next Steps**

The team did a great job and managed to implement a number of complex, complex mechanics. Unfortunately, a number of the functionality originally conceived will most likely not be completely ready by the time of presentation, but it already looks presentable enough to show the essence of the original idea. During the final week, the team will implement existing sprites into the game, complete the interface, and add an anti-aircraft machine gun. If time permits, sounds and neural networks for a new enemy will be added. Also, the main task of the team will be to prepare a presentation and text for it, as well as upload the project on the ITCH.IO website.
