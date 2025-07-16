---
title: "Week #4"
---

# **Week #4**

## Testing and QA

*Summary of testing strategy and types of tests implemented.*
Our team developed, and research project's QA aspects from first capstone week so, we have multiple testing scenarious, because our project is consist of complex components, which really need QA testing.
In our project we have:
 - Graph generation testing
 - Basic Unit testing
 - Vector RAG testing
 - Docker Compose Configuration testing
 - Linting and styling checks

### Evidence of test execution
- [Tests CI Results](https://github.com/Beer-Bears/scaffold/actions/workflows/tests.yml?query=branch%3Amain)
- [Style CI Results](https://github.com/Beer-Bears/scaffold/actions/workflows/pre-commit.yaml?query=branch%3Amain)
- [Security CodeQL Scanning Results](https://github.com/Beer-Bears/scaffold/actions/workflows/codeql.yml?query=branch%3Amain)
- [Docker Compose CI Results](https://github.com/Beer-Bears/scaffold/actions/workflows/compose-check.yaml?query=branch%3Amain)

## CI/CD

### Security Code QL Scanning 
[Workflow](https://github.com/Beer-Bears/scaffold/blob/main/.github/workflows/codeql.yml)

Automated Security Scanner for repository find vulnerabilities in code logic.

### Docker Compose Check
[Workflow](https://github.com/Beer-Bears/scaffold/blob/main/.github/workflows/compose-check.yaml)

Checks if docker compose can prorerly configure, build and run using default configuration.

### Pre-commit style check
[Workflow](https://github.com/Beer-Bears/scaffold/blob/main/.github/workflows/pre-commit.yaml)

Check code styling and linting uses pre-commit configuration.

### Pull request aproval celebration
[Workflow](https://github.com/Beer-Bears/scaffold/blob/main/.github/workflows/pull-request-approved.yaml)
When pull request is approved by person sends cute bear picture into comments to congradulate with approval and readiness for merge.

### Conventional PR title checker
[Workflow](https://github.com/Beer-Bears/scaffold/blob/main/.github/workflows/pull-request-conventional-title.yaml)
Checks pr title with conventional rules, because that we use squashing [ruleset](https://github.com/Beer-Bears/scaffold/settings/rules/5972646) into main (protected) branch.

### Testing CI (Graph generation & Unit Testing)
[Workflow](https://github.com/Beer-Bears/scaffold/blob/main/.github/workflows/pull-request-conventional-title.yaml)
Checks pr title with conventional rules, because that we use squashing [ruleset](https://github.com/Beer-Bears/scaffold/settings/rules/5972646) into main (protected) branch.

## Deployment

As deployment we do not need any deployment now, but in near future we will create docker image building and publishing into register.

## Vibe Check
<img title="Team vibe picture" alt="Team vibe picture" src="https://i.pinimg.com/736x/51/e7/5e/51e75e2b5cbe03cbdc5abf1b0f097765.jpg">
<img title="Team vibe picture" alt="Team vibe picture" src="https://i.pinimg.com/736x/92/63/c2/9263c2aa91a1440a7a62557e80898b48.jpg">
<img title="Team vibe picture" alt="Team vibe picture" src="https://i.pinimg.com/736x/71/e4/f1/71e4f17c3ee3d02e46c8da1132479437.jpg">

> Now we are feeling exited by project, we are currently adding more and more complex features into project, but feeling a bit tired and overwhelmed with a lot of tasks and deals we need to implement in near future.
 
# Weekly commitments

## Individual contribution of each participant

#### Trunn5
- **Add Pytest**  
  Add pytest framework for testing infrastructure
- **Parse Async Functions**  
  Added support for asynchronous function parsing
- **[Generator] Connect Files to Folders nodes**  
  Implemented file-to-folder mapping in generator component

#### onemoreslacker
- **Essential Integration Tests**  
  Developed core integration tests for critical paths
- **CI: Graph Generation Auto Testing**  
  Set up automated graph testing in CI pipeline

#### peplxx
- **Classical Vector RAG approach**
  Introduce Vector RAG approach in project

#### 4hellboy4
- **Research: Efficiency information search in codebases**  
  Investigating optimization techniques for code search

### mashfeii
- **Week 4 Report**  
  Compiling weekly progress metrics and findings


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).