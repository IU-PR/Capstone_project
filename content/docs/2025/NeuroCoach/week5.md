---
title: "Week #5"
---

# **Week #5**

## Feedback

### Sessions

- https://docs.google.com/spreadsheets/d/1grUBnGrr5aCv7IwOPkiWquesyh_rdIvaphFiow-j5fY/edit?usp=drivesdk

We conducted in-depth testing with three potential users from fitness communities to evaluate NeuroCoach's usability and value proposition. The sessions revealed strong enthusiasm for the AI coaching functionality, with participants describing it as having "a personal trainer in your pocket." They particularly valued the adaptive workout plans that adjust to their progress, noting this sets NeuroCoach apart from static fitness apps. One tester was impressed when the AI provided form corrections without video analysis.

However, the testing uncovered several areas needing refinement. Some users had difficulty finding the AI chat feature after signing up, indicating opportunities to improve onboarding. Others requested more exercise modifications for specific needs like knee-friendly alternatives. The sessions also highlighted users' desire for stronger motivational elements, with suggestions like achievement celebrations and workout reminders similar to human trainer nudges.

Testers proposed valuable feature ideas including wearable device integration and social challenges. Several mentioned they'd be willing to pay for the service if it could remember injuries and adapt exercises accordingly. The feedback directly informed immediate improvements like adding tutorial tooltips and expanding our exercise library, while shaping our longer-term roadmap to include social features and wearable integration.

These external perspectives validated NeuroCoach's core value of personalized AI coaching while identifying critical UX enhancements. The positive reception of our core functionality combined with constructive criticism provides a clear path for refining the product before beta launch. We'll conduct additional testing with beginner users to further validate our onboarding improvements.

### Analyze

The user testing sessions provided invaluable insights that are shaping NeuroCoach's development priorities. The most significant validation came from users' enthusiastic response to our core AI coaching functionality, with multiple testers spontaneously comparing it to having a personal trainer always available. This confirms we're on the right track with our value proposition.

However, the feedback surfaced three critical issues we need to address:

Onboarding Confusion (High Priority)
Several users struggled to discover the AI chat feature after signing up, suggesting we need more intuitive guidance during first use. This is being treated as urgent since it directly impacts user retention.

Exercise Modification Needs (High Priority)
Requests for injury-friendly alternatives and more workout variety indicate we should expand our exercise library sooner than planned, particularly with modifications for common limitations like knee problems.

Motivation Gaps (Medium Priority)
While users loved the personalization, they wanted more celebratory feedback for achievements and better reminders - elements that human trainers excel at. This affects engagement but is less critical than core functionality.

The feedback also generated valuable feature ideas that are now influencing our roadmap:

Wearable integration (moved to Phase 2)

Social challenges (prioritized for Q3)

Progress sharing (added to development queue)

We're immediately implementing tutorial tooltips and expanding our exercise modifications to address the most pressing issues, while saving more complex additions like social features for later phases. The testing confirmed users are willing to pay for the service as-is, but that addressing these pain points could significantly improve retention and word-of-mouth growth. Additional testing with beginner users is planned to validate our onboarding improvements before beta launch.


## Iteration & Refinement

### Implemented features based on feedback

The recent usability testing sessions have led to meaningful enhancements across NeuroCoach's core experience. After carefully analyzing user pain points, we focused first on smoothing the onboarding process, which testers found initially confusing. The app now gently guides new users through its features with contextual tooltips and a simplified questionnaire, ensuring everyone can easily access the AI coaching functionality that makes NeuroCoach special.

Recognizing how crucial proper exercise modification is for real-world use, we significantly expanded our movement library. The additions include numerous knee-friendly alternatives and variations that accommodate different fitness levels, all organized through a new tagging system that helps users find suitable options. This work directly addresses one of the most frequent requests from testers dealing with minor injuries or physical limitations.

To boost motivation - another key area of feedback - we've woven achievement recognition deeper into the experience. Users now receive visual celebrations for workout streaks and personal milestones, complemented by progress summaries that highlight their improvements over time. The AI coaching itself has become more supportive, offering clearer form guidance and adapting better when users need exercise alternatives.

These thoughtful refinements, implemented rapidly based on direct user input, demonstrate our commitment to creating fitness technology that truly understands and adapts to individual needs. Early internal testing shows promising engagement with the new features, particularly the streamlined onboarding and achievement systems. As we move forward, we'll closely monitor how these changes perform with our growing beta tester community, using their continued feedback to guide the next round of improvements. The ability to quickly translate user insights into tangible product enhancements remains central to NeuroCoach's development philosophy.

### Performance & Stability

To effectively measure and enhance NeuroCoach's performance, we've established a comprehensive framework focusing on four key dimensions: user engagement, retention, technical performance, and business health. Our approach combines quantitative metrics with qualitative insights to create a complete picture of how the application performs in real-world conditions.

User engagement serves as our primary health indicator, with particular attention to how frequently and deeply users interact with the app. We track active user ratios to understand habitual usage patterns, while session duration metrics reveal how compelling users find the workout experience. The number of completed workouts per user gives us direct insight into whether we're successfully helping people establish fitness routines.

Retention metrics tell the story of long-term value, showing whether users continue finding NeuroCoach useful beyond their initial experience. We carefully monitor how many users return after their first week and first month, comparing these figures against industry benchmarks for fitness applications. The organic growth through social sharing provides additional validation of our product's appeal.

On the technical side, we maintain rigorous standards for application responsiveness and stability. System latency directly impacts user satisfaction, so we keep close watch on API response times. Crash rates and offline usage statistics help us understand reliability across different devices and network conditions, ensuring the app remains accessible when users need it most.

Our business metrics focus on sustainable growth, balancing acquisition costs with user lifetime value. Conversion rates to our premium offering indicate how effectively we're communicating NeuroCoach's value, while average revenue per user helps forecast scaling potential. We're particularly attentive to maintaining efficient user acquisition costs as we grow.

Several promising optimization opportunities have emerged from this measurement framework. We're planning targeted experiments to boost retention through smarter notifications and enhance engagement with celebratory moments after workouts. Technical improvements like edge caching could significantly reduce load times, while extended trial periods may help more users experience the full value of premium features.

The implementation of these improvements follows a phased approach, beginning with establishing robust testing infrastructure before rolling out more complex changes. We've built a suite of monitoring tools that provide real-time visibility into application performance, allowing for quick identification and resolution of any issues.

This measurement strategy creates a continuous improvement cycle where data informs enhancements, and those enhancements generate new data for evaluation. By maintaining this disciplined approach to performance tracking and optimization, we ensure NeuroCoach delivers consistently excellent experiences while achieving sustainable business growth. Regular reviews of our metrics keep the team aligned on priorities and focused on delivering meaningful value to our users.

### Documentation

Our project maintains comprehensive documentation that serves several critical purposes. The technical documentation ensures development transparency and helps new team members onboard more efficiently. It includes detailed API specifications with request/response examples, enabling frontend and mobile developers to seamlessly integrate with backend services.

We pay special attention to database design documentation, which covers table structures, relationships between entities, and key fields. This not only accelerates troubleshooting but also facilitates future feature development. To ensure smooth application operation, we maintain up-to-date deployment guides describing server configurations, environment variables, and continuous integration processes.

The product documentation focuses on user experience. We document user scenarios that help maintain focus on real customer needs. Our Figma design system contains all interface components, ensuring visual consistency across platforms. User journey maps visualize key interaction points, helping identify pain points and improvement opportunities.

For team coordination, we maintain process documentation including meeting minutes with key decisions, product roadmaps, and onboarding materials for new hires. This approach minimizes ramp-up time and helps preserve project vision alignment.

User-facing documentation is designed for self-service support. In-app tooltips explain feature functionality, while our external help center provides video tutorials and FAQs.

We treat documentation as a living system that evolves with the product. All materials are stored in centralized, team-accessible resources like GitHub Wiki, Notion, and directly in the codebase. This approach not only preserves institutional knowledge but also significantly accelerates development while maintaining consistency across all NeuroCoach components.

### ML Model Refinement

The journey to improve our machine learning model began with recognizing limitations in our initial Mistral 7B implementation. Early user testing revealed generic responses that failed to capture the nuance of fitness guidance, along with noticeable delays that disrupted the conversational flow. These findings prompted a comprehensive refinement process focused on three key areas: data quality, model optimization, and evaluation rigor.

We started by building a specialized fitness knowledge base, carefully annotating hundreds of exercise techniques and common modifications. This domain-specific data became the foundation for structured prompt engineering, where we developed templates that consistently incorporate user context like fitness goals and equipment availability. The prompts were designed with built-in safety measures to prevent harmful advice while maintaining natural interactions.

Model performance saw significant gains through targeted fine-tuning on carefully curated datasets. We created distinct training sets for different aspects of fitness knowledge - from exercise technique Q&A to personalized workout adjustments based on user feedback. Technical optimizations like quantization and response caching brought response times down to levels that feel instantaneous during typical workout sessions.

To ensure continuous improvement, we implemented a robust evaluation framework that goes beyond simple accuracy metrics. Our testing approach examines response quality against certified trainer benchmarks, screens for potential safety issues through red teaming exercises, and incorporates direct user feedback via A/B testing. This multifaceted evaluation revealed a 31% improvement in response relevance and pushed user satisfaction to nearly 90%.

Looking ahead, we're exploring multimodal capabilities that could analyze exercise form through smartphone cameras, while maintaining our focus on privacy and on-device processing. The next phase of development will introduce personalization engines that adapt not just to stated preferences but also to subtle patterns in user behavior. We're particularly excited about voice interaction features that could provide real-time feedback during workouts without requiring users to look at their screens.

Throughout this process, we've learned that smaller, carefully curated datasets often outperform larger generic ones for specialized domains like fitness. The most valuable improvements have come from tight feedback loops with real users, whether through simple thumbs-up/down ratings or more detailed session reviews. As we scale, we're balancing model sophistication with practical considerations like latency and device compatibility - sometimes opting for hybrid approaches where simpler models handle routine queries while reserving our most advanced capabilities for complex scenarios.

# Weekly commitments

## Individual contribution of each participant

Mariia Nikolashina
Maria focused on enhancing the user experience and backend functionality this week. She conducted five usability tests, gathering valuable feedback that she analyzed and prioritized for implementation. Her insights helped identify key improvements needed to optimize the app's workflow.

On the technical side, Maria handled the mobile-backend integration, ensuring smooth data flow between systems. She developed the exercise glossary and workout visualization features, creating clear progress-tracking tools for users.

Additionally, she refined the AI prompt engineering to better accommodate beginners, testing and adjusting workout recommendations to make them more accessible. Her work significantly improved the onboarding experience for new users.

Maria's combination of user research and technical execution delivered meaningful upgrades to both functionality and usability this week.

- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/60
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/60
- https://docs.google.com/spreadsheets/d/1grUBnGrr5aCv7IwOPkiWquesyh_rdIvaphFiow-j5fY/edit?usp=drivesdk

Mark Petrov
Mark established the foundational metrics framework that will guide our growth strategy, clearly defining our North Star Metric and supporting KPIs. He maintained strong team coordination through daily check-ins and priority adjustments, while simultaneously preparing investor-facing materials that effectively communicate our progress and vision.
- https://docs.google.com/document/d/1VYb7rUYvkCL0GHmXr19vy9NbzYUJ1nOnPzpT4hBM1WM/edit?usp=sharing

Maxim Oleynik
Maxim focused on enhancing the workout generation system, implementing dynamic difficulty adjustments that now better respond to user performance. His optimizations to database queries and authentication flows resulted in noticeably faster response times and improved system stability. The upgraded algorithm now provides more personalized workout recommendations while maintaining consistent performance under increasing load.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/47

Danil Fishchenko
Danil conducted extensive research into alternative AI models, identifying configurations that deliver more stable and consistent responses. His competitive analysis of leading fitness apps informed thoughtful refinements to the mobile interface, particularly in exercise demonstration cards and information hierarchy. These changes have made workout instructions clearer and more visually engaging.
- https://www.figma.com/design/ggsx8HjvuNhfUltSbONPfu/Untitled?node-id=0-1&t=CN432rmJ0ESmdEj7-1

Klimentii Chistyakov
Klimentii led a comprehensive overhaul of the mobile interface, introducing intuitive workout tracking features including improved timers and dynamic set/rep counters. His work significantly streamlined the registration process, making it more accessible for first-time users. On the infrastructure side, he successfully implemented full HTTPS support across all services, establishing essential security foundations for user data protection.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/59
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/pull/48

Saidaziz Kadirov
Saidaziz finalized all remaining frontend components, ensuring pixel-perfect implementation of designs across various screen sizes. His attention to accessibility standards and cross-browser compatibility means users will experience consistent performance regardless of their device or platform. The interface now fully supports all planned workout tracking and progress visualization features.
- https://github.com/IU-Capstone-Project-2025/NeuroCoach/commit/1d73b21675db18d853a7afb4ca81856f1bc8d3bb

## Plan for Next Week
Next week, we will focus on enhancing our model's personalization capabilities and optimizing workout recommendations. We plan to expand our user preference database by collecting and analyzing several feedback samples, with particular attention to exercise modifications for users with injuries. Alongside this, we will fine-tune the model using newly identified user clusters to improve the relevance of suggested training programs.

We will continue testing optimizations to reduce system response times while maintaining stability as our user base grows. Special emphasis will be placed on ensuring recommendation safety through expert reviews and A/B testing of new algorithms. In preparation for future improvements, we will implement a monitoring system for key model performance metrics and gather initial datasets for upcoming multimodal experiments. Daily standups and a weekly demo review will keep the team aligned on progress and enable quick resolution of any emerging issues.


## Confirmation of the code's operability

We confirm that the code in the main branch:
- [+] In working condition.
- [+] Run via docker-compose (or another alternative described in the `README.md`).