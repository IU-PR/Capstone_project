# Capstone project at Innopolis University

This is a repo of
the [Capstone project at the Innopolis University](https://capstone.innopolis.university/) - <https://capstone.innopolis.university/>

Table of contents

- [Capstone project at Innopolis University](#capstone-project-at-innopolis-university)
    - [Contribution rules](#contribution-rules)
    - [Run the website locally](#run-the-website-locally)
    - [Git essentials (for beginners)](#git-essentials-for-beginners)
    - [Shortcodes](#shortcodes)
        - [LaTeX](#latex)
        - [Mermaid (graphs)](#mermaid-graphs)
        - [PDF embedding](#pdf-embedding)
        - [Other shortcodes](#other-shortcodes)

## Short desciption of the project:
A puzzle-platformer game with a fairytale setting, mixed with cyberpunk elements. Involves the paper-like artstyle, simple but intriguing mechanics, and a touch of light phylosophy. Lamps are significant and playable objects: player advances through the levels and interacts with the world by manipulating them.
## Contribution rules

Throughout the project, you will be required to write progress reports. These reports will be published on
the [Capstone project website](https://capstone.innopolis.university/). To contribute to the website, you will need to
follow these steps:

1. On the first week:
    - One of the team member (e.g. `john5000`) should fork this repository under the name of the team (e.g.
      `dream-team`). This will create a copy of the repository under the name `john5000/dream-team`.
    - To edit reports, you can use online GitHub Markdown editor (easy way)
      OR [run this website locally](#run-the-website-locally) (more complex way)
    - Create a folder with your group name (same as the name of the forked repository e.g. `dream-team`)
      in `content/docs/$YEAR/` (e.g. `content/docs/$YEAR/dream-team`).
    - Create `_index.md` file in your group folder (e.g. `content/docs/2025/dream-team/_index.md`) with the following
      content:
      ```md
      ---
      bookCollapseSection: true
      title: "Dream Team"
      ---
      ```
2. All your progress reports should be stored in `content/docs/$YEAR/$TEAM` and should be named as `weekX.md`
   (e.g. `content/docs/2025/dream-team/week1.md`).
    - Your report should contain all the parts listed in the weekly tasks in the course description. The absence of any
      parts will lead to a decrease in grade.
    - If you need to add an image or file, add this file to your personal repository (NOT the current repository with
      reports), and specify a direct link to it in your report (the link must start with
      `https://raw.githubusercontent.com/IU-Capstone-Project-$YEAR`).
    - For images, you can use the syntax `![name](link)` (e.g.
      `![course_logo](https://raw.githubusercontent.com/IU-PR/Capstone_project/f667e54b1978116943533748cc02229ac0046ef7/static/capstone_logo.png)`.
    - **!!!** Note that if you create/modify/delete any other files other than your report, **you will not pass the
      CI/CD pipeline**, your changes will not be merged and your **report grade will be 0**.
3. After the weekly report is done, you will need to properly submit them via Pull Request so that no merge conflicts
   happen.
    - Open your github repo (e.g. <https://github.com/john5000/dream-team>)
    - Click on `Contribute` button
    - Click on `Open pull request`
    - Make sure that the base repository is `IU-PR/Capstone_project` and the base branch is `master`
    - Make sure that the head repository is your repository name (e.g. `john5000/dream-team`) and the head branch is
      `your-branch-name`
    - Name your pull request in a format `dream-team: Week X`
    - Once done, press `Create pull request`
    - Make sure that the CI/CD pipeline has passed. If not, fix the errors and push the changes again to your
      branch (you don't need to create a new pull request, just push the changes to your branch)
    - You can preview your changes by clicking on `Deploy preview` link provided by netlify bot in the pull request
      comments
    - Done! Admins will review your work and merge your changes into the main repo soon!

## Run the website locally

- Install latest version of [Hugo](https://gohugo.io/getting-started/installing/) on your local machine. Also, make sure
  you have a code editor installed. [VSCode](https://code.visualstudio.com/) is recommended, but you may use the one you
  prefer.

- Clone the forked repository **with submodules** to your local machine using

```bash
git clone --recursive https://github.com/john5000/dream-team
```

- To start the website locally, run

```bash
hugo server --minify --theme=hugo-book
```

- The last line in the terminal output should look like

```bash
Web Server is available at http://localhost:port/ (by default: http://localhost:1313/)
```

- Visit `http://localhost:port` in your browser to access your local instance of the website. Now all of you changes in
  the website's source code should be propagated automatically.

## Git essentials (for beginners)

After you feel you have made enough changes, run

```bash
git add .
```

to [stage all changes](https://git-scm.com/docs/git-add), then

```bash
git commit -m "Your very informative progress report that describes the changes you've made"
```

to [commit your changes](https://git-scm.com/docs/git-commit) to the local repository. Finally, run

```bash
git push
```

to [push your changes](https://git-scm.com/docs/git-push) to the remote repository or

```bash
git push --set-upstream origin your-branch-name
```

if you are pushing for the first time.

## Shortcodes

This blog template uses a handful of shortcodes. Shortcode *(in a nutshell)* is "mark" inside your markdown code that
enables certain features within its code block. For example, you can define a codeblock of LaTeX code that renders LaTeX
formulas. You can also define a codeblock that describes a structure of a graph. Below are example of these two.

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
3. Write necessary code

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

will be rendered as

```mermaid
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
```

Refer to [Mermaid documentation](https://mermaid.js.org/intro/) for examples.

### PDF embedding

To embed a PDF file, use the following shortcode:

```md
{{< embed-pdf
url="https://raw.githubusercontent.com/IU-Capstone-Project-2025/dream-team/refs/heads/master/reports/some-file.pdf" >}}
```

### Other shortcodes

This project's shortcodes and their descriptions can be found in `layouts/shortcodes`. They all use the same syntax:

```
{{<shortcode>}}
...stuff/..
{{</shortcode>}}
```

Try them out if you think they are useful in your progress reports.
