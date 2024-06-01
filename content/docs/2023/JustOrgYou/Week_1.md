---
weight: 1
bookFlatSection: true
title: "Week #1"
---

# Week #1 Report

## Team Members

| Team Member        | Telegram ID                                            | Email Address                       |
| ------------------ | ------------------------------------------------------ | ----------------------------------- |
| Gurniak Nikita     | [@care_your_eyes](https://t.me/care_your_eyes)         | n.gurniak@innopolis.university      |
| Ragulin Aleksandr  | [@sunya_shine](https://t.me/sunya_shine)               | a.ragulin@innnopolis.university     |
| Stepan Tsepa       | [@tsepan](https://t.me/tsepan)                         | s.tsepa@innopolis.university        |
| Diana Tomilovskaya | [@diana_tomilovskaya](https://t.me/diana_tomilovskaya) | d.tomilovskaia@innopolis.university |

## Value Proposition

### Intoduction

Many people, especially related to business and educatuion, deal with significant amount of tasks, notes, reminders and also other people. Keeping everething in head is complicated task when number of actions overhelm person. So, time and task management systems were introduced. Nowadays one of the famoust ones is Getting Things Done (GTD further) by David Alen. 

Now, let's define a couple of words. By **GTD** we mean superset of systems, so solving general problem solves any particular. And by **tasks**, **entry** we assume any action, note and other thing that come from _inside_ or _outside_ of your _brain_. 

#### Abstract GTD system review

Let's quickly review key points of abstract GTD system:

- _collect_ all incomming tasks in inbox
- process inbox, _sort_ entries to _N categories_ (originally N = 7)
  - `TODO`
  - `Waiting`
  - `Someday`
  - `etc`
- Follow _your_ rules with categories
  - do things in `TODO` during week
  - review `Someday` to not forget
  - any other rules

Without loosing customization abilities, we cover really many time management systems. Even when person write notes on paper and process it immediately by pinning on the board. So, we narrow down a bit. 

Assumptions that we keep in mind:
- digital word require digital task management systems
- we don't really thing how user will actually do its tasks. It is up to you to go for the milk, not task management system.
- future proof: don't create irreplaceble solution, system should be as comfortable as possible, but user is free to choose.
- easy to integrate. Solution should _not_ force to _migrate from or to. Just use it _with_


### Pain points

We've used GTD as our task management system for a while. With different software, different devices and different circumstances. Also, we participate in chats with people that uses GTD and some of us took cource from experienced time manager. So, we heart and fealt a lot about pain during system usage.

The main **pain points**:
- adding new task is time consuming, hard to do it on the go
- UI is too distrupting, hard to quickly add thing
- process of sorting is too long
- process of sorting is too complicated
- too complicated for newcommer to set up environment
- no unified way to work on desktop and on mobile device
- intenet is unreliable
- inbox processing on mobile device is very painful (due to device specific)
- no app that **keep in mind** GTD aspects


## Solution - JustOrgYou

We have concrete cases to work with. And we are in "the same boat" with customers. So, to solve the problems we developed application **designed** to work with any task management subsystem that we've defined earlier. It is quite a big deal to do, isn't it? Let's proceed to details.

### Architecture

We design system to be abstract from details of concrete formats and user flow. To do this, we split app into parts
- `todo library` handle bare work task entries. Contain business logic of their merging in example.
  - Also low level dependecies for file format parsing included
- `frontend` literally any module to interact with user. It does not "think" but keep user state and call `todo library`
- `api server` simple web component that provide api abstraction over additional (mainly AI) features.
- `AI models` contain hard to deploy locally business logic. App not depends from them so offline is not a problem. Like Copilot extention works.

<!-- todo add image -->

### Technologies stack

We plan to write `todo library` on **Rust** to get performant solution what not require runtime (for web possible integration). Also, it's **Rust**, so definitely yes!

`frontend` is going to be in several variations. _Mobile_ and _desktop_ apps on **Flutter**. Maybe _web_ too, we've tested, it is possible. And _cli_ client also on **Rust**.

For `api server` we've chousen **Python**. Servers on it are simple to develop, easy to maintain and performant enough. 

`AI models` are dependend from concrete case, but our code will be on **Python**. 

## Lean Startup Questionnaire #

> What problem or need does your software project address?
JustOrgYou solves pain during digital GTD system maintaining. It helps to spend more time on deals not to planning them.

> How will you validate and test your assumptions about the project?
We have well defined pain points and community to share solution with. So, we plan to share and get feedback.

> What metrics will you use to measure the success of your project?
Firstly, we are currently suffer from problems above. If we stop, then project is successive at least for us. Secondly, open source community is free to fork, star and PR! Activity is a metric. And thirdly, we are going to get feedback from GTD community.

> How do you plan to iterate and pivot if necessary based on user feedback?
 is modular and library handle most of basic operations (CRUD at least), so changing UI is not big deal. But any change should be meaningful. And welcome to fork)


{{< hint danger >}}
**Feedback**  
**Value Proposition**

How do you differentiate for mother solution? 
Where are your uses cases, impact and user benefits? 
When writing the report try to answer what in the template and don’t neglect them 

**Lean startup question**

Weak, you didn’t take any consideration while answering the questions.

**AI** 

Missing 


**Vision Of The Project**

Missing

**Overall**
The report is weak, and need to redo it. Beside half of the report is missing

1/5

_Feedback by Moofiy_
{{< /hint >}}
