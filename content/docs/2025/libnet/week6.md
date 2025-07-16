# Week 6
## Links 
Specify all the necessary links to your resources:

| Category       | Link      |
|----------------|-----------|
| 🌐 Deployment  | [libnet](https://libnet.site/) |
| 📚 API Docs    | [FastAPI](http://libnet.site:8000/docs) |
| 🎨 Design      | [Figma](https://www.figma.com/design/PEK6pAX4gh7f5oO9C0jNfq/libnet?node-id=0-1&t=sEVJZ4Fg0AY8jxIw-1) |
| ▶️ Demo       | [Video](https://github.com/IU-Capstone-Project-2025/libnet/raw/refs/heads/main/reports/DEMO2.mp4) |
| 📦 Repository  | [GitHub](https://github.com/IU-Capstone-Project-2025/libnet) |
## Final deliverables
### Project overview
#### Problem Statement
LibNet addresses three core challenges in library management systems:
1. **Fragmented book search** across multiple libraries
2. **Outdated interfaces** with poor user experience
3. **Difficulties in obtaining books** simplified the search and booking of books

### Key Implemented Features

#### For Readers
- 🔍 Unified book search across all partner libraries
- 📅 Online reservation system with status tracking
- ❤️ Favorites list for saved books
- 📱 Responsive design for devices

#### For Library Staff
- 📊 Manager dashboard for reservations
- 📚 Book inventory management
- 🏢 Multi-library support

#### Technical Highlights
- ⚡ FastAPI backend with JWT authentication
- 🎨 React frontend with Vite optimization
- 📊 Grafana/Loki monitoring stack
- 🔄 Automated database migration (Ollama)
- 🛡️ Role-based access control

### Impact
- Fast book discovery for users
- Centralized management for library networks
### Features

#### For All Users
- **Book Search & Discovery**
  - Unified catalog across multiple libraries
  - Advanced filters (author, genre, year, availability)
  - "Nothing found" handling with suggestions
  - Book details with cover images

- **User Management**
  - Registration with email validation
  - Login/Logout functionality
  - Password reset/change flow
  - Profile editing

#### For Readers
- **Reservation System**
  - Book reservation with status tracking
  - Booking cancellation
  - Favorites list (like/unlike books)
  - Order history

- **UI/UX**
  - Responsive design (mobile/desktop)
  - Loading skeletons
  - Accessible navigation

#### For Library Staff
- **Manager Tools**
  - Library-specific dashboard
  - Booking management (approve/reject)
  - Book inventory CRUD operations
  - Library working days configuration
  - Manager assignment system

- **Admin Features**
  - Multi-library management
  - User role administration
  - System monitoring access
  - Self-deletion protection

#### Technical Features
- **Security**
  - JWT authentication
  - Role-based access control
  - DDOS protection
  - HTTPS enforcement

- **Infrastructure**
  - Dockerized deployment
  - Grafana/Loki monitoring
  - CI/CD pipelines
  - Automated database migrations


### Tech stack

#### Backend
**Python**  
- Simple syntax with extensive libraries  
- Rapid development capabilities  

**FastAPI**  
- High-performance async framework  
- Seamless PostgreSQL integration  
- Automatic OpenAPI documentation  

#### Frontend  
**React**  
- Component-based architecture  
- Reusable UI elements (book cards, forms)  
- Future-proof scalability  

**Vite**  
- Lightning-fast build tool  
- Hot module replacement  

#### Database  
**PostgreSQL**  
- Relational structure for complex queries  
- Built-in JSON support  
- Easy schema migrations  

#### Monitoring & Analytics  
**Grafana + Loki**  
- Real-time application monitoring  
- Centralized logging system  
- Performance dashboards  

#### Data Processing  
**Ollama**  
- Library database migration tool  
- Cross-format parsing (.xls, .csv, .json)  
- Schema mapping automation  

#### DevOps  
**Docker**  
- Containerized environments  
- Development/production parity  

**GitHub Actions**  
- Automated CI/CD pipelines  
- Pull request testing  
- Zero-downtime deployments  

#### Project Management  
**ClickUp**  
- Task tracking  
- Sprint planning  
- Team coordination
### Setup instructions

#### Prerequisites
- Docker and Docker Compose installed
- Google account with 2FA enabled
- Git installed

#### Deployment Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/IU-Capstone-Project-2025/libnet.git
   cd libnet
   ```
2. Configure environment

    ```bash
    cd backend
    nano  .env  # Create environment file
    ```
3. Edit `.env` file:

    ```ini
    DATABASE_URL=database-url
    SECRET_KEY=your-secret-key
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_DB=your_db_name
    SMTP_USER=your-email@gmail.com
    SMTP_PASS=your-google-app-password
    ```
4. Google SMTP Setup:
   * Enable 2FA on your Google account
   * Get a key for the application via Google
   * Enter the key in SMTP_PASS, SMTP_USER as email
5. Launch services

    ```bash
    docker-compose up -d --build
   ```
The project has been launched!

## Presentation draft
[Link to the Draft](https://github.com/IU-Capstone-Project-2025/libnet/blob/main/reports/libnet%20presentation.pdf)
## Production (Bonus Assignment)
### Production Deployment

For **production deployment**, we selected a reliable Virtual Dedicated Server (**VDS**) provider.  
At first, we compared several platforms: **host-wds**, **Beget**, and **Timeweb**. We went with **Beget**, because:
- It came with a pre-installed **Docker** service, making environment setup easier.
- Pricing was attractive.
- The UX/design was user-friendly.
- Some competitors offered VDS abroad with latency and performance issues; we preferred speed and chose a server in Russia.

**Server configuration**:
- **2 CPU cores** (for multiprocessing)
- **4GB RAM**
- **50GB NVMe SSD** (fast SSD connected directly to motherboard)

**Production environment setup:**
1. **Purchased the server** and connected via SSH.
2. **Cloned the repository** to the server.
3. Created a local `.env` for secrets:  
    - DB connection string (includes DB name, user, password)
    - Credentials for a DB user
    - Secret key for password encoding
    - SMTP user/password for sending confirmation codes  
    > The `.env` is only on the server; never committed to source control.

4. **Containerization/Orchestration**:
    - Used `docker-compose.yml` to configure and run all containers.
    - Authored Dockerfiles for both backend and frontend.
    - Initially, Nginx was in a separate container; to simplify, later merged Nginx and frontend into one container.  
      The frontend Dockerfile has **build** and **production** stages.
    - Nginx has its own config for **HTTP→HTTPS** redirection.
    - Custom `loki.yml` and `prometheus.yml` for logging and monitoring setup.

5. **CI/CD Pipeline**:
    - `docker-compose.test.yml` runs backend and test Postgres for CI.
    - GitHub Actions (.github/workflows) was split:
        - One file for **CI** (triggered on push to `main`/`devops`)
        - One file for **CD** (auto-deploy, on push to `main`, runs only after CI passes)
    - Secrets (.env) are never in git, only on the server. `.dockerignore` is set up.
    - For autodeploy:
        - Created a `deploy.yml` workflow in `.github/workflows` with commands for deployment.
        - Generated a private SSH key on a different workstation;  
          added the public key to `~/.ssh/authorized_keys` on the server.
        - Stored the private key in **GitHub repo secrets** as `SSH_PRIVATE_KEY`.
        - Other secrets: `SSH_HOST`, `SSH_USER`, `PROJECT_DIR`.

6. **Domain name setup**:
    - Registered `libnet.site` at reg.ru.
    - Configured DNS:  
        - A-record `@` → `83.222.17.10`
        - A-record `www` → `83.222.17.10`


## Weekly commitments 
### Individual contribution of each participant
| Team Member     | Completed Work                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ivan Murzin     | [Create FAQ](https://github.com/IU-Capstone-Project-2025/libnet/commit/91f3317a71e3aa3d4b8c3a3adc8516750c5a2f13). [Add buttons, create new page for user - Libraries with description and contacts](https://github.com/IU-Capstone-Project-2025/libnet/commit/2ff9141bf757cb330de4a65be8bb42f543ed50a5). [Add info to orders, add cursor pointer to select list in manager navbar](https://github.com/IU-Capstone-Project-2025/libnet/commit/3e7fd91f4beb9dc45c7b2d413937b78344b8acc5). [Fix styles for Manager and Admin pages](https://github.com/IU-Capstone-Project-2025/libnet/commit/e592eba8c3ea66cac28ef0cc7e5faaab56d7d6d2). [Add back button to Book.jsx, add dividers to LibraryInfo](https://github.com/IU-Capstone-Project-2025/libnet/commit/ea8a27a34a294ef0c2a84d01b689b6377d8bd201). [Fix slider over login popup issue](https://github.com/IU-Capstone-Project-2025/libnet/commit/ad4e318785037ab5064b4f17322e40f03ef45a86). [Fix styles](https://github.com/IU-Capstone-Project-2025/libnet/commit/20a90d01bef74d106260ce2a04d2e3104b1b7e79). [library styling](https://github.com/IU-Capstone-Project-2025/libnet/commit/1ac5251d3c5979d90235926f1a3301eb7357c428). [Fix styles for buttons](https://github.com/IU-Capstone-Project-2025/libnet/commit/4b7993215f487d93887468c113cf1ffd8c190581). [Fix style for list-item](https://github.com/IU-Capstone-Project-2025/libnet/commit/416cecd75ffbbebea420c6b446691679a031a1e4). [Profile buttons fix, warning display fix on small screens](https://github.com/IU-Capstone-Project-2025/libnet/commit/5a4537ce7aee515b7e53ec384122e2dc3d93affc)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Aliya Sagdieva  | [Updated roadmap in the README.](https://github.com/IU-Capstone-Project-2025/libnet/commit/4ffbe5eeb5dfe18f562ec759342370db145d2df8) Made the report documentation. Recorded a demo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Alena Averina   | Updated Jinx configuration. Monitored the site's performance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Anna Serova     | Implemented the following tasks on the frontend: [new library adding](https://github.com/IU-Capstone-Project-2025/libnet/commit/43bc66f98f4a2b8ea28d22e29bde8036f9f6d6dc), [adding publisher of books](https://github.com/IU-Capstone-Project-2025/libnet/commit/fc35ef88b9e5e212bbd80abad9c7a7f043c0c9ce), [library and cities filter](https://github.com/IU-Capstone-Project-2025/libnet/commit/fd70446887501022f631674cdd9cb993204ea6be), [cancelling a booking as a user](https://github.com/IU-Capstone-Project-2025/libnet/commit/9a8a1c8148cc6cf327a7cf211cacc26efc3843bb), [verification requirement message](https://github.com/IU-Capstone-Project-2025/libnet/commit/0bd650d66ed3184856605fdf182d0d9dc513bd35), [verification status update fix](https://github.com/IU-Capstone-Project-2025/libnet/commit/8fa64bd5527a10324a0a81de77c8eda39b2b32f4), [library filter responsive to city](https://github.com/IU-Capstone-Project-2025/libnet/commit/8b47ac4c92886117795b656000ceab18128f849c), [Automatic library filter at manager](https://github.com/IU-Capstone-Project-2025/libnet/commit/150cd3403b7ab9092bbb2ac61906b1b082420f29), [protect admins from deleting themselves](https://github.com/IU-Capstone-Project-2025/libnet/commit/7cd36c8d49037463e5c43e9813e3caf0c3f14bc4), [unliking a book](https://github.com/IU-Capstone-Project-2025/libnet/commit/aca804a63440bd64ecc53c18ead628a46eee43a8), [search, filters in all account types](https://github.com/IU-Capstone-Project-2025/libnet/commit/a267e5b056946054bce15152fc4d3ac79400e2d6), ["nothing found" message + change in loading display principle](https://github.com/IU-Capstone-Project-2025/libnet/commit/1d4a2ef8ba3668913bc3bb8d5d2dcef61c948d1f), [orders user info + weekdays styling](https://github.com/IU-Capstone-Project-2025/libnet/commit/46fe5b9502c3ee3b6510a53ff6ffe35bf0095cd3), [display, setting working days of the library by buttons](https://github.com/IU-Capstone-Project-2025/libnet/commit/c22a59ca08db18d27cbd2de2d8efd17122e089f3),[change filters by authors and genres with search and signs](https://github.com/IU-Capstone-Project-2025/libnet/commit/a5162ae18aa6ed50aba40b174dff44cb9eae00c7) |
| Artem Ostapenko | [Add bookings sorting](https://github.com/IU-Capstone-Project-2025/libnet/commit/de68914ce8bd58e8d5f79e3add58e82dff189f56). [Implementation of Enhance city search](https://github.com/IU-Capstone-Project-2025/libnet/commit/4cf37628c56ca13c7ded7cec623c3b344435984f). [Add ability to change books quantity](https://github.com/IU-Capstone-Project-2025/libnet/commit/76edfb1172fccd9a6085e700e8722e86f2f17f31) [Add get libraries by city](https://github.com/IU-Capstone-Project-2025/libnet/commit/df9681dca5465482b12fec67ff61eba83a567da9). [Optimize get_bookings](https://github.com/IU-Capstone-Project-2025/libnet/commit/10175e6f6679c2d256913619329351c1f384cbc2). [Add easier way to access filter parameters](https://github.com/IU-Capstone-Project-2025/libnet/commit/19866d80a02376b37c8da670be14818433172231). [Add booking search for managers](https://github.com/IU-Capstone-Project-2025/libnet/commit/981c6f5b6a33c4940fcfed4a463a6c88523665e3). [Add book quantity logic](https://github.com/IU-Capstone-Project-2025/libnet/commit/f2f0b654683be250617e4ce8ab9a8aaee1c7989f). [Add endpoint for repeating the verification code](https://github.com/IU-Capstone-Project-2025/libnet/commit/c6d866ed7604d0d0b2f6b3af44810fee523ee111).[Limit endpoints' access to prevent DDOS](https://github.com/IU-Capstone-Project-2025/libnet/commit/52d5f6da46d27444932c73e0f7c6d544f1b134da). [Add alembic migrations](https://github.com/IU-Capstone-Project-2025/libnet/commit/7389ba41ebb1cb6a4232d8f5969d337387128e5d). [Add email verification via code](https://github.com/IU-Capstone-Project-2025/libnet/commit/0d759c2c53d193de6d66a59cd2c80e9d3733b1af). [Fix library creation](https://github.com/IU-Capstone-Project-2025/libnet/commit/c7b14c7985ac9342e3e484aef57b0ad52be6415e). <br/>                                                                                                                                                                                                                                                                                                                                                                                                | 
### Plan for Future

#### Backend

- Recursive deletion of objects to avoid conflicts

#### Frontend

- Fix possible bugs
- Clean up code from console output

### Confirmation of the code’s operability

We confirm that the code in the main branch:

- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the README.md). 


