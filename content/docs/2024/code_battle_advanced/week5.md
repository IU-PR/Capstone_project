---
title: "Week #5"
---

# **Week #5**

## **Feedbacks**

- **Feedback collection plan**

Our team is making swift progress in understanding the key points that need to be improved, so before all else, we start using the website and view all the things that make for a bad experience. After that, we plan to conduct a couple of meetings with the people that show the most interest in supporting this project. They should give us insights of what needs to be added or changed to improve the user experience and enhance the possibilities.

The main points that we prioritized during the collection were: the usability of the website, the design of the website, the speed of responses and any general ideas such as abilities and other choices. This appears to have been effective and we plan to keep doing this, as well as create a simple google form for a less personalized approach if we find ourselves unable to keep up with the number of feedback providers. Moreover, these sessions will be the main points of meeting with potential stakeholders. 

The feedback collection will continue as it provides priceless insights as to where to continue our development.

- **Conducted user surveys or feedback sessions**

After conducting the feedback sessions, we have primarily gathered the same information that we already knew or understood from our time using the website:

- The appearance of our website is NOT satisfactory, and should be improved or even overhauled.

- As of currently, it is best to completely omit the missing functionality rather than keep some buttons that do nothing. This was primarily shown when we iterated through the website after the first two sessions and started using it for the third time.

- The website requires a living community. Without contests and tasks, there is nothing to show in the site and the activities, whilst possibly endless, still need to be created by someone. The fact that any admin can create them is very powerful long-term, but there needs to be something to show right now.

- The lack of documentation is severely detrimental to new people learning to use our site for hosting their own contests. Furthermore, there are simply too many buttons and too little explanation on how to use them.

Overall, most people were very enthusiastic about the product’s idea, but strongly reinforced the need to work on the project until it is able to have a low enough entry point. 

- **Analyzing feedback, identifying and prioritizing issues**

After conducting the feedback sessions we have gathered the information necessary to create a roadmap that should improve the project. Most of the results can be seen in the roadmap itself, but here are some of them:

- We should consider asking for experts/outside help in terms of designing the website.

- We need to create contests that could help lure people to use our platform.

- We have to enhance the existing systems, document them, and make them have full functionality.


## **Roadmap**:

| №  | Date          | Milestone                                                                                                                                                        |
|----|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0  | in 1 week     | Allow for contest changes during the contest                                                                                                                     |
| 1  | in 2 weeks    | Team-support                                                                                                                                                     |
| 2  | in 2 weeks    | Finish the main functionality                                                                                                                                    |
| 3  | in 2 weeks    | Create 10 Contests with special activities                                                                                                                       |
| 4  | in 2-4 weeks  | Add a personal account page that is capable of showcasing all resources that a person has created in one place to facilitate a large and reusable resource base. |
| 5  | in 3-4 weeks  | Implement more features for the contest customization                                                                                                            |
| 6  | in 3-4 weeks  | Invite an expert at frontend                                                                                                                                     |
| 7  | in a month    | Allow for a video player                                                                                                                                         |
| 8  | in a month    | Get a partnership with the university                                                                                                                            |
| 9  | in 4-6 weeks  | Rewrite Frontend to NextJS & It is preferable to use Tailwind CSS                                                                                                |
| 10 | in 2 months   | Launch the website                                                                                                                                               |
| 11 | in 3-4 months | Implement addons for contests for further customization                                                                                                          |
| 12 | in 3-4 months | Get a partnership with some schools                                                                                                                              |
| 13 | in a year     | Host a hackathon                                                                                                                                                 |

## **Weekly Progress Report**:

Our team did: 

- Meetings for feedback, that were necessary for the completion of the current report.

- Added timings of completions for judging the solutions.

- Fully implemented the functionalities of widgets so contest creators can now add custom elements to contests.

- Handcrafted a calculator using the widgets that we ourselves created for testing purposes.

- Finished the prototype design of the website. Now all the pages are colored and have a unified theme.

### **Challenges & Solutions**

1. In one of the previous reports we stated that we allowed for java solutions. Well, it turned out that some functionality was still missing. It was concerning to see it during testing of a different part of the judging system, but ended up being reasonably easy to implement.
2. The intricacies of bash are so finicky that it is best to change it as little as possible. Having said that, we need to update it every once and again.
3. Page task.html raised some questions about its implementation: whether it is worth displaying the uploaded task or not. If to display, then what and how to display. There were also issues with parsing the uploaded task from the .md file and integrating it into .html.
4. In creating our widgets, one of the main questions was how would we render them on a website to be somewhat organized and not all in a straight line. The solution was to take inspiration from game engines and introduce alignment boxes that the user can use to order their widgets horizontally or vertically. However, as rendering them on the web application side would require too much overhead, because loading the same modules into it or developing new ones would just bloat the system, rendering of widgets to HTML was moved over to the contest management server, where it could be easily implemented using existing classes and recursion.

### **Conclusions & Next Steps**

In conclusion, we are still iterating through our project, refining it to become something better. The feedback showed that we need to better our system in many ways, but most are centered around users. The most important creation of this week is the roadmap, which makes for a great plan for the future and may allow the team to advance some points faster.

As for the next steps, we still need to add a couple of functions and polish the system to be sustainable for prolonged periods of time, and deploy it to test that. Overall, the main idea of all our upcoming actions are: make an MVP that could last enough to create more insights.
