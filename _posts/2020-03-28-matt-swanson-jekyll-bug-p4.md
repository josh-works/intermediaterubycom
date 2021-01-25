---
layout: jekyll-bug-fix-series
title: "Making an OSS Contribution, Part 4: Making the PR"
published: true
description: "Matt and I prep the pull request; cleaning up the fix, making lots of little decisions as we go. Unsurprisingly, there are many decision points along the way."
permalink: /matt-swanson-jekyll-bug-p4
image: "images/matt-swanson-jekyll/2020-08-18 at 5.08 PM.jpg"
series_part: "Part 4"
---



## How to read this particular post

This is the last in this bugfix series. 

We convert our passing test to [this pull request](https://github.com/jekyll/jekyll/pull/8167). 

There's quite a lot of complexity to think through at every step of the way.

## Video Walk-through

<iframe width="560" height="315" class="youtube-video-embed" src="https://www.youtube.com/embed/Uvsc9S7qkUk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Video Timestamps

Coming Soon

## Expanding on what came up in the walk-through

### "Intermediate" Commit Messages VS Wip Commits

If you're not into verbose, detailed commit messages, it's probably OK. That said, if you've been inspired by the Chelsea Troy's [Commit Tracing](https://chelseatroy.com/2018/07/21/leveling-up-skill-6-commit-tracing/), and want to write commits good enough for _others_ to trace, you've got your work cut out for you.

I usually do a short commit message that loosely described what I did. Some commits are very bare, like `WIP - tweaking LoggedInAccountAdmin Factory`, others are verbose.

I often rebase my commits before making the PR, and selectively retain/drop/squash the less-useful commit messages.

I try to be concise, specific, detailed, and well-organized in my writing, which includes Pull Requests and commit messages. Some situations call for extreme brevity, others for extreme detail.

My thought is that I won't make further optimizations on my commit message writing until I have a specific reason to make them better - either to adhere to norms for the teams I work on, or because I've improved every other element of this software development thing and my inadequate commit messages are the primary thing holding me back from further improvement.

### Rubocop options

There's much we could say about Rubocop. For now, [here's a ton that I've written about it](https://github.com/josh-works/intermediate_ruby_obstacle_course/tree/master/rubocop), which is a synthesys of all the available resources I could find. 

### Merging the PR as-is

Here's the PR: [Switch slugify regex to support more Unicode character groups](https://github.com/jekyll/jekyll/pull/8167). It gets merged! There's a little conversational back-and-forth between a few folks. 

One maintainer wants to merge it as-is, another asks about adding a config option to opt-in for the change.

I made a case for making this change the default for accessiblity purposes: 

> This is certainly an edge-case fix, but I'm afraid that making it an opt in feature, the populations most positioned to benefit from the fix would now be implicitly required to go dig deep through the source code to figure out how to use this fix in a way that targets their use case.
> 
> Especially if the bug fix aids in slugifying non-standard characters, certainly all individuals who would use Jekyll for Tamil-language websites, or any other non-English website, _would be expected to read source code in English to accommodate their non-English use case_.

I don't know if what I said mattered at all, but either way, the maintainers marged the PR!


## Checks for Understanding

Coming soon!

----------------------------

## If I helped you, can you help me?

This was an unusual project, wasn't it? 

I have three ways I am going to ask for your help. Choose any, all, or none of them:
- Drop your email in below. I'll ask some questions via email, you can reply, and we'll go from there.
- A 30 minute zoom call! I'll ask questions, you'll provide answers, and I'll use that time to gether tons of valuable feedback. [Schedule that call here]()
- If you thought it was good, but don't really wanna do the email or video call thing, could you send this URL to a friend, or tweet about it? 





<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>

{% include jekyll-bug-fix-index.md %}