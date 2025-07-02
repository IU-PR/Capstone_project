---
title: "Week #3"
---
# **Week #3**

## Implemented MVP Features

### 1. 3D Scene Reconstruction Pipeline (Mahmoud Mousatat)

We have successfully established an end-to-end 3D scene reconstruction pipeline, converting images into structured, interactive 3D visualizations. The main pipeline stages are:

- **MASt3R-SLAM**: Produces dense point clouds from image sequences.
    
- **Point Cloud Alignment**: Ensures canonical coordinate system orientation via PCA.
    
- **SpatialLM**: Utilizes spatially-aware large language models for semantic scene descriptions.
    
- **Web Frontend (Three.js/WebGL)**: Allows interactive visualization of point clouds and scene layouts.
    
- **Backend API (Flask REST API)**: Manages processing jobs and integrates all pipeline components.
    

### 2. Drone Simulation Environment (Ilvina Akhmetzianova)

- Implemented basic drone simulation environment using Unity, focusing on simplified physics for ease of control.
    
- WebSockets connection established between Unity simulation and Python-based backend, facilitating command execution and data exchange.
    
- Developed intuitive drone control APIs for easy integration with future agentic systems.
    

### 3. Drone Data Server (Alexander Rozanov)

- Dockerized backend server setup with dynamic indexing (ELK stack-inspired), providing flexibility for evolving data schemas without additional code modifications.
    

### 4. Agentic Architecture (Nikita Sergeev)

- Initial conceptual sketches completed for the architecture of the agentic system, identifying key interactions with backend and simulation components.
    

## Demonstration of the Working MVP
visualization of the point cloud - https://vkvideo.ru/video-230535967_456239019
Drone simulation - https://vkvideo.ru/video-230535967_456239018

## Internal Demo

- Demonstrated a working integration between simulation and backend services.
    
- Verified the full reconstruction pipeline from simulated drone-captured images to interactive 3D visualization.
    
- Received feedback to refine point cloud scale consistency for better real-world applicability.
    

# Weekly Commitments

### Individual Contributions

- **Mahmoud Mousatat**: Developed and optimized MASt3R-SLAM algorithm; refined point cloud alignment method ensuring canonical orientation.
    
- **Ilvina Akhmetzianova**: Finalized drone simulation environment, including Unity-Python integration via WebSockets and control API enhancements.
    
- **Alexander Rozanov**: Completed backend server with dynamic indexing and containerized deployment via Docker Compose; performed code reviews and merges.
    
- **Nikita Sergeev**: Developed agentic architecture sketches, highlighting integration points for future AI-driven drone navigation and data collection.
    

## Plan for Next Week

- Achieve full integration testing between backend services and the drone simulation environment.
    
- Begin implementation of the agentic system architecture based on the initial sketches.
    
- Resolve outstanding scaling issue in point cloud generation by integrating accelerometer data from drone simulation.
    

## Confirmation of Code's Operability

We confirm that the code in the main branch:

-  Is in working condition.
    
-  Runs via docker-compose (as described in the `README.md`).
    
