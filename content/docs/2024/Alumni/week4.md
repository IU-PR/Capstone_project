---
title: "Week #4"
---

# Week 4 Report: Alumni Portal

**Authors:** Chulpan Valiullina, Nazgul Salikhova, Liubov Smirnova, Anzhelika Akhmetova, Olesia Grediushko, Galia Shabanova, Anastasiia Ozerova

![logo_design](/2024/Alumni/logo_design.png)

## Table of Contents
1. [Introduction](#introduction)
2. [Progress](#progress)
   - [Donation page](#donation-page)
   - [Main page](#main-page)
3. [System Updates](#system-updates)
4. [Testing](#testing)
5. [External Feedback](#external-feedback)
6. [Priorities](#priorities)
7. [Plans for the next week](#plans-for-the-next-week)

## Introduction
This week, we completed the donations page for alumni, wrote several tests, and developed the main page's frontend. We also overcame various obstacles related to integrating all pages into a single portal using Django.

## Progress
### Donation page
After a meeting with the Alumni Relations Department (319), we learned that the alumni club needs to raise funds to implement its plans within the club. In response, we have created a donations page. This page includes a form validation feature, ensuring that certain fields must be filled out before proceeding. If these required fields are not completed, a message saying "fill in this field" will appear, prompting the user to provide the necessary information. After successfully filling out the form and making a donation, the user is redirected to a thank you page, expressing our gratitude for their contribution.

![donation](/2024/Alumni/donation_1.jpeg)

![donation](/2024/Alumni/donation_2.jpeg)

![donation](/2024/Alumni/donation_3.jpeg)

![donation](/2024/Alumni/donation_4.jpeg)

### Main page
For the main page, we have made several key improvements:
- Replaced the logo with an updated version.
- Converted all PNG files to SVG format for better scalability and performance.
- Reformatted the pattern to ensure it displays at full width, eliminating partial views.

The main page has been developed using HTML and CSS for the design. It includes links to all existing pages, ensuring easy navigation throughout the site.

![main_page](/2024/Alumni/main_page.jpeg)

## System Updates
The login page verifies user-entered data against the database. The CSS file for the profile page has been repaired. Currently, all data entered on the edit profile page is successfully started in the database, and users can modify and save individual data fields separately. Both the login and profile pages utilize the same user model. However, an issue arose where new data entries were replacing existing ones in the database, resulting in unchanged data previously stored in the database being replaced with empty values.

![db_test](/2024/Alumni/db1_test.jpeg)

![db_test](/2024/Alumni/db2_test.jpeg)

## Testing
This week we have writed the tests for both the main page and the access pass pages. The tests are accessible for viewing in the repository.

![testing](/2024/Alumni/testing.jpeg)

## External Feedback
We received feedback last week, which has boosted our confidence that each page of our site has its own meaning and purpose. Additionally, this week we began implementing a graduate's idea to create a map displaying the locations of alumni. The main feedback highlighted concerns about the site's potential inconvenience. Many suggested integrating it with a TC bot to enhance usability, which we aim to implement by the end of the semester. Despite these concerns, most people appreciated the design of the site. Next week, our goals include gathering feedback from graduates, creating a survey form, and compiling statistics based on the responses. This week, we were unable to proceed due to adhering to the content plan of the Alumni Telegram channel. However, we plan to publish the survey on the channel next week to solicit valuable input.

## Priorities
We have structured our backlog on the platform Linear and assigned priorities accordingly.
[https://linear.app/capstone-project-alumni-website/team/CAP/active](https://linear.app/capstone-project-alumni-website/team/CAP/active)

## Plans for the next week
Next week, we plan to create a page featuring the alumni map. Additionally, we aim to complete the main milestone, which involves implementing the majority of the project. Our main milestone spans 4 weeks and prioritizes the implementation of critical pages: merchandise, mentoring, user profiles and registration, AI chat integration, donations and pass access, and the main homepage. These pages are pivotal to the platform's functionality and user experience. We are allocating time for testing and finalizing the project to ensure everything functions smoothly. 

Also we are planning to develop a recommendation system based on AI. This system aims to assist graduates by recommending relevant activities and content tailored to their interests and profile.
