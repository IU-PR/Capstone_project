---
title: "Week #1"
---

# Week #1

## Project description

### Project name: *Kolobok*

**Code repository**: [https://github.com/IU-Capstone-Project-2025/Kolobok](https://github.com/IU-Capstone-Project-2025/Kolobok)

Many car service centers offer tire trade-ins, but pricing used tires is slow and error-prone. It typically requires manual measurement of tread depth and a subjective evaluation of spike wear, which is not scalable.

This project uses machine learning to automate tire valuation. Users send two photos of a tire to a Telegram bot. The system then detects the brand and parameters, estimates tread depth, and analyzes the condition of spikes.

The solution is designed for both car owners and retail employees, reducing manual workload and enabling remote consultations. Developed in response to a real-world need from a mid-sized car services.

### **Team Members**

| Team Member                           | Telegram Alias | Email Address                    | Track                                     | Responsibilities                                                                       |
|---------------------------------------|----------------|----------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------|
| Nikita Menshikov (Lead)               | @NikitaMensh   | n.menshikov@innopolis.university | Project manager                           | Team management, reports writing, customer communication, work environment maintenance |
| Nikita Zagainov                       | @V1adych       | n.zagainov@innopolis.university  | ML                                        | Core models research & development                                                     |
| Vladislav Strelkov                    | @motrooo       | v.strelkov@innopolis.university  | DevOps                                    | Product deployment, CI/CD                                                              |
| Sergey Aitov                          | @SerggAidd     | s.aitov@innopolis.university     | Backend, annotator                        | Dataset labelling + establishing backend logic                                         |
| Darya Stepanova                       | @darriyano     | d.stepanova@innopolis.university | UX designer                               | Construction and verification of telegram bot scenarious                               |
| Ekaterina Petrova                     | @vougeress     | e.petrova@innopolis.university   | Backend, annotator                        | Dataset labelling + establishing backend logic                                         |
| Dmitry Tetkin                         | @dimasik057    | d.tetkin@innopolis.university    | Frontend                                  | Implementing telegram bot to communicate with the user                                 |

## Brainstorming
### Ideas during brainstorming
1. **Tire Valuation System** (Chosen):  
   ML-powered analysis of tire condition through photos
2. **Virtual Car Detailing Platform**:  
   App for visualizing car modifications + service pricing
3. **Automated Maintenance Tracker**:  
   Service scheduling platform + maintenance history

### Brief market research / problem validation (1st idea)
- No comprehensive solutions combining brand detection, tread measurement and spike analysis
- One brand detection [solution](https://www.griddynamics.com/blog/how-to-identify-vehicle-tires-using-deep-learning-visual-models) using CV was found, however, we have a better idea (need testing) 
- 2 car services will be pilot platform for our solution

## Basic requirements
### Target users and their primary needs
1. **Car owners**:  
   Quickly value tires for sale/trade-in without visiting service center
2. **Retail employees**:  
   Accelerate tire evaluation process during customer interactions
3. **Service managers**:  
   Maintain consistent pricing routines across car service centers

### User stories
1. As a car owner, I want to photograph my tires and get instant valuation of thread depth and spikes condition so I can sell them faster
2. As retail staff, I want automated tread measurements and spikes analysis to reduce human error in evaluations
3. As a service manager, I want remote tire valuation to scale operations and accelerate processes

### Initial scope
| IN Scope (MVP)                          | OUT of Scope                 |
|-----------------------------------------|------------------------------|
| Telegram bot interface                  | E-commerce integration       |
| Tread depth measurement                 | Full tire marketplace        |
| Spike condition analysis                | Advanced damage detection    |
| Brand/size detection                    | Multi-platform support       |

## Tech-stack
| Component       | Technology                   | Justification                                                  |
|-----------------|------------------------------|----------------------------------------------------------------|
| Frontend        | Python (python-telegram-bot) | Team member has an experience developing with this library     |
| Backend         | Python (FastAPI)             | Async support, ML integration                                  |
| ML              | PyTorch, OpenCV              | Industry standard for vision tasks                             |
| Deployment      | Docker                       | Environment consistency, scalability                           |
| Annotation      | Label Studio                 | Easy deployment on local server, rich annotation capabilities  |

## Additional notes
- Kanban board created for task tracking
- Initial research on tire measurement algorithms completed
- Team communication channels established (Telegram)

# Weekly commitments
## Individual contribution of each participant
| Team Member         | Contributions                                                                                                                                               |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nikita Menshikov    | Project setup, report writing, [[kanban board](https://github.com/orgs/IU-Capstone-Project-2025/projects/9)] creation                                                                                                       |
| Nikita Zagainov     | ML [[research](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/4a60648dd629b54b227625ab7d07d34c2b51bd86)] |
| Vladislav Strelkov  | Docker setup ([[1](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/main/docker-compose.yml)], [[2](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/main/tg_bot/.env)], [[3](https://github.com/IU-Capstone-Project-2025/Kolobok/blob/main/tg_bot/Dockerfile)])                                                                                                                                               |
| Sergey Aitov        | 20 spike condition [[annotations](https://github.com/NikitaMensh/IU_Capstone_project_2025/blob/main/sergey_annotations_w1.png)] ([[sample](https://github.com/NikitaMensh/IU_Capstone_project_2025/blob/main/sergey_annotation_sample_w1.png)])                                                                                                                              |
| Darya Stepanova     | Telegram bot user flow [[design](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/038c5b913fdf6d97ffc62945ec45a03931973142)]                                                                                                                              |
| Ekaterina Petrova   | 20 spike condition [[annotations](https://github.com/NikitaMensh/IU_Capstone_project_2025/blob/main/kate_annotations_w1.png)] ([[sample](https://github.com/NikitaMensh/IU_Capstone_project_2025/blob/main/kate_annotation_sample_w1.png)])                                                                                                                              |
| Dmitry Tetkin       | "Hello World" Telegram bot [[implementation](https://github.com/IU-Capstone-Project-2025/Kolobok/commit/f2784c39f27eb312e1c638c4c0465555951ac97c)]                                                                                                                   |

## Confirmation of the code's operability
We confirm that the code in the main branch:
- [x] In working condition
- [x] Run via method described in README.md
