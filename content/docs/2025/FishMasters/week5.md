---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

**Session 1: Anna, Marine Biology Student & Fisherman (20)**  
Anna is in her third year studying marine biology, and she’s always in the water—swimming, snorkeling, fishing, and exploring. When she tried out the app, she was genuinely impressed by how well it could identify fish from her descriptions. But she also ran into some real-life issues: “If I get a good look at a fish, the app nails it. But sometimes I just catch a glimpse, or I’m reeling in a fish quickly, and then I can’t remember enough details for it to work.” Anna loved all the info about each species, but she wished it included things like how deep the fish usually live and their conservation status. She also pointed out that offline mode would be a good idea, since she often fishes or dives where there’s no internet.

**Session 2: Alexey, Hobby Fisherman (45)**  
Alexey spends his weekends fishing in lakes and rivers. He took the app out on his trips and gave us some feedback: “This is exactly what I need when I catch something I don’t recognize! But I’d love it if the app could also tell me if the fish is safe to eat, and what the local rules are about keeping it.” He found the app easy to use, but said it needs to be faster—when he’s got a fish on the line, he doesn’t want to wait. Alexey also suggested a way log, so he is fishing on the boat, he could see his path afterwards

**Session 3: Olesya, Fisherman & Aquarium Enthusiast (34)**  
Olesya is an fisherman who also keeps several saltwater aquariums at home and enjoys visiting public aquariums around Moscow. She tested the app both while fishing and with her aquarium and tropical fish. Her feedback: “It’s really helpful for identifying fish I catch, especially the common ones, but it sometimes struggles with rare or exotic species—especially if I can’t give a detailed description.” Olesya appreciated the educational features, but wanted even more—like information on aquarium care, which species are compatible, and breeding tips, both for her catches and her aquarium fish.

### Analyze

Based on the user feedback, we identified several key improvement areas with the following priorities, some of them might be realeased after finishing the main requirments:

**High Priority Issues:**
1. **Identification accuracy with vague descriptions** - Multiple users mentioned difficulties when they could only provide general or incomplete descriptions of the fish.
2. **Processing speed optimization** - Users need faster identification for real-time scenarios
3. **Offline functionality** - Critical for users in remote locations without internet access

**Medium Priority Issues:**
4. **Enhanced species database** - Need to expand coverage of rare and exotic species
5. **Handling ambiguous descriptions** - Improve performance for descriptions that could match multiple species, for example for rare or exotic fish.
6. **Additional fish information** - Add conservation status, habitat depth, local regulations, and aquarium care details

**Low Priority Features:**
7. **Catch logging system** - Personal record-keeping with GPS way of fishing
8. **Regulatory information integration** - Local fishing laws and safety guidelines
9. **Aquarium-specific features** - Compatibility and breeding information for aquarium enthusiasts

## Iteration & Refinement

### Implemented features based on feedback

Based on the user feedback received, we have implemented several key improvements:

1. **Dual Resource Mode System**: Implemented both low-resource and high-resource modes to address performance concerns. Users can now choose between fast processing (low-resource mode using random vectors) and accurate semantic search (high-resource mode using Qwen embeddings).

2. **Comprehensive Timing Metrics**: Added detailed performance tracking throughout the API to identify bottlenecks, including separate timing for text embedding, FAISS search, and metadata retrieval.

3. **Enhanced Fish Information**: Expanded the fish database to include more detailed species information including genus, species, common names, and descriptions to address user requests for more comprehensive data.

4. **Flexible Search Parameters**: Added configurable top-k results and search modes to allow users to optimize for their specific use cases (speed vs accuracy).

### Performance & Stability

We measure application performance using several key metrics implemented in our benchmark system:

**Response Time Metrics:**
- Text embedding generation: Currently averaging 1.2ms per query
- FAISS index search: Averaging 0.45ms for top-5 results  
- Total API response time: Under 6ms for semantic search mode
- Database initialization: 1-2 seconds (low-resource) vs 10-30 seconds (high-resource)

**Accuracy Metrics:**
- Similarity score distribution across 20 test queries
- Current average similarity score: 0.72 for semantic search mode
- Accuracy grades: 68% "good" or better results (>0.6 similarity)

**System Stability:**
- FAISS index synchronization with Qdrant database: 100% synchronized
- Database contains 35000+ fish species with embeddings
- Memory usage: ~2GB for high-resource mode, ~200MB for low-resource mode

**Areas for Improvement:**
- Embedding generation could be optimized with model quantization
- FAISS index could be GPU-accelerated for larger databases
- Caching frequent queries could reduce response times by 30-40%


### Documentation

Our project includes documentation for both frontend and backend. The mobile_app Flutter directory contains a *README* with build instructions, while the back Java backend has its own respective Markdown setup guide. Additionally, we maintain general project documentation on GitHub Pages: [FishMasters Docs](https://iu-capstone-project-2025.github.io/FishMasters/)

### ML Model Refinement

Our ML model has undergone several refinement iterations to improve accuracy and performance:

**Current Architecture:**
- **Embedding Model**: Qwen text embedder for semantic query understanding
- **Vector Database**: FAISS indexing with Qdrant metadata storage
- **Search Strategy**: Hybrid approach supporting both random vectors (fast) and semantic embeddings (accurate)

**Recent Improvements:**
1. **Query Processing Enhancement**: Refined the query embedding process to better handle fish descriptions with multiple characteristics (e.g., "large predatory fish with sharp teeth")

2. **Index Optimization**: Implemented synchronized FAISS/Qdrant indexing to ensure consistency between vector search and metadata retrieval

3. **Dual-Mode Architecture**: Developed resource-adaptive system allowing deployment in both resource-constrained and high-performance environments

# Weekly commitments

## Individual contribution of each participant

Stepan Vagin:
- Build AI endpoint for ml search with functionality:
   - Two modes: low resource and high resource
   - Return of top-k fish based on description
   - Link to [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/113)
- Created script for downloading fish images from FishBaseAPI, also generates list with all fishes with images, preparating it for downloading into the Qdrant, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/128)


Kostya Zimin:
- Create logic and endpoints for getting water points, one water point, change water db and some bug fixes, [issue](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/114)
- Create discussion db, message db, fix water database, [issue](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/29)
- Create discussion with possibility to put message for each fisher, one discussion per one water point:
[issue](https://github.com/IU-Capstone-Project-2025/FishMasters/issues/29)

Ivan Vasiliev:
- Build basic CNN(if we increase amount of data), [Link](https://colab.research.google.com/drive/1FtPluhihg3swVpO5fyCh7DDB7kDe4C5E#scrollTo=SDTDOR6hdtEa)
- Found and analyzed some material on realization of one-shot models(if we have small amount of data),  [Link_1](https://www.geeksforgeeks.org/machine-learning/)one-shot-learning-in-machine-learning-1/, [Link_2](https://github.com/orobix/Prototypical-Networks-for-Few-shot-Learning-PyTorch)
-  Adding few more characteristics to compare different search models, [commit](https://github.com/IU-Capstone-Project-2025/FishMasters/commit/5bc2ae95e6b491c71c1b7b0e176143254fe7dea9)

Kirill Greshnov:

- Add localization support (EN/RU), [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/126)
- Profile photo upload (with backend integration), [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/127)
- My Catch Page in FlutterFlow, [Link](https://drive.google.com/file/d/1Rx2WwKm2HIPMoBhxfIfoHzO7WNDjyxra/view?usp=sharing)

Egor Belozerov:
- create gh pages doc, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/123)
- setup monitoring for 2 servers with new CD jobs, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/117)
can be accessed via [Link](http://capstone.aquaf1na.fun:3000)
user: admin 
pass: 1523

Damir Sadykov:
- Fix profile photo upload, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/125)
- Continue to rebuild design from Figma to Flutter in FlutterFlow

Adel Gaznanov:
- add possibility to upload user's photo in the profile, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/107)
- fix bug with uploading caught fish photo, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/109)
- implement user's score increasing after uploading photo with a caught fish during fishing, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/112)
- create leader-board with all and with best-N users, [PR](https://github.com/IU-Capstone-Project-2025/FishMasters/pull/122)

## Plan for Next Week

- Integrate ML search into the app
- Continue building database for CNN-model
- Adjust requirments of product according to feedback
- Continue building screens from FlutterFlow

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).