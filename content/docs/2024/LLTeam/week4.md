---
weight: 4
bookFlatSection: true
title: "Week #4"
---

---
weight: 4
bookFlatSection: true
title: "Week #4"
---

# **Week #4**

## **Weekly Progress**

During this week, our team has moved towards a fully-functioning MVP.

### Front-end Development

Our front-end developers have made up several website pages. In particular, main page, register and authorization pages have been implemented. Moreover, we integrated all implemented pages with the current version of the API. The user can access the application and interact with our backend application via pleasant and modern interface.

### Back-end Development

We have added the ability to customize banners. When creating a link, the user can upload a banner through the API and attach it to the link. When users will visit the shortened link, they will see the customized banner.
Moreover, you can specify additional settings for link, such as redirect limits, views, expiration date, custom link. They will be saved in the database, and will be supported by the API without the need to change the response schemes. Additionally, we started to implement unit testing to make the process of internal API development more reliable and robust.

## **External Feedback**

We collected external feedback from a group of fellow students. As the website prototype is in active stage of development and refinement, part of the feedback was based on our Figma prototype. After analyzing the feedback, the following points were highlighted:

### Pros

All users liked the broad functionality for link customization. The UX/UI part of the website was, in general, evaluated as visually pleasing, consistent, intuitive and easy to use (7 people). In particular, users appreciated the presence of two color themes (3 people). When users interacted with our frontend prototype, they praised the implemented interface and its convenience. Also, users highlighted the adaptability of header buttons (i.e. users on login page will see only Register button in header and vice versa).

### Cons

Several minor bugs, like unexpected button behavior, were found and fixed. Some users expressed their frustration with the fact that there is no cross in the corner of LinkLink Pro banner (2 users). Also, one of the users found medium priority bug that the header buttons were not adapted to current login status. This bug was carefully inspected and fixed. Moreover, users noticed that there are less features implemented than in Figma prototype and expressed their desire to test them as soon as possible.

## **Testing**

As stated previously, we conducted the tests of Figma and development version of frontend prototypes across the group of students, which was consisting of 10 people. Our team organized one-to-one meetings with users. They evaluated our prototypes through active using and found several bugs and possible areas for the improvement, while our team observed them and documented the issues.
Some users (3 out of 10 from focus group) reported that it would be desirable to add the cross in the corner of the redirect banner.
Moreover, one user noted the adaptability issue of header buttons. They were able to see both Login and Register button in the header of authorization pages, which was confusing fact. To address this bug, we carefully examined this bug and found the solution using state manager of Svelte.
Additionally, during the testing of frontend prototype, 1 user noticed that he was able to set the visit limit to a negative number of users, which is not acceptable nor expected value for this feature. We located this minor bug and fixed it.
In fact, the major part of the users (4 users) reported issues with the link creation form field validation: some fields were having too narrow validation schema. This issue was also addressed and fixed shortly.

## **Iteration**
In conclusion, the first version of frontend and Figma prototype turned out relatively successful. Based on the users feedback, we refined the developed version of the prototype and fixed several bugs. As users expressed their desire to try out new features, this week we plan to finally implement secondary features functionality and leave improvements, testing and bug fixes for the next weeks. We also plan to accomplish DevOps tasks and deploy the application on a remote server.
