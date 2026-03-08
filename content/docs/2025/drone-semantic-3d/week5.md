---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

**Session 1: Industrial Drone Operator (Construction Industry)**

**Key Feedback:**
- "The MASt3R-SLAM system looks promising for dense 3D reconstruction, but our biggest concern is the internet connectivity requirement. Construction sites often have poor or unreliable network coverage, and drones lose signal frequently when operating in remote areas or around steel structures."
- "We need a system that can work completely offline during flight missions and sync data only when back at base station."
- "The real-time visualization is impressive, but if it requires constant internet connection, it's not practical for our field operations."

**Priority Issues Identified:**
1. **MEDIUM PRIORITY**: Add data synchronization mechanisms for intermittent connectivity
2. **LOW PRIORITY**: Optimize bandwidth usage for limited connection scenarios

**Session 2: Robotics Research Engineer (University Lab)**

**Key Feedback:**
- "While the visual SLAM approach with MASt3R is innovative, LiDAR-based solutions like LIO2 or LeGO-LOAM are significantly faster and more robust for real-time applications. Visual SLAM struggles in low-light conditions, textureless environments, and fast motion."
- "LiDAR provides direct 3D measurements without the computational overhead of stereo matching and depth estimation."
- "The 25000 point limit seems arbitrary - LiDAR can easily handle millions of points in real-time."

**Priority Issues Identified:**
1. **HIGH PRIORITY**: Benchmark performance against LiDAR-based alternatives
2. **MEDIUM PRIORITY**: Improve computational efficiency of visual processing
3. **LOW PRIORITY**: Consider hybrid visual-LiDAR fusion approach

**Session 3: Archaeological Survey Specialist**

*Participant: Digital archaeologist using drones for site documentation*

**Key Feedback:**
- "The 3D reconstruction quality is excellent, but we desperately need object detection and classification capabilities. We want to automatically identify and catalog artifacts, structures, and features during flight."
- "Manual post-processing to identify objects is too time-consuming. We need the system to automatically detect pottery shards, walls, foundations, and other archaeological features."
- "Integration with object scanning and measurement tools would make this perfect for our documentation workflow."

**Priority Issues Identified:**
1. **HIGH PRIORITY**: using agentic image crossing algorithms
2. **HIGH PRIORITY**: Add automatic object cataloging and measurement features
### Analyze

*Describe the important points that you received from the user feedback, what issues and with which priority you created.*

**Critical Analysis of User Feedback:**

1. **Connectivity Dependency (Highest Priority)**
   - All industrial users emphasized the need for offline operation
   - Current architecture requires internet for model inference and cloud processing
   - **Action Required**: Implement edge computing capabilities and offline model execution

2. **Performance Limitations (High Priority)**
   - Visual SLAM computational overhead compared to LiDAR solutions
   - Real-time processing requirements not met in complex environments
   - **Action Required**: Optimize algorithms and consider sensor fusion approaches

3. **Missing AI Features (High Priority)**
   - Users expect intelligent scene understanding beyond basic reconstruction
   - Object detection, classification, and measurement capabilities essential
   - **Action Required**: Integrate computer vision AI modules for semantic understanding

4. **Robustness Concerns (Medium Priority)**
   - Visual SLAM limitations in challenging lighting and texture conditions
   - Need for more robust tracking and mapping algorithms
   - **Action Required**: Improve algorithm robustness and add failure recovery mechanisms

## Iteration & Refinement

### Implemented features based on feedback

**Professional 3D Visualization System Enhancement**

- **Fixed Critical Camera Pose Extraction Bug**: Resolved issue where all camera positions were incorrectly extracted as [0,0,0] due to improper handling of lietorch.Sim3 batch dimensions. Now correctly extracts real 3D camera trajectories.

- **Performance Optimization for Large Datasets**: 
  - Implemented intelligent age-based subsampling (recent keyframes at full resolution, older keyframes progressively decimated)
  - Added spatial decimation using grid-based point cloud filtering
  - Introduced adaptive update frequency based on scene complexity
  - Point cloud processing now limited to recent keyframes to maintain real-time performance

- **Professional Viser-Based 3D Visualization**:
  - Complete trajectory visualization with green point clouds showing camera path
  - Blue coordinate frames displaying camera poses with proper orientations
  - Red current camera marker for real-time position tracking
  - Orange pose graph edges showing SLAM optimization connections
  - Interactive GUI controls for performance tuning (trajectory points, camera poses, spatial decimation)

- **Robust Error Handling and Validation**:
  - Added comprehensive position validation with shape checking
  - Implemented multiple fallback visualization methods (point clouds → spheres → coordinate frames)
  - Professional error suppression to avoid terminal spam
  - Connection health monitoring with automatic reconnection attempts

- **Real-time Performance Monitoring**:
  - Live FPS tracking and visualization statistics
  - Optimization status indicators showing when performance modes are active
  - Point cloud size and processing time metrics
  - Adaptive performance controls accessible through web interface

### Performance & Stability

**Performance Metrics:**

1. **Visualization Frame Rate**: 
   - Target: 10 FPS for visualization updates
   - Achieved: 7-10 FPS with 30+ keyframes (down from <2 FPS before optimization)
   - Measurement: Real-time FPS counter in GUI

2. **Point Cloud Processing Efficiency**:
   - Before: Processing all keyframes every frame (O(n) growth)
   - After: Processing last 10 keyframes only (O(1) fixed cost)
   - Memory Usage: Reduced by ~70% through intelligent subsampling

3. **Camera Pose Accuracy**:
   - Fixed extraction bug enabling proper trajectory visualization
   - Measurement: Real-time position validation and coordinate verification
   - All poses now correctly display in 3D space instead of clustering at origin

4. **Stability Improvements**:
   - Eliminated shape mismatch crashes through robust position validation
   - Added graceful degradation when visualization methods fail
   - Implemented automatic scene recovery after errors

**Areas for Further Improvement:**
- Reduce dependency on internet connectivity for core SLAM processing
- Optimize visual feature extraction and matching algorithms
- Implement GPU acceleration for point cloud processing

### Documentation

**Documentation Types in Project:**

1. **Technical Documentation**:
   - `README_PROFESSIONAL_VISER.md`: Comprehensive guide for the 3D 

**Rationale**: This documentation structure supports both end-users needing quick setup instructions and developers requiring detailed technical implementation details.

### ML Model Refinement

**Current MASt3R Model Optimization:**

1. **Inference Optimization**:
   - Implemented batch processing for keyframe feature extraction
   - Optimized point cloud confidence filtering (threshold: 1.0 → adjustable)
   - Added intelligent subsampling to maintain visual quality while reducing computational load

2. **Memory Management**:
   - Limited point cloud size to 25,000 points (configurable)
   - Implemented age-based keyframe processing to prevent memory overflow
   - Added spatial decimation with 5cm minimum point spacing

**Future Model Improvements Planned:**
- Implementation of sensor fusion with LiDAR data when available
- Custom model training for specific application domains (archaeology, construction)

## Plan for Next Week

### Task 1 – Unity Integration (Alexander & Ilvina)

**Objective**: Extend the Unity environment to simulate drone behavior and communicate with the backend system in real-time.

**Subtasks:**

1. **Capture Command Response**:
   Implement a command in Unity that captures and returns the following to the backend:
   * RGB Image
   * Depth Map
   * Camera Intrinsics
   * Camera Extrinsics

2. **User Prompt Input**:
   Enable the Unity interface to send user-generated textual prompts to the backend server for AI-based interpretation or agent dispatch.

3. **Drone Pose Synchronization**:
   Integrate a mechanism to receive real-time drone position and orientation data from the backend. The drone inside Unity should update its transform accordingly to reflect the commanded state.

4. **Obstacle Avoidance System**:
   Develop a basic obstacle avoidance algorithm:
   * Stop the drone if any object is detected within a 50 cm radius.
   * Send a warning to the backend including:
     * Detected object's position
     * Drone's current intrinsic and extrinsic parameters

5. **Justification**:
   Although real-world drones often have closed proprietary systems for navigation and sensing, this Unity simulation is necessary to prototype and test AI decision-making pipelines, especially in environments where hardware access is limited or delayed.

6. **System Integration**:
   Ensure full connectivity with the backend services (via API or socket), allowing for immediate experimentation and iterative development.

---

### Task 2 – Agentic AI Modules (Nikita)

**Objective**: Develop lightweight AI agents to interpret visual data and make actionable decisions for drone control and scene understanding.

**Subtasks:**

1. **Camera Orientation Agent**:
   Create an agent that analyzes the captured image and issues orientation commands to ensure the camera is aligned with the horizon.
   * Output: "Turn Camera Up" / "Turn Camera Down"

2. **Altitude Adjustment Agent**:
   Design an agent that adjusts drone altitude based on visual feedback to maintain its height at the vertical center of the room.
   * Output: Positional offset command: (ΔX, ΔY, ΔZ)

3. **Visual Description Agent**:
   Implement an image captioning model that generates semantic descriptions of captured images and logs them into a persistent database.

4. **Object Retrieval Agent**:
   Build an agent that:
   * Matches a user's natural language prompt with stored image descriptions.
   * Locates the most relevant image and extracts its capture position.
   * Sends a command to move the drone to the location of that viewpoint.
   * Example Prompt: *"Find the red vase"*

5. **Spatial Estimation Agent**:
   Develop an agent capable of estimating room or building size (length, width, height) from a single or sequence of images

---

### Task 3 – Path Planning (Mahmoud)

**Objective**: Develop motion planning logic for drone navigation based on 3D spatial data and SLAM.

**Subtasks:**

1. **A*-Based Path Planning**:
   Implement a 3D A* path planner that calculates a series of straight-line segments from the drone's current position to a target point within a known 3D map.

2. **Dynamic Updates**:
   Incorporate real-time updates from:
   * SLAM outputs (to reflect new environmental data)
   * Obstacle warnings from the Unity system
   Replan as necessary to ensure safe navigation.

---

### Task 4 – Frontier-Based Exploration (Mahmoud)

**Objective**: Implement an exploration strategy that drives autonomous discovery in unknown environments using SLAM.

**Subtask:**

* Develop a frontier-based exploration algorithm that continuously identifies and moves toward unexplored regions of the environment. This enables autonomous mapping and coverage of indoor scenes.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).