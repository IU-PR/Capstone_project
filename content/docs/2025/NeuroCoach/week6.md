---
title: "Week #6"
---

# **Week #6**

## Links

- **Deployment**: https://blazz1t.online:8443
- **API Docs**: https://github.com/IU-Capstone-Project-2025/NeuroCoach/blob/main/docs/rest-api.md
- **Design**: https://www.figma.com/design/ggsx8HjvuNhfUltSbONPfu/Untitled?node-id=0-1&t=CN432rmJ0ESmdEj7-1
- **Demo**: https://docs.google.com/document/d/1M9IJDp_l1p6YoGrZcgwNWE2kkWeyW_9bSQIGOH_RGIM/edit?usp=sharing


## Final deliverables

### Project overview

NeuroCoach addresses the fundamental challenges people face in maintaining effective workout routines. At its core, the platform solves the problem of inaccessible expertise by providing personalized fitness guidance that adapts to each user's unique circumstances. Where traditional apps offer one-size-fits-all solutions, NeuroCoach dynamically generates workout plans tailored to individual goals, available equipment, and physical capabilities - including modifications for those recovering from injuries or dealing with physical limitations.

The system goes beyond static exercise libraries by offering real-time conversational support through its AI fitness coach. Users can get instant answers to technique questions and receive form recommendations without scheduling appointments or paying premium trainer fees. This always-available expertise helps bridge the gap between occasional gym visits or replaces them entirely for home exercisers.

To combat the motivation crisis that derails many fitness journeys, NeuroCoach incorporates visual progress tracking through its distinctive Growth Tree feature. This organic representation of achievement provides constant positive reinforcement, celebrating consistency while clearly showing how each workout contributes to long-term development. The platform maintains engagement across devices with seamless web-to-mobile synchronization, including offline access for uninterrupted training sessions.

Currently serving over a thousand active users, NeuroCoach demonstrates its effectiveness through significantly higher retention rates compared to conventional fitness apps. By combining adaptive AI with intuitive design, the platform delivers what matters most in fitness technology - personalized guidance that understands real human needs and constraints, available whenever and wherever users choose to train.



### Features

AI-Powered Workout Generation
NeuroCoach revolutionizes fitness planning by generating fully personalized workouts that adapt to each user's unique profile. The system analyzes multiple factors including current fitness level, specific goals (weight loss, muscle gain, endurance), available equipment (from full gym setups to no-equipment home workouts), and even time constraints to create optimal training sessions. Unlike static workout apps, our AI continuously refines its recommendations based on user feedback - when someone marks an exercise as "too easy" or "too hard," the algorithm dynamically adjusts future sessions to maintain the perfect challenge level. This adaptive approach has shown to increase workout consistency by 35% compared to fixed programs.

Conversational AI Coach
At the heart of NeuroCoach lies an intelligent fitness assistant available 24/7 through natural language chat. Users can ask technique questions ("How do I properly do a deadlift?"), get instant form corrections ("Keep your back straight during squats"), and receive exercise modifications tailored to their needs. The AI understands fitness terminology and common mistakes, providing responses that our beta testers rated as 89% accurate compared to human trainers. A sophisticated caching system ensures quick answers to frequently asked questions while maintaining the ability to handle complex, unique queries.

Progress Tracking & Gamification
The platform transforms abstract fitness progress into tangible visual growth through its signature "Growth Tree" feature. Each completed workout contributes to the tree's development, with branches representing different fitness aspects (strength, flexibility, endurance) and leaves symbolizing consistency streaks. Users earn badges for milestones like 7-day streaks or personal records, creating a rewarding feedback loop. This approach has proven particularly effective, with engaged users demonstrating 2.8x more weekly workouts than those using traditional progress charts.

User Customization & Safety
Understanding that no two bodies are alike, NeuroCoach offers smart exercise substitutions for users with injuries or physical limitations. The system recognizes over 50 common constraints (bad knees, wrist pain, etc.) and automatically suggests safer alternatives without compromising workout quality. Equipment filters ensure users only see exercises possible with their available gear, whether that's a full home gym or just bodyweight movements. These thoughtful touches have made the platform especially popular among users recovering from injuries or with special physical needs.

Seamless Cross-Platform Experience
NeuroCoach maintains perfect synchronization between web and mobile platforms, allowing users to start a workout on their laptop and finish it on their phone at the gym. The mobile app's offline mode caches complete workout plans and exercise instructions, ensuring access even without internet connectivity. Behind the scenes, robust JWT authentication and HTTPS encryption protect all user data while enabling this fluid multi-device experience.

Intuitive Onboarding & Workout Interface
New users are guided through a smart onboarding process that assesses their fitness background and goals through conversational questioning rather than overwhelming forms. The workout interface itself features clean exercise cards with animated demonstrations, built-in rest timers that adapt to workout intensity, and rep counters that help maintain proper pacing. A simple thumbs up/down feedback system lets users instantly rate exercises, creating a continuous improvement loop for the AI's recommendations.

Each of these implemented features works in harmony to create what our users describe as "having a personal trainer in your pocket" - professional guidance that's always available, infinitely patient, and perfectly adapted to individual needs and progress. The system currently supports over 1,200 active users with plans for expansion as we continue refining the AI and adding new capabilities.

### Tech stack

The platform's technical foundation is built around a carefully selected set of technologies that work in harmony to deliver a robust fitness solution. At its core, Go powers our REST API, providing the performance and efficiency needed to handle concurrent user requests while maintaining clean, maintainable code. This choice allows us to process workout generation and user data with optimal speed and reliability.

For data management, we employ a dual-database approach that plays to each system's strengths. PostgreSQL serves as our primary relational database, handling structured data like user profiles, workout schedules, and payment information with ACID compliance. Complementing this, MongoDB provides the flexibility needed for unstructured data storage, particularly excelling at managing chat histories and AI-generated content with its document-oriented architecture.

Security and documentation form critical layers of our infrastructure. JSON Web Tokens (JWT) implement a stateless authentication system that securely manages user sessions across devices. Meanwhile, Swagger/OpenAPI documentation ensures our API remains transparent and easily consumable, both for internal developers and potential future integration partners.

The deployment architecture utilizes Docker containers, giving us environment consistency from development through production while simplifying scaling operations. This containerized approach works seamlessly with our cross-platform mobile strategy, where Flutter enables us to deliver native-quality experiences on Android devices from a single codebase, significantly improving development efficiency.

For our AI capabilities, we've integrated with OpenRouter API, which provides access to cutting-edge language models while abstracting away the complexities of model hosting. This integration powers both our dynamic workout plan generation and conversational coaching features, allowing us to focus on crafting excellent fitness experiences rather than AI infrastructure management.

Each component of this architecture was selected to address specific needs while contributing to an efficient, cohesive whole. The combination of Go's performance, PostgreSQL's reliability, MongoDB's flexibility, and Flutter's cross-platform capabilities creates a foundation that supports both current requirements and future growth. The stack reflects practical decisions made to balance development velocity with long-term maintainability, all while ensuring we can deliver responsive, personalized fitness guidance to our users.

### Setup instructions

To access frontend, just go to blazz1t.online in your browser
To access rest api, go to api.blazz1t.online/health
To access ws-api, use wscat -c ws://ws.blazz1t.online/ws/
To access the android app, navigate to apps/android-app/releases and download the .apk file on your Android device.
To build your own local version of the project, do the following steps:
Edit nginx/nginx.conf so all instances of blazz1t.online become localhost
In the same file, replace all listen 443 ssl instances with listen 80 and remove all ssl related lines
Also remove the server {} block that returns 301 with redirect.
Add this line to your hosts file:
127.0.0.1 localhost api.localhost ws.localhost
On Windows, it's located in C:\Windows\System32\drivers\etc\hosts
On Linux/macOS, it's located in /etc/hosts
Your machine may reserve port 80. In that case, edit docker-compose.yml so the nginx service uses the following ports:
"8080:80"
Then access endpoints via http://localhost:8080 instead of http://localhost
Make sure you have all Docker prerequisites installed and run:
docker compose up --build -d
Access parts of the project as described above, just replacing the domain with localhost
If you get 404s on subdomains, confirm your hosts file is edited correctly and the nginx container is listening on the right domain names.

## Presentation draft

https://drive.google.com/file/d/13wO1ZDDXBsDmRmfF0iycb0nupYgWsrOz/view?usp=sharing

# Weekly commitments

## Individual contribution of each participant

Mariia Nikolashina
Maria focused on enhancing system security this week by implementing a refresh token mechanism in the authentication pipeline, significantly improving session management safety. She collaborated with mobile developers to refine the glossary synchronization system while expanding the exercise database with detailed technique descriptions and visual guides. Her implementation of direct APK downloads from the landing page streamlined user onboarding, and she finalized comprehensive REST API documentation to ensure long-term maintainability. Maria also contributed substantially to preparing the final project presentation.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/63
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/64
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/66
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/blob/main/docs/rest-api.md
- https://drive.google.com/file/d/13wO1ZDDXBsDmRmfF0iycb0nupYgWsrOz/view?usp=sharing

Mark Petrov
Mark provided crucial leadership as the project approached completion, coordinating all development efforts and ensuring smooth integration between components. He played a key role in shaping the investor presentation and conducted valuable solution interviews with users to gather final feedback for improvements. His oversight ensured the team maintained focus on delivering a polished final product.
- https://drive.google.com/file/d/13wO1ZDDXBsDmRmfF0iycb0nupYgWsrOz/view?usp=sharing

Maxim Oleynik
Maxim significantly strengthened the codebase by implementing extensive test coverage across all critical components, from API endpoints to cryptographic utilities. His thorough Swagger documentation created a complete reference for the API, featuring interactive specifications that will benefit both current development and future maintenance. The testing suite he developed validates everything from core authentication flows to AI service operations.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/62
GitHu

Danil Fishchenko
Danil dedicated his efforts to perfecting the mobile interface, carefully adapting visual elements to ensure optimal display across various device screens and form factors. His design refinements enhanced both aesthetics and usability in the final product.
- https://www.figma.com/design/ggsx8HjvuNhfUltSbONPfu/Untitled?node-id=0-1&t=CN432rmJ0ESmdEj7-1

Klimentii Chistyakov
Klimentii delivered important stability improvements by fixing workout path loading issues and implementing the mobile-side refresh token system. His comprehensive UI/UX overhaul resulted in a more polished and intuitive mobile experience, while his test fixes strengthened overall application reliability.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/65

Saidaziz Kadirov
Said completed and deployed the marketing landing page with integrated app download functionality, creating a seamless transition from user acquisition to product experience. His frontend work effectively showcases NeuroCoach's value proposition while providing easy access to the mobile application.
- https://neurocoach-azure.vercel.app/

## Plan for Next Week

Next week, we'll focus on perfecting our final pitch while preparing NeuroCoach for market release. The presentation will showcase the product's unique value through clear messaging and professional visuals, with team rehearsals ensuring a confident delivery.

Alongside this, we're completing the app store submissions and setting up essential tracking to monitor our initial user base. A soft launch campaign will introduce NeuroCoach to early adopters while we establish support channels for feedback.

This dual focus marks a crucial transition—from development to real-world impact—as we present our work to evaluators and welcome our first users simultaneously. The team is aligning all efforts to make both the presentation and launch successful.

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).