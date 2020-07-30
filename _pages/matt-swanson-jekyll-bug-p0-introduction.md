---
layout: jekyll-bug-fix-series
title: "Make an OSS Contribution, Part 0: Introduction"
published: true
description: "'When you ask someone how to get better at software development, they might tell you to make open source contributions.' That advice is hard to follow if you don't know how to do this, or how long it will take, or even what you'll get out of it. Here's the series introduction to a curated, annotated, edited pairing session where Matt and I worked on a bug in the Jekyll codebase. "
permalink: /make-oss-contributions-part-0-introduction
image: ""
series_part: "Part 0"
---


## Why This Series Exists

A few weeks ago, I sent out this tweet:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">any Ruby devs interested in paid OSS work, recording their screen/verbalizing their thought process? <br><br>I&#39;ll process that recording, end-goal being &quot;a resource for early-career developers more quickly become mid-career developers&quot;<br><br>⁰⁰$100, hopefully will &lt; 2 hrs of your time.</p>&mdash; Josh Thompson (@josh_works) <a href="https://twitter.com/josh_works/status/1256667563963977728?ref_src=twsrc%5Etfw">May 2, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

I ended up connecting with Matt Swanson, and he thought my plan was interesting, and was willing to help me out.

Matt Swanson is _brilliant_. He's behind [Boring Rails](https://boringrails.com/), and has forgotten more about Ruby, Rails, and software development than <strike>I'll ever know</strike> I currently know. 

I hope to someday learn more than he's forgotten. 🤞

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">&quot;Do open source&quot; is common advice for devs trying to improve. But like...how do you actually do it?<br><br>Recorded a video w/ <a href="https://twitter.com/josh_works?ref_src=twsrc%5Etfw">@josh_works</a> of us<br><br>- Finding an issue<br>- Setting up codebase<br>- Fixing a bug<br>- Submitting a PR<br><br>Josh is going to pull out the highlights to share soon!</p>&mdash; matt swanson 🤔 🦢 (@_swanson) <a href="https://twitter.com/_swanson/status/1258868684921147395?ref_src=twsrc%5Etfw">May 8, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


Before we started, Matt suggested this Jekyll github issue to work on: [slugify replaces Tamil vowel marks with hyphen #7973](https://github.com/jekyll/jekyll/issues/7973)

We finished with this pull request: [Switch slugify regex to support more Unicode character groups #8167](https://github.com/jekyll/jekyll/pull/8167)

I recorded the whole session, which was two hours, end-to-end, from 
> how Matt found this particular issue

to 

> writing a test that fails, making it green, refactoring, and then making/submitting the pull request.

I learned a lot, and more importantly, there was a lot of information that we covered as we worked through this fix of a real-world problem that would be of great value to early-career software developers, specifically _tacit knowledge_.

I'm editing it down, optimizing for moving quickly through what we did, to show all of the thought process and to highlight as much of the [tacit knowledge](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/) as possible. 

## What is Tacit Knowledge

Cedric Chin wrote something recently that gave me language for a phenomina I'd felt for years but never figured out how to say directly. 

Quoting from his piece [Why Tacit Knowledge is More Important Than Deliberate Practice](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/)

> Tacit knowledge is knowledge that **cannot be captured through words alone.**

He goes on to say:

> ...[T]acit knowledge does exist, and understanding that it does exist is one of the most useful things you can have happen to you. 
> 
> Once you understand that tacit knowledge exists, you will begin to see that big parts of any skill tree is tacit in nature, which means that you can go hunting for it, which in turn means you can start to ask the really useful question when it comes to expertise, which is: _that person has it; that person is really good at it; how can I have it too?_

This tacit knowledge stands in contrast with _transmissionism_. There are communities of people, lets call them "transmissionists", who think that all knowledge one can obtain or need can be communicated directly, explicitely, in a book or a lecture.

Cedric explains transmissionism thusly:

> In pedagogy, this is known as ‘[transmissionism](https://andymatuschak.org/books/)’, and it is regarded amongst serious educators with the same sort of derision you and I might have about flat-earth theories today. 
> 
> It goes something like this: some people believe that it is possible to teach technique by explaining things to others. They think that if you can find just the right combinations of words with the right sorts of analogies; if you can really break things down into the right level of atomic details, things will magically click in their students’s heads and [the students] will succeed. 
> 
> Such people have likely never attempted to do so in a serious manner. 

I've spent hundreds of hours over the last few months (and years!) helping less experienced software developers learn their craft.

Over and over again, I've seen the truth of this statement. 

It's completely impossible to impart useful knowledge by stating it - the individual learning the knowledge has to do it themselves. They have to drill it, practice it, make mistakes, explore the problem space, and pattern-match on examples from those who have gone before.

Cedric, again:

> In other words, tacit knowledge instruction happens through things like imitation, emulation, and apprenticeship. You learn by copying what the master does, blindly, until you internalise the principles behind the actions.

So, I wanted to systematically start copying the masters, and I want to help others do the same. 

## Studying the finished product is only part of the solution

Over the years, I've tried different tacts, like [rebuilding portions of the Rake gem](https://josh.works/deliberate-practice-avdi-grimm-rake-gem), to practice writing ruby in the style of experts.

This approach didn't bear much fruit, as software is not written in such a linear fashion. I tried to rebuild a class from scratch, top-to-bottom, using tests as a guide. This approach doesn't model the actual iterative nature of software development.

Next, I thought I'd investigate pull requests, and practice building the equivalent code myself. This also came up short, as it didn't let me directly inspect the process that lead to that pull request.

Eventually, I concluded that one of the most effective ways of learning is to _observing expert practitioners doing their job_.

This observation-based learning comes with two additional challenges.

**Challenge One**

First, if the expert is navigating a codebase/application that they are deeply familiar with, and I have no familiarity with, I'll just be lost the whole time. 

How much of their effectiveness is related to knowledge of the codebase, vs. knowledge of generalized principles of software development?

I needed to observe an expert who had knowledge of the codebase equal to my own. Since I know nothing about most codebases in the world, that meant myself and the expert had to approach the same codebase with zero (or near-zero) prior knowledge.

**Challenge Two**

Second, assuming we both approach the codebase with zero prior knowledge, it won't be long before the expert does something that I don't understand. Even if I understand all the code they're writing, what if they investigated some portion of the codebase, _and I didn't understand why that portion of the codebase was of interest to them_?

I needed to inject _myself_ into the process, so when the expert does something I didn't understand, I could stop them and say
> Why did you do that?

## This video/companion blog post "format" is a good way to highlight tacit knowledge

These constraints have led directly to this project. 

I'm working on a few different types of resources, but most of the work I'll do here will be pairing with experts to observe them at work, in a way where I can ask them to explain why they did something when their decisions deviate from my understanding.

_And I will do all of this in a way that can be shared with others._


## Why other formats for transferring knowledge don't quite meet my needs

You would be well justified in expressing some skepticism here.

> Josh, there are entire shelves of books, written by absolute experts _who are good at teaching others_ about all of this. Courses, blog posts, conference talks, etc. Are you really telling me all of that isn't effective?

All of those resources are effective! I'm glad they exist, and I will continue to make use of them for my own learning.

Cedric Chin linked to [Why books don’t work](https://andymatuschak.org/books/), and I'd recommend you click through and give it a read. Books, lectures, and textbooks all have a role to play, but are substantially less effective at transferring knowledge than nearly everyone recognizes.

But all of these resources have the same problem. They are resources _about work_, but they are not resources of _doing the work_. 

Steven Shorrock wrote a piece called [The Varieties of Human Work](https://safetydifferently.com/the-varieties-of-human-work/), in which he outlines four varieties of human work:

- Work-as-imagined
- Work-as-prescribed
- Work-as-disclosed
- Work-as-done

![varieties of work](/images/matt-swanson-jekyll/varieties-of-work.jpg)

You'll notice that "work-as-done" is _very_ difficult to learn about as a non-practitioner, because you would rely upon someone _disclosing_ their work to you, to learn anything about it. 

By definition, every piece of knowledge that comes from a book, blog post, course, conference talk, or conversation is coming from the `work-as-disclosed` category. I don't mean to imply that the creator of that resource intends to mislead! Far from it! I simply mean that the work-as-disclosed necessarily deviates from work-as-done, and I want to directly inspect the `work-as-done` category.

Remember Cedric's earlier discussion of `tacit knowledge`?

> Tacit knowledge is knowledge that cannot be captured through words alone.

Which means _I cannot rely exclusively on stated knowledge from senior developers_. I simply must observe them working in order to observe their use of tacit knowledge. 

And that's why this series of videos exists.

To get started, jump over to part 1:

But before you go, why not subscribe to get updates when more guides in this series are done, as well as when future guides go up?

<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>

{% include jekyll-bug-fix-index.md %}