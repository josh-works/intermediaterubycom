---
layout: post
title:  "Rebuilding Rails, Part 1"
description: "I take detailed notes, nearly all the time"
date:  DATE 06:00:00 -0700
crosspost_to_medium: false
categories: [course_notes, tutorial_walkthrough, rebuilding_rails]
tags: [rails, rebuilding_rails, tutorial_walkthrough]
permalink: rebuilding-rails-course-walkthrough-part-1
image: /images/title_image.jpg
issue_id: 6
---

## Rebuilding Rails Course Notes

Supposedly, the completion rate for online courses is rather low. I've certainly bought many more courses than I've finished.

I don't want to do this with Noah Gibbs' [Rebuilding Rails](https://rebuilding-rails.com/) course. He's an expert by every measure of the word, and learning directly from him sounds like some of the best use of my time available. 

This page will be my scratch-pad of notes, observations, gotchas, and more. 

I'm working through this course a week or two after a friend started it, and I wanted to make sure I could document the things he recommended. For example, two days ago, he said something like: 

> When in doubt, add testing for at least Minitest, when the option presents itself. It'll make working through one of the chapters or extensions easier. 

I bought the course, read the introduction, and skimmed the first few chapters, and the last chapter. I've been working in Ruby and Rails for a while, so I didn't need to do anything from a "setup" perspective.


------------------

## Chapter 1: Zero to "It Works"

The first command to run is `bundle gem rulers`.

I've not done lots with bundle, so I looked up `bundle --help`. Lots of output. Of import:

```
  bundle gem NAME [OPTIONS]      # Creates a skeleton for creating a rubygem
```

So `bundle gem --help`:

```
> bundle gem --help
Usage:
  bundle gem NAME [OPTIONS]

Options:
  --bin, -b, [--exe], [--no-exe]   # Generate a binary executable for your library.
          [--coc], [--no-coc]      # Generate a code of conduct file. Set a default with `bundle config set gem.coc true`.
  -e, [--edit=EDITOR]              # Open generated gemspec in the specified editor (defaults to $EDITOR or $BUNDLER_EDITOR)
          [--ext], [--no-ext]      # Generate the boilerplate for C extension code
          [--git], [--no-git]      # Initialize a git repo inside your library.
                                   # Default: true
          [--mit], [--no-mit]      # Generate an MIT license file. Set a default with `bundle config set gem.mit true`.
  -t, [--test=rspec]               # Generate a test directory for your library, either rspec or minitest. Set a default with `bundle config set gem.test rspec`.
          [--no-color]             # Disable colorization in output
  -r, [--retry=NUM]                # Specify the number of times you wish to attempt network commands
  -V, [--verbose], [--no-verbose]  # Enable verbose output mode

Creates a skeleton for creating a rubygem
```

OK. Off to the races. 

```
> bundle gem rulers
Creating gem 'rulers'...
Do you want to generate tests with your gem?
Type 'rspec' or 'minitest' to generate those test files now and in the future. rspec/minitest/(none):
```

I'll initialize it with `minitest`. Worst case, I just won't run those tests. This _might_ be what my friend Mark was referencing earlier about "initialize the Gem with a test file!"

Cool. Initial commit done. I'm tracking this all in [this repo](https://github.com/josh-works/rebuilding-rails/tree/main).

Arg, running `bundle gem NAME` initializes the gem with its own git repo, so I'm going to update my directory structure.

Here's what I have:

![directory structure](/images/2021-05-04 at 9.53 AM.jpg)

And I'm going to bump the `rulers` directory up one level.

... 

Nevermind. `rm -rf`'d the directory. Rebuilding from scratch. (I was running into a problem renaming the branch from `master` to `main`, I should have `git add/commit` before running `git branch -m master main`)

Turns out I've now set the defaults from my first time through. Run:

`ls ~/.bundle` to see the files you've got related to bundler default. 

`cat ~/.bundle/config` and you'll see the defaults you just set:

![defaults](/images/2021-05-04 at 9.58 AM.jpg)

Onward!

I'm now tracking this gem here: [https://github.com/josh-works/rulers/tree/main](https://github.com/josh-works/rulers/tree/main)


updated `rulers.gemspec` per the recommendation, ran:

```
$ gem build rulers.gemspec
$ gem install rulers-0.0.1.gem
```

Checking that it worked:

```
> gem list | grep rulers
rulers (0.0.1)
```

[Inspecting the output of `gem list --help` to find that `-d` flag]

```
> gem list -d rulers

*** LOCAL GEMS ***

rulers (0.0.1)
    Author: Josh Thompson
    Homepage: https://intermediateruby.com
    License: MIT
    Installed at: /Users/joshthompson/.rvm/gems/ruby-2.5.8

    Practicing Noah Gibb's Rebuilding Rails course
```

Looks like it worked! off to the races!

Commit [60065dc](https://github.com/josh-works/rulers/commit/60065dc)

### Hello World, more or less

`cd`-ing up a directory, making a new "app", per the recommendation:

Done. All looks good:

![making the app](/images/2021-05-04 at 10.26 AM.jpg)

### Gotcha: `Gem::InvalidSpecificationException`

![Gem::InvalidSpecificationException](/images/2021-05-04 at 11.26 AM.jpg)

I ran into a minor problem when I modified the gem and tried to run `gem build rulers.gemspec`:

```
> gem build rulers.gemspec
WARNING:  See http://guides.rubygems.org/specification-reference/ for help
ERROR:  While executing gem ... (Gem::InvalidSpecificationException)
    rulers-0.0.1 contains itself (rulers-0.0.1.gem), check your files list
```

I tried deleting `rulers-0.0.1.gem` from my terminal, but the error still cropped up. I don't remember the exact order that I went with, but it wasn't until I `git add`ed the deleted file that the command worked. 

I googled the error, found [this](https://stackoverflow.com/a/26945253/3210178) StackOverflow suggestion.

So, I'm going to ignore the "compiled" gem going forward. Might end up `.gitignore`-ing it or something. 

Followed the next steps, and now I've got "rackup" sourced/working from the `rulers` gem instead of the `bestquotes` app. Here's links to the specific commits:

- [best_quotes commit](https://github.com/josh-works/best_quotes/commit/328ed2b6af8455ea624fe6d3614b24c523ddb71a)
- [rulers commit](https://github.com/josh-works/rulers/commit/710faf0d185ed4fa65f7a3a5f9ed967fc8d0f289)

And here's how we know in the browser:

![hello from RoRulers](/images/2021-05-04 at 11.47 AM.jpg)

## Chapter 1 Exercises

### Exercise 1: Add Debugging to the app

```diff
diff --git a/lib/rulers.rb b/lib/rulers.rb
index 25760e3..ccf735f 100644
--- a/lib/rulers.rb
+++ b/lib/rulers.rb
@@ -3,6 +3,7 @@
 module Rulers
   class Application
     def call(env)
+      `echo debug > debug.txt`;
       [200, {'Content-Type' => 'text/html'},
       ["Hello from RoRulers"]]
     end
```


Then re-build/re-install the gem, restart rack, reload the page, and you'll get a file titled `debug.txt` in your `best_quotes` directory. 

```
$ cat debug.txt
debug
```

It's not super exciting. I wanted more info.

For the record, I didn't know that running shell commands inside of backticks would... run shell commands. 

So that's cool. But I wanted more info than this, so I tried logging `env` inside the debug statement, like so:

```
`echo debug env > debug.txt`;
```

And rebuild the gem, reinstall it, restart `rack`, reload the page... and I started getting `parse errors` and `unexpected newlines`. I knew I was getting closer.

So I tried some string interpolation:

```ruby
`echo debug "#{env}" > debug.txt`;
```

Still not quite there.

Here's what I was seeing:

![no good](/images/2021-05-04 at 3.33 PM.jpg)

I know string interpolation and character escaping in Ruby isn't trivial, but it's also not that hard. 

I googled `ruby escape control characters string`, clicked the first result, ["Escaping Characters in Ruby" (AppSignal)](https://blog.appsignal.com/2016/12/21/ruby-magic-escaping-in-ruby.html), skimmed it down to `Escaping Interpolation`, where they say:

> Escaping interpolation
> 
> Ruby supports interpolation inside strings. But once again, not all string definitions are created equal. Interpolation only works in double quoted strings.
> 
> In the code example below we see that interpolation works in a double quoted string, but that Ruby escapes the interpolation sequence in a single quoted string, rendering it useless.

And they included the following snippet:

```ruby
name = "world"

"Hello #{name}"
=> "Hello world"

'Hello #{name}'
=> "Hello \#{name}"
```
This is actually exactly what I wanted! I "upgraded" my double quotes around `env` to single quotes:

```diff
diff --git a/lib/rulers.rb b/lib/rulers.rb
index 25760e3..ccf735f 100644
--- a/lib/rulers.rb
+++ b/lib/rulers.rb
@@ -3,6 +3,7 @@
 module Rulers
   class Application
     def call(env)
+      `echo debug '#{env}' > debug.txt`;
       [200, {'Content-Type' => 'text/html'},
       ["Hello from RoRulers"]]
     end
```

And it worked! 

One quick rebuild, reinstall, restart, reload later:

![success](/images/2021-05-04 at 3.40 PM.jpg)

[Here's the commit](https://github.com/josh-works/rulers/commit/872c6b46119a4681b2431ad110221924edaeb847)

### Exercise 2: Your Library's Library

The guide has us adding a new array method (it's actually already an existing array method, but we'll cross that bridge later) and it talks about the importance of `git add`-ing the new files, because when you call `gem build rulers.gemspec`, it checks with _git itself_ to see what files to compile. 

This is totally sensical, reasonable, etc.

In the `gemspec`, we've got:

```ruby
spec.files         = Dir.chdir(File.expand_path('..', __FILE__)) do
  `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
end
```

I've used `git ls-files` quite a bit. Most recently, when figuring out how to get `Rubocop` to run only on modified files. I wrote about that general process extensively in  [intermediate_ruby_obstacle_course/rubocop](https://github.com/josh-works/intermediate_ruby_obstacle_course/tree/main/rubocop#run-rubocop-only-on-modified-files-using-git-ls-files). Take a gander there, if you'd like. 

Anyway, all this to say - if you add a new file to your gem and don't `git add` it, even if you `gem build ...` the files will be missing.

Also, I wanted evidence that this new method was working, so I named my new method `summm`:

[Add Array#summm](https://github.com/josh-works/rulers/commit/1de7d2d49a71d93fe7e37d97c8dc4c49d0e742c8)

In my `best_quotes` repo:

```ruby
# /best_quotes/config/application.rb
require 'rulers'

module BestQuotes
  class Application < Rulers::Application
    puts "hi there"
    puts [1, 3, 5].sum # I added this to test the "base case"
    puts [1, 3, 5, 11].summm # and to test the new method from the gem
  end
end
```

Evidence that it succeeds:

![Array#summm](/images/2021-05-04 at 4.14 PM.jpg)

### Exercise 3: Test Early, Test Often

I added `rack-test` and `minitest` to the `rulers.gemspec` file as a `development_dependency`. 

I then noticed I already had a `test` directory with a `test_helper` inside of it, containing everything the tutorial wanted me to add. I think this is what I get by specifying "minitest" in the interactive `gem new NAME` command process.

The `$LOAD_PATH` is familiar to me, assuming it's at all related to my Linux/Mac's `$PATH`. 

the `__dir__` is probably related to `__FILE__` and `__LINE__`, which I've encountered doing some [commit tracing with the Pry gem](https://www.intermediateruby.com/commit-tracing-in-pry-part-3#step-43-tdd-your-way-through-this-as-best-as-you-can) and [trying to implement the principles of deliberate practice with Avdi Grimm and the Rake gem](https://josh.works/deliberate-practice-avdi-grimm-rake-gem). 

OK, I'm not going to add more tests, even though I'm suggested that I do.

[this gist](https://gist.github.com/JoshCheek/989a099594059ebf3015) by Josh Cheek is great! Tons of potential. I'll upgrade my testing some day.

Current commit: [https://github.com/josh-works/rulers/commit/d562747261bcf1f94af5b4e5de2bc73344576582](https://github.com/josh-works/rulers/commit/d562747261bcf1f94af5b4e5de2bc73344576582)

### Exercise 4: Other Application Servers

```
gem install unicorn
unicorn config.ru
```

Unicorn serves on localhost:8080 by default, but you can override to 3001 w/ `unicorn -p 3001`. This exercise was... easy.

### Exercise 5: Ignoring Files

Ah, he recommends doing what I'd suspected I should do earlier - .gitignore the compiled versions of the gem.

A one-line addition to the `.gitignore`:

[https://github.com/josh-works/rulers/commit/cf9e1d295da17bdecf34ba45322bbc5780ba6287
](https://github.com/josh-works/rulers/commit/cf9e1d295da17bdecf34ba45322bbc5780ba6287
)
And this concludes chapter 1.

## Chapter 2: Your First Controller

This went pretty smoothly, until I tried to run the changes to my `best_quotes` app.

I spent a little while on this error:

![Uninitialized Constant](/images/2021-05-05 at 6.06 PM.jpg)

I poked around for a little bit, confirmed that I'd named things correctly, couldn't figure it out.

I eventually had to pull up the [Chapter 2 commit](https://github.com/noahgibbs/rulers/commit/cb3f322f0425baca0d09baecc9579ee56c57ceab) from Noah Gibb's implementation of this project, and I found the problem.

In `lib/rulers.rb`, I forgot to `require` my new routing file.

Fixed that, and we were off to the races!

Also, I'm following along with Ben Orenstein's "Improve your code quality" challenge. Today's challenge was [get rid of a warning you're used to ignoring](https://forum.codequalitychallenge.com/t/day-3-get-rid-of-a-warning/1125).

These warnings seemed like good candidates: 

![bad warnings](/images/2021-05-05 at 6.10 PM.jpg)

So I `gem list`'ed the offending gems, picked ~a version at random~ the newest gem version, and [added it to my `Gemspec`]. Now when I `gem build rulers.gemspec` the output is nice and clean:

![no warnings](/images/2021-05-05 at 6.12 PM.jpg)

[9e730b9](https://github.com/josh-works/rulers/commit/9e730b9792aa745dc4d702fbd36ac7036894033b)


UGH, stuff is still broken. 

```
> gem build rulers-0.0.2.gem
Invalid gemspec in [rulers-0.0.2.gem]: undefined local variable or method `metadata' for Gem::Specification:Class
ERROR:  Error loading gemspec. Aborting.
```

### Gotcha: Update the `best_quotes` `Gemfile.lock` to source the `0.0.2` version of `rulers`


Ah, here's the problem - I combed through the commit on the `rulers` gem for chapter 2, couldn't see my problem. I looked at the [chapter 2 commit for `best_quotes`](https://github.com/noahgibbs/best_quotes/commit/d50f8a983cb67176978a02b6fa1f1ac0d4c637b5), and found the issue:

```diff
diff --git a/Gemfile.lock b/Gemfile.lock
index d5880f6..81087d4 100644
--- a/Gemfile.lock
+++ b/Gemfile.lock
@@ -2,7 +2,7 @@ GEM
   remote: https://rubygems.org/
   specs:
     rack (2.2.3)
-    rulers (0.0.1)
+    rulers (0.0.2)
       rack

```

you can manually increment the value, or run `bundle update rulers`. 

Noah mentioned this at the beginning of the chapter. He said:

> You may also need to "bundle update rulers" in best_quotes.

This didn't land when I read it the first time, but I'm seeing it now. 

I'm making progress...

Now I'm getting more errors. Le sigh. When I visit `localhost:3001`, I get:

```
NameError at /
uninitialized constant Controller
```

`localhost:3001/hi`:

```
NameError at /hi
uninitialized constant HiController
```

So, something is wrong, obviously. What?

...

### Gotcha: Visit `http://localhost:3001/quotes/a_quote`, not `http://localhost:3001/`

Oh boy. I simply forgot to visit the intended URL. Wow. 

I'd been running `rackup -p 3001`, and then visiting `localhost:3001`, expecting to see... well, not an error. 

But for this to work, I needed to visit http://localhost:3001/quotes/a_quote, which Noah mentioned in his book. 

So, nothing was broken. That was a lot of combing through code, trying to diff my code and his, and not understanding why it wasn't working. 

Well, now I know.

Noah even called this out explicitely. I wish I wasn't so bad at reading:

> If you didn’t quite get it, please make sure to include “quotes/ a_quote” in the URL, like you see above -- just going to the root no longer works. If you see "Uninitialised constant Controller" then your URL is probably off.

Now I'm playing around with trying to get the tests to work, so I can stick a `pry` in various spots and see how this is all wired together.

Phew. Chapter 2, going slowly. 

