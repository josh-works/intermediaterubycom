---
layout: post
title: "Commit Tracing In Pry (Part 2)"
published: true
date: 2021-02-26 06:00:00 -0700
description: "Applying Chelsea Troy's Leveling Up Skill of Commit Tracing"
permalink: /commit-tracing-in-pry-part-2
image: ""
---

## How Done Is This Post?

_Anything I write ranges from "super rough notes-as-i-go, don't even expect full sentences" to "this post is done and proven to deliver what it promises to deliver"_

1. Scratch-pad, take-notes-as-I-go [scratch pad notes here: Commit Tracing In Pry, notes]({{ site.baseurl }}{% link _posts/2021-02-16-commit-tracing-with-pry-part-1.md %}) 
1. Review post, clean up for first 'share' **<-- we are here**
1. I `mkdir` new directory, follow my own steps, clarify
1. Integrate feedback/answer questions from others
1. Final cleanup, post is considered `done` unless someone reaches out with further questions

----------------------

I spent a few hours working struggling through commit tracing once. PLEASE go read the companion post, at least the first few main points: [Commit Tracing in Pry take 1]({{ site.baseurl }}{% link _posts/2021-02-16-commit-tracing-with-pry-part-1.md %}) 

I've finished that first pass, and now I want to do it quickly, concisely, from scratch, and timed to various steps. I'm making a resource I can hand off to an early-career software developer and have them gain _immediate_ value. 

## Commit Tracing Overview

Read Chelsea Troy's post: [Leveling Up Skill #6: Commit Tracing](https://chelseatroy.com/2018/07/21/leveling-up-skill-6-commit-tracing/).

### Why To trace commits in the Pry Gem

Pry is a ubiquitous tool in the Ruby/Rails community, seemed like a good place to start.

## Which Commit to Trace?

Last time, I spent a long time exploring commits. Now I've traced a commit, and, having found a few good commits to execute this technique upon, you'll get the enjoyable, smoother journey. Again, refer to part 1 of this series for my raw notes of explorations, mis-steps, and more.

Here's the list of commits I explored. I mostly skimmed the commit titles, occasionally opening up the commit to look harder: [Pry commits](https://github.com/pry/pry/commits/master)

We'll start with this commit: [Add Pry::Env](https://github.com/pry/pry/commit/7ce5ca70bb4a1ff447269bdde4cb5d07b8932c8a)

## Step 1: Get Pry Source Code

In whatever directory you'd like to work in (I have a `commit-tracing` directory) clone down the `pry` repo:

```shell
git clone git@github.com:pry/pry.git
cd pry
```

## Step 2: Check out the repo to the commit in question

Based on the [PR in question](https://github.com/pry/pry/commit/473bc9f2d6a0ebd93c9a09ea3c699c14e01330b0), you'll have what you need to check the repo out to the right place, which is _the commit of the changes we're about to trace_


```shell

git checkout 7ce5ca70bb4a1ff447269bdde4cb5d07b8932c8a
git checkout 7ce5ca # the first six characters of the commit sha is sufficient
```

## Step 3: get the diffs for the prior commit

```
$ git diff HEAD~
```

Open up the files in question:

## Step 4: Open these files in your editor


```
git diff HEAD~ --name-only 
git diff HEAD~ --name-only | xargs atom
```

## Step 5: Copy all the diffs down by hand on paper

This commit took me about 10 minutes. Do it. Do it. DO NOT SKIP THIS STEP WITHOUT WRITING IT OUT ON PAPER!

## Step 6: Delete the lib code

Run the tests. You could just run `rspec` and see all the tests run, or pass the path to the test in question:

```
rspec spec/env_spec.rb
```

Now that you're running just that one test, can delete the lib code, and rebuild it from the tests.

THIS IS WHERE THE LEARNING HAPPENS! Everything up to here has been _prep_ for the learning that's about to happen.

## Step 7: Make the tests pass

## Step 8: Delete the lib AND the `spec` code

now do `git reset --hard HEAD~`, and rebuild the entire commit. 

Do it at least twice, until you can do it from scratch, without looking at the paper.

Here's the code I ended up with, without refering to any paper, writing tests and making them pass as I go:

```ruby
class Pry
  module Env
    def self.[](key)
      value = ENV[key] 
      return if value == ''
      
      value
    end
  end
end
```

```ruby
RSpec.describe Pry::Env do
  describe "#[]" do
    let(:key) { "test-key" }
    after { ENV.delete(key) }
    
    context "when ENV is provided" do
      before { ENV[key] = 'test-value' }
      it "should return the value" do
        expect(described_class[key]).to eq 'test-value'
      end
    end
    
    context "when ENV is not provided" do
      it "should return nil" do
        expect(described_class[key]).to be_nil
      end
    end
    
    context "when ENV is provided but set to '' " do
      before { ENV[key] = '' }
      
      it "should return nil" do
        expect(described_class[key]).to be_nil
      end
    end
  end
end
```

Cool. I'm done tracing this commit.

## Checks for Understanding

### What is commit tracing? 

### `git stash` not working, how to fix?

If you are trying to move commits, you don't care about saving your work, and you do something like:

```
$ git checkout 7ce5ca
error: The following untracked working tree files would be overwritten by checkout:
	lib/pry/env.rb
	spec/env_spec.rb
Please move or remove them before you switch branches.
Aborting
```

What do you do?

```
git stash
```

and try again?

Not quite! Run `git status`, you'll see they're unaffected.

1. Add the files to git: `git add .`
2. stash them: `git stash`
3. now checkout the new commit: `git checkout 7ce5ca`

### How do you view what the current commit changed?

`git diff` gives you nothing...

```
git diff HEAD~
```

### What commit does `HEAD~1` reference? What's a common alias?

```
HEAD   => wherever the repo "is", "right now"
    ~1 => "backwards" one commit
```

If you don't pass a number, you can shorten this to:

```
HEAD~
```

### How do you find the names of the changed files?

```
git diff HEAD~1 --name-only
```

### How can you pass the list of changed files to your editor to open them all at once?

```
git diff HEAD~1 --name-only | xargs atom
```

`xargs` is a great tool. Look it up. (link to `til/cli/xargs`)


### Why would you need `after { ENV.delete(key) }`?

Answering this is an exercise for the reader

### What does Rspec's `described_class` mean?

Answering this is an exercise for the reader

