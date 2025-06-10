---
title: "Week #1"
---

# Week #1

## Project description

### Project name: Scaffold

**Code repository**: https://github.com/IU-Capstone-Project-2025/LINK_TO_YOUR_REPOSITORY <- ????

Scaffold is a temporary structure used to support a work crew and materials to aid in the construction, maintenance and repair of buildings

Our Scaffold is a code management system designed to translate and maintain source code as a graph in a graph database,
enabling seamless context injection for large language models (LLMs). And helps AI agents in construction, maintenance and repair of your project.

### **Team Members**

| Team Member     | Telegram Alias   | Email Address           | Track         | Responsibilities                          |
| :-------------- | :--------------- | :---------------------- | :------------ | :---------------------------------------- |
| Melnikov Sergei        | @peplxx        | s.melnikov@innopolis.university        | Project Owner       | Team Management, RAG Algorithms |
| Razmakhov Serhei      | @onemoreslacker       | s.razmakhov@innopolis.university         | Developer      | Languages parsers, AT Generation |
| Prosvirkin Dmitry | @dmitry5567          | d.prosvirkin@innopolis.university          | Developer        | Vector, Graph Database Management|
| Mashenkov Timofei  | @mashfeii       | t.mashenkov@innopolis.university      | Developer  |  Context Fethcing Algotihm |
| Glazov Sergei      | @pushkin404          | s.glazov@innopolis.university       |  QA        | QA Research, MCP Analysis|

## Brainstorming

### Ideas during brainstorming

*Put here your ranked ideas with short description*

### Brief market research / problem validation

*Put here a brief market research/problem validation for 1–2 ideas*


## Basic requirements

Parse code into AST and build code graphs

Store in a graph DB (e.g., Neo4j) and vector DB (e.g., Qdrant)

Extract structural/code entity relationships (calls, imports, etc.)

Provide API/CLI for context queries

Support incremental updates (e.g., Git hooks or file watchers)

Enable context injection into LLMs (RAG)

Basic testing and validation tools

### Target users and their primary needs

Developers	Understand and refactor code faster using AI and graph context
AI Engineers	Provide structured context to LLMs for better accuracy
Tech Writers	Auto-generate or update documentation from code structure
QA Engineers	Understand dependencies and test impact of code changes

### User stories

As a developer, I want to find all references to a function to safely rename it.

As an AI engineer, I want structured code context to improve RAG results.

As a tech writer, I want to auto-generate docs from code relationships.

As a QA engineer, I want to trace service dependencies for better test coverage.

### Initial scope

Python code parser → graph + vector DB

Neo4j + Qdrant integration

Basic API/CLI for context lookup

LLM context injection (early RAG prototype)

CLI tool for developers

Basic graph update system (e.g., file watcher)


## Tech-stack

Python – Widely used in AI and tooling; ideal for building parsers, integrating LLMs, and rapid prototyping.

Neo4j – Purpose-built graph database optimized for modeling and querying complex code relationships.

VectorDB (e.g., Qdrant) – Enables high-performance semantic search over embedded code/document chunks.

Docker – Provides consistent, containerized environments for development, testing, and deployment.

LLM Chain (e.g., LangChain) – Modular framework for orchestrating Retrieval-Augmented Generation pipelines.

# Weekly commitments

## Individual contribution of each participant

Melnikov Sergei - brainstorming, repository, informtaion research
Razmakhov Serhei- brainstorming, repository
Prosvirkin Dmitry - brainstorming, writing report 
Mashenkov Timofei - brainstorming, informtaion research
Glazov Sergei - brainstorming, writing report

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
