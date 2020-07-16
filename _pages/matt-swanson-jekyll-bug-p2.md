---
layout: page
title: "Making an OSS Contribution, Part 2: Getting our first failing test"
published: true
description: ""
permalink: /matt-swanson-jekyll-bug-p2
image: ""
---

_This is the second part of a short series on pairing with a super-experienced software developer to fix an open-source issue in Jekyll._

_In Part 1, Matt explained how he identified [this particular issue](https://github.com/jekyll/jekyll/issues/7973) for us to work on._

_This series (and more series in the future) will constantly attempt to surface the [tacit knowledge](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/) that experienced developers use to do their work._

### Series Index

- [Part 1: How Matt found this perfectly-suited issue to fix]({{ site.baseurl }}{% link _pages/matt-swanson-jekyll-bug-p1.md %}) 
- [Part 2: Setting up the app, basic investigation, and writing a failing test]({{ site.baseurl }}{% link _pages/matt-swanson-jekyll-bug-p2.md %}) _you are here_
- `Part 3: Making that failing test pass! 🙌` (coming soon)
- `Part 4: Making the Pull Request` (coming soon)

-----------------------

Want to get updates on these posts as they come out?

<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>

## Timestamps

- 0:38, Setup to start working on the jekyll repository
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

#### Jargon: I18N (internationalization)

`i18n`, `a16z`, `a11y` are all phrases you might have come accros in the industry. 

`i18n`=> `internationalization` (there are 18 letters between the `i` and the `n`)
`a16z`=> `AndreessenHorowitz` (there are 16 letters between the `a` and the `z`)
`a11y`=> `accessibility` (there are 11 letters between the `a` and the `y`)

### How Matt looks at and uses tests

- it'll be easy to get a failing test.

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

Matt splits the panes horizontally, since he's running his fonts unsually large, just so they come through better in the recording.

### Keybindings

Matt has keyboard shortcuts set up for his commonly used applications.

I noticed that I don't think he used alt-tab once. 

I've got keyboard shortcuts set up for `Atom`, `Firefox`, `iTerm`, and a few other tools. I hardly ever use `alt+tab` on my laptop, and it _feels_ like this saves time and effort. 

I'm all for copying what experts do, might be worth setting something similar up on your own machine.

<link to my "tooling" document>

### Writing the first test

At about an hour in, we've written three lines of code:

```ruby
it 'should do something' do
  assert_equal "", Utils.slugify("")
end
```

If we were both earning about $100k/yr for salaried work, our company would have paid out ~$100/person-hour for our time pairing on this.

If you're doing the math at home, we've spent $200 person-hours to achieve this single line. 

It's not about _time_, when you work. It's about value. 

And it's not about writing lots of code, or doing it quickly, it's about having good process.

### Running a single test from a file

If you've got 30 tests in a file, and many of them test the same method, you'd want to run just a single test in the file. 

In Rspec, you can call `rspec path/to/test/file:line_number`, with `line_number` representing the line of code your test is on.

We don't have that option here, but we do have the `--name` flag, where we can specify the _name_ of the test we want to run.

If our test name as the word `tamil` in it, we can say `test/test_utils.rb -n /tamil/`, and any test with the matching word in it gets run.

[according to the docs](https://github.com/seattlerb/minitest#label-Running+Your+Tests) you can pass both a regular expression _or_ a string:

```
% ruby -Ilib:test test/minitest/test_minitest_test.rb --help
minitest options:
    -h, --help                       Display this help.
    -s, --seed SEED                  Sets random seed. Also via env. Eg: SEED=n rake
    -v, --verbose                    Verbose. Show progress processing files.
    -n, --name PATTERN               Filter run on /regexp/ or string.
    -e, --exclude PATTERN            Exclude /regexp/ or string from run.
```

Now you know!


### Adding Pry where it's not otherwise required

We had success (and the answer!) from StackOVerflow:

[How do I drop to the IRB prompt from a running script? (StackOverflow)](https://stackoverflow.com/questions/1144560/how-do-i-drop-to-the-irb-prompt-from-a-running-script)


Ended up using:

```ruby
require 'irb'
binding.irb
```

Now we can inspect the state of the program a bit:

```ruby
> script/test test/test_utils.rb -n=/tamil/
+ ruby -S bundle exec ruby -I test test/test_utils.rb -n=/tamil/
# -------------------------------------------------------------
# SPECS AND TESTS ARE RUNNING WITH WARNINGS OFF.
# SEE: https://github.com/Shopify/liquid/issues/730
# SEE: https://github.com/jekyll/jekyll/issues/4719
# -------------------------------------------------------------

# Running tests with run options -n=/tamil/ --seed 59662:

cannot load such file -- awesome_print

From: /Users/joshthompson/crap/jekyll/lib/jekyll/utils.rb @ line 364 :

    359:         else
    360:           SLUGIFY_DEFAULT_REGEXP
    361:         end
    362:
    363:       # Strip according to the mode
 => 364:       require 'irb'; binding.irb
    365:       string.gsub(replaceable_char, "-")
    366:     end
    367:   end
    368: end

>> replaceable_char
=> /[^\p{M}\p{L}\p{Nd}]+/
>> string
=> "மல்லிப்பூ வகைகள்"
>> string.gsub(replaceable_char, '-')
=> "மல்லிப்பூ-வகைகள்"
>> mode
=> "default"
```

### Breaking the REGEX into components

These are sorta crazy regular expressions to try to read:

```ruby
/[^\p{M}\p{L}\p{Nd}._~!$&'()+,;=@]+/
/[^[:alnum:]._~!$&'()+,;=@]+/
/[^\\p{M}\\p{L}\\p{Nd}._~!$&'()+,;=@]+/
```

Right? What the heck is going on here.

Fortunately, a large portion of these can be quickly ignored and simplifed. 

Compare these pairs:

```ruby
/[^\p{M}\p{L}\p{Nd}._~!$&'()+,;=@]+/   # option 1, original
/[^\p{M}\p{L}\p{Nd}]+/                 # option 1, simplifed

/[^[:alnum:]._~!$&'()+,;=@]+/   # option 2, original
/[^[:alnum:]]+/                 # option 2, simplifed

/[^\\p{M}\\p{L}\\p{Nd}._~!$&'()+,;=@]+/   # option 3, original
/[^\\p{M}\\p{L}\\p{Nd}]+/                 # option 3, simplifed

```

Obviously the "simplifed" ones are... simpler. So, why evaluate these regular expressions as if they are the "simple" versions and not the original ones?

That string that we've eliminated, `._~!$&'()+,;=@`, is a pretty common list of characters that represent all the "special" characters that exist on many keyboards. When "sanitizing" text input, trying to clean out everything but letters and spaces, these characters are a good starting point.

So, Matt isn't worrying about this part of the regular expression as it's not related to the bug we're trying to fix. 

<!-- add link to p1 here -->
<!-- add link to p3 here -->

-----------------------

Want to get updates on these posts as they come out?

<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>


 