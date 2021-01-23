---
layout: post
title:  "Guiding Principles"
published: false
description: ""
date:  2020-01-31 06:00:00 -0700
categories: []
tags: []
permalink: simple-email-in-rails-localhost-mailcatcher
image: /images/title_image.jpg
---

I want to build a Sinatra app that I can use to teach others about APIs, HTTP verbs, networking, and more. 

It's 2:45p, 01/22/21. 

Taking notes as I go, because my primary "value add" in the world is learning things (albeit slowly) and helping _others_ learn whatever I learned _very very quickly_.

Since me (1 person) learns slowly, but I can teach that same thing to 50 people quickly, I don't have to feel bad when I broadcast to the world that I'm a slow learner. ;)

Lets start up a Sinatra app, from scratch. I'll be taking notes how I usually do:

# Minimum steps to get a running Sinatra app:

MVP sinatra setup:

```shell
$ mkdir sinatra-starter
$ cd sinatra-starter
$ touch app.rb
```

Inside of `app.rb` add:

```ruby
require 'sinatra'

get '/' do
  "hi"
end
```

Install `sinatra` if you have not: `gem install sinatra`

Start the Sinatra server with: `ruby app.rb` (Basically, tell ruby to run the file with the `require` statement, and the `get '/'` do) block...

Open up [localhost:4567](localhost:4567) and you should see:

![sinatra running](/images/sinatra-running.jpg)

Now, I want to receive and serve JSON, so I might as well start returning JSON. 

How to do...

Oh, I just finished the first commit here: [https://github.com/josh-works/sinatra-starter/commits/main](https://github.com/josh-works/sinatra-starter/commits/main)

-----------------------------

## Step 2

The app doesn't recognize changes, so you either need to stop/restart the app to catch new code, or use [Sinatra::Reloader](http://sinatrarb.com/contrib/reloader)

To stop the app, if you still have it running in the terminal, great, `ctrl-c`. If you closed the pane or cannot find the running process, find the process ID with 

```
$ lsof -i :4567
```

or 

```
ps aux | grep ruby
```

then kill the PID:

```
kill <pid>
```

and re-run with `ruby app.rb`

ooor... use `rerun` (an app), easier than what Sinatra's docs recommend:

```
$ gem install rerun
$ rerun app.rb
```

super clean.

## Step 3: Lets get JSON out of this thing

I'm surprised to see that it looks like Sinatra doesn't have any built-in JSON support.

...

OK. We'll use the `json` gem, though this seems a little crusty. Surely not the `sinatra` way?

Here's the gem: [https://rubygems.org/gems/json/versions/1.8.3](https://rubygems.org/gems/json/versions/1.8.3) and of course check out the github page, though I didn't get much from it: [https://github.com/flori/json/](https://github.com/flori/json/)

```diff
commit 29a33fd7dbb2c231d67cfe4ede5c6f11f6d1b2ea (HEAD -> main)
Author: Josh Thompson <thompsonjoshd@gmail.com>
Date:   Fri Jan 22 15:33:40 2021 -0700

    now serving json

diff --git a/app.rb b/app.rb
index 7736302..d7f7f63 100644
--- a/app.rb
+++ b/app.rb
@@ -1,5 +1,6 @@
 require 'sinatra'
+require 'json'

 get '/' do
-  "hi"
+  JSON.generate(foo: "hi hello")
 end
```

### Step 4: Lets read AND return JSON

Lets say I want to spiff this up just a tiny little level - instead of rendering a static result, lets render something about the request, just so folks can see something unique to them.

you could swap to `JSON.generate(env)` but the response is a bit wordy. Lets select what we want to get out.

Note: if you stick a pry in the `get`, like so:

```ruby
require 'sinatra'
require 'json'

get '/' do
  require "pry"; binding.pry
  env.to_json
end
```

and try to visit this in `postman` OR your browser, note that these are different:

```
http://localhost:4567
http://localhost:4567/
```


### Resources

- [Getting Started (Sinatra)](http://sinatrarb.com/intro.html)
- [How to get Sinatra to auto-reload the file after each change?](https://stackoverflow.com/questions/1247125/how-to-get-sinatra-to-auto-reload-the-file-after-each-change)
- [How do you set all of your Sinatra responses to be JSON? (StackOverflow)](https://stackoverflow.com/questions/27644016/how-do-you-set-all-of-your-sinatra-responses-to-be-json)