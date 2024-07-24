---
title: "Week #5"
---

# Week #5

## **Feedbacks**

- **Feedback collection plan**

1. Find people who have sought emergency counseling using a psychologist
2. Set up appointments with 6-7 people.
3. At the meetings, ask them to fake an attack and talk to the AI psychologist as if they needed emergency help.
4. After the meeting, ask them to fill out a feedback form

- **Conducted user surveys or feedback sessions**

This report presents the findings from focus group meetings conducted with seven individuals aged 18-25, who had prior experience with emergency psychologist consultations. The focus groups included both men and women, ensuring a diverse range of perspectives. These discussions aimed to explore the participants' experiences, focusing on the effectiveness, accessibility, and overall satisfaction with the emergency psychological services they received. The insights gathered from these meetings are intended to inform improvements in the provision of emergency psychological care for young adults.

## External testing

Improvements made:

1. **Direct Techniques**: The new system offers clear, concise psychological techniques without unnecessary text, although the advice still tends to be verbose.

![screenshot1](/2024/ClearMind/week5_scr1.png)

1. **Changes technics on the good level**

![screenshot2](/2024/ClearMind/week5_scr2.png)

What to improve in the future:

1. **Persistent Issues**: Similar to the older version, the system continues to crash on specific sensitive terms.

![screenshot3](/2024/ClearMind/week5_scr3.png)

![screenshot4](/2024/ClearMind/week5_scr4.png)

1. **Handling Suicidal Content**: Initially, suicidal messages were overlooked, but the system now recognizes and responds to them, albeit not consistently.

![screenshot5](/2024/ClearMind/week5_scr5.png)

![screenshot6](/2024/ClearMind/week5_scr6.png)

1. **Verbose Messages**:Advice is often buried at the end of lengthy messages, reducing its impact.

![screenshot7](/2024/ClearMind/week5_scr7.png)

1. **Context Memory**: The system struggles to maintain context after several messages, leading to a disjointed conversation flow.

Possible improvements:

**Apologies**: There is a repetitive pattern of apologies from the system, which users found unnecessary.

**Lack of Initial Explanation**: There was a consensus on the need for a welcoming message explaining the purpose and functionality of the system.

**Text Generation Visibility**: Users suggested adding a feature to show when text was being generated to set the right expectations.

- **Analyzing feedback, identifying and prioritizing issues**

We have the following feedback in the form

![screenshot8](/2024/ClearMind/week5_scr8.png)

![screenshot9](/2024/ClearMind/week5_scr9.png)

![screenshot10](/2024/ClearMind/week5_scr10.png)

![screenshot11](/2024/ClearMind/week5_scr11.png)

![screenshot12](/2024/ClearMind/week5_scr12.png)

Analyzing the feedback received, the issues can be categorized and prioritized based on their potential impact on user experience and system functionality. Here's a structured analysis and prioritization:

**High Priority Issues**

1. **Persistent Issues (Crashing on Sensitive Terms)**: System stability is critical, especially for an emergency consultation platform. Crashing during interactions can deter users from relying on the system when they need it most. This issue is paramount and should be addressed first to ensure the system's reliability.
2. **Handling Suicidal Content**: Given the sensitive nature of the system’s purpose, inconsistent responses to suicidal content can have serious ramifications. Improving the system's ability to consistently and appropriately handle such messages is crucial for user safety and trust.
3. **Context Memory**: The system's inability to maintain context can lead to a fragmented conversation flow, significantly diminishing the user's experience and the relevancy of the system's support. Enhancing memory capabilities will improve personalized interactions and user satisfaction.

**Medium Priority Issues**

1. **Verbose Messages**: The effectiveness of communication is key in psychological support. Lengthy messages that bury vital advice can undermine the usefulness of the system’s guidance. Streamlining responses to deliver concise and impactful advice should be prioritized to enhance clarity and actionability.

**Lower Priority Improvements**

1. **Apologies**: Reducing unnecessary apologies can help make interactions with the system feel more natural and less repetitive. This is more about refining the conversational tone and is less critical than functional issues but still important for user experience.
2. **Lack of Initial Explanation**: Adding a clear introductory message explaining the system’s functionalities can set proper expectations and enhance user orientation when they first interact with the system.
3. **Text Generation Visibility**: Showing when text is being generated might help manage user expectations about response times and system activity. While beneficial for transparency, this feature is less critical than those directly impacting the quality of support and advice.

**Additional User-Requested Features**

- **Diverse Responses for Different Issues**: Enhancing the system to provide varied responses based on the specific problem presented can greatly improve the relevance and helpfulness of the advice given.
- **Continued Dialogue**: Allowing the system to not only respond once but continue the dialogue based on user feedback or follow-up questions can create a more engaging and supportive

## **Roadmap**

| Timeframe | Q3 - Q4: by Jan, 2025 | Q1: by April, 2025 | Q2: by July, 2025 | Q3: by Oct, 2025 |
| --- | --- | --- | --- | --- |
| Milestone | MVP | MVP | MMP | MMP |
| Goals/Challenges | Develop effective algorithm for selecting a crisis technique | Increase product visibility and awareness | Improve User Experience and Interface Design, Expand Database for Better Personalization | Prepare for Full Launch, Ensure Long-term Sustainability and Support |
| Metrics | Functional AI providing initial therapy sessions | Coverage in at least 3 major educational institutions | 500+ registered users | User satisfaction score above 80% |
| Features | Advanced selecting algorithm | Detailed analytics dashboard for user interactions | Marketing campaign  | Regular updates based on user feedback |
|  | User testing and feedback collection | Advanced emotional intelligence capabilities | Integration with emergency support services | Develop partnerships with universities and mental health organizations |

## **Weekly Progress Report**

### **Backend & ML**

---

**Backend part:**

This week, we successfully deployed our enhanced backend on Azure and ensure it has scalable infrastructure to support our chat-based LLM agent. This deployment allows us integration with our frontend user chat and enables real-time interactions and efficient case handling. The backend now handles user inputs and processes them through our machine learning pipeline ensures that the system can handle multiple concurrent users without compromising performance.

**ML part:**

On the machine learning side, we developed a new LLM agent designed to enhance the user experience by generating embeddings for user messages. This agent uses these embeddings to identify the most appropriate psychological technique from a prepared CSV file of techniques that we will use. In the absence of context, the agent selects a technique. Once a technique is identified, the agent uses it as a system instruction and retrieves relevant paper from our database, which contains detailed papers of each technique in pdf format. This RAG system ensures that users receive contextually relevant guidance and significantly improves psychological aid provided by our product. For building our system we used LangChain.

### **Frontend & Design**

During this week, we mainly focused on doing the welcome page and signing in with Google. The work is still in progress, yet we have implemented the main functions and structure and we only have some minor problems to solve and we also have to implement design with CSS. Overall, the planned work is done for the week.

### **Challenges & Solutions**

### **Backend & ML**

**Backend part:**

One of the primary challenges we faced in the backend development was to ensure that our backend system continued to function even if the server terminal was closed. This issue was critical because it affects our users experience and system reliability. So, we implemented background processing which allowed our backend services to run independently of the terminal session.

**ML part:**

In the machine learning aspect to select the most suitable LLM was a major challenge. We tested several models, including Mistral and Cohere, but faced difficulties in achieving satisfactory user interaction. Finally, we chose gpt-4o due to its superior performance in user interactions. Another challenge was accurately identify the correct psychological technique from user messages. The current embedding comparison sometimes selects multiple techniques from our CSV file (database of technics descriptions), making it difficult to determine the precise technique to use. So, we will continue to work on that issue on the next week and will make the choice of particular technic more precise.

### **Frontend & Design**

The main challenge was to implement the sign in with Google function, as we’ve never worked with it before and it was our first experience. As a solution we did our research and implemented it in fronted code.

Another challenge was to create connections between the welcome page and the dialogue window. The user can’t send anything if they’re not signed in, and we had to somehow create a function that controlls the process. Yet we succeeded.

Design part:

On this week we seriously think about should we have log in or not. We have a lot of pros and cons for this question. All in all, we decided that we would have a log in.

### **Conclusions & Next Steps**

All in all, this week we have some challenges but we solve most of them. We did roadmap for our project and now we can understand what we will do further. Main problems in ml part solved and continue work.

Our next steps will be finish welcome page in frontend part and continue working on the ml part to satisfy comments after feedback.
