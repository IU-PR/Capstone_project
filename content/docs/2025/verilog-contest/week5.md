---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions
We made a Google Form to collect feedback from the users. We sent the form and send it to tha potential participants from InnoChipDesign Club.

#### Results(10 responses):

- **Submit interface clarity:** Mostly clear; one user noted confusion between Example and Your Solution panels.

- **Expected results data:** Status, simulation time, memory usage; detailed per-test data with waveforms; participant counts and average solves.

- **Bugs/issues:** Non-functional “Browse Contest” button; mobile layout overflow and dynamic height issues.

- **Navigation suggestions:** Scroll-to-top reset; horizontal nav; fix unresponsive buttons.

- **Feature requests:** Dark mode; “Restart last submission”; contest filters; linting; usage examples.

### Analyze

**High Priority:**

1. Restore “Browse Contest” button functionality.
2. Clarify submit UI layout (distinct Example and Your Solution).

**Medium Priority:**

1. Improve navigation UX (scroll reset, horizontal menu).
2. Fix mobile responsive overflow.
3. Enhance Results page with detailed metrics per test.

**Low Priority:**

1. Implement contest filtering and submission linting.
2. Add dark mode and restart button.
3. Provide usage examples and descriptions.


## Iteration & Refinement

### Implemented features based on feedback

- Complete work of submit-flow in UI.
- Added new features in Kanban-board for frontend development.
- Fixed bugs in the frontend.

### Performance & Stability
We used OpenTelemetry to get general metrics for our service in general for latency. 
https://drive.google.com/file/d/1dL2jNTaGq-yVP58fBRb1oKRgrulMwEFi/view?usp=sharing

### Documentation

- **Arcgitecture diagram:** 
  - General: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/architecture-diagram.png
  - Runner: https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/inside-runner.png
- **Submission-flow:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/submission-flow.png

- **User flow:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/user-flow.png

- **Frontend components with API:** https://excalidraw.com/#json=dhm9VrgFtowewja70TNCk,uZGGNYJ0-tBXG5Y154f8Jg

- **System architecture:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/system-architecture.md

- **Specifications:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/docs/specifications.md

- **README:** https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/main/README.md*


# Weekly commitments

## Individual contribution of each participant


| Team Member            | Week #2 Contributions                                                                      | Commits| 
| ---------------------- | ------------------------------------------------------------------------------------------ | ----------------------|
| **Mikhail Panteleev**  |         Submit-flow integration in frontend, service configs, user survey scenarios, fix bugs in backend.               | [f85eec9](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/f85eec954e86597f430ed9242a5385defe9945ee), [PR №43](https://github.com/IU-Capstone-Project-2025/verilog-contest/pull/43) 
| **Vladislav Merkulov** | Refactoring of status-codes. General settings for tracer.                    | [909d808](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/909d80851f0193bfb374e5543ec76f71bd4c8a07), [780fe11](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/780fe11881d1cb1d3d67a494b913edfe0b26c4f9) |
| **Aleksei Fominykh**   | Redis, MinIO k8s manifests.                                         | [285f349](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/285f349e0c273f963e1281c957be0ce38c081adf), [807542d](https://github.com/IU-Capstone-Project-2025/verilog-contest/commit/807542d7249b0e459c334a691318f4fc99503c96) |
| **Sofia Kulagina**     | Proccess isolation and sendboxing research with advantages and disadvantages of different tools for our system.            | [Process isolation](https://github.com/IU-Capstone-Project-2025/verilog-contest/blob/dev/docs/docs/process-isolation.md)|
| **Diana Yakupova**     | Meetings organization, report, kanban-board, frontend component diagram with API, collection of feedbacks. | [Frontend diagram](https://excalidraw.com/#json=dhm9VrgFtowewja70TNCk,uZGGNYJ0-tBXG5Y154f8Jg), [Google form](https://docs.google.com/forms/d/e/1FAIpQLSfuTJYcMXL06iWLRy_t8xrZvs9GfkT6k8W-N3zT_HRubE7TNQ/viewform?usp=header) |


## Plan for Next Week

On Week #6, each participant will complete its tasks: Aleksei will deploy Kubernetes, vladislav will introduce complete tracing and metric, Mikhail will bring the front to the final state. Also Sofia will make the administration panel, and Diana will prepare the final presentation and organize the work.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [✔] In working condition.
- [✔] Run via docker-compose (or another alternative described in the `README.md`).