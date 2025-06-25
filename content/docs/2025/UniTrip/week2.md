---
title: "Week #2"
---

# **Week #2**

## Detailed Requirements Elaboration

### User Story 1: Moving around the location

**As a** player **I want to** move my character around the university locations so that I can explore the university and get a feeling of its atmosphere.

**Given:**  
I’m a player in the game on the first location (main hall).

**When:**  
I tap/click on location area parts on my screen.

**Then:**  
- The character moves accordingly on the screen.
- The character cannot leave the predefined bounds of the location.
- Movement is responsive and smooth.

### User Story 2: Talking with NPCs

**As a** player **I want to** interact with NPCs so that I can learn more about the university life and students.

**Given:**  
I’m a player moving around the location and see NPCs(Professor/Security guard) with an interaction marker (!).

**When:**  
I click on the NPC.

**Then:**  
- A dialogue window appears with the conversation.
- I can progress through the dialogue using button next or choices button.
- After completing the dialogue, the dialogue window closes.
- Game state updates accordingly (unlocking new quest with "!" or moving to next location).


### User Story 3: Starting the game from the main screen

**As a** player **I want to** start the game from the main menu so that I can enter the gameplay easily.

**Given:**  
I launch the game and see the main screen.

**When:**  
I press the “Start” button.

**Then:**
- The first location loads and gameplay begins.
- Background music starts.
- I see a prompt to follow the “!” signs.
- The character appears at the entrance of the university.



### Prioritized backlog
We created the backlog with tasks for all weeks and planned to follow the sprints. The workload on each members are spreaded and trying to be balanced, however during the planning we noticed that on first week there are more work for designers, because we need to create a lot of design and 3D models, however in the last weeks the load on the developers team is more, because of hard features to implement. We cannot avoid it, because it is a flow of our project and will try to balance between weight of tasks as we can. Thats the reason why we decided to divide the sprint deadlines on two parts to balance the designers and developers:  
during the first part of week designers create all staff, required for the week tasks and then developers during the second part of week implement it and repeat the process. During the gap each part of team could start work, which do not depend on previos implementations.  

For backlog we chosed Jira, because among all tools checked by PM (such as Asana, github issues and gitlab milestones) - it shows the better and wide functionality and customization such as custom fields (in Asana its paid), free usage for team less than 10 people and illustrative interface with sprints (in conrtast to github and gitlab, where milestones are separate of each other in different pages).
To check our backlog follow the link:
https://unitrip.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog


## Project specific progress

### Whole team progress
- Finalize the narrative for the game.  
- Agreed with the customer ideas, narrative and plans for testing and using a game.

### PM
- Created a backlog with all spints and estimation
- Create a user flow diagram for the whole project

### Design
- Finalize the 3D model of first location with background sprites and upload to Unity
- Create a sprites for 4 characters of the first location
- Finalize prototyping for the whole project


### Unity development
- Create the zero welcome scene with the start button and transition to the first scene 
- Crete a main character walking through the first location
- Create a first interaction scripts without designed sprites

### ML
- Start creation of dataset for AI assistant


# Weekly commitments

## Individual contribution of each participant

**Marina Lavrova(Lead)** - organized the teamwork, spreaded the tasks, created a [backlog](https://unitrip.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?label=Design&selectedIssue=SCRUM-27), organized team meet with [narrative](https://docs.google.com/document/d/1iMLAHSx76uULx53z7i-xRVh0EfPteNgj682SRBlNNjo/edit?usp=sharing) finalizing and created user flow [diagrams](https://www.figma.com/design/lSDrdh8XspHjlDYsoE9kKA/User-flow-diagram?node-id=0-1&t=0SVQ1DFlW8wU7V0n-1)  
**Merkulov Leonid** - created a [zero scene](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/40ff76e14b6fe52d76210442ddbfd3ce816e9a65) with start button and the main character [walking](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/1dcb50252706a240fadd15ad4310222edfd4f9f7), upload paricipated in [narrative](https://docs.google.com/document/d/1iMLAHSx76uULx53z7i-xRVh0EfPteNgj682SRBlNNjo/edit?tab=t.0) writing  
**Ivan Makarov** - organized meet with customer, created a [interaction scripts](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/c6fd8b068f9abc1d45d6cbfd09d94788ca171398) with objects on location, participated in [narrative](https://docs.google.com/document/d/1iMLAHSx76uULx53z7i-xRVh0EfPteNgj682SRBlNNjo/edit?tab=t.0) writing, start collecting [dataset](https://drive.google.com/drive/folders/1tLW5yMGEfuf8ABdVGM7FMp_B2li4KbN-?usp=sharing)    
**Tarubarova Nadia** - finalized creating the [first location](https://drive.google.com/drive/folders/1tOgQVp6NgdZlooWGwSPTcuapUi9yx5kQ?usp=sharing), participated in [narrative](https://docs.google.com/document/d/1iMLAHSx76uULx53z7i-xRVh0EfPteNgj682SRBlNNjo/edit?tab=t.0) writing   
**Pokhodyaeva Polina** - created [sprites](https://drive.google.com/drive/folders/13HPbsBE8fOnZaMYTB2S0OX5y6IpHdIcc) for 3D location background, created [sprites](https://drive.google.com/drive/folders/11HQP3-jThDvhKhujYdB21xxgTCo_IqBf?usp=sharing) for 4 characters in first location, finalized the whole project [protorypes](https://drive.google.com/drive/folders/10yk3KXb1-QyhiQZRcKuYPSGiJnsx5py9?usp=sharing), participated in [narrative](https://docs.google.com/document/d/1iMLAHSx76uULx53z7i-xRVh0EfPteNgj682SRBlNNjo/edit?tab=t.0) writing   

## Plan for Next Week
- Create a 3D model of the all characters in first location and upload it
- Create a sprites for dialogue screens and "!" signes
- Implement all interactions in first locations (first MVP version)
- Add deploy to GitHub pages
- Start creation of the second location (sprites for background and 3D model)
- Finalize the dataset collection and train initial version of a ML model.


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✓] In working condition.
- [✓] Run via docker-compose (or another alternative described in the `README.md`).

## Run the project
Full project and initial version of the game you could see here:  
https://github.com/IU-Capstone-Project-2025/UniTrip  
