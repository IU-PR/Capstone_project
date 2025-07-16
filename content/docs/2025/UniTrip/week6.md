---
title: "Week #6"
---

# **Week #6**

Code Freeze date is this Sunday 20th of June.

## Links

- **Deployment**: https://github.com/IU-Capstone-Project-2025/UniTrip/deployments  
https://github.com/IU-Capstone-Project-2025/UniTrip/releases
- **Design**: https://drive.google.com/drive/folders/1tUE_X1SlwDvRpjWii1ShtD2xwbUh5oWw?usp=sharing
- **Demo**: https://drive.google.com/drive/folders/1V3TFQ9x-W3XwaodKQAQTNzkMqSIU2pbS?usp=share_link
- **ML model**: https://huggingface.co/cody82/innopolis_bot_model


## Final deliverables

### Project overview



**UniTrip** is an interactive Unity-based game that offers a virtual tour of Innopolis University.  
It is designed to help students, parents, and tourists explore university life even if they cannot visit it physically.

The player explores detailed 2.5D university locations, interacts with NPCs (students and professors), and participates in mini-quests and dialogues to learn more about student life, infrastructure, and feel the atmosphere of the university.

At the current stage, two locations are fully implemented — including quests, walking, and NPC interactions.

### Features

- ✅ Two fully functional locations:
  - **The outer hall**: 3 NPC's with dialogues, passing through metal detector and turnstile
  - **Main Hall**: 2 NPC's and 2 miniquests:
    - **Auditorium** - explore 108 room and find 3 objects
    - **Vending Machine Zone**: buy some snacks or drinks
- ✅ Dialogue system for NPC's (professors, guards and student)
- ✅ Scene transition system
- ✅ Character movement + interaction trigger zones
- ✅ 3D models and assets designed in Blender and Procreate
- ✅ Signal "!" and "i" sings to all interactions
- 🚧 Basic implementation of chat interface (UI without final design)
- 🚧 ML model for AI-guide (integration pending, will be completed before Sunday)

### Tech stack

- **Unity** 2022.3.56f1 — game engine
- **Blender** — 3D modeling of characters and environment
- **Procreate** — 2D design of characters, objects, and UI
- **C#** — scripting and logic
- **Google Drive** — collaborative design/documents
- **GitHub + GitHub Pages** — version control and deployment
- **LLM-based AI (planned)** — used for contextual dialogue (in progress)


### Setup instructions

Follow the webpage and open the game  
https://github.com/IU-Capstone-Project-2025/UniTrip/deployments

if it doesnt work becuase of some issues you could also use our released build here:  
https://github.com/IU-Capstone-Project-2025/UniTrip/releases
## Presentation draft

https://www.figma.com/design/i53mGIjdl5nX5xkG6WmsJ2/UniTrip?node-id=39-2&t=Y8yohbemqqmK2liK-1
# Weekly commitments

## Individual contribution of each participant

**Marina Lavrova(Lead)** - organized work and managed the last tasks of the work, wrote [text](https://docs.google.com/document/d/1-o0qwfHCAGDmvtK15Bc0ViVmdquCL1-UFHGuJlWN9Gw/edit?usp=share_link) for final demo, created [demo](https://drive.google.com/drive/folders/1V3TFQ9x-W3XwaodKQAQTNzkMqSIU2pbS?usp=sharing) 

**Merkulov Leonid** -  fixed interactions on the second location, added start screen with design, implemented chat screen - all [here](https://github.com/IU-Capstone-Project-2025/UniTrip/commits/v2.0.1/)

**Ivan Makarov** - load the model to [hudging faces](https://huggingface.co/cody82/innopolis_bot_model), tune the model, trying to create connection with Untiy

**Tarubarova Nadia** - created the [first screen](https://drive.google.com/drive/folders/1L1DSVXuyZEBRLMX37ywX76_2UyVmoYyY?usp=sharing) of the game, fixed the [text](https://docs.google.com/document/d/1-o0qwfHCAGDmvtK15Bc0ViVmdquCL1-UFHGuJlWN9Gw/edit?usp=share_link) for presentation

**Pokhodyaeva Polina** - created a [prototype](https://drive.google.com/drive/folders/1mqKbgIN0dFVr1hg1rUJXAJVL_0jLILtM?usp=share_link) design of chat with ML, created the [draft](https://www.figma.com/design/i53mGIjdl5nX5xkG6WmsJ2/UniTrip?node-id=39-2&t=Y8yohbemqqmK2liK-1) of presentation

## Plan for Next Week
> Until the Sunday

- Finalize the chat with ML
- Add description to the 2 mini quests in 2nd location
- Minor bug fixes

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).