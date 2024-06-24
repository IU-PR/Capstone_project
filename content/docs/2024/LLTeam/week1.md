---
weight: 1
bookFlatSection: true
title: "Week #1"
---

# Week #1

## **Team Formation and Project Proposal**

### **Team Members**

| Team Member        | Telegram ID   | Email Address                      |
| ------------------ | ------------- | ---------------------------------- |
| Evgeniy Anisov     | @anijack      | e.anisov@innopolis.university      |
| Maksim Kamenetskii | @Elonnmax     | m.kamenetskii@innopolis.university |
| Munir Khisamov     | @Monitor_PC   | m.khisamov@innopolis.university    |
| Roman Pogrebnyak   | @ropero_2     | r.pogrebnyak@innopolis.university  |
| Polina Moiseeva    | @hesterika    | p.moiseeva@innopolis.university    |
| Daniil Nikulin     | @JustDanman   | d.nikulin@innopolis.university     |
| Marat Akhmetov     | @Leflop_James | m.akhmetov@innopolis.university    |

### **Value Proposition**

#### Identify the Problem

Existing URL shortening services offer users limited functionality for their analytics and management, which significantly limits the potential of this useful marketing tool.

#### Solution Description

We are going to create a service with shortening links as its main, but not only feature. Further customizing the shortened links, analyzing the statistics and monetization will be possible. The features could be:

1. Advanced statistics for the URLs, e.g. referrer sites, geographical distribution, time distribution
2. Customizing the expiration time of URLs
3. Customizing the redirects limit of URLs
4. Adding pass code protection to the URLs
5. Adding info (or advertisement) banners before the redirect

#### Benefits to Users

Our advanced link shortening service can provide users with several valuable features. Users will be able to create custom easy-to-remember URLs, making links more attractive and shareable. Also, they will be able to track how many people click on their links and see details like visit times and user locations. Not only that, users will be able to set expiration dates or limits on clicks, add password protection for extra security, and include advertisement banners to monetize the URLs.

#### Differentiation from existing solutions

As already mentioned, existing services do not provide URL customization, advanced statistics, expiration limit, or passcode protection.

#### User Impact:

Using our service can help the marketing mechanics of companies to use such a tool more flexibly.

#### User Testimonials or Use Cases:

One of our team members is developing his own product, and if such a service as we offer existed, he would be able to automate part of the business logic in this product, which would bring a reduction in spending on some manipulations by marketers. 

## **Lean Questionnaire**

1. What problem or need does your software project address?

   Our link shortening service makes long, complex URLs shorter and easier to share. It also offers extra features like custom links, tracking stats, expiration dates, password protection, and ads, which help users manage their links better and even make money from them.

2. Who are your target users or customers?

   Any internet user who wants to share links online will be able use our service. However, the target customers are businesses and content creators.

3. How will you validate and test your assumptions about the project?

   The number of uses of features will be a decisive factor in validating assumptions about our project.

4. What metrics will you use to measure the success of your project?

   The success of the project can be measured by looking at the number of users who use the service, how many links they create, and how often the links are clicked.

5. How do you plan to iterate and pivot if necessary based on user feedback?

   To ensure that the project meets the users' needs, we will collect user feedback using Google form surveys. We may adjust the functionality by removing or adding certain features based on user feedback.

## **Leveraging AI, Open-Source, and Experts**

Our team may leverage open-source code to enhance development efficiency. We may also use LLMs to generate some parts of the code. At the moment, we do not plan to consult experts or involve students from other teams.

## **Defining the Vision for Your Project**

#### Overview

The link shortening service will be presented as a website. The functionality can be described as follows: the user pastes the original link, checks the features that they would like to use, and gets a shortened link. We also consider a possibility of implementing a telegram bot with the same functionality.

#### Schematic Drawings

The following model describes the service architecture:

![C4 Diagram](/2024/LLTeam/week1/c4.jpg)

#### Tech Stack

The following list describes the technologies that will be used in the project, although adjustments may be made:

- Frontend: SvelteKit
- Backend: Python, FastAPI
- Database: PostgreSQL
- Telegram Bot: Python, Aiogram
