---
layout: post
title: "Commit Tracing In Pry"
published: false
description: "Applying Chelsea Troy's Leveling Up Skill of Commit Tracing"
permalink: /commit-tracing-in-pry
image: ""
series_part: ""
---

I'm working through [Leveling Up Skill #6: Commit Tracing](https://chelseatroy.com/2018/07/21/leveling-up-skill-6-commit-tracing/), as applied to the `pry` gem.

## The Backstory

[Iuliu Pop](https://www.iulspop.dev/) and I are working to maximize learning, targeting "top 10% software developer", perhaps scoped down to things like a specific programming language, business domain, etc. 

For now, top 10% software developer.

The question we both think about are "what are the specific and tactical tools one can apply to improving one's skills?"


### What And Why To Trace Commits

Read Chelsea Troy's post: [Leveling Up Skill #6: Commit Tracing](https://chelseatroy.com/2018/07/21/leveling-up-skill-6-commit-tracing/).

### Why To examine the Pry Gem

Pry is a ubiquitous tool in the Ruby/Rails community, seemed like a good place to start.

## The Technique

Open the gem in your editor:

```
$ EDITOR=atom bundle open griddler
Could not find gem 'pry'
```

Hm. I check to see that the gem is installed locally:

```
$ gem list pry

*** LOCAL GEMS ***

pry (0.14.0, 0.13.1)
pry-byebug (3.9.0)
```

Ah, of course, we're calling "bundle open", so it wants to look at our `Gemfile` or `Gemfile.lock`

So, I'm `cd`ing into a directory that has a `Gemfile` and `Gemfile.lock` containing `pry`. 

If you'd like to follow along, I'm using my [intermediate ruby obstacle course](https://github.com/josh-works/intermediate_ruby_obstacle_course), and you can follow along with:

```
git clone git@github.com:josh-works/intermediate_ruby_obstacle_course.git
cd intermediate_ruby_obstacle_course
bundle install
EDITOR=atom bundle open pry
```
Here's what it looked like for me:

![opening pry](/images/commit-tracing-pry.jpg)

You'll see pry open in the specified editor

Success! [^til]

[^til]: Here's my [today-i-learned](https://github.com/josh-works/til/blob/main/ruby/open-specific-gem-in-editor-with-bundler.md) for the above topic. 

...

Arg. Not success, duh. As soon as I spent 3 seconds thinking about it, I realized that of course the code included in the Gemfiles doesn't include version control info. We'll need to change tacts, clone down the actual pry gem (_with_ the `.git` folder included) and try again.

## The Technique (Take 2)

### 1. Create a place for the Pry source code

Make a new directory, clone down the [pry gem](https://github.com/pry/pry)

```
$ mkdir /me/warmup/commit-tracing/
$ cd commit-tracing
$ git clone git@github.com:pry/pry.git
$ cd pry
```

Now we can work through this together!

### 2. Find a promising commit

Chelsea Troy says she looks for:

> A fairly complex code base that exemplifies my topic of study and has clearly named, well-circumscribed commits.

So, I'm going to start [browsing Pry commits](https://github.com/pry/pry/commits/master)

I'm skimming through a handful, I'm going to find 5 "promising" commits before moving to step 3. (I expect that my first few attempts at commit tracing will not be precisely the right size/complexity, so I'm not getting held up on this step)

Here's some interesting commits that I might use for the next step:

- [config: return `nil` on unknown option instead of raising ](https://github.com/pry/pry/commit/5dd061c3406aa84e5cafd489a5c77e550b00d122)
- [pry-backtrace frozen bug ](https://github.com/pry/pry/commit/da81c960272ae0a265f7ded21697d1f09f151ffb)
- [Display all syntax error messages when catching SyntaxException](https://github.com/pry/pry/commit/f6736d526260b2aa9f50b61150a67fcfa2045893)
- [Add Pry::Env](https://github.com/pry/pry/commit/7ce5ca70bb4a1ff447269bdde4cb5d07b8932c8a)
- [Add Pry::Warning](https://github.com/pry/pry/commit/473bc9f2d6a0ebd93c9a09ea3c699c14e01330b0)
- [Push edit contents to history](https://github.com/pry/pry/commit/782a09e057d1e714074d61891a5fba293eb9faca)






### Notes, further reading

- [](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/)
- [How To Open A Specific Gem In A Specific Editor (github.com/josh-works/til)](https://github.com/josh-works/til/blob/main/ruby/open-specific-gem-in-editor-with-bundler.md)
