# Week 6 Report: Final Touches & Presentation Preparation

## Project Links

<div align="center">

| Resource | Link |
|----------|------|
| Deployment | [Ego AI Production Environment](http://egoai.duckdns.org:3000) |
| API Documentation | [Interactive API Docs](http://egoai.duckdns.org:8000/docs) |
|Figma UI/UX Design | [Figma Design System](https://www.figma.com/design/um3jVUbRhCpPOtH0rnKo8D/EGO-AI--Copy-?node-id=0-1&p=f&t=exIR69T2XF2a7Vax-0) |
| Architecture | [System Architecture Board](https://excalidraw.com/#room=0a55400de3e2cf3441c6,bBFRwjpDKsK64Lti2_I28A) |
| Source Code | [GitHub Repository](https://github.com/IU-Capstone-Project-2025/Ego_AI) |

</div>

---

## Final Deliverables

### Project Overview
Ego AI serves as an intelligent personal assistant designed to optimize daily productivity. The platform offers comprehensive task management across daily, weekly, and monthly timelines, complemented by personalized news curation capabilities. This solution aims to become an essential life optimization tool for modern users.

### Key Features
- **Basic calendar features**: Basic calendar system with saving you added tasks
- **AI Assistant Integration**: Groq-powered conversational interface
- **Dynamic Rescheduling**: AI-driven task reorganization
- **Personalized Recommendations**: Context-aware suggestions
- **Location-Based Services**: Geo-specific activity recommendations

### Technology Stack

<div align="center">

| Component | Technologies |
|-----------|--------------|
| **Backend** | Python FastAPI, SQLAlchemy (ORM) |
| **Frontend** | React.js (TypeScript) |
| **Databases** | PostgreSQL (relational), MongoDB (NoSQL) |
| **DevOps** | Docker, Docker Compose, GitHub CI/CD |
| **Version Control** | Git, GitHub |

</div>

### Deployment Instructions
The recommended implementation method is through our production environment:

<div align="center">
  
**[Ego AI Production Deployment](http://egoai.duckdns.org:3000)**

</div>

For development purposes, local execution is possible via Docker Compose. Note this requires proper configuration of environment variables across all services (backend, ML, frontend). Technical documentation for local setup is available in the repository's README.


## Challenge Faced & Lessons Learned  


- CI/CD creation and tests creation
- Auto Deployment script via SHH(now it work via secret keys)
- GitHub merge conflicts(in development process we have a lot of merge conflicts)


## Presentation Materials
<div align="center">

**[Final Presentation Draft](https://docs.google.com/presentation/d/1AMmDY9dipsmXbvNJjZ6g2lNiUU4mzPrBraJWue1M4N4/edit?usp=sharing)**

</div>

---

## Team Contributions

### Individual Commitments (Week 6)

<div align="center">

| Team Member | Contributions | Verification |
|-------------|---------------|--------------|
| Dmitriy Ryazanov | Connect Geo-Search page with backend | [GitHub commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/399e06c7f0c79dc3e2a299efb5a241359f4fb28e) |
| Diana Tsoi | Start connect recomendation page to backend|  |
| Stepan Sarantsev | - Sending UTC model to AI| [GitHub commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/e7bd46e958b36a7e5a3d1df87ed2f647ec54d91c#diff-248830b05d6c69bdff5c0bf1ccd9b2388ca4100ed98431b7cccae9c29ce887cc) |
| Andrey Zhdanov | - Fix AI time zone issue <br> - fix AI language change issue <br> - add readme for ml services | [GitHub commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/6473dfeb80618c9e5c5df9bb0b577858160eb278) |
| Artyom Lapin | Help with creation Draft of presentration| [Google Slides](https://docs.google.com/presentation/d/1AMmDY9dipsmXbvNJjZ6g2lNiUU4mzPrBraJWue1M4N4/edit?usp=sharing) |
| Mikhail Sofin | Increase calendar user expirience | [GitHub commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/11dc05c03e7bec775f9bd4d058dcdeb09ccb2c28) |
| Salavat Zaynulin | • AI chat task creation fixes<br>• Presentation draft development<br>• Week 6 report composition | [GitHub commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/7f63c1b74f8cbf4f7a4417762a2904aeae589fba) <br> [Google Slides](https://docs.google.com/presentation/d/1AMmDY9dipsmXbvNJjZ6g2lNiUU4mzPrBraJWue1M4N4/edit?usp=sharing) |

</div>

---

## Next Steps
1. Finalize presentation materials for Demo Day
2. Conduct final testing and quality assurance
3. Prepare demonstration scenario

## Quality Assurance
The team confirms that:
- The `main` branch contains production-ready code
- The system operates as expected via Docker Compose