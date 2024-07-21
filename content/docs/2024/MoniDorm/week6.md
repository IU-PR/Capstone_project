---
title: "Week #6"
---

# **Week #6**

## **Presentation**:

{{< embed-pdf url="/2024/MoniDorm/MoniDorm_Presentation.pdf" >}}

## **Weekly Progress Report**:

This week our team has been trying to improve the comments we received during feedback from users.
For the most part it was about the frontend and admin panel:

### **Frontend Admin Panel**

#### **Failure section**

Failures section added to admin panel, now contains grouped failures with their summarised description:

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/MoniDorm/failures.jpg">
</div>

#### **Fix API for graphics and plots**

We had a problem with the connection between the admin panel and the backend API, but we were able to solve it and now we get real data from the backend instead of mocked data:

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/MoniDorm/fixapi.jpg">
</div>

#### **Add filters for Reports**

We have added filtering by dorms, in the form of a drop-down list, to make it easier to see the plots that are needed:

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/MoniDorm/filter.jpg">
</div>

---

The Telegram Bot has also been improved:

### **Telegram Bot**

#### **Explanation for the attentive**

We have added a message to users asking them to be *responsible* with their reports so that false reports are not submitted.

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/MoniDorm/reports.jpg">
</div>

#### **Notification subscriptions**

We have added the ability to subscribe to notifications of certain events or dorms: for example you can subscribe only to the dorm where you live or to the floor.

users can unsubscribe from these subscriptions in a special section of the main menu:

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/MoniDorm/subscribe.jpg">
</div>

When a fault occurs, subscribers receive notifications of the problem, its location, number, and a brief summary of all messages:

<div style="display: flex; justify-content: center; align-items: center;">
    <img style="max-width: 100%; height: auto;" src="/2024/MoniDorm/notification.jpg">
</div>

#### **Save failures in DB**

We've done failures saving in the database, so it's not just reports that are stored there now.

### **Challenges & Solutions**

While developing frontend admin panel we faced CORS policy issues on react js. Fortunately we were able to solve this problem on [Stackoverflow](https://stackoverflow.com/questions/46337471/how-to-allow-cors-in-react-js)

### **Conclusions & Next Steps**

In conclusion, this week was aimed at finalising our project before demo day. In the future, we plan to refactor our project before the final presentation: we will containerise all applications, run internal review and testing. We will announce the operability of the project and prepare a nice demonstration.
