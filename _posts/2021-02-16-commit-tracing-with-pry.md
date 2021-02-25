---
layout: post
title: "Commit Tracing In Pry"
published: true
date: 2021-02-24 06:00:00 -0700
description: "Applying Chelsea Troy's Leveling Up Skill of Commit Tracing"
permalink: /commit-tracing-in-pry
image: ""
---

I'm working through [Leveling Up Skill #6: Commit Tracing](https://chelseatroy.com/2018/07/21/leveling-up-skill-6-commit-tracing/), as applied to the `pry` gem.

## The Backstory

[Iuliu Pop](https://www.iulspop.dev/) and I are working to maximize learning, targeting "top 10% software developer", perhaps scoped down to things like a specific programming language, business domain, etc. 

For now, top 10% software developer.

The question we both think about are "what are the specific and tactical tools one can apply to improving one's skills?"


### What And Why To Trace Commits

Read Chelsea Troy's post: [Leveling Up Skill #6: Commit Tracing](https://chelseatroy.com/2018/07/21/leveling-up-skill-6-commit-tracing/).

### Why To examine the Pry Gem

Pry is a ubiquitous tool in the Ruby/Rails community, seemed like a good place to start.

## The Technique

Open the gem in your editor:

```
$ EDITOR=atom bundle open griddler
Could not find gem 'pry'
```

Hm. I check to see that the gem is installed locally:

```
$ gem list pry

*** LOCAL GEMS ***

pry (0.14.0, 0.13.1)
pry-byebug (3.9.0)
```

Ah, of course, we're calling "bundle open", so it wants to look at our `Gemfile` or `Gemfile.lock`

So, I'm `cd`ing into a directory that has a `Gemfile` and `Gemfile.lock` containing `pry`. 

If you'd like to follow along, I'm using my [intermediate ruby obstacle course](https://github.com/josh-works/intermediate_ruby_obstacle_course), and you can follow along with:

```
git clone git@github.com:josh-works/intermediate_ruby_obstacle_course.git
cd intermediate_ruby_obstacle_course
bundle install
EDITOR=atom bundle open pry
```
Here's what it looked like for me:

![opening pry](/images/commit-tracing-pry.jpg)

You'll see pry open in the specified editor

Success! [^til]

[^til]: Here's my [today-i-learned](https://github.com/josh-works/til/blob/main/ruby/open-specific-gem-in-editor-with-bundler.md) for the above topic. 

...

Arg. Not success, duh. As soon as I spent 3 seconds thinking about it, I realized that of course the code included in the Gemfiles doesn't include version control info. We'll need to change tacts, clone down the actual pry gem (_with_ the `.git` folder included) and try again.

## The Technique (Take 2)

### 1. Create a place for the Pry source code

Make a new directory, clone down the [pry gem](https://github.com/pry/pry)

```
$ mkdir /me/warmup/commit-tracing/
$ cd commit-tracing
$ git clone git@github.com:pry/pry.git
$ cd pry
```

Now we can work through this together!

### 2. Find a promising commit

Chelsea Troy says she looks for:

> A fairly complex code base that exemplifies my topic of study and has clearly named, well-circumscribed commits.

So, I'm going to start [browsing Pry commits](https://github.com/pry/pry/commits/master)

I'm skimming through a handful, I'm going to find 5 "promising" commits before moving to step 3. (I expect that my first few attempts at commit tracing will not be precisely the right size/complexity, so I'm not getting held up on this step)

Here's some interesting commits that I might use for the next step:

- [config: return `nil` on unknown option instead of raising ](https://github.com/pry/pry/commit/5dd061c3406aa84e5cafd489a5c77e550b00d122)
- [pry-backtrace frozen bug ](https://github.com/pry/pry/commit/da81c960272ae0a265f7ded21697d1f09f151ffb)
- [Display all syntax error messages when catching SyntaxException](https://github.com/pry/pry/commit/f6736d526260b2aa9f50b61150a67fcfa2045893)
- [Add Pry::Env](https://github.com/pry/pry/commit/7ce5ca70bb4a1ff447269bdde4cb5d07b8932c8a)
- [Add Pry::Warning](https://github.com/pry/pry/commit/473bc9f2d6a0ebd93c9a09ea3c699c14e01330b0)
- [Push edit contents to history](https://github.com/pry/pry/commit/782a09e057d1e714074d61891a5fba293eb9faca)



## Picking a Commit: `Add Pry::Env`

I decided to start with [Add Pry::Warning](https://github.com/pry/pry/commit/473bc9f2d6a0ebd93c9a09ea3c699c14e01330b0)

First, I'm going to check out the repo to right before the commit that adds `Pry::Warning`

Here's how to find that commit:

![check out the prior commit](/images/2021-02-23 at 9.52 AM-checkout.jpg)

Next, use `git diff <sha-of-the-next-commit>` to see the contents of this pull request, represented inside of your editor:

```
git diff 7ce5ca
```

Here's how I grabbed the commit sha:

![get the sha](/images/2021-02-23 at 9.56 AM-get-current-sha.jpg)

Now, if you do the above `git diff` command, it's comparing the current commit against the future commit, which shows what the current commit is missing. 

Here's the output:

![git diff output](/images/2021-02-23 at 10.00 AM-git-diff-wrong-direction.jpg)

This isn't _exactly_ what I want - I want to see the code as what's added, not what's deleted.

Alternatively, I'll check out the commit that adds the feature:

```
git checkout 7ce5ca
```

And now I'll diff this feature commit _against the prior commit_, which we could either hardcode the commit to diff, or use a shortcut.

Run both of these in your editor:

```shell
git co 7ce5ca # co is aliased to 'check out'
git diff 17bdfd7 # diffs against the prior commit
git diff HEAD~1 # HEAD is "wherever the repo is set right now"
               # ~1 means "one commit earlier", you could 
               # also drop the 1, because if no number is 
               # provided, it assumes you mean 1

git diff HEAD~ # these last two commands are the same. Actually, these are all ways of saying the same thing
```

Whatever method you use, here's what you'll see:

![git diff looking good](/images/2021-02-23 at 10.06 AM-git-diff-good.jpg)

### Write Out All Added Code, Including what file it's in

Now I'm going to copy this code down on paper. I'll time how long this takes me: It's `Time.now` when I start. 

[_music plays while Josh puts pen to paper_]

OK! Finished. It took 9 minutes for me to write out that commit, by hand, on paper:

_TODO: Add photos of paper, they're on my phone, 02/23/21_

### Open the affected files in my editor:

Now, I'm going to diverge a little from Chelsea's path. I'm going to open each changed file in my editor:

```
$ git diff HEAD~1 --name-only # shows the name of modified files
$ git diff HEAD~1 --name-only | xargs atom
```

You'll end up with something like this: 

![open files in atom](/images/2021-02-23 at 10.23 AM-open-in-atom.jpg)

(I could have done `atom .` and used the fuzzy finder to open these individual files up in sequence, but that would have taken longer)

I'm going to run the tests for just the affected spec. In atom, `shift-ctrl-c` copies the _relative_ path for the selected pane to my clipboard, and I can paste that in my terminal, and do `rspec ctrl-v`, or `rspec spec/env_spec.rb`

> josh, that seems like a lot of work for just running a single test file

Yeah, when I skip around a project, running many different test files, especially deeply-tested test files, I use the `shift-ctrl-c` thing _all the dang time_. 

Tests pass!

Now lets reset the repo to the prior commit, and _manually_ rebuild this commit, from paper. 

## Reset repo to prior commit

Boom. Here's what I just did:

![reset stuff](/images/2021-02-23 at 10.28 AM.jpg)


Running just the specs, without the actual code to make it run...

When I add `require pry/env` and:

```ruby
# lib/env.rb
class Pry
  module Env
    
  end
end
```

The tests all pass. 

Siiiiiiiiigh this is annoying. The tests shouldn't pass. Why are they passing???

## Rspec conventions

Time to dig into RSPEC a bit. 

First, what's this `specify` thing? Hashrocket with the explanation:

[RSpec Specify](https://til.hashrocket.com/posts/edefa42db2-rspec-specify)

I wanted to be able to put a pry in that line of code and be able to call `key`, or `described_class[key]` or `Pry::Env[key]`.

I'll have to "deconstruct" the `specify` block to get a pry closer to this line of code.

We'll go from this:

```ruby
context "when ENV contains the passed key" do
  before { ENV[key] = 'val' }
  after { ENV.delete(key) }

  specify { expect(described_class[key]).to eq('val') }
end
```
to this:

```ruby
context "when ENV contains the passed key" do
  before { ENV[key] = 'val' }
  after { ENV.delete(key) }

  it "should equal 'val'" do
    expect(described_class[key]).to eq('val')
  end
end
```

I don't have access to `key` here:

![key](/images/2021-02-24 at 11.02 AM.jpg)

But I do have it now, after refactoring from `specify {}` to `it/do`:

![it works](/images/2021-02-24 at 11.06 AM-pry-better.jpg)

## A little digression on ENV, test 1: `when ENV contains the passed key`

Time to learn a little about your `env`, if you've not already. In Pry (or your terminal session), type `ENV` (it's case sensitive)

You'll get a bunch of results back. When I run `ENV.count` I get 87 results. I've had to search through my `ENV` before to find matching results, and I use a little ruby method like so:

```ruby
ENV.select { |k| k =~ /pry/i }
```

This selects all my `ENV` entries that have the string `pry` in them, in a case-insensitive way. (that's what the trailing `i` specifies.)

I can see that as the code executes, the first spec should pass. It sets `ENV['PRYTESTKEY']` to `val`, and then asserts that... well, that it did this. Cool. On to test 2.

## test 2: `when ENV doesn't contain the passed key`

By the way, when running the tests like so:

```shell
rspec spec/env_spec.rb
```

You can add `:line-number` to the end, and it'll run the spec associated with the `should` block in that line of code. I do this to run tests one-at-a-time:

```shell
rspec spec/env_spec.rb:17
```
So, we're testing ENV behavior when there's no assigned key. 

Instead of `ENV['PRYTESTKEY'] = 'val'` having been run, now we're just calling a bare, non-assigned `env` variable, like `ENV['totallyfake']`

What happens when you call a hash key that doesn't exist? You usually get `nil`, so this test also doesn't really tell us new things:

```ruby
ENV['PRYTESTKEY']
=> nil
```

So this also passes. 

## Test 3: `when ENV contains the passed key but its value is nil`

I converted the `specify` to a `it/do` block, added the pry, and am visually/manually reproducing the assertion:

```ruby
expect(described_class[key]).to be_nil
```

In pry:

```ruby
ENV['PRYTESTKEY'].nil?
=> false
```
Seems like it should fail, but it doesn't. 

Sigh. Here's how `rspec` handles `true`, `false`, `truthy`, `falsey`, and `nil`. This still doesn't adhere to my expectations:

[Truthiness and existentialism (rspec cheatsheet)](https://kapeli.com/cheat_sheets/RSpec_Expectations.docset/Contents/Resources/Documents/index#//dash_ref_Built-in%20Matchers/Entry/Truthiness%20and%20existentialism/0)

Arg. I feel disconent messing with code when the tests don't even fail.

---------------------

AAAAAAH it's because I created the new file in the wrong directory. Once I move `env.rb` to the `lib/pry` directory (or something like that) the tests are failing. Huzzah.

## From the top, `git reset --hard 17bdfd70`

OK, I deleted the lib code, rebuilt it using the tests. No problem, ended up with a close copy to what was in the PR. It didn't take very long. Enjoyed it.

Now to rebuild the whole thing, _including_ the tests.

I ran `git reset --hard 17bdfd70`, to check out the whole repo to right before this feature that I want to add. 

I added a "shell" of the test file to `spec/env_spec.rb`, like so:

```ruby
RSpec.describe Pry::Env do
  describe "#[]" do
    context "when ENV contains the passed key" do
      ENV['testkey'] = 'val'
      it "should equal 'val'" do
        expect(ENV['testkey']).to eq('val')
      end
    end
  end
end
```

and when I was running it, I kept getting `uninitialized constant RSpec` errors. No idea why - I matched what exists in other files, so I did a `bundle exec rspec spec/env_spec.rb`, got the same error. `bundle installed`, re-ran it, and all worked. no idea why.

Now I'm getting `uninitalized constant 'Pry::Env'`, which is reasonable, because... well, I've not added the constant.

So, added:

```ruby
class Pry
  module Env
  end
end
```

and the test passes. Upgraded the test to include the 2nd assertion:

```ruby
RSpec.describe Pry::Env do
  describe "#[]" do
    context "when ENV contains the passed key" do
      ENV['testkey'] = 'val'
      it "should equal 'val'" do
        expect(ENV['testkey']).to eq('val')
      end
    end
    
    context "when ENV does not contain the passed key" do
      it "should be nil" do
        expect(ENV['testkey']).to be_nil
      end
    end
  end
end
```

And now the `ENV` value is persisting between test runs, so I need to clean it up.

In the `describe` I added:

```ruby
RSpec.describe Pry::Env do
  describe "#[]" do
    after { ENV.delete('testkey') } 
    # ^^ these deletes the key I'm creating in various tests
```

Now all the tests pass again. So far so good. The last test case is where the real work happens, I think.

Here's the last test I added:

```ruby
context "when ENV contains the passed key but its value is '' " do
  ENV['testkey'] = ''
  it "should return nil" do
    expect(ENV['testkey']).to be_nil
  end
end
```
and the test output:

```shell
rspec spec/env_spec.rb

Pry::Env
  #[]
    when ENV contains the passed key
      should equal 'val' (FAILED - 1)
    when ENV does not contain the passed key
      should be nil
    when ENV contains the passed key but its value is ''
      should return nil

Failures:

  1) Pry::Env#[] when ENV contains the passed key should equal 'val'
     Failure/Error: expect(ENV['testkey']).to eq('val')

       expected: "val"
            got: ""

       (compared using ==)
     # ./spec/env_spec.rb:9:in `block (4 levels) in <top (required)>'

Finished in 0.01615 seconds (files took 0.3045 seconds to load)
3 examples, 1 failure

Failed examples:

rspec ./spec/env_spec.rb:8 # Pry::Env#[] when ENV contains the passed key should equal 'val'

```

colorized:

![failure](/images/2021-02-24 at 1.18 PM-failed.jpg)

Lets make it pass.



### Notes, further reading

- [Tacit Knowledge is a Real Thing](https://commoncog.com/blog/tacit-knowledge-is-a-real-thing/)
- [How To Open A Specific Gem In A Specific Editor (github.com/josh-works/til)](https://github.com/josh-works/til/blob/main/ruby/open-specific-gem-in-editor-with-bundler.md)
