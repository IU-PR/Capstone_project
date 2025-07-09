---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

We conducted three user feedback sessions with 1st- and 2nd-year students working on summer software engineering projects.

**Session 1: Nikita (2nd year student)**
- Working on a Python-based project involving API development, machine learning, and DevOps practices.
- Found the core idea of a living knowledge graph compelling and tested Scaffold on his own project.
- Noted some bugs during usage and ultimately decided not to integrate it fully at this stage.
- Expressed interest in adopting it later once the system becomes more stable.

**Session 2: Veronika (1st year student)**
- Found the concept very accessible and engaging.
- Together with her team, visualized the structure of their small project using Scaffold.
- Identified a few opportunities for refactoring based on the generated graph.
- Did not use the MCP interface, but mentioned that the visual structure alone provided clear value.

**Session 3: Maksim (2nd year student)**
- Working on a monorepo project using TypeScript and Node.js.
- Was interested in the tool but could not try it meaningfully because Scaffold currently supports only Python.
- Expressed strong interest in multi-language support, especially for JavaScript/TypeScript, and noted that understanding cross-package dependencies is a real challenge in his stack.

### Analyze

**Key Insights:**
1. High demand for automated context extraction during onboarding (High Priority).
2. Users need better documentation for internal concepts (High Priority).
3. Interest in infrastructure-level code understanding (Medium Priority).
4. Integration with CI/CD is a clear direction for future iterations (Medium Priority).

We created and prioritized tasks accordingly:
- Improve beginner-facing docs and onboarding (#docs-onboarding)
- Prototype infrastructure knowledge extraction (#infra-parsing)
- Simplify terminology explanations in docs (#doc-glossary)

## Iteration & Refinement

### Implemented features based on feedback

- Improved AST parsing: added more robust handling of imports, class structures, and ignored files via `.scaffoldignore`.
- Integrated initial version of the MCP (Model Context Protocol) interface for connecting AI agents to external systems.
- Added basic infrastructure config parsing (Dockerfile and docker-compose) into the parsing system.
- Simplified onboarding documentation with visual walkthroughs and clarified key terminology (e.g., MCP, Signal Interface).
- Continued development of the Signal Interface prototype for triggering workflows from context graph updates.

### Performance & Stability

To measure performance, we focused on:

- **AST Generation Time**: Measured average time to parse and convert files into abstract trees.
- **Graph Insertion Speed**: Time taken to push entities into the graph database.
- **Context Fetch Latency**: Time to retrieve relevant subgraphs or vectors for a user query.

Current benchmark results (small codebase):
- AST Generation: ~1m/codebase
- Graph Insert: ~30ms/codebase
- Context Fetch: <200ms/query

### Documentation

Types of documentation:

- `docs/research`: Detailed reports and experimental notes.
- `docs/docmost`: Configuration and setup for documentation generation.
- `README.md`: Project overview, links.
- `Schemas/`: Structured documentation of internal architecture, interfaces, use cases.

This structure supports onboarding, development, and research directions simultaneously.

### ML Model Refinement

Not applicable in Week #5 – focus was on MCP integration, AST parsing, and GraphRAG enhancements.

# Weekly commitments

## Individual contribution of each participant

| Team Member         | Contributions |
|---------------------|---------------|
| Sergei Melnikov (@peplxx) | Implemented vector-based RAG pipeline and docker-compose profiles |
| Sergei Razmakhov (@onemoreslacker) | Continued work on Graph-Based Context Fetching for MCP |
| Dmitry Prosvirkin (@dmitry5567) | Maintained and refined vector/graph database logic |
| Timofei Mashenkov (@mashfeii) | Prototyped the MCP interface and researched Signal integrations |
| Sergei Glazov (@pushkin404) | Conducted QA, user sessions, and updated onboarding docs |

## Plan for Next Week

- Finalize MCP <-> Graph interface with automatic signal triggers.
- Implement AST-based use case extraction.
- Improve `.scaffoldignore` coverage and performance.
- Begin benchmarking on larger repositories.
- Start prototype for infrastructure knowledge extraction.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
