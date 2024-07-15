---
title: "Week #6"
---

# Week #6

## Presentation

{{< embed-pdf url="/2024/Team44/week_6_presentation_v2.pdf" >}}

## Weekly Progress Report:
This week, our team focused on addressing the challenges related to 
the connection between the front-end and back-end. 
Additionally we worked on UX/UI design, 
after receiving feedback from testers and aimed to make it more adaptive and looking nicer.


### Challenges & Solutions

1. Front-End and Back-End Connection:
- Issue: There were problems with the connection between the front-end and back-end components, causing inconsistencies in data display and functionality.
- Solution: We identified and rectified the mismatches in API calls and data handling, improving the communication between the front and back ends.
2. Adaptive UX/UI Design:
- Issue: Ensuring the design adapts smoothly across different devices and screen sizes posed a significant challenge.
- Solution: We implement responsive design techniques and conducted thorough testing on various devices to ensure adaptability.
3. Frontend deploy:
- Issue: Disability to deploy to vercel.com since repository with our code doesn’t belong to us
- One of the solution might be exposing svelte port on server’s virtual machine and allow to connect it with backend, which wasn’t implemented yet due to needness of asynchronous connect between backend and frontend
4. Implementing asynchronous backend:
- Issue: A limiting factor in the implementation of the previous problem is the need for asynchronous communication between the frontend and backend. So in this case probably some other connection should be established on the virtual machine. Main challenge here: lack of knowledge and experience with Django WebSockets or Celery + Redis, and which one to choose for our specific case. 
-We have not been able to solve this problem this week and it will become our main focus next week, since it’s crucial for user experience. How might we resolve this: analyze existing products with asynchronous Django and learn from them how we can handle our case and which tools are most optimal for us


### Conclusions & Next Steps

In conclusion, the back-end functionalities, including machine learning models, are operating smoothly and are stable, while the primary issue with the front-end 
connection has not been largely resolved, leading to stagnation in synchronization with the back-end. Moving forward, we will continue to monitor and address any 
remaining or new issues in the front-end and back-end connection as the implementation of the asynchronous backend. 
We will also prepare for upcoming presentations by ensuring the entire program functions seamlessly and by creating comprehensive presentation materials that highlights.



