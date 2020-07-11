---
layout: page
title: "Pairing with Matt Swanson on Jekyll, part 1: Finding a Good Issue to Work On"
published: false
description: ""
permalink: /matt-swanson-jekyll-bug-p1.md
image: ""
---

_First of a short series on pairing with a super-experienced software developer to fix an open-source issue in Jekyll_

## Context

A few weeks ago, I sent out this tweet:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">any Ruby devs interested in paid OSS work, recording their screen/verbalizing their thought process? <br><br>I&#39;ll process that recording, end-goal being &quot;a resource for early-career developers more quickly become mid-career developers&quot;<br><br>⁰⁰$100, hopefully will &lt; 2 hrs of your time.</p>&mdash; Josh Thompson (@josh_works) <a href="https://twitter.com/josh_works/status/1256667563963977728?ref_src=twsrc%5Etfw">May 2, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


I ended up connecting with Matt Swanson, and he thought my plan was interesting, so we did it!

Matt Swanson is _brilliant_, and I expect we'll be seeing a lot more of him around here. He's behind [Boring Rails](https://boringrails.com/), and has forgotten more about Ruby, Rails, and software development than ~I'll ever know~ I currently know. 🤞(I hope to someday learn more than he's forgotten...)

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">&quot;Do open source&quot; is common advice for devs trying to improve. But like...how do you actually do it?<br><br>Recorded a video w/ <a href="https://twitter.com/josh_works?ref_src=twsrc%5Etfw">@josh_works</a> of us<br><br>- Finding an issue<br>- Setting up codebase<br>- Fixing a bug<br>- Submitting a PR<br><br>Josh is going to pull out the highlights to share soon!</p>&mdash; matt swanson 🤔 🦢 (@_swanson) <a href="https://twitter.com/_swanson/status/1258868684921147395?ref_src=twsrc%5Etfw">May 8, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


Before we started, Matt found this _amazing_ Jekyll github issue to work on: [slugify replaces Tamil vowel marks with hyphen #7973](https://github.com/jekyll/jekyll/issues/7973)

We finished with this pull request: [Switch slugify regex to support more Unicode character groups #8167](https://github.com/jekyll/jekyll/pull/8167)

I recorded the whole session, but I'm not expecting you to watch two hours of pairing - I'm editing it, heavily, to show all of the thought process and to highlight as much of the [tacit knowledge](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/) as possible. 

## How Matt found this particular Jekyll issue

This video opens with Matt saying:

> People say, if you're looking to practice
> 
> > Oh, contribute to open source
> 
> and I think there is misrepresentation there of how easy that is to just... do.
> 
> Is it going to take five minutes, five hours, five days, five weeks?

And we spend the rest of this short (10 minute) video learning _from Matt_ how he found such a well-suited issue for us to work on.

I was particularly impressed with Matt because he was so good at _verbalizing his thought process_. So, jump in as he walks us through how he found this issue:

<embed video here>

- He walks through examining the _tags_ as an entry point, and how he "discards" most of the tags for further digging.
- Once he's looking at this particular issue, what is Matt looking for, and what is he ignoring? 


## What Matt noticed when looking through this particular Jekyll issue

_Timestamp: 4:23_

The user reported a bug, and gave a _very_ detailed explanation of the bug. 

_Lesson: The more detail you can give when raising an issue, the better_

When Matt said:

> This is *way* more detail than I would expect

My radar went off. We're about to learn something _very_ helpful, for opening/filing bug reports.

This bug report is _so good_ that Matt and I were able to fix the issue in _two hours_. If it were a lower-quality bug report, we would have never touched this issue. 

We both agree that neither of us know much about Unicode character encoding. _But we don't need to have extensive knowledge about Unicode to fix this bug._

Matt had to dig a bit to cross-reference detailed notes from the github issue and the linked StackOverflow question/answer. _This is par for the course_.

Matt:

> I didn't look up what this regex does...

He has some guesses about portions of the RegEx, but he still _doesn't need to know it in detail_. 



