---
layout: jekyll-bug-fix-series
title: "Making an OSS Contribution, Part 3: Into The Weeds with RegEx"
published: true
description: ""
permalink: /matt-swanson-jekyll-bug-p3
image: ""
series_part: "Part 3"
---

## How to read this particular post

Make sure to read part 0, and watch part 1 and 2. It won't make much sense otherwise.

We've started with a failing test. I encourage you to follow the [setup instructions](https://intermediateruby.com/matt-swanson-jekyll-bug-p2#how-to-follow-along-with-us) from Part 2.

Make sure to add the same test we did, [which is visible here](https://intermediateruby.com/matt-swanson-jekyll-bug-p2#writing-the-first-test)

Now, lets make the test pass! Feel free to take a stab at it yourself, or watch along with us in the video. 

## Video Walkthrough

<iframe width="560" height="315" class="youtube-video-embed" src="https://www.youtube.com/embed/0ffyhDQB_XI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Video Timestamps

- [0:15](https://youtu.be/0ffyhDQB_XI?t=0m15s) Conventions for writing Context blocks, generating useful error messages
- [1:00](https://youtu.be/0ffyhDQB_XI?t=1m00s) our test failure matches the bug report. 💪
- [1:30](https://youtu.be/0ffyhDQB_XI?t=1m30s) running a single test from the test file. Trying line number first
- [1:45](https://youtu.be/0ffyhDQB_XI?t=1m45s) How to pass the name of the test through, in a regular expression: -n=/tamil/
- [3:00](https://youtu.be/0ffyhDQB_XI?t=3m00s) Applying the fix "as suggested", hoping it'll be easy. (sad trombone)
- [4:15](https://youtu.be/0ffyhDQB_XI?t=4m15s) Making the first change, running test, hoping for different output
- [4:40](https://youtu.be/0ffyhDQB_XI?t=4m40s) Figuring out if what we're thinking is getting called IS getting called
- [5:10](https://youtu.be/0ffyhDQB_XI?t=5m10s) Oops, wrong mode. Updating the Regular Expression. Easy fix. 
- [5:48](https://youtu.be/0ffyhDQB_XI?t=5m48s) Now applying the given Regex to SLUGIFY_DEFAULT_REGEX
- [6:24](https://youtu.be/0ffyhDQB_XI?t=6m24s) We made a change and got a change! Huzzah! 
- [6:50](https://youtu.be/0ffyhDQB_XI?t=6m50s) Oh boy. It didn't work. Lets debug. Lots of things to check. JUMP TO 33:45 TO SEE ANSWER IF YOU DON'T WANT TO WATCH US DEBUG THIS
- [8:28](https://youtu.be/0ffyhDQB_XI?t=8m28s) "Slimming down" the magnitude of our change, seeing if that helps.
- [8:55](https://youtu.be/0ffyhDQB_XI?t=8m55s) Adding non-special-characters to see if they show up in the test output. they don't. :( 
- [9:53](https://youtu.be/0ffyhDQB_XI?t=9m53s) Adding a breakpoint so we can shorten the feedback loop. Pry for the win! 
- [10:16](https://youtu.be/0ffyhDQB_XI?t=10m16s) Oops. Pry doesn't work. 
- [10:35](https://youtu.be/0ffyhDQB_XI?t=10m35s) Installing pry globally with -g flag. Still doesn't work. 
- [11:15](https://youtu.be/0ffyhDQB_XI?t=11m15s) Pry still not working. 
- [11:57](https://youtu.be/0ffyhDQB_XI?t=11m57s) Incomprehensible error messages. Story of my life.
- [12:20](https://youtu.be/0ffyhDQB_XI?t=12m20s) Looking up a Pry alternative, like IRB
- [12:35](https://youtu.be/0ffyhDQB_XI?t=12m35s) using 'debugger' statement
- [13:10](https://youtu.be/0ffyhDQB_XI?t=13m10s) Using require 'irb'; binding.irb. it works!🎉 
- [14:00](https://youtu.be/0ffyhDQB_XI?t=14m00s) Exploring "state" of what's available in this #replace_character_sequence_with_hyphen
- [15:00](https://youtu.be/0ffyhDQB_XI?t=15m00s) Playing with return values of `string.gsub(replaceable_char, "-")`
- [15:20](https://youtu.be/0ffyhDQB_XI?t=15m20s) Introducing Rubular, a great tool for working with Regular Expressions
- [16:05](https://youtu.be/0ffyhDQB_XI?t=16m05s) Building up the regular expression and test string in Rubular
- [18:20](https://youtu.be/0ffyhDQB_XI?t=18m20s) Trying the suggested Regular Expression in Rubular to see if it works
- [18:44](https://youtu.be/0ffyhDQB_XI?t=18m44s) it works! 
- [19:21](https://youtu.be/0ffyhDQB_XI?t=19m21s) Trying the working Regular Expression in IRB
- [20:35](https://youtu.be/0ffyhDQB_XI?t=20m35s) Still stumped. Even more stumped than before. This is not what we expected.
- [22:45](https://youtu.be/0ffyhDQB_XI?t=22m45s) Still stumped. We're wondering what we're missing. Cannot find it. 
- [24:32](https://youtu.be/0ffyhDQB_XI?t=24m32s) Comparing strings. 💡
- [24:40](https://youtu.be/0ffyhDQB_XI?t=24m40s) Pasting the regular expression straight into IRB
- [25:30](https://youtu.be/0ffyhDQB_XI?t=25m30s) Looking at the construction of the regular expression
- [26:33](https://youtu.be/0ffyhDQB_XI?t=26m33s) Trying to look in the docs for a hint of why Regexp.new(regex) might behave differently from /regex/
- [27:13](https://youtu.be/0ffyhDQB_XI?t=27m13s) Regular Expression Character Properties. Check the notes for more details.
- [28:44](https://youtu.be/0ffyhDQB_XI?t=28m44s) barking up the wrong tree. 
- [29:00](https://youtu.be/0ffyhDQB_XI?t=29m00s) Finding better words to google thanks to a JavaScript question
- [29:30](https://youtu.be/0ffyhDQB_XI?t=29m30s) advanced GoogleFu: how to exclude certain answers
- [30:20](https://youtu.be/0ffyhDQB_XI?t=30m20s) Noticing the escape characters. Getting warmer...\
- [32:20](https://youtu.be/0ffyhDQB_XI?t=32m20s) "OR-ed together." What strange words. 
- [33:50](https://youtu.be/0ffyhDQB_XI?t=33m50s) Matt sees the problem! We have to double-escape certain characters. 🤦🏻‍♂️ So simple.
- [34:40](https://youtu.be/0ffyhDQB_XI?t=34m40s) Seeing the correct regular expression, with `\p{}` visible
- [35:00](https://youtu.be/0ffyhDQB_XI?t=35m00s) The test passes. 🙃. What a 🐇 hole!
- [35:45](https://youtu.be/0ffyhDQB_XI?t=35m45s) Meta-principle: If evaluated Regular Expression isn't doing what you expect, make sure the regex being run is the same as what you think you're giving it. 
- [36:38](https://youtu.be/0ffyhDQB_XI?t=36m38s) Running all the tests. Still pass. 🏁 🎉🎊🎉🎊🎉🎊🎉🎊



## Expanding on what came up in the walk-through

### Test Naming Conventions

The `context/should` blocks in this project give nice error output, like:

> The `Utils.slugify` method should break right now for this issue.

How nice!



### Running a single test from a file

If you've got 30 tests in a file, and many of them test the same method, you'd want to run just a single test in the file for two reasons:
1. This will save you time (no running unnecessary tests)
2. If you use pry or a breakpoint down the road, you can hit the breakpoint with the context of _just_ the single test you're working for.

In this case, we'd want to hit the breakpoint with `மல்லிப்பூ வகைகள` as our input, not any of the other values in `test/test_utils.rb`

How to run a specific test and exclude all others?

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

### Adding a Breakpoint (Pry) 

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

### Breaking the Regex into smaller pieces

These are sorta crazy regular expressions to try to read:
+There's a lot to say about Regular Expressions, but in this case, we don't have to worry _too_ much about the exact details of the Regex we were working with.

```ruby
/[^\p{M}\p{L}\p{Nd}._~!$&'()+,;=@]+/
/[^[:alnum:]._~!$&'()+,;=@]+/
/[^\\p{M}\\p{L}\\p{Nd}._~!$&'()+,;=@]+/
```

The characters in common are:

```
._~!$&'()+,;=@
```

If you put `[._~!$&'()+,;=@]` into Rubular, and give it the following test strings, you'll see what it does:

```
this-matches_any;chars
_one!might~not%want.
=@in'a$url
_~!$&'()+,=@+
```

The `+` means `one or more of`, so these big regular expressions are trying to a variety of character properties, with the potential matches enclosed inside the outter brackets.

Here's how I "read" the regex:

```
[anything_in_here_including._~!$&'()+,;=@]+
```


### Regular Expressions (character properties)

There's a lot to say about Regular Expressions, but in this case, we don't have to worry _too_ much about the exact details of the Regex we were working with.

We got wrapped up in Regex `Character Properties`. Take a look at [Regex Character Properties(ruby-doc.org)](https://ruby-doc.org/core-2.5.1/Regexp.html#class-Regexp-label-Character+Properties)

All the examples that they give look like the regular expression we got from `@deepestblue`'s Github issue: `/[^\p{M}\p{L}\p{Nd}._~!$&'()+,;=@]+/`

We can "parse" thise Regex a bit. I'd never seen the `\p{}` thing before. From [the docs](https://ruby-doc.org/core-2.5.1/Regexp.html#class-Regexp-label-Character+Properties):
  
> The `\p{}` construct matches characters with the named property, much like POSIX bracket classes.

In the above Regex, we've got:

- `\p{M}`
- `\p{L}`
- `\p{Nd}`

Which translates to:

```
\p{M}  => 'Mark'
\p{L}  => 'Letter'
\p{Nd} => 'Number: Decimal Digit'
```

These were the changes that DeepestBlue suggested. He suggested we change it _from_:

`[^[:alnum:]._~!$&'()+,;=@]`

According to the docs, `[:alnum]` is a POSIX _bracket expression_, which is similar to [character classes](https://ruby-doc.org/core-2.5.1/Regexp.html#class-Regexp-label-Character+Classes)

If you're like me, reading the above definition, you thought:

> What does POSIX mean?

[Wikipedia says](https://en.wikipedia.org/wiki/POSIX)

> The Portable Operating System Interface (POSIX) is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.

None of this was what caused Matt and I to spend so much time working on this fix - we had a problem with character escaping. 

Compare:

```ruby
Regex.new(/[^\p{M}\p{L}\p{Nd}._~!$&'()+,;=@]+/)
Regex.new(/[^\\p{M}\\p{L}\\p{Nd}._~!$&'()+,;=@]+/)
```

As I was writing these notes, long after the video recording, I thought to myself:

> Do the docs even mention the need for escape characters? We didn't see any in use in the docs.

The answer is yes, the docs mention this:

[Metacharacters and Escapes](https://ruby-doc.org/core-2.5.1/Regexp.html#class-Regexp-label-Metacharacters+and+Escapes)

> The following are metacharacters `(`, `)`, `[`, `]`, `{`, `}`, `.`, `?`, `+`, `*`. They have a specific meaning when appearing in a pattern. To match them literally they must be backslash-escaped. To match a backslash literally, backslash-escape it: `\\`.

The included example doesn't really seem that helpful, either:

```ruby
/1 \+ 2 = 3\?/.match('Does 1 + 2 = 3?') #=> #<MatchData "1 + 2 = 3?">
/a\\\\b/.match('a\\\\b')                #=> #<MatchData "a\\b">
```

Anytime in the future that I am dealing with Regular Expressions, I'll think about escape characters. 

Hopefully now you will too!




## Checks for Understanding

- What are two reasons you might want to run just a _specific_ test from a file?
- Googling: How do you run a query and exclude results containing a certain word? (for example, googling on Regular Expressions, and you don't want any answers that reference `javascript`)
- If you see `\p{something}` in a regular expression, what does it mean? (Check the docs, no need to know this off the top of your head)
- If I want my regular expression to be `/\p{L}/`, what should it _really_ be? 
- What's an `alnum`?
- How many characters in a string will this regular expression capture? `/[abc]/`
- How many characters in a string will this regular expression capture? `/[abc]+/`
- Will `/[^abc]+/` match `a`? 
- What online tool is helpful for using Regular Expressions with Ruby?
- How do you run a specific test using the `--name` flag?
- If `pry` doesn't work in a Ruby project, what is a good alternative to try?

----------------------------

Next, jump over to part 4:

But before you go, why not subscribe to get updates when more guides in this series are done, as well as when future guides go up?

<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>

{% include jekyll-bug-fix-index.md %}

