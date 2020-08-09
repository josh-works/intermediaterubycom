---
layout: jekyll-bug-fix-series
title: "Making an OSS Contribution, Part 2: Getting our first failing test"
published: true
description: ""
permalink: /matt-swanson-jekyll-bug-p2
image: ""
series_part: "Part 2"
---

_This is the third part of a short series on pairing with a super-experienced software developer to fix an open-source issue in Jekyll._

_In the last post, Matt explained how he identified [this particular issue](https://github.com/jekyll/jekyll/issues/7973) for us to work on._

_This series (and more series in the future) will constantly attempt to surface the [tacit knowledge](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/) that experienced developers use to do their work._


-----------------------

## How to read this particular post

Remember, the goal of this entire series is for you to do the exact same things an expert does. So, clone down the repository.

Now, this series will be useful for years to come, but the PR Matt and I made has been merged into the repository, so you'll have to check out the repo at the same state it was in when he and I started working on it.

Since you're not necessarily making your own PR, you don't have to fork it to your own repo, you can just clone it. Here's how to set it up:

```shell
$ git clone git@github.com:jekyll/jekyll.git

// now checkout the codebase where Matt and I were working:
$ git checkout 8403184b 
```

Open up the [Contribution Guidelines](https://jekyllrb.com/docs/contributing/) and work through the video with us! The Jekyll docs talk about the various scripts we used [here](https://jekyllrb.com/docs/contributing/#running-tests-locally)

## Video Walkthrough

<iframe width="560" height="315" class="youtube-video-embed" src="https://www.youtube.com/embed/sqMh7sM541M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Video Timestamps

- [0:00](https://youtu.be/sqMh7sM541M?t=0m00s) Talking about what setup Matt has done (almost none!)
- [0:40](https://youtu.be/sqMh7sM541M?t=0m40s) Jekyll contribution docs: https://jekyllrb.com/docs/contributing/
- [0:48](https://youtu.be/sqMh7sM541M?t=0m48s) Looking for `CONTRIBUTING.markdown` in project
- [1:15](https://youtu.be/sqMh7sM541M?t=1m15s) Running tests locally, running scripts (we start with `script/bootstrap`)
- [1:35](https://youtu.be/sqMh7sM541M?t=1m35s) exploring script directory, running recommended scripts
- [2:00](https://youtu.be/sqMh7sM541M?t=2m00s) how to execute scripts in the shell
- [2:45](https://youtu.be/sqMh7sM541M?t=2m45s) Looking at GH Issue for clue of what file to start with
- [3:05](https://youtu.be/sqMh7sM541M?t=3m05s) \#1 keyboard shortcut to know: `Fuzzy-finder/go-to-file`
- [3:30](https://youtu.be/sqMh7sM541M?t=3m30s) "run tests for current file" - I've never used this extension, but I've also never used .NET or Java.
- [4:40](https://youtu.be/sqMh7sM541M?t=4m40s) installing all the gems takes FOREVER
- [4:53](https://youtu.be/sqMh7sM541M?t=4m53s) Matt does some amazing keyboard work to do something specific, quickly.
- [5:32](https://youtu.be/sqMh7sM541M?t=5m32s) reading the method in question, starting to figure out what it does, what jumps out at Matt
- [6:36](https://youtu.be/sqMh7sM541M?t=6m36s) quick `select-find-jump` usage to jump around file
- [8:15](https://youtu.be/sqMh7sM541M?t=8m15s) the bootstrap script is finished, finally!
- [9:00](https://youtu.be/sqMh7sM541M?t=9m00s) still exploring relationship between `Utils#slugify` and `Utils#replace_character_sequence_with_hyphen`
- [10:00](https://youtu.be/sqMh7sM541M?t=10m00s) "we're getting warmer" with finding what to pay attention to, what to ignore
- [11:20](https://youtu.be/sqMh7sM541M?t=11m20s) explaining what I18n means, and a16z, not mentioned but commonly seen: a11y => "accessibility"
- [12:40](https://youtu.be/sqMh7sM541M?t=12m40s) Matt supposing that #slugify probably changes a lot. It's "a hotspot". 
- [13:40](https://youtu.be/sqMh7sM541M?t=13m40s) Matt searches for slugify, then .slugify. 
- [15:38](https://youtu.be/sqMh7sM541M?t=15m38s) Running ./script/cibuild, 2nd script recommended in contribution guidelines. (because the first script *finally* finished)
- [16:30](https://youtu.be/sqMh7sM541M?t=16m30s) Matt explains how he found the file to add the test too
- [18:29](https://youtu.be/sqMh7sM541M?t=18m29s) splitting tabs, test on one side, lib on the other. (SEE NOTES FOR FURTHER THOUGHTS ON SPLITTING PANES)
- [19:40](https://youtu.be/sqMh7sM541M?t=19m40s) Matt mentions that this repo is in his /junk folder  😂
- [20:10](https://youtu.be/sqMh7sM541M?t=20m10s) Checking out a new branch! 🙌
- [20:23](https://youtu.be/sqMh7sM541M?t=20m23s) Odd issue where git was picking up test artifacts. Must have been a temporary file. 
- [21:27](https://youtu.be/sqMh7sM541M?t=21m27s) Figuring out how to run an individual test file
- [21:57](https://youtu.be/sqMh7sM541M?t=21m57s) What test framework ARE we using? Looking at script/test
- [22:53](https://youtu.be/sqMh7sM541M?t=22m53s) Running just the test_utils.rb file.
- [23:40](https://youtu.be/sqMh7sM541M?t=23m40s) Talking about test output, how overwhelming this all is!
- [24:04](https://youtu.be/sqMh7sM541M?t=24m04s) What is the "options --seed" thing?
- [25:51](https://youtu.be/sqMh7sM541M?t=25m51s) Expounding on test coverage, timing, understanding the "time" output (real vs. user vs. system)
- [26:50](https://youtu.be/sqMh7sM541M?t=26m50s) "the only thing that is of minor use to use... is the test coverage percentage"
- [28:55](https://youtu.be/sqMh7sM541M?t=28m55s) Figuring out WHERE to put our new test.
- [30:16](https://youtu.be/sqMh7sM541M?t=30m16s) Narrowing down to the "#slugify" context block
- [31:10](https://youtu.be/sqMh7sM541M?t=31m10s) Starting to actually add lines of code. 👩‍💻
- [31:33](https://youtu.be/sqMh7sM541M?t=31m33s) copying from the test below to get our basic test
- [31:48](https://youtu.be/sqMh7sM541M?t=31m48s) copying expected/actual values from @deepestblue's issue (thanks again, @deepestblue, for such a good bug report)
- [32:44](https://youtu.be/sqMh7sM541M?t=32m44s) running the file again, this time expecting a failure. And getting it! 🎉🎊🎉🎊

## Expanding on things that came up in the video:


### Running scripts per the contribution guidelines

The Jekyll [Contribution Guidelines](https://jekyllrb.com/docs/contributing/) specifies running a certain script (`script/boostrap`) to kick off all the tests.

This means there's a directory of scripts (appropriately lableled `script`, which presumably has many scripts, but we care about only one of them. `boostrap`)

To execute a script, you have to prepend it with `./`. This will tell your operating system that you do indeed intend on running the given script. 

So, Matt runs the script with:

```
$ ./script/boostrap
```

and that runs under the hood something like:

```
bundle install
```

While it installs, Matt and I talk about a next iteration of this project that might involve work on `dev.to`. It's more of an application than a library (Jekyll is a library) so it might be a bit more relevant to the day-to-day of the normal software developer. 

Shipping a library for your day job is different than working on an application.

As I've mentioned, one of the goals of this project is to find instances where the expert uses Tacit Knowledge. I'll use this section to bring attention to as much of Matt's tacit knowledge as possible.

### Top keyboard shortcut for Atom/VS Code

Matt says "the top two shortcuts..."
1. fuzzy finder ([Atom](https://github.com/atom/fuzzy-finder/), [VS Code](https://github.com/gayanhewa/vscode-fuzzysearch))
2. run test file for current file (Josh needs to find this, requires a plugin)

For "run tests for current file" I usually want to look at the test file before running it, so my workflow is:

1. use fuzzy finder to open up the desired test file
2. Use keyboard shortcut to copy the _relative_ path of the test file to my clipboard. Atom: `shift+ctrl+c`
3. Run the test file in whatever method the project requires: `ruby <file>`, `bundle exec ruby -Itest <file>`, `./test <file>`, etc. 

### `copy-find-paste-enter` keyboard shortcuts

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

Note - When you're staying inside the editor, at least for Atom, I can double-click any text, and when I hit `⌘+f` Atom inserts the selected string in the search box. This saves me a copy/paste. 

### Jargon: I18N (internationalization)

`i18n`, `a16z`, `a11y` are all phrases you might have come accros in the industry. 

- `i18n`=> `internationalization` (there are 18 letters between the `i` and the `n`)
- `a16z`=> `AndreessenHorowitz` (there are 16 letters between the `a` and the `z`)
- `a11y`=> `accessibility` (there are 11 letters between the `a` and the `y`)


### Running another script (`cibuild`)

Runs rubocop, the unit tests. 

The Jekyll team has confidence in the build setup, so we run the tests to make sure we're starting in a clean state.

### Splitting panes horizontally vs. vertically

Add screenshots here, mention being able to see lots of test output at the same time

Matt says
> Usually I split my panes vertically...

Here's why. Look at the line counts:

![so much text](/images/matt-swanson-jekyll/recommended_screen_setup.jpg)

With the keyboard shortcut of `⌘+\`, you can toggle the visibility of the sidebar effortlessly.

![visible sidebar](/images/matt-swanson-jekyll/recommended_screen_setup_with_sidebar.jpg)

If instead we split the screens horizontally, here's what we'd get:

![horizontal split](/images/matt-swanson-jekyll/horizontal_screen_setup.jpg)

Matt splits the panes horizontally, since he's running his fonts unsually large so they come through better in the recording.

### How Matt decided which file to add the failing test to

Searching for `slugify` vs. `.slugify`

Ah, the file name convention is different from what I expected.

I expected `{class_under_test}_test.rb`, but it's actually `test_{class_under_test}.rb`

Try this yourself, in your editor of choice. Do you see the difference in results?


### Keybindings

Matt has keyboard shortcuts set up for his commonly used applications.

I noticed that I don't think he used alt-tab once. 

I've got keyboard shortcuts set up for `Atom`, `Firefox`, `iTerm`, and a few other tools. I hardly ever use `alt+tab` on my laptop, and it _feels_ like this saves time and effort. 

I'm all for copying what experts do, might be worth setting something similar up on your own machine.

I've written extensively about exactly how I have my "environment" set up [here](https://josh.works/developer-workflow)

### Writing the first test

At about an hour in, we've written three lines of code:

```ruby
# test/test_utils.rb:140
it 'should not break certain tamil characters' do
  assert_equal "மல்லிப்பூ-வகைகள்", Utils.slugify("மல்லிப்பூ வகைகள்")
end
```



## Checks for Understanding

1. When prepping to do open-source work, should you fork the repo before cloning it?
1. What script should we run that, according to the [Jekyll docs](https://jekyllrb.com/docs/contributing/), makes sure the project is set up and running correctly?
1. How do you run a script? What directory would we expect scripts to be in? 
1. _Why_ would you run a script?
1. What 2 things does `./script/bootstrap` do?
1. What's the keyboard shortcut for opening `go-to-file`/`fuzzy-finder` for your editor? 
1. What script would we use to make sure the repo is in good shape to work with? Hint: `CircleCI` runs against every new PR. What does this script do?
1. What script do you use to run tests?
1. How would you find every spot that `slugify` is mentioned? How about every time the method is called?
1. What does the `test_utils` script do?
1. What are the implications of Jekyll's test coverage? (It's 64%). 
1. How would we run tests for _just_ the `lib/jekyll/utils.rb` file?
1. When you add the first test, what should the `assert_equals` arguments be? (Hint: they come from the Jekyll issue report)

-----------------------
Next, jump over to part 3.

But before you go, why not subscribe to get updates when more guides in this series are done, as well as when future guides go up?

<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>

{% include jekyll-bug-fix-index.md %}