---
title: "Week #5"
---

# **Week #5**

## 📝 **Feedback**

### ❓ **Sessions**

Our team conducted 4 interviews with our first users. Now you can see summary of all interviews below

* 💡 **Project Idea**
    * **User 1**
      * "Cool idea, I think that personalosed roadmap will make learning much simpler."
    * **User 2**
      * "It is cool, but I think that we have enough sites with courses. But Automatic roadmap generation is good idea."
    * **User 3**
      * "I agree with User 2, furthermore, have you think about copyright"
    * **User 4**
      * "I really love your name."

* 🎨 **Site Design**
    * **User 1**
      * "Good design, I really love capybara on main page"
    * **User 2**
      * "Good design overal, but I prefer dark theme"
    * **User 3**
      * "I think that yellow color is not the best, additionally where is dark theme?"
    * **User 4**
      * "You have animations, thats enough to satisfy me"

 * 📝 **Onboarding**
   * **User 1**
      * "In case if I want to increase my python level, why I cant take it as a goal skill?"
    * **User 2**
      * "Maybe in education section you should add passed courses, to get better user background"
    * **User 3**
      * "I could not find all my skills, plus there are too many level selection pages"
    * **User 4**
      * "It was fast, too fast. I like it"

 * 🗺️ **Roadmap**
    * **User 1**
      * "Good looking roadmap plus it was created from scratch, I like it"
    * **User 2**
      * "Some courses have less information that other ones"
    * **User 3**
      * "Good, but it could be even better with more interaction features"
    * **User 4**
      * "Lol, Your roadmap updates 100 times a second, you should fix your rerender"

 * ♾️ **General Impressions**
   * **User 1**
      * "I think that this project have a good future. I think you will get an A"
    * **User 2**
      * "Good project, if you add more interactive features it would be perfect"
    * **User 3**
      * "Well, If you will work on it and add feature for automatic CV generation you totaly will succeed"
    * **User 4**
      * "I like it. Wish good luck on final presentation"

In case if you want to try our project visit [kizak.ru ](https://kizak.ru/)

### 🔎 **Analyze**

* Server lack of resources (not enough RAM)
* Black theme required
* More user statistics required
* Dataset with larger size required

## 💅🏻 **Iteration & Refinement**

### 🚀 **Implemented features based on feedback**

* Feedback feature (In progress)
  * User can send a feedback to generated roadmap
    * Exclude author
    * Exclude course
   
* Frontend optimisation
* Automatic course scrapping

All planned features could be found in our [backlog](https://github.com/orgs/IU-Capstone-Project-2025/projects/11) 

### 🏎️ **Performance & Stability**

* Maximum load
  * ❓ To test this we ask our friends to DDoS our site
  * 📝 Our site can handle up to 10 active users
  * 🔮 In future we plan to increase the performance of project and upgrade our server

* Site performance
  * ❓ To test this we used utilities provided by React
  * 📝 Some parts of site were constantly updating (rerendering) 
  * ✅ Our frontend developers optimised component rerender and increase site performance

* Backend and ML performance
  * ❓ To test this we will stress test our site
  * 🔮 In case of low performance, we plan to add load balancers

### 📄 **Documentation**

* Small documantation in [README](https://github.com/IU-Capstone-Project-2025/KIZAK/blob/main/README.md)
  * Contains requirements and instruction for project setup
* Built in API documentation by **SwaggerAPI** (works only while deployed)
  * Comes by default with FastAPI
  * Provides validation and test capabilities
* Simple markdown documentation
  * In case if **SwaggerAPI** not avaliable, user can see our [docs](https://github.com/IU-Capstone-Project-2025/KIZAK/tree/main/docs)

### 🤖 **ML Model Refinement**

* Improved course ranking (see Weekly commitments)
* Added template for user feedback (see Weekly commitments)

# 📝 **Weekly commitments**

## 📊 **Individual contribution of each participant**

* **Marsel Berheev:** m.berheev@innopolis.university
  * Report
  * ML and Backend connection (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/92))

* **Maksim Malov:** m.malov@innopolis.university
  * OAurh fix (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/91))
  * JWT token (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/91))
  * Code refactor

* **Makar Egorov:** m.egorov@innopolis.university
  * Automatic course scrapper (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/98))

* **Timur Farizunov:** t.farizunov@innopolis.university
  * Roadmap design and API connection (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/97))

* **Sarmat Lutfullin:** s.lutfullin@innopolis.university
  * Adaptive and authorisation (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/97))
 
* **Ulyana Chaikovskaya:** u.chaikouskaya@innopolis.university
  * Course normalisation (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/96))

* **Kseniia Khudiakova:** k.khudiakova@innopolis.university
  * Metrics update and course feadback feature template (see [pull request](https://github.com/IU-Capstone-Project-2025/KIZAK/pull/95))

## 🎯 **Plan for Next Week**

* Increase dataset size
* Update deployment instructions
* Add load balancers
* Refine UI

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).

