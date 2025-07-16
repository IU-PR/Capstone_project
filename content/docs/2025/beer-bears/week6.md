---
title: "Week #6"
---

# **Week #6**

## Links

- **Docs**: [README](https://github.com/Beer-Bears/scaffold/blob/main/README.md)
- **Design**: [Design Schema Excalidraw](https://excalidraw.com/#json=8DxFWGT66eisYHShw5etd,FTPXATItDi33jkpVtVr54A)
- **Demo**: [Google Drive Video](https://drive.google.com/file/d/1ox1fetxowuctBUm16TeusSQT7uAzJuvs/view?usp=sharing)

## Final deliverables

### Project overview

*Describe your project, what problems it solves and what key features it has (only those that are implemented).*

### Features

  - Python Codebase Parsing
  - Code Entities Graph Generation
  - Vector Embedding Indexing
  - MCP tool for searching code-node information

### Tech stack

 - Python 3.10
 - PyTest
 - FastMCP
 - llama-index
 - Neo4j (neomodel)
 - ChromaDB

### [Setup instructions](https://github.com/Beer-Bears/scaffold/blob/main/README.md#startup)

```
## Create .env:
cp .env.example .env  # Replace variables if you wish

## in the __main__.py set the path to your python project
PROJECT_PATH = "./codebase"
## or put some python files to the `codebase` directory

## Run the app.
docker-compose up

## Cursor setup:
## Add mcp server into the mcp.json:

{
  "mcpServers": {
    "scaffold-mcp": {
      "url": "http://localhost:8000/mcp"
    }
  }
}

## Look at graph
## Neo4j webui with creds from .env:

http://localhost:7474/
```

## Presentation draft

[Presentation Draft In Figma](https://www.figma.com/slides/mxkeotWt8NB9TiCsLROgfV/Product-Review?node-id=1-848&t=Hr5DLigf77WcQexo-1)

# Weekly commitments

## Individual contribution of each participant

| Team Member                            | Contributions                                                                                        |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| **Sergei Melnikov (@peplxx)**          | Implemented vector-based RAG pipeline and docker‑compose profiles; added vector RAG to MCP response  |
| **Sergei Razmakhov (@onemoreslacker)** | Developed Graph-Based Context Fetching for MCP; introduced `.scaffoldignore` file                    |
| **Dmitry Prosvirkin (@dmitry5567)**    | Maintained and refined graph database logic, code parsing                                            |
| **Timofei Mashenkov (@mashfeii)**      | Prototyped the MCP interface; researched Signal integrations                                         |
| **Sergei Glazov (@pushkin404)**        | Conducted QA and user sessions; updated onboarding documentation                                     |

## Plan for Next Week

 - Docker image
 - Fine tuning system prompt
 - Parser Fixs
 - Publish on https://mcp.so/
 - Presentation

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).
