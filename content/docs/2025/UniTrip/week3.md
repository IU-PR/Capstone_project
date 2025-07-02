---
title: "Week #3"
---

# **Week #3**

## Implemented MVP features
- Create a 3D model of the all characters in first location and upload it
- Update 3D model of the first location(add bg sprites and fix some objects)
- Create a sprites for dialogue screens and "!" signes and upload it
- Implement all interactions in first locations with designed sprites
- Add camera transition for the dialogue scenes
- Add animation of walking
- Fix bugs with walking in unrestricted zone and glitching of character

If summarize everything we create full user journey in first location with all interactions, functionality and also add animation and camera transitions for better user experience. 

During the deploy to the gh-pages we faced some issues with access to github actions and then with WebGL specific moments, so decided to focus on MVP features implementation and reschedule the deploy part to the next week, where according to the requirements it asked. For now we tested web verion locally and it works, for deploy on pages we need more time. For getting the MVP you could use the created [build](https://github.com/IU-Capstone-Project-2025/UniTrip/releases/tag/v1.1.0)

### Full user journey

0) Open the game
1) Click the button start
2) Click the "!" sign for first character - security guard
3) Read the dialogue and click on the screen to continue
4) Walk through area and click the "!" sign for the second character - Professor Burmyakov
5) Read the dialogue and click on the screen to continue
6) Click to the last "!" sign for the third character - 2nd security guard
7) Read the dialogue, click on the right answer or try again
8) Click continue and go to turnstille to go to the second location

## Demonstration of the working MVP
You could see full demo and screenshoots [here](https://drive.google.com/drive/folders/1FiEUsC9ZYDPfgYo-tCPPDZgA6FGsVrWJ?usp=sharing)

### First interaction
![First interaction](https://github.com/IU-Capstone-Project-2025/UniTrip/blob/main/assets/week3/first_interaction.gif)

### Update states of "!"

![Update states](https://github.com/IU-Capstone-Project-2025/UniTrip/blob/main/assets/week3/states_updates.png)

### Dialog
![Dialog](https://github.com/IU-Capstone-Project-2025/UniTrip/blob/main/assets/week3/dialog.png)

### Dialog with choices
![Dialog with choices](https://github.com/IU-Capstone-Project-2025/UniTrip/blob/main/assets/week3/choices.png)

## ML

### Model Architecture
We used microsoft/phi-2, a small but capable causal language model (decoder-only transformer) with ~2.7 billion parameters. It is optimized for reasoning and instruction-following tasks.

### Training Data
We created a custom dataset from publicly available text documents about Innopolis University, such as:
- A university information sheet (Справка об Университете Иннополис.docx)
- A guided tour program document (Программа экскурсии по УИ.docx).  

Combined into one large .txt file: innopolis_data.txt.  
From that, we automatically generated training samples in the following format:
```
{
  "instruction": "Что ты можешь рассказать по следующей теме об Университете Иннополис?",
  "input": "",
  "output": "Университет Иннополис — это современное высшее учебное заведение, специализирующееся на IT и инженерии..."
}
```
This dataset was split into train/test subsets, typically 90% training, 10% validation.

### Training Parameters

We used the Hugging Face Trainer API with the following configuration:

Model - microsoft/phi-2  
Batch Size - 2 (per device)  
Epochs - 3  
Max Sequence Length - 512 tokens  
Learning Rate -  2e-5  
Weight Decay - 0.01  
Warmup Steps - 10  
Mixed Precision (fp16) - Disabled (CPU only)  
Optimizer - AdamW  
Padding Token - Same as eos_token  

The training was done on CPU due to hardware constraints, meaning slower runtime but functional with a reduced dataset.


### How the Model Makes Decisions
Once trained, the model makes predictions using causal decoding:

1) It receives an instruction (question or prompt).

2) It tokenizes the input and passes it through the transformer layers.

3) Based on its internal weights (adjusted during fine-tuning), it predicts the next token one-by-one until a stop condition is met (e.g., end-of-sequence token or max length).

4) The response is decoded back into human-readable text.

The model uses self-attention, which means it considers all previous tokens in the context window when generating each new token. Fine-tuning makes the model more likely to prefer responses grounded in your data.

**Link to the training code**: [link](https://drive.google.com/drive/folders/1tLW5yMGEfuf8ABdVGM7FMp_B2li4KbN-)  
**Links to the initial model artifacts**: [link](https://drive.google.com/drive/folders/1tLW5yMGEfuf8ABdVGM7FMp_B2li4KbN-)

## Internal demo


During the internal demo we noticied several bugs and parts to improve:
- when main character turn around - it sometimes overflow the locations model
- not understandable how to continue during the dialogue
- dialogue text in some parts is boring
- text font looks weird
- during the scene with Professor Burmyakov the sprite of the bg of cava looks weird
- Professor Burmyakov and 2nd security guard without skin
- Animation of moving should be more realistic, and also shadow glitching during the animation
- The 3d model contains some redundant sprite of the glass in the corner
- Good to add light

Then we discussed the priority of this ideas

**Priority tasks(will completed during next week)**
- update collaiders sizes(to avoid overflow)
- add text hint "click to continue"
- update texts
- update font, colors and fix alignment of text
- change camera position

**Need to be discussed (need help in resolving issues)**
- fix bug with skin texture of 2 characters

**Need to be done, but later(week 7 with resolving bugs)**
- Update animation of character moving and fix shadow
- Fix 3d location corner texture
- Add light

After all we updtaed the backlog and splitted the task for the next week between the team

# Weekly commitments

## Individual contribution of each participant

**Marina Lavrova(Lead)** - organized work and 3 team meets(sprint planning, tasks check in the mid of week and sprint retrospective with planning for next week), collected the feedback from testing session, updated the [backlog](https://unitrip.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?assignee=712020%3Aaa1621bd-0ebc-4918-974f-e4df728ce60d), created a [demo](https://drive.google.com/drive/folders/1FiEUsC9ZYDPfgYo-tCPPDZgA6FGsVrWJ?usp=sharing), add init version of [gh-pages](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/e9fd282da6feb8b6e6706e98f1332dcb4be3510d) with solving bugs

**Merkulov Leonid** - [fixed](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/993a44051fea7e8034f11da50d5c69f45e0840f8) character moving and added animation, [add](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/03750f0d0a54f59bd2532194ac532fc1c7839c61) dialog interactions and implement them for 3 characters, [add camera transition](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/74c7c6854db9837510269a977d6b7d0903e67ed4), upload 3d models of [characters and location](https://github.com/IU-Capstone-Project-2025/UniTrip/commit/59fddc818f8d4bbd9affa855e454828ae88e0800), check all commits [here](https://github.com/IU-Capstone-Project-2025/UniTrip/commits/v1.1.0/).  

**Ivan Makarov** - finalized the [dataset](https://drive.google.com/drive/folders/1tLW5yMGEfuf8ABdVGM7FMp_B2li4KbN-), train a [model](https://drive.google.com/drive/folders/1tLW5yMGEfuf8ABdVGM7FMp_B2li4KbN-). 

**Tarubarova Nadia** - created 3D models of [characters](https://drive.google.com/drive/folders/1SCWUktnMDkrhyACH4vOi0N1BnLhQe6C3?usp=share_link) for the first location, and fixed 3D model of the [first location](https://drive.google.com/drive/folders/1DzZf5G3drAUxYQ7efT0owwVSzABO9ym5?usp=share_link)

**Pokhodyaeva Polina** - created [sprites](https://drive.google.com/drive/folders/1KsW154ZuQXik0OXDuvlWU6mL0Q5XtTSD) for dialogue screens, "!" marks and stated fonts, created detailed [prototype](https://drive.google.com/drive/folders/18uRJz-ha5B0eQUZthT0oTfeQjx_a9wBX) for the second location

## Plan for Next Week
- Fix bugs noticed in first location
- Create a sprites for background for the 2nd location
- Create a first version of 3D model the second location
- Create sprites for first part of interactions (108 auditorium)
- Upload 2nd location to Unity and implement first part of interactions(108 auditorium and professor Shilov)
- Create a connection of trained model to Unity
- Add Unit tests
- Add CI and fix CD
- Start creation of prototypes for characters on the second locations
- Start creation of characters for the second location


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✓] In working condition.
- [✓] Run via docker-compose (or another alternative described in the `README.md`).