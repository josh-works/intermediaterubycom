---
layout: jekyll-bug-fix-series
title: "Making an OSS Contribution, Part 2: Getting our first failing test"
published: true
description: ""
permalink: /matt-swanson-jekyll-bug-p2
image: ""
---

_This is the third part of a short series on pairing with a super-experienced software developer to fix an open-source issue in Jekyll._

_In the last post, Matt explained how he identified [this particular issue](https://github.com/jekyll/jekyll/issues/7973) for us to work on._

_This series (and more series in the future) will constantly attempt to surface the [tacit knowledge](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/) that experienced developers use to do their work._


-----------------------



## Timestamps

- 0:38, Setup to start working on the jekyll repository
- forked and cloned the repo

## Follow along with us

Remember, the goal of this entire series is for you to do the exact same things an expert does. So, clone down the repository.

Now, this series will be useful for years to come, but the PR Matt and I made has been merged into the repository, so you'll have to check out the repo at the same state it was in when he and I started working on it.

Since you're not necessarily making your own PR, you don't have to fork it to your own repo, you can just clone it. Here's how to set it up:

```shell
$ git clone git@github.com:jekyll/jekyll.git

// now checkout the codebase where Matt and I were working:
$ git checkout 8403184b 
```

Open up the [Contribution Guidelines](https://jekyllrb.com/docs/contributing/) and work through the video with us! The Jekyll docs talk about the various scripts we used [here](https://jekyllrb.com/docs/contributing/#running-tests-locally)


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
```

While it installs, Matt and I talk about a next iteration of this project that might involve work on `dev.to`. It's more of an application than a library (Jekyll is a library) so it might be a bit more relevant to the day-to-day of the normal software developer. 

Shipping a library for your day job is different than working on an application.


Matt says "the top two shortcuts..."

### Tacit knowledge

- fuzzy finder ([Atom](https://github.com/atom/fuzzy-finder/), [VS Code](https://github.com/gayanhewa/vscode-fuzzysearch))
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

Note - When you're staying inside the editor, at least for Atom, I can double-click any text, and when I hit `⌘+f` Atom inserts the selected string in the search box. This saves me a copy/paste. 

#### Jargon: I18N (internationalization)

`i18n`, `a16z`, `a11y` are all phrases you might have come accros in the industry. 

`i18n`=> `internationalization` (there are 18 letters between the `i` and the `n`)
`a16z`=> `AndreessenHorowitz` (there are 16 letters between the `a` and the `z`)
`a11y`=> `accessibility` (there are 11 letters between the `a` and the `y`)


### Running another script (`cibuild`)

Runs rubocop, the unit tests. 

The Jekyll team has confidence in the build setup, so we run the tests to make sure we're starting in a clean state.

### How Matt decided which file to add the failing test to

Searching for `slugify` vs. `.slugify`

Ah, the file name convention is different from what I expected.

I expected `{class_under_test}_test.rb`, but it's actually `test_{class_under_test}.rb`

Try this yourself, in your editor of choice. Do you see the difference in results?

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

Matt splits the panes horizontally, since he's running his fonts unsually learge, just so they come through better in the recording.

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
1. What script should we run that, according to the jekyll docs, makes sure the product is set up and running correctly?
1. How do you run a script? What directory would we expect scripts to be in? 
1. Why would you run a script?
1. What 2 things does `./script/bootstrap` do?
1. What's the keyboard shortcut for opening `go-to-file`/`fuzzy-finder` for your editor? 
1. What script would we use to make sure the repo is in good shape to work with? Hint - `CircleCI` runs against every new PR. What does this script do?
1. What script do you use to run tests?
1. How would you find every spot that `slugify` is mentioned? How about every time the method is used?
1. What does the `test_utils` script do?
1. What are the implications of Jekyll's test coverage? (It's 64%). 
1. How would we run tests for _just_ the `lib/jekyll/utils.rb` file?
1. When you add the first test, what should the `assert_equals` arguments be? (Hint: they come from the Jekyll issue report)


-----------------------

{% include jekyll-bug-fix-index.md %}

