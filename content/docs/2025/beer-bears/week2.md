---
title: "Week #2"
---
# Week #2 (Jun 12 - Jun 18)

## Detailed Requirements Elaboration

This week focused on establishing Scaffold's core technical foundation through detailed requirements specification. We defined and implemented: 
- (1) **Graph entity schemas** (Nodes, Relationships, Tags, Metainfo) to structurally represent code components and their dependencies; 
-   (2) **AT Generator specifications** for transforming parsed code into srtuctured database; 
-   (3) **Database configuration requirements** ensuring Neo4j compatibility for graph persistence; 
-   (4) **MCP interface standards** create interface for llm inregration;
-   (5) **Testing infrastructure** create Python projects test group, research now to setup pipeline for context fetching technique.
### Prioritized backlog

[Scaffold Planning Board](https://github.com/orgs/Beer-Bears/projects/1)

## Project specific progress

### Software Development

- Database configuration (#6) - Done (Trunn5)
- AT Generator (#11) - Done (Trunn5, onemoreslacker)
- Parser for Python project (#9) - In Progress (onemoreslacker)
- Define Graph Entities: Nodes, Relationships, Tags, Metainfo (#10) - Done (Trunn5, peplxx, onemoreslacker)
- Simple MCP interface (#18) - Pull Request (mashfeii)

### Management
- Project Roles for points evaluation (#31) - Done (peplxx)
- Setup Planning Board (#27) - Done (Trunn5, peplxx)
- Update project README (#30) - Done (peplxx)
- Week 2 Report (#25) - In Progress (peplxx)

### Research
- Research: How QA pipeline will be setup (#12) - Done (4hellboy4)

### DevOps & Infrastructure
- CI: Pull Request Conventional Checker (#38) - Done (peplxx)
- Setup Dependabot for project (#42) - Pull Request (peplxx)

### Testing
- Create testgroup with python projects (#33) - Done (peplxx)

# Weekly commitments

## Individual contribution of each participant
- **4hellboy4**: 
  - Researched and finalized QA pipeline setup (#12)
- **peplxx**: 
  - Updated project README (#30)
  - Defined project roles for points evaluation (#31)
  - Setup CI Pull Request Conventional Checker (#38)
  - Created Python project testgroup (#33)
  - Setup Planning Board (#27) with Trunn5
  - Defined Graph Entities (#10) with team
  - Setup Dependabot (#42) - PR
  - Preparing Week 2 report (#25) - In Progress
- **Trunn5**: 
  - Configured database system (#6)
  - Developed AT Generator (#11) with onemoreslacker
  - Setup Planning Board (#27) with peplxx
  - Defined Graph Entities (#10) with team
- **onemoreslacker**: 
  - Developed AT Generator (#11) with Trunn5
  - Developing Python project parser (#9) - In Progress
  - Defined Graph Entities (#10) with team
- **mashfeii**:
  - Developed Simple MCP interface (#18) - PR

## Plan for Next Week

1. **Implement full MCP server** with needed llm integration
2. **Integrate MCP server** with Python pasrser and Neo4j database  
3. **Research signal interface** for Database refreshing mechanism.  
4. **Develop autotesting setup** for parser and AT generator components  
5. **Implement testing pipeline** for context fetching evaluation metrics  
6. **Establish QA framework** for graph accuracy validation

## Usefull Links

 - [Course Repository](https://github.com/IU-Capstone-Project-2025/scaffold)
 - [Main Repository](https://github.com/Beer-Bears/scaffold)

- [Excalidraw Board](https://excalidraw.com/#json=DNp6vtk7Ps-d8IqUnFX5p,F8fM6s7Bx-8FcoYoUmuDmA)

- [Google Document](https://docs.google.com/document/d/1K4CPKvia2kNnlKm9MNFnxmQRqHM1KS_lJMJzueEnQVE/edit?usp=sharing)

- [Weekly Report](https://github.com/Beer-Bears/beer-bears/tree/master/content/docs/2025/beer-bears)

- [Weekly Role Distibution Table](https://docs.google.com/spreadsheets/d/1uc_GRhpqoXTGrU90zRO2Lp6TWDvCVzt__PE6KlVH9DU/edit?gid=0#gid=0)

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).