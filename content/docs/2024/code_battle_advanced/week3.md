---
title: "Week #3"
---

# **Week #3**

## **Developing the first prototype, creating the priority list**

- **Technical Infrastructure**:
  Our team is using [Innopolis Gitlab](https://gitlab.pg.innopolis.university/) for a shared development environment and
  everyone is familiar with the said platform. To speed up the initialization we have a file called launch.sh that
  initializes the system. We do not require any more Infrastructure for effective development, but may create a CI/CD
  pipeline to check for general tests.

- **Backend Development**:
  The backend part of our project is already in a state for a minimal value product, but we are constantly adding more
  improvements to achieve better security and a wider variety of options for languages and modifications support.

- **Frontend Development**:
  Our team has completed the barebones functionality of the current model of the website, but we still find areas of
  improvement and we are currently mid-way through creating a user-friendly look and implementing it. To see the current
  look of the website, please watch our video that you can find after this general section.

- **Data Management**:
  The current state of our data management allows for all the features that we were planning to use it for, but we are
  still improving our safety and creating more interactions that require tweaks to the system.

- **Prototype Testing**:
  The current prototype is working precisely as intended, without any deviations from our expectations, the available
  features are working in a stripped down version, but they allow for all the necessary testing and showcasing. For a
  more detailed look, please refer to the video we are providing in the very next portion of this report. As for
  refinements of the current abilities, we are improving every bit of functionality, but there is no significant
  direction to underline in this part as all parts are currently under some sort of tweaking to fit our view of the
  project.

- **Video showcase**
-

[![Prject video](https://img.youtube.com/vi/aW6B97lPjbg/0.jpg)](https://www.youtube.com/watch?v=aW6B97lPjbg)

That is what is visible from the client side, but for the insides you can see the logs of Kubernetes:

![w3KubernetesStatistics.png](/2024/code_battle_advanced/w3KubernetesStatistics.png)

## **Weekly Progress Report**:

For a video of the prototype please click on the video that is put before this section with a photo of the Kubernetes
logs. Now, for the code itself, you can visit [GitHub](https://github.com/IU-Capstone-Project-2024/code-battle-advanced)
to view it.

### **Prototype features**

Whilst we are still lacking the activities that we were promising, the underlying structure is now sufficient to start
implementing them, as well as the judging is now in working order, although it requires us to make more adjustments to
improve security. As for core interactions, all of them are already working as described several times with this photo
in mind:

![Diagram.png](/2024/code_battle_advanced/Diagram.png)

Other than that we do not see what needs to be reported in this part of the document.

### **User Interface**

We are already working on it, and it is already in working order, just needs polishing and improving. For a more visible
understanding, please refer to the video that we have showcased.

### **Challenges & Solutions**

1. Creating a uniform style. Define the colors, fonts, and styles that match our product to create a consistent design
   for all pages.
2. Adaptive design. Using media queries to adapt styles to different screen sizes and devices.
3. Stylization of forms. Apply styles to various form elements such as input fields and submit buttons to make forms
   more attractive and user-friendly.
4. Animations and transitions. Using CSS properties such as transition and animation to add animation when interacting
   with elements.
5. Creating user interface elements. Using CSS to style elements to add interactivity to create custom interface
   elements such as buttons, shapes.
6. One of the teammates took desperate measures on trying to learn coding via Vim Code Editor for a more productive
   development along with the use of git commands via Terminal. Roughly, this mistake took two weeks that could bring
   successful code delivery. Now the lessons demonstrated that IDE is an integral part of creating the projects.
7. Regular changes of database structure(number of tables and its columns) should have been avoided originally from the
   initial project planning of week 1. Violating such precautions led to a substantial amount of time wasted on this
   little part of the code.
8. Designing and partially implementing a simple but powerful system for contest customization. It is very hard to make
   everything fit nicely with the systems that are already implemented, although I believe I have managed to do it.
9. Debugging of just one container from the system. Rebuilding the whole architecture takes a while. Thankfully,
   kubernetes allows removing any part and substituting it with a newly built version with changes applied in the code.

### **Conclusions & Next Steps**

A set of wrong decisions have been made that caused significantly reduced efficiency of some developers. Still, the
platform keeps its evolution with features planned to appear in the next week that will set us apart from the
competitors. As for the next steps, the team is now ready to work at full capacity and will attempt to do so to improve
the existing code and make the planned modules such as activities into reality, which should separate the workload
between the two directions and allow us all to achieve greater effectiveness. 
