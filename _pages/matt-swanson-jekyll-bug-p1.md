---
layout: jekyll-bug-fix-series
title: "Make an OSS Contribution, Part 1: Pairing with Matt Swanson on Jekyll"
published: true
description: "When you ask someone how to get better at software development, they might tell you to make open source contributions. That advice is hard to follow if you don't know how to do this, or how long it will take, or even what you'll get out of it. This is part 1 of a series where Matt Swanson and I work together on fixing a small bug in an open-source repo. This series isn't about us, though, it's about you, and helping you learn as much as I did from pairing with a senior software developer!"
permalink: /make-oss-contributions-part-1-finding-an-issue
image: ""
series_part: "Part 1"
---

_This is the second of a short series on pairing with a super-experienced software developer to fix an open-source issue in Jekyll_


Want to get updates on these posts as they come out?

<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>

## Context for Part 1

Remember, a recurring theme of these videos is to highlight as much [tacit knowledge](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/) as possible. 

-----------------------

<iframe width="560" height="315" class="youtube-video-embed" src="https://www.youtube.com/embed/_-m0MhmZfZk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




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

He has some guesses about portions of the Regular Expression, but he still _doesn't need to know it in detail_. 

Also, 👏👏👏 for Ambarish Sridharanarayanan, [@deepestblue](https://github.com/deepestblue), for opening this bug report. He not only opened the Jekyll issue, but he asked the StackOverflow question [Why do some Unicode combining markers (like \u0BCD) not match \[:alpha:\] in Ruby?](https://stackoverflow.com/questions/59707795/why-do-some-unicode-combining-markers-like-u0bcd-not-match-alpha-in-ruby) which led to the solution.

Had he _just_ opened the bug report, and not asked the StackOverflow question and then interpreted between the answers there and the solution posed in the Jekyll issue, Matt and I would have had nothing to work with. 

So, Ambarish has _truly_ done 90-95% of the work for resolving this issue. Next time you report a bug, ask yourself:

> What would Ambarish do?


## Checks for Understanding

I desperately desire for these videos to be of enormous value. That said, passively watching videos is a miserable way of learning things. 

How do I, the creator of this video, justify that this is time well spent?

Here's the general questions you should be able to answer after watching this video; they're all _generalizable_ to becoming a better software developer:

1. Why is "make open-source contributions" difficult advice to implement?
2. If someone suggested looking through open issues on the [Jekyll](https://github.com/jekyll/jekyll) project, what filters/tags would you end up using to find a good place to start? (hint - look at the issues, then _all three pages_ of labels)
3. Go ahead and [open up the issue we worked on](https://github.com/jekyll/jekyll/issues/7973). Find the specific StackOverflow answer that the issue reporter referenced, and find _the exact instance of the RegEx the user suggested_.
4. What are a few concerns about jumping in and trying to fix an issue someone else reported? Maybe not `concerns`, but `topics to be aware of`?
5.  What are a few related issues that are _not_ worth worrying about right now? (hint: configuration options, exact regex syntax, etc)


Next, head to part 2!

[Part 2: Setting up the app, basic investigation, and writing a failing test]({{ site.baseurl }}{% link _pages/matt-swanson-jekyll-bug-p2.md %})

-----------------------
