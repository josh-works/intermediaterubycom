---
layout: jekyll-bug-fix-series
title: "Making an OSS Contribution, Part 3: ..."
published: false
description: ""
permalink: /matt-swanson-jekyll-bug-p3
image: ""
series_part: "Part 3"
---



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