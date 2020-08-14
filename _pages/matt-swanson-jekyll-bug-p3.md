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


## Video Walkthrough

<iframe width="560" height="315" class="youtube-video-embed" src="https://www.youtube.com/embed/0ffyhDQB_XI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Video Timestamps

_coming soon_


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

### Regular Expressions

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
- If you see `p{}` in a regular expression, what does it mean? (Check the docs, no need to know this off the top of your head)
- If I want my regular expression to be `/\p{L}/`, what should it _really_ be? 
- What online tool is helpful for using Regular Expressions with Ruby?
- How do you run a specific test using the `--name` flag?

----------------------------

Next, jump over to part 4:

But before you go, why not subscribe to get updates when more guides in this series are done, as well as when future guides go up?

<script async data-uid="518bab5f60" src="https://josh-thompson.ck.page/518bab5f60/index.js"></script>

{% include jekyll-bug-fix-index.md %}

