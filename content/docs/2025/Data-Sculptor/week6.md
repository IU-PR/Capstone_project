## Links

- **Deployment**: link
- **Solution Design Artifacts:** [link](https://strategic-control.kaiten.ru/documents/g/712fc661-6763-48dd-bd71-b40953de200a)
- **Product Backlog:** [link](https://strategic-control.kaiten.ru/space/606257/boards)
- **Engineering Decisions Documentation: (API docs included)** [link]()
- **System Design:** [link](https://strategic-control.kaiten.ru/documents/d/75a331fd-6a8b-4109-9ac9-20e4346e8111)
- **Technical Backlog**: [link](https://strategic-control.kaiten.ru/space/606259/boards)
- **Design**: [link](https://www.figma.com/design/rwyyRy5C4erUkl8Y3EbyLE/Untitled?node-id=0-1&p=f&t=srZiw3lEU7COFbWg-0)
- **Demo**: [link](https://disk.yandex.ru/d/H3dRW7BWHSQtIQ)

## Final deliverables

### Project Overview

> **Target Audience**
> EdTech businesses selling online courses in the context of Continuing Professional Education (CPE) in Machine Learning and Data Science relying on mentors recruited from industry experts for client homework assignments assessment

> **Problem Statement**
>The cost of mentorship and industry expertise for client homework assignments assessment is extreme (35-45% of annual budget), while the average review delay and extra delays caused by timezone differences cause continuous and unavoidable waves of customer complaints, refund requests, and lawsuits

> **Key Strategic Bet**
> Approximately 90% of mentor efforts when reviewing homework assignments do not require their full expertise: standard well-documented errors, typical violations of machine learning and data science industry standards, routine code style checks etc. Thus, 90% of assessment efforts can be automated, making the feedback extremely cheap, instantaneous, yet still of high quality

> **Solution**
> Implemented automatic deep homework (cases) assessment system and integrate it into the target businesses, automating 90% of homework assessment efforts while using the mentors' expertise for the most complex and uncertain cases

#### Active Features

1. **Semantic feedback generation.** Whenever the user completes a subtask and requests its validation, LLM generated feedback, which complies with key quality attributes, appears in the chat window of this cell. This feedback addresses discrepancies between the user solution and the ideal solution in a manner that encourages reflection and learning from the user's mistakes.
2. **Realtime code validation.** While the user writes code, any critical syntax errors or mistakes that guarantee real-time errors are highlighted to the user. Code style and critical errors are not shown in realtime. This is done to encourage the user to write code that works first, before adapting it to the industry standards and best practices.
3. **Syntactic feedback generation.** When a user completes a subtask and receives approval from the system's semantic analysis, then the user can request syntactic feedback generation. Syntactic feedback addresses violations of industry best practices and widely accepted standards, encouraging the user to comply with them.
4. **LLM chat.** Whenever the user misunderstands or doubts the received feedback, it can be clarified in a chat with the assistant that generated the feedback. At any point in time the assistant is aware of the current code, ideal solution of the task, previously provided feedback, and the conversation history, thus providing highly personalized and accurate clarifications.
5. **Case uploading**. Administrators who have access to the system deployment can upload case files (case profile, case solution template, case dataset, and requirements) to enable the system to validate solutions of new tasks. During case uploading the system generates a custom environment to suit the test execution.

#### Passive Features

1. **Secure communications.** All the system components communicate via mTLS protocol using internal identities, making data interception and fake requests infeasible.
2. **Isolated dynamic user environments.** User environments for code execution are enabled and disabled dynamically based on users' activity. Each environment is isolated from others on process level, network level, and identity verification level, protecting users and the system itself from external attacks.
3. **Progress tracking.** All user progress for each case is tracked and saved dynamically to enable users to work in sessions without losing any progress.

### Tech stack

- **Languages**
	- Python
	- Typescript
- **Frameworks**
	- FastAPI
	- React
- **Integrated tools**
	- JupyterHub
	- Qwen/Qwen3-30B-A3B
	- vllm
	- Keycloak
	- HashiCorp Vault
	- PostgreSQL
	- MinIO
	- ruff
	- MyPy
	- Bandit
	- Vulture
	- MLScent (ml_smell_detector)
	- repo2docker

### Setup instructions

Please see detailed setup and usage in the [repository README](https://github.com/IU-Capstone-Project-2025/Data-Sculptor).

## Presentation draft

See presentation draft [here](https://www.beautiful.ai/player/-OVJAgN74c4mW2OylaRk).

# Weekly commitments

## Individual contribution of each participant

### Dmitriy Prokopyev

- Added new increments, existing ones advanced and validated, see [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) for details
- Conducted Sprint Planning and other meetings required to orchestrate project development
- Invalidated some interface changes and provided detailed feedback to ensure correspondence with 
- Prepared the presentation draft
- Finalized some internal documents and project requirements to ensure successful completion
- Prepared the requirements for project migration to other servers after the Capstone course completion

### Egor Torshin

- Implemented progress tracker microservice
- Helped to migrate progress tracking into the custom docker spawner
- Coordinated backend development, held responsibility for all backend increments

### Aziz Vundirov

- Implemented custom docker spawner, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/71203fe076a4ee34bf525813da0bbc709f366986#diff-47e935b31d81158b9bb489cc2f0948576eff04a4006fea6f42462a4a75ba8875)
- Implemented cases progress tracking, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/4124b16c8ca301632324005a1316417bd912bfd6)
- Implemented LLM feedback saving, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/90ff1fb4c5e8bab688b7f42f9d33628ae3a4cae5)

### Nikita Tiurkov

- Rewritten the module for automatic quality assessment of main ML pipeline of the project, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/db378e59960e2d2534e384777f465c19d46f8792)
- Optimized metrics processing module and replaced the bootstrapping logic with a more suitable beta distribution bootstrapping for more appropriate confidence interval calculations, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/1aff50df9293ccd88432d3e37f078ace1f59b514)
- Located test cases that contained warnings leakage, causing biased evaluation, see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/665e2ad05f976da152347adf75033cf6dab4c6fa)
- Merged profile uploader microservice (older version) with case uploader microservice (newer version), see [commit](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/commit/0fb1b2a575526af4c5f7ac8f4318944ca1ac5db6)

### Oleg Shchendrigin

- Updated metrics calculation logic in LLM-as-a-judge evaluation service
- Updated the metrics evaluation logic to pull generated feedback from the semantic feedback microservice based on test cases prepared in advance

### Marsel Fayzullin

- Implemented domain name routing to enable simple service access
- Implemented reverse proxy to enable public access to private server where the project is deployed
- Implemented automatic public SSL certificate rotation based on certbot

> See [increment definition](https://strategic-control.kaiten.ru/space/606257/boards/card/51810103) for more detailed requrements

### Dmitriy Yashin

- Setup HashiCorp Vault to distribute TLS certificates across microservices via REST API
- Setup IP whitelisting for internal microservices
- Setup automatic internal certificates rotation via HashiCorp Vault
- Setup CORS for some domains for compliance and initial filtering of invalid requests
- Implemented a custom class for valid mTLS communication
- Implemented a custom endpoint for TLS certificates requests
- Implemented a custom class to wrap HTTP requests for HTTPS communication, to establish a valid HTTPS communication with other microservices

## Plan for Next Week

- [ ] Finalize the project presentation preparations
- [ ] Perform the final presentation
- [ ] Prepare the codebase and documentation for future project migration
- [ ] Maximize test coverage
- [ ] Maximize compliance with linting and SAST tools
- [ ] Burn down the accumulated tech debt
- [ ] Conduct final retrospective to gain valuable project management insights for the future 

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x]  In working condition.
- [x]  Run via docker-compose (or another alternative described in the `README.md`).
