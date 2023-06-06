# Capstone project at Innopolis University:
This is a repo of the [Capstone project at the Innopolis University](https://capstone-pr.netlify.app/) - https://capstone-pr.netlify.app/

Table of contents
- [How to contribute](#how-to-contribute)
  - [Pull requests](#pull-requests)
  - [Shortcodes](#shortcodes)
    - [LaTeX](#latex)
    - [Mermaid (graphs)](#mermaid-graphs)
    - [Other shortcodes](#other-shortcodes)
  - [Familiarize yourself with our techstack](#familiarize-yourself-with-our-techstack)

## How to contribute
If you **do not have** the repo on your machine:

- Make sure you have [git](https://git-scm.com/downloads), [hugo](https://gohugo.io/installation/), and any code editor installed ([VSCode](https://code.visualstudio.com/) is recommended, but you may use the one you prefer)
- Clone the repository **with submodules**: 
  ```
  $ git clone --recursive https://github.com/IU-PR/Capstone_project.git
  ```
  (Note) If you have already clone this repo without submodules, run this from the source directory
  ```
  $ git submodule init && git submodule update
  ```
Now you can start contributing:
- To start the website localy, run
  ```
  $ hugo server --minify --theme=hugo-book
  ``` 
- The last line in the terminal output should look like
  ```
  Web Server is available at //localhost:some-port-number/ (bind address 127.0.0.1)
  ```
  Visit `localhost:some-port-number` in your browser to access your local instance of the website. Now all of you changes in the website's source code should be propageted automatically.

- After you feel you have made enough changes, run <br> 
  [`git add .`](https://git-scm.com/docs/git-add),<br>
   then <br>
  [`git commit -m "Your very informative progress report that describes the changes you've made"`](https://git-scm.com/docs/git-commit). 

Note that this saves and documents changes on your machine only.

**Important note!**

- Group leads and personal track participants have to be collaborators to do changes in this repo. We will collect a list with your Github ID's and give you the rights
- You need to open your own branch to start making your progress report contributions! Name of the branch should be "**group_name/family_name**"
- After project is over, we will ask you to make a pull request into a master branch, so we can collect all reports ito a single document/blog
- Don't forget to pull changes from the master branch, we will be publishing weekly tasks and updated information!

## Pull requests
Now that you have made your changes, you will need to properly submit them so that no merge conficts happen.<br>
 To do so:
- Switch to a new branch *(if you haven't done that already)*:
  ```
  $ git checkout -b <branch>
  ```
  Ex: `git checkout -b My_Cool_Project_Group_Name`
- If you have any changes left uncommited, commit them as usual
- Push your new branch to the server
  ```
  $ git push origin <branch>
  ```
**Instructions to merge your branch with the master branch**

It should push the branch normally. If not, send the error to the group.
Make sure to run [`git pull`](https://git-scm.com/docs/git-pull) before you make any new changes after you've pushed, so that you avoid creating merge conflicts.

- Now go to the [github repo](https://github.com/IU-PR/Capstone_project)
- Press ["Pull requests"](https://github.com/IU-PR/Capstone_project/pulls)
- Press ["New pull requests"](https://github.com/IU-PR/Capstone_project/compare)
- Press "Create pull request"
- Describe what have you modified, maybe provide some suggestions for future imporvements
- Once done, press "Create pull request"
- Done! Admins will review your work and merge your changes into the main repo soon  

## **To upload images into your report .md file**  
 Please, create a folder with your group name in /static/your_group_folder/your_images.png

  
## Shortcodes
This blog template uses a handful of shortcodes. Shortcode *(in a nutshell)* is "mark" inside your markdown code that enables certain features within its code block. For example, you can define a codeblock of LaTeX code that renders LaTeX formulas. You can also define a codeblock that describes a structure of a graph. Below are example of these two.

### LaTeX
How to write in LaTeX:
```md
{{<katex>}}
your latex formula
{{</katex>}}
```
This produces an inline formula. If you want to center your formula, use `display` property like so:
```md
{{<katex display>}}
your centered latex formula
{{</katex>}}
```
[Latex cheatsheet](https://wch.github.io/latexsheet/latexsheet.pdf)

### Mermaid (graphs)
How to create graphs:
1. [Take a look at Mermaid syntax](https://mermaid.js.org/intro/)
2. Pick a graph you want to use
3. Write neccesary code
 
**Ex:**
```md
{{<mermaid>}}
gitGraph
  commit
  commit
  branch develop
  commit
  commit
  commit
  checkout main
  commit
  commit
{{</mermaid>}}
```
This will produce a git graph. There are 12 other graph types you can use. Refer to [Mermaid documentation](https://mermaid.js.org/intro/) for examples.

### Other shortcodes
This project's shortcodes and their descriptions can be found in `layouts/shortcodes`. They all use the same syntax: 
```
{{<shortcode>}}
...stuff/..
{{</shortcode>}}
```
Try them out if you think they are useful in your progress reports.