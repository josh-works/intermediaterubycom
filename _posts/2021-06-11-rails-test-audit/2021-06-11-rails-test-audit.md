---
layout: post
title:  "Lessons Learned from Three Rails Test Audits: How To Audit and Improve the Performance of Your RoR test Suite"
description: "I got paid by three different companies (startup, startup, and established org) to audit several different Rails test suites. Here's what I've learned"
date:  2021-06-22 06:00:00 -0700
crosspost_to_medium: false
categories: [programming]
tags: [consulting, performance_optimization, ruby, rails]
permalink: how-to-audit-and-improve-your-ruby-rails-test-suite
image: /images/title_image.jpg
github_issue_id: 8
---

_Author's note: This is a very work-in-progress guide, more of a scratchpad than finished page/guide/product/"thing". Please keep that in mind as you read! Stick questions in comments below, or add a comment to this twitter thread: [](https://twitter.com/josh-works/)_

A few weeks ago, I tweeted this thread:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">How long do your tests take to run?<br><br>Some tests suites take 5 minutes. Others take 45 minutes. <br><br>I&#39;ve done work around speeding up tests, and want to test my skills against real-world applications. <br><br>Will you pay me at least $100 to audit your <a href="https://twitter.com/hashtag/RoR?src=hash&amp;ref_src=twsrc%5Etfw">#RoR</a> test suite? <br><br>🧵👇</p>&mdash; Josh Thompson (@josh_works) <a href="https://twitter.com/josh_works/status/1392951464574787600?ref_src=twsrc%5Etfw">May 13, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

I offered to do this for $100. 🤦‍♀️, quickly upgraded it to $1000 after a few tweets suggested $1000 was the minimum possible amount for this service:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Strongly recommend you charge at least $1,000 to signal you&#39;re serious and know what you&#39;re doing. <br><br>&quot;I gave access to our source code to an extremely cheap contractor&quot; is not something most folks want to say to their boss.</p>&mdash; Ben Orenstein (@r00k) <a href="https://twitter.com/r00k/status/1393124330461143042?ref_src=twsrc%5Etfw">May 14, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Since then, I've had three customers! It's been an absolute blast, and I've learned a ton. (For example, getting an entire app running locally, from `git clone` to `rails test` and having all passing tests _never_ takes just a few minutes). I'll charge substantially more next time around. 

This document will be a living guide for how I accomplished the audit (and how I'll conduct future audits) and what steps I've taken to do two things:

1. Profile the test suite (and what this actually means/why it's important, if it seems odd to spend time on this topic.)
2. Reduce the test run time (or related times, like file load time, CircleCI "time", etc)

For one customer, I took a 5 min test suite to 1:10, a 75% reduction in speed, thanks to VCR. I'll show you exactly how I did this.

For another customer, I got a ~20min test suite to ~11min, but it failed when getting pushed to CircleCI, and then the underlying issue (some _really_ slow DB queries) got partially fixed, so I'm auditing the app a second time, expecting to find a different set of issues.

For the third customer, the app is huge, complicated, and the tests take so long they don't run the whole suite on a regular laptop - it's delegated to CircleCI, and test runs eat up a lot of credits and time. 

I'm going to offer all of my lessons learned as this finished guide soon. Preorder the guide for $49, or an upgrade package that will come with at least a 1-hour call, where we talk about your questions, we can screenshare through your codebase, etc. Any purchaser gets added to my slack group, and you can ping me with questions at any time.

I'm offering this on pre-order, because I've not finished the guide yet! Once the guide is done )especially when I do this again and get a bit more experienced/sophisticated), I'll raise the rates quite a bit. I don't know when that'll be - could be months from now. 

👉 [Preorder: (A) Partially-Complete Guide to Making Your Rails Tests Run Faster for $49](https://buy.stripe.com/fZeaF38kb3RZ73GeUU)

👉 [Preorder: The guide + a one-hour zoom call for $249](https://buy.stripe.com/8wMaF39of2NVfAcdQR)

Early adapters will obviously work more closely with me, and vice versa - as I/my written instructions create additional value, I'll raise my rates.

If you'd like a student discount, email me! I'll hook you up!

# The Guide

I'm keeping _some_ running notes in this document. I'll eventually expand it into a coherent, elegant document, titled `The Complete Guide to Making Your Rails Tests Run Faster`, but like anything I make, it goes through many rounds of iteration and testing, and I need a "dump my thoughts" spot somewhere close to hand and easily accessible. 

Before I go farther, please know that I, _of course_ stand on shoulders of giants.

I'm fortunate to have crossed paths with Nate Berkapec's [The Complete Guide to Rails Performance](https://www.railsspeed.com/) and Jason's [The Complete Guide to Rails Testing](https://www.codewithjason.com/complete-guide-to-rails-testing/). 

Both of those guides are extensive, and incredible collections of learning and knowledge. In ways I'm trying to apply lessons from both of them to this problem, and nearly any thought I have in this domain _that is correct_ comes directly from Nate or Jason. (If you've not bought their books/courses for yourself _or especially your development team_ I'd encourage you to do so! You and your team will be thrilled!)

## Benchmarking & Profiling

Step 1 is always "benchmark and profile". 

Ideally, I use a command like:

```
$ time bundle exec rails test --profile 40 
$ time bundle exec rspec --profile 40
```

The `time` command is easy - look it up on your machine, or use [TLDR](https://github.com/josh-works/til/blob/main/cli/tldr-what-is-it-install-it.md). It `times` whatever comes next. 

`bundle exec` (I have aliased to `b` ) runs the exact gems/versions specified in the `Gemfile.lock`

`rails test`/`rspec` run the test suite

`--profile 40` `rspec` has this `profile` functionality already included. It prints out diagnostic information about the slowest `n` tests, defaults to 10, I usually look at the slowest 40. There's a minitest gem for enabling profiling in minitest. 

## Get the app running locally

Oh man, this was a doozy. I ran into many issues. Many were tiny, required just a few Google queries to get through. Others were heftier.

We're used to something like:

```
$ git clone <company_app>
$ cd <company_app>
$ bundle install
$ bin/rails rspec
```

It's often quite a bit more. I actually wanna build a service that times how long from `git clone` to tests being done running _and passing_, or the app running locally and DB properly seeded, or both. 

For example:

- xcode-select commandline tools. Reinstalling fixes many things that get inexplicably broken.
- Elasticsearch can be a PITA to get running w/Homebrew
- MySQL can be a doozy to get various flavors of databases connected to the app. 
- services are not trivial. (mongdb, mysql/mysqld, elasticsearch, running them in a container, or locally, or via homebrew, or all of the above, credentials/ports so all services can connect appropriately.)

There are lots of services that developers can install on their machines.

More on this to come someday.

## After you've run some profiling/benchmarks

I'm free-associating through this. Each time I've done this, my "eye" is drawn in different directions to explore, so I'm hesitant to suggest hard-and-fast rules.

1. Tons of deprecation warnings, and a slow file load time? Maybe look into that.
1. Clean/easy test run, fast file load time? Look for common threads among the slowest tests.


Here's the specific items I'm auditing:

1. Best-case test run time
2. File load time
3. No-wifi run time/results
4. Flaky test count (if any)

Lets say you're investigating a slow file load time, especially if it's a low file load time for _every_ test:

```
Finished in 1.77 seconds (files took 1 minute 4.97 seconds to load)
```

That's the output of running a sample little test I built. I just created an empty file, and write a minimum-viable-spec for `String#capitalize`:

```ruby
# spec/models/string_spec.rb
require 'rails_helper'

describe String do
  it "should be capitalizable" do
    string = "josh"
    expect(string.capitalize).to eq("Josh")
  end
end
```

When I run:

```
$ time bin/rspec spec/models/string_spec.rb

String
  should be capitalizable

Finished in 1.77 seconds (files took 1 minute 40.54 seconds to load)
1 example, 0 failures

bin/rspec spec/models/string_spec.rb  0.25s user 0.14s system 0% cpu 1:44.37 total
```

There's a few reasons this high file load time causes problems, some obvious, some subtle. All there is to say is it's worth fixing. It's a big, complicated application, so I'm just capturing my thoughts...

Next, lets use two very sophisticated benchmarking tools to explore this ~2min file load time:

1. commenting things out
2. Strategic shotgunning of well-formatted `puts` statements 

See, first, I commented out pretty much everything in `rails_helper`, to try to get the file load time down. Where might you start commenting things out, to see what is causing the slowdown?

Try commenting out `require 'rails_helper`. When I do that, the files now load in about .7 seconds. 

I've come to enjoy Spring w/Rspec: [https://github.com/jonleighton/spring-commands-rspec](https://github.com/jonleighton/spring-commands-rspec)
```ruby
# Gemfile
group :test do
  gem 'spring-commands-rspec'
```

`bundle install` and then `bundle exec spring binstub rspec`

Now the _first_ time I run `b rspec spec/models/string_spec.rb` Spring re-loads the app, but all subsequent runs, the app is pre-loaded and it seems to run _much_ faster:

```
$ b rspec spec/models/string_spec.rb

String
  should be capitalizeable

Finished in 0.00503 seconds (files took 0.19154 seconds to load)
1 example, 0 failures
```

So we're loading files in 0.19 seconds, more or less. _maybe_. This is just early recon, with `require 'rails_helper'` still commented out. Uncommenting that will inject lots of slowness, but it's OK!

## Running single spec with `require 'rails_helper'`

```

String
  should be capitalizeable

Finished in 1.4 seconds (files took 1 minute 17.78 seconds to load)
1 example, 0 failures
```

I'm running this a few times to see how much variability there is on the file load time. The times I'm seeing are all around 1.5 minutes. An improvement off of 2 minutes, but not good enough. I can see from the terminal output, however, thanks to my `puts` statements (which all look like:

```ruby
puts "TIMING: doing_such_and_such"
puts "TIMING: DB Cleaner"
puts "TIMING: setting up users"
puts "TIMING: connection.execute"
```

etc. I stick these throughout `rails_helper` and `application.rb`, various helper files, etc, to see where things are moving "quickly" and "slowly". This is _extremely_ imprecise - if I wanted to be fancy, I could create a little timer class, and then do fancy calls that time exactly how long has elapsed between calls, and could order by the longest elapsed time between calls. Maybe next time.

Anyway, in iTerm, i can then `ctrl-f` for `TIMING` and have my statements highlighted as they come out:

![timing calls](/images/2021-06-16 at 11.55 AM.jpg)

This means that even when deprecation warnings and logs are being printed out, by just watching the presence of those little highlighted boxes popping up, I can get a sense of how long various components of the application/tests take to process. I'm aiming to shave _minutes_ from the test time, not milliseconds.





### Resources for file load time issues

- [How I got RSpec to boot 50 times faster](https://schwad.github.io/ruby/rails/testing/2017/08/14/50-times-faster-rspec-loading.html)
- [RSpec load time incredible long on OS X](https://stackoverflow.com/questions/33299812/rspec-load-time-incredible-long-on-os-x)
- [Testing Rails (by ThoughtBot)](https://gumroad.com/l/testing-rails)
- [Rails Testing: Files Took ‘x’ Seconds To Load](https://medium.brianemory.com/rails-testing-files-took-x-seconds-to-load-c4cbd4fa53a9)
- [How Fast is Spring?](https://spring.io/blog/2018/12/12/how-fast-is-spring)
- []()

# Conclusion

This guide is a heavy work-in-progress. If you've got questions on anything, leave a comment below. It's hooked up to a Github issue, so it's really just leaving comments via Github. 


