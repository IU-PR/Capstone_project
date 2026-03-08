---
title: "Week #4"
---

# **Week #4**

## Testing and QA

The team relies on manual testing to validate the application’s functionality, which has proven sufficient for the current feature set. Tests are conducted on macOS 15 devices using Xcode, covering the quantized model integration, refactored LLM code, and UI components such as the text editor and settings window. Manual testing ensures that core features, including model loading from Hugging Face and text autocomplete animations, work as expected. For the audio modality, exploratory testing was performed to diagnose training issues, with loss visualizations used to analyze mode collapse. This approach, while labor-intensive, meets the project’s needs at this prototype stage.

### Evidence of test execution

*Screenshots of manual UI testing results and loss visualizations for the audio modality are stored in the project’s [cloud folder](https://disk.yandex.ru/d/kFXGfXGUAn55mg). No automated test reports are available due to the reliance on manual testing.*


## CI/CD

Setting up a CI/CD pipeline has been challenging due to the absence of Xcode Cloud, which is a subscription-based service, and the complexity of the project’s custom environment. The application requires a non-sandboxed setup with integrated Python processes for model execution, making it difficult to configure automated builds in tools like GitHub Actions. Currently, the team manually builds and tests the application on macOS 15 devices before each commit to ensure stability. Efforts to establish a GitHub Actions workflow are ongoing, but the custom environment’s unique requirements (e.g., disabled sandbox, Python dependencies) have delayed progress.

### Links to CI/CD configuration files

*No CI/CD configuration files are available yet, as the pipeline setup is still in progress.*

## Deployment

### Staging

The staging environment consists of local macOS 15 devices running the application via Xcode. Before each commit, the team deploys the application on physical devices to verify functionality in the custom environment (non-sandboxed, with Python processes). This process ensures that features like the quantized model, refactored LLM code, and UI improvements (e.g., settings window, text editor) operate correctly. No external staging server is used, as the focus remains on local testing to accommodate the project’s unique setup.

### Production

*Production deployment is currently being implemented by Vlad. The process is in progress, focusing on setting up a stable environment for deploying the application with the custom non-sandboxed setup and Python processes. Details on the production environment, including potential public domain and VDS setup, will be provided in future reports as the implementation progresses.*

## Vibe Check

The team made significant progress in enhancing the application’s functionality and advancing the AI component, though some challenges were encountered. Polina successfully quantized the model and refactored the LLM code, improving maintainability. Vlad faced difficulties with the audio modality training, experiencing mode collapse, which has impacted his morale, and he is exploring a new approach to address this. He also worked on application improvements and production deployment, though some tasks are still in progress. Kira resolved model format errors, improved dataset preprocessing, and implemented a custom Trainer for LoRA adapters. Max implemented a demo script for Persona-Plugs and enhanced the dataset download script for scalability. Janna conducted a UX interview briefing regarding the interactive text caret, identifying that added text appears too noisy over existing text; a full UX interview is postponed until the model is better trained to gather initial feedback from the target audience. The team bonded over a trip to karaoke for Vlad’s birthday, which strengthened team dynamics and boosted morale. Despite Vlad’s challenges with model training, the team remains motivated, acknowledges the need to address technical hurdles, particularly in AI training and UI refinement, and plans to coordinate closely to ensure smooth integration of new features. Everyone’s contributions were discussed, and the team is committed to supporting each other to resolve open issues.

## Weekly commitments

### Individual contribution of each participant

- **Polina**:
  - Added a quantized model (8-bit quantization) to the application. [Commit: 88834ce](https://github.com/vladkalinichencko/Killah-Prototype/commit/88834ce6517ed24588b395803f02cdeab2a002da)
  - Refactored LLM code to improve usability and maintainability for future development. [Commit: bc4ef06](https://github.com/vladkalinichencko/Killah-Prototype/commit/bc4ef0602218b5301f8af717bc1f6cddc5a12b0d)
- **Vlad**:
  - Worked on application improvements, including a settings window, a more stable and bug-free text editor, text autocomplete animation, and model loading from Hugging Face directly in the interface (work in progress, commit pending). [commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/8d9fd11808224ce82875bb7916fc5f2a11b24ff9)
  - Continued training the audio modality for the AI model, encountering issues with early loss convergence and mode collapse. Replicated the approach from “An Embarrassingly Simple Approach for LLM with Strong ASR Capacity” but faced the same issue. Currently implementing and training a method from “Bridging the Modality Gap: Softly Discretizing Audio Representation for LLM-based Automatic Speech Recognition” to address modality convergence (work in progress, commit pending). Visualizations of training attempts stored in a cloud folder. [commit](https://github.com/vladkalinichencko/Killah-Prototype/commit/629eb566128a78d4b35a03c1d51e8022016c7a9e)
- **Kira**:
  - Fixed errors with the model format, cleaned the dataset from book texts, split it into sentences, and tokenized it with overlap. [Commit: e037ab0](https://github.com/vladkalinichencko/Killah-Prototype/commit/e037ab0734134b6aa40cb624b31f17cb7f70b7c1)
  - Added several LoRA adapters in sequence, applying a previously trained LoRA adapter and adding a new one for additional training. Implemented a custom Trainer with logging and protection from NaNs. [Commit: 58c0b2c](https://github.com/vladkalinichencko/Killah-Prototype/commit/58c0b2c7ab8a9a0cfcfb76cdae1cd098c4d1ac4e)
- **Max**:
  - Implemented a demo script for Persona-Plugs based on the article, processing the dataset with half used for personalization context and the other half for training on continuations. [Commit: d746ea0](https://github.com/vladkalinichencko/Killah-Prototype/commit/d746ea0335a4f62ca4ae061e8b9e18cdf8610558)
  - Modified the LiveJournal dataset download script to collect a dataset of a specified size (minimum 10 GB). [Commit: 8852564](https://github.com/vladkalinichencko/Killah-Prototype/commit/8852564df825a964ff43718e25e9338071eca419)
- **Janna**:
  - Conducted analysis and developed a strategy for marketing communications to support the project’s positioning and user engagement. [strategy for marketing communications](https://disk.yandex.ru/d/kFXGfXGUAn55mg)
  - Conducted a UX interview briefing for the interactive text caret, identifying that added text appears too noisy over existing text. Planned a full UX interview once the model is better trained to gather initial feedback from the target audience.
  - Looked for a target audience ready to conduct UX interviews

  

## Plan for Next Week

- Train an adapter for the audio modality (final attempt).
- Train an adapter for text continuation.
- Implement a document preview window.
- Develop a script for personalization in the training code.
- Create a landing page, starting with prototypes and followed by implementation.
- Finalize audio recognition integration into the application, using uninitialized or early checkpoints for the same architecture currently being trained.

## Confirmation of the Code’s Operability

We confirm that the code in the main branch:
- Is in working condition (not fully free of bugs yet).
- Runs on the intended platform: macOS 15 via Xcode.
If you encounter any problems running the setup, feel free to contact us for assistance. We can also provide a video demonstrating the current state of the prototype upon request.
