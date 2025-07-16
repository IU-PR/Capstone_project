# Week #6

## Links

- Deployment: https://looki-app.ru
- API Docs: http://31.57.61.167:8000/docs
- Demo: https://drive.google.com/drive/folders/1qpJOGIswTJbN_ZaWY7nF6p6oM15QxEeB?usp=sharing
- **Source Code**: [GitHub Repository](https://github.com/IU-Capstone-Project-2025/Looki)

## Final deliverables

### Project Overview

**Looki** is an innovative virtual fitting room application that revolutionizes online shopping by:
- Creating accurate 3D body models from user photos
- Providing precise size recommendations across brands
- Enabling realistic virtual try-on experiences
- Reducing clothing return rates by up to 40%

Key implemented features:
- AI-powered body measurement extraction
- Personalized 3D avatar generation
- Size recommendation system
- Virtual clothing try-on functionality
- Cross-platform mobile experience

### Implemented Features

**Core Functionality:**
1. User authentication system (JWT)
2. Photo-based body measurement extraction
3. 3D avatar generation with MakeHuman
4. Size recommendation engine
5. Virtual try-on with basic garment overlay
6. Product catalog browsing

**Advanced Features:**
- Measurement correction interface
- Photo processing
- Brand-specific size charts
- Measurement history tracking
- Responsive Flutter UI

### Tech Stack

**Frontend:**
- Flutter (iOS/Android)
- BLoC state management
- Three.js for 3D rendering
- ObjectBox for local caching

**Backend:**
- Python FastAPI
- PostgreSQL database
- SQLAlchemy ORM
- Redis caching
- Docker containers

**AI/ML Components:**
- MediaPipe for pose estimation
- OpenCV for image processing
- Random Forest models (scikit-learn)
- MakeHuman for 3D modeling

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/IU-Capstone-Project-2025/Looki.git
cd Looki
```
2. Configure environment:

```bash
cp .env.example .env
# Edit .env with credentials
```
3. Build and launch with Docker:

```bash
docker-compose up --build
```
4. Access services:

Frontend: http://localhost

Backend API: http://localhost:8000

Swagger Docs: http://localhost:8000/docs

## Presentation draft

[Presentation](https://www.figma.com/deck/QdBT32ASBFzACl1sjVbvwb/Untitled?node-id=1-42&t=BcZ9r7vWpjeSjSjM-1)

# Weekly commitments

## Individual contribution of each participant

**Ilya Maksimov**  
- Implemented clothing try-on functionality for 3D models  
- Enhanced try_on screen with interactive clothing cards  
- Developed UI for selecting and applying garments to avatar  

**Aleksandr Gavrovskii**  
- Added 3D model generation visualization  
- Implemented model regeneration with new body parameters  
- Redesigned body parameters screen for better UX  

**Nikita Shiyanov**  
- Developed backend clothing attachment functionality  
- Optimized body generation parameters  
- Added new API endpoints for clothing management  
- Updated server-side MakeHuman for clothing integration  
- Implemented clothing-related database operations

## Plan for Next Week

### Frontend Refinement
- UI/UX improvements for clothing selection interface  
- Performance optimization for 3D clothing rendering  
- Enhanced error handling during garment try-on  
- Virtual wardrobe organization system  

### AI Model Development
- Advanced garment fitting algorithms  
- Realistic cloth physics simulation  
- Improved body measurement accuracy  
- **Clothing generation ML model**:
  - Neural network for automatic garment fitting  
  - Style transfer for clothing variations  
  - Size adaptation algorithms  
  - Texture and pattern generation  

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).
