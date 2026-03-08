---
title: "Week #5"
---

# **Week #5**

## Feedback

### We gave our MVP to customers and asked them to give us feedback and answer questions. The questions we asked, in order:

- What do you think about the feature that allows using HTML as a project appearance? And what do you think about using AI for auto-generating it?
- What do you think about using Markdown as a project appearance?
- What do you think about AI-generated project tags?

### Sessions

#### Customer 1:
All's good, but why can random team members spam projects? I think only trusted leads should be able to start projects.

- This idea is absolutely terrible. There are a lot of vulnerabilities with HTML code and tags. I think you can't ensure that someone won't just add a malicious link or script. And editing the HTML code for changing project appearance will overcomplicate project management—it will be better to make your product as easy-to-use as possible (in my opinion).
- Sounds better, but use widespread formats, like .md files.
- Cool idea! And please, implement it as an additional feature with the ability to regenerate tags.

#### Customer 2:
In my opinion, it will be good to add a color (theme) switching button. I personally like working on the same site with a dark theme at night and a light theme during the day.

- I don’t know, HTML sounds hard.
- Yeah, if it's optional, I think it’s very nice.
- Good.

#### Customer 3:
It would be good if I could identify team members by their unique ID in their profile link. Also, add the ability to invite by those links.

- NO. Just no. HTML is for developers, not regular users. The last thing I need is teammates breaking layouts with hacked-together code.
- Simple formatting like headers and lists is really helpful.
- 10/10 – would save me some time for project setup.

#### Customer 4:
I think users should be able to change colors on the site.

- A security nightmare waiting to happen. My company would block this feature immediately.
- Love it, especially if it supports code formatting.
- A game-changer for saving time.

#### Customer 5:
The project is now looking raw, but I think the idea is good. In my opinion, you should focus on the main functionality instead of adding a lot of unusable features.

- Terrible UX. 95% of users will just want clean templates, not code wrestling.
- Yes, but only if the editor has a live preview pane.
- It will also be good if it learns from existing tag patterns.

#### Customer 6:
In my experience, role architecture makes the key difference between platforms. As soon as your goal (at least one of them) is to help build teams with random people, only the project founder should have access to inviting or kicking out members or managing project settings.

Absolutely not. This isn’t 1995.
Useful, but keep it simple.
Would help non-native English speakers with proper tagging.

#### Customer 7:
Add a footer to the main page.

Smells like a "Why was bank data leaked after visiting your website?!?!?!"
Good for README-style descriptions.
Tagging is my least favorite part of project setup; it would be nice.

#### Customer 8:
I think you are on the right path; keep going :)

Love it. Everyone with a unique design sounds awesome.
Ideal for proper noting.
Sounds useful; good if you implement it.

#### Customer 9:
I personally love the idea of having Markdown as a description; I don’t know why only GitHub/GitLab uses it.

Sounds interesting.
Good, I think you must implement it. It will be like your key feature.
Yes, but needs manual override.

#### Customer 10:
I like the minimalism style, auth also simple and good.

Laughs in cybersecurity.
Yeah, maybe.
Not sure.

### Analyze

- Abandon the idea of using HTML for styling due to the complexity of writing for clients and possible security issues
- Use Markdown as a formatting method because it is simple and clear
- Add AI tag generation with training on already entered tags.
- Only the project founder or trusted participants should manage access and structure

## Iteration & Refinement

### Implemented features based on feedback

- Now only a person with the founder role can create a project.
- Added the ability to change the theme on the site
- Updated main page

### Performance & Stability

Our application demonstrates a high level of performance:

Fast loading,

Stable interface,

Instant response.

There are no bottlenecks or reasons for optimization at the interface level.

![](https://github.com/IU-Capstone-Project-2025/ProjectOR/blob/main/docs/images/performance.jpg?raw=true)

### Documentation

We have md files in our project with instructions for launching the frontend and backend. There is also autodocumentation for the API

# Weekly commitments

## Individual contribution of each participant

**Timur Nabiullin**: 
- Conducted interviews with clients
- Found the main points of all clients' wishes and wishes
- Distributed priorities to each task

**Almaz Andukov**:
- Add functionality to create projects only for founder
- Add models: Applications and ProjectMemebers 
- Add route to apply for a project
- Add route to get new applications for a project
- Add route to get all applications for a project 
- Add route to approve application
- Edit project model to have more fields

**Nikita Timofeev**:
- Created new landing page
- Created project description page
- Add role selection window
- Add updated project creation window
- Implemented profile page

**Kirill Karsakov**: 
- Wrote a report
- Added new tasks to task board


## Plan for Next Week

- Complete any remaining high-priority features or bug fixes
- Conduct thorough final testing
- Code Freeze: Announce a code freeze date, after which only critical bug fixes are allowed
- Develop presentation slides covering
- Ensure README.md is comprehensive: project overview, features, tech stack, setup instructions, deployment link

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [x] In working condition.
- [x] Run via docker-compose (or another alternative described in the `README.md`).