## Testing and QA

Project focus on extensive real-time code validation significantly complicates the testing strategy, especially due to integration with JupyterHub. Regardless, we have come up with an original approach.

1. Validate strict formal requirements with end-to-end tests and unit tests
2. Validate informal requirements using strictly defined Acceptance Criteria (see [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards))
3. Validate semi-formal quality attributes using an evaluation script that approximates statistical performance metrics based on natural language definitions of acceptance criteria and quality attributes (almost done)

### Evidence of test execution

- See tests execution and CI/CD pipeline [results](https://disk.yandex.ru/d/f4aICLBKDf5xeQ)
- See [examples](https://disk.yandex.ru/d/Tw--chsGt1_ALQ) of semi-formal quality attributes evaluation script launches

## CI/CD

Current CI/CD setup is established to gradually move incremental product changes between various completion and approval stages: dev (testing), beta (staging), UAT (production).

**PR or commit to dev:**
1. Deploy to dev (no validation during intermediate development steps)

**PR to beta:**
1. Perform linting
2. Perform SAST (Static Application Security Testing)
3. Run internal tests
4. If all validations pass, deploy to beta (staging)

**PR to main:**
1. Perform linting
2. Perform SAST (Static Application Security Testing)
3. Run internal tests
4. Await manual approval from team lead
5. Deploy to UAT (production)

> **Python Linting and Formatting**
> 	- **Ruff**: Fast Python linter and formatter (replaces Black, Flake8, isort)
> 	- **mypy**: Static type checking
> 	- **bandit**: Security vulnerability scanning
**TypeScript Quality (for custom frontend injections)**
> 	- **ESLint**: Linting for TypeScript/JavaScript code
> 	- **Prettier**: Code formatting

### Links to CI/CD configuration files

- Please see CI/CD configuration files [here](https://github.com/IU-Capstone-Project-2025/Data-Sculptor/tree/main/.github/workflows)

## Deployment

### Staging

In respect to the schema described above and in previous report, current `beta` deployment is considered a staging requirement, which is used to test increments compatibility with each other, ensure match with their acceptance criteria, and receive approval from the team members responsible for meeting the business requirements.

> Please see current `beta` deployment [here](http://10.100.30.239:52152/user/developer/)

## Vibe Check

Processes established within the team facilitate weekly discussion of any encountered roadblocks. Technical issues and suggested changes are discussed weekly, example issue list was documented in the previous week report.

Additionally, such discussions led to some changes into the internal team processes. **Examples** include:
- Server ports allocation document was introduced to prevent deployment chaos
- Daily check-ins were introduced for backend developers to ensure progress alignment with sprint plans
- Regular meeting times for different team subsections were established instead of one Sprint Planning event

# Weekly commitments

## Individual contribution of each participant

### Dmitriy Prokopyev

- Added new increments, existing ones advanced and validated, see [Product Backlog](https://strategic-control.kaiten.ru/space/606257/boards) for details
- Conducted Sprint Planning and other meetings required to orchestrate project development
- Invalidated some increments due to misalignments with acceptance criteria (["Reopened" status](https://strategic-control.kaiten.ru/space/606257/boards)), ensured that they are fixed and deployed
- Introduced changes into internal team processes
- Validated current UI/UX design to ensure alignment with project criteria

### Other Contributions

Due to focus on testing, increments finalization (those), and partial implementation of further increments, the individual development contributions are quite granular, and are interconnected in a complex way.

Due to this, we suggest to discuss them in detail during the weekly meeting.

## Plan for Next Week

- [ ] Integrate multiple sessions support for every other implemented feature
- [ ] Integrate customized environments support (pre-installed packages, included datasets and template files for cases)
- [ ] Transition to the first version of custom UI (from the current JupyterHub integration)
- [ ] Integrate authentication mechanisms for managing user sessions
- [ ] Implement secure communication between microservices
- [ ] Finalize integration of the quality attributes auto-evaluator into the CI/CD pipeline to validate intermediate
- [ ] Iterate on case-aware feedback provision to improve speed, context awareness, and answers quality
- [ ] Isolate user sessions via individual containers and subdomains

## Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x]  In working condition.
- [x]  Run via docker-compose (or another alternative described in the `README.md`).
