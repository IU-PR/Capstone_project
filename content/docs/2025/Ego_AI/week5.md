# **Week #5: Feedback, Iteration & Polishing**  

## Feedback

### Sessions

We conducted independent user testing of the **Ego AI webapp**, collecting insights from real-world usage scenarios. All users who gave feedback preferred to stay anonymous.

**User 1:**
- "AI works great at first but becomes painfully slow during long planning sessions."
- "The assistant sometimes returned completely broken responses that looked like corrupted code."

**User 2:**
- "Scheduled a meeting for 2pm but it appeared as 4am in my calendar. Something broken("
- "I love the smart scheduling, but why can't it sync with my existing Google Calendar?"

**User 3:**
- "I really like Ego AI design, all functions is intuitivly easy."
- "Had trouble finding where to edit scheduled events after creation. I think this function does not exist"

**User 4:**
- "Would pay for a premium version with more customization options."
- "I try to use it in phone but when I open it something gone wrong."

**User 5:**
- "The timezone handling is confusing - it doesn't automatically detect my location."

**User 6:**
- "Love the clean interface, but sometimes text in AI chat stay in bottom of buttons."


### Analyze

Based on user testing, we identified the following issues:

| Issue | Priority | Complexity | Business Impact |
|-------|----------|------------|-----------------|
| JSON in User chat| High | Medium | Critical for backend stability |
| Calendar Time Corruption | High | High | Breaks core functionality |
| Chat History Performance | Medium | Medium | Affects user experience over time |
| UI Overflow in Chat | Medium | Low | Impacts mobile usability |
| Google Calendar Integration | Medium | High | Important requested feature |
|Crossplatfor|Medium|High|Can found users from other platforms|

### Critical Bugs Identified

1. **JSON Transmission Failure**  
   - *Issue*: AI occasionally generated JSON for backend API calls  and send it for users 
   - *Resolution*: Create issuse for fix this problen

2. **UI Overflow in Chat**  
   - *Issue*: Long messages caused text field to overlap with action buttons  
   - *Impact*: Create issuse for fix this problem

3. **Calendar Integration Demand**  
   - *User Request*: Strong interest in Google Calendar synchronization  

4. **Temporal Data Corruption**  
   - *Bug*: AI-generated calendar entries had incorrect time in calendar
   - *Severity*: High (affects core functionality)  

5. **Performance Degradation**  
   - *Pattern*: Chat slowed significantly after 45-60 messages  
   - *Root Cause*: Unoptimized chat history handling, after 50 message AI chat compresed t one message with instructions

6. **Cross platform work**
   - *User request:* Adaptade website for using on mobile devices 

## Iteration & Refinement

### Implemented features based on feedback

All features and bugs founded by user now started to implement/fix. In one week.

 We had anticipated that we would have been prepared for all of these issues. Based on the feedback we have received, we are currently addressing the issue with JSON in our AI chat. The AI is no longer sending JSON to you, now it correctly add the tasks, but rather sending a message indicating which tasks have not yet been added.

The reason for the AI not completing tasks and adding them back to your calendar on time was due to time zone differences. We need to instruct the AI to use the user's preferred time zone for accurate task completion. This issue will be addressed promptly as it is not considered a critical matter.

### Performance & Stability

We noticed significant slowdowns after 45–60 chat messages due to growing chat history. Now after 50 message AI compress chat history to one message.

### Documentation

Readme.md explain how to run Ego.AI in localhost. But Ego.AI now is hosted so we can edit part with starting in localhost like optional.

### ML Model Refinement

We applied improvements to AI behavior:

- Refined system prompts for more reliable JSON output
- Implemented chat history compression logic for better memory and speed balance
- Added post-processing checks to ensure safe calendar entries


# Weekly commitments

## **Individual Contributions**  

| Team Member          | Key Contributions | Links |  
|----------------------|-------------------|-------|  
| **Dmitriy Ryazanov** | Create eondpoints for profile page|  [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/42070176f5c6f89fcdab45636a082dc7a71e3bechttps://github.com/IU-Capstone-Project-2025/Ego_AI/commit/13c83615a747ae41929b01730817055337fe5040) |  
| **Diana Tsoi**       |Integrate recomendations page for code frontend architecture| [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/e00548ef0b4f1c9b7526f22fcf8e79e55d7b75ba) |  
| **Stepan Sarantsev** |improve and fix endpoint for geo position recomendations and for weather| [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/13c83615a747ae41929b01730817055337fe5040) |  
| **Andrey Zhdanov**   |AI improvements, create more base promts in create,add or update task| [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/64b7834fc257c8d787521c0d7bb28e9118ab132c) |  
| **Artyom Lapin**     |Change deployment method, now deployment work with SSH keys| [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/e9ee79c0cfa68c270e4e1117ffc4168ad92fc46a) |  
| **Mikhail Sofin**    |create user profile page| [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/f7c3f4af9c4ecc1016f74475419371c267993ede) |  
| **Salavat Zaynulin** |Write report for week 5, create compressing of AI chat history after 50 message for improving speed of answers| [github commit](https://github.com/IU-Capstone-Project-2025/Ego_AI/commit/2883699ab7f3a6b2e262f1992f38d3fd8dc615e6) |  

---

## Plan for Next Week

1. Fix all remaining known bugs, also founded by users
2. connect Google Calendar
3. Create final presentation

## Confirmation of Code Operability

We confirm that the code in the `main` branch:

- Is fully operational  
- Runs successfully via `docker-compose`

---