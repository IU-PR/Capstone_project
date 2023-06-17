---
weight: 1
bookFlatSection: true
title: "BudgetAI"
---

# BudgetAI

Our team studies the use of low-rank adaptation (LoRA) of large language models (LLM).
We plan to take an existing language model as a base and fine-tune it using LoRA for
a programming-related downstream task.

# Week 1

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

## Defining the Vision for Your Project

A complete, clear, and compelling vision is something that might not be the strongest
trait of us as a team because, as the first two weeks of our work have shown, we do not
have a wholesome vision of the goal we are going towards. We mitigate this by working
closely with our project's mentor, which also helps us to extend and deepen our vision.

# Week 2

## Questionnaire
1. As of now, we are not utilizing any project-based books. However, we plan to base our project on scientific articles and publicly available open-source language models, see Question 4 for more details.
2. We believe that having a mentor in our project is vital since we initially did not have a clear vision or our goal, so we stay close to our mentor, Roman Garaev [@GRoman20](https://t.me/GRoman20), who has clarified the project's objective and provided our team with some supplementary materials.
3. We use the following resources as the primary sourse of knowledge:
-- Ashish Vaswani _et al._. Attention is all you need. [arXiv: 1706.03762](https://arxiv.org/abs/1706.03762)
-- Edward J. Hu _et al._. LoRA: Low-Rank Adaptation of Large Language Models. [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
-- Tim Dettmers _et al._. QLoRA: Efficient Finetuning of Quantized LLMs. [arXiv: 2305.14314](https://arxiv.org/abs/2305.14314)
-- RedPajama 7B model ([Available here](https://www.together.xyz/blog/redpajama-7b))
4. Our biggest knowledge gap is not having a clear understanding of the core algorithms used in our project - transformers, LoRA, and QLoRA. ML ingineers in our group - Nikolay Nechaev,  Hadi Salloum, and Danil Mechsherekov - plan to address this issue with the help of our mentor and the materials provided by him.
5. At this point, we do not seek professional help from the tech community outside of Innopolis University.
6. The main objective of this week is for everyone to understand the topics mentioned above: how transformers, LoRA, and QLoRA algorithms work. As was mentioned above, we plan to achieve this with the help of our mentor and additional materials.
7. Our main means of communication is meetings. We conduct frequent meetings with all the team members and our mentor.
8. We have not employed any AI tool or platform in our studying yet.

## Tech Stack & Team Allocation
Our project has two distinct components:
- A backend component, a large language model based on RedPajama 7B model and the Pytorch library. This component is the main point of interest in our project, and it is managed by all three members of our team: Nikolay Nechaev, Hadi Salloum, and Danil Meshcherekov.
- A frontend component that will, tentatively, be a simple command line. Since we are not planning to include any graphics or complex user interface, we have not assigned anyone to this part of the project.
