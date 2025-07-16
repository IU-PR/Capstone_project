---
title: "Week #6"
---

# **Week #6**

## Links

- **Design**: [Figma with product design](https://www.figma.com/design/RteDCWd7yRf7yq2MyOUbD4/Killah?node-id=0-1&t=jgXC8QuecVqdQaXT-1)
- **Demo**: [demo video](https://disk.yandex.ru/d/5h_tWQ2GTu768w)
- **Codebase**: [Github](https://github.com/vladkalinichencko/Killah-Prototype)
  

## Final deliverables

### Project overview

Killah - is an AI writing companion that helps people start, continue writing, and form their ideas using a responsive macOS app with a custom post-trained on-device large language model. Our solution addresses three key problems in current writing tools:

1. **Creative Block**: Helps overcome writer's block with style-consistent suggestions
2. **Voice-to-Workflow**: Enables seamless transition from voice dictation to polished text
3. **Style Preservation**: Maintains the author's unique voice through personalized adaptation
   
## Installation & Setup
Setup instructions are provided in the repository's README markdown file.

## Technology Stack

### Frontend
- Swift & SwiftUI: Primary UI framework
- AppKit: Native macOS application framework

### Backend
- Python: Core backend language
- PyTorch: Machine learning framework
- Llama.cpp: AI model inference engine

## Core Features

### User Interface
- Theme Management: Dynamic theme switching capabilities
- File System: Comprehensive file management with customizable save directories
- Document Handling: File preview and saving functionality

### Text Editing Suite
- Formatting Options: Bold, italic, underline, and strikethrough text styling
- List Management: Support for both bullet points and numbered lists
- Typography Controls: Font family selection, highlighting, and dynamic font size adjustment

### AI Integration
- Autocomplete System: Intelligent text completion with configurable generation temperature settings

## Features in Development
- Story Generation: AI-powered narrative creation
- Advanced Text Editing: Enhanced editing capabilities
- Audio Transcription: Speech-to-text functionality
- Personalization: User-specific customization features

## Project Status
The application is currently in active development with core features implemented and additional functionality being continuously added to enhance user experience.
## Presentation draft

[Draft of presentation's structure](https://disk.yandex.ru/d/5h_tWQ2GTu768w)

# Weekly commitments

## Individual contribution of each participant

- **Janna**:
   - Designed the landing page. 
   - Compiled a report
   - Work has also begun on developing a landing page in Framer
   - create a draft of presentations structure
     
- **Kira**: I conducted experimental personalization of the Gemma model via Persona-Plug in three ways:
Using the English-language encoder BAAI/bge-base-en-v1.5 — as in the original paper. [commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/a0c284e340a239b26683a548f3fdffe55f6bc209)

  Using the multilingual encoder sentence-transformers/paraphrase-multilingual-mpnet-base-v2 to cover Russian. [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/dd5e0101499db1cb2ef2b1822f12c62f987ba067)

  Using the internal text encoder of Gemma itself, assuming that the embedded representation may be more consistent with the generation model. [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/e7fcdd04ab0fdce7575468978c784459cf5dbe2d)

I performed the full cycle of preparation, preprocessing, integration and training of projectors. Although I haven't yet achieved a consistent improvement, I'm confident that I can identify the source of the problems and continue to work on personalizing the model. Initially, training projectors for the first two encoders was unsuccessful — the loss remained high or grew, and the generation did not improve. An attempt to use the Gemma encoder also failed, which confirmed our assumption about the insufficient suitability of the embedded layers for the tasks of style embedding extraction. But finally, the first progress to merge embeddings has been achieved and now we start to see progress in training convervence and hope it'll become into the final version.

- **Vlad**: Completed App Development Tasks
  Most important – Added a Welcome window with a file explorer

 • Fixed theme switching in settings - Resolved issues with theme changes not properly applying or persisting in the application settings
 
 • Added support for two languages in the application - Implemented internationalization features to support multiple language options
 
 • Added base folder for document storage with configurable path in settings - Created default document directory with ability to change the storage location through settings
 
 • Redesigned WelcomeView - Updated the welcome screen interface and user experience
 
 • Added model deletion and re-download functionality in settings - Implemented options to remove and reinstall the AI model through the settings menu
 
 • Added default documents folder - Established a standard directory structure for document management
 
 • Fixed final bugs with UI element positioning - Resolved various interface positioning issues including:
 
 • Caret positioning elements
 
 • Title bar overlapping issues
 
 • Autocomplete animations
 
 • Shadow effects
 
 • Prevented welcome window from appearing when editor window already exists - Fixed window management logic to avoid duplicate welcome screens
 
 • Implemented text editing features - Added font size adjustment capabilities and theme switching functionality
 
 • Fixed caret positioning during text scrolling - Resolved issue where cursor would remain static while scrolling through text
 
 • Added context menu for personalization toggle and status in welcome view - Implemented right-click menu options and status indicators
 
 • Added model loading functionality to welcome view - Extended model loading capabilities to the initial welcome screen
 
   [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/cabaf21dcda5d831ba2284e75159914d2c84a4f5)
   And model development task
   
 • Fine-tuned model for instruction following - Additional training needed for better instruction adherence when editing text
 
 • Conducted an interpretability research on what's been going on with projector embeddings. Currently investigating the outcomes: added the Sinkhorn loss that dramatically improved convergence and finally got it off the ground our efforts.
   [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/6b04fef6b72aacf2a574030c8983898fec3dd240)
- **Polina**:Implemented local server llama-cpp to handle problem with asynchrony and model downloading multiple times which drastically increased memory usage. Now all models functionality is going through APIs and model is on the server. [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/5a3df3a3fbfabdc3fe3a585d6e2107d81e5b0289)
    Implemented LoRA functionality for autocomplete and created pipeline for LoRAs for other functions [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/0e03f681fa8ac38e7cddfff9be971ae06d08a9d0)
- **Maxim**: mplemented a module for dynamically calculating user history attention weights, inspired by the original work of LLMs + Persona-Plug = Personalized LLMs. It consists of two stages:
  
  1. Calculating the cosine similarity between the current user query and history messages based on TF-IDF vectorization, taking into account Russian and English stop words.
  2. Normalizing the attention weights to the range from 0.1 to 1.0, where the most similar messages receive a higher weight.
  Thus, the module allows adapting the model's behavior depending on the history content and implements soft attention to the personal context. [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/51fcd85ef7044bdb333144906a0fba6289c5a971)

  I developed a script to gather a dataset of posts from LiveJournal for specified users over the period from 2020 to 2024. The script extracts posts that meet a minimum length requirement and saves them into JSON files, with delays between requests to avoid being blocked. It also provides output on the progress, including the number of posts found and saved. [Commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/8986b6da9435673eea718ead449654e3f5d60d89)

## Plan for Next Week

- **Janna**:

  - Finalize the presentation draft.
  - Complete the landing page design in Framer, ensuring it is fully functional and ready to launch with a single button press.

- **Kira and Maxim**:

  - Work on fine-tuning the story generation feature, focusing on improving instruction-based training.
  - Complete implementing personalization features.

- **Polina**:

  - Complete integration of all systems.
  - Identify and resolve errors in the story generation functionality to ensure stable performance.

- **Vlad**:

  - Oversee and contribute to the training of personalization features, focusing on resolving challenges with adapters.
  - Trying to pack the app for the final release on Mac, for delivering it to final users.
  - Web-server for generating pass keys for access in the app and trying to make payment system.

- **Entire Team**:

  - Package the application into a production-ready state.
  - Conduct final testing on target user devices.
  - Implement and test the API key generation system for the paywall feature.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- Is in working condition (not fully free of bugs yet).
- Runs on the intended platform: macOS 15 via Xcode.
If you encounter any problems running the setup, feel free to contact us for assistance. We can also provide a video demonstrating the current state of the prototype upon request.
