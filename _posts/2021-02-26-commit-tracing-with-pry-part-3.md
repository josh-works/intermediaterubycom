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

<embed tweet to clean_caller thing>



## Checks for Understanding



## Footnotes