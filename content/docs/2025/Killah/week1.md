---
title: "Week #1"
---

# Week #1

## Project description

### Project name: Killah 

**Code repository**: https://github.com/vladkalinichencko/Killah-Prototype/

Killah - is an AI writing companion that helps people start, continue writing, and form their ideas using a responsive macOS app with a custom post-trained on-device large language model. Our solution addresses three key problems in current writing tools:

1. **Creative Block**: Helps overcome writer's block with style-consistent suggestions
2. **Voice-to-Workflow**: Enables seamless transition from voice dictation to polished text
3. **Style Preservation**: Maintains the author's unique voice through personalized adaptation

Technical foundation:
- Core model: Google Gemma 3 4B with Low-Rank Adaptation (LoRA)
- On-device processing for privacy (8GB memory requirement)
- Hierarchical adaptation layers for style preservation
- Voice integration via Conformer-based audio processing


### **Team Members**

| Team Member | Telegram Alias | Email Address | Track | Responsibilities |
|------------|---------------|--------------|-------|------------------|
| [Janna Ivanova] | [@i_jeannee] | [j.ivanova@innopolis.university] | Design | UX/UI design, report maker, manager |
| [Polina Korobeinikova] | [@poinkaa] | [p.korobeinikova@innopolis.university] | ML |Swift developer for LLM / ML Lead integration |
| [Vlad Kalinichenko] | [@vladotpad] | [v.kalinichenko@innopolis.university] | Fullstack| UX/UI,LLM Algorithm Lead / Swift Architect |
| [Kira Maslennikova] | [@NECHEBURASHKA] | [k.maslennikova@innopolis.university] | ML | ML engineer|
| [Maksim Menshikh] | [@okay1pullup] | [m.menshikh@innopolis.university] | ML | ML Engineer (data & learning)|

## Brainstorming

### Ideas during brainstorming

1. **Selected Concept**: Killah Writing Companion
   - Key differentiator: Style-consistent assistance (not content replacement)
   - Technical innovation: personalized, multimodal adaptation of on-device models
   - UX innovation: Voice-driven writing workflow, predictive text continuation

2. Alternative Concepts:
   - Technical documentation generator - AI-powered tool that automatically creates and maintains API docs from code comments with version-synced accuracy.
   - Academic writing assistant - Specialized editor enforcing citation standards and academic style while preventing plagiarism in research papers.
   - Social media content creator - Platform-specific post generator adapting tone/length to each network while maintaining brand voice consistency.

### Brief market research / problem validation


In the process of writing posts in the telegram channel, we have encountered the problem that neural networks cannot provide quality assistance to writers of this kind. Chat gpt and other similar neural networks completely invent the text for you, and if they edit yours, the result of their work is completely different from your writing style most often. When trying to use such technologies, you may also face the problem of AI slop.  In his essay “How to Get Startup Ideas”, Paul Graham recommends that startups create products that solve their own problems, which is what we decided to follow


## Unique market position

by addressing the fundamental weaknesses of AI tools from frontier labs (harm from RLHF and over-reliance on user preference and safety that reduces creativity and uniqueness) we're taking a promising product-market fit


## Basic requirements

### Target users and their primary needs

**Primary users:**
- Fiction writers (style preservation)
- Journalists (fast drafting)
- Academic writers (idea formulation)
- Content creators (voice-first workflow)
  
**Core needs:**
1. Overcoming initial writing resistance
2. Maintaining consistent voice across documents
3. Converting spoken ideas to structured text
4. Privacy-focused writing environment

### User stories

1. "As a novelist, I want the AI to continue my draft in my established style so I maintain voice consistency"
2. "As a journalist, I need to dictate notes and get properly structured drafts"
3. "As a PhD student, I want help reformulating complex ideas without losing academic tone"

### Initial scope

**MVP Features:**
- Intelligent text continuation (style-adaptive)
- Voice dictation with command recognition
- Document-based personalization (PersonaPlugs)
- macOS-native editor with caret-centric UI
- Export to .rtf, .txt

**Technical Scope:**
- Gemma 3 4B base model
- 3-layer LoRA architecture (style/audio/task)
- <8GB memory footprint
- Swift/SwiftUI/AppKit implementation

## Tech-stack

**Core components:**
1. **Model Architecture**:
   - Base: Google Gemma 3 4B
   - Adaptation: Hierarchical LoRA (r=64)
   - Personalization: PersonaPlugs runtime conditioning
   - Runtime: separate Python process with Hugging Face Transformers, Pytorch and Apple MLX in the future

2. **Application Layer**:
   - Platform: macOS (SwiftUI + AppKit)
   - Audio: Apple AudioKit + Audio encoder
   - Storage: SwiftData for version history

3. **Training Infrastructure**:
   - 85-160 A100 GPU-hours estimated
   - Datasets: LibriSpeech, Common Voice, Open STT
   - Training: LoRA fine-tuning with Accelerate and Hugging Face Trainer API

## Weekly commitments

### Individual contribution of each participant

1. [Janna]: Record and assign tasks for the week in a common space. Write a report. Create a design for the main screen of the application, including the text editor and toolbar. Start iterating on logo design.
   ![editor window](https://raw.githubusercontent.com/vladkalinichencko/Killah-Prototype/master/Documents/images/editor-window-overview.png)
2. [Polina]: Create a script to run the base model (Gemma 3 4B) for a “common sense” check, implement running a pre-trained language model (Gemma) through a Python script.

   Commits:
   - https://github.com/vladkalinichencko/Killah-Prototype/commit/6d14b3d666d7d188c80a8e29d1cdce2977d749f9
   - https://github.com/vladkalinichencko/Killah-Prototype/commit/ee3b8fc56d2d7cf7e2774da489a2fc5f5d343f05
   ![first week progress](https://raw.githubusercontent.com/vladkalinichencko/Killah-Prototype/master/Documents/images/First%20week%20progress.jpg)

3. [Vlad]: Create an Xcode project using Swift/SwiftUI/AppKit, implement the main application screen with a full text editor based on NSTextView. Add a toolbar with formatting features.

   Commits:
   - https://github.com/vladkalinichencko/Killah-Prototype/commit/edf785026cc31d308114ecc4fcea35a32d5febfb
   - https://github.com/vladkalinichencko/Killah-Prototype/commit/5237c1b4ba38bc2dc4e9f7b1e668f66faf1a347a
   
4. [Maxim]: Prepare audio datasets (LibriSpeech, Common Voice, Open STT)

   Commits:
   - https://github.com/vladkalinichencko/Killah-Prototype/commit/0de8a68762d97e3d299a9f21aa035687d34d5ffb

   - https://github.com/vladkalinichencko/Killah-Prototype/commit/200a6be7e136c6567f5da82b069abe1fddfea44d
   
5. [Kira]: Write scripts to download and process datasets.

   Contribution:
    - https://colab.research.google.com/drive/1IP1t4tISERn_5bHdbOHRdCBOTNQGVBeP?usp=sharing
   

## Confirmation of the code's operability

We confirm that the code in the main branch:

 * Can be run (Not fully free of bugs yet).
 * Runs on the intended platform: macOS 15 via Xcode.

If you encounter any problems running the setup, feel free to contact us and get help. Or maybe we can provide a video with how the current state of the prototype is working. 
