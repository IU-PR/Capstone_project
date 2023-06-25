---
weight: 1
bookFlatSection: true
title: "Week #3"
---

# Week #3 Report

## TODO

{{< hint danger >}}
Todo list of required parts to ensure that nothing missed
{{< /hint >}}

- [ ] Prototype Features: Outline the features and functionalities that you have
      successfully implemented in your prototype. Include any core interactions,
      user flows, or data management capabilities that are essential to your
      project’s goals.
- [ ] User Interface: Showcase the user interface design of your prototype
      through screenshots or interactive prototypes. Highlight the key screens and
      explain how users will interact with your application. If your project has no
      UI elements, you may skip this part.
- [ ] Challenges and Solutions: Share any challenges or obstacles you
      encountered during the development of your prototype. Describe how you
      addressed these challenges and provide insights into the solutions you
      implemented.
- [ ] Next Steps: Discuss your plans for the upcoming weeks and outline the
      features or improvements you intend to focus on. Create a priority list of
      features needed to be implemented. This will demonstrate your project’s
      trajectory and provide a glimpse into the future development phases.

## Prototype Features

This week was very productive for development!
For overview, list of features:
- develop mobile app under the hood business logic template, integrate NoSQL database and network management
- implemented mobile app basic ui
- adapted figma design for further ui development
<!-- TODO rephrase if text is not close enough -->
- proved concept that rust is able to run on mobile devices
- created mvp backed
- developed ML part for searching similar tasks

### Todo library

We successfully tested possibility to run Rust code on various platforms.
<!-- TODO complete paragraph -->

### Backend

We rich mvp state for backen. We have master backend (facade) that provide REST api for
clients. And isolate ML from direct requests. This help us to isolate changes in AI part
from client and vice versa. It makes easy to deploy heavy services separately and provide
green blue deployment process in future.


### Mobile app 

Desired approach is offline first, so starting point should be database, isn't it?
Besides it is very true, but database is just detail and other business logic should
be abstract from it. So we started from defining app specific models that used across all
internal parts. And created simple UI that give us a possibility to interact on mobile devices.
And afterwards we tested several databases. [Isar](https://pub.dev/packages/isar) showed awesome
development experience and work on all platforms. But to save possibility to change our mind, we
use abstraction over it.

## User Interface

We updated our [figma prototype!](https://www.figma.com/file/gc679jQhRxzZi29xVcwOO0/ui-workflow?type=design&node-id=0-1&mode=design):)
We intentionally left design more about UX, for since for mvp it is deadly important to focus on
primary features. Styling is postponed, but we plan to follow our style, [check it here](https://www.figma.com/file/gc679jQhRxzZi29xVcwOO0/ui-workflow?type=design&node-id=108-2&mode=design).
Well, to desribe primary mechanics, imagine that tinder made app for sorting your tasks.
Required time to implement it in figma is considerable, so we define basics and left
it to mobile devs. Wait for an update if it not fully clear now.

What about things already relized in app? Let's check gallery a bit

![app demo gif](./assets/week_3/v1-demo.gif)
![edit screen](./assets/week_3/v1-edit-screen.png)
![overview screen](./assets/week_3/v1-overview-screen.png)


And, as an interface for developers we integrated swagger!
<!-- TODO add swagger page -->

## Challenges and Solutions

We faced several challenges during development.
Firstly, it was not as obvious as we though to run Rust on mobile device. For now it is still quite
complicated manual process to link things for app publishing. In future we want to use scripts at least
but tends to integrate CI. And to separate direct native dependency in app, we want to create separate
package that will be used in app. So, it is quite painfull for now, but very rare since app uses mock
during library development.



## Next Steps

We want to update ui, since couple of bugs found and start implementing primary mechanics. Since 
required parts satisfy it tends to be not too complicated.
Second part is to get rid of pain during native code update. This is quite challenging task but not
emergent. So we plan to fit into two weeks with that.

Backend reach state when we are not bounded with it. So, for the next week our developer will
help with todo library. This made not only to speedup the overall development process, but also
to decrease [bus factor](https://en.wikipedia.org/wiki/Bus_factor). But minor changes are planned, 
to get some authentification process for mobile app.


