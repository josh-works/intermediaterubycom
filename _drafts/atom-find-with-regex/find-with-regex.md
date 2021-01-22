---
layout: post
title:  "Find with Regex in Atom"
description: "Basic Regular Expressions to make you a bit quicker in your editor"
date:  2020-10-19 06:00:00 -0700
crosspost_to_medium: false
categories: [category]
tags: [tag1, tag2]
permalink: find-with-regex
image: /images/title_image.jpg
---


### Use Atom's "find with Regex" feature to find specific strings (with an obstacle course!)



Lets say you have this blob of text:

```
- item 1
- item 2
- item 3
- item 4
- item 5
```

And you want to switch it to an ordered list. Easy enough to use multi-cursor "support".

It would look like this:

https://share.getcloudapp.com/qGuvJ5Z0

But what if you have two lists, like this?

```
1. item 1
1. item 2
1. item 3
1. item 4
1. item 5

then some other paragraph that separates these

1. item 1
1. item 2
1. item 3
1. item 4
1. item 5
```

Now, multi-cursor won't work, because it would try to "grab" lintes that you don't want. You can use a clever "find next", like so:

https://share.getcloudapp.com/kpuwnDvQ

Which works, unless your list looks like this:


```
- item 1: explanations and oh yeah - I forgot a note
- item 2: more explanations, and - this character ruins my "easy" find-and-replace
- item 3: because now I'm looking for the string `- ` which occures at the beggining of the line
- item 4: and at the middle of the line. 
- item 5

then some other paragraph that separates these

- item 1
- item 2
- item 3
- item 4
- item 5
```

So, a little Regular expression to the rescue. We're going to filter our searching to _just_ strings that match what we're looking for, _if they're at the beginning of the string_:

`⌘+f` opens up "find". Use `opt+cmd+/` to toggle regex search mode.

Use the `start of string` regex character, followed by what you're looking for:

```
^- 
```

(don't forget the space)

![regex screenshot](/_drafts/atom-find-with-regex/regex-find-and-replace.jpg)


