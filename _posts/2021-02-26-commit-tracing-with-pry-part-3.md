---
layout: post
title: "Commit Tracing In Pry (Part 3)"
published: true
date: 2021-02-26 06:00:00 -0700
description: "Applying Chelsea Troy's Leveling Up Skill of Commit Tracing"
permalink: /commit-tracing-in-pry-part-3
image: ""
---

## How Done Is This Post?

_Anything I write ranges from "super rough notes-as-i-go, don't even expect full sentences" to "this post is done and proven to deliver what it promises to deliver"_

1. Scratch-pad, take-notes-as-I-go [scratch pad notes here: Commit Tracing In Pry, notes]({{ site.baseurl }}{% link _posts/2021-02-16-commit-tracing-with-pry-part-1.md %}) 
1. Review post, clean up for first 'share'
1. I `mkdir` new directory, follow my own steps, clarify **<-- we are here**
1. Integrate feedback/answer questions from others
1. Final cleanup, post is considered `done` unless someone reaches out with further questions

----------------------

- Part 1: [Commit Tracing in Pry (part 1)]({{ site.baseurl }}{% link _posts/2021-02-16-commit-tracing-with-pry-part-1.md %})
- Part 2: [[Commit Tracing in Pry (part 2)]({{ site.baseurl }}{% link _posts/2021-02-26-commit-tracing-with-pry-part-2.md %})]
- Part 3: (you're reading this right now)

---------------------


I've now practiced "commit tracing" in the `pry` gem several times on a single commit, to prepare parts 1 and 2 of this series.

Now I'm trying a whole new (slightly modified) commit tracing exercise on another commit

I spent a few hours working struggling through commit tracing once. PLEASE go read the companion post, at least the first few main points of part 1 and 2. 

We're stepping the complexity of the commit up quite a bit. Check it out:
 
[Add Pry::Warning](https://github.com/pry/pry/commit/473bc9f2d6a0ebd93c9a09ea3c699c14e01330b0)
 
Read the [associated PR](https://github.com/pry/pry/pull/2031)
 
This looks perfect for us to practice upon! 
 
## Step 1: Navigate to the correct commit

Navigate to where you've got pry, perhaps cloan it down inside of a `commit-tracing` directory?

```
mkdir commit-tracing
cd commit-tracing
git clone https://github.com/pry/pry
cd pry
atom .
```

Now that you've got the code cloned down, you'll have to navigate to the right spot of the repository:

``` 
git co 473bc9
```

Confirm that the commit is what we expect (adding all the code in the PR):

```
git diff HEAD~
```

Cool. Lets open it up in Atom:

```
atom .
```

Then open up the desired files in Atom, either via the fuzzy finder or in your terminal:

```
git diff HEAD~ --name-only | xargs atom
```

## Step 2: Write down that commit on a piece of paper

Now, lets write out the commit on paper. I _think_ I'm going to only write down the _added_ code. TBD if this is the right approach:

<add picture of handwritten code>

OK, 13 min later, here's what I wrote:

<add picture of handwritten code>

## Step 3: Annotate that hand-written code

Now, I'll annotate it. The process of writing it out brought me quite a bit "closer" to it. I now have a grasp of what portions of it made sense to me, and what portions _didn't_ make sense. 

I understand lots of the primitive bits of the ruby, but nearly nothing else.

First, underlining things in red that I have questions with, doodling notes elsewhere. I used two pens (red and black) and these additions took about 7 minutes, and increased my understanding of exactly what's going on quite a bit.

## Step 4: Keep the test, re-build `prompt.rb`:

### Step 4.0: Confirm tests pass

```
rspec spec/warning_spec.rb
```

### Step 4.1: Delete `lib/warning`

Here's the beginning of this step:

![setup for step 1](/images/2021-02-26 at 2.40 PM-rebuild-code.jpg)

### Step 4.2: rerun the test, confirm it's failing

And finishing the step:

![deleted the code](/images/2021-02-26 at 2.41 PM-rerun.jpg)


### Step 4.3: `tdd` your way through this as best as you can

For example, you know how to fix `uninitialized constant Pry::Warning`:

```ruby
class Pry
  module Warning
    
  end
end
```

I already know it'll next throw a `method not found`, so lets just add that:

```ruby
class Pry
  module Warning
    def self.warn(message)
      
    end
  end
end
```

Now I have no idea... running the test:

```shell
rspec spec/warning_spec.rb

Pry::Warning
  #warn
    prints a warning with file and line (FAILED - 1)

Failures:

  1) Pry::Warning#warn prints a warning with file and line
     Failure/Error:
       expect(Kernel).to receive(:warn).with(
         "#{__FILE__}:#{__LINE__ + 2}: warning: foo bar"
       )

       (Kernel).warn("/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar")
           expected: 1 time with arguments: ("/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar")
           received: 0 times
     # ./spec/warning_spec.rb:4:in `block (3 levels) in <top (required)>'
```

Yeah, makes sense, I never bubbled anything up to `Kernal#warn` [checking the docs](https://ruby-doc.org/core-3.0.0/Kernel.html#method-i-warn)

```ruby
class Pry
  module Warning
    def self.warn(message)
      Kernal.warn(message)
    end
  end
end
```

Hah, I cannot spell `Kernal` correctly...

```
rspec spec/warning_spec.rb

Pry::Warning
  #warn
    prints a warning with file and line (FAILED - 1)

Failures:

  1) Pry::Warning#warn prints a warning with file and line
     Failure/Error: Kernel.warn(message)

       Kernel received :warn with unexpected arguments
         expected: ("/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar")
              got: ("foo bar")
     # ./lib/pry/warning.rb:4:in `warn'
     # ./spec/warning_spec.rb:7:in `block (3 levels) in <top (required)>'

```

OK, so the expected strings are different. We want `file_path:line-number: warning: <message>`

Way back when, I was trying to TDD my way through the Rake gem. I wrote about it here: [Deliberate Practice in Programming with Avdi Grimm and the Rake gem](https://josh.works/deliberate-practice-avdi-grimm-rake-gem)

I remember encountering `__LINE__` and `__FILE__` from that. Re-reading it to refresh my memory...

(So far, I've not glanced at my piece of paper with the "answers" for this method. I'm moving right along, not losing any time to unproductive struggle.)

the `File` class can help us here. [`File#expand_path`](https://ruby-doc.org/core-3.0.0/File.html#method-c-expand_path). Fire up a `pry` session in your terminal and try running `__FILE__`, `__LINE__`, etc:

![self-explanatory](/images/2021-02-26 at 2.55 PM-exploration.jpg)

Not too complicated. Lets use a little string interpolation to get us closer to our desired output:

```ruby
class Pry
  module Warning
    def self.warn(message)
      
      
      msg = "#{__FILE__}:#{__LINE__}: #{message}"
      
      Kernel.warn(msg)
    end
  end
end
```

Yep, very close. Here's our actual/intended output:

```shell
expected: "/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar"  
got:      "/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/lib/pry/warning.rb:6: foo bar"
```
I'll simplify the output to make it more readable. 

```
expected: "./commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar"  
got:      "./commit-tracing/pry/lib/pry/warning.rb:6: foo bar"
```

OK, we can close most of this gap easily:

```ruby
class Pry
  module Warning
    def self.warn(message)
      
      
      msg = "#{__FILE__}:#{__LINE__ + 1}: warning: #{message}"
      
      Kernel.warn(msg)
    end
  end
end
```

```
expected: ("./commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar")
     got: ("./commit-tracing/pry/lib/pry/warning.rb:7: warning: foo bar")
```

So, the source of the file is coming back wrong. 

It's showing to have been generated in `warning.rb`, but really it should be reported as coming from the `warning_spec` file. 

I've gotten this far without looking at my notes, but now I'm going to take a look. 

There's this `caller_locations` thing I need to examine... we'll stick a pry in our new method, and explore `caller_locations`.

![caller_locations](/images/2021-02-26 at 3.03 PM-caller-locations.jpg)

Oh, that reminds me of this `clean_caller` thing I dealt with long ago...

<embed tweet to clean_caller thing in pry>

[https://twitter.com/josh_works](https://twitter.com/josh_works)

In my `~/.pryrc`, I have:

```ruby
Pry.config.commands.command 'caller_clean', 'show call stack with lines mentioning "gem" removed' do |foo|
  output.puts caller.reject {|l| l.include?('/gems')}.join("\n")
```

So... I've interacted with the `caller` before. I can use it in pry, and call `caller_clean` and it "cleans up" the output


Anyway, I stuck a `pry` in the `Pry::Warning::warn` method, like so:

```ruby
class Pry
  module Warning
    def self.warn(message)
    
      require "pry"; binding.pry
      # 'breaking' the code here is messing with my output
      msg = "#{__FILE__}:#{__LINE__ + 1}: warning: #{message}"
      
      Kernel.warn(msg)
    end
  end
end
```

This is messing with my test output, since I'm trying to generate a `caller` entry from `warning_spec.rb`. Lets take the pry out of `warning.rb` and move it here:

```ruby
RSpec.describe Pry::Warning do
  describe "#warn" do
    it "prints a warning with file and line" do
      require "pry"; binding.pry
      expect(Kernel).to receive(:warn).with(
        "#{__FILE__}:#{__LINE__ + 2}: warning: foo bar"
      )
      described_class.warn('foo bar')
    end
  end
end
```
Let's see what `__FILE__` is:

```
> __FILE__
=> "(pry)"
```

Also take a look at `caller`. It reads top-to-bottom, doesn't match up with the desired output as far as I can tell...

Hm. Taking a look at my notes now...

```
caller_locations(1..1)
```

Hm. OK, in the pry session, I'm calling (and examining):

```
caller_locations
caller_locations(1..1)
caller_locations(1..1)
caller_locations.first
```

So now I'm updating my `warning.rb` to be:

```ruby
class Pry
  module Warning
    def self.warn(message)
      location = caller_locations.first
      # __FILE__ and `caller_locations.first` are the same?
      
      msg = "#{location}:#{__LINE__ + 1}: warning: #{message}"
      
      Kernel.warn(msg)
    end
  end
end
```

Getting close:

```
Kernel received :warn with unexpected arguments
        expected: ("pry/spec/warning_spec.rb:7: warning: foo bar")
             got: ("pry/spec/warning_spec.rb:7:in `block (3 levels) in <top (required)>':8: warning: foo bar")
```

So, now the path is correct. Win. I... don't know what to do about the error message, though. 

_glances at notes_

Ah, I guess I should examine `location`and `caller_locations` a bit more in pry...

```ruby
[4] pry> location = caller_locations.first
=> "/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/lib/pry/pry_instance.rb:370:in `eval'"
[5] pry> location.class
=> Thread::Backtrace::Location
[6] pry>
```

Oh. So... this `caller_locations` thing _looked_ like an array of strings, but it's actually an array of `Thread::Backtrace::Location` objects.

```ruby
location.methods
```

Try calling some of these methods...

![location stuff](/images/2021-02-26 at 4.08 PM-exploring-location-object.jpg)

OK. Now, working this back into the `warning.rb` class, futzing around with adding + 1, + 2, adding/removing the pry from `warning_spec.rb`, in order to evaluate the output:

```ruby
class Pry
  module Warning
    def self.warn(message)
      location = caller_locations.first
      # __FILE__ and `caller_locations.first` are the same?
      path = location.absolute_path
      lineno = location.lineno
      
      msg = "#{path}:#{lineno}: warning: #{message}"
      
      Kernel.warn(msg)
    end
  end
end
```

Here's some of the error messages I was getting on the way:

```
expected: ("commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar")
     got: ("commit-tracing/pry/spec/warning_spec.rb:8: warning: foo bar")
     
 expected: ("commit-tracing/pry/spec/warning_spec.rb:7: warning: foo bar")
      got: ("commit-tracing/pry/spec/warning_spec.rb:9: warning: foo bar")
```

And with the above code, the test passes!

Woot.

I'm not going to worry about the `ruby 1.9` support `if/else`. `ruby 2.0.0` came out in 2015, and I kinda doubt that people are still running `ruby 1.9`.

I also don't want to do `rvm install ruby 1.9.0`, deal with configuring my machine to run ruby 1.9.

We can see that both of these approaches would work though. I hopped back into pry, called `caller.first.split(':')`, etc. Explore it yourself. I don't know what to make of it.

_delete the code, rebuild it all again_

### Step 4.4: `tdd` your way through this _again_

OK, take a long break. Do it again. Try to not look at your paper this time. I'm not going to need it, I don't think...

A little bit of running the tests, and I'm here:

```ruby
class Pry
  module Warning
    def self.warn(message)
      caller = caller_locations.first
      file = caller.absolute_path
      
      msg = "#{file} #{message}"
      
      Kernel.warn(msg)
    end
  end
end
```

The output is almost right...

A little more work, and the tests pass, with:

```ruby
class Pry
  module Warning
    def self.warn(message)
      caller = caller_locations.first
      file = caller.absolute_path
      lineno = caller.lineno
      msg = "#{file}:#{lineno}: warning: #{message}"
      
      Kernel.warn(msg)
    end
  end
end
```

This 2nd rebuild took about... 4 minutes. Maybe 5. Didn't look at my paper once. I'm going to go with this dramatically simplified implementation of this class. 

I re-ran all the tests, and got some failures. Let me add this if/else case and see if they pass...

Nope, still fails. OK, don't know why they, but not worrying about it. 

A little refactor brings us to:

```ruby
class Pry
  module Warning
    def self.warn(message)
      caller = caller_locations.first
      file = caller.absolute_path
      lineno = caller.lineno
      
      Kernel.warn("#{file}:#{lineno}: warning: #{message}")
    end
  end
end
```

I'm content with this. 

## Delete the test, re-write the test and the class

Just like before, select everything in the `warning_spec.rb` and `warning.rb` files, rebuild it, running tests as you go.

_had to look at the page to refresh myself on what to name it_

_got a little farther, still don't have an MVP test, looking at my paper again_

Here's my MVP test, deviated slightly from what was written, but I grok this:

```ruby
RSpec.describe Pry::Warning do
  describe "#warn" do
    it "should get a message" do
      expect(Kernel).to receive(:warn).with(
        "blarg"
      )
      
      Pry::Warning.warn('blarg')
    end
  end
end
```

Run the tests, get things like `no class`, `no method`, and now it passes, like so:

(I am so bad at spelling `Kernel`. `el`, not `al`)

```ruby
class Pry
  module Warning
    def self.warn(message)
      
      Kernel.warn(message)
    end
  end
end
```

Let's make our tests a bit better:

```ruby
RSpec.describe Pry::Warning do
  describe "#warn" do
    it "should get a message" do
      expect(Kernel).to receive(:warn).with(
        "#{__FILE__}:#{__LINE__}: warning: blarg"
      )
      
      Pry::Warning.warn('blarg')
    end
  end
end
```

Now things fail again, so make it pass.

```ruby
class Pry
  module Warning
    def self.warn(message)
      caller = caller_locations.first
      file = caller.absolute_path
      lineno = caller.lineno
      
      
      Kernel.warn("#{file}:#{lineno}: warning: #{message}")
    end
  end
end
```

OK, now the test fails again:

```
1) Pry::Warning#warn should get a message
   Failure/Error: Kernel.warn("#{file}:#{lineno}: warning: #{message}")

     Kernel received :warn with unexpected arguments
       expected: ("/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/spec/warning_spec.rb:5: warning: blarg")
       got: ("/Users/joshthompson/me/intermediate_ruby_obstacle_course/commit-tracing/pry/spec/warning_spec.rb:8: warning: blarg")
```

Notice the difference - the line number is wrong. We can see where we're going wrong, look at the line numbers of the spec!

Subtract the 5 from the 8, and that's the expected difference in where the actual `Kernal.warn(message)` message is sent, vs where `__LINE__` is in the file when it's called.

And... you can play around to get it to work:

```ruby
RSpec.describe Pry::Warning do
  describe "#warn" do
    it "should get a message" do
      expect(Kernel).to receive(:warn).with(
        "#{__FILE__}:#{__LINE__ + 2}: warning: blarg"
      )
      Pry::Warning.warn('blarg')
    end
  end
end
```

Sick. I rebuilt this test and got it working in not many minutes. Lets try it again, see if I can do it without paper notes.

### Step 4.5: rebuild the test (and the library) a second time

Start fresh again:

Ended up with:

```ruby
RSpec.describe Pry::Warning do
  describe "#warn" do
    it "should return path, line number, message" do
      expect(Kernel).to receive(:warn).with(
        "message"
      )
      
      Pry::Warning.warn("message")
    end
  end
end
```

No notes needed, off to make it pass

30 seconds later, it passes. Lets update the test:

```ruby
RSpec.describe Pry::Warning do
  describe "#warn" do
    it "should return path, line number, message" do
      expect(Kernel).to receive(:warn).with(
        "#{__FILE__}:#{__LINE__ + 2}: warning: message"
      )
      
      Pry::Warning.warn("message")
    end
  end
end
```

Make it pass...

other than forgetting that the method is `absolute_path`, and not `absolute_url`, this was easy.

I did it all with good process, in just three or four minutes. 

## Step 5 Reset the repo to before this commit

You'll end up rebuilding this one more time, should take only 4 minutes, and you'll also get to now make the refactors included in this PR. I'm still avoiding looking at my paper

```
git stash
git reset --hard HEAD~
```

## Step 6 Refactor the existing codebase to use `Pry::Warning::Warn`

So... I'm not sure how to find the files that need refactoring. 

Obviously I've got the names in the PR, but if I were doing this myself, how would I find them? It's likely that this class is going to replace some existing method calls, maybe to `Kernel` directly?

I kinda combined steps 5 and 6 together, sorry for the confusion. 

Now that the repo is reset to before this PR, re-add the test, make it pass, and then lets find the refactoring opportunities...

OK, that took me about 4 minutes to rebuild, completely. I'm feeling comfortable with this now...

For the refactor... I give up. I don't know how I would have found these...

`ctrl-f`-ing the entire repo for:

- `Kernel.warn` (nothing)
- `warn` (lots of things. 120 results, 30 files)
- `.warn` (6 results, 4 files. )
- `warn(` this is the key search wherry to find the refactors?



## Checks for Understanding

### From round 1, rebuilding `warning.rb`

- what is `caller`? 
- what is `__LINE__`? 
- what is `__FILE__`?
- what does `caller_locations` look like? What are some of it's methods. 
- why might you use `caller_locations` instead of `__FILE__` in `Pry::Warning::Warn`


OK. I had to study it a bit, the finished PR, and the refactors I was just doing, in order to make each exact change.

I'm now understanding how all these pieces fit together, quite nicely.

I'm going to call it a day here, and I'll come back and repeat this entire PR, from scratch, without looking at my paper or the actual changed code, and I'll see if I can get the whole thing done.

I'll start from:

```
git reset --hard 473bc9f2d6a0ebd93c9a09ea3c699c14e01330b0~
git clean --dry-run
git clean -f
```

Look up `git clean` (`tldr git clean`) to get a feel for how it works. 

PHEW! Taking a break for a while now.



## Footnotes