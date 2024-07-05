# Crucial phases of testing, feedback integration, and continuous iteration

## External Feedback

As part of improving the user experience of our web platform, an independent
survey was conducted to gather feedback. The testing focused on evaluating the
intuitiveness and usability of the interface, especially in the context of
creating and editing student room allocations.

### Overall impressions

Most users expressed a high degree of satisfaction with their use of our
platform. Several key aspects were noted:

- **Interface clarity**: Users found the interface clear and logical, making it
  easy to navigate.
- **Intuitiveness of navigation**: The ease of creating new allocations was
  emphasized, indicating efficient user interface design.

### Editing allocations

The page for editing current assignments was specifically tested:

- **Allocation Process**: Testers noted that the progress bar of assigning
  students to rooms was clear and did not cause difficulties.
- **Page Adaptability**: Despite changes in the state of the page during the
  editing process, users had no difficulty understanding the functionality.

### Conclusions

The overall external feedback indicates that the interface development is moving
in the right direction. By paying attention to the details of user interaction,
we can significantly improve the perception and usability of the platform.

## Testing

Our team is actively engaged in the development and improvement of machine
learning and backend components. These efforts are aimed at improving the
efficiency, reliability and scalability of our platform.

### Machine Learning

A novel metric has been devised for evaluation purposes. This metric's valuation
is computed through the average room ratio, the count of subscriptions, and the
utmost feasible number of subscriptions within a designated area. An random
distribution algorithm was selected as the foundational strategy. This algorithm
acted as the foundation for subsequent experiments and analyses.

The examination encompassed three methodologies: spectral clusterization,
spectral clusterization, and the approach utilized by the Louvain Institute.
Each methodology was assessed relative to the benchmark set by the initially
chosen random algorithm. Notably, all three algorithms exhibited a quadrupled -
quintuple efficiency compared to the random algorithm. This enhancement was
attributed to the algorithms' inherent capacity to deliver more precise results.

Despite almost equal results for all three methods, the method of the Louvain
Institute emerged as the superior alternative, albeit marginally, by a few
percentage points. To augment the results further, the decision was made to
integrate greedy logic into the evaluation procedure. Among the three algorithms
scrutinized, this tactic permitted a minor but noteworthy boost in performance,
elevating the metric by 5%. This improvement was considered substantial enough
to justify further exploration.

Ultimately, the method of the Louvain Institute, enhanced with greedy
heuristics, was selected for its potential to yield even superior results.

### Backend

At the moment of Sprint 4, the backend of the system is equipped with 450 unit
tests. The emphasis on unit-testing is not accidental, because it is this type
of tests that allows us to guarantee high quality and stability of the code at
the earliest stages of development. Unit-tests provide checking the correctness
of work of separate modules, which greatly simplifies error detection and
elimination. Thanks to a thorough approach to testing, we can confidently move
forward knowing that our system is reliable and ready for further development.

## Iteration

Continuous iteration plays a key role in the success of our project development.
This process not only involves consistent product improvement through feedback
and testing, but also involves close interaction and collaboration between
different parts of the team. Our approach to iteration includes weekly team
meetings to adjust plans and share experiences, which greatly enhances
development efficiency.

Every week, our team meets to assess current progress and adjust the development
plan. These meetings allow us to share experience and information between the
frontend, backend and machine learning departments, which helps us to better
understand the processes in each area.

The iterative process in our company is unique in that each development area is
not only informed of the actions of other teams, but also actively participates
in discussing and commenting on progress. This creates an environment for
collaborative development, where each team member can contribute to the overall
result.

By regularly evaluating and adjusting our plans and products based on a
collective view and feedback, we not only adapt our products to changing
requirements, but also continuously improve them in pursuit of our original
goals.

# Progress Report

This week our team made significant progress on our key components - machine
learning, backend and frontend.

You can learn about the progress of this sprint, as well as a detailed roadmap,
on our page
[Notion Page](https://www.notion.so/randorm/Week-4-ef7c9e2c7de64821bedf564bff6f7895)

## Challenges and Solutions

**Challenge A**: The machine learning team encountered problems with the initial
performance of the new recommendation algorithm, which did not meet the expected
accuracy and efficiency metrics.

**Solution**: Using real-time performance data, we were able to improve our
models more efficiently.

**Challenge B**: As we migrated the frontend design from Figma prototypes to a
React implementation, maintaining visual and functional consistency across
platforms and browsers was challenging.

**Solution**: The frontend development team has created a common component
library that aligns with our system design principles. This library is
integrated into our development process, ensuring that our user interfaces are
consistent regardless of platform. We also conducted extensive cross-browser
testing to ensure that our designs display correctly in all supported browsers.

### Machine Learning

The machine learning team has completed the development of the recommendation
system algorithm, which has been successfully refined and validated. Future
plans include work on distribution algorithms, which is the second type of
algorithm we will be developing in the coming weeks.

### Backend

Development of the open source GraphQL API in Python continues, with plans to
integrate the Telegram bot into the server in future sprints. This will be an
important step in making our service more interactive and accessible.

### Frontend

In Frontend, the team started implementing the design from Figma on the Next.js
framework. The main focus was on creating a responsive UI that adapts to
different screen sizes and devices.

### Next Steps

Our next steps include:

- **Machine Learning**: Work on the distribution algorithm.
- **Backend**: Integration of the Telegram bot into the server.
- **Frontend**: Continue implementing the design from Figma.

As we continue to follow an iterative approach to development, we have
maintained a high level of motivation and effective communication within the
teams. This week was filled with important accomplishments that prepare us for
the next phases of development. Our goal is to stay focused on the most
significant aspects of the project and ensure its successful completion.
