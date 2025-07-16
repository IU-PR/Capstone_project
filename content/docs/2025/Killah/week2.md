---
title: "Week #2"
---
# **Week #2**

## Detailed Requirements Elaboration

In the second week, the team focused on refining the functional and technical requirements for implementing key components of the project. The main focus was on improving user interaction, integrating machine-learning models and data processing, and generating user stories for further market analysis.

### Interactive user interaction:
Developed requirements for a fully functional toolbar with all features, ensuring uninterrupted operation and seamless integration with the application’s frontend (Vlad).

Defined requirements for an interactive text caret to ensure smooth and intuitive interaction with the application. Parameters for caret behavior, including data input handling and visual feedback, were specified (Vlad).

Requirements for integrating the model with the projector and adapter into the application interface were clarified to ensure compatibility with the frontend and improve usability (Polina).

### Data processing and model support:
Requirements for loading and pre-processing of new datasets have been formulated, including data formats, volumes and cleaning methods. This will allow the project to scale to handle a variety of input data (Max).


Technical details for running models with projection support and LoRA (Low-Rank Adaptation), including hyperparameter tuning and performance optimization are worked out (Vlad).

### Visualization and monitoring:
Requirements for visualization of model training loess functions are defined to provide transparency of the training process and simplify debugging. Graphs should be interactive and exportable for analysis (Vlad, Kira).

### Code migration and infrastructure:
Clarified requirements for migrating code from Colab to a Git repository, including folder structure, documentation, and ensuring reproducibility of experiments (Kira).

### User and market requirements:
Based on market analysis and user stories, work has started on defining the target audience and key usage scenarios of the application. This includes the visual style of the interface and user expectations from the functionality (Janna).

### Prioritized backlog

*(Publicly accessible link OR screenshots OR table) of your prioritized backlog (Kanban board)*

[Project Backlog - Kanban Board](https://github.com/users/vladkalinichencko/projects/1/views/3)


## Requirements

### Application Requirements

During this week, we successfully implemented several key requirements for our application:

**Responsive Interface**: We developed a responsive and intuitive user interface that adapts to different screen sizes and provides smooth user interaction. This ensures accessibility across various devices and enhances user experience.

**macOS Compatibility**: The application has been specifically optimized for macOS platform, ensuring native performance and seamless integration with the operating system. This choice allows us to leverage macOS-specific features and provide the best possible performance on Apple devices.

**Local Model Integration**: We implemented local machine learning model support, allowing the application to run AI models directly on the user's device. This approach provides several advantages:
- Reduced latency for real-time processing
- Independence from internet connectivity
- Better performance for local computations

These requirements form the foundation for our application's core functionality and ensure we meet our users' needs for privacy, performance, and usability.


## Project specific progress

### Frontend

- Implemented interactive text caret functionality (by Vlad).
- Developed a fully functional toolbar with all features, ensuring stable and uninterrupted operation (by Vlad).
- Integrated model with projector and adapter into the application (by Polina).

### Backend

- Developed code for loading and processing new datasets (by Max).
- Implemented code for running models with various features, including projections and LoRAs (by Vlad).
- Transferred Colab code to the Git repository (by Kira).

### Design/Market Research

- Prepared report, design screenshots, user stories, and market research analysis (by Janna).

### Machine Learning

- Created visualizations for training loss functions (by Vlad and Kira).

## Weekly commitments

### Individual contribution of each participant

- **Vlad**: Developed interactive text caret code, implemented a fully functional toolbar with uninterrupted operation, created model running code with projections and LoRAs, and generated training loss function visualizations.
- **Kira**: Generated training loss function visualizations and transferred Colab code to the Git repository.
- **Max**: Wrote code for loading and processing new datasets.
- **Polina**: Integrated the model with projector and adapter into the application.
- **Janna**: Compiled the report, provided design screenshots, wrote user stories, and conducted market research.

  All materials showing our progress are stored on disk. Screenshots are sorted into folders for each team member.
  
  [Project Materials - Yandex Disk](https://disk.yandex.ru/d/gOtDVatB0l5FQw)

### Evidence of Individual Contributions

All team members have provided evidence of their work through various deliverables:

- **Code commits and pull requests**: 
  - [Vlad's smart caret](https://github.com/vladkalinichencko/Killah-Prototype/commit/2f4a7ea70bf807affaeb9adfdab0ecc86b3db08f)
  - [Polina's model integration](https://github.com/vladkalinichencko/Killah-Prototype/commit/0363f49c1cedb632d74ac1a899be2bbedfce8fdf)
  - [Max's dataset processing](https://github.com/vladkalinichencko/Killah-Prototype/commit/200a6be7e136c6567f5da82b069abe1fddfea44d)
  - [Kira's Colab migration](https://colab.research.google.com/drive/1k1pF6HXKqJNHN7tRNnDmQZj6H9ndsLJE?authuser=1#scrollTo=1nTnnTy8Gr7j)
- **Design mockups and screenshots**: [Here](https://disk.yandex.ru/d/gOtDVatB0l5FQw)
- **Research documentation**: [Market research started by Janna](https://disk.yandex.ru/d/gOtDVatB0l5FQw)
- **Technical documentation**: [Comprehensive technical documentation](https://github.com/vladkalinichencko/Killah-Prototype/tree/master/Documents)

Detailed evidence and work samples are available in our shared repository and documentation system.


## Plan for Next Week

### Development Goals for Week #3

For the upcoming week, our team has identified several key objectives to advance the project:

**Audio Processing Integration**: Implement audio input and processing capabilities to expand the application's functionality beyond text-based interactions. This will enable users to interact with the application using voice commands and audio content.

**On-Device Model Enhancement**: Continue development of local machine learning models that can efficiently run on user devices, ensuring optimal performance and privacy.

**Interactive Text Caret Refinement**: Complete the implementation of a fully functional interactive text caret that provides smooth and responsive text editing experience, as well as complex UI for audio input.

**Full-Featured Text Editor**: Complete a comprehensive text editor with advanced features including syntax highlighting, font alignment, and streamed auto-completion.

**MLP Projector Training**: Begin training the first component of our model architecture - the MLP (Multi-Layer Perceptron) projector specifically designed for audio processing. This will serve as the foundation for audio-to-text and audio understanding capabilities.

### Success Metrics

- Functional audio input system
- Trained and validated MLP projector model
- Responsive text caret with real-time feedback
- Complete text editor with core features
- Performance benchmarks for on-device model execution

## Confirmation of the code's operability

We confirm that the code in the main branch:

- Can be run (Not fully free of bugs yet).
- Runs on the intended platform: macOS 15 via Xcode.

If you encounter any problems running the setup, feel free to contact us and get help. Or maybe we can provide a video with how the current state of the prototype is working.
