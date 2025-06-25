# Week 3
## Description of all implemented features
### User Management
- **CRUD operations for users** 
  Full implementation of Create, Read, Update, and Delete functionalities for user accounts.

### Book Management  
- **CRUD operations for books** 
  Complete functionality to add, view, edit, and delete books in the system.  
- **Books quantity tracking**  
  Implemented the ability to monitor and manage book quantities.  
- **Book assignment to libraries**  
  Added functionality to assign books to different libraries.  

### Booking System   
- **Adding book images(covers)**
- **User booking retrieval**  
  Added the ability for users to view their own bookings.  
### Library Management  
- **CRUD operations for libraries** 
  Full implementation of Create, Read, Update, and Delete functionalities for libraries.  
- **Manager assignment** 
  Added the ability to attach and detach managers to/from libraries. 
### Authentication & Security  
- **Registration and authentication**  
  Implemented user sign-up and login functionality.  
- **Route protection with JWT**  
### Additional Features  
- **Favorite books functionality**  
- **Book images**  
- **Booking date calculation**  

### PRs links:
Changing the status of books: https://github.com/IU-Capstone-Project-2025/libnet/pull/32 \
Ability to unlike a book: https://github.com/IU-Capstone-Project-2025/libnet/pull/28 \
Ability to get specific liked book by user: https://github.com/IU-Capstone-Project-2025/libnet/pull/25 \
Cancelled status to a booking: https://github.com/IU-Capstone-Project-2025/libnet/pull/24 \
Favorite books interaction: https://github.com/IU-Capstone-Project-2025/libnet/pull/22 \
Implementation of filter with and_ for book lookup: https://github.com/IU-Capstone-Project-2025/libnet/pull/30 \
Ability to get all libraries that have the book: https://github.com/IU-Capstone-Project-2025/libnet/pull/21 \
Implementation of logins for different access, view library catalogue: https://github.com/IU-Capstone-Project-2025/libnet/pull/18 




## Functional User Journeys for LibNet System
### **1. Admin User Journey**
**Scenario**: Admin manages libraries and access rights.

#### **Authentication Flow**
| Step | User Action               | UI Elements                          | System Response                     | Errors/Alternate Paths            |
|------|---------------------------|--------------------------------------|-------------------------------------|-----------------------------------|
| 1    | Clicks "Admin" in auth type selector | Logo dropdown (User/Manager/Admin) | Redirects to `Main Admin Auth Page` | -                                 |
| 2    | Enters email/password     | Fields: Email, Password             | Validates credentials               | "Invalid credentials" toast       |
| 3    | Clicks "Войти"            | Button "Войти"                       | Redirects to `Main Admin Page`      | -                                 |

#### **Library Management**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Clicks "Добавить библиотеку" | Button on `Main Admin Page`         | Opens `Library Admin Page` (empty)  |
| 2    | Fills library details     | Fields: Name, Address, Hours, etc.  | Enables "Сохранить" button          |
| 3    | Assigns managers          | Multi-select dropdown               | Saves manager permissions           |
| 4    | Clicks "Сохранить"        | Button "Сохранить"                   | Updates DB; shows success toast     |

#### **Account Management**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Clicks username in header | Profile dropdown                     | Opens `Account Admin Page`          |
| 2    | Edits profile info        | Fields: Name, Email, etc.           | Enables "Сохранить"                 |
| 3    | Clicks "Выйти"            | Button "Выйти"                       | Logs out; redirects to auth page    |

---

### **2. Manager User Journey**
**Scenario**: Manager processes book orders and updates library info.

#### **Authentication Flow**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Clicks "Manager" in auth type selector | Logo dropdown                     | Redirects to `Main Manager Auth Page` |
| 2    | Enters email/password     | Fields: Email, Password             | Validates credentials               |
| 3    | Clicks "Войти"            | Button "Войти"                       | Redirects to `Manager Main Page`    |

#### **Order Management**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Clicks "Бронирования"     | Navbar button                        | Opens `Orders Manager Page`         |
| 2    | Searches orders           | Search bar                           | Filters orders in real-time         |
| 3    | Updates order status      | Dropdown: "Ожидает выдачи" → "Выдано" | Saves to DB; updates UI            |

#### **Book Management**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Clicks "Добавить книгу"   | Button on `Manager Main Page`        | Opens empty `Book Manager Page`     |
| 2    | Fills book details        | Fields: Title, Author, Availability | Enables "Сохранить"                 |
| 3    | Clicks "Сохранить"        | Button "Сохранить"                   | Adds book to catalog; shows toast   |

---

### **3. User (Reader) Journey**
**Scenario**: User browses books, makes reservations, and manages favorites.

#### **Authentication Flow**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Clicks "User" in auth type selector | Logo dropdown                     | Redirects to `Main User Auth Page`  |
| 2    | Clicks "Создать аккаунт"  | Button under login form              | Opens registration form             |
| 3    | Fills details + clicks "Зарегистрироваться" | Fields: Name, Email, Password | Creates account; redirects to `Main Page` |

#### **Book Reservation**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Searches for a book       | Search bar on `Main Page`            | Shows results in real-time          |
| 2    | Clicks "Забронировать"    | Button on `Book Page`                | Opens library selector modal        |
| 3    | Selects library + confirms | Dropdown + "Подтвердить" button    | Reserves book; shows status in `Заказы` |

#### **Favorites Management**
| Step | User Action               | UI Elements                          | System Response                     |
|------|---------------------------|--------------------------------------|-------------------------------------|
| 1    | Click "Добавить в избранное"     | Heart icon on `Book Page`            | Adds to `Избранное` page            |
| 2    | Navigates to `Избранное`  | Navbar button                        | Displays all favorited books        |
| 3    | Clicks "Удалить из избранного"          | Button next to book                  | Removes from favorites              |

---

### Demonstration of the working MVP: 
* https://github.com/IU-Capstone-Project-2025/libnet/raw/refs/heads/main/reports/Video.Guru_20250625_222004511.mp4
### Internal demo
**Date**: 2025-06-25
#### User (Reader) Flow:
1. **Homepage**  
   - Book catalog display
2. **Book Details Page**  
   - Full book description  
   - Availability across libraries
3. **Registration**  
   - New user sign-up process
4. **Profile Management**  
   - Personal information editing  
   - Field updates (email, password etc.)
5. **Authentication**  
   - Login with credentials  
   - Error handling for invalid inputs
6. **Favorites System**  
   - Add/remove books to favorites  
   - Favorites list view
7. **Account Actions**  
   - Successful logout flow

#### Manager Flow:
1. **Dashboard Access**  
   - Manager authentication
2. **Book Management**  
   - Edit book information  
   - Catalog browsing
3. **Order Processing**  
   - View orders list  
   - Change order statuses
4. **Library Administration**  
   - Edit library details
5. **Navigation**  
   - Access to: Catalog, Favorites, Orders sections

### Link to API endpoints documentation.
* http://83.222.17.10:8000/docs
## Weekly commitments
### Individual contribution of each participant
| Team Member     | Completed Work                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ivan Murzin     | HTML layout mastering on existing pages, layout re-structurizing and writing styles for components and pages. Fixing existing styles.                                                                                                                                                                                                                                                                                                                                                                    |
| Aliya Sagdieva  | Updated the readme. Made the report documentation. Recorded a demo.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Alena Averina   | Made uploading book covers in url or file format. Started doing logging on the loki + grafana stack.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Anna Serova     | Implemented the frontend: Functionality and display of user orders. Functionality and display of user favorites. Changing the choice of city in registration and account to existing ones, choosing a library for ordering a book, duplicating books in several libraries. Manager panel: displaying books of a specific library, switching to user pages, loading and interacting with orders in the library for the manager, changing the library, part of the styles of the manager side, fixing part of the back endpoints. |
| Artem Ostapenko | Implemented in backend development: get cities of existing libraries, add ability to assign book to different libraries, favorite books, protect endpoint via JWT tokens, books quantity functional, book images, calculate date_to when a creating book, refine the change of booking status.  <br/>                                                                                                                                                                                                    |

### Plan for Next Week 
#### Frontend Development Plan:
1) Add missing user and administrator functions.
2) Make a FAQ page.
3) Make an admin part and functionality for it.
#### Backend Development Plan:
1) Search & Filters – Find books by title, author, genre, etc.
2) To identify missing backend functionality, we will analyze and implement necessary API endpoints for different user roles (admin, manager, regular user) based on current system requirements.
### Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md). 