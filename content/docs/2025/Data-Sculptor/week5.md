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
