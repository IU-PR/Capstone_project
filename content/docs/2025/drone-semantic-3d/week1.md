---
title: "Week #1"
---

# Week #1

## Project description

### Project name: **Autonomous Semantic 3D Reconstruction and High-Fidelity Mapping**

**Code repository:** https://github.com/Mousatat/Autonomous-Drone-Semantic-3D-Reconstruction-and-High-Fidelity-Mapping

An autonomous UAV-based system designed for semantic 3D spatial reconstruction and high-fidelity mapping. The project integrates real-time semantic segmentation via SpatialLM, autonomous UAV navigation using agentic AI, and precise exploration strategies to efficiently generate detailed digital twins.

---

## Problem Statement

Existing autonomous 3D mapping solutions face limitations in:

- Real-time semantic understanding of environments.
    
- Autonomous optimal exploration decision-making.
    
- Efficient and effective data processing for high-quality spatial reconstructions.
    

Our system addresses these challenges through advanced semantic models, autonomous UAV navigation powered by agentic AI, and two-stage reconstruction techniques for superior spatial accuracy and usability.

---

## Team Members

| Team Member          | Telegram Alias | Email Address                        | Track                 | Responsibilities                                 |
| -------------------- | -------------- | ------------------------------------ | --------------------- | ------------------------------------------------ |
| Mahmoud Mousatat     | @Mousatat      | m.mousatat@innopolis.university      | Computer Vision       | Semantic understanding from visual data          |
| Nikita Sergeev       | @nary_2        | n.sergeev@innopolis.university       | AI & Backend          | Developing agentic AI logic                      |
| Alexander Rozanov    | @alrozanov     | al.rozanov@innopolis.university      | DevOps                | Integrating AI solutions with cloud environments |
| Ilvina Akhmetzianova | @IviUnicorn    | i.akhmetzianova@innopolis.university | Simulation & Frontend | Building simulation environments and interfaces  |

---

## Brainstorming

### Ideas during brainstorming

1. **Autonomous Semantic 3D Mapping (Chosen idea)** — UAV system using semantic segmentation, real-time navigation, and agentic AI for 3D mapping and digital twin creation.
    

---

## Basic requirements

### Target users and their primary needs

- **Construction and Architecture Firms:** Require accurate digital twins for BIM and project monitoring.
    
- **Disaster Response Teams:** Need rapid and accurate maps for damage assessment and planning.
    
- **Urban Planning and Infrastructure Management:** Require updated spatial data for urban management.
    

---

### Initial scope (MVP)

**Included:**

- Real-time semantic spatial reconstruction using SLAM and SpatialLM.
    
- Autonomous navigation planning and exploration via agentic AI.
    
- Simple game-server communication setup for simulation integration.
    

**Excluded (future iterations):**

- Detailed photogrammetric reconstruction using traditional methods.
    
- Neural rendering for interactive visualizations.
    
- Fully scaled cloud solutions and multi-UAV coordination.
    

---

## Tech-stack

### Frontend / Visualization

- **PlayCanvas:** Chosen as an initial game engine for simulation and frontend interactions.
    

### Backend / AI Models

- **SpatialLM:** Semantic segmentation.
    
- **Visual-Inertial SLAM:** SLAM3R or similar solutions.
    
- **Claude 4 or Gemini 2.5 Pro:** Agentic AI path planning and decision-making.
    

### Cloud Infrastructure

We are utilizing a **Virtual Dedicated Server (VDS)** to host our cloud infrastructure, specifically deploying an **Nginx server** to facilitate efficient and secure communication between LLM and agentic AI.

---

## Weekly commitments

### Individual contribution of each participant:

- **Mahmoud Mousatat:**
    
    - Investigated suitable vision models for semantic understanding.
        
- **Nikita Sergeev:**
    
    - Explored agentic frameworks for semantic vision integration and spatial data processing.
        
- **Alexander Rozanov:**
    
    - Prepared initial weekly report.
        
    - Explored integration solutions for agentic AI and cloud infrastructure.
        
- **Ilvina Akhmetzianova:**
    
    - Evaluated suitable game engines, initially selecting PlayCanvas for simulation.
        

---

## Confirmation of the code's operability

We confirm that the code in the main branch:

-  In working condition.
