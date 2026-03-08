---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

### Session 1: Arthur's Feedback
**User Reviews:**
- **Interface:** The interface is clear and easy to use, Navigation is intuitive. Keyboard shortcuts for text formatting significantly speed up workflows.
- **Context Understanding:** The model generally captures the context of queries, but sometimes it needs to be rephrase or clarified to provide more accurate answers.
- **Performance:** The main drawback is the delay in generating answers, which disrupts the workflow, especially when performing quick tasks. Faster response times would greatly improve the work.

### Session 2: Misha's Feedback
**User Review:**
- **Interface:** The interface is intuitive and well-designed, navigation is smooth. The clear structure helps maintain focus while completing tasks.
- **Performance:** The response rate is slow, which is annoying and reduces productivity, especially when quick answers are needed.
- **Response Consistency:** The model sometimes produces random or inconsistent results at the beginning of the interaction, so it takes a few more tries to get relevant answers.
### Session 3: Diana's Feedback
**User Feedback:**
- **Interface:** The interface is attractive and easy to use. The tools are well laid out
- **Context Understanding:** The model handles general queries well, but sometimes misinterprets complex or domain-specific queries, resulting in less accurate results
- **Voice Input Usability:** Using the cursor to dictate felt unintuitive, making it difficult to use voice input effectively compared to other methods.

### Analyze


### Key Points from User Feedback

1. **Positive aspects:**
- All users appreciated the intuitive and clear interface, which supports efficient navigation and task execution in various use cases.
- Keyboard shortcuts (noted by Arthur) improve productivity
- The model generally handles simple queries efficiently

2. **Problems and suggestions:**
- **Response speed (Arthur, Misha):** Slow response times are a persistent issue that significantly reduces productivity. This can be off-putting to potential customers who are used to working at a fast pace
- **Context accuracy (Arthur, Diana):** The model struggles to handle complex, highly specialized, or domain-specific queries. This often requires rephrasing or else the model returns less relevant results.
- **Response consistency (Misha):** Random or inconsistent results at the beginning of the interaction irritate users and undermine trust in the reliability of the system at the very beginning of the user flow

- **Ease of use of voice input (Diana):** The dictation function, especially the use of the cursor, seems unintuitive.

  
### Issues and Prioritization

1. **Issue #1: Slow Response Speed**
   - **Priority:** High
   - **Description:** Delays in generating responses hinder productivity, especially for users with fast-paced workflows.
   - **Recommendation:** Optimize model performance through server-side improvements or more efficient processing algorithms to reduce latency.

2. **Issue #2: Inaccurate Context Understanding**
   - **Priority:** High
   - **Description:** The model struggles with nuanced or domain-specific queries, leading to inaccurate or generic responses that require user rephrasing.
   - **Recommendation:** Enhance natural language processing capabilities to improve context comprehension and response relevance.

3. **Issue #3: Inconsistent Response Generation**
   - **Priority:** Medium
   - **Description:** Random or inconsistent outputs at the start of interactions reduce the system’s reliability and frustrate users.
   - **Recommendation:** Implement mechanisms to stabilize initial responses, such as improved context retention or pre-processing checks.

4. **Issue #4: Unintuitive Voice Input**
   - **Priority:** Low
   - **Description:** The caret-based dictation feature feels clunky and unintuitive.
   - **Recommendation:** When using for the first time, add a tutorial to help you understand the interface


## Iteration & Refinement

### Implemented features based on feedback

Based on earlier user feedback, we improved the interactive text caret by making its text more distinct from surrounding content for better visibility. We also restored functional text streaming to ensure smoother and more responsive output, addressing previous concerns about delays. [Commit: 7fae6f5](https://github.com/vladkalinichencko/Killah-Prototype/commit/7fae6f5082baa4ed48cc9a884069050d87a1bd2c), [Commit: a264daf](https://github.com/vladkalinichencko/Killah-Prototype/commit/a264daf6943add4c9f6e3565bfb957858d221898)

### Performance & Stability

Since our performance issues are tied to the models, we evaluate them based on subjective feel. After training, Kira tests several model completions for our model (named LIL Pushkin), compares them to previous outputs, and notes noticeable improvements in quality and coherence. We tried using ChatGPT to automatically assess the model’s writing quality, but it struggles to accurately evaluate what makes text good, making it an unreliable method for automated checks. As this would be the only feasible way to automate evaluation, we currently rely on vibe-based assessments.

### Documentation

Our project includes two key documentation files: `llm.md` and `app.md`. These files provide comprehensive details for other developers, covering the model’s architecture, training process, and application setup, ensuring smooth onboarding and collaboration.

### ML Model Refinement

We’re currently fine-tuning and further training our model, monitoring writing metrics and vibe-based metrics. During training, we track the loss. We’re working on automated text evaluation metrics, including mathematical ones outlined in `llm.md`. However, automatic text evaluation using language models hasn’t been effective, as they struggle to identify what makes text good, even for human-written content. For now, we rely on subjective vibe checks to assess performance.

## Weekly commitments

### Individual contribution of each participant

- **Janna**:
  - Developed the structure and draft for the landing page, including initial versions of key selling texts and headlines. [Figma](https://www.figma.com/design/0JZd4kLqI8uzJoKe3oqEMd/Untitled?node-id=0-1&t=hxW62JbtFokjK1YS-1)
  - Conducted three user feedback sessions and performed a user review to gather insights on the application’s usability. 
  - Collected information from the team about the week’s progress and compiled this report.
- **Polina**:
  - Implemented caching for autocomplete and modified prompt generation logic to use only text before the cursor. [Commit: 1f3c198](https://github.com/vladkalinichencko/Killah-Prototype/commit/1f3c198367ebd3fcd9eb854c75a5462ca9e0b1b5)
  - Fixed bugs in streaming functionality. [Commit: a8330b0](https://github.com/vladkalinichencko/Killah-Prototype/commit/a8330b0982375b4a36eab14a8794a20cbb3a53a7)
  - Added UI arrows for temperature adjustment and implemented min-p sampling. [Commit: 1bb73aa](https://github.com/vladkalinichencko/Killah-Prototype/commit/1bb73aa0445ffaca3dc18d34f0b57671e2d3e6e1)
- **Max**:
  - Cleaned and normalized a text corpus for training, removing visual and technical artifacts. [Commits: 8f2fe4a](https://github.com/vladkalinichencko/Killah-Prototype/commit/8f2fe4ad08b363115a2e3c0533667e3ae629722f), [4155bfc](https://github.com/vladkalinichencko/Killah-Prototype/commit/4155bfca734aadaf970250daf40e58a1794c7a34), [8986b6d](https://github.com/vladkalinichencko/Killah-Prototype/commit/8986b6da9435673eea718ead449654e3f5d60d89), [7edc521](https://github.com/vladkalinichencko/Killah-Prototype/commit/7edc5217c0c1e7ec588aea329fd421c80dc58a3b), [ef458e4](https://github.com/vladkalinichencko/Killah-Prototype/commit/ef458e463488e5f4fd13e8584d96ed2e6b736464)
  - Created a "Torn Context" dataset with variable-length fragments to simulate real-time typing. [Commits: b015f5a](https://github.com/vladkalinichencko/Killah-Prototype/commit/b015f5aae7694f71e5470c2dc32251056d93e4ef), [e463d95](https://github.com/vladkalinichencko/Killah-Prototype/commit/e463d95934c6f6f6eff5d65668bf7c8f26e3d0bc), [8409194](https://github.com/vladkalinichencko/Killah-Prototype/commit/84091949ca479bd705e02347573234f328615f25)
- **Kira**:
  - Completed the CLM script for training a Gemma LoRA-adapter with logging, checkpoint saving, dataset cleaning, and speed checks. [Commit: 673316c](https://github.com/vladkalinichencko/Killah-Prototype/commit/673316ca46479eb0f86f293cd02a8a63106e580c)
  - Modified the script for the "Torn Context" method, achieving a validation loss reduction from 2.3 to 0.4. [Commit: 044d9a0](https://github.com/vladkalinichencko/Killah-Prototype/commit/044d9a0f3c345b8611304cd51713b1ff76e10c3e)
  - Loaded saved model weights and conducted manual generation testing, confirming meaningful and grammatically correct outputs. [Commit: cab9fa1](https://github.com/vladkalinichencko/Killah-Prototype/commit/cab9fa1dafd152170e57b7355aa66611a84987cf)
- **Vlad**:
  - Delivered the true token streaming – previously it was imitated, resulting in a larger delays before the models outputs its answer. [Commit: a264daf](https://github.com/vladkalinichencko/Killah-Prototype/commit/a264daf6943add4c9f6e3565bfb957858d221898)
  - Bringed the real complex animation for the newly arriving tokens. This little change required digging into the lowest of abstraction layers of macOS developement kit and we will work further to polish it more and make the app ready for their first customers. [Commit: 7fae6f5](https://github.com/vladkalinichencko/Killah-Prototype/commit/7fae6f5082baa4ed48cc9a884069050d87a1bd2c)
  - Added the whole pipeline for downloading the foundation models from the cloud, so the users now get a sleek new UI that prompts them to download the model. We handle downloading directly from the Hagging Face repository, resulting in less work to integrate handcrafted APIs. [Commit: 6bdf1a2](https://github.com/vladkalinichencko/Killah-Prototype/commit/6bdf1a217e2f5c92e8519bae39a7d261cda65233)
  - Found instruction following datasets for textual editing, both in English and multilingual. The needed datasets specifically for Russian were not found, however our hopes are that the model would emergently handle Russian instructions as well.
  - Completed a series of failed experiments to integrate audio modality into the model: Q-Former, SLAM-ASR, Llama-AVSR, Diversity-loss, CosSim-regularization, directly replicating experiments, and combining different parts. Right now we are setting back to the convensional ASR system, Whisper to be precise, however we plan to continue experiments when the model becomes at the later stage of development, gaining instruction following abilities. [Commit: f093a8a](https://github.com/vladkalinichencko/Killah-Prototype/commit/f093a8ad62b4e7a717ef8d2d08b7617a4bf9d9c5)

## Plan for Next Week

Polina:
- Development of an audio recognition system in GGUF
- Implementation of KV cache
- Implementation of GGUF streaming

Janna:
- Development of landing page design
- Creation of materials for market communication in accordance with market research
  
Max:
- Creation of a dataset from blogs
- Training of models
  
Kira:
- Work on the personalization script
-  Training of models
-   valuation of the quality of models
  
Vlad:
- Development of a document viewing window
- Training of the model to follow instructions

## Confirmation of the code's operability

We confirm that the code in the main branch:
- Is in working condition (not fully free of bugs yet).
- Runs on the intended platform: macOS 15 via Xcode.
- Includes a CI/CD script that automates project setup.
If you encounter any problems running the setup, feel free to contact us for assistance. We can also provide a video demonstrating the current state of the prototype upon request.
