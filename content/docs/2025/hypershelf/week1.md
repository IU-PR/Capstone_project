
![repo-banner](https://github.com/user-attachments/assets/d399bea8-f6dc-4581-987c-dda419c1aa4e)

> Repo: https://github.com/IU-Capstone-Project-2025/hypershelf

# Team members

| Name              | Telegram ID                           | Email Address                     | Track | Responsible |
| ----------------- | ------------------------------------- | --------------------------------- | ----- | ----------- |
| Daniil Gazizullin | [659800858](https://t.me/dgazizullin) | d.gazizullin@innopolis.university | SD    | Full-Stack  |

# «Why we need it?» a.k.a the Problem

Right now, cybersecurity training environments suffer from a major issue: asset tracking. Teams spin up vulnerable VMs, update tasks in Confluence, Google Sheets, Excel, Notion or Obsidian, and there's zero consistency or transparency between different company teams. You have no reliable record of who changed what, when, or why, and, consequently, no single source of truth for the asset's current status. The result is an endless game of detective work, reconciling half-baked spreadsheets and disconnected wikis just to figure out the status of the particular task.

This is particularly annoying right before the polygon deployment - let me give you the example:
First, you look at the team of __Developers__. They use Google Sheets for asset tracking

![CleanShot 2025-06-07 at 8  02 06@2x](https://github.com/user-attachments/assets/7c4d1f27-258d-48a0-afd6-253f6984038a)

So, the task `broslers` is done? No. The status _Done_ here means that it's completed by **Developers**.
But what about **Auditors** - the people, who spin up the audit software on the tasks? They use YouTrack to track statuses

![CleanShot 2025-06-07 at 8  12 48@2x](https://github.com/user-attachments/assets/ef2ba8ff-e710-403e-8295-a218ea43f93a)

So **Auditors** are done, but waiting for **Developers** to finish, so the task is in `Hold On` state. But wait, **Developers** are done, so... Are **Auditors** done? You send an email to check. They reply

> *Hey! Yeah, we are done on our side. I checked with Bob, they are done as well. But just to be sure, check with SOC as well.*

So you go to yet another team to check. **SOC** checks, that **Auditors** have done everything correctly and tell you "_ok from us_".
And all this to check the status of the VM.

What if the data in Google Sheets and Confluence is different? Like, say, in Confluence it says that the IP of `broslers.local` is `10.0.0.8`, but in Google it's `10.0.0.1`. And to pile it up, in YouTrack the comment says `10.0.0.80`. Whoever you trust the most...

This is just the example, but exactly the same happens in real life. Communication between teams is weak, since everyone uses different platforms - that is why if you change something, you need to change it in many different places, and even then the _stuff_ happens...

The general idea and goal of the project is to completely eradicate this and make **all** information up-to-date for **everyone**.

# Hypershelf

One could say that this project is a recreation of Google Sheets, and I might even agree with them. The goal is to provide a tailored solution for a particular task - with reliability, good design, easy integrations and specific features, which are not possible in Google Sheets without plugins.

# Market research

The market research in the scope of this project boils down to the real issue we have at our company, which no one is willing to put time and effort into solving. Once I told my colleagues about Hypershelf, they were excited to see the early demos and suggested new features tailored to their specific job position. As an example, architect asked me to build a synchronization layer with our hypervisor to check the current state of VM deployment and adhesion to the original office architecture.

# Key requirements

- Reliability - if the data was updated on the website, it 100% was updated in the database. At least 4 nines SLA.
- Design and accessibility - pretty interface, which is easy to use for everyone.
- Mutex - only one person can work on the asset at a time. Lock it in before interacting with the item, release after you are done - eliminates conflicts.
- Universality - a single table of properties per asset for all teams to get rid of the desynchronization between different management solutions.
- Usability - static views for each team with the information they need - nothing else.
- Flexibility - deep integration with VMWare vSphere, Confluence, YouTrack, Jira and anything else through flexible plugin system.
- Sync - real-time database synchronization layer to further trim the possibility of a conflict when editing the asset.

# Optional Features

- Markdown editor
- SSO support
- OAuth2

# Tech Stack

- Next.JS + React + Typescript + Prettier + Convex Client
- Patroni + etcd + pgBouncer
- Convex Backend
- Docker with compose (dev), Ansible (prod)
- HAProxy
- Keepalived
- SLA-SLO monitoring tool (TBA: Uptime Kuma / Zabbix / SLO-tracker / ...)

# Architecture

Allows for unlimited horizontal scaling while being pretty compact.

> [!WARNING]
> Architecture is not final and is subject to changes, even major reorganization is possible.

![image](https://github.com/user-attachments/assets/9e8c7408-b3fe-4d4a-a66a-089b140cb6e2)

# Week 1 results

- Development environment using Docker (backend + dashboard + Postgres)
- Pitch with detailed features and architecture
- Complete login + sign up pages, with working backend
- Started working on the main assets page and field management page
- Started researching Ansible to deploy everything bare-metal

Authentication page:
![Pasted image 20250610213659](https://github.com/user-attachments/assets/7a6d81a9-548c-4cc0-a8bf-640d344344e1)

Deployed convex dashboard:
![Pasted image 20250610213743](https://github.com/user-attachments/assets/b6e1ad08-2f45-4ce8-817a-5fabebd191a0)

Fields management page:
![Pasted image 20250614142519](https://github.com/user-attachments/assets/35503949-7612-4b1f-ad56-fc2bef2691d3)

Two different sessions with live sync and locks to prevent edit conflicts:
![Screenshot 2025-06-14 at 2 22 53 PM](https://github.com/user-attachments/assets/41e993a4-64cd-426e-9a1c-2e0e55eadd1c)

# Plans ahead

![Screenshot 2025-06-14 at 4 03 53 PM](https://github.com/user-attachments/assets/3329ac48-700b-4a4e-b96d-70b1d7fd96d4)


# Conclusion

As discussed with TA, the code is in working condition, though is pretty hard to deploy due to Convex (and will be even harder due to multiple servers architecture). Going forward I will deploy the project on my infrastructure and provide the link in the project report, as soon as I get access to servers.
