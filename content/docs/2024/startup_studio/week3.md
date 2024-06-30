---
title: "Week #3"
---

# **Week #3**

This week our team has been working on both the frontend and backend parts of our project. First of all we worked on authorization, monitoring and cluster manager, as well as configured the manifest builder. To monitor and help each other our team organized meetings several times this week.

## **Backend Development**:

### **Authorization Service**:

On the backend, we developed authentication service
using [JWT concept](https://datatracker.ietf.org/doc/html/rfc7519) and role-based access control. This service
handles user registration, login, and password hashing to ensure security. The primary feature of this service, user
authentication and authorization, is nearly complete. The only remaining step is to integrate authorization in all the
routes, that require protection.

### **Manifest Builder**:

We have also developed a service that generates manifests for applications. This service is responsible for creating
an abstraction layer between user and k8s entities, to ensure that our app will keep backward compatibility with
[parental](https://helm.sh/) project (since it can be integrated inside our project to validate and test manifests),
we decided to use manifests rendering via Jinja2 templates. At first, we constructed manifests itself, and then made
it generic and implemented some templating techniques. At the end of the day we got those items: namespace, deployment,
service, horizontal-pod-autoscaler manifests. Those manifests are dynamic and logically correct, so we can use them in
k8s.

### **Cluster Manager**:

For the cluster management service, we built some basic logic this week. We connected kubeconfig and integrated k8s API.
In details, we used [kubernetes](https://pypi.org/project/kubernetes/) client for Python, parsed our kubeconfig from a
remote cluster and connected it to our app. Furthermore, we introduced creating of project (or namespace in terms of
k8s)
and application itself. At first, we go to manifest builder and then ask it to validate user's request and render
manifests,
then we apply those manifests to the cluster. Finally, we get working application, deployed in our cluster and VPC.

Our API http://babyhelm-api-svc.taila53571.ts.net/docs 

## **Frontend Development**:

We successfully implemented the login and registration pages on the frontend. These pages are now fully functional and
connected to the backend, allowing users to register and log in seamlessly.

![Main page](/2024/startup_studio/main_page.png)
![Login](/2024/startup_studio/login_page.png)
![Registration](/2024/startup_studio/registration_page.png)

## **Technical Infrastructure**:

In general, infrastructure is the most important part of our project. We have set up a Kubernetes cluster on premise,
and here are the components we use, which were fully described in report week 2: K8S cluster (core component), Prometheus/Grafana (monitoring), PostgreSQL (data management),
Tailscale (VPC), Nginx (reverse proxy for frontend). All the components are hosted on VM's from different cloud providers, such
as timeweb, cloud.ru and firstfvds. 

### **Monitoring system**:

Regarding monitoring, we initially aimed to use Splunk but found it challenging to configure and not meeting our
expectations. We switched to Prometheus, which offers more robust and ready-made solutions for cluster monitoring. We used kube-state-metrics that is focused on generating completely new metrics from Kubernetes' object state. We completed the configuration of Prometheus this week, and we now have fully functional dashboards in Grafana where we can
monitor our namespaces. New user namespaces will also be displayed on these dashboards, allowing users to monitor their
applications effectively. 

![Grafana Dashboard](/2024/startup_studio/grafana_dashboard1.png)
![Grafana Dashboard 2](/2024/startup_studio/grafana_dashboard2.png)
![Grafana Dashboard 3](/2024/startup_studio/grafana_dashboard3.png)
![Grafana Dashboard 4](/2024/startup_studio/grafana_dashboard4.png)


You can visit our dashboards here: https://grafana.babyhelm.ru/dashboards

Login: visitor Password: visitor

### **Prototype Testing**:

You can take a look at our site yourself, but since we have everythtake iting running inside a virtually-private-cloud,
you need to join our private network, here are the steps to:

1) Install tailscale (you will need VPN or proxy to do it)

   For Linux **curl -fsSL https://tailscale.com/install.sh | sh**

   For Windows https://tailscale.com/download/windows

   For MacOS https://tailscale.com/download/mac

2) Connect to our VPN (via CLI)

   **tailscale up --auth-key tskey-auth-kZKWRrf2dD11CNTRL-LiVxGmRYbvF3krEfGPh8vFGUT45ELF5sa**

3) Visit our frontend

   http://babyhelm-front-svc.taila53571.ts.net/

### **Challenges & Solutions**

**Difficulties with metrics:**\
We use kube-state-metrics, of which we found only two versions. Each has its own disadvantages. One gives metrics for
telemetry only, the other does not give detailed metrics for cpu usage and memory of pods. In the end we chose the
second version, but we had to figure out how to convert the metrics that are available to us to the ones we need. To
solve the problem we used PromQL.

**Migrations issues:**\
For database migrations we used alembic and encountered some issues with our development, we had several migrations
that were not connected with each other (no downgrade revision specified). So we manually removed them and created new
ones. In real production this would lead to disaster xD, since we will probably lose tables consistency and lose user
data.

### **What could be done better**:

Metrics, we could spend more time on research and not stop at one not-so-successful monitoring solution (Splunk).

Migrations, we could review MR's and add fixes quicker, without stretching this process over several days, this way 
we will not get any conflicts.

### **Plans for next weeks**

Looking ahead, our focus for next week includes:

- Creating a page for user where he can see his projects. Also we want to have subpage for applications from projects.
- Developing an application deployment page for inputting Docker image details and project configurations.
- Continuing to build out the cluster management service with a focus on namespace control and resource allocation
  logic.
- Finish dashboard and make dynamic links for user
- Add alerts for metrics anomalies
- Test authentification service and develop role-based authorization