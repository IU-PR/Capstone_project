---
title: "Week #6"
---

# **Week #6**

## **Presentation**:

{{< embed-pdf url="/2024/semargl/presentation.pdf" >}}

## **Weekly Progress Report**:

Our team finished module loading funcitonality and tested it in virtualized environments. We made a significant progress connecting GUI client to gRPC protocol. 

### **Challenges & Solutions**

#### 1. Loading modules from memory

To implement extensible and dynamic behaviour of agent, we needed to implement module loading from memory, not from disk. This means that server will transfer binary (DLL or shellcode) to an agent and execute a function inside it.

We leveraged a technique called DLL `LoadLibaryA()` and `GetProcAddress()` for it.

#### 2. Fetching MITRE ATT&CK TTPs

The MITRE does not have well documneted feed for TTPs, so we needed to implement a parser for the website. Now, the parser takes data from website to form local database for semargl.

Currently we are planning to host the database in separate repository (like in `nuclei` and `wpscan`), so clients could dynamically load it without need to update the semargl itself.

### **Conclusions & Next Steps**

Our team did a good work implementing core features that was in high demand for a end users.

Out next steps include:

- Form a presentation with understanable and comprehensive demo
- Add help or guide to GUI for helping new users
- Update documentation on the website
