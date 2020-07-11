---
layout: page
title: "Pairing with Matt Swanson on Jekyll, part 2"
published: false
description: ""
permalink: /matt-swanson-jekyll-bug-p2.md
image: ""
---

_This is the second part of a short series on pairing with a super-experienced software developer to fix an open-source issue in Jekyll._

_In Part 1, Matt explained how he identified [this particular issue](https://github.com/jekyll/jekyll/issues/7973) for us to work on._

_This series (and more series in the future) will constantly attempt to surface the [tacit knowledge](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/) that experienced developers use to do their work._

<add partial for series here>

## Context

- 0:38, Setup to start working on the repository
- forked and cloned the repo

## Setting up the project locally

Step 1: Matt forked the repo to his own account 
Step 2: Click the link in the repo description to www.jekylirb.com
Step 3: Clicked the link for the "contributin guidelines" (add link)
Quickly skimmed it, made note of what we might want to return to later.

## Running tests per the docs

The Jekyll project specifies running a certain script (`script/boostrap`) to kick off all the tests.

This means there's a directory of scripts (appropriately lableled `script`, which presumably has many scripts, but we care about only one of them. `boostrap`)

To execute a script, you have to prepend it with `./`. This will tell your operating system that you do indeed intend on running the given script. 

So, Matt runs the script with:

```
$ ./script/boostrap
```

and that runs under the hood something like:

```
bundle install
bundle exec rspec
```

while it installs, Matt and I talk about a next iteration of this project that might involve work on `dev.to`. It's more of an application than a library (Jekyll is a library) so it might be a bit more relevant to the day-to-day of the normal software developer. 

Shipping a library for your day job is different than working on an application.


Matt says "the top two shortcuts..."

### Tacit knowledge

- fuzzy finder (expand)
- run test file for current file (Josh needs to find this, requires a plugin)

#### copy-find-paste-enter keyboard shortcuts

keyboard shortcuts! Matt uses this one all the time, and if you're not using this keyboard shortcut, might be time to start.

This file we're looking at is 350+ lines long. Scrolling up and down is a waste of time. 

Here's what he does:
1. Double-click the method name or constant he wants to jump to.
2. hit `⌘+c` to copy it to his clipboard
3. hit `⌘+f` to open the `find in current file` tool. 
4. Hit `⌘+v` to paste the clipboard contents into the search box
5. hit `return` on his keyboard to jump to the top result. Hitting enter repeatedly cycles through all the instances of the string in the file. 

This isn't just _fast_, but allows him to not waste thought trying to find bits of code, or scroll around. He doesn't care _where_ in the file a constant or method is defined, just wants to look at it.

Please add this general process to your own workflow, if it's not already there.

#### Jargon: I18N (internationalization)

`i18n`, `a16z`, `a11y` are all phrases you might have come accros in the industry. 

`i18n`=> internationalization (there are 18 letters between the `i` and the `n`)
`a16z`=> andreesenhorowitz (there are 16 letters between the `a` and the `z`)
`a11y`=> accessibility (there are 11 letters between the `a` and the `y`)


