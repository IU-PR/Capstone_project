---
title: "Week #4"
---

# Week 4 Report: Alumni Portal

**Authors:** Chulpan Valiullina, Nazgul Salikhova, Liubov Smirnova, Anzhelika Akhmetova, Olesia Grediushko, Galia Shabanova, Anastasiia Ozerova

## Introduction
This week, we completed the donations page for alumni, wrote several tests, and developed the main page's frontend. We also overcame various obstacles related to integrating all pages into a single portal using Django.

## External Feedback
We received feedback last week, which has boosted our confidence that each page of our site has its own meaning and purpose. Additionally, this week we began implementing a graduate's idea to create a map displaying the locations of alumni. The main feedback highlighted concerns about the site's potential inconvenience. Many suggested integrating it with a TC bot to enhance usability, which we aim to implement by the end of the semester. Despite these concerns, most people appreciated the design of the site. Next week, our goals include gathering feedback from graduates, creating a survey form, and compiling statistics based on the responses. This week, we were unable to proceed due to adhering to the content plan of the Alumni Telegram channel. However, we plan to publish the survey on the channel next week to solicit valuable input.

## Testing

During this week we wrote unit - tests for most of the pages on our site. These tests have been committed to the master branch. Below we provide a brief description of what we are checking:

### Main Page Tests

- `test_main_page_status_code` // Ensures main page returns status code 200.
- `test_main_page_template_used` // Verifies main page uses `main/main.html` template.
- `test_main_page_content` // Checks for "Welcome to Alumni website!" text on main page.

### Market Page Tests

- `test_product_list_view` // Ensures product list view returns status 200, uses `market/market.html`, and shows test product.
- `test_product_detail_view` // Verifies product detail view returns status 200, uses `market/product_details.html`, and includes test product.
- `test_product_buy_view_get` // Checks product buy view (GET) returns status 200, uses `market/product_buy.html`, includes test product and no selected size.
- `test_product_buy_view_post` // Ensures product buy view (POST) redirects to checkout, sends two emails, and emails contain specific content.
- `test_checkout_view` // Simulates session with selected product, checks checkout view returns status 200, uses `market/gratitude_buy.html`, and shows correct price.

### Login Page Tests

- `test_login_page_status_code` // Ensures login page returns status code 200.
- `test_login_with_valid_credentials` // Verifies login with valid credentials redirects to profile page.
- `test_login_with_invalid_credentials` // Checks login with invalid credentials returns status code 200 and displays error message.

### Donation Page Tests

- `test_donation_page_status_code` // Ensures donation page returns status code 200 on GET request.
- `test_donation_page_template_used` // Verifies donation page uses `donation/donation.html` template.
- `test_donation_form_submission` // Simulates POST request to donation page, checks status code 200, and response contains "Thank you for your donation!" message.

### Card Request Page Tests

- `test_page_status_code` // Ensures card request page returns status code 200 on GET request.
- `test_page_template_used` // Verifies card request page uses `card_request/card_request.html` template.
- `test_handle_form_submission` // Simulates POST request to form submission handler, checks status code 200, response JSON contains `{'message': 'Success'}`, and verifies email notification details.

### AI Chat Tests

- `test_chat_view_post` // Simulates POST request to `/chat/` endpoint with JSON message (`'Hello!'`). Checks status code 200 and verifies `response` field in JSON response is a string.
- `test_chat_view_post_empty_message` // Simulates POST request to `/chat/` endpoint with empty JSON payload. Checks status code 200 and verifies JSON response contains `{"response": "No input provided"}`.
- `test_chat_view_invalid_method` // Simulates GET request to `/chat/` endpoint (expected to handle only POST). Checks status code 405 and verifies JSON response contains `{"response": "Invalid request method"}`.


## Iteration

Our weekly work process is structured into two main phases. At the beginning of each week, we convene on Monday to outline and assign tasks for the upcoming week. Midweek, on Wednesday, we come together again to address any challenges or issues encountered during task execution. By Friday, we consolidate our progress and review the tasks originally set, culminating in a meeting with our TA to provide updates and seek guidance.

The process is conventionally divided into two distinct parts: from Monday to Wednesday, we focus on planning, goal-setting, and troubleshooting, while from Wednesday to Sunday, our emphasis shifts towards task execution and development.




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




## Priorities
We have structured our backlog on the platform Linear and assigned priorities accordingly.
[https://linear.app/capstone-project-alumni-website/team/CAP/active](https://linear.app/capstone-project-alumni-website/team/CAP/active)

## Plans for the next week
Next week, we plan to create a page featuring the alumni map. Additionally, we aim to complete the main milestone, which involves implementing the majority of the project. Our main milestone spans 4 weeks and prioritizes the implementation of critical pages: merchandise, mentoring, user profiles and registration, AI chat integration, donations and pass access, and the main homepage. These pages are pivotal to the platform's functionality and user experience. We are allocating time for testing and finalizing the project to ensure everything functions smoothly. 

Also we are planning to develop a recommendation system based on AI. This system aims to assist graduates by recommending relevant activities and content tailored to their interests and profile.
