## Feedback Acquisition
### Methodology

UAT (User Acceptance Testing) deployment link was shared with the test users. It contained a partially filled .ipynb notebook and a task description. The test users were tasked with fixing the pre-written sections and completing the .ipynb notebook to comply with the task description.

> The task description was taken from the corresponding case profile. 

During this process, they were personally observed by the project team lead, who kept silence at this time to avoid interfering with the test results. Afterwards, they were questioned about the learning outcomes of the experience and the encountered challenges.

> Questioning was conducted in person focusing on two aspects of the experience:
> 1. Learning outcomes
> 2. UX challenges

Afterwards, the received feedback was clarified and categorized into issues specified below. These issues have been rephrased in the project terms for clarity.

### Usability Testing Sessions, Key Findings

#### Session 1

- **Subject**
	- First year bachelor student interested in Machine Learning applications in scientific context
- **Reported learning outcomes**
	- Learn to check for missing values
	- Learn to notice and eliminate data leakage
	- Learn to correctly evaluate model performance
	- Learn to correctly encode categorical features
- **Reported UX challenges**
	- Buttons location, meaning, and differences are not intuitively clear
	- Overloaded real-time analysis: too many warnings to focus on performing the task
	- Inconsistency in generated feedback: sometimes certain issues get detected, sometimes not, therefore it is unclear whether they have been resolved
	- Warnings appearing after pressing one of the buttons do not disappear after being fixed, this is confusing
	- Newly added libraries have to be manually installed in the environment, while the user wants to focus on task itself

#### Session 2

- **Subject**
	- First year bachelor student interested in AI research and math
- **Reported learning outcomes**
	- Learn to check for missing values
	- Learn to identify overfitting via suspicious performance metrics imbalance
	- Learn to check for class imbalance and handle it
	- Learn to correctly encode categorical features
	- Learn to correctly evaluate model performance
- **Reported UX challenges**
	- Buttons location, meaning, and differences are not intuitively clear
	- Warnings appearing after pressing one of the buttons do not disappear after being fixed, this is confusing

#### Session 3

- **Subject**
	- Innopolis city resident (not a student) interested in career as an ML engineer
- **Reported learning outcomes**
	- Learn to notice and eliminate data leakage
	- Learn to check for class imbalance and handle it
	- Learn to check for missing values
- **Reported UX challenges**
	- Buttons location, meaning, and differences are not intuitively clear
	- Inconsistency in generated feedback: sometimes certain issues get detected, sometimes not, therefore it is unclear whether they have been resolved
	- Overloaded real-time analysis: too many warnings to focus on performing the task
	- Feedback provided in md files appears to be too abstract and generic
	- Feedback provided in md files often intersects with feedback generated in comments, this is confusing
	- Warnings appearing after pressing one of the buttons do not disappear after being fixed, this is confusing

### Feedback Analysis

- **Issue:** buttons location, meaning, and differences are not intuitively clear
	- **Cause:** this is an intermediate solution implemented due to delayed UI implementation
	- **Solution:** full UI implementation
	- **Priority:** critical
- **Issue:** overloaded real-time analysis, there are too many warnings to focus on performing the task
	- **Cause:** this was initially overlooked due to assuming that any feedback aligned with industry standards is valuable at any point in time
	- **Solution:** focus real-time code analysis on critical syntax errors and detection of future runtime errors
	- **Priority:** high
- **Issue:** inconsistency in generated feedback, sometimes certain issues get detected, sometimes not, therefore it is unclear whether they have been resolved
	- **Cause:** the generated feedback is not fully tied to the case profiles yet, this is a question of time
	- **Solution:** finalize feedback provision based on case profiles for generated feedback consistency
	- **Priority:** critical
-  **Issue:** feedback provided in md files appears to be too abstract and generic
	- **Cause:** the generated feedback is not fully tied to the case profiles yet (same reason)
	- **Solution:** finalize feedback provision based on case profiles for generated feedback consistency (same solution)
	- **Priority:** critical
- **Issue:** feedback provided in md files often intersects with feedback generated in comments, this is confusing
	- **Cause:** this seems to be a natural model limitation
	- **Solution:** use quality enhancement solutions described below
	- **Priority:** critical
- **Issue:** warnings appearing after pressing one of the buttons do not disappear after being fixed, this is confusing
	- **Cause:** due to heavy processing necessitated by deep syntactic analysis, it cannot be launched in runtime and therefore attached to syntactic analysis button
	- **Solution:** allow user to mark corrected issues to make them disappear from view
	- **Priority:** mid
- **Issue:** newly added libraries have to be manually installed in the environment, while the user wants to focus on task itself
	- **Cause:** automatic environment setup based on case profiles is not yet implemented, this is a question of time
	- **Solution:** finish implementing case-based automatic environment setup
	- **Priority:** critical

> See all newly created and changed [product backlog](https://strategic-control.kaiten.ru/space/606257/boards) increments [here](https://strategic-control.kaiten.ru/space/606257/boards)

## Iteration & Refinement

### Implemented features based on feedback


- **Issue:** buttons location, meaning, and differences are not intuitively clear
	- **Progress Summary:** custom UI that resolves this issue is approximately 60% implemented, it will be finalized by the end of this week
	- **Corresponding Documentation Item:** [link](https://www.figma.com/design/rwyyRy5C4erUkl8Y3EbyLE/Untitled?node-id=0-1&p=f&t=Ppl0LwiYf3Fxzllt-0)
- **Issue:** overloaded real-time analysis, there are too many warnings to focus on performing the task
	- **Progress Summary:** done
	- **Corresponding Product Backlog Item:** [link](https://strategic-control.kaiten.ru/space/606257/boards/card/52201600)
- **Issue:** inconsistency in generated feedback, sometimes certain issues get detected, sometimes not, therefore it is unclear whether they have been resolved
	- **Progress Summary:** in progress, requires evaluation on test dataset to claim completion with certainty
	- **Corresponding Product Backlog Item:** [link](https://strategic-control.kaiten.ru/space/606257/boards/card/51907146)
	- **Corresponding Documentation Item:** [link](https://strategic-control.kaiten.ru/documents/d/01024c00-2c48-4713-930c-cb82ca8158d5)
-  **Issue:** feedback provided in md files appears to be too abstract and generic
	- **Progress Summary:** in progress, requires evaluation on test dataset to claim completion with certainty
	- **Corresponding Product Backlog Item:** [link](https://strategic-control.kaiten.ru/space/606257/boards/card/51907146)
	- **Corresponding Documentation Item:** [link](https://strategic-control.kaiten.ru/documents/d/01024c00-2c48-4713-930c-cb82ca8158d5)
- **Issue:** feedback provided in md files often intersects with feedback generated in comments, this is confusing
	- **Progress Summary:** in progress, requires evaluation on test dataset to claim completion with certainty
	- **Corresponding Product Backlog Item:** [link](https://strategic-control.kaiten.ru/space/606257/boards/card/51907146)
	- **Corresponding Documentation Item:** [link](https://strategic-control.kaiten.ru/documents/d/01024c00-2c48-4713-930c-cb82ca8158d5)
- **Issue:** warnings appearing after pressing one of the buttons do not disappear after being fixed, this is confusing
	- **Progress Summary:** delayed to prioritize other issues since this is the last stage of feedback for the user
- **Issue:** newly added libraries have to be manually installed in the environment, while the user wants to focus on task itself
	- **Progress Summary:** almost done
	- **Corresponding Product Backlog Item:** [link](https://strategic-control.kaiten.ru/space/606257/boards/card/51432381)

> See deployed application link and entrance credentials [here](https://strategic-control.kaiten.ru/documents/d/c3e7daa4-1678-4e99-839b-6caee4383234)

### Performance & Stability

The following is a list of measurable clearly defined metrics demonstrating performance and efficiency of key aspects of the project along with measurement and decision making methods applicable to each metric.

- **LLM-generated feedback quality**
	- *How to measure:* LLM-as-a-judge evaluation for semi-formal quality metrics of LLM-generated feedback
	- *Context (balance) metric*: solution size
	- *Measurement unit and conditions:* measure after sprints affecting LLM feedback generation logic using no less than 5 diverse test notebooks
- **Waiting time for LLM-generated feedback**
	- *How to measure:* feedback requests latency
	- *Context (balance) metric*: feedback generation RPM (requests per minute)
	- *Measurement unit and conditions:* measure after sprints affecting LLM feedback generation logic over no less than 2 weeks and 50 feedback requests
- **Waiting time for feedback clarifications**
	- *How to measure:* chat requests latency
	- *Context (balance) metric*: chat RPM (requests per minute)
	- *Measurement unit and conditions:* measure after sprints affecting LLM feedback generation logic over no less than 2 weeks and 80 clarification requests
- **Waiting time for real-time static analysis**
	- *How to measure:* real-time syntactic analysis requests latency
	- *Context (balance) metric*:
		- RPS (requests per second)
		- Provided code length (in symbols)
	- *Measurement unit and conditions:* measure after sprints affecting real-time syntactic analysis logic over no less than 1 week and 200 requests
- **Waiting time for deep syntactic analysis**
	- *How to measure:* deep syntactic analysis requests latency
	- *Context (balance) metrics*: 
		- RPS (requests per second)
		- Provided code length (in symbols)
	- *Measurement unit and conditions:* measure after sprints affecting deep syntactic analysis logic over no less than 2 weeks and 100 requests
- **Resource efficiency**
	- *How to measure:* tokens per case per student account
	- *Context (balance) metric*: case profile code size
	- *Measurement unit and conditions:* measure after sprints affecting LLM feedback generation logic over no less than 3 weeks and 30 solved cases


> **How to evaluate any of these metrics and make decisions based on it?**
> 1. Build a graph of the base metric combined with context metrics over measurement period
> 2. Calculate appropriate pairwise correlation coefficients between base metric and context metrics to evaluate
> 3. Calculate overall base metric statistics over measurement period: mean, standard deviation, confidence interval for mean (95%), confidence interval for standard deviation (95%), prediction interval (95%)
> 4. Compare the graph, the correlation coefficients, and the overall statistics to the previous week measurements
> 5. Make contextually-informed conclusions about the actual progress based on these metrics
> 6. Use these conclusions and context gained from metrics to decide next actions

### Documentation

**Internal Documentation**
- [Project Layer](https://strategic-control.kaiten.ru/documents/g/712fc661-6763-48dd-bd71-b40953de200a)
	- **Contents:**
		- Strategy (Hypothesis Map)
		- Target User Experience (Process-Experience Map)
		- Key Design Decisions (Story Implementation Map)
		- Project Design Flow (Requirements Engineering Backlog)
	- **Purpose:** defines project goals, strategy, user experience, and scope, sets the tone and setting for the entire project
- [Product Layer](https://strategic-control.kaiten.ru/documents/g/f3f0b50a-94b2-4811-8f85-a37e9a399b00)
	- **Contents:**
		- Feedback Quality Requirements
			- A detailed document with acceptance criteria and quality attributes for LLM-generated feedback
		- Feedback Metrics Distribution
			- A document detailing methods of measuring compliance with given metrics
		- Product Backlog
			- Dynamic tasks board detailing the incremental feature implementation plans from the product perspective
	- **Purpose:** defines product progression rules
- [Engineering Layer](https://strategic-control.kaiten.ru/documents/g/0ce62c64-1394-4c12-af8a-93ea39d793a9)
	- **Contents:**
		- Documents about endpoints
			- Specify endpoint signatures for internal team coordination and technical tasks decomposition
		- LLM Inference Optimization
			- Describes reproducible procedures to optimize LLM inference speed
		- Security Specifications
			- Documents describing security decisions critical to the project requirements
		- LLM inference speed measurements
			- Details inference speed test results for various LLMs deployed on our GPUs
		- System Design document
	- **Purpose:** describes important implementation decisions made by engineers for reproducibility and context awareness within the team
- [Development Layer](https://strategic-control.kaiten.ru/documents/g/9f08154e-5b3d-43e9-9906-aa9df964ebcb)
	- **Contents:**
		- Deployments
			- Specifies the deployment types (`dev` for developers, `beta` as staging, `uat` as pre-production), their target addresses and details
		- Servers
			- Specifies how to use the project server
		- Technical Backlog
			- Dynamic tasks board detailing technical tasks and their current states
	- **Purpose:** supports development process by synchronizing the team understanding of the technical details of the project
- **API Endpoints Documentation**
	- **Contents:**
		- Swagger API documentation for FastAPI endpoints of all microservices
	- **Purpose:** simplifies development, enables asynchronous development cycles and more straightforward developers onboarding

### ML Model Refinement

We validate semi-formal quality attributes of the generated LLM feedback using an evaluation script that approximates statistical performance metrics based on natural language definitions of acceptance criteria and quality attributes.

Afterwards, we make informed decisions from these metrics to iterate on the model setup, see "Performance & Stability" section.

# Weekly commitments

## Individual contribution of each participant

### Dmitriy Prokopyev

- Added new increments, existing ones advanced and validated, see [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) for details
- Conducted Sprint Planning and other meetings required to orchestrate project development
- Invalidated some increments due to misalignments with acceptance criteria (["Reopened" status](https://strategic-control.kaiten.ru/space/606257/boards)), ensured that they are fixed and deployed
- Participated in designing architectural changes for multi-user support

### Egor Torshin

- Migrated parsing tools from real-time to the syntactic analysis microservice side
- Cleaned up the GitHub branches of the deployment stages in PR, see [comparison](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/compare/dev...main)
- Participated in the design of Multi-User Access architecture
- Updating the user documentation, see [pull request](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/26)
- Rented a VM for JupyterHub hosting to solve an intermediate technical issue
- Coordinated backend development, held responsibility for all backend increments

### Aziz Vundirov

- Replaced `Bandit` and `Vulture` with ruff configuration, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/f4149ed9f59c31b3e670fe7f5e23c8b0e14c4a94)
- Updated `ruff` config to match updated project requirements, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/b436651fd8eae8a335a46e2bdf53798d45c06538)
- Migrated real-time analysis into a separate microservice, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/cea5ebb0268b564b195669254ded365ec05466dd#diff-969989fab9ec34405a292d925caa243e33fe465fb4a41f5b7cf0bd179f617b17)
- Progressed significantly in resolving cgroupv2 process spawning issue on the server

### Nikita Tiurkov

- Implemented case-aware feedback generation logic, see [pull request](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/pull/22)
- Conducted various tests to optimize LLM inference speed, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/5e43f8d2348151e72ed0e2fe71bb8e89a40a9ed4)
- Migrated from vLLM to SGLang for LLM inference speed optimization
- Fixed newly encountered bugs in semantic feedback microservice, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/ae887dd5418118e002192f6ddc41e6aebbce2615)

### Oleg Shchendrigin

- Prepared data samples for LLM feedback generation validation
- Implemented automated evaluation of LLM feedback quality via guided LLM-as-a-judge
- Designed metrics distribution logic, see [document](https://strategic-control.kaiten.ru/documents/d/3ae29a77-cfa5-4cd4-93d4-32794d0d4534)

### Marsel Fayzullin

- Contributed significantly to debugging intermediate deployment issues
- Setup and deployed HiashiCorp Vault

### Dmitriy Yashin

- Setup and deployed integration of JupyterHub and Keycloak
- Implemented security measures for JupyterHub protection planned during the earlier weeks
- Implemented dynamic subdomain generation and redirection of users via their own subdomains for security purposes and integrated this logic with JupyterHub
- Managed to identify the key technical issue hindering the development process so far and suggest a working solution

## Plan for Next Week

- [ ] Finalize secure microservices communication over mTLS (until the end of the project)
- [ ] Finalize internal TLS certificates generation, distribution, and rotation
- [ ] Ensure test coverage for key code areas
- [ ] Implement progress permanence between user sessions
- [ ] Finalize custom UI integration
- [ ] Ensure quality via CI/CD pipeline results
- [ ] Start to prepare the final presentation

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x]  In working condition.
- [x]  Run via docker-compose (or another alternative described in the `README.md`).
