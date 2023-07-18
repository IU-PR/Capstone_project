---
weight: 1
bookFlatSection: true
title: "Week 5 report"
---

# **Week #5**

Our main objectives this week were to arrange meetings or interviews with stakeholders from Gazstroyprom. In our case, these included the client and our team members. This enabled us to gather feedback on the current version of our product.

In an effort to facilitate efficient feedback collection, we devised a detailed plan. This encompassed defining the specific questions or focus areas for our feedback gathering. We implemented a Google form that included further analysis. This allowed our users to quantitatively evaluate our product and its features.

Here is a link to the [form](https://docs.google.com/forms/d/e/1FAIpQLSdCHSs1JjkzRj7HRddbX6TS6y84ThbMA7eLMgLkHBBu19fXWg/viewform) with detailed instructions for reaching our site.
Our objective was to gather insights into the product’s usability, functionality, and overall user satisfaction.
We meticulously documented the feedback received from our stakeholders, taking care to highlight specific areas for improvement or enhancement. After a thorough analysis of the collected feedback, we identified common themes, patterns, and recurring issues that needed addressing.

The first important insight from the form is that a minority of users desired to have more detailed errors for better understanding of user flow (it concerncs to a person who picked 3 out of 5). This wish was given in the section with additional comments.

![User visual satisfaction plot](/PipeVision/plot_visual.png "Plot").

When it comes to the next questions about functionality, the respondents said that everything is good.

Satisfaction with the product is high enough. Nevertheless, the users are waiting for CV integration to the system. So, some of the grades are influenced by the lack of model recognition.

![User satisfaction plot](/PipeVision/plot_satisf.png "Plot").

Based on the feedback received, we implemented necessary modifications or enhancements to the product, adhering strictly to the project’s development process. For example, now the incorrect file format is triggering an error that indicates it.

![Not image error](/PipeVision/not_image_error.png "Error").

![Type image error](/PipeVision/type_image_error.png "Error").

Notably, one user mentioned a discrepancy in the "date" field under "history," where the time displayed was three hours behind the actual time. Our team added a task to synchronize our server to some NTP server for displaying the correct UTC+3 time to our project management system.

These insights are invaluable and will guide our future enhancements.

Furthermore, our ML engineers made a significant step in CV development. They tested different approaches and deployed the environment for data marking using SVAT. All team members are involved in this process to accelerate data preparation for the CV.

![Sample marking](/PipeVision/sample_marking.png "Marking").

For those of us keen on continuing the project after Capstone, we made time to discuss and refine the product roadmap, taking into account the feedback and improvements identified. Our discussion included potential feature additions for the next few months depending on the decision of Gazstroyprom regarding the involvement of our team in the full-scale deployment of this project.

{{< hint danger >}}
**Feedback**

Good job gathering the feedback. now the feedback you collected is good. but you need t learn more rather than getting just a number.
you can ask them additional question like Why did you chose the number above. this will give you more insight why they pick a number.

you have someone who picked 3/5 -- but do you know why?

Grade 5/5

_Feedback by Moofiy_
{{< /hint >}}
