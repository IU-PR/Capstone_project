---
title: "Week #3"
---

# Week #3

## Implemented MVP Features

During Week #3, the team made significant progress toward implementing core features of the **Killah Writing Companion** MVP, focusing on enhancing the text editor, integrating audio modality, and advancing machine learning capabilities. Below is a detailed list of implemented features and their associated user journeys, along with links to relevant pull requests or issues.

1. **Interactive List Support in Text Editor** (Vlad):
   - Added support for creating and managing lists (bulleted and numbered) within the macOS-native text editor.
   - Ensures seamless integration with the existing NSTextView-based editor, maintaining a caret-centric UI.
   - **User Journey**: As a novelist or journalist, I can now create structured lists within my drafts, improving document organization and readability while maintaining my writing flow.
   - **Relevant PR**: https://github.com/vladkalinichencko/Killah-Prototype/commit/b19c20ca4444a630d8787492645a563b149c873b

2. **Audio Modality Integration** (Polina):
   - Integrated audio input processing to enable voice dictation and command recognition.
   - Implemented embedding generation from audio inputs, allowing the application to convert spoken ideas into structured text.
   - Fixed token streaming issues to ensure smooth real-time text generation from audio inputs.
   - **User Journey**: As a journalist or content creator, I can dictate notes or ideas, and the application will convert them into polished, style-consistent text drafts, streamlining my workflow.
   - **Relevant PR** https://github.com/vladkalinichencko/Killah-Prototype/commit/5e728e5152dddf96125648c9b50817961da3e2a4

3. **LoRA Adapter Integration for Model Training** (Kira):
   - Added a LoRA (Low-Rank Adaptation) adapter to the model training and inference scripts, enhancing the personalization capabilities of the Gemma 3 4B model.
   - Ensured compatibility with the existing hierarchical LoRA architecture (r=64) for style preservation.
   - **User Journey**: As a fiction writer, I benefit from the model adapting to my unique writing style, ensuring text suggestions align with my established voice.
   - **Relevant PR/Notebook**: https://github.com/vladkalinichencko/Killah-Prototype/commit/387483a68ff27d78be43637a15563092ee4be9b6

4. **MLP Projector Training for Audio Processing** (Vlad, Maxim):
   - Trained an MLP (Multi-Layer Perceptron) projector specifically for audio processing, enabling the model to handle audio-to-text and audio understanding tasks.
   - Used datasets such as LibriSpeech, Common Voice, and Open STT for training.
   - **User Journey**: As a user relying on voice input, I can trust the application to accurately process and convert my spoken ideas into structured text.
   - **Relevant PR**: https://github.com/vladkalinichencko/Killah-Prototype/commit/a2fac512a0dc83f1ffcebcc3b46bf692c437bdc5

5. **User Stories and Market Analysis** (Janna):
   - Developed detailed user stories to refine the target audience and use cases.
   - Conducted extensive market research, analyzing direct competitors (e.g., Grammarly, ProWritingAid) and indirect competitors to validate the unique market position of Killah.
   - Identified key differentiators: style preservation, on-device processing for privacy, and voice-to-text workflow.
   - **User Journey**: As a PhD student or content creator, I can rely on Killah to provide personalized, style-consistent assistance without compromising my data privacy.
   - **Relevant Documentation**: https://disk.yandex.ru/d/x64yvKSf8DIJDQ
  
6. **Dataset with books** (Maxim):
   - Developed a scripts that collected a corpus of long literary texts to train a language model: connected and processed the institutional-books dataset, implemented filtering, saving books with a volume of more than 128,000 tokens and began developing scripts for parsing modern literature: blogs from LiveJournal, author Telegram channels and other high-quality sources.
   - **Relevant commit**: https://github.com/vladkalinichencko/Killah-Prototype/commit/14eb1dae260c38878dd0ea00106cdeff180785e7
https://github.com/vladkalinichencko/Killah-Prototype/commit/29613eae976f20f3e65102c19688f4e2432cdf81

## Demonstration of the Working MVP

The current MVP includes a functional macOS-native text editor with list support, audio input processing, and initial model personalization via LoRA adapters. Below are the planned deliverables to demonstrate the MVP : 
[video is here](https://disk.yandex.ru/d/x64yvKSf8DIJDQ) 

## ML

### Link to the Training Code: https://github.com/vladkalinichencko/Killah-Prototype/commit/a2fac512a0dc83f1ffcebcc3b46bf692c437bdc5

### Model Training Description
- **Data Used**:
  - **LibriSpeech, Common Voice, Open STT**: Audio datasets used for training the MLP projector to handle audio-to-text tasks. These datasets provide diverse speech samples for robust audio processing.
  - **Text Datasets**: Not explicitly mentioned for Week #3, but likely include user-provided text samples for style personalization (as per Week #1 scope).
- **Training Process**:
  - The MLP projector was trained using A100 GPUs (estimated 85-160 GPU-hours from Week #1).
  - **Improvements**:
    - **Normalization**: Applied proper loss normalization by dividing by gradient accumulation steps, with weight updates only after accumulation.
    - **Learning Rate Scheduling**: Used OneCycleLR for stable training.
    - **Activation Functions**: Incorporated Z-normalization and GELU for improved audio understanding.
    - **Model Architecture**: Increased projector parameters for better performance.
  - **Validation Enhancements**:
    - Added debug prints for 3-5 examples with detailed diagnostics.
    - Conducted error analysis to detect empty, redundant, or insufficient generation.
    - Tracked detailed statistics (e.g., word length, error types).
  - **Console Output Overhaul**:
    - Implemented `print_vanishing()` for intermediate metrics, debug examples, validation results, checkpoints, and graphs to keep the console clean.
    - Ensured the progress bar remains stable and readable, with only critical validation results and events persisting.
  - **Metrics Logging**:
    - Automatically logged all metrics to Weights & Biases (W&B) for real-time monitoring.
    - Targeted significant Word Error Rate (WER) reduction from ~3.0 to 0.2-0.5 (20-50% improvement).
    - Aimed for improved BLEU and ROUGE scores due to enhanced architecture.
  - LoRA fine-tuning was applied to the Gemma 3 4B base model using the Hugging Face Trainer API and Accelerate for efficient training.
- **Model Decision Parameters**:
  - The model uses a 3-layer LoRA architecture (r=64) to adapt the base Gemma 3 4B model for style preservation and audio processing.
  - PersonaPlugs runtime conditioning ensures personalized text generation based on user writing samples.
  - Audio processing relies on a Conformer-based encoder integrated with Apple AudioKit, with the MLP projector handling audio-to-text tasks.
- **Next Steps if WER Remains High**:
  - Fine-tune Gemma with LoRA by unfreezing specific layers.
  - Increase projector dimensionality (e.g., 4096 or 8192).
  - Add more layers (4-5) to the projector.
  - Introduce cross-attention mechanisms between audio and text.

### Links to Initial Model Artifacts
https://huggingface.co/google/gemma-3-4b-pt

https://huggingface.co/facebook/wav2vec2-base


## Internal Demo
### Notes from Internal Demo
Since the language model is in the training stage, our team focused on refining the interface. An internal demo was conducted among our ML specialists. In our plans for the next week, we have a user experience interviews.



## Weekly Commitments

### Individual Contribution of Each Participant
1. **Janna**:
   - Developed detailed user stories for fiction writers, journalists, and academic writers.
   - Added information into market research, analyzing direct (e.g., Grammarly) and indirect competitors to validate Killah’s unique position.
   - Updated design documentation with new user story insights.
   [Market Research and User Stories](https://disk.yandex.ru/d/x64yvKSf8DIJDQ)

2. **Maxim**:   
   - Collect a dataset with books, other good literature from the Internet, blogs: mainly lengths greater than 128,000 tokens
   - Trained the MLP projector for audio processing using LibriSpeech, Common Voice, and Open STT datasets.
   - Implemented training improvements (e.g., normalization, W&B logging, console output cleanup).
     [datasets](https://github.com/vladkalinichencko/Killah-Prototype/commit/29613eae976f20f3e65102c19688f4e2432cdf81)

3. **Kira**:
   - Integrated LoRA adapter into model training and inference scripts.
   - Updated Colab scripts for reproducibility and migrated them to the Git repository.
     

4. **Vlad**:
   - Trained the MLP projector for audio processing using LibriSpeech, Common Voice, and Open STT datasets.
   - Implemented list support (bulleted and numbered) in the NSTextView-based editor.
   - Ensured seamless integration with the existing toolbar and caret functionality.

6. **Polina**:
   - Integrated audio modality for voice input and embedding generation.
   - Fixed token streaming for real-time text generation from audio inputs.

## Plan for Next Week

### Development Goals for Week #4
1. **Adjust Caret Window Positioning**:
   - Implement functionality to move the text caret window away from the edges of the application window, improving usability and visual clarity.
2. **Collect Dataset for Instruction-Following in Audio Transcription**:
   - Gather a dataset tailored for training the model to follow specific instructions during audio transcription, enhancing command recognition accuracy.
3. **Collect Dataset of Long-Form Text**:
   - Compile a dataset of books, high-quality literature, and blogs from the internet, prioritizing texts longer than 128,000 tokens to support style adaptation for extended writing.
4. **Integrate Model with Projector and Adapter into Application**:
   - Embed the trained model, including the MLP projector and LoRA adapter, into the macOS application for seamless on-device processing.
5. **Add Sequential LoRA Adapters for Syntax**:
   - Incorporate multiple LoRA adapters in sequence within the model to improve syntactic accuracy and style consistency in generated text.
6. **Start conducting and UX interviews**:
   - Begin conducting user experience (UX) interviews to gather feedback on the Killah application, focusing on usability, feature relevance, and user needs to inform further design iterations.



### Success Metrics
- Caret window repositioning implemented with improved user feedback.
- Datasets for instruction-following and long-form text collected and pre-processed.
- Model with projector and adapter successfully integrated into the application.
- Sequential LoRA adapters implemented and validated for syntactic improvements.
- Stable performance on macOS 15 with <8GB memory footprint.

## Confirmation of the Code’s Operability

We confirm that the code in the main branch:
- Is in working condition (not fully free of bugs yet).
- Runs on the intended platform: macOS 15 via Xcode.

If you encounter any problems running the setup, feel free to contact us for assistance. We can also provide a video demonstrating the current state of the prototype upon request.
