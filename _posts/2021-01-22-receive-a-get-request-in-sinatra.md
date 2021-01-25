---
layout: post
title:  "Sinatra Basics (Part 1)"
published: false
description: ""
date:  2020-01-31 06:00:00 -0700
categories: [basics]
tags: [sinatra, ruby]
permalink: sinatra-basics
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

### Step 5: Lets figure out what matters in the `request`:

Sticking a `pry` in the `get "/"` here's my ENV:

```ruby
=> {"SERVER_SOFTWARE"=>"thin 1.7.2 codename Bachmanity",
 "SERVER_NAME"=>"localhost",
 "rack.input"=>#<StringIO:0x00007fe64c2b6530>,
 "rack.version"=>[1, 0],
 "rack.errors"=>#<IO:<STDERR>>,
 "rack.multithread"=>true,
 "rack.multiprocess"=>false,
 "rack.run_once"=>false,
 "REQUEST_METHOD"=>"GET",
 "REQUEST_PATH"=>"/",
 "PATH_INFO"=>"/",
 "QUERY_STRING"=>"dfd=sdfdf",
 "REQUEST_URI"=>"/?dfd=sdfdf",
 "HTTP_VERSION"=>"HTTP/1.1",
 "HTTP_USER_AGENT"=>"PostmanRuntime/7.26.8",
 "HTTP_ACCEPT"=>"*/*",
 "HTTP_CACHE_CONTROL"=>"no-cache",
 "HTTP_POSTMAN_TOKEN"=>"aa6e3d77-8491-4c29-85db-6b120a81d0b9",
 "HTTP_HOST"=>"localhost:4567",
 "HTTP_ACCEPT_ENCODING"=>"gzip, deflate, br",
 "HTTP_CONNECTION"=>"keep-alive",
 "HTTP_COOKIE"=>"fd827a2c5655094bcce3748d6ee6d3e4=ImRhMDY1YjdjYjMwNGNjNWUxNzFkNDhjOGQ0YzA0OTIwIg%3D%3D--98c228cb35af1a269ee894c22540b81848e2ed09",
 "GATEWAY_INTERFACE"=>"CGI/1.2",
 "SERVER_PORT"=>"4567",
 "SERVER_PROTOCOL"=>"HTTP/1.1",
 "rack.url_scheme"=>"http",
 "SCRIPT_NAME"=>"",
 "REMOTE_ADDR"=>"::1",
 "async.callback"=>
  #<Method: #<Thin::Connection:0x00007fe64c2b67b0 @signature=9, @request=#<Thin::Request:0x00007fe64c2b65d0 @parser=#<Thin::HttpParser:0x00007fe64c2b65a8>, @data=nil, @nparsed=374, @body=#<StringIO:0x00007fe64c2b6530>, @env={...}>, @response=#<Thin::Response:0x00007fe64c2b64e0 @headers=#<Thin::Headers:0x00007fe64c2b6468 @sent={}, @out=[]>, @status=200, @persistent=false, @skip_body=false>, @backend=#<Thin::Backends::TcpServer:0x00007fe64c0de140 @host="::1", @port=4567, @connections={70313548559320=>#<Thin::Connection:0x00007fe64c2b67b0 ...>}, @timeout=30, @persistent_connection_count=1, @maximum_connections=1024, @maximum_persistent_connections=100, @no_epoll=false, @ssl=nil, @threaded=true, @started_reactor=true, @server=#<Thin::Server:0x00007fe64c0ded98 @app=Sinatra::Application, @tag=nil, @backend=#<Thin::Backends::TcpServer:0x00007fe64c0de140 ...>, @setup_signals=true, @signal_queue=[], @signal_timer=#<EventMachine::PeriodicTimer:0x00007fe64b07e570 @interval=1, @code=#<Proc:0x00007fe64b07e5c0@/Users/joshthompson/.rvm/gems/ruby-2.5.8/gems/thin-1.7.2/lib/thin/server.rb:244>, @cancelled=false, @work=#<Method: EventMachine::PeriodicTimer#fire>>>, @stopping=false, @signature=2, @running=true>, @app=Sinatra::Application, @threaded=true, @can_persist=true, @idle=false>.post_process>,
 "async.close"=>#<EventMachine::DefaultDeferrable:0x00007fe64c2ceae0>,
 "sinatra.commonlogger"=>true,
 "rack.logger"=>
  #<Logger:0x00007fe64c2ce9c8
   @default_formatter=#<Logger::Formatter:0x00007fe64c2ce8b0 @datetime_format=nil>,
   @formatter=nil,
   @level=1,
   @logdev=#<Logger::LogDevice:0x00007fe64c2ce860 @dev=#<IO:<STDERR>>, @filename=nil, @mon_count=0, @mon_mutex=#<Thread::Mutex:0x00007fe64c2ce7c0>, @mon_owner=nil, @shift_age=nil, @shift_period_suffix=nil, @shift_size=nil>,
   @progname=nil>,
 "rack.request.query_string"=>"dfd=sdfdf",
 "rack.request.query_hash"=>{"dfd"=>"sdfdf"},
 "sinatra.route"=>"GET /"}
```

Lots to explore, but using Pry is kinda annoying.


## Step X: I decided to spend a minute on the html/css

Using [new.css](https://newcss.net/), and a bare-bones index.html, check out:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baby Yoda</title>
    <link rel="stylesheet" href="https://fonts.xz.style/serve/inter.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@exampledev/new.css@1.1.2/new.min.css">

</head>
<body>
  <header>
    Its a Starter!
  </header>
    <h1>Hello, world. I'm a baby sinatra application</h1>
    
    <form>
     <label for="fname">First name:</label><br>
     <input type="text" id="fname" name="fname"><br>
     <label for="lname">Last name:</label><br>
     <input type="text" id="lname" name="lname">
    </form> 
    
    <details>
      <summary>Click me!</summary>
      <p>Lorem ipsum dolor sit amet.</p>
    </details>    
</body>
</html>
```


### Resources

- [Getting Started (Sinatra)](http://sinatrarb.com/intro.html)
- [How to get Sinatra to auto-reload the file after each change?](https://stackoverflow.com/questions/1247125/how-to-get-sinatra-to-auto-reload-the-file-after-each-change)
- [How do you set all of your Sinatra responses to be JSON? (StackOverflow)](https://stackoverflow.com/questions/27644016/how-do-you-set-all-of-your-sinatra-responses-to-be-json)