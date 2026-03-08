# Week 5
## Feedback
### Sessions
#### Participants:
1. Gleb Popov
2. Victoria Gorbacheva
3. Sofia Selyutina
4. Damir Zagidullin
5. Maria Ilyina
6. Matvey Kancerov
7. Konstantin Smirnov

#### User Feedback Highlights

1. *"I really enjoy the modern design - it's clean and intuitive. The book search works instantly, though I wish the header stayed fixed while scrolling. The footer design could be more polished."*

2. *"The reservation concept is great, but I got a 'booking failed' error twice. Also, why can I book the same book multiple times? Email verification during registration would make me feel more secure."*

3. *"Love the visual style! But the filters don't work when I press Enter. A genre dropdown and library/city filters would save so much time. The logo should be clickable to return home."*

4. *"Getting HTTP errors when accessing My Orders (401) and year search (500). The search reset behaves oddly - books don't reappear after deleting my query unless I refresh."*

5. *"The book covers open in new tabs instead of details. An age gate ('Are you 18?') and content tags like 'for teens' or 'animals' would help navigation. Library contacts would be useful too."*

6. *"Password changes lack confirmation messages. The terms checkbox should be mandatory. Overall though, it's much better than most library sites I've used!"*

7. *"The admin features for managers work well, but we need better feedback when editing profiles. Automatic search triggers would improve workflow. HTTP 500 errors need fixing."*


### Analyze
#### Collected Feedback:
**Positive Aspects:**
- Modern and visually appealing design
- Intuitive interface organization
- Useful core functionality for book search and reservation
- Clean and responsive layout

**Functional Improvements Needed:**
1. Header/footer fixes:
   - Sticky header implementation
   - Footer redesign for better aesthetics
   - Clickable LibNet logo redirecting to homepage

2. Booking system:
   - Prevent multiple bookings of same book
   - Fix "booking failed" error messages
   - Add age verification ("Are you 18+?")

3. Search enhancements:
   - Working filters by libraries/cities
   - Genre dropdown list
   - Author search dropdown
   - Fix search reset behavior
   - Enter key support for filters
   - Fix year filter (HTTP 500 error)

4. User account:
   - Email validation/confirmation
   - Required checkbox enforcement
   - Password change notifications
   - Profile update confirmations

5. Additional features:
   - Book tags system ("for girls", "ocean", "animals")
   - Library contact information
   - Technical support contacts

**Technical Issues Reported:**
- HTTP errors on Orders/Favorites pages
- Book cover opens instead of details in new tab
- Search field persistence issues
- Filter activation delays

**General Impressions:**
Users appreciated the project's concept and modern interface, while providing constructive feedback for further refinement. The most praised elements were the visual design and core book search functionality. Critical pain points included filter reliability and booking process clarity.
## Iteration & Refinement
### Implemented Features Based on Feedback

#### UI/UX Improvements
- **Fixed footer overlapping**  
  Resolved text overlapping issues in footer layout
- **Mandatory checkbox**  
  Added required consent checkbox for user registration
- **Streamlined search**  
  Implemented auto-search 
  Added keyboard support (Enter key triggers search)

#### Functional Fixes
- **Year filter correction**  
  Fixed date range filtering logic in book search
- **Booking system stability**  
  Patched error causing crashes during book reservations

#### Future Improvements Based on Feedback
- Add city/library filters to search functionality  
 

### Performance & Stability
### Key Metrics Dashboard
![Request Metrics](https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/main/reports/photo_5438316903803255072_y.jpg)
![Request Metrics](https://raw.githubusercontent.com/IU-Capstone-Project-2025/libnet/main/reports/photo_5438316903803255073_y.jpg)
#### Current Performance 
| Metric                  | Value          | Status  |
|-------------------------|----------------|---------|
| Total Requests          | 624            | ✅ Good |
| Avg. Duration (fastest)| 1.21ms         | ⚡ Excellent |
| Avg. Duration (peak)   | 24.2ms         | ⚠️ Monitor |
| Success Rate (2xx)     | 80-100%        | ✅ Stable |
| Error Rate (5xx)       | 0%             | 🟢 Ideal |

#### Endpoint Analysis
1. **`/docs`**  
   - Consistently fast (1-3ms)  
   - 100% success rate  

2. **`/search/`**  
   - Variable latency (3-24ms)  
   - 80% success rate (needs optimization)  

3. **`/metrics`**  
   - Stable performance  
   - No errors detected  

### Improvement Recommendations
1. **Search Optimization**  
   - Implement caching for frequent queries  
   - Add query timeout protection  

2. **Capacity Planning**  
   - Scale resources if duration exceeds 50ms  


### Documentation
#### Key Documentation Types
1. **Design Specifications**  
   - Comprehensive Figma prototypes: [View Designs](https://www.figma.com/design/PEK6pAX4gh7f5oO9C0jNfq/libnet?node-id=0-1&t=sEVJZ4Fg0AY8jxIw-1)  
   *Purpose: Visual reference for UI/UX consistency*

2. **API Documentation**  
   - Interactive Swagger docs: [API Reference](http://libnet.site:8000/docs)  
   *Purpose: Backend integration guide for developers*

3. **User Flows**  
   - Diagrams covering all user roles (Admin/Manager/Reader)  
   *Purpose: Clarify system navigation logic*

4. **Weekly Reports**  
   - Progress tracking and task accountability  
   *Purpose: Maintain project transparency*

5. **User Stories**  
   - Functional requirements mapped to user needs  
   *Purpose: Ensure feature-user alignment*
### ML Model Refinement
#### Completed Task
- **Data Migration System**  
Implemented automated book catalog migration from multiple formats:    
  ✅ `.csv`  
  ✅ `.json`  
  ✅ `.xls`  
  ✅ `.xlsx`  
  ✅ `.db`
- #### Implementation Details
    Implemented a migration algorithm for book databases (.xls, .xlsx, .db, .json, .csv) into system with library email matching using Ollama.
- #### Validation
    Successfully processed test datasets in:  
  - CSV
  - JSON

### Link to the deployed application
The live demo is publicly available with **standard user access**:  
🌐 [libnet.site](https://libnet.site)  
## Weekly commitments 
### Individual contribution of each participant
| Team Member     | Completed Work                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ivan Murzin     | [Fix scrollbar issue.](https://github.com/IU-Capstone-Project-2025/libnet/commit/1cc3dbd5ca72cebd0a9cabad2ba0161dda49c667) [Style search + filters and making it pretty on mobile devices.](https://github.com/IU-Capstone-Project-2025/libnet/commit/773d1702b19c09112310dfe9edb64402d5ca6c56) [Add coarse media query with button hovering disabled.](https://github.com/IU-Capstone-Project-2025/libnet/commit/1cc3dbd5ca72cebd0a9cabad2ba0161dda49c667) [Centering the books when the device is small (width < 450px).](https://github.com/IU-Capstone-Project-2025/libnet/commit/1cc3dbd5ca72cebd0a9cabad2ba0161dda49c667) [Proper navbar centering.](https://github.com/IU-Capstone-Project-2025/libnet/commit/1cc3dbd5ca72cebd0a9cabad2ba0161dda49c667)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Aliya Sagdieva  | [Updated README roadmap documentation, Added Grafana/Loki logs access instructions.](https://github.com/IU-Capstone-Project-2025/libnet/commit/db5365e197d38cee82d9dba9f1f4090b31d53425) Collected user feedback. Prepared project report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Alena Averina   | [Configured HTTPS implementation.](https://github.com/IU-Capstone-Project-2025/libnet/commit/33dd41c532d9d114a7e078436154d96b41d49cd8) Participated in user feedback collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Anna Serova     | Implemented the following tasks on the frontend: [added book deletion](https://github.com/IU-Capstone-Project-2025/libnet/commit/59e65cbbe8e1c4e2ae8d2a0f8501a65dbad8b1e1),  [added display, adding and deleting managers.](https://github.com/IU-Capstone-Project-2025/libnet/commit/f6467b016d6cf30547e85c934f6b7ff754b81c0d) [Fixed book change issues.](https://github.com/IU-Capstone-Project-2025/libnet/commit/4859ca49cb6e6af4e03b949c03d0db0bb08f7e95) [Implemented role-based access protection.Applied tokens to endpoints.](https://github.com/IU-Capstone-Project-2025/libnet/commit/8f113930f6680b0e9dbbe2e1bcc5bcf9da6bd2a4) [Added navbar and footer for unauthorized users.](https://github.com/IU-Capstone-Project-2025/libnet/commit/80f1108b4e89e5a8d4b4d3529f02a33b3364a1db) [Added unauthorized user notice on book pages.](https://github.com/IU-Capstone-Project-2025/libnet/commit/96635eee9592b5f12f8cb221e25ca48e2dc74e94) [Implemented password change feature.](https://github.com/IU-Capstone-Project-2025/libnet/commit/8cc6778fe50f32e5541a682ea741c760e2dcf19a)[Created book addition functionality.](https://github.com/IU-Capstone-Project-2025/libnet/commit/86f4571ca861c3e272f855b41e0030c962e034b7) [Fixed proper book image loading.](https://github.com/IU-Capstone-Project-2025/libnet/commit/56d0f5b04aa8cd36a60535a0e50b4d129bd732e0) [Improved search functionality.]( https://github.com/IU-Capstone-Project-2025/libnet/commit/4d27256084e774f60841db77f05218a5d8d3c9f1) |
| Artem Ostapenko | [Made an endpoint for password update.](https://github.com/IU-Capstone-Project-2025/libnet/commit/68408460bcf13243f82ba58ef1bfa8bf61fe589c) [Attached token check to endpoints.](https://github.com/IU-Capstone-Project-2025/libnet/commit/2e4b816f31f01636a0f22110580baacee6449d23) [Made a test for password update check. Updated tests for token support.](https://github.com/IU-Capstone-Project-2025/libnet/commit/05fcaaee0afd0dfa0a7f74c95e7f7a417f226c0e)  [Organized an algorithm for migration from different types of other book databases.](https://github.com/IU-Capstone-Project-2025/libnet/commit/5b904b1a8ac913dbdfa87ca55fbdf33fc06f965f) [Added an endpoint for receiving books by user's city.](https://github.com/IU-Capstone-Project-2025/libnet/commit/34913f958bd329ed935589c216d8042767e6a9d0)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 
### Plan for Future

#### Frontend Development
- **Library Management**
  - [ ] Display library contact info (email/phone) for users

- **Catalog Improvements**  
  - [ ] Implement city/library filters  
  - [ ] Add year range slider  
  - [ ] Fix "No books found" display  

- **User Experience**  
  - [ ] Age verification check ("Are you 18+?")  

- **Booking System**  
  - [ ] Add booking cancellation flow  

#### Backlog Tasks
- Publisher field integration  
- Favorite books removal ("No like anymore")  
- Book details loading fix  

### Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md). 

