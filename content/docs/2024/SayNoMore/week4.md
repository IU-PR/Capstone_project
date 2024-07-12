---
title: "Week #4"
---

# **Week #4**

## External Feedback

Our product is not yet ready for beta testing and broader external feedback. We are currently focusing on fixing some core bugs in the code to ensure the stability and reliability of the bot. This week, our primary focus has been on internal testing and gathering feedback from our team members to refine the bot's functionality and user experience.

However, we have shared our prototype with our Teaching Assistant (TA) and mentor to gain preliminary external insights. Their feedback has been valuable in shaping the direction of our improvements and identifying potential issues early. Once we have resolved the core bugs and completed our internal testing, we will be better prepared to open the product for external beta testing and broader feedback.

___
## Testing

Our approach to testing has been comprehensive, incorporating both unit testing and thorough internal testing of our bot. 

#### Unit Testing
We have implemented unit tests across our codebase to ensure each module functions as expected in isolation. These tests help us catch issues early in the development process and maintain code quality.

#### Internal Testing
In addition to unit tests, we have started a detailed internal testing phase for our bot. This involves simulating user interactions, gathering feedback from internal users, and meticulously documenting every bug and anomaly we encounter. The internal feedback we collect is invaluable for refining the bot and enhancing its performance and user experience.

While we prefer not to publicly disclose all our internal testing logs, we are sharing two test cases to illustrate our testing process and the types of issues we are addressing.

#### **Test Case ID**: TC004  
**Date**: 2024-07-01  
**Tester**: Maxim Martyshov  
**Scenario**: Request with error  

#### **Test Case Description:**
This test involves making a request with an error in it. Specifically, it tests how the bot handles a departure or arrival date that is in the past.

#### **Test Log:**

| **Step No.** | **Message Sent**                | **Bot Response**                                             | **Code Crash Message (if any)** |
|--------------|---------------------------------|--------------------------------------------------------------|---------------------------------|
| 1            | хочу уехать из Казани 1 июня    | *Ваш запрос не содержит некоторых необходимых данных. Пожалуйста, укажите даты вылета и возвращения, а также город назначения. Кроме того, если у вас есть бюджет, вы можете указать и его, хотя это не обязательно. Спасибо!* | *-*                             |
| 2            | в москву до 7 июня              | Ваш запрос содержит некоторые ошибки. Пожалуйста, убедитесь, что дата возвращения введена позднее даты прибытия. Кроме того, если у вас есть бюджет, вы можете указать и его, хотя это не обязательно. Спасибо! | <br>-                           |
| 3            | в москву до 7 июля бюджет 100тр | Route from KZN to MOW:<br>Flight: KZN to MOW, Departing at: 2024-07-07T07:55:00+03:00, Returning at: 2024-07-07T20:40:00+03:00, Airline: N4, Flight Number: 250, Price: 43946 rub, Transfers: 1, Return Transfers: 1, Duration: 955 minutes<br>Hotel: 1-komнатная квартира, Location: Moscow, None, Russia, Stars: 0, Price From: 8551.76 rub, Average Price: 8551.76 rub<br>________________________ | *-*                             |


#### **Additional Notes:**
- Here is the `Request analyzer` return from this interaction:
  ```json
  {"Arrival": "2024-07-07", "Return": "2024-07-07", "Departure": "KZN", "Destination": "MOW", "Budget": 100000}
  ```
  * We see some issues with arrival retrieval.

---

#### **Test Case ID**: TC005  
**Date**: 2024-07-02  
**Tester**: Maxim Martyshov  
**Scenario**: Request outside Russia  


#### **Test Case Description:**
This test involves making a request completely outside the Russian Federation, such as planning a trip from London to Paris.

#### **Test Log:**

| **Step No.** | **Message Sent**                                          | **Bot Response** | **Code Crash Message (if any)**                              |
|--------------|-----------------------------------------------------------|------------------|--------------------------------------------------------------|
| 1            | Хочу уехать из Лондона в Париж с 3 по 9 июля бюджет 300тр |                  | *File "/home/SayNoMore/api_collector/air_tickets/air_tickets_api.py", line 101, in fetch_cheapest_tickets<br>    raise Exception(<br>Exception: Failed to fetch cheapest tickets. Status code: 420* |


#### **Additional Notes:**
- Here is the `Request analyzer` return from this interaction:
  ```json
  {"Arrival": "2024-07-09", "Return": "2024-07-09", "Departure": "LOZ", "Destination": "PRX", "Budget": 300000}
  ```
  * We notice some issues with the arrival retrieval.
  * `LOZ` is IATA code for London-Corbin airport in the USA, and we need `LHR` for London Heathrow.
  * `PRX` IATA code is also not correct. Paris should be `CDG`.

___
## Progress Report

During this week, we continued developing our first prototype. Our bot is now fully functional, with all basic functions implemented and major bugs related to connecting all three modules fixed. However, we are working on improving the quality of our recommendations, which currently need refinement. Additionally, we have started extensive testing of the bot to find and fix bugs. During the next iterations, we will focus on adding extra features and improving the bot's interface (buttons, hotel pictures, etc.).

---


### Challenges and Solutions

1. **LLM Deployment Issues**:
   - **Challenge**: Running the local LLaMA model requires significant GPU resources and presents challenges in deployment, making it difficult to scale and manage.
   - **Solution**: We realized the need to switch from a local LLM to an already deployed one, using REST API requests. This transition brought several challenges, including setting up a server and running our bot on the same server where the LLM is deployed, accessible via SSH connection.

2. **Remote LLM Regularly Being Down**:
   - **Challenge**: The remote LLM's frequent downtimes have significantly disrupted our development process.
   - **Solution**: We are considering alternatives such as utilizing more stable cloud-based LLM services or improving our infrastructure to better handle these downtimes.

---

### Next Steps

In the next iteration, we plan to:
- Enhance the quality of our travel recommendations.
- Continue rigorous testing to uncover and fix any remaining bugs.
- Add extra features to the bot, such as interactive buttons and hotel pictures, to improve user experience.

---
