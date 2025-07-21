---
title: "Week 2"
---

# Week 2 Progress Report

## Executive Summary

This week marked significant progress across all project components. We successfully established the foundational architecture for our tire analysis system, with substantial advances in machine learning model development, backend API implementation, and user interface design. The team has demonstrated strong collaboration and technical execution, setting a solid foundation for the upcoming development phases.

## Requirements Analysis

### User Stories and Acceptance Criteria

Our project addresses three core user needs through carefully defined acceptance criteria:

#### 1. Tire Brand and Model Detection
**User Story:** As a user, I want to upload a photo of my tire so that the system identifies its brand and key specifications.

**Acceptance Criteria:**
- System outputs brand name and size specification (e.g., "215/65 R16")
- Achieves accuracy above 90% for clear, well-lit photographs
- Gracefully handles unrecognized brands with appropriate user feedback

#### 2. Tread Depth Measurement
**User Story:** As a user, I want to receive accurate tread depth measurements from my tire photos to assess wear condition.

**Acceptance Criteria:**
- Mean Absolute Error (MAE) must not exceed 1mm
- Results displayed with 2 decimal place precision
- System provides warnings for poor image quality

#### 3. Spike Condition Assessment
**User Story:** As a user, I want to know the condition of my tire spikes to understand wear patterns.

**Acceptance Criteria:**
- Combined false positive and false negative rate below 10
- Detects various spike conditions: worn, missing, loose, and re-nailed
- Provides clear count of good versus damaged spikes

### Performance Benchmarks

| Feature | Output Format | Performance Target |
|---------|---------------|-------------------|
| Tread Depth Estimation | Numeric value (mm), 2 decimal places | MAE ≤ 1mm |
| Spike Analysis | Count of good/bad spikes | FP + FN ≤ 10 |
| Brand Detection | Brand name and size string | ≥90% accuracy |

## Technical Implementation Progress

### Backend Development

The FastAPI backend has been successfully scaffolded with a well-structured architecture:

- **API Endpoints:** Two primary endpoints implemented (`/analyze/tread`, `/analyze/brand`)
- **Containerization:** Complete Docker setup with proper service orchestration
- **Security:** Bearer token authentication implemented across all endpoints
- **Integration Ready:** Backend prepared for ML model integration and Telegram bot connectivity

The API follows RESTful principles with proper error handling for invalid tokens (401) and malformed images (400).

### Frontend Development (Telegram Bot)

The Telegram bot implementation has progressed beyond initial prototypes:

- **User Flow:** Complete conversation handler with state management
- **User Experience:** Intuitive menu system with fallback mechanisms
- **Integration Status:** Ready for backend API connection

The bot supports two main workflows: tire brand identification and tread depth analysis, with proper error handling and user feedback loops.

### Machine Learning Pipeline

#### Tread Depth Estimation Model
We've implemented a comprehensive regression model using CNN architecture:

- **Architecture:** Multiple backbone options including Swin Transformer, EfficientNet-B7, Vision Transformer, DenseNet-201, and ConvNeXt
- **Training:** Custom PyTorch Dataset with proper data loading and augmentation
- **Metrics:** MSE loss function with MAE tracking for performance evaluation
- **Status:** Initial training completed with promising results

#### Spike Quality Detection
Binary classification model for spike condition assessment:

- **Model Type:** CNN-based classifier for good vs. bad spike detection
- **Loss Function:** CrossEntropy with class-wise accuracy metrics
- **Validation:** Comprehensive testing workflow implemented

#### Brand Recognition System
OCR-based approach for tire sidewall text extraction:

- **Preprocessing:** Image enhancement pipeline for sidewall flattening
- **Status:** Image processing methods validated, model integration pending

### Dataset Development

Our dataset has grown significantly through systematic annotation:

- **Size:** Approximately 700 annotated images, 400 with spikes analysis
- **Annotation Quality:** Manual inspection for tread depth and spike condition
- **Diversity:** Real-world conditions with variable lighting and angles
- **Structure:** Organized folder structure with CSV metadata

## User Experience Design

### Conversation Flow

The user journey begins with a welcoming interface that presents two primary options:

**Path 1: Tire Brand and Model Detection**
1. User selects "Tire Brand and Model" option
2. System prompts for sidewall photo upload
3. Image validation checks (size, format, quality)
4. Processing with user feedback
5. Results display with confirmation options
6. Optional manual correction with feedback collection

**Path 2: Tread Depth Analysis**
1. User selects "Tread Depth" option
2. System requests tread photo with visibility guidelines
3. Image validation and processing
4. Results showing depth measurement and spike count
5. Confirmation or manual input options
6. Feedback collection for model improvement

### Technical Implementation Details

#### Telegram Bot Architecture
- **Framework:** python-telegram-bot with ConversationHandler
- **States:** MENU, SIDE_PHOTO, SIDE_RESULT, SIDE_CUSTOM, TREAD_PHOTO, TREAD_RESULT, TREAD_CUSTOM
- **Commands:** /start for main menu, /cancel for conversation reset
- **Features:** Inline keyboards, image processing, text input handling

#### API Specification
**Authentication:** Bearer token required for all endpoints
**Request Format:** JSON with base64-encoded image
**Endpoints:**
- `/api/v1/analyze_thread` - Tread depth and spike analysis
- `/api/v1/identify_tire` - Brand and model detection

## Machine Learning Development

### Training Infrastructure

Our training notebook provides a complete ML pipeline for tread depth estimation:

**Data Management:**
- CSV-based metadata with image paths and labels
- Custom ThreadDataset class for PyTorch integration
- 80/20 train-validation split with proper randomization

**Model Architecture:**
- Multiple pre-trained backbone options
- Regression head for depth estimation
- Configurable hyperparameters and optimization

**Training Process:**
- Mini-batch processing with DataLoader
- Real-time progress tracking
- Comprehensive logging and visualization
- Model checkpointing and evaluation

**Evaluation Framework:**
- MAE-based performance assessment
- Prediction vs. ground truth analysis
- Model persistence for deployment

## Team Contributions

| Team Member | Primary Contributions | Deliverables |
|-------------|----------------------|--------------|
| Nikita Menshikov | Project documentation and user flow design | Comprehensive report and [backlog](https://github.com/orgs/IU-Capstone-Project-2025/projects/9/views/1), setup [labelling](https://github.com/NikitaMensh/IU_Capstone_project_2025/blob/main/photo_2025-06-17_10-52-36.jpg) [environment](https://github.com/NikitaMensh/IU_Capstone_project_2025/blob/main/photo_2025-06-17_10-52-37.jpg) |
| Nikita Zagainov | Machine learning model development | Training notebook and model implementations [[notebook](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/main/ML/notebooks/train.ipynb)] |
| Vladislav Strelkov | Infrastructure and deployment | Docker environment and service orchestration, tire annotation tool [[annotation tool](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/ec520dcdb5376281db28b381b7304d03cb107230)] [[Docker setup](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/c894595c8928c915249d5a11dc25195ba1534777)] [[docker-compose](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/d34838a54e748eed72ff9adee51dd193c6f2c974)] |
| Sergey Aitov | Data annotation and API development | Labeled dataset (350 images collected) and backend scaffolding [[dummy endpoints](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/main/backend/app.py)] [[tires dataset](https://disk.yandex.ru/d/WTfWlQqAaTR-ZA)] |
| Darya Stepanova | User experience design | Bot flow refinement and interface design [[figma](https://www.figma.com/design/llkM7QUkBNkwm0pit8qUhn/KolobokBoard?node-id=0-1&t=S58PeihoZSgsA2XF-1)] |
| Ekaterina Petrova | Dataset preparation and API support | Labeled dataset (350 collected) and backend assistance [[tires dataset](https://disk.yandex.ru/d/WTfWlQqAaTR-ZA)] |
| Dmitry Tetkin | Bot interaction logic | Telegram bot [prototype](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/main/tg_bot/logic.py) |

We confirm that all code in the main branch:
- [x] Compiles and runs without errors
- [x] Deploys successfully via docker-compose (via instructions in README.md)
