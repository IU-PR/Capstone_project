---
weight: 1
bookFlatSection: true
title: "BudgetAI"
---

  

# **BudgetAI**

Our team studies the use of low-rank adaptation (LoRA) of large language models (LLM).
We plan to take an existing language model as a base and fine-tune it using LoRA for
a programming-related downstream task.

{{< hint danger >}}
**Feedback**
  
Why are you doing this? Describe the purpose of the task and expected outcome. I suppose it should be a better model?
{{< /hint >}}

# **Week 1**
## Team Formation and Project Proposal
### Team Members

Please list the names and contact details (Telegram and email) of your team members:

| Team Member | Telegram alias | Email Address |
|-------------|----------------|---------------|
| Nikolai Nechaev | [@kolayne](https://t.me/kolayne) | n.nechaev@innopolis.university |
| Danil Meshcherekov | [@calandoassai](https://t.me/calandoassai) | d.meshcherekov@innopolis.university |
### Value Proposition

The topic of the project we are working on is application of LoRA in LLMs. I will leave
aside the discussion of importance of LLMs themselves and the benefits they give to
users. The goal of our project is to apply the LoRA algorithm to fine-tune already
existing language models for a specific downstream task. The use of LoRA allows for
more computationally- and memory-efficient model adaptation, compared to
the conventional means of language model fine-tuning, which still gives approximately
as good (sometimes even better) results.
  
{{< hint danger >}}
**Feedback**  

Is this LoRa applicable only to LLM's or you do something generally working with DL?
{{< /hint >}}
## Leveraging AI, Open-Source, and Experts

Our project relies on all the aforementioned resources heavily.
The single target outcome of our project is a machine learning model, so the whole work
is AI-centric.
We are going to use a publicly available and open-source-licensed language
model as a base and, most likely, train it on publicly available data. Even the key
algorithm we are using is a (publicly available) scientific article backed by a
corresponding open-source implementation.

Finally, we stay in close contact with our mentors who target us in terms of
supplementary materials and the roadmap of the project.
## Inviting Other Students
  
We already have a first-year bachelor studnet named Hadi Salloum working with our team
on this project. _Perhaps_, we could welcome more students in the team, on the other
hand, the current team size is probably optimal for the task we have chosen.

{{< hint danger >}}
**Feedback**  
Sounds very uncertain, imho
{{< /hint >}}

## Defining the Vision for Your Project

A complete, clear, and compelling vision is something that might not be the strongest
trait of us as a team because, as the first two weeks of our work have shown, we do not
have a wholesome vision of the goal we are going towards. We mitigate this by working
closely with our project's mentor, which also helps us to extend and deepen our vision.

{{< hint danger >}}
**Feedback**  
Considering that week 1 report was late and report do not describe much - 2/5
{{< /hint >}}
# **Week 2**
  
## Questionnaire

1. As of now, we are not utilizing any project-based books. However, we plan to base our project on scientific articles and publicly available open-source language models, see Question 4 for more details.

2. We believe that having a mentor in our project is vital since we initially did not have a clear vision or our goal, so we stay close to our mentor, Roman Garaev [@GRoman20](https://t.me/GRoman20), who has clarified the project's objective and provided our team with some supplementary materials.

3. We use the following resources as the primary sourse of knowledge:

-- Ashish Vaswani _et al._. Attention is all you need. [arXiv: 1706.03762](https://arxiv.org/abs/1706.03762)

-- Edward J. Hu _et al._. LoRA: Low-Rank Adaptation of Large Language Models. [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)

-- Tim Dettmers _et al._. QLoRA: Efficient Finetuning of Quantized LLMs. [arXiv: 2305.14314](https://arxiv.org/abs/2305.14314)

-- RedPajama 7B model ([Available here](https://www.together.xyz/blog/redpajama-7b))

4. Our biggest knowledge gap is not having a clear understanding of the core algorithms used in our project - transformers, LoRA, and QLoRA. ML ingineers in our group - Nikolay Nechaev,  Hadi Salloum, and Danil Mechsherekov - plan to address this issue with the help of our mentor and the materials provided by him.

5. At this point, we do not seek professional help from the tech community outside of Innopolis University.

6. The main objective of this week is for everyone to understand the topics mentioned above: how transformers, LoRA, and QLoRA algorithms work. As was mentioned above, we plan to achieve this with the help of our mentor and additional materials.

7. Our main means of communication is meetings. We conduct frequent meetings with all the team members and our mentor.

8. We have not employed any AI tool or platform in our studying yet.

{{< hint danger >}}

**Feedback**  

Alright, I like that this section is very detailed. Keep in mind it's only 7 weeks
{{< /hint >}}
## Tech Stack & Team Allocation

Our project has two distinct components:

- A backend component, a large language model based on RedPajama 7B model and the Pytorch library. This component is the main point of interest in our project, and it is managed by all three members of our team: Nikolay Nechaev, Hadi Salloum, and Danil Meshcherekov.

- A frontend component that will, tentatively, be a simple command line. Since we are not planning to include any graphics or complex user interface, we have not assigned anyone to this part of the project.

{{< hint danger >}}

**Feedback**  

I liked the project description part with technologies, but major aspects of the program are not discussed and it's not clear what are you trying to achieve - is it just the experiment? On which data? How are you planning to collect it?  
Could be better - 3.5/5

{{< /hint >}}
# **Week 3**

## Development Process

The biggest achievement of this week is assigning each member a task:

- Dataset parsing: downloading sources of data, parsing and creating datasets (Mahmoud Mousatat and Danil Meshcherekov);

- Building infrastructure: researching how to generalize the pipelines in current solutions and how to load the model/dataset (Nikolay Nechaev and Mostafa Kira);

- Evaluation: defining metrics fo chat bot performance (Hadi Salloum)

  

Here is what have we have accomplished this week:

- Mostafa Kira has trained one of the base models on a small instructions dataset. Now we know how to work with the models, and this aspect of our work will greatly increase our efficiency.

- Hadi Salloum has found various ways to measure the model's efficiency, from benchmarks to some custom ways to do so.

- Mahmoud Mousatat is searching for quality textbooks and have already found some of them.

- Nikolay Nechaev has dig into tools that we are likely to use and proposed the efficient way to collaborate while working on the project.

- We are now waiting to be granted access to the server where we will store the collected datasets and train the model.

## Prototype Features

As of this week, no prototype is ready.
In our team's opinion, all three parts are necessary for a prototype to work.

## User Interface

The main means of communication between the user and the language model is a command line; therefore, we do not plan to introduce any GUI in our product.

## Challenges and Solutions

We have a number of challanges.

Firstly, we still have not decided on how data in dataset should be represented; we have tentatively settled to use a json file with a source, prompt, and an answer for each prompt.

Secondly, we do not know what sources to use to train our model; would high quality data from textbook be sufficient, or should we also include open-source Haskell snippets from Git and Stackoverflow answers. As a solution for this question we would like to train and compare two different models: trained on our data only and trained on all data.
 

Lastly, as it was mentioned above, it is still not clear what metric would be most suitable for measuring our model's performance.

## Next Steps

Our plan for the upcoming weeks is to address the challenges discussed above:

- We need to make a final decision on what resources we will use for training our language model and how to design the dataset for it;

- We need to make a final decision on the metric for evaluating the model's performance;

- We need to assemble all the necessary parts to use them on a server.

{{< hint danger >}}

**Feedback**  

Consider adding more details about the project. Describe the things get done last week and what needs to be done to accomplish the project.
Overall, 4/5 for the week

{{< /hint >}}

# **Week 4**

The topic of this week is external feedback, testing, and iteration. Unfortunately, we are not quite there yet
to even have an early prototype, that's why at the current stage we are not yet ready to start testing our
product or collecting feedback for it not only in the community, but even among the team members.

As for the iterative development, I am happy to say that this is something we do apply in our teamwork. Twice
a week we gather all (or almost all) together and discuss the progress each of us has made in the direction
they were working on and assign new tasks to work on. During these meetings we discuss the project and our
views on its further development. This helps us to synchronize both in terms of vision, when some of the team
members have different understanding of a particular feature or implementation detail, and in terms of
individual progress, so we can make sure no one is stuck with their assigned task.

One thing that has changed in our workflow this week is that we started using YouTrack for tasks description
and assignment. It has several advantages, for instance, all the tasks and the assigned workers can be easily
viewed on a single page, all the details of assignments are written down, so it's easy to refresh, etc.

Here are some of our current tasks:

-   Understanding the [Stack dataset](https://huggingface.co/bigcode).
    <br>
    Make sure it fits our purpose well (that is, contains enough data related to Haskell), understand how to
    work with it, e.g., load only the desired data.

-   Come up with a filtering algorithm for StackOverflow dataset.
    <br>
    Propose a filter that would help to distinguish high-quality StackOverflow answers that are worth learning
    from garbage.

-   Develop a script for loading books from [LibGen](https://libgen.is).
    <br>
    One of the sources we are considering for potential use is Library Genesis. The task is to develop a script
    for automated books downloading.

-   Extract data from CodeForces.com
    <br>
    Another suitable resource is the competetive programming website [CodeForces.com](https://codeforces.com),
    more specifically, the problems that have public Haskell solutions. The task is to parse and collect
    the appropriate problems and their solutions.

etc... Quite some work to do!

{{< hint danger >}}

**Feedback**  

Alright, this week report is better. Consider showing some intermediate results and expected timeline for the first prototype
4/5 for the week
{{< /hint >}}

{{< hint danger >}}

I know you have been busy building the model, and have accomplished a lot!
However, I don't see the report.
0/5 for the week
{{< /hint >}}