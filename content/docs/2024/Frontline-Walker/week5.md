---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

Our team has several ways to collect feedback on the project:

1. Ask familiar video game developers (from previous educational institutions, universities or online communities) to share their impressions.
2. Ask professional game developers to share their impressions. It is rare for students to meet such people, but many professional developers can be emailed asking for help.
3. Ask video game analysts (for example, game journalists) to share their impressions. Getting the attention of such individuals is sometimes even more difficult, but regularly reminding yourself of yourself can help.

Feedback from the first group can be collected using Internet resources to create surveys with virant answers and open-ended questions. Due to the large number of potential respondents, this method will allow the team to collect fairly accurate statistics on product satisfaction and many different ideas for possible improvement of the project.

With the second and third group, the team should take a different approach. It is worth conducting an interview or simply a more detailed conversation with everyone we interview, because due to their experience, they can very accurately identify the weaknesses of the project and give the most useful advice on improving our game

- **Conducted user surveys or feedback sessions**

The team interviewed familiar video game developers who gave some useful advice on improving projects (adjusting camera speed and proximity, adding gun rollback, etc.), but they found it difficult to give an overall assessment of the project at the current stage. The team will have to complete a number of key components before the project can be considered a full-fledged MVP (the game has a test level with full controls and constant addition of mechanics, however, it is not enough to reflect the team's vision of the project for full demonstration to potential clients).

In addition, the team met with popular analysts in the community and received advice on implementing bold ideas. Despite their riskiness, their chance of success is much higher than using proven and popular mechanics alone due to the oversaturation of the video game market.

![MeetingWithJournalists](/2024/Frontline-Walker/MeetingWithJournalists.jpg)

- **Analyzing feedback, identifying and prioritizing issues**

A number of mechanics that our colleagues advised us were easy to implement based on existing code. Others were analyzed, prioritized and included (if realization is possible with our skills) in the project development roadmap.

## **Roadmap**:

Implementation of a damage system for player and enemy components.

Implementation of a fuel and projectile resuply system.

Implementation of enemy control using neural networks.

Implementation of a touch interface.

Implementation of transition between scenes.

Adding sprites, visual effects and sounds to the game.

PROJECT PRESENTATION.

Adding new walker modules.

Adding environmental destruction based on the walker's weight.

Improving the interaction of individual project components and their operation. (optimization)

Adding the ability to replace walker modules (build your own model from existing modules).

Extrapolating content to new levels.

An attempt to introduce procedural generation.

An attempt to add a cooperative mode on one/two devices with separate control of movement and weapons.

The steps described after the presentation of the project are major milestones in the development of the project. After implementation (sometimes during) each step, feedback will be collected to evaluate the work done and formulate a new one.

The steps described before the presentation of the project are smaller intermediate stages. The highest man-hour costs are expected in the last 4 stages. Fortunately, they can be performed independently of each other.

## **Weekly Progress Report**:

Inspired by expert advice, the team managed to implement many mechanics. Firing from the main gun, recoil and rollback of the gun, limitation of ammunition and rate of fire, basic behavior of enemies (detection, guidance, attack), rotation of the projectile in flight along the velocity vector, etc. were added. Destabilization mechanics were improved (now completely dependent on speed, shooting from the top position is not spared, and enemy shells can critically accelerate), binoculars (attached to the walker. It has touch controls, adjustable magnification and position, remembering the last position), etc. In addition, the team continues to create model sprites (at the moment they are drawing a model of the turret and bombs) and recording sounds (grinding of metal, operation of mechanics, etc.). In addition to direct work on the project, advice and consultations were received from experts in the field of video games and colleagues.

![FirstTriesInTouchInterface](/2024/Frontline-Walker/FirstTriesInTouchInterface.png)
![TestingLevel](/2024/Frontline-Walker/TestingLevel.png)

### **Challenges & Solutions**

During active work, the team encountered many difficulties.

Some of the sounds (most) are missing or not suitable for free access. For full immersion, sounds are necessary, so one person from the team started recording them.

The project requires a large number of sprites. In addition to a banal increase in working time, it is planned to use neural networks to generate images and/or outside assistance.

The project is actively expanding, which has led to the complexity and complexity of the code. The code is not yet critical, but adding new functionality in an adequate form is becoming more difficult. What saved us from turning the code into spaghetti was the hierarchical system of modules adopted at the early stage of the project, the atomicity of logical blocks, and work on different functionality in separate scenes. To improve the situation, a review and analysis of the existing code is required, as well as time for its optimization, unification of style and refactoring. This step is mentioned in the roadmap, but the team may have to move it to an earlier stage, in the worst case before the presentation.

A number of difficulties were also encountered during the implementation of the mechanics described above. The solution was simple, thoughtful reading of the code and documentation. The team paid special attention to the rotation methods found in the quaternion class, the ray cast function from Physics2D and its arguments (the impossibility of passing a mask of physical layers without specifying the ray length), as well as the principle of operation of global and local coordinates in Unity.

### **Conclusions & Next Steps**

Based on the results of the work completed, this week is the most productive both in the direction of the project and in the direction of new professional acquaintances. Almost everything is ready to create a MVP, but the team hopes to do a little more to make the project truly memorable. Now the team is planning further progress on the roadmap, as well as starting preparations for the presentation of the MVP, selecting wording to highlight the existing functionality.
