# EdHub Week 1 Report

<aside>

Capstone Project course

Innopolis University

June 2025

</aside>

# Team

| Gleb Popov | Backend Developer, Project Manager |
| --- | --- |
| Timur Usmanov | Backend Developer |
| Asqar Dinikeev | Backend Developer, DevOps |
| Alina Suhoverkova | Frontend Developer, UI/UX designer |
| Timur Struchkov | Frontend Developer |

# Project Description

### Idea

We want to develop a Learning Management System for interaction between teachers, students, and parents. Teachers can create courses, upload materials, create homework assignments, see student submissions, grade them based on criteria, and calculate course grade.

### Target Users

Our goal is to develop a platform that both school teachers can use in their classes and university professors can use when planning courses. In our project, we want to emphasize the simplicity and usability of the product. We want any school teacher, who does not know much about technology, too be able to use our LMS and improve the quality of an educational process.

### Market Research

Most existing LMSs have limited functionality and cannot be fully utilized in schools and universities. For example, [Google Classroom](https://classroom.google.com/) has a user-friendly interface and pleasant design, but does not support parental access, creating the need for teachers to explain the details of grades to students' parents, does not support the grading of entire course as well as the tracking of student attendance. In addition, Google Classroom is a proprietary platform that hosted by Google and can not be launched on local servers.

On the other hand, a lot of LMSs have awkward website design and cause difficulties in everyday use. For example, [Moodle](https://moodle.org/) platform has extensive functionality, but is too complex to use, requiring clear customization and support at the IT administrator level. In addition, the platform has no assessment of assignments by criteria.

# Roles & User stories

We have four main roles in our LMS: **Teacher**, **Student**, **Parent**, and **Administrator**. The first three roles operate within a specific course. Any user of LMS can create a course and become a **Teacher** in it or join an already existing course as a **Student**, **Parent**, or an additional **Teacher**.

The role of **Administrator** applies to the entire LMS, its goal is to help users in case of any difficulties and/or bugs. **Administrator** can view system logs, access any page of the website, edit any blocks / materials / assignments / submissions on any course in LMS.

### Teacher

- **As a** teacher, **I want to** create courses fast and simply **so that** interaction with a group of students becomes easier.
- **As a** teacher, **I want to** invite students to a course **so that** they can access the course materials and have the opportunity to submit their work.
- **As a** teacher, **I want to** invite students‘ parents to a course **so that** they can track the students‘ grades without disturbing me.
- **As a** teacher, **I want to** upload, remove, and change materials **so that** students will receive them fast.
- **As a** teacher, **I want to** receive the students’ work submissions **so that** I can collect them in one place without direct interaction.
- **AAs a** teacher, **I want to** track the time of student submissions **so that** I can monitor for deadline violations.
- **As a** teacher, **I want to** grade the students’ submissions **so that** students get detailed feedback on the criteria in one place.
- **As a** teacher, **I want to** mark student attendance **so that** I can collect this information in one place.
- **As a** teacher, **I want to** assign a user as a parent of another user **so that** they can monitor another user’s progress.

### **Student**

- **As a** student, **I want to** access courses **so that** interaction with a teacher be- comes easier.
- **As a** student, **I want to** see the study materials **so that** I can review the lesson material at home on my own.
- **As a** student, **I want to** submit my work **so that** I can deliver the work to the teacher quickly and without direct interaction.
- **As a** student, **I want to** receive my grades **so that** get feedback on my work.
- **As a** student, **I want to** view which teacher graded my submission **so that** I know which teacher to contact in case of any questions

### Parent

- **As a** parent, **I want to** access the grades of my student **so that** I can track their academic progress.

### Administrator

- **As an** administrator, **I want to** deploy my own instance of LMS (similar to GitLab) **so that** my organization's sensitive data will be stored locally.
- **As an** administrator, **I want to** edit any blocks / materials / assignments / submissions on any course **so that** I can help users in case of any difficulties and/or bugs.
- **As an** administrator, **I want to** access all the service logs **so that** I can localize the problem and help fix it.
- **As an** administrator, **I want to** enable/disable the registration of new users in the LMS **so that** I can control access to the local LMS model.
- **As an** administrator, **I want to** register new users manually **so that** I can provide ready-made accounts to the teachers at my organization.

# Repository

[https://github.com/IU-Capstone-Project-2025/edhub](https://github.com/IU-Capstone-Project-2025/edhub)

# Tech Stack

- React framework was chosen as the main **frontend stack** for its component-based architecture, rich ecosystem, and strong community support, enabling rapid UI development.
- FastAPI Python framework was chosen as the main **backend stack** for its high development speed and extensive documentation
- PostgreSQL was chosen as the main **database** for its reliability and extensibility.
- Docker Compose is chosen for the **deployment process** as it is the industry standard for service deployment using containers.
