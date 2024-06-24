---
title: "Week #3"
---

### Week #3

#### Prototype functionality:
Because we currently do not have deployed prototype (except figma prototype [here](https://www.figma.com/proto/OqYWcu5new2YzWO7XfQE2I/capstone-project?node-id=1-2200&t=C79svI9vX0ffFJWD-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A2200)) we will provide pictures. We are trying as much as we can to achieve the same design as the prototype.

##### Home page:
![home_page](/2024/innobazaar/week3/week3_4.png)


##### Products page 1:
![products_page_1](/2024/innobazaar/week3/week3_1.png)


##### Products page 2 (category filter applied):
![products_page_2](/2024/innobazaar/week3/week3_2.png)


##### Products page 3 (category, min/max price, sort by filters applied):
![products_page_3](/2024/innobazaar/week3/week3_3.png)


##### Sign in page:
![products_page_1](/2024/innobazaar/week3/week3_5.png)

Please note that this is not a final prototype. The design and functionality will continue to be refined and enhanced based on our team feedbacks and further development.

### Developing the First Prototype, Creating the Priority List

#### Technical Infrastructure:

-   Set up the development environment with React for the frontend and Django for the backend. Organized the GitHub repository into separate sections for frontend and backend to have better workflow.
-   Installed necessary dependencies and frameworks such as `react-router-dom` for navigation, `axios` for API requests, and basic CSS for styling.
-   Because we do not have a deployed prototype, we use a python virtual environment to run local server to handle API requests.
-   We settled on to use this structure for our backend:

![db_schema](/2024/innobazaar/week3/week3_6.png)

#### Backend Development:

-   Established endpoints for fetching product data based on categories and filters.
-   Implemented a REST API to handle requests for product data, including filtering by category, price range, and search query.
-   Connected the backend to a mock database to simulate real data interactions.

#### Frontend Development:

-   Developed the main components for the application: `CategoryCarousel`, `FilterPage`, `ProductList`, `Filters`, `SortDropdown`, `Header`, and `Footer`.
-   Implemented a responsive category carousel with navigation buttons and click handlers to navigate to the product list page with the selected category.
-   Created a dynamic `FilterPage` that fetches and displays products based on selected filters and categories.
-   Integrated routing using `react-router-dom` to enable smooth navigation between the home page and the product list page.

#### Data Management:

-   Defined a data structure for categories and products.
-   Implemented state management within components to handle category selection, filtering, and sorting.
-   Utilized Axios to fetch data from the backend and update the UI accordingly.
This is the current scheme of our database:
![db_schema](/2024/innobazaar/week2_1.png)
It will most probably change, because we are planning to add more functionality to the website.

#### Prototype Testing:

-   Conducted initial tests to ensure that category selection and filtering work as expected.
-   Verified that the carousel navigation correctly updates the visible categories.
-   Tested the entire navigation flow from the home page to the product list page with various categories and filters.

### Weekly Progress Report:
This week, our team primarily focused on advancing the frontend development of our application. We concentrated on creating an interactive and seamless user experience by designing and implementing key components like the CategoryCarousel, FilterPage, and ProductList. These components were integrated with smooth navigation and dynamic data fetching capabilities, allowing users to easily switch between categories and see relevant products.

We also set up routing using react-router-dom to facilitate smooth transitions between the home page and the product listing page. Additionally, we integrated Axios for efficient API requests, enabling the frontend to fetch and display product data based on selected filters and categories.

Our efforts extended to styling and layout improvements to ensure the application is visually appealing and user-friendly. We have started initial user testing to identify and address any potential issues, laying a solid foundation for further enhancements in the upcoming weeks.

### Challenges & Solutions

**Challenge:**

-   Ensuring smooth navigation and data fetching when transitioning between different pages and states.

**Solution:**

-   Utilized `useNavigate` from `react-router-dom` v6 for efficient navigation.
-   Implemented state management and conditional rendering to handle different states of the application (loading, error, data fetched).

**Challenge:**

-   Handling multiple filters and ensuring they work together without conflicts.

**Solution:**

-   Managed state effectively within the `FilterPage` component to ensure that all filters (category, price, search query) update the product list correctly.
-   Used `componentDidUpdate` lifecycle method to trigger data fetching whenever a relevant state changes.

### Conclusions & Next Steps

**Conclusions:**

-   The first prototype successfully demonstrates the core functionality of the application, including category navigation, filtering, and product listing.
-   Initial testing indicates that the application is responsive and handles user interactions as expected.

**Next Steps:**

-   Enhance the user interface with more detailed styling and responsive design considerations.
-   Implement product adding and additional backend endpoints for a more complete user experience.
-   Conduct thorough testing, including user testing, to identify and fix any remaining issues.
-   Do more research on how we can utilize AI in our website.


While the initial prototype effectively showcases the core functionalities such as category navigation, filtering, and product listing, we recognize that this is just the beginning of our development journey. This prototype serves as a foundation, but it may not represent the final design or feature set. We are dedicated to continuous improvement and enhancement based on comprehensive testing and our findings. Our immediate next steps include refining the user interface to enhance usability and design, implementing whether product publication or robust user authentication, expanding backend functionalities, and introducing more dynamic features. We will also conduct extensive user testing to gather valuable insights and make informed adjustments. Ultimately, we aim to iterate and evolve the application to ensure a seamless, efficient, and engaging user experience, preparing it for a successful deployment and scalability.