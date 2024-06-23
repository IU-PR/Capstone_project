## **Week 3 - Finishing the Plans**
### **Weekly Progress Report**
**Frontend**:
- Different languages are now supported
- English translation added
- Several critical bugs fixed

**Backend and Database**:
- Database schema outline created

![Database schema](/2024/SmashUp/week3/database_schema.png)

- Data migration performed
- Simple end-points implemented
- Mock end-points created for complex features

**Machine Learning**:
- Research performed

---

**Technical Infrastructure:**
We rented cloud server, where MariaDB database server and back-end application are located, to write front-end without the need for running local back-end application.

**Backend Development:**
All API endpoints necessary for the current project stage were designed together with their request and response formats. Authorization system, content streaming and some other content access functions are made. Some endpoints are not fully realized yet, substituted with mock endpoints.

**Frontend Development:**
Frontend is fully designed, design is available at Figma. 

**Data Management:**
MariaDB database following the presented scheme is deployed.

**Prototype Testing:**
Feedback among the team members was collected and we are currently working on enhancing the prototype based on it.

---

### **Challenges & Solutions**

**Frontend**:
- Unexpected differences between next.js and react.js caused several problems to appear, but they were solved after some research

**Backend and Database**:
- Data migration was long and difficult, but was performed after all

**Machine Learning**:
- Lack of understanding of possible problem solutions was solved with extensive research

### **Plans for the Next Week**
- Connect frontend and backend
- Implement connection pool for database
- Create MVC-tests
- Create basic recommendation system
